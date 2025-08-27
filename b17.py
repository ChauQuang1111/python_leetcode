# 3459. Length of Longest V-Shaped Diagonal Segment(27/08/2025)
import functools
from typing import List

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        # 4 hướng chéo
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        n = len(grid)     # số hàng
        m = len(grid[0])  # số cột

        # Bảng ánh xạ giá trị kế tiếp cần có
        # grid[x][y] = 1 => cần 2
        # grid[x][y] = 2 => cần 1
        # nv[v] cho ta giá trị tiếp theo mong muốn
        nv = [2, 2, 0]

        @functools.cache
        # @functools.cache là một decorator trong Python. Nó giúp bạn tối ưu hóa các hàm đệ quy hoặc các hàm tốn thời gian bằng cách 
        # lưu trữ kết quả của các lần gọi hàm trước đó. Kỹ thuật này được gọi là memoization
        def helper(x, y, turned, dir):
           
            # DFS + ghi nhớ
            # x, y    : vị trí hiện tại
            # turned  : đã rẽ hướng 1 lần chưa (True/False)
            # dir     : hướng hiện tại (0..3)
            # Trả về độ dài đường chéo dài nhất bắt đầu từ (x,y)
            
            res = 1  # ít nhất lấy được ô (x,y)
            dx, dy = dirs[dir]

            # --- 1. Tiếp tục đi thẳng theo cùng hướng ---
            if (0 <= x + dx < n and 0 <= y + dy < m 
                and grid[x + dx][y + dy] == nv[grid[x][y]]):
                res = helper(x + dx, y + dy, turned, dir) + 1

            # --- 2. Nếu chưa rẽ, thử rẽ sang hướng tiếp theo (90°) ---
            if not turned:
                ndir = (dir + 1) % 4  # quay sang hướng kế tiếp
                dx, dy = dirs[ndir]
                if (0 <= x + dx < n and 0 <= y + dy < m 
                    and grid[x + dx][y + dy] == nv[grid[x][y]]):
                    res = max(res, helper(x + dx, y + dy, True, ndir) + 1)

            return res

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:  # chỉ bắt đầu từ ô có giá trị 1
                    # ước lượng tối đa có thể đi theo mỗi hướng
                    # nếu nhỏ hơn đáp án hiện tại thì bỏ qua
                    tm = (n - i, j + 1, i + 1, m - j)
                    for d in range(4):
                        if tm[d] > ans:
                            ans = max(ans, helper(i, j, False, d))

        return ans



# ## 🚀 Ý tưởng chính của thuật toán

# * Bài toán: Tìm đoạn đường chéo dài nhất trong ma trận `grid`, bắt đầu từ ô có giá trị `1`, đi theo đường chéo **luân phiên 1 → 2 → 1 → 2 …**
# * Có thể đi theo **4 hướng chéo**:

#   * ↘ `(1,1)`
#   * ↙ `(1,-1)`
#   * ↖ `(-1,-1)`
#   * ↗ `(-1,1)`
# * Trong quá trình đi, ta được phép **rẽ hướng đúng 1 lần** (biến `turned` = True/False).
# * Dùng **DFS + memoization** (`functools.cache`) để tránh tính toán lại.

# ---

# ## 📜 Code có chú thích chi tiết

# import functools
# from typing import List

# class Solution:
#     def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
#         # 4 hướng chéo
#         dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
#         n = len(grid)     # số hàng
#         m = len(grid[0])  # số cột

#         # Bảng ánh xạ giá trị kế tiếp cần có
#         # grid[x][y] = 1 => cần 2
#         # grid[x][y] = 2 => cần 1
#         # nv[v] cho ta giá trị tiếp theo mong muốn
#         nv = [2, 2, 0]

#         @functools.cache
#         def helper(x, y, turned, dir):
#             """
#             DFS + ghi nhớ
#             x, y    : vị trí hiện tại
#             turned  : đã rẽ hướng 1 lần chưa (True/False)
#             dir     : hướng hiện tại (0..3)
#             Trả về độ dài đường chéo dài nhất bắt đầu từ (x,y)
#             """
#             res = 1  # ít nhất lấy được ô (x,y)
#             dx, dy = dirs[dir]

