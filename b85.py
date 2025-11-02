
# // 2257. Count Unguarded Cells in the Grid(02/11/2025)
# // Tốt lắm 👍 — đây là bài **LeetCode 2257: "Count Unguarded Cells in the Grid"**, một bài *simulation (mô phỏng)* khá hay.
# // Mình sẽ giúp bạn hiểu **đề bài**, **ví dụ**, và **ý tưởng giải** nhé 👇
# Rất hay 👍 — đoạn code Python của bạn là một lời giải **đúng và dễ hiểu** cho bài **LeetCode 2257: Count Unguarded Cells in the Grid**.
# Mình sẽ **giải thích thuật toán chi tiết** và thêm **chú thích từng dòng vào code** để bạn hiểu sâu cách hoạt động nhé 👇

# ---

# ### 🔍 Giải thích ý tưởng

# 1. **Tạo lưới `grid` kích thước `m × n`**, mỗi ô ban đầu là `0` (ô trống).
# 2. **Đánh dấu tường (`walls`) và bảo vệ (`guards`) là `1`**, vì đây là những ô “bị chặn” — ánh sáng của guard không chiếu qua được.
# 3. **Từ mỗi guard**, quét 4 hướng:

#    * **Trên, Dưới, Trái, Phải**
#    * Dừng lại nếu gặp `1` (tường hoặc guard khác)
#    * Đánh dấu các ô bị chiếu sáng là `2` (bị giám sát)
# 4. Sau khi quét xong, **đếm số ô còn là `0`** (chưa bị giám sát, không có guard, không có wall).


### 🧠 Thuật toán có độ phức tạp

# * Mỗi guard chiếu 4 hướng, tối đa `O(m + n)` ô mỗi hướng.
#   → Độ phức tạp tổng: **O(G × (m + n))**, rất hiệu quả.

# ---

# ### ✅ Code có chú thích chi tiết

# ```python
from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Tạo lưới m x n, ban đầu tất cả là 0 (ô trống)
        grid = [[0] * n for _ in range(m)]

        # Đánh dấu tường là 1 (ô bị chặn)
        for r, c in walls:
            grid[r][c] = 1

        # Đánh dấu guard là 1 (cũng là ô bị chặn, không thể bị giám sát)
        for r, c in guards:
            grid[r][c] = 1

        # Với mỗi guard, quét 4 hướng
        for r, c in guards:
            # Hướng lên (giảm hàng)
            u = r - 1
            while u >= 0 and grid[u][c] != 1:  # Dừng nếu gặp guard hoặc wall
                grid[u][c] = 2  # Đánh dấu là ô bị giám sát
                u -= 1          # Tiếp tục đi lên

            # Hướng xuống (tăng hàng)
            d = r + 1
            while d < m and grid[d][c] != 1:
                grid[d][c] = 2
                d += 1

            # Hướng trái (giảm cột)
            l = c - 1
            while l >= 0 and grid[r][l] != 1:
                grid[r][l] = 2
                l -= 1

            # Hướng phải (tăng cột)
            ri = c + 1
            while ri < n and grid[r][ri] != 1:
                grid[r][ri] = 2
                ri += 1

        # Đếm số ô chưa bị giám sát (vẫn là 0)
        unguarded = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    unguarded += 1

        # Trả về kết quả
        return unguarded
# ```

# ---

# ### 🧮 Ví dụ chạy thử

# ```python
# m = 3
# n = 3
# # guards = [[1, 1]]
# walls = [[0, 1]]

# sol = Solution()
# print(sol.countUnguarded(m, n, guards, walls))
# ```

# **Kết quả:**

# ```
# 4
# ```

# ---

# ### 🗺️ Minh họa trực quan ví dụ trên

# ```
# Bảng ban đầu:
# . W .
# . G .
# . . .

# Sau khi guard ở (1,1) quét 4 hướng:
# → Trái: (1,0)
# → Phải: (1,2)
# → Lên: bị tường (0,1)
# → Xuống: (2,1)

# Bảng kết quả:
# . W .
# 2 G 2
# . 2 .

# Tổng ô chưa giám sát (0): 4 ô.
# ```

# ---

# Bạn có muốn mình viết lại phiên bản này theo **cách gọn hơn (dùng mảng hướng `dx, dy`)** để tránh lặp 4 đoạn `while` không?

# import java.util.*;

# public class b86 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {

#         int m = sc.nextInt();

