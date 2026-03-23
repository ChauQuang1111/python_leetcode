# // Bài **“Maximum Non Negative Product in a Matrix”** (23/03/2026)

# Mình sẽ giúp bạn **hiểu rõ thuật toán bottom-up (DP)** này + thêm **chú thích trực tiếp vào code** 👇

# ---

# # 🔥 Ý tưởng chính của code này

# 👉 Đây là **Dynamic Programming tối ưu bộ nhớ (rolling array)**

# Thay vì dùng `dp[m][n]` ❌
# → chỉ dùng **2 hàng**:

# * `prev_row`: hàng trên
# * `current_row`: hàng hiện tại

# ---

# # ## 🔑 Mỗi ô lưu gì?

# # ```python
# # [x][0] = min product (nhỏ nhất)
# # [x][1] = max product (lớn nhất)
# # ```

# # 👉 giống hệt tư duy bạn dùng trong Java

# # ---

# # ## 🔥 Quy tắc quan trọng

# Tại mỗi ô:

# * Nếu `val > 0`:

#   * min = val * min trước đó
#   * max = val * max trước đó

# * Nếu `val < 0`:

#   * min = val * max trước đó
#   * max = val * min trước đó

# * Nếu `val == 0`:

#   * cả min & max = 0

# ---

# # ✍️ Code đã thêm chú thích

# ```python
from math import inf
MOD = int(1e9+7)

class Solution:
    def maxProductPath(self, grid):
        
        # prev_row[j] = [min, max] tại cột j của hàng trước
        prev_row = [[inf, -inf] for _ in grid[0]]

        # ====== KHỞI TẠO Ô (0,0) ======
        if grid[0][0] < 0:
            prev_row[0][0] = grid[0][0]   # min
        else:
            prev_row[0][1] = grid[0][0]   # max

        # ====== XỬ LÝ HÀNG ĐẦU TIÊN ======
        for j in range(1, len(grid[0])):
            val = grid[0][j]

            if val < 0:
                # âm → đảo min/max
                prev_row[j][0] = val * prev_row[j-1][1]
                prev_row[j][1] = val * prev_row[j-1][0]

            elif val > 0:
                # dương → giữ nguyên
                prev_row[j][0] = val * prev_row[j-1][0]
                prev_row[j][1] = val * prev_row[j-1][1]

            else:
                # gặp 0 → reset
                prev_row[j][0] = 0
                prev_row[j][1] = 0

        # dùng để tính hàng hiện tại
        current_row = [[inf, -inf] for _ in grid[0]]

        # ====== DUYỆT TỪ HÀNG 1 TRỞ ĐI ======
        for i in range(1, len(grid)):

            row = grid[i]

            # ====== CỘT ĐẦU TIÊN ======
            val = row[0]

            if val < 0:
                current_row[0][0] = val * prev_row[0][1]
                current_row[0][1] = val * prev_row[0][0]

            elif val > 0:
                current_row[0][0] = val * prev_row[0][0]
                current_row[0][1] = val * prev_row[0][1]

            else:
                current_row[0][0] = 0
                current_row[0][1] = 0

            # ====== CÁC CỘT CÒN LẠI ======
            for j in range(1, len(row)):
                val = row[j]

                if val == 0:
                    current_row[j][0] = 0
                    current_row[j][1] = 0

                else:
                    # lấy từ 2 hướng: trên và trái
                    most_neg = min(prev_row[j][0], current_row[j-1][0])
                    most_pos = max(prev_row[j][1], current_row[j-1][1])

                    if val < 0:
                        # âm → đảo
                        current_row[j][0] = val * most_pos
                        current_row[j][1] = val * most_neg
                    else:
                        # dương → giữ
                        current_row[j][0] = val * most_neg
                        current_row[j][1] = val * most_pos

            # ====== SWAP 2 HÀNG ======
            prev_row, current_row = current_row, prev_row

        # ====== KẾT QUẢ ======
        prod = prev_row[-1][1]  # lấy max ở ô cuối

        if prod >= 0:
            return prod % MOD

        return -1
# ```

