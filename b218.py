# Bài **Largest Submatrix With Rearrangements** yêu cầu hiểu như sau:

# Thuật toán của bạn giải bài **Largest Submatrix With Rearrangements** bằng ý tưởng:

# * Mỗi cột lưu **chiều cao liên tiếp của số 1** (histogram).
# * Với mỗi hàng, ta **có quyền rearrange cột**, nên ta **sort chiều cao giảm dần**.
# * Sau đó tính diện tích với công thức:

# ```
# area = height × width
# ```

# trong đó:

# ```
# width = số cột đang dùng = j + 1
# ```

# ---

# # Code có chú thích chi tiết

# ```python
class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        # nếu matrix rỗng thì không có submatrix
        if not matrix: 
            return 0
        
        # m = số hàng, n = số cột
        m, n = len(matrix), len(matrix[0])
        
        # heights[j] = chiều cao của cột j (số lượng 1 liên tiếp từ trên xuống)
        heights = [0] * n
        
        # lưu diện tích lớn nhất
        max_area = 0

        # duyệt từng hàng
        for row in matrix:

            # BƯỚC 1: cập nhật histogram heights
            for j in range(n):
                # nếu ô hiện tại là 1 → tăng chiều cao
                # nếu là 0 → reset về 0
                heights[j] = heights[j] + 1 if row[j] else 0

            # BƯỚC 2: vì được phép rearrange column
            # nên ta sort heights giảm dần
            sorted_heights = sorted(heights, reverse=True)

            # BƯỚC 3: thử tất cả width có thể
            for j in range(n):
                # width = j + 1 (đang dùng j+1 cột)
                # height = sorted_heights[j] (chiều cao nhỏ nhất trong các cột đó)
                area = sorted_heights[j] * (j + 1)

                # cập nhật diện tích lớn nhất
                max_area = max(max_area, area)

        return max_area
# ```

# ---

# # Ví dụ chạy từng bước

# Matrix:

# ```
# [
#  [0,0,1],
#  [1,1,1],
#  [1,0,1]
# ]
# ```

# ### Row 1

# heights:

# ```
# [0,0,1]
# ```

# sort:

# ```
# [1,0,0]
# ```

# area:

# ```
# 1×1 = 1
# ```

# ---

### Row 2

# update heights:

# ```
# [1,1,2]
# ```

# sort:

# ```
# [2,1,1]
# ```

# area:

# ```
# 2×1 = 2
# 1×2 = 2
# 1×3 = 3
# ```

# max = 3

# ---

# ### Row 3

# update heights:

# ```
# [2,0,3]
# ```

# sort:

# ```
# [3,2,0]
# ```

# area:

# ```
# 3×1 = 3
# 2×2 = 4
# 0×3 = 0
# ```

# max = **4**

# ---

# # Độ phức tạp

# Time:

# ```
# O(m * n log n)
# ```

# * m hàng
# * mỗi hàng sort n phần tử

# Space:

# ```
# O(n)
# ```

# ---

# 💡 Nếu bạn muốn, tôi có thể giải thích thêm **intuition rất quan trọng của bài này**:

# > **Tại sao chỉ cần sort heights là đủ để mô phỏng rearranging columns?**

# Đây chính là **trick khiến nhiều người không nghĩ ra bài 1727.**



# ---

# ## 1. Đầu vào

# Bạn có một **ma trận nhị phân** `matrix` kích thước `m x n` gồm các giá trị **0 và 1**.

# Ví dụ:

# ```
# matrix =
# [
#  [0,0,1],
#  [1,1,1],
#  [1,0,1]
# ]
# ```

# ---

# ## 2. Phép biến đổi được phép

# Bạn **được phép hoán đổi vị trí các cột trong mỗi hàng**.

# Quan trọng:

# * **Chỉ đổi cột trong cùng một hàng**
# * Không được đổi hàng
# * Mỗi hàng có thể sắp xếp cột theo thứ tự khác nhau

# Ví dụ:

# ```
# [1,0,1]  → có thể đổi thành →  [1,1,0]
# ```

# ---

# ## 3. Mục tiêu

# Sau khi sắp xếp lại các cột của từng hàng, bạn phải tìm:

# **Diện tích lớn nhất của một submatrix chỉ chứa toàn số 1.**

# Diện tích =

# ```
# height × width
# ```

# ---

# ## 4. Ví dụ minh họa

# ### Input

# ```
# [
#  [0,0,1],
#  [1,1,1],
#  [1,0,1]
# ]
# ```

# ### Sau khi rearrange cột tốt nhất

# Ta có thể biến thành:

# ```
# [
#  [1,0,0],
#  [1,1,1],
#  [1,1,0]
# ]
# ```

# Bây giờ ta thấy submatrix toàn 1:

# ```
# 1 1
# 1 1
# ```

# Diện tích:

# ```
# 2 × 2 = 4
# ```

# Output:

# ```
# 4
# ```

# ---

# ## 5. Ý tưởng trực quan

# Thực chất bài toán là:

# 1. Xem mỗi cột như **chiều cao của histogram của số 1 liên tiếp**.
# 2. Với mỗi hàng:

#    * tính **height của 1 liên tiếp từ trên xuống**
# 3. **sort các height giảm dần** (tương đương với việc rearrange column)
# 4. tính diện tích:

# ```
# height[i] × (i + 1)
# ```

# vì width = số cột đang dùng.

# ---

# ## 6. Ví dụ height

# Matrix:

# ```
# [
#  [0,0,1],
#  [1,1,1],
#  [1,0,1]
# ]
# ```

# Chuyển thành **height matrix**:

# ```
# [
#  [0,0,1]
#  [1,1,2]
#  [2,0,3]
# ]
# ```

# Sau đó sort từng hàng để tìm diện tích.

# ---

# ## 7. Độ khó thật của bài

# Đây là bài **Medium nhưng trick khá hay**:

# * prefix height
# * sort mỗi hàng
# * greedy width

# Time complexity:

# ```
# O(m * n log n)
# ```

# ---

# 💡 Nếu bạn muốn, tôi có thể giải tiếp:

# * **intuition rất dễ hiểu (vì sao sort lại đúng)**
# * **dry run từng bước**
# * **code Java tối ưu O(mn log n)**
# * hoặc **cách nghĩ ra bài này trong interview**.