#         int n = sc.nextInt();

#         int g = sc.nextInt();
#         int[][] guards = new int[g][2];

#         for (int i = 0; i < g; i++) {
#             guards[i][0] = sc.nextInt();
#             guards[i][1] = sc.nextInt();
#         }
#         ;
#         int w = sc.nextInt();
#         int[][] walls = new int[w][2];

#         for (int i = 0; i < w; i++) {
#             walls[i][0] = sc.nextInt();
#             walls[i][1] = sc.nextInt();
#         }

#         // Gọi hàm xử lý

#         int result = countUnguarded(m, n, guards, walls);

#         // Xuất kết quả
#         System.out.println(result);

#         sc.close();
#     }

#     public static int countUnguarded(int m, int n, int[][] guards, int[][] walls) {

#         int[][] visit = new int[m][n]; // Mảng đánh dấu: 0 = trống, 1 = bị giám sát, 2 = tường hoặc guard
#         int count = 0; // Đếm số ô bị giám sát
#         int gr = guards.length; // Số lượng guards
#         int wr = walls.length; // Số lượng walls

#         // Đánh dấu các ô là tường (2)
#         for (int[] wall : walls) {
#             visit[wall[0]][wall[1]] = 2;
#         }

#         // Đánh dấu các ô là guards (2)
#         for (int[] gu : guards) {
#             visit[gu[0]][gu[1]] = 2;
#         }

#         // Duyệt qua từng guard
#         for (int row = 0; row < gr; row++) {
#             int dx = guards[row][0]; // Hàng của guard
#             int dy = guards[row][1]; // Cột của guard

#             // Hướng xuống
#             for (int i = dx + 1; i < m; i++) {
#                 if (visit[i][dy] == 2)
#                     break; // Gặp tường hoặc guard thì dừng
#                 if (visit[i][dy] == 1)
#                     continue; // Nếu đã giám sát thì bỏ qua
#                 visit[i][dy] = 1; // Đánh dấu là bị giám sát
#                 count++;
#             }

#             // Hướng phải
#             for (int i = dy + 1; i < n; i++) {
#                 if (visit[dx][i] == 2)
#                     break;
#                 if (visit[dx][i] == 1)
#                     continue;
#                 visit[dx][i] = 1;
#                 count++;
#             }

#             // Hướng trái
#             for (int i = dy - 1; i >= 0; i--) {
#                 if (visit[dx][i] == 2)
#                     break;
#                 if (visit[dx][i] == 1)
#                     continue;
#                 visit[dx][i] = 1;
#                 count++;
#             }

#             // Hướng lên
#             for (int i = dx - 1; i >= 0; i--) {
#                 if (visit[i][dy] == 2)
#                     break;
#                 if (visit[i][dy] == 1)
#                     continue;
#                 visit[i][dy] = 1;
#                 count++;
#             }
#         }

#         // Tính tổng số ô không được giám sát
#         int sum = (m * n) - (gr + wr + count);
#         return sum;
#     }
# }

# // ---

# // ## 🧩 Đề bài (dịch và giải thích)

# // Bạn có một **bảng (grid)** gồm `m` hàng và `n` cột,
# // ban đầu tất cả các ô đều **trống**.

# // Trên bảng có hai loại ô đặc biệt:

# // * **guards (bảo vệ)** — có thể “nhìn thấy” theo 4 hướng (trái, phải, lên,
# // xuống)
# // * **walls (tường)** — chặn tầm nhìn của guards

# // ---

# // ### 🧱 Quy tắc “tầm nhìn” của guard:

# // Một guard có thể **giám sát (guard)** các ô **trống** theo 4 hướng:

# // * Trái ←
# // * Phải →
# // * Trên ↑
# // * Dưới ↓

# // Nhưng **dừng lại khi gặp tường hoặc guard khác**.

# // ---

# // ### 🎯 Yêu cầu:

# // Tính xem có **bao nhiêu ô không được giám sát (unguarded)**.

# // ---

# // ### 📥 Input:

# // * `m, n` — kích thước bảng.
# // * `guards` — danh sách các tọa độ `[r, c]` của các guard.
# // * `walls` — danh sách các tọa độ `[r, c]` của các tường.

# // ---

# // ### 📤 Output:

# // * Một số nguyên — số lượng **ô trống không bị giám sát**.

# // ---

# // ## 📊 Ví dụ minh họa

# // ### Ví dụ 1:

# // ```
# // m = 4, n = 6
# // guards = [[0,0],[1,1],[2,3]]
# // walls = [[0,1],[2,2],[1,4]]
# // ```

# // Bảng ban đầu:

# // ```
# // G W . . . .
# // . G . . W .
# // . . W G . .
# // . . . . . .
# // ```

# // 🔹 “G” là guard
# // 🔹 “W” là wall
# // 🔹 “.” là ô trống

# // ---

# // Từng guard giám sát:

# // * Guard (0,0) → nhìn phải bị tường chặn ở (0,1), nhìn xuống hết hàng (0,0)
# // * Guard (1,1) → nhìn phải đến tường (1,4), nhìn lên (0,1: tường, chặn), nhìn
# // xuống (2,1: ok), (3,1: ok)
# // * Guard (2,3) → nhìn trái bị tường (2,2), nhìn phải (2,4), (2,5), nhìn lên
# // (1,3), (0,3), nhìn xuống (3,3)

# // Sau khi đánh dấu các ô được giám sát,
# // → Số ô **không được giám sát** = **7**

# // ✅ Output: `7`

# // ---

# // ## 💡 Ý tưởng giải:

# // 1. **Tạo bảng `grid`** để lưu trạng thái:

# // * `0` = ô trống
# // * `1` = guard
# // * `2` = wall
# // * `3` = ô được giám sát

# // 2. **Đặt các guard và wall vào bảng**.

# // 3. **Duyệt từng guard**, và theo 4 hướng:

# // * Dừng nếu gặp guard khác hoặc wall
# // * Đánh dấu các ô trống là “được giám sát” (`3`)

# // 4. Cuối cùng, **đếm số ô có giá trị `0`** (chưa bị giám sát).

# // ---

# // ## ⏱️ Độ phức tạp:

# // * Giả sử có `G` guards và `W` walls.
# // * Với mỗi guard, ta có thể đi qua tối đa `O(m + n)` ô.
# // → Độ phức tạp khoảng **O(G × (m + n))** — đủ nhanh cho giới hạn đề bài (`m, n
# // ≤ 1000`).

# // ---

# // Bạn có muốn mình viết cho bạn **một phiên bản code Java hoặc Python giải bài
# // này** (có chú thích từng bước) không?
# // Rất tuyệt 👏 — bạn đã tự viết ra một **thuật toán chạy đúng logic cho bài
# // 2257 – Count Unguarded Cells in the Grid**,
# // mình sẽ **giải thích chi tiết cách thuật toán hoạt động** để bạn hiểu rõ vì
# // sao nó đúng và có thể tối ưu thêm.

# // ---

# // ## 🎯 Mục tiêu của bài

# // Tính **số ô chưa được giám sát** (unguarded) trong một lưới `m × n`,
# // khi biết vị trí của **guards** (bảo vệ) và **walls** (tường).

# // ---

# // ## 🧠 Ý tưởng tổng quát của bạn

# // 1. Tạo một **ma trận `visit[m][n]`** để đánh dấu trạng thái từng ô.

# // * `0`: ô trống, chưa được giám sát.
# // * `1`: ô đã được giám sát bởi guard.
# // * `2`: ô bị chiếm (guard hoặc wall).

# // 2. **Đặt tường và guard** vào trong `visit` (đánh dấu bằng `2`).

# // 3. **Từ mỗi guard**, chiếu ra 4 hướng:

# // * Dừng lại nếu gặp tường hoặc guard khác (`visit == 2`).
# // * Đánh dấu các ô trống (`visit == 0`) là “được giám sát” (`visit = 1`).
# // * Nếu ô đã giám sát rồi (`visit == 1`) → bỏ qua (continue).

# // 4. **Đếm tổng số ô bị giám sát (`count`)** trong quá trình đó.

# // 5. Cuối cùng, tổng số ô **không được giám sát** =
# // [
# // \text{sum} = (m × n) - (\text{số guard} + \text{số wall} + \text{số ô giám
# // sát})
# // ]
# // tức là:

# // ```java
# // int sum = (m * n) - (gr + wr + count);
# // ```

# // ---

# // ## 🧩 Giải thích từng phần trong code của bạn

# // ### 1️⃣ Khởi tạo và đánh dấu guards / walls

