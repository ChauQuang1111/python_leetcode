# // Minimum Cost Path with Teleportations(28/01/2026)
# // Ok, mình **giải thích thuật toán đúng theo code bạn gửi**, đi **từng ý – từng biến**, để bạn hiểu **vì sao code chạy được** chứ không chỉ “thuộc” 👌
# // (Bài này khá nâng cao, giống **DP + Dijkstra nén trạng thái**)
# Ok 👍 mình sẽ làm **đúng 2 việc bạn yêu cầu**:

# 1. **Giải thích thuật toán bằng lời (tư duy → công thức → vì sao đúng)**
# 2. **Chèn chú thích trực tiếp vào code Python**, để bạn đọc code là hiểu ngay

# ---

# 1️⃣ Giải thích thuật toán (hiểu bản chất)

## Bài toán (rút gọn)

# * Có ma trận `grid`
# * Đi từ **(0,0)** → **(m-1,n-1)**
# * Cost = tổng giá trị các ô đi qua
# * Được dùng **tối đa `k` teleport**

# 👉 **Teleport** cho phép:

# * Không cần cộng cost của ô hiện tại
# * Nhưng chỉ dùng được **k lần**
# * Teleport hoạt động dựa trên **giá trị ô**

# ---

# ## Ý tưởng cốt lõi

# Thay vì:

# * Dijkstra (rất nặng)

# Ta dùng:

# > **DP + tối ưu bằng suffix minimum**

# ---

# ## Trạng thái DP

# ### `f[j]`

# > Chi phí nhỏ nhất để đi tới **cột j** ở **hàng hiện tại**

# 👉 Dùng mảng 1D để tiết kiệm bộ nhớ

# ---

### `min_f[x]`

# > Chi phí nhỏ nhất nếu ta đang đứng ở ô có **giá trị = x**

# ---

# ### `suf_min_f[x]`

# > Chi phí nhỏ nhất trong số **mọi ô có giá trị ≥ x**

# 📌 **Teleport dùng mảng này**

# ---

## Công thức chuyển trạng thái (QUAN TRỌNG NHẤT)

# Tại ô có giá trị `x`:

# ```
# f[j+1] = min(
#     min(f[j], f[j+1]) + x,   # đi bình thường
#     suf_min_f[x]             # teleport
# )
# ```

# ### Ý nghĩa:

# * `min(f[j], f[j+1]) + x` → đi từ trái hoặc trên
# * `suf_min_f[x]` → dùng teleport (không cộng x)

# ---

# ## Vì sao cần lặp `k + 1` lần?

# * Mỗi vòng lặp cho phép **thêm 1 lần teleport**
# * Sau mỗi vòng:

#   * Cập nhật lại khả năng teleport tốt hơn
# * Nếu không cải thiện nữa → **dừng sớm**

# ---

# # 2️⃣ Code Python (đã chú thích chi tiết)

# ```python
from typing import List
from math import inf

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        n = len(grid[0])

        # mx = giá trị lớn nhất trong grid
        mx = max(map(max, grid))

        """
        suf_min_f[x]:
        chi phí nhỏ nhất trong số các ô có giá trị >= x
        (dùng cho teleport)
        """
        suf_min_f = [inf] * (mx + 2)

        # Lặp theo số teleport đã dùng
        for _ in range(k + 1):

            """
            min_f[x]:
            chi phí nhỏ nhất khi đứng ở ô có giá trị = x
            trong vòng lặp hiện tại
            """
            min_f = [inf] * (mx + 1)

            """
            f[j]:
            chi phí nhỏ nhất để đi tới cột j
            của hàng hiện tại (DP cuộn theo hàng)
            """
            f = [inf] * (n + 1)

            # Trick khởi tạo ô (0,0)
            f[1] = -grid[0][0]

            # Duyệt từng ô trong grid
            for row in grid:
                for j, x in enumerate(row):

                    # Lấy min từ trái (f[j]) hoặc trên (f[j+1])
                    v = f[j + 1]
                    if f[j] < v:
                        v = f[j]

                    # Đi bình thường: cộng cost ô hiện tại
                    v += x

                    # Teleport: không cộng cost, dùng kết quả tốt nhất trước đó
                    if suf_min_f[x] < v:
                        v = suf_min_f[x]

                    # Cập nhật DP
                    f[j + 1] = v

                    # Ghi nhận chi phí nhỏ nhất tại ô có giá trị x
                    if f[j + 1] < min_f[x]:
                        min_f[x] = f[j + 1]

            # Lưu trạng thái cũ để kiểm tra dừng sớm
            tmp = suf_min_f.copy()

            # Cập nhật suffix minimum
            for i in range(mx, -1, -1):
                v = suf_min_f[i + 1]
                if min_f[i] < v:
                    v = min_f[i]
                suf_min_f[i] = v

            # Nếu không cải thiện được nữa thì dừng
            if suf_min_f == tmp:
                break

        # Kết quả là chi phí nhỏ nhất tới ô cuối
        return f[n]