# ---

# # 🔥 Tóm tắt cực dễ nhớ

# 👉 Mỗi ô lưu:

# * min product
# * max product

# 👉 Mỗi bước:

# * lấy từ **trên + trái**
# * chọn:

#   * `most_neg` (nhỏ nhất)
#   * `most_pos` (lớn nhất)

# 👉 rồi:

# * nếu âm → đảo
# * nếu dương → giữ

# ---

# # ⚡ So sánh với code Java của bạn

# | Cách                   | Ưu điểm                 |
# | ---------------------- | ----------------------- |
# # | DFS + memo (Java)      | dễ viết                 |
# # | Bottom-up (Python này) | nhanh hơn, ít tốn stack |
# # | Rolling array          | tối ưu memory           |

# ---

# Nếu bạn muốn, mình có thể:

# * Giải từng bước trên **1 ví dụ cụ thể (trace từng ô)**
# * Hoặc convert code Python này → Java chuẩn style bạn đang dùng



# // Ok, mình sẽ giải thích **thuật toán trong code của bạn** theo kiểu dễ hiểu + đúng bản chất 👇

# import java.util.*;

# public class b225 {
#     static final int INF = Integer.MAX_VALUE; // dùng để đánh dấu đường không hợp lệ
#     static final int MOD = (int) 1e9 + 7; // mod theo đề
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         // nhập kích thước ma trận
#         int m = sc.nextInt();
#         int n = sc.nextInt();

#         int[][] grid = new int[m][n];

#         // nhập ma trận
#         int i = 0;
#         while (i < m) {
#             int j = 0;
#             while (j < n) {
#                 grid[i][j] = sc.nextInt();
#                 j++;
#             }
#             i++;
#         }

#         int result = maxProductPath(grid);

#         System.out.println(result);
#     }

#     public static int maxProductPath(int[][] grid) {
#         int m = grid.length, n = grid[0].length;

#         // dp[i][j] lưu min và max product từ (i,j) -> đích
#         Res[][] dp = new Res[m][n];

#         Res res = solve(grid, 0, 0, dp);

#         // nếu max < 0 -> không có đường hợp lệ
#         if (res.max < 0)
#             return -1;

#         return (int) (res.max % MOD);
#     }

#     // ================= DFS + MEMO =================
#     public static Res solve(int[][] grid, int i, int j, Res[][] dp) {
#         int m = grid.length, n = grid[0].length;

#         // ====== BASE CASE: tới đích ======
#         if (i == m - 1 && j == n - 1)
#             return new Res(grid[i][j], grid[i][j]);

#         // ====== OUT OF BOUND ======
#         if (i >= m || j >= n)
#             return new Res(INF, INF);

#         // ====== MEMO ======
#         if (dp[i][j] != null)
#             return dp[i][j];

#         // ====== ĐI XUỐNG & SANG PHẢI ======
#         Res down = solve(grid, i + 1, j, dp);
#         Res right = solve(grid, i, j + 1, dp);

#         Res res = new Res(0, 0);

#         // ====== CẢ 2 HƯỚNG HỢP LỆ ======
#         if (down.min != INF && right.min != INF) {

#             // thử tất cả trường hợp (vì có số âm)
#             long op1 = (long) grid[i][j] * down.min;
#             long op2 = (long) grid[i][j] * right.min;
#             long op3 = (long) grid[i][j] * down.max;
#             long op4 = (long) grid[i][j] * right.max;

#             // lấy min và max mới
#             res.min = Math.min(Math.min(op1, op2), Math.min(op3, op4));
#             res.max = Math.max(Math.max(op1, op2), Math.max(op3, op4));

#         }
#         // ====== CHỈ CÒN HƯỚNG RIGHT ======
#         else if (down.min == INF) {
#             res.min = (long) grid[i][j] * right.min;
#             res.max = (long) grid[i][j] * right.max;
#         }
#         // ====== CHỈ CÒN HƯỚNG DOWN ======
#         else if (right.min == INF) {
#             res.min = (long) grid[i][j] * down.min;
#             res.max = (long) grid[i][j] * down.max;
#         }

