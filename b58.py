# 778. Swim in Rising Water(06/10/2025)
# Ok 👍 ta cùng **giải thích thuật toán của bài “778. Swim in Rising Water”** và thêm **chú thích chi tiết vào code** để bạn hiểu rõ từng phần nhé.

# ---

# ## 🧠 **Tư duy thuật toán**

# ### 🎯 **Mục tiêu**

# * Bạn có một ma trận `grid[n][n]`, trong đó `grid[r][c]` biểu thị độ cao của ô (r, c).
# * Nước dâng dần theo thời gian t = 0, 1, 2, ...
# * Tại thời điểm `t`, bạn có thể di chuyển đến các ô có độ cao `<= t`.
# * Bạn muốn **tìm thời gian nhỏ nhất `t`** sao cho có thể đi từ `(0,0)` → `(n-1,n-1)`.



# ### 💡 **Ý tưởng chính**

# 1. Dễ thấy rằng **khi t đủ lớn**, bạn chắc chắn có thể đi được (vì tất cả ô đều ≤ t).

# 2. Ngược lại, nếu t quá nhỏ, đường sẽ bị chặn.
#    👉 Vậy ta có thể **dùng Binary Search** trên giá trị `t`.

# 3. Với mỗi `t` (gọi là `mid` trong code), ta dùng **DFS (hoặc BFS)** để kiểm tra xem **có thể đi từ (0,0) → (n-1,n-1)** mà **tất cả các ô ≤ mid** hay không.

# 4. Nếu có thể đi được ⇒ ta thử giảm `t` xuống (vì có thể vẫn có giá trị nhỏ hơn).
#    Nếu không đi được ⇒ phải tăng `t` lên.

# ---

# ## 🧩 **Code có chú thích chi tiết**

# ```python
from typing import List
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)  # Kích thước ma trận n x n
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 4 hướng di chuyển (phải, xuống, trái, lên)
        visited = set()  # Tập hợp các ô đã đi qua để tránh lặp vô hạn

        # Hàm DFS kiểm tra có thể đến đích với mực nước max_time hay không
        def dfs(r, c, max_time):
            # Nếu đến được góc dưới phải (đích)
            if r == n - 1 and c == n - 1:
                return True 
            
            visited.add((r, c))  # Đánh dấu ô hiện tại là đã thăm

            # Duyệt qua 4 hướng xung quanh
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc  # Tính tọa độ ô kế bên

                # Kiểm tra điều kiện:
                # - Nằm trong lưới
                # - Chưa thăm
                # - Độ cao ô ≤ max_time (nghĩa là nước đã đủ cao để qua)
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] <= max_time:
                    # Gọi đệ quy kiểm tra từ ô mới
                    if dfs(nr, nc, max_time):
                        return True 
        
            # Không có đường hợp lệ
            return False
        
        # Phạm vi tìm kiếm giá trị thời gian t
        # Bắt đầu từ max(grid[0][0], grid[n-1][n-1]) (vì ít nhất phải cao bằng ô đầu hoặc ô cuối)
        s = max(grid[0][0], grid[n-1][n-1])
        e = n * n - 1  # Giá trị lớn nhất có thể có trong grid
        res = e  # Lưu kết quả nhỏ nhất tìm được

        # Binary Search trên khoảng [s, e]
        while s <= e:
            m = (s + e) // 2  # Lấy giá trị t giữa (mid)
            visited = set()  # Reset visited mỗi lần kiểm tra

            # Nếu có thể đến đích với mực nước m
            if dfs(0, 0, m):
                res = m      # Cập nhật kết quả
                e = m - 1    # Thử giảm mực nước xuống
            else:
                s = m + 1    # Không đến được → tăng mực nước lên
        
        return res  # Trả về mực nước nhỏ nhất đủ để đi từ (0,0) → (n-1,n-1)


# ---

# ## ⚙️ **Độ phức tạp**

# * **DFS mỗi lần**: O(n²)
# * **Binary Search**: O(log(max_height)) ≈ O(log(n²)) = O(log n)

# ➡️ **Tổng thể**: O(n² * log n)

# ---

# ## ✅ **Ví dụ minh họa**

# ```
# grid = [
#   [0, 2],
#   [1, 3]
# ]

# - t = 0 → chỉ có thể đứng ở (0,0)
# - t = 1 → có thể đi (0,0) → (1,0)
# - t = 2 → đi được (0,0) → (0,1) → (1,1)
# → Kết quả = 3 (nhỏ nhất sao cho có đường tới đích)
# ```

# ---

# Bạn có muốn mình vẽ thêm **sơ đồ minh họa luồng đi DFS + binary search** cho ví dụ trên không? (rất dễ hiểu bằng hình 👀)

# # 778. Swim in Rising Water - Giải thích đề bài

# ## Đề bài
# Cho một lưới **n x n** chứa các số nguyên không âm, mỗi ô `grid[i][j]` đại diện cho **độ cao** (elevation) tại vị trí đó.

# Ban đầu, bạn đang ở ô **góc trên cùng bên trái** `(0, 0)` và muốn đến ô **góc dưới cùng bên phải** `(n-1, n-1)`.

# Mỗi giây, mực nước tăng lên 1 đơn vị. Tại thời điểm `t`:
# - Bạn có thể **bơi** (di chuyển) giữa 2 ô kề nhau (lên/xuống/trái/phải)
# - **Điều kiện**: độ cao của cả 2 ô phải **≤ t** (nước đã ngập đến đủ cao)

# ## Yêu cầu
# Tìm **thời gian nhỏ nhất** để có thể bơi từ `(0,0)` đến `(n-1, n-1)`.

# ## Ví dụ minh họa

# **Ví dụ 1:**
# ```
# Input: grid = [[0,2],
#                [1,3]]
# Output: 3
# ```

# **Giải thích:**
# - t=0: Ở (0,0), độ cao = 0
# - t=1: Có thể đi sang (0,1) không? Không, vì độ cao (0,1) = 2 > 1
# - t=2: Vẫn chưa thể đi (0,1) vì 2 > 2 là sai
# - t=3: Bây giờ có thể đi (0,0)→(0,1)→(1,1) vì tất cả độ cao ≤ 3

# **Ví dụ 2:**
# ```
# Input: grid = [[0,1,2,3,4],
#                [24,23,22,21,5],
#                [12,13,14,15,16],
#                [11,17,18,19,20],
#                [10,9,8,7,6]]
# Output: 16
# ```

# ## Ý nghĩa
# - Về bản chất, bạn cần tìm **đường đi** từ góc trên-trái đến góc dưới-phải
# - Sao cho **giá trị lớn nhất** trên đường đi đó là **nhỏ nhất có thể**
# - Đây là bài toán **minimax path** (minimize the maximum)

# ## Gợi ý cách giải
# - **Binary Search** + BFS/DFS: Tìm kiếm nhị phân thời gian t, kiểm tra xem có đường đi nào với tất cả ô ≤ t không
# - **Dijkstra's Algorithm**: Coi như tìm đường đi với "chi phí" là giá trị max trên đường đi
# - **Union-Find**: Tăng dần ngưỡng độ cao và kiểm tra khi nào 2 góc được kết nối