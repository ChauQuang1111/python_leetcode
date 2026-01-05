# #  Maximum Matrix Sum(05/01/2026)
# Dưới đây là **giải thích thuật toán rõ ràng, đúng bản chất bài 1975 – Maximum Matrix Sum**, sau đó mình **thêm chú thích chi tiết trực tiếp vào code của bạn** 👇

# ---

# ## 1️⃣ Ý tưởng & thuật toán (Algorithm Explanation)

# ### 🔹 Quan sát quan trọng

# * Mỗi phép biến đổi **đổi dấu 2 ô kề nhau**
# * → Số lượng phần tử âm **chỉ thay đổi theo bội số của 2**
# * → **Tính chẵn / lẻ của số phần tử âm là bất biến**

# ---

# ### 🔹 Chiến lược tối ưu

# 1. **Luôn muốn mọi số đều dương** → tổng lớn nhất
#    ⇒ cộng **giá trị tuyệt đối** của mọi phần tử

# 2. **Đếm số phần tử âm (`num_neg`)**

#    * Nếu **chẵn** → có thể đổi dấu để tất cả thành dương
#    * Nếu **lẻ** → buộc phải để lại **1 số âm**

# 3. Nếu buộc phải để lại 1 số âm
#    → chọn số có **giá trị tuyệt đối nhỏ nhất** (`least_abs`)
#    → để giảm thiệt hại nhỏ nhất

# ---

# ### 🔹 Công thức kết quả

# * `num_neg` **chẵn**
#   👉 `answer = sum(|a[i][j]|)`
# * `num_neg` **lẻ**
#   👉 `answer = sum(|a[i][j]|) − 2 × min(|a[i][j]|)`

# ---

# ### 🔹 Độ phức tạp

# * **Time:** `O(n²)`
# * **Space:** `O(1)`

# ---

# ## 2️⃣ Code của bạn + chú thích chi tiết

# ```python
from typing import List
class Solution:
    def maxMatrixSum(self, a: List[List[int]]) -> int:
        # pos_sum: tổng các giá trị tuyệt đối của toàn bộ ma trận
        pos_sum = 0
        
        # num_neg: đếm số phần tử âm trong ma trận
        num_neg = 0
        
        # least_abs: giá trị tuyệt đối nhỏ nhất trong ma trận
        least_abs = float('inf')

        # Duyệt từng phần tử trong ma trận
        for row in a:
            for x in row:
                # Nếu x là số âm
                if x < 0:
                    num_neg += 1   # tăng số lượng số âm
                    x = -x         # lấy trị tuyệt đối
                
                # Cập nhật giá trị tuyệt đối nhỏ nhất
                if x < least_abs:
                    least_abs = x
                
                # Cộng trị tuyệt đối vào tổng
                pos_sum += x
        
        # Nếu số phần tử âm là chẵn
        # => có thể đổi dấu để tất cả đều dương
        if num_neg % 2 == 0:
            return pos_sum
        else:
            # Nếu số phần tử âm là lẻ
            # => bắt buộc phải có 1 số âm
            # => trừ đi 2 * least_abs để giảm tổng ít nhất
            return pos_sum - least_abs * 2


## 3️⃣ Ví dụ minh họa nhanh

# ```
# a = [[1, -2],
#      [-3, -4]]
# ```

# * |1| + |2| + |3| + |4| = **10**
# * num_neg = 3 (lẻ)
# * least_abs = 1

# ➡️ `10 − 2 × 1 = 8`

# ---

# ## 4️⃣ Ghi nhớ khi đi phỏng vấn / thi LeetCode

# > ❝ Không cần mô phỏng thao tác đổi dấu
# > Chỉ cần quan tâm **tính chẵn/lẻ của số âm** ❞

# ---

# Nếu bạn muốn mình:

# * ✍️ Viết **giải thích ngắn gọn 3–4 dòng** để nộp bài
# * 🧠 Chứng minh vì sao **không thể loại bỏ hết số âm khi lẻ**
# * ⚡ Viết phiên bản **C++ / Java**

# 👉 cứ nói, mình hỗ trợ tiếp đúng gu của bạn 👍

# # ---

# # ### 1️⃣ Mô tả bài toán

# # Bạn được cho **một ma trận vuông** kích thước `n x n`, trong đó mỗi phần tử là **số nguyên** (có thể âm, dương hoặc 0).

# # Bạn được phép thực hiện **vô số lần** thao tác sau:

# # 👉 **Chọn hai ô kề nhau (chung cạnh)** và **đổi dấu cả hai số**

# # * Số dương → âm
# # * Số âm → dương

# # Mục tiêu:
# # ➡️ **Tính tổng lớn nhất có thể của tất cả các phần tử trong ma trận sau khi thực hiện các thao tác hợp lệ.**

# # ---

# ### 2️⃣ Ý nghĩa quan trọng của thao tác

# * Mỗi lần thao tác **đổi dấu 2 số cùng lúc**
# * Tổng số phần tử âm trong ma trận **chỉ thay đổi chẵn lần**
#   → **Tính chẵn/lẻ của số lượng số âm là yếu tố quyết định**

# ---

# ### 3️⃣ Tư duy chính để giải bài này

# #### 🔹 Bước 1: Lấy trị tuyệt đối

# Vì ta có thể đổi dấu, nên **giá trị lớn nhất mỗi ô có thể đạt được là trị tuyệt đối của nó**

# ➡️ Tính:

# ```
# sum = tổng |a[i][j]|
# ```

# ---

# #### 🔹 Bước 2: Đếm số phần tử âm

# * Gọi `negCount` = số phần tử âm ban đầu
# * Tìm `minAbs` = **giá trị tuyệt đối nhỏ nhất** trong ma trận

# ---

# ### 4️⃣ Hai trường hợp quan trọng

# #### ✅ Trường hợp 1: `negCount` là **số chẵn**

# 👉 Ta có thể biến **tất cả số âm thành dương**

# ➡️ **Kết quả = sum**

# ---

# #### ❌ Trường hợp 2: `negCount` là **số lẻ**

# 👉 Luôn phải còn **ít nhất 1 số âm**
# 👉 Ta nên để số âm đó có **giá trị tuyệt đối nhỏ nhất** để thiệt hại ít nhất

# ➡️ **Kết quả = sum − 2 × minAbs**

# (vì thay vì +minAbs ta bị −minAbs → mất 2×minAbs)

# ---

# ### 5️⃣ Ví dụ minh họa

# #### Ví dụ:

# ```
# matrix = [
#   [ 1, -2],
#   [-3,  4]
# ]
# ```

# * |1| + |−2| + |−3| + |4| = **10**
# * Số âm = 2 (chẵn)

# ➡️ **Đáp án = 10**

# ---

# #### Ví dụ khác:

# ```
# matrix = [
#   [ 1, -2],
#   [-3, -4]
# ]
# ```

# * Tổng trị tuyệt đối = 10
# * Số âm = 3 (lẻ)
# * minAbs = 1

# ➡️ **Đáp án = 10 − 2×1 = 8**

# ---

# ### 6️⃣ Tóm tắt ngắn gọn (rất hay thi)

# * Luôn cộng **trị tuyệt đối**
# * Nếu số âm **chẵn** → lấy hết
# * Nếu số âm **lẻ** → trừ `2 × minAbs`

# ---

# Nếu bạn muốn:

# * ✔️ Giải thích **vì sao thao tác đổi dấu hoạt động như vậy**
# * ✔️ Code Java / C++ / Python
# * ✔️ Phân tích test khó

# 👉 cứ nói, mình giải tiếp đúng kiểu bạn hay học 👍