# // ```java
# // int[][] visit = new int[m][n];
# // for (int[] wall : walls)
# // visit[wall[0]][wall[1]] = 2;
# // for (int[] gu : guards)
# // visit[gu[0]][gu[1]] = 2;
# // ```

# // 👉 Mỗi guard hoặc tường đều là vị trí **không thể được giám sát** (vì bị
# // chiếm),
# // nên gán `2`.

# // ---

# // ### 2️⃣ Duyệt qua từng guard

# // ```java
# // for (int row = 0; row < gr; row++) {
# // int dx = guards[row][0];
# // int dy = guards[row][1];
# // ```

# // * Lấy tọa độ `(dx, dy)` của từng guard để bắt đầu quét.

# // ---

# // ### 3️⃣ Quét 4 hướng độc lập

# // #### a. Hướng **xuống** (tăng hàng)

# // ```java
# // for (int i = dx + 1; i < m; i++) {
# // if (visit[i][dy] == 2) break;
# // if (visit[i][dy] == 1) continue;
# // visit[i][dy] = 1;
# // count++;
# // }
# // ```

# // * Từ guard, đi từng bước xuống (hàng tăng).
# // * Nếu gặp tường/guard (`2`): dừng lại.
# // * Nếu gặp ô đã giám sát (`1`): bỏ qua.
# // * Nếu ô trống (`0`): đánh dấu `1` và tăng `count`.

# // ---

# // #### b. Hướng **phải** (tăng cột)

# // ```java
# // for (int i = dy + 1; i < n; i++) {
# // if (visit[dx][i] == 2) break;
# // if (visit[dx][i] == 1) continue;
# // visit[dx][i] = 1;
# // count++;
# // }
# // ```

# // ---

# // #### c. Hướng **trái** (giảm cột)

# // ```java
# // for (int i = dy - 1; i >= 0; i--) {
# // if (visit[dx][i] == 2) break;
# // if (visit[dx][i] == 1) continue;
# // visit[dx][i] = 1;
# // count++;
# // }
# // ```

# // ---

# // #### d. Hướng **lên** (giảm hàng)

# // ```java
# // for (int i = dx - 1; i >= 0; i--) {
# // if (visit[i][dy] == 2) break;
# // if (visit[i][dy] == 1) continue;
# // visit[i][dy] = 1;
# // count++;
# // }
# // ```

# // ---

# // ### 4️⃣ Tính kết quả cuối cùng

# // ```java
# // int sum = (m * n) - (gr + wr + count);
# // return sum;
# // ```

# // * Tổng ô = `m × n`
# // * Trừ đi:

# // * guard (`gr`)
# // * wall (`wr`)
# // * các ô bị giám sát (`count`)

# // → Kết quả là **số ô không bị giám sát**.

# // ---

# // ## 🧮 Ví dụ minh họa

# // ```
# // m = 3, n = 3
# // guards = [[1,1]]
# // walls = [[0,1]]
# // ```

# // Bảng ban đầu:

# // ```
# // . W .
# // . G .
# // . . .
# // ```

# // Guard ở (1,1) giám sát:

# // * Trái: (1,0)
# // * Phải: (1,2)
# // * Lên: bị tường (0,1)
# // * Xuống: (2,1)

# // Các ô giám sát: 3 ô
# // Tổng ô = 9, guard = 1, wall = 1 →
# // `sum = 9 - (1+1+3) = 4`

# // ✅ Kết quả đúng: còn 4 ô không được giám sát.

# // ---

# // ## ⏱️ Độ phức tạp

# // * Có `G` guards, mỗi guard có thể chiếu tối đa `O(m + n)` ô.
# // * Tổng độ phức tạp: **O(G × (m + n))**, phù hợp với giới hạn LeetCode.

# // ---

# // ## ⚙️ Nhận xét & Cải thiện

# // * ✅ Ưu điểm:

# // * Code dễ hiểu, chạy đúng, không cần thêm mảng phụ.
# // * ⚠️ Có thể tối ưu:

# // * Dùng mảng `boolean` thay vì `int` để tiết kiệm bộ nhớ.
# // * Gom 4 hướng vào một mảng `dxdy` để tránh lặp code.
# // * Không cần `if (visit == 1) continue;` vì khi `1` thì `break` cũng không
# // sai.

# // ---

# // Bạn có muốn mình giúp **viết lại phiên bản ngắn gọn hơn** (ít lặp code, dùng
# // vòng lặp hướng tổng quát) nhưng **giữ nguyên logic của bạn** không?