#             # --- 1. Tiếp tục đi thẳng theo cùng hướng ---
#             if (0 <= x + dx < n and 0 <= y + dy < m 
#                 and grid[x + dx][y + dy] == nv[grid[x][y]]):
#                 res = helper(x + dx, y + dy, turned, dir) + 1

#             # --- 2. Nếu chưa rẽ, thử rẽ sang hướng tiếp theo (90°) ---
#             if not turned:
#                 ndir = (dir + 1) % 4  # quay sang hướng kế tiếp
#                 dx, dy = dirs[ndir]
#                 if (0 <= x + dx < n and 0 <= y + dy < m 
#                     and grid[x + dx][y + dy] == nv[grid[x][y]]):
#                     res = max(res, helper(x + dx, y + dy, True, ndir) + 1)

#             return res

#         ans = 0
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == 1:  # chỉ bắt đầu từ ô có giá trị 1
#                     # ước lượng tối đa có thể đi theo mỗi hướng
#                     # nếu nhỏ hơn đáp án hiện tại thì bỏ qua
#                     tm = (n - i, j + 1, i + 1, m - j)
#                     for d in range(4):
#                         if tm[d] > ans:
#                             ans = max(ans, helper(i, j, False, d))

#         return ans


# ## 🔑 Giải thích các bước

# 1. **Bắt đầu từ mỗi ô có giá trị 1** vì đường chéo luôn khởi đầu bằng số 1.
# 2. Với mỗi hướng chéo `d`, gọi `helper(i, j, False, d)` để DFS tìm đường dài nhất:

#    * Nếu ô tiếp theo hợp lệ (còn trong ma trận và giá trị đúng), đi tiếp.
#    * Nếu chưa rẽ (`turned = False`), thử rẽ sang hướng mới.
#    * Dùng `cache` để nhớ kết quả, tránh tính toán lại.
# 3. **Pruning (tối ưu)**: trước khi DFS, ước lượng độ dài tối đa có thể đi từ ô `(i,j)` theo từng hướng (`tm`). Nếu `tm[d] <= ans` thì bỏ qua để tiết kiệm thời gian.
# 4. Trả về `ans` là chiều dài đường chéo dài nhất tìm được.

# ---

# ## ⏱️ Độ phức tạp

# * Có `O(m*n*4*2)` trạng thái (`m*n` ô, 4 hướng, turned=True/False).
# * Mỗi trạng thái tính tối đa 2 bước (đi thẳng hoặc rẽ), nên độ phức tạp **O(m\*n)**.
# * Không gian `O(m*n*4*2)` cho memoization.

# ---

# Bạn có muốn mình vẽ thêm **hình minh họa ví dụ đường đi zigzag** để dễ hiểu hơn không?
# Thuật toán bạn đưa ra là một giải pháp hiệu quả để tìm đường chéo hình chữ "V" dài nhất trong một lưới, sử dụng **tìm kiếm theo chiều sâu (DFS) và ghi nhớ (memoization)**.

# ### Tổng quan thuật toán

# Ý tưởng chính là duyệt qua mọi ô trong lưới. Nếu gặp một ô có giá trị `1`, thuật toán sẽ bắt đầu một quá trình tìm kiếm đệ quy để khám phá tất cả các đường đi hình chữ "V" có thể bắt đầu từ đó.

# Để tránh tính toán lại, một kỹ thuật **ghi nhớ** được sử dụng. Mọi kết quả của các bài toán con sẽ được lưu lại, giúp chương trình chạy nhanh hơn nhiều. Cuối cùng, kết quả dài nhất trong số tất cả các đường đi được tìm thấy sẽ là câu trả lời.

# ---

# ### Phân tích chi tiết mã nguồn

# #### Các biến và cấu trúc dữ liệu chính