# ```

# ---

# # 3️⃣ Tóm tắt 1 câu để nhớ

# > **DP theo số teleport, mỗi ô chọn đi thường hoặc teleport, teleport được tối ưu bằng suffix minimum theo giá trị ô.**

# ---

# Nếu bạn muốn, mình có thể:

# * Chạy **tay 1 ví dụ nhỏ 3×3**
# * Viết **pseudocode để học thuộc**
# * So sánh với **Dijkstra + state (i, j, t)**

# 👉 Chỉ cần nói bạn đang **học để thi hay để hiểu sâu** nhé 👌

# import java.util.*;

# public class b162 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {

#         // Nhập số hàng, số cột, số teleport
#         int m = sc.nextInt();
#         int n = sc.nextInt();
#         int k = sc.nextInt();

#         // Nhập grid
#         int[][] grid = new int[m][n];
#         for (int i = 0; i < m; i++) {
#             for (int j = 0; j < n; j++) {
#                 grid[i][j] = sc.nextInt();
#             }
#         }

#         int result = minCost(grid, k);

#         // In kết quả
#         System.out.println(result);

#         sc.close();

#     }

#     /**
#      * Hàm chính giải bài toán
#      * grid: ma trận chi phí
#      * k: số lần teleport tối đa
#      */
#     public static int minCost(int[][] grid, int k) {
#         int m = grid.length;
#         int n = grid[0].length;

#         // Nếu có ít nhất 1 teleport và giá trị ô đầu >= ô cuối
#         // => có thể teleport trực tiếp, cost = 0
#         if (k > 0 && grid[0][0] >= grid[m - 1][n - 1]) {
#             return 0;
#         }

#         // mx = giá trị lớn nhất trong grid
#         int mx = 0;
#         for (int[] row : grid) {
#             for (int x : row) {
#                 mx = Math.max(mx, x);
#             }
#         }

#         /*
#          * sufMinF[x]: chi phí nhỏ nhất trong số các ô
#          * có giá trị >= x (dùng cho teleport)
#          */
#         int[] sufMinF = new int[mx + 2];
#         Arrays.fill(sufMinF, Integer.MAX_VALUE);

#         /*
#          * minF[x]: chi phí nhỏ nhất khi đứng tại ô có giá trị = x
#          * trong lần duyệt hiện tại
#          */
#         int[] minF = new int[mx + 1];

#         /*
#          * f[j]: chi phí nhỏ nhất để đi tới cột j
#          * của hàng hiện tại (DP cuộn theo hàng)
#          */
#         int[] f = new int[n + 1];

#         // Lặp theo số teleport đã dùng
#         for (int t = 0; t <= k; t++) {

#             // Reset mảng cho vòng teleport mới
#             Arrays.fill(minF, Integer.MAX_VALUE);
#             Arrays.fill(f, Integer.MAX_VALUE / 2);

