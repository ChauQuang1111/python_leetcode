# # // // Bài **“Get Biggest Three Rhombus Sums in a Grid”(16/03/2026)

# Bài này thuộc bài Get Biggest Three Rhombus Sums in a Grid.
# Thuật toán Python bạn đưa **khó hơn version Java** vì nó dùng **prefix sum theo đường chéo** để tối ưu.

# Mình sẽ giải thích theo 3 phần:

# 1️⃣ Ý tưởng thuật toán
# 2️⃣ Prefix sum đường chéo là gì
# 3️⃣ Code có chú thích chi tiết

# ---

# # 1. Ý tưởng thuật toán

# Mục tiêu:

# ```
# Tìm 3 rhombus sum lớn nhất (khác nhau)
# ```

# Rhombus:

# ```
#       *
#     *   *
#   *       *
#     *   *
#       *
# ```

# Chỉ cộng **viền (border)**.

# ---

# ## Cách làm

# ### Bước 1: Tính prefix sum theo đường chéo

# Ta tạo 2 mảng:

# ```
# diagonalPrefixSum
# antiDiagonalPrefixSum
# ```

# Ví dụ grid:

# ```
# 1 2 3
# 4 5 6
# 7 8 9
# ```

# Diagonal prefix:

# ```
# 1
#   5
#     9
# ```

# Anti diagonal:

# ```
# 3
#   5
# 7
# ```

# Nhờ prefix sum ta tính **tổng đường chéo trong O(1)**.

# ---

# ### Bước 2: Duyệt mọi vị trí làm đáy rhombus

# ```
# for r
#    for c
# ```

# coi `(r,c)` là **đỉnh dưới** của rhombus.

# ---

# ### Bước 3: Tính kích thước lớn nhất

# Rhombus không được vượt grid.

# ```
# largest_horizontal = min(c, n-1-c)
# largest_vertical = r//2
# largest = min(...)
# ```

# ---

# ### Bước 4: Tính sum bằng prefix sum

# Thay vì đi từng cạnh như Java:

# ```
# O(k)
# ```

# ở đây dùng prefix:

# ```
# O(1)
# ```

# ---

# ### Bước 5: dùng heap giữ top 3

# Python dùng:

# ```
# heapq
# ```

# để giữ **3 giá trị lớn nhất**.

# ---

# # 2. Hình minh họa rhombus

# Nếu `(r,c)` là đáy:

# ```
#         top
#       /     \
#    left     right
#       \     /
#       (r,c)
# ```

# tọa độ:

# ```
# top = (r-2k, c)
# left = (r-k, c-k)
# right = (r-k, c+k)
# bottom = (r,c)
# ```

# ---

# # 3. Code có chú thích chi tiết