#         // lưu vào dp
#         dp[i][j] = res;

#         return res;
#     }

#     // ================= CLASS LƯU MIN/MAX =================
#     static class Res {
#         long min, max;

#         Res(long min, long max) {
#             this.min = min;
#             this.max = max;
#         }
#     }
# }

# // ---

# // # 🔹 Ý tưởng cốt lõi của thuật toán

# // Bài này không thể chỉ lưu **max** ❌
# // Vì có số âm:

# // 👉 âm × âm = dương
# // 👉 nên **min có thể biến thành max**

# // => Vì vậy, tại mỗi ô `(i, j)` ta phải lưu:

# // * `min`: tích nhỏ nhất đi đến đây
# // * `max`: tích lớn nhất đi đến đây

# // 👉 Class `Res` chính là để lưu 2 giá trị này.

# // ---

# // # 🔹 Ý tưởng tổng thể

# // Bạn đang dùng:

# // 👉 **DFS + Memoization (Top-down DP)**

# // ```java
# // solve(grid, i, j)
# // ```

# // = trả về:
# // 👉 min & max product từ `(i, j)` → `(m-1, n-1)`

# // ---

# // # 🔹 Base case (điểm dừng)

# // ```java
# // if (i == m - 1 && j == n - 1)
# // return new Res(grid[m - 1][n - 1], grid[m - 1][n - 1]);
# // ```

# // 👉 Nếu đang ở ô cuối:

# // * min = max = chính giá trị ô đó

# // ---

# // # 🔹 Out of bound

# // ```java
# // if (i >= m || j >= n)
# // return new Res(INF, INF);
# // ```

# // 👉 Nếu đi ra ngoài:

# // * coi như đường này **không hợp lệ**

# // ---

# // # 🔹 Memoization

# // ```java
# // if(dp[i][j] != null) return dp[i][j];
# // ```

# // 👉 Tránh tính lại → tối ưu từ exponential → O(m*n)

# // ---

# // # 🔹 2 hướng di chuyển

# // ```java
# // Res down = solve(grid, i + 1, j, dp);
# // Res right = solve(grid, i, j + 1, dp);
# // ```

# // 👉 Tại mỗi ô, bạn chỉ có 2 lựa chọn:

# // * đi xuống
# // * đi sang phải

# // ---

# // # 🔹 Tính toán giá trị tại (i, j)

# // Đây là phần **quan trọng nhất** 🔥

# // ```java
# // long op1 = grid[i][j] * down.min;
# // long op2 = grid[i][j] * right.min;
# // long op3 = grid[i][j] * down.max;
# // long op4 = grid[i][j] * right.max;
# // ```

# // 👉 Tại sao phải 4 phép?

# // Vì:

# // | grid[i][j] | xuống/phải | kết quả |
# // | ---------- | ---------- | ------- |
# // | dương | max | tốt |
# // | âm | min | tốt |

# // 👉 nên phải thử tất cả:

# // * nhân với min
# // * nhân với max
# // * từ down
# // * từ right

# // ---

# // ## 🔹 Lấy min và max mới

# // ```java
# // res.min = min(op1, op2, op3, op4);
# // res.max = max(op1, op2, op3, op4);
# // ```

# // 👉 đảm bảo không bỏ sót trường hợp:

# // * âm → dương
# // * dương → âm

# // ---

# // # 🔹 Xử lý trường hợp 1 hướng invalid

# // ```java
# // if (down.min == INF)
# // ```

# // 👉 nghĩa là không đi xuống được → chỉ đi phải

# // Tương tự cho right

# // ---

# // # 🔹 Lưu vào DP

# // ```java
# // dp[i][j] = res;
# // ```

# // 👉 mỗi ô chỉ tính 1 lần

# // ---

# // # 🔹 Kết quả cuối cùng

# // ```java
# // if (res.max < 0)
# // return -1;
# // ```

# // 👉 nếu max vẫn âm → không có đường hợp lệ

# // ---

# // ```java
# // return res.max % MOD;
# // ```