#             // Trick: khởi tạo ô (0,0)
#             f[1] = -grid[0][0];

#             // Duyệt từng ô trong grid
#             for (int[] row : grid) {
#                 for (int j = 0; j < n; j++) {
#                     int x = row[j];

#                     /*
#                      * 2 lựa chọn:
#                      * 1. Đi bình thường (từ trái hoặc trên)
#                      * 2. Teleport (dùng sufMinF)
#                      */
#                     f[j + 1] = Math.min(
#                             Math.min(f[j], f[j + 1]) + x,
#                             sufMinF[x]);

#                     // Ghi nhận chi phí nhỏ nhất tại ô có giá trị x
#                     minF[x] = Math.min(minF[x], f[j + 1]);
#                 }
#             }

#             // Cập nhật suffix minimum cho teleport vòng sau
#             boolean done = true;
#             for (int i = mx; i >= 0; i--) {
#                 int mn = Math.min(sufMinF[i + 1], minF[i]);
#                 if (mn < sufMinF[i]) {
#                     sufMinF[i] = mn;
#                     done = false;
#                 }
#             }

#             // Nếu không cải thiện được nữa thì dừng sớm
#             if (done) {
#                 break;
#             }
#         }

#         // Kết quả là chi phí nhỏ nhất tới ô cuối
#         return f[n];
#     }

# }

# // ## 1. Ý nghĩa bài toán (ngầm trong code)

# // * `grid[m][n]`: mỗi ô có giá trị `x`
# // * Đi từ `(0,0)` → `(m-1,n-1)`
# // * **Cost = tổng giá trị các ô đi qua**
# // * Được dùng **tối đa `k` teleport**
# // * Teleport cho phép:

# // > **Bỏ qua chi phí của một đoạn**, nhưng chỉ áp dụng khi gặp ô có giá trị **≥
# // một ngưỡng nào đó**

# // 👉 Bài toán thực chất là:

# // > **Tìm tổng cost nhỏ nhất với tối đa k lần “bỏ qua thông minh”**

# // ---

# // ## 2. Ý tưởng lớn của thuật toán

# // Thuật toán dùng **Dynamic Programming theo số teleport đã dùng**
# // và một kỹ thuật **tối ưu bằng suffix minimum**

# // ### Tư duy cốt lõi:

# // * `t = số teleport đã dùng`
# // * Mỗi vòng `t`:

# // * Tính **chi phí nhỏ nhất để đi tới mọi ô**
# // * Cho phép dùng teleport **t lần**
# // * Khi dùng teleport:

# // * Không cộng cost ô hiện tại
# // * Mà lấy từ **giá trị tốt nhất đã lưu**

# // ---

# // ## 3. Giải thích từng biến quan trọng

# // ### 🔹 `mx`

# // ```java
# // int mx = max value trong grid
# // ```

# // 👉 Dùng để **index theo giá trị ô**
# // (vì teleport phụ thuộc vào giá trị `x`)

# // ---

# // ### 🔹 `f[j]`

# // ```java
# // f[j] = chi phí nhỏ nhất để tới cột j ở hàng hiện tại
# // ```

# // * Chỉ lưu **1 hàng** → tối ưu bộ nhớ
# // * Giống DP rolling array

# // ---

# // ### 🔹 `minF[x]`

# // ```java
# // minF[x] = chi phí nhỏ nhất khi đứng ở ô có giá trị = x
# // ```

# // 👉 Dùng để **chuẩn bị cho teleport**

# // ---

# // ### 🔹 `sufMinF[x]`

# // ```java
# // sufMinF[x] = min chi phí với ô có giá trị ≥ x
# // ```

# // 📌 Đây là **trái tim của teleport**

# // Teleport nghĩa là:

# // > Nếu ô hiện tại có giá trị `x`,
# // > ta có thể lấy **best cost của mọi ô ≥ x** trong lần teleport trước

# // ---

# // ## 4. Khởi tạo ban đầu

# // ```java
# // f[1] = -grid[0][0];
# // ```