# ```python
import heapq
from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:

        # kích thước grid
        m, n = len(grid), len(grid[0])

        # prefix sum theo đường chéo chính
        diagonalPrefixSum = [[0] * (n + 2) for _ in range(m + 2)]

        # prefix sum theo đường chéo phụ
        antiDiagonalPrefixSum = [[0] * (n + 2) for _ in range(m + 2)]

        # heap để giữ 3 số lớn nhất
        ans = []

        # -------------------------
        # BƯỚC 1: TÍNH PREFIX SUM
        # -------------------------
        for r in range(m):
            for c in range(n):

                ur, uc = r + 1, c + 1  # chuyển sang index 1

                # prefix sum đường chéo chính
                diagonalPrefixSum[ur][uc] = (
                    grid[r][c] + diagonalPrefixSum[ur - 1][uc - 1]
                )

                # prefix sum đường chéo phụ
                antiDiagonalPrefixSum[ur][uc] = (
                    grid[r][c] + antiDiagonalPrefixSum[ur - 1][uc + 1]
                )

        # -------------------------
        # BƯỚC 2: DUYỆT TỪNG ĐIỂM
        # -------------------------
        for r in range(m):
            for c in range(n):

                # kích thước rhombus tối đa theo chiều ngang
                largest_horizontal = min(c, n - 1 - c)

                # kích thước rhombus tối đa theo chiều dọc
                largest_vertical = r // 2

                # kích thước rhombus tối đa
                largest = min(largest_horizontal, largest_vertical)

                ur, uc = r + 1, c + 1

                # chỉ cần thử tối đa 3 kích thước
                for _ in range(3):

                    if largest < 0:
                        break

                    # rhombus size = 0
                    elif largest == 0:
                        rhombus = grid[r][c]

                    else:
                        rhombus = 0

                        # cộng 4 cạnh bằng prefix sum
                        rhombus += diagonalPrefixSum[ur][uc]
                        rhombus += antiDiagonalPrefixSum[ur][uc]
                        rhombus += diagonalPrefixSum[ur - largest][uc + largest]
                        rhombus += antiDiagonalPrefixSum[ur - largest][uc - largest]

                        # trừ phần dư
                        rhombus -= diagonalPrefixSum[ur - largest - 1][uc - largest - 1]
                        rhombus -= antiDiagonalPrefixSum[ur - largest - 1][uc + largest + 1]
                        rhombus -= diagonalPrefixSum[ur - 2 * largest - 1][uc - 1]
                        rhombus -= antiDiagonalPrefixSum[ur - 2 * largest - 1][uc + 1]

                        # trừ 4 đỉnh vì bị tính 2 lần
                        rhombus -= grid[r][c]
                        rhombus -= grid[r - largest][c - largest]
                        rhombus -= grid[r - 2 * largest][c]
                        rhombus -= grid[r - largest][c + largest]

                    # -------------------------
                    # BƯỚC 3: CẬP NHẬT TOP 3
                    # -------------------------
                    if rhombus not in ans:

                        if len(ans) < 3:
                            heapq.heappush(ans, rhombus)
                        else:
                            heapq.heappushpop(ans, rhombus)

                    largest -= 1

        return sorted(ans, reverse=True)
# ```

# ---

# # 4. Độ phức tạp

# Version Java:

# ```
# O(n^4)
# ```

# Version Python này:

# ```
# O(n^3)
# ```

# vì mỗi rhombus sum tính trong:

# ```
# O(1)
# ```

# nhờ prefix sum.

# ---

# 5. Điểm khó nhất của bài

# 90% người học không hiểu:

# ```
# prefix sum đường chéo
# ```

# và công thức:

# ```
# rhombus += diagonalPrefixSum...
# ```

# Nếu bạn muốn, mình có thể vẽ **diagram cực dễ hiểu** để bạn hiểu ngay:

# * vì sao cần **2 prefix sum**
# * cách **tính 4 cạnh rhombus trong O(1)**
# * cách bài này từ **O(n⁴) → O(n³)**.



# import java.util.*;

# public class b218 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         // nhập số hàng và cột
#         int m = sc.nextInt();
#         int n = sc.nextInt();

#         int[][] grid = new int[m][n];

#         // nhập ma trận
#         for (int i = 0; i < m; i++) {
#             for (int j = 0; j < n; j++) {
#                 grid[i][j] = sc.nextInt();
#             }
#         }

#         // gọi thuật toán

#         int[] result = getBiggestThree(grid);

#         // in kết quả
#         for (int x : result) {
#             System.out.print(x + " ");
#         }

#         sc.close();

#     }

#     // 3 biến lưu 3 tổng rhombus lớn nhất (khác nhau)
#     public static int first = -1; // lớn nhất
#     public static int second = -1; // lớn thứ 2
#     public static int third = -1; // lớn thứ 3

#     public static int[] getBiggestThree(int[][] grid) {

#         int m = grid.length; // số hàng
#         int n = grid[0].length; // số cột

#         // Bước 1: rhombus size = 0 (chỉ 1 ô)
#         // mỗi ô tự nó cũng là 1 rhombus
#         for (int i = 0; i < m; i++) {
#             for (int j = 0; j < n; j++) {
#                 add(grid[i][j]); // thêm giá trị vào top 3
#             }
#         }