# // 👉 vì số có thể rất lớn

# // ---

# // # 🔥 Tóm tắt thuật toán (cực ngắn)

# // 👉 Mỗi ô lưu 2 giá trị:

# // * min product
# // * max product

# // 👉 Với mỗi ô:

# // * thử đi xuống + đi phải
# // * thử nhân với cả min và max
# // * lấy min/max mới

# // 👉 dùng memo để tối ưu

# // ---

# // # 🔹 Độ phức tạp

# // * Time: **O(m × n)**
# // * Space: **O(m × n)**

# // ---

# // # 🔥 Insight quan trọng nhất (phải nhớ)

# // 👉 Khi có số âm:

# // > Không bao giờ chỉ lưu max
# // > Luôn phải lưu cả min

# // ---

# // Nếu bạn muốn, mình có thể:

# // * Viết lại code dạng **bottom-up (dễ hiểu hơn)**
# // * Hoặc vẽ bảng DP từng bước (rất dễ “ngộ” luôn)

# // ## 🔹 Ý tưởng chính của đề

# // Bạn được cho một ma trận `grid` kích thước `m x n`, mỗi ô chứa một số nguyên
# // (có thể **âm, dương hoặc 0**).

# // 👉 Bạn **bắt đầu từ ô trên cùng bên trái (0,0)**
# // 👉 Và cần đi đến ô dưới cùng bên phải (m-1, n-1)

# // ### ⚠️ Quy tắc di chuyển:

# // * Chỉ được đi:

# // * **sang phải** ➡️
# // * **xuống dưới** ⬇️

# // ---

# // ## 🔹 Mục tiêu

# // * Tìm đường đi sao cho:
# // 👉 **tích của tất cả các số trên đường đi là lớn nhất**

# // * Nhưng có một điều kiện:
# // 👉 **Chỉ lấy kết quả nếu tích ≥ 0 (không âm)**

# // ---

# // ## 🔹 Kết quả trả về

# // * Nếu tồn tại đường đi có tích **không âm** → trả về **tích lớn nhất**
# // * Nếu **tất cả đường đều cho tích âm** → trả về **-1**

# // ---

# // ## 🔹 Ví dụ dễ hiểu

# // ### Ví dụ 1:

# // ```
# // grid =
# // [ [1, -2, 1],
# // [1, -2, 1],
# // [3, -4, 1] ]
# // ```

# // ### Các đường đi có thể:

# // 1. 1 → -2 → 1 → 1 → 1
# // 2. 1 → 1 → 3 → -4 → 1
# // 3. ...

# // 👉 Mỗi đường sẽ có **tích khác nhau**

# // ---

# // ## 🔹 Điểm khó của bài

# // 💡 Vì có số âm nên:

# // * **Âm × âm = dương**
# // * **Dương × âm = âm**

# // 👉 Vì vậy:

# // * Một đường đi có tích nhỏ ban đầu có thể trở thành **lớn nhất** nếu gặp thêm
# // số âm

# // ---

# // ## 🔹 Ý nghĩa thật sự của bài

# // Không phải chỉ tìm max bình thường ❌
# // Mà phải theo dõi:

# // 👉 **2 giá trị tại mỗi ô:**

# // * Tích lớn nhất đến đây
# // * Tích nhỏ nhất đến đây

# // (Vì tích nhỏ có thể biến thành lớn nếu nhân với số âm)

# // ---

# // ## 🔹 Tóm lại cách hiểu đề (rất ngắn)

# // 👉 Đi từ (0,0) → (m-1,n-1)
# // 👉 Chỉ đi phải hoặc xuống
# // 👉 Tính tích các số trên đường
# // 👉 Lấy **tích lớn nhất ≥ 0**
# // 👉 Nếu không có → trả **-1**

# // ---

# // Nếu bạn muốn, mình có thể:

# // * Giải chi tiết từng bước DP 🧠
# // * Viết code Java (đúng style bạn đang dùng)
# // * Hoặc vẽ bảng để bạn hiểu ngay trong 1 phút

# // Bạn muốn đi tiếp theo hướng nào?