# * `dirs`: Một mảng tĩnh chứa các cặp số nguyên, đại diện cho **bốn hướng di chuyển chéo**: `(1, 1)` (xuống-phải), `(1, -1)` (xuống-trái), `(-1, -1)` (lên-trái), và `(-1, 1)` (lên-phải).
# * `nv`: Mảng `[0, 2, 1]` giúp xác định giá trị tiếp theo mong đợi trên đường đi.
#     * `nv[1]` là `2`, nghĩa là nếu ô hiện tại là `1`, ô tiếp theo phải là `2`.
#     * `nv[2]` là `1`, nghĩa là nếu ô hiện tại là `2`, ô tiếp theo phải là `1`.
#     * `nv[0]` không được sử dụng.
# * `@functools.cache`: Đây là một decorator của Python. Nó tự động lưu kết quả của hàm `helper` vào bộ nhớ đệm. Nếu hàm được gọi lại với cùng một bộ tham số (`x, y, turned, dir`), nó sẽ trả về kết quả đã lưu mà không cần chạy lại hàm.

# #### Hàm đệ quy `helper(x, y, turned, dir)`

# Đây là trái tim của thuật toán, thực hiện việc tìm kiếm đường đi.

# * **Tham số**:
#     * `x, y`: Tọa độ hiện tại của ô.
#     * `turned`: Một biến boolean (`True` hoặc `False`) cho biết đường đi đã rẽ hay chưa.
#     * `dir`: Hướng di chuyển hiện tại.
# * **Logic**:
#     * `res = 1`: Khởi tạo độ dài đoạn đường thẳng từ ô hiện tại là 1.
#     * Kiểm tra ô tiếp theo: Nó tính toán tọa độ của ô tiếp theo theo hướng `dir` và kiểm tra xem ô đó có nằm trong lưới và có giá trị đúng (`nv[grid[x][y]]`) hay không.
#     * Nếu hợp lệ, nó gọi đệ quy `helper` cho ô tiếp theo và cộng thêm 1 vào kết quả.
#     * Kiểm tra rẽ: `if not turned`: Nếu đường đi **chưa** rẽ, nó sẽ thử một hướng mới (hướng tiếp theo trong `dirs`).
#         * Nó kiểm tra ô tiếp theo sau khi rẽ.
#         * Nếu hợp lệ, nó gọi đệ quy `helper` với tham số `turned` được đặt là `True` (vì đường đi đã rẽ).
#         * Nó so sánh kết quả của đường đi thẳng và đường đi rẽ, lấy giá trị lớn nhất và cập nhật vào `res`.

# #### Vòng lặp chính và các tối ưu hóa

# * Vòng lặp `for i in range(n)` và `for j in range(m)`: Thuật toán duyệt qua từng ô trong lưới.
# * `if grid[i][j] == 1`: Chỉ bắt đầu tìm kiếm từ những ô có giá trị `1`.
# * **Tối ưu hóa**:
#     * `tm = (n - i, j + 1, i + 1, m - j)`: Mảng này tính toán độ dài **tối đa lý thuyết** của một đường đi thẳng từ ô `(i, j)` đến biên của lưới theo mỗi hướng.
#     * `if tm[d] > ans`: Trước khi gọi đệ quy `helper`, thuật toán kiểm tra xem độ dài lý thuyết có lớn hơn kết quả tốt nhất hiện tại (`ans`) hay không. Nếu không, nó sẽ bỏ qua cuộc gọi đệ quy đó, giúp tiết kiệm thời gian đáng kể.
#     * `ans = max(ans, helper(i, j, False, d))`: Kết quả của hàm `helper` là độ dài của đoạn đường sau ô bắt đầu. Do đó, chúng ta không cần cộng thêm 1 vào đây. (Lưu ý: Cách triển khai này hơi khác với phiên bản Java, nơi `dfs` trả về độ dài đoạn đường sau ô đầu tiên và cần cộng thêm 1 sau khi gọi).