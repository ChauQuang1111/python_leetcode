# // // 407. Trapping Rain Water II(03/10/2025)
# Rất hay 👍. Bạn đã viết lời giải bằng **BFS + Min-Heap** cho bài **Trapping Rain Water II (LeetCode 407)**. Mình sẽ giải thích chi tiết thuật toán và thêm chú thích vào code của bạn.

# ---

# ## 🔑 Ý tưởng thuật toán:

# 1. **Nước luôn bị giữ lại bởi các rào chắn thấp nhất ở biên ngoài.**
#    → Vì thế ta bắt đầu từ **biên (boundary)** và tiến dần vào trong.

# 2. **Dùng min-heap (priority queue):**

#    * Luôn lấy ô có độ cao nhỏ nhất ở biên hiện tại.
#    * Điều này đảm bảo khi ta duyệt vào trong, ta biết mực "rào chắn" thấp nhất bao quanh nó.

# 3. **BFS mở rộng:**

#    * Lấy ô thấp nhất từ heap ra.
#    * Duyệt các ô kề.
#    * Nếu ô kề thấp hơn rào chắn hiện tại, thì **nước sẽ bị giữ lại**.
#    * Đưa ô kề vào heap với chiều cao = `max(rào chắn, chiều cao ô kề)` (vì nước có thể dâng lên bằng rào chắn).

# 4. **Lặp lại cho đến khi heap rỗng.**

# ---

# ## 📌 Code có chú thích:

# ```python

import heapq
from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        heap = []

        m = len(heightMap)
        n = len(heightMap[0])

        # visited[i][j] = True nếu ô (i,j) đã xử lý
        visited = [[False for _ in range(n)] for _ in range(m)]

        # 1. Đưa tất cả các ô biên vào heap trước (chúng là "rào chắn" ban đầu)
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        # 4 hướng đi (trái, phải, trên, dưới)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        trapped_water = 0

        # 2. BFS mở rộng từ biên vào trong
        while heap:
            height, i, j = heapq.heappop(heap)  # ô có chiều cao nhỏ nhất hiện tại

            # 3. Duyệt các ô kề
            for dx, dy in directions:
                newX, newY = i + dx, j + dy
                # chỉ xét các ô trong phạm vi và chưa được thăm
                if 0 <= newX < m and 0 <= newY < n and not visited[newX][newY]:
                    visited[newX][newY] = True
                    cell_height = heightMap[newX][newY]

                    if cell_height < height:
                        # Nếu ô thấp hơn rào chắn → giữ nước
                        trapped_water += height - cell_height
                        # Đưa ô này vào heap với chiều cao bằng rào chắn hiện tại
                        heapq.heappush(heap, (height, newX, newY))
                    else:
                        # Nếu ô cao hơn → nó trở thành rào chắn mới
                        heapq.heappush(heap, (cell_height, newX, newY))

        return trapped_water
# ```

# ---

# ## 🔎 Ví dụ minh họa:

# ```
# heightMap = [
#   [1,4,3,1,3,2],
#   [3,2,1,3,2,4],
#   [2,3,3,2,3,1]
# ]
# ```

# * Các biên (1,4,3,1,3,2,...) được đưa vào heap.
# * Bắt đầu từ ô biên thấp nhất → mở rộng vào trong.
# * Khi gặp ô (1,2)=1, nó bị bao quanh bởi rào chắn cao hơn (min=3),
#   → giữ được `3-1 = 2` đơn vị nước.

# ---

# 👉 Tóm lại:

# * **Heap đảm bảo ta luôn mở rộng từ ô thấp nhất.**
# * **Nước giữ được phụ thuộc vào rào chắn thấp nhất.**
# * **Khi gặp ô thấp hơn rào chắn, nước được cộng dồn.**

# ---

# Bạn có muốn mình vẽ **hình minh họa trực quan (bằng ASCII hoặc ảnh)** cho ví dụ nhỏ để dễ hình dung hơn cách nước bị giữ lại không?

# import java.util.*;

# public class b56 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int m = sc.nextInt();
#         int n = sc.nextInt();

#         int[][] heightMap = new int[m][n];
#         for (int i = 0; i < m; i++) {
#             for (int j = 0; j < n; j++) {
#                 heightMap[i][j] = sc.nextInt();
#             }
#         }

#         int result = trapRainWater(heightMap);
#         System.out.println(result);

#         sc.close();
#     }

#     public static int trapRainWater(int[][] heightMap) {
#         int m = heightMap.length; // số hàng
#         int n = heightMap[0].length; // số cột

#         // Mảng vols lưu lại "mực nước có thể chứa" tại từng ô
#         // Ban đầu gán = heightMap (nghĩa là chưa có nước thêm)
#         int[][] vols = new int[m][n];
#         for (int i = 0; i < m; i++) {
#             for (int j = 0; j < n; j++) {
#                 vols[i][j] = heightMap[i][j];
#             }
#         }

#         boolean upt = true; // cờ kiểm tra có cập nhật mực nước không
#         boolean init = true; // lần quét đầu tiên cho phép cập nhật hết