# // ❓ Tại sao là số âm?

# // 👉 Vì khi cập nhật:

# // ```java
# // f[j+1] = min(...) + x
# // ```

# // → cộng lại đúng `grid[0][0]`
# // ➡️ Trick để tránh xử lý riêng ô đầu

# // ---

# // ## 5. Công thức DP cốt lõi (quan trọng nhất)

# // ```java
# // f[j + 1] = min(
# // min(f[j], f[j + 1]) + x, // đi bình thường
# // sufMinF[x] // teleport
# // );
# // ```

# // ### 🔹 Trường hợp 1: Đi bình thường

# // ```java
# // min(f[j], f[j+1]) + x
# // ```

# // * Từ trái sang
# // * Hoặc từ trên xuống
# // * Cộng cost ô hiện tại

# // ---

# // ### 🔹 Trường hợp 2: Teleport

# // ```java
# // sufMinF[x]
# // ```

# // * Nếu đã dùng teleport trước đó
# // * Có thể **nhảy tới đây**
# // * Không cộng cost ô hiện tại

# // ---

# // 👉 Lấy **min của 2 cách**

# // ---

# // ## 6. Cập nhật dữ liệu cho vòng teleport tiếp theo

# // Sau khi duyệt hết grid:

# // ```java
# // minF[x] = min(minF[x], f[j+1]);
# // ```

# // → Ghi nhận:

# // > “Nếu đứng ở ô có giá trị `x`, chi phí nhỏ nhất là bao nhiêu?”

# // ---

# // ### Tạo suffix minimum

# // ```java
# // for (int i = mx; i >= 0; i--) {
# // sufMinF[i] = min(sufMinF[i+1], minF[i]);
# // }
# // ```

# // 👉 Giúp truy vấn:

# // ```
# // min cost của mọi ô có value ≥ x
# // ```

# // trong **O(1)**

# // ---

# // ## 7. Vòng lặp theo số teleport

# // ```java
# // for (int t = 0; t <= k; t++)
# // ```

# // * Mỗi vòng:

# // * Cho phép thêm **1 teleport**
# // * Nếu `sufMinF` **không thay đổi**

# // ```java
# // if (done) break;
# // ```

# // 👉 Không thể tối ưu thêm → dừng sớm

# // ---

# // ## 8. Kết quả cuối

# // ```java
# // return f[n];
# // ```

# // 👉 Chi phí nhỏ nhất để tới **ô cuối cùng**

# // ---

# // ## 9. Độ phức tạp

# // * Thời gian:

# // ```
# // O(k × m × n + k × mx)
# // ```

# // * Không cần Dijkstra
# // * Nhanh nhờ:

# // * Rolling DP
# // * Suffix minimum

# // ---

# // ## 10. Tóm tắt 1 câu (rất quan trọng)

# // > **Thuật toán dùng DP theo số teleport,
# // > mỗi ô chọn giữa đi thường hoặc teleport,
# // > teleport được tối ưu bằng suffix minimum theo giá trị ô.**

# // ---

# // Nếu bạn muốn, mình có thể:

# // * Vẽ **bảng DP minh họa từng bước**
# // * Giải thích bằng **ví dụ grid nhỏ 3×3**
# // * So sánh với **Dijkstra truyền thống**

# // 👉 Chỉ cần nói bạn muốn **kiểu nào** 😄

# // (Chưa cần code, chỉ tập trung **hiểu đề**)

# // ---

# // ## 1. Bài toán đang nói về cái gì?

# // Bạn có một **bản đồ / đồ thị / lưới** (tùy đề cụ thể), trong đó:

# // * Có **điểm bắt đầu** `S`
# // * Có **điểm kết thúc** `T`
# // * Mỗi bước di chuyển sẽ **tốn chi phí**
# // * Ngoài các bước đi **bình thường**, bạn còn có thể dùng **teleport (dịch
# // chuyển tức thời)**

# // 👉 **Mục tiêu:**