#         // Bước 2: duyệt từng ô làm tâm rhombus
#         for (int i = 0; i < m; i++) {
#             for (int j = 0; j < n; j++) {

#                 // k = "bán kính" rhombus
#                 // rhombus phải nằm trong grid
#                 for (int k = 1; i - k >= 0 && i + k < m && j - k >= 0 && j + k < n; k++) {

#                     int sum = 0;

#                     // Cạnh 1: từ đỉnh trên -> phải
#                     for (int d = 0; d < k; d++) {
#                         sum += grid[i - k + d][j + d];
#                     }

#                     // Cạnh 2: từ phải -> xuống
#                     for (int d = 0; d < k; d++) {
#                         sum += grid[i + d][j + k - d];
#                     }

#                     // Cạnh 3: từ dưới -> trái
#                     for (int d = 0; d < k; d++) {
#                         sum += grid[i + k - d][j - d];
#                     }

#                     // Cạnh 4: từ trái -> lên
#                     for (int d = 0; d < k; d++) {
#                         sum += grid[i - d][j - k + d];
#                     }

#                     // thêm tổng rhombus vào top 3
#                     add(sum);
#                 }
#             }
#         }

#         // trả về kết quả tùy số lượng tìm được
#         if (second == -1)
#             return new int[] { first };

#         if (third == -1)
#             return new int[] { first, second };

#         return new int[] { first, second, third };
#     }

#     // Hàm cập nhật 3 giá trị lớn nhất
#     public static void add(int val) {

#         // nếu giá trị đã tồn tại thì bỏ qua
#         if (val == first || val == second || val == third)
#             return;

#         // nếu lớn nhất
#         if (val > first) {
#             third = second;
#             second = first;
#             first = val;
#         }

#         // nếu lớn thứ 2
#         else if (val > second) {
#             third = second;
#             second = val;
#         }

#         // nếu lớn thứ 3
#         else if (val > third) {
#             third = val;
#         }
#     }
# }

# // Bài này thuộc bài Get Biggest Three Rhombus Sums in a Grid.Mình sẽ**giải
# // thích thuật toán+thêm`main`dùng`Scanner`+chú thích từng dòng**.

# // ---

# // #1. Ý tưởng thuật toán

# // ##Bước 1:Lưu 3 tổng lớn nhất

# // Ta dùng 3 biến:

# // ```first->lớn nhất second->lớn thứ 2 third->lớn thứ 3```

# // Ví dụ:

# // ```first=20 second=15 third=10```

# // Mỗi khi có`sum`mới→gọi`add(sum)`để cập nhật.

# // ---

# // #Bước 2:Rhombus size=0

# // Tức là**chỉ 1 ô**

# // ```grid[i][j]```

# // Ví dụ:

# // ```[5]```

# // Sum=`5`

# // Code:

# // ```add(grid[i][j])```

# // ---

# // #Bước 3:Rhombus size=k

# // Rhombus có dạng:

# // ```(i-k,j)/\(i,j-k)(i,j+k)\/(i+k,j)```

# // Ví dụ`k=2`

# // ```********```

# // Ta cần cộng**4 cạnh**:

# // 1 ️⃣cạnh trên phải 2 ️⃣cạnh phải dưới 3 ️⃣cạnh dưới trái 4 ️⃣cạnh trái trên

# // ---

# // #2. Code có chú thích

# // ```java

# // import java.util.*;

# // class Solution {

# // // 3 tổng lớn nhất
# // private int first = -1;
# // private int second = -1;
# // private int third = -1;

# // public int[] getBiggestThree(int[][] grid) {

# // int m = grid.length;
# // int n = grid[0].length;

# // // Bước 1: rhombus size = 0 (mỗi ô riêng lẻ)
# // for (int i = 0; i < m; i++) {
# // for (int j = 0; j < n; j++) {
# // add(grid[i][j]);
# // }
# // }