#         // Lặp lại cho đến khi không còn cập nhật nữa
#         while (upt) {
#             upt = false;

#             // Quét từ trên trái xuống dưới phải
#             for (int i = 1; i < m - 1; i++) {
#                 for (int j = 1; j < n - 1; j++) {
#                     // Mực nước tại ô (i,j) không thể thấp hơn chiều cao gốc heightMap[i][j]
#                     // và cũng bị giới hạn bởi nước từ phía trên (i-1,j) hoặc bên trái (i,j-1)
#                     int val = Math.max(heightMap[i][j],
#                             Math.min(vols[i - 1][j], vols[i][j - 1]));

#                     // Nếu là lần đầu init, hoặc có thể hạ thấp mức nước hiện tại
#                     if (init || vols[i][j] > val) {
#                         vols[i][j] = val; // cập nhật mực nước tại ô (i,j)
#                         upt = true; // đánh dấu có thay đổi
#                     }
#                 }
#             }
#             init = false; // sau lần quét đầu thì tắt init

#             // Quét từ dưới phải lên trên trái
#             for (int i = m - 2; i >= 1; i--) {
#                 for (int j = n - 2; j >= 1; j--) {
#                     // Tương tự nhưng xét hàng xóm phía dưới (i+1,j) và phải (i,j+1)
#                     int val = Math.max(heightMap[i][j],
#                             Math.min(vols[i + 1][j], vols[i][j + 1]));

#                     // Nếu mức nước hiện tại cao hơn mức hợp lý, hạ xuống
#                     if (vols[i][j] > val) {
#                         vols[i][j] = val;
#                         upt = true;
#                     }
#                 }
#             }
#         }

#         // Tính tổng lượng nước = (mực nước - chiều cao đất)
#         int res = 0;
#         for (int i = 1; i < m - 1; i++) {
#             for (int j = 1; j < n - 1; j++) {
#                 if (vols[i][j] > heightMap[i][j]) {
#                     res += vols[i][j] - heightMap[i][j];
#                 }
#             }
#         }
#         return res;
#     }

# }

# // Ok bài**407.
# // Trapping Rain
# // Water II**
# // khá hay😃
# // Nó là
# // phiên bản

# // nâng cao (2D) của bài **Trapping Rain Water (1D)**.

# // ---

# // ## 🚰 Đề bài tóm tắt

# // * Cho một ma trận `heightMap` (m × n), mỗi ô là chiều cao cột tường.
# // * Nước mưa có thể bị giữ lại trong các “hố”

# // bên trong (giữa các tường cao).
# // * Hãy tính tổng lượng nước tối đa có thể giữ.

# // ---

# // ## 💡 Ý tưởng thuật toán

# // Nếu bạn đã học bài **Trapping Rain Water (1D)** thì cách tư duy khá giống:

# // * Ở 1D: để biết nước tại 1 vị trí, ta cần biết **max chiều cao bên trái** và
# // **max chiều cao bên phải**.
# // * Ở 2D: tại 1 ô `(i, j)`, lượng nước giữ được phụ thuộc vào **tường thấp nhất
# // bao quanh nó**.

# // ---

# // ## 🔑 Thuật toán

# // chi tiết (dùng BFS + Min-Heap)

# // 1. **Khởi tạo hàng rào**:

# // * Nước chỉ có thể bị giữ bên trong, không thể vượt qua biên.
# // * Thêm tất cả các

# // ô biên (boundary cells) vào **min-heap**, coi như bức tường bao ngoài.

# // 2. **BFS mở rộng vào trong**:

# // * Luôn lấy ra ô **thấp nhất**

# // từ heap (gọi là `cell`).
# // * Duyệt 4 hướng (lên, xuống, trái, phải).
# // * Nếu gặp ô láng giềng `next`:

# // * Nếu `height[next] < height[cell]` → chỗ này có thể chứa nước:

# // ```
# // water += height[cell] - height[next]
# // ```
# // * Cập nhật chiều cao của `next`:

# // ```
# // newHeight = max(height[next], height[cell])
# // ```

# // (vì nước lấp đầy đến tường thấp nhất).
# // * Thêm `next` vào heap với `newHeight`.

# // 3. **Lặp đến khi heap rỗng**:

# // * Khi duyệt xong tất cả, tổng `water` chính là kết quả.

# // ---

# // ## 📊 Độ phức tạp

# // * Sử dụng min-heap chứa tối đa `m * n` phần tử.
# // * Mỗi ô vào heap đúng 1 lần.
# // * Độ phức tạp:

# // * **Thời gian**: `O(m * n * log(m*n))`
# // * **Không gian**: `O(m * n)`

# // ---

# // ## 🌊 Ví dụ

# // ```
# // heightMap =
# // [
# // [1,4,3,1,3,2],
# // [3,2,1,3,2,4],
# // [2,3,3,2,3,1]
# // ]
# // ```