# // > Tìm **chi phí nhỏ nhất** để đi từ `S` đến `T`.

# // ---

# // ## 2. Di chuyển bình thường là gì?

# // Tùy đề, thường sẽ là:

# // * Đi sang ô **trên / dưới / trái / phải**
# // * Hoặc đi theo **cạnh của đồ thị**

# // Mỗi lần đi:

# // * Tốn **1 cost**
# // * Hoặc tốn cost được cho sẵn

# // 📌 Đây là phần **quen thuộc** như các bài *Shortest Path* (Dijkstra / BFS).

# // ---

# // ## 3. Teleportation là gì?

# // Teleport = **nhảy ngay lập tức** từ một vị trí sang vị trí khác.

# // Có thể có các dạng sau (rất hay gặp):

# // ### 🔹 Dạng 1: Teleport cố định

# // * Từ `(x1, y1)` → `(x2, y2)`
# // * Mất **cost = k**

# // Ví dụ:

# // ```
# // Teleport từ (1,1) → (5,5) với cost = 3
# // ```

# // ---

# // ### 🔹 Dạng 2: Teleport theo nhóm

# // * Các điểm có cùng màu / cùng ký hiệu
# // * Có thể teleport giữa **bất kỳ 2 điểm trong nhóm đó**

# // Ví dụ:

# // ```
# // Tất cả ô ký hiệu 'A' có thể teleport cho nhau
# // ```

# // ---

# // ### 🔹 Dạng 3: Teleport có giới hạn

# // * Chỉ được dùng **tối đa K lần**
# // * Hoặc mỗi teleport có chi phí khác nhau

# // ---

# // ## 4. Vì sao bài này khó hơn đường đi ngắn nhất bình thường?

# // 👉 Vì:

# // * Không chỉ đi từng bước
# // * Mà còn có **cạnh đặc biệt (teleport)**
# // * Teleport có thể:

# // * Rẻ hơn đi bộ
# // * Hoặc giúp “nhảy cóc” qua đoạn rất dài

# // ➡️ Không thể dùng BFS đơn giản
# // ➡️ Thường phải dùng **Dijkstra** hoặc **State Graph**

# // ---

# // ## 5. Mô hình hóa bài toán (rất quan trọng)

# // Ta coi mỗi **vị trí** là một **node**

# // ### Các cạnh:

# // 1. **Cạnh thường**

# // * Đi sang ô bên cạnh
# // * Cost = 1 (hoặc cho trước)

# // 2. **Cạnh teleport**

# // * Từ node A → node B
# // * Cost = teleport_cost

# // ➡️ Bài toán trở thành:

# // > **Shortest Path trên đồ thị có cạnh thường + cạnh teleport**

# // ---

# // ## 6. Nếu teleport bị giới hạn số lần thì sao?

# // Lúc này, trạng thái không còn là:

# // ```
# // (node)
# // ```

# // Mà là:

# // ```
# // (node, số teleport đã dùng)
# // ```

# // 📌 Khi đó:

# // * Mỗi trạng thái là **1 node mới**
# // * Dùng **Dijkstra đa chiều**

# // ---

# // ## 7. Tóm tắt ngắn gọn

# // 📌 **Minimum Cost Path with Teleportations** =

# // * Tìm đường đi **rẻ nhất**
# // * Từ `S` đến `T`
# // * Có:

# // * Di chuyển bình thường
# // * * Teleport (dịch chuyển đặc biệt)

# // 📌 **Ý tưởng cốt lõi**:

# // * Mô hình hóa thành đồ thị
# // * Thêm các cạnh teleport
# // * Dùng **Dijkstra / BFS mở rộng trạng thái**

# // ---

# // Nếu bạn muốn, bạn có thể:

# // * Gửi **nguyên đề bài**
# // * Hoặc nói rõ: **dạng lưới hay đồ thị, teleport kiểu nào**

# // 👉 Mình sẽ giải thích **đúng sát đề bạn đang học / thi** 💯