# // // Bước 2: thử tất cả tâm rhombus
# // for (int i = 0; i < m; i++) {
# // for (int j = 0; j < n; j++) {

# // // k = bán kính rhombus
# // for (int k = 1; i - k >= 0 && i + k < m && j - k >= 0 && j + k < n; k++) {

# // int sum = 0;

# // // cạnh trên -> phải
# // for (int d = 0; d < k; d++)
# // sum += grid[i - k + d][j + d];

# // // cạnh phải -> dưới
# // for (int d = 0; d < k; d++)
# // sum += grid[i + d][j + k - d];

# // // cạnh dưới -> trái
# // for (int d = 0; d < k; d++)
# // sum += grid[i + k - d][j - d];

# // // cạnh trái -> trên
# // for (int d = 0; d < k; d++)
# // sum += grid[i - d][j - k + d];

# // // cập nhật top 3
# // add(sum);
# // }
# // }
# // }

# // // trả kết quả
# // if (second == -1)
# // return new int[] { first };
# // if (third == -1)
# // return new int[] { first, second };

# // return new int[] { first, second, third };
# // }

# // // hàm cập nhật 3 giá trị lớn nhất
# // private void add(int val) {

# // // nếu trùng thì bỏ qua
# // if (val == first || val == second || val == third)
# // return;

# // if (val > first) {
# // third = second;
# // second = first;
# // first = val;
# // }

# // else if (val > second) {
# // third = second;
# // second = val;
# // }

# // else if (val > third) {
# // third = val;
# // }
# // }
# // }```

# // ---

# // #3. Thêm`main`dùng`Scanner`

# // ```java
# // import java.util.*;

# // public class Main {

# // public static void main(String[] args) {

# // Scanner sc = new Scanner(System.in);

# // // nhập số hàng và cột
# // int m = sc.nextInt();
# // int n = sc.nextInt();

# // int[][] grid = new int[m][n];

# // // nhập matrix
# // for (int i = 0; i < m; i++) {
# // for (int j = 0; j < n; j++) {
# // grid[i][j] = sc.nextInt();
# // }
# // }

# // Solution sol = new Solution();

# // int[] result = sol.getBiggestThree(grid);

# // // in kết quả
# // for (int x : result) {
# // System.out.print(x + " ");
# // }
# // }
# // }

# // // ---

# // // #4.

# // // Ví dụ input

# // // ```3 3 3 4 5 1 2 6 7 8 9```

# // // Output

# // // ```20 9 8```

# // // ---

# // // #5.
# // // Độ phức
# // // tạp

# // // Giả
# // // sử grid:

# // // ```
# // // m x n```

# // // Loop:

# // // ```i->
# // // m
# // // j->
# // // n
# // // k->

# // // // min(m,n)
# // // // d -> k
# // // // ```

# // // // Time complexity:

# // // // ```
# // // // O(m * n * k * k)
# // // // ≈ O(n^4)
# // // ```

# // // ---

# // // # 6. Điểm hay của thuật toán

# // // Không dùng:

# // // ```
# // // Set
# // // PriorityQueue
# // // Sort
# // // ```

# // // Chỉ dùng **3 biến** để giữ top 3 → rất **tối ưu bộ nhớ**.

# // // ---

# // // Nếu bạn muốn mình có thể giải thích thêm **phần khó nhất của bài này**:

# // // * **4 vòng lặp cộng cạnh rhombus (90% người học không hiểu đoạn này)**
# // // * **vẽ hình minh họa grid + tọa độ i,j,k,d cực dễ hiểu**.

# // // ---

# // // ## 1. Input của bài

# // // Bạn được cho một **ma trận số nguyên** `grid` kích thước `m x n`.

# // // Ví dụ:

# // // ```
# // // grid =
# // // [ [3,4,5],
# // // [1,2,6],
# // // [7,8,9] ]
# // // ```