# // * Ban đầu lấy biên làm rào chắn.
# // * Từ biên thấp nhất, lấp dần vào trong.
# // * Kết quả cuối cùng = **4 đơn vị nước**.

# // ---

# // 👉 Bạn có muốn mình viết hẳn code Java có chú thích chi tiết cho thuật toán
# // này không?
# // Ok 👍 để mình giải thích thuật toán của bạn nhé. Đây là một cách giải bài
# // **Trapping Rain

# // Water II (LeetCode 407)**.

# // ---

# // ## Ý tưởng thuật toán

# // * Bài toán yêu cầu tính **lượng nước mưa bị giữ lại** trên một bản đồ 2D
# // `heightMap`.
# // * Nước bị giữ lại khi **xung quanh ô đó cao hơn** và nước không thoát ra
# // ngoài biên.
# // * Thuật toán của bạn dùng cách **lặp cập nhật (relaxation)** để tìm ra mực
# // nước tối đa có thể giữ tại mỗi ô.

# // ---

# // ## Các bước chính

# // ### 1. Khởi tạo

# // ```java
# // int[][] vols = new int[m][n];
# // for (int i = 0; i < m; i++) {
# // for (int j = 0; j < n; j++) {
# // vols[i][j] = heightMap[i][j];
# // }
# // }
# // ```

# // 👉 `vols[i][j]` ban đầu lưu **mực nước tối đa** tại ô `(i, j)` = chiều cao
# // gốc.

# // ---

# // ### 2. Cập nhật

# // dần dần (relaxation)

# // ```java
# // boolean upt = true;
# // boolean init = true;
# // while (upt) {
# // upt = false;
# // // Quét từ trên trái xuống dưới phải
# // for (int i = 1; i < m - 1; i++) {
# // for (int j = 1; j < n - 1; j++) {
# // int val = Math.max(heightMap[i][j],
# // Math.min(vols[i - 1][j], vols[i][j - 1]));
# // if (init || vols[i][j] > val) {
# // vols[i][j] = val;
# // upt = true;
# // }
# // }
# // }
# // init = false;

# // // Quét từ dưới phải lên trên trái
# // for (int i = m - 2; i >= 1; i--) {
# // for (int j = n - 2; j >= 1; j--) {
# // int val = Math.max(heightMap[i][j],
# // Math.min(vols[i + 1][j], vols[i][j + 1]));
# // if (vols[i][j] > val) {
# // vols[i][j] = val;
# // upt = true;
# // }
# // }
# // }
# // }
# // ```

# // 👉 Ý nghĩa:

# // * `vols[i][j]` = mực nước cao nhất có thể giữ được tại ô `(i, j)`.
# // * Khi quét, bạn lấy:

# // * `heightMap[i][j]`: mặt đất thật.
# // * `Math.min(vols[x][y], vols[u][v])`: giới hạn từ ô lân cận.
# // * `Math.max(...)`: đảm bảo mực nước ≥ mặt đất.
# // * Lặp tới khi **không còn cập nhật** (`upt == false`).

# // Nói cách khác, bạn đang **lan truyền ràng buộc về mực nước từ biên vào
# // trong**.

# // ---

# // ### 3. Tính kết quả

# // ```java
# // int res = 0;
# // for (int i = 1; i < m - 1; i++) {
# // for (int j = 1; j < n - 1; j++) {
# // if (vols[i][j] > heightMap[i][j])
# // res += vols[i][j] - heightMap[i][j];
# // }
# // }
# // return res;
# // ```

# // 👉 Với mỗi ô, lượng nước giữ được = `vols[i][j] - heightMap[i][j]`.

# // ---

# // ## Độ phức tạp

# // * **Thời gian**:
# // Vòng `while` có thể chạy nhiều

# // lần (đến khi không thay đổi nữa).
# // Mỗi lần quét mất `O(m*n)`.
# // → Trường hợp xấu có thể khá chậm (gần `O((m*n)^2)`).

# // * **Bộ nhớ**: `O(m*n)` cho mảng `vols`.

# // ---

# // ## So sánh với cách tối ưu

# // Thuật toán chuẩn của bài này dùng **Priority Queue (min-heap)**:

# // * Bắt đầu

# // từ biên (biên không giữ được nước).
# // * Mở rộng vào trong bằng BFS/heap, luôn lấy ô thấp nhất.
# // * Đảm bảo chạy **O(m*n log(m*n))**.

# // Thuật toán của bạn tuy chậm hơn nhưng **trực quan**:

# // * Nó giống như việc **giả sử mực nước cao**, rồi dần dần “xả” xuống khi thấy
# // thấp hơn từ biên → cuối cùng tìm được mức ổn định.

# // ---

# // 👉 Tóm lại:
# // Thuật toán = **iterative relaxation**: cập nhật mực nước từ biên vào trong,
# // lặp cho đến khi ổn định.

# // ---

# // Bạn có muốn mình viết lại **cách giải bằng Priority Queue** (tối ưu hơn,
# // thường gặp trong LeetCode) để bạn so sánh không?
