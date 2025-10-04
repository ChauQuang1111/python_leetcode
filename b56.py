# 11. Container With Most Water (04/10/2025)
# Tốt lắm 👍 Đây là phiên bản **Python code có chú thích chi tiết từng dòng** cho bài **11. Container With Most Water**, kèm **giải thích thuật toán** ở cuối 👇

# ---

# ### 🐍 **Code có chú thích chi tiết**

# ```python
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = i = 0                 # ans là diện tích lớn nhất; i là con trỏ bên trái
        j = len(height) - 1         # j là con trỏ bên phải (cuối mảng)

        while j > i:                # lặp khi 2 con trỏ chưa gặp nhau
            # Tính diện tích nước giữa 2 cột i và j
            temp = (j - i) * min(height[i], height[j])

            # Nếu diện tích hiện tại lớn hơn max -> cập nhật
            if temp > ans:
                ans = temp
            else:
                # Nếu cột bên trái cao hơn cột bên phải
                if height[i] > height[j]:
                    temp = j        # Lưu lại vị trí cột phải hiện tại
                    # Dịch con trỏ phải sang trái để tìm cột cao hơn
                    while j != i:
                        j -= 1
                        # Nếu gặp cột cao hơn cột cũ -> dừng
                        if height[j] > height[temp]:
                            break
                else:
                    temp = i        # Lưu lại vị trí cột trái hiện tại
                    # Dịch con trỏ trái sang phải để tìm cột cao hơn
                    while j != i:
                        i += 1
                        # Nếu gặp cột cao hơn cột cũ -> dừng
                        if height[i] > height[temp]:
                            break

        return ans                  # Trả về diện tích lớn nhất tìm được

# ### 🧠 **Giải thích thuật toán**

# Thuật toán này là **biến thể của Two Pointer Optimization**, ý tưởng như sau:

# 1. **Hai con trỏ `i` (trái) và `j` (phải):**

#    * Ban đầu, đứng ở hai đầu của mảng `height`.
#    * Diện tích nước giữa hai cột = `(khoảng cách) × (chiều cao thấp hơn)`
#      👉 `area = (j - i) * min(height[i], height[j])`

# 2. **Cập nhật kết quả:**

#    * Giữ lại diện tích lớn nhất `ans`.

# 3. **Dịch con trỏ thấp hơn:**

#    * Nếu `height[i] < height[j]`, ta di chuyển `i` sang phải để tìm cột cao hơn → **hy vọng tăng chiều cao**.
#    * Ngược lại, nếu `height[j] < height[i]`, ta di chuyển `j` sang trái.
#    * Trong code này, nó **dịch con trỏ nhiều bước liền một lúc** (bỏ qua các cột thấp hơn cột cũ để tiết kiệm thời gian).

# 4. **Dừng khi hai con trỏ gặp nhau.**

# ---

# ### 🧩 **Ví dụ minh họa**

# ```
# height = [1,8,6,2,5,4,8,3,7]
# ```

# * Bắt đầu: i=0 (1), j=8 (7)
#   → min=1, width=8 → area=8
# * Dịch i vì 1<7
#   → i=1 (8), j=8 (7) → min=7, width=7 → area=49 ✅
# * Sau đó dịch j sang trái khi gặp cột thấp hơn...
#   → kết quả cuối cùng: **49**

# ---

# 👉 **Tóm gọn:**

# * Dùng 2 con trỏ để tìm diện tích tối đa.
# * Luôn dịch con trỏ ở phía có cột thấp hơn.
# * Phiên bản code của bạn là bản **tối ưu hơn**, vì nó bỏ qua các cột không có khả năng tạo diện tích lớn hơn.

# ---

# Bạn có muốn mình vẽ **sơ đồ minh họa trực quan từng bước di chuyển của con trỏ (i, j)** không?
# Rất dễ hiểu khi nhìn bằng hình.

# Tất nhiên 👍
# Đề bài **“11. Container With Most Water”** (LeetCode 11) là một bài **kinh điển về hai con trỏ (two pointers)**.
# Giải thích chi tiết như sau 👇

# ---

# ### 🧩 **Đề bài (phiên bản dễ hiểu)**

# Bạn được cho một **mảng số nguyên `height[]`**, trong đó mỗi phần tử biểu thị **chiều cao của một cột**.
# Hai cột này và trục hoành (x-axis) tạo thành **một cái “container” chứa nước**.

# Mục tiêu là:
# 👉 **Chọn hai cột sao cho container giữa chúng chứa được nhiều nước nhất.**

# ---

# ### 📊 **Ví dụ**

# Giả sử:

# ```python
# height = [1,8,6,2,5,4,8,3,7]
# ```

# Nếu ta chọn:

# * cột thứ 2 (cao 8)
# * và cột thứ 9 (cao 7)

# → chiều rộng giữa hai cột là `9 - 2 = 7`
# → chiều cao bị giới hạn bởi cột thấp hơn: `min(8,7) = 7`

# => **Diện tích nước chứa được = 7 * 7 = 49**

# Đây cũng là **kết quả lớn nhất** trong ví dụ này.

# ---

# ### 📐 **Công thức tính diện tích nước giữa hai cột**

# Nếu chọn hai cột ở vị trí `i` và `j` (với `i < j`):

# [
# \text{Area} = (j - i) \times \min(height[i], height[j])
# ]

# ---

# ### ⚙️ **Tư duy thuật toán (Two pointers)**

# 1. Đặt hai con trỏ:

#    * `left = 0` (đầu mảng)
#    * `right = n - 1` (cuối mảng)

# 2. Tính diện tích:

#    ```java
#    area = (right - left) * min(height[left], height[right])
#    ```

#    Cập nhật `maxArea` nếu lớn hơn.

# 3. **Di chuyển con trỏ thấp hơn**:

#    * Nếu `height[left] < height[right]`, tăng `left++`
#    * Ngược lại, giảm `right--`

# ➡️ Vì chỉ có việc **di chuyển cột thấp hơn mới có khả năng tăng diện tích** (chiều cao giới hạn sẽ tăng).

# 4. Lặp đến khi `left >= right`.

# ---

# ### 💡 **Ví dụ minh họa ngắn**

# | left | right | height[left] | height[right] | width | minHeight | area | max    |
# | ---- | ----- | ------------ | ------------- | ----- | --------- | ---- | ------ |
# | 0    | 8     | 1            | 7             | 8     | 1         | 8    | 8      |
# | 1    | 8     | 8            | 7             | 7     | 7         | 49   | **49** |
# | ...  | ...   | ...          | ...           | ...   | ...       | ...  | ...    |

# Kết quả cuối cùng: **49**

# ---

# ### 🧠 **Độ phức tạp**

# * **Thời gian:** O(n)
# * **Bộ nhớ:** O(1)

# ---

# Bạn có muốn mình viết luôn **code Java** cho bài này kèm **chú thích từng dòng** không?