# // // ---

# // // ## 2. Rhombus là gì?

# // // **Rhombus** (hình thoi) trong grid nghĩa là một hình như thế này:

# // // ```
# // // a
# // // b c
# // // d e
# // // f g
# // // h
# // // ```

# // // Nhưng trong bài này **chỉ tính các số trên BIÊN của hình thoi**, không
# // tính bên trong.

# // // Ví dụ hình thoi trong grid:

# // // ```
# // // x
# // // x x
# // // x
# // // ```

# // // hoặc lớn hơn:

# // // ```
# // // x
# // // x x
# // // x x
# // // x x
# // // x
# // // ```

# // // ---

# // // ## 3. Rhombus sum là gì?

# // // **Rhombus sum = tổng các số nằm trên cạnh (border) của hình thoi**

# // // Ví dụ:

# // // ```
# // // grid =
# // // [ [3,4,5],
# // // [1,2,6],
# // // [7,8,9] ]
# // // ```

# // // Một rhombus nhỏ:

# // // ```
# // // 4
# // // 1 6
# // // 8
# // // ```

# // // Sum:

# // // ```
# // // 4 + 1 + 6 + 8 = 19
# // // ```

# // // ---

# // // ## 4. Các rhombus hợp lệ

# // // Rhombus phải **nằm hoàn toàn trong grid**.

# // // Có 2 loại:

# // // ### 1️⃣ Rhombus size = 0

# // // Chỉ là **1 ô đơn**

# // // ```
# // // [5]
# // // ```

# // // Sum = `5`

# // // ---

# // // ### 2️⃣ Rhombus size > 0

# // // Ví dụ:

# // // ```
# // // a
# // // b c
# // // d e
# // // f g
# // // h
# // // ```

# // // Chỉ cộng **đường viền**.

# // // ---

# // // ## 5. Yêu cầu bài toán

# // // Sau khi tìm **tất cả rhombus sums**, bạn cần:

# // // 👉 Lấy **3 giá trị LỚN NHẤT KHÁC NHAU**

# // // * phải **distinct**
# // // * nếu không đủ 3 thì trả về ít hơn

# // // ---

# // // ## 6. Ví dụ

# // // Input:

# // // ```
# // // grid =
# // // [ [3,4,5],
# // // [1,2,6],
# // // [7,8,9] ]
# // // ```

# // // Các rhombus sums có thể là:

# // // ```
# // // 9
# // // 8
# // // 7
# // // 6
# // // 5
# // // 4
# // // 3
# // // 2
# // // 1
# // // 19
# // // ...
# // // ```

# // // Kết quả:

# // // ```
# // // [19, 9, 8]
# // // ```

# // // (3 tổng lớn nhất khác nhau)

# // // ---

# // // ## 7. Tóm tắt đề

# // // Cho một **matrix `grid`**.

# // // 1. Tìm **tất cả rhombus có thể tạo được**
# // // 2. Tính **sum của border**
# // // 3. Lấy **3 sum lớn nhất khác nhau**
# // // 4. Trả về **mảng giảm dần**

# // // ---

# // // ## 8. Ý tưởng thuật toán (tóm tắt)

# // // Duyệt:

# // // ```
# // // mỗi ô (i,j) là đỉnh trên của rhombus
# // // thử các size = 0,1,2,...
# // // nếu còn nằm trong grid
# // // tính border sum
# // // ```

# // // Sau đó:

# // // ```
# // // set để loại trùng
# // // sort giảm dần
# // // lấy 3 phần tử đầu
# // // ```

# // // ---

# // // ✅ Nếu bạn muốn, mình có thể giải thích thêm:

# // // * **cách duyệt rhombus trong grid (rất nhiều người không hình dung được)**
# // // * **cách tối ưu từ O(n⁴) → O(n³)**
# // // * **code Java / Python / C++ dễ hiểu**
# // // * **visual từng bước tìm rhombus**.
