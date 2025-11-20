# 757. Set Intersection Size At Least Two
# Dưới đây là **giải thích đề bài LeetCode 757 – Set Intersection Size At Least Two** một cách **dễ hiểu và chi tiết**.
# Dưới đây là **giải thích thuật toán** + **code có chú thích đầy đủ** cho lời giải bạn đưa ra.

# ---

# # 🧠 **Giải thích thuật toán**

# Ta muốn chọn **ít nhất 2 số** trong mỗi interval. Thuật toán dùng greedy:

# 1. **Sort intervals theo điểm kết thúc tăng dần (b)**
#    → Greedy kinh điển: đặt điểm càng về cuối càng dễ “ăn” được nhiều segment.

# 2. Duy trì hai điểm:

#    * `prev1`: điểm nhỏ hơn
#    * `prev2`: điểm lớn hơn
#      Đây là **2 điểm cuối cùng** ta đã chọn sao cho thỏa mãn tất cả các interval trước đó.

# 3. Xét từng interval `cur = [L, R]`:

# ---

# ## 🎯 **TH1: Không giao với 1 trong 2 điểm → Không đủ 2 điểm**

# Nếu:

# ```
# prev2 < L
# ```

# ⇒ Cả hai điểm hiện tại (`prev1`, `prev2`) đều nằm ngoài đoạn mới.

# 👉 Ta phải **thêm 2 điểm mới**:
# Chọn hai điểm gần R nhất:

# ```
# prev1 = R - 1
# prev2 = R
# ```

# Vì chọn điểm càng lớn càng “ăn” được nhiều đoạn sau.

# ---

# ## 🎯 **TH2: Chỉ có 1 điểm nằm trong đoạn**

# Nếu:

# ```
# prev1 < L ≤ prev2
# ```

# ⇒ `prev2` nằm trong interval, nhưng `prev1` không nằm trong.

# 👉 Ta cần thêm **1 điểm**, ưu tiên đặt ở điểm cuối của đoạn để có lợi nhất.

# * Nếu `R == prev2` → prev2 đã là điểm cuối → ta chọn `prev1 = R - 1`
# * Ngược lại → chọn `prev1 = R`

# Sau đó sắp lại prev1, prev2 để prev1 luôn nhỏ hơn prev2.

# ---

# ## 🎯 **TH3: Cả hai điểm đã nằm trong đoạn**

# Không cần làm gì.

# ---

# # 🧮 **Độ phức tạp**

# * Sắp xếp: **O(n log n)**
# * Duyệt 1 lần: **O(n)**
#   → Tổng: **O(n log n)**

# ---

# # ✅ **Code có chú thích đầy đủ**

# ```python
from typing import List
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        # Sắp xếp intervals theo điểm kết thúc tăng dần
        intervals.sort(key=lambda x: x[1])

        # Chọn hai điểm cho interval đầu tiên:
        # prev1 là điểm nhỏ hơn, prev2 là điểm lớn hơn
        prev1 = intervals[0][1] - 1
        prev2 = intervals[0][1]
        count = 2  # Đã chọn 2 điểm

        # Duyệt các interval tiếp theo
        for i in range(1, n):
            L, R = intervals[i]

            # CASE 1: Không có điểm nào nằm trong đoạn này → cần chọn 2 điểm mới
            if prev2 < L:
                # Chọn 2 điểm gần R nhất (R-1 và R)
                prev1 = R - 1
                prev2 = R
                count += 2

            # CASE 2: Chỉ có 1 điểm nằm trong đoạn → cần chọn thêm 1 điểm
            elif prev1 < L:
                # prev2 ăn được khoảng, prev1 không ăn được
                # Ta phải chọn 1 điểm mới trong đoạn này

                if R == prev2:
                    # Nếu prev2 chính là điểm cuối, ta đành lấy R-1
                    prev1 = R - 1
                else:
                    # Nếu prev2 chưa phải điểm cuối, ta lấy R
                    prev1 = R

                # Đảm bảo prev1 < prev2
                prev1, prev2 = min(prev1, prev2), max(prev1, prev2)

                count += 1

            # CASE 3: prev1 và prev2 đều đã nằm trong interval → không cần làm gì

        return count


# # 🎉 Nếu bạn muốn, mình có thể viết thêm:

# ✔ Phiên bản Java
# ✔ Thêm hàm `main()` + chú thích
# ✔ Giải thích bằng hình minh họa từng bước

# Chỉ cần nói “viết Java” hoặc “giải thích bằng hình”.

# ---

# # 📝 **📌 Đề bài nói gì?**

# Bạn được cho một danh sách các **interval** (đoạn), mỗi đoạn có dạng:

# ```
# [a, b]
# ```

# Bạn cần chọn ra **một tập hợp các số nguyên** sao cho:

# 👉 **Mỗi đoạn phải giao với tập hợp ít nhất 2 phần tử.**
# Tức là với mỗi đoạn `[a, b]`, trong tập bạn chọn phải có **ít nhất 2 số nằm trong khoảng từ a đến b** (bao gồm cả a và b).

# 🎯 **Mục tiêu:**
# Chọn **ít nhất bao nhiêu số** để đảm bảo **tất cả các khoảng đều chứa ≥ 2 số từ tập bạn chọn**.

# ---

# # 📌 Ví dụ

# ## Ví dụ 1:

# Input:

# ```
# intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
# ```

# Output:

# ```
# 3
# ```

# Giải thích:
# Bạn có thể chọn tập `{2, 3, 5}`:

# * `[1, 3]` chứa 2 và 3 → đủ
# * `[1, 4]` chứa 2 và 3 → đủ
# * `[2, 5]` chứa 2, 3, 5 → đủ
# * `[3, 5]` chứa 3 và 5 → đủ

# Tập có **3 số**, là tối thiểu.

# ---

# # 📌 Hiểu đơn giản hơn

# Bạn có các đoạn, và bạn cần “bắn” các điểm sao cho **mỗi đoạn bị bắn trúng ít nhất 2 viên đạn**.

# Đặt ít đạn nhất có thể.

# ---

# # 🧠 Ý tưởng giải greedy (tham lam)

# 1. **Sort (sắp xếp)** các đoạn theo:

#    * **Tăng dần theo điểm kết thúc b**
#    * Nếu bằng nhau thì giảm dần điểm bắt đầu a

# 2. Duy trì **hai điểm lớn nhất** mà bạn đã chọn cho vùng giao.

# 3. Với mỗi đoạn:

#    * Nếu đoạn đã chứa đủ 2 điểm → bỏ qua
#    * Nếu chứa 1 điểm → chọn thêm 1 điểm (b)
#    * Nếu chứa 0 điểm → chọn 2 điểm (b-1, b)

# 4. Mỗi lần luôn ưu tiên **chọn điểm lớn nhất có thể** (điểm cuối của đoạn), để tăng khả năng “khớp” với các đoạn sau.

# Đây là greedy kinh điển cho bài toán “đảm bảo intersection size ≥ 2”.

# ---

# # 📌 Tại sao phải sắp xếp theo điểm kết thúc b?

# Vì khi ta đặt một số ở gần **b (điểm kết thúc)**, nó có khả năng nằm trong **nhiều đoạn nhất**, giúp giảm số lượng số phải đặt.

# ---

# # 📌 Độ khó?

# **Hard** (LeetCode đánh giá Hard), nhưng ý tưởng greedy lại rất đẹp.

# ---

# # 📌 Nếu bạn muốn mình viết code Java + chú thích chi tiết, mình có thể viết ngay.
