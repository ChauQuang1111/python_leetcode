# Bài **“Count Submatrices with Top-Left Element and Sum Less Than k”(18/03/2026)

# Mình sẽ giải thích **từng dòng + tư duy thuật toán**, rồi viết lại code có **chú thích rõ ràng** cho bạn 👇

# ---

# # 🧠 Ý tưởng chính của thuật toán

# Thay vì:

# * duyệt từng submatrix rồi tính tổng (rất chậm ❌)

# 👉 Ta dùng **2D Prefix Sum** để:

# * biến mỗi ô `(i, j)` thành **tổng của submatrix từ (0,0) → (i,j)**

# Sau đó:

# * chỉ cần đếm bao nhiêu ô có giá trị ≤ k

# ---

# ⚙️ Phân tích code từng bước

## 🔹 Dòng 1

# ```python
# grid = map(accumulate, grid)
# ```

# 👉 `accumulate` (từ `itertools`) = tính **prefix sum theo hàng**

# Ví dụ:

# ```
# [1, 2, 3] → [1, 3, 6]
# ```

# Áp dụng cho mỗi hàng:

# ```
# grid =
# 1 2
# 3 4

# → sau bước này:

# 1 3
# 3 7
# ```

# ---

# ## 🔹 Dòng 2

# ```python
# grid = map(accumulate, zip(*grid))
# # ```

# # 👉 `zip(*grid)` = transpose (đổi hàng ↔ cột)

# # Ví dụ:

# # ```
# # 1 3
# # 3 7

# # → zip(*grid):

# # (1,3)
# # (3,7)
# ```

# 👉 Sau đó lại `accumulate` → prefix sum theo cột

# ```
# (1,3) → (1,4)
# (3,7) → (3,10)
# ```

# ---

# 👉 Khi transpose lại, ta có:

# ```
# 1   3
# 4  10
# ```

# 🔥 Đây chính là:
# 👉 **prefix sum 2D**

# Mỗi ô = tổng từ (0,0) → (i,j)

# ---

# ## 🔹 Dòng 3

# ```python
# return sum(val <= k for row in grid for val in row)


# 👉 Duyệt tất cả các ô:

# * nếu `val <= k` → tính 1

# 👉 Vì:

# * mỗi ô đại diện cho **1 submatrix từ (0,0)**

# ---

# # 🎯 Tổng kết thuật toán

# 1. Prefix sum theo hàng
# 2. Prefix sum theo cột
# 3. Mỗi ô = tổng submatrix (0,0 → i,j)
# 4. Đếm số ô ≤ k

# ⏱️ Time: `O(m * n)`
# ⚡ Rất tối ưu

# ---

# 🧾 Code có chú thích đầy đủ

from itertools import accumulate
from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        
        # Bước 1: Tính prefix sum theo từng hàng
        # Ví dụ: [1,2,3] -> [1,3,6]
        grid = list(map(accumulate, grid))
        
        # Bước 2: Transpose ma trận rồi tính prefix sum theo cột
        # zip(*grid) dùng để chuyển hàng thành cột
        # Sau đó accumulate sẽ cộng dồn theo cột
        grid = list(map(accumulate, zip(*grid)))
        
        # Bước 3: Đếm số phần tử <= k
        # Mỗi phần tử (i,j) bây giờ là tổng của submatrix từ (0,0) đến (i,j)
        return sum(
            val <= k   # nếu tổng <= k thì tính 1
            for row in grid
            for val in row
        )
# ```

# ---

# # 🔥 Insight quan trọng (cực đáng nhớ)

# 👉 Sau 2 lần accumulate:

# ```
# grid[i][j] = sum của hình chữ nhật từ (0,0) → (i,j)
# ```

# 👉 Vì đề **fix top-left = (0,0)**
# → chỉ cần prefix sum là giải được ngay

# ---

# # 🚀 Nếu bạn muốn nâng level

# Mình có thể giúp bạn:

# * Viết lại cách này bằng Java (chuẩn interview 💼)
# * Hoặc mở rộng sang bài khó hơn: submatrix bất kỳ (không fix (0,0))

# Chỉ cần nói 👍


# ---

# ## 🧠 Ý nghĩa đề bài

# Bạn được cho:

# * Một ma trận số nguyên `grid` kích thước `m x n`
# * Một số nguyên `k`

# Nhiệm vụ:
# 👉 Đếm **bao nhiêu ma trận con (submatrix)** thỏa mãn:

# 1. **Bắt đầu từ góc trên bên trái (top-left)** của ma trận (tức là luôn bắt đầu tại `(0,0)`)
# 2. Tổng các phần tử trong ma trận con đó **< k**

# ---

# ## 📦 Submatrix là gì?

# Submatrix = một phần hình chữ nhật con của ma trận.

# Ví dụ:

# ```
# grid =
# 1 2
# 3 4
# ```

# Các submatrix bắt đầu từ (0,0):

# 1. Chỉ lấy (0,0):

# ```
# 1
# ```

# 2. Lấy hàng đầu:

# ```
# 1 2
# ```

# 3. Lấy cột đầu:

# ```
# 1
# 3
# ```

# 4. Lấy toàn bộ:

# ```
# 1 2
# 3 4
# ```

# ---

# ## 🎯 Điều kiện quan trọng

# 👉 **Chỉ xét các submatrix có góc trên trái cố định tại (0,0)**
# → Không xét submatrix bắt đầu từ chỗ khác

# 👉 Tính tổng từng submatrix rồi:

# * Nếu tổng < k → tính vào kết quả

# ---

# ## 🔍 Ví dụ

# ```
# grid =
# 1 1
# 1 1
# k = 3
# ```

# Các submatrix từ (0,0):

# 1. `[1]` → sum = 1 < 3 ✅
# 2. `[1 1]` → sum = 2 < 3 ✅
# 3. `[1; 1]` → sum = 2 < 3 ✅
# 4. `[1 1; 1 1]` → sum = 4 ≥ 3 ❌

# 👉 Kết quả: **3**

# ---

# ## 💡 Tóm lại cách hiểu

# * Fix điểm bắt đầu là `(0,0)`
# * Mở rộng xuống dưới và sang phải
# * Với mỗi hình chữ nhật tạo được:

#   * Tính tổng
#   * Nếu < k → đếm

# ---

# ## 🚀 Hint cách làm (ngắn gọn)

# * Dùng **prefix sum 2D** để tính tổng nhanh
# * Duyệt tất cả `(i, j)` là góc dưới phải
# * Tính tổng từ `(0,0)` → `(i,j)`

# ---

# Nếu bạn muốn, mình có thể:

# * Giải chi tiết bằng code Java (đúng style bạn đang học)
# * Hoặc vẽ hình giúp bạn hiểu trực quan hơn 👍
