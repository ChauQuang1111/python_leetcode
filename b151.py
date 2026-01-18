# # // // **Largest Magic Square – Giải thích đề bài (18/01/2026)
# Mình sẽ làm **đúng 2 yêu cầu** của bạn:

# 1️⃣ **Giải thích thuật toán 1895. Largest Magic Square (Python)**
# 2️⃣ **Thêm chú thích trực tiếp vào code** (đọc là hiểu ngay)

# Không lan man, đúng kiểu **ôn thi / đọc code LeetCode**.

# ---

# ## 1️⃣ Ý tưởng thuật toán (tóm tắt trước)

# 👉 Ta cần tìm **hình vuông con lớn nhất k×k** sao cho:

# * Tổng **mọi hàng = mọi cột = 2 đường chéo**

# ### Chiến lược:

# 1. Dùng **prefix sum** để tính tổng nhanh O(1)

#    * hàng (`row`)
#    * cột (`col`)
#    * chéo chính (`diag1`)
#    * chéo phụ (`diag2`)
# 2. Thử kích thước `k` từ **lớn → nhỏ**
# 3. Với mỗi vị trí `(r, c)` → kiểm tra có magic square không
# 4. Gặp cái đầu tiên → trả về ngay

# ---

# ## 2️⃣ Vì sao cần 4 mảng prefix sum?

# | Prefix  | Dùng để làm gì        |
# | ------- | --------------------- |
# | `row`   | Tổng nhanh 1 hàng     |
# | `col`   | Tổng nhanh 1 cột      |
# | `diag1` | Tổng đường chéo chính |
# | `diag2` | Tổng đường chéo phụ   |

# ⏱️ Mỗi phép tính tổng → **O(1)**

# ---

# ## 3️⃣ Code có chú thích chi tiết

# ```python
class Solution:
    def largestMagicSquare(self, grid):
        m, n = len(grid), len(grid[0])

        # =========================
        # Prefix sum khởi tạo
        # =========================

        # row[i][j]  = tổng hàng i từ cột 0 → j-1
        row = [[0] * (n + 1) for _ in range(m)]

        # col[i][j]  = tổng cột j từ hàng 0 → i-1
        col = [[0] * n for _ in range(m + 1)]

        # diag1[i][j] = tổng đường chéo chính từ (0,0) → (i-1,j-1)
        diag1 = [[0] * (n + 1) for _ in range(m + 1)]

        # diag2[i][j] = tổng đường chéo phụ từ (0,n-1) → (i-1,j)
        diag2 = [[0] * (n + 2) for _ in range(m + 1)]

        # =========================
        # Tính prefix sum
        # =========================
        for i in range(m):
            for j in range(n):
                row[i][j + 1] = row[i][j] + grid[i][j]
                col[i + 1][j] = col[i][j] + grid[i][j]
                diag1[i + 1][j + 1] = diag1[i][j] + grid[i][j]
                diag2[i + 1][j] = diag2[i][j + 1] + grid[i][j]

        # =========================
        # Kiểm tra magic square k×k tại (r, c)
        # =========================
        def is_magic(r, c, k):
            # Lấy tổng hàng đầu tiên làm magic sum chuẩn
            target = row[r][c + k] - row[r][c]

            # Kiểm tra tất cả các hàng
            for i in range(r, r + k):
                if row[i][c + k] - row[i][c] != target:
                    return False

            # Kiểm tra tất cả các cột
            for j in range(c, c + k):
                if col[r + k][j] - col[r][j] != target:
                    return False

            # Kiểm tra đường chéo chính
            if diag1[r + k][c + k] - diag1[r][c] != target:
                return False

            # Kiểm tra đường chéo phụ
            if diag2[r + k][c] - diag2[r][c + k] != target:
                return False

            return True

        # =========================
        # Thử kích thước từ lớn → nhỏ
        # =========================
        max_k = min(m, n)
        for k in range(max_k, 0, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if is_magic(i, j, k):
                        return k

        # Magic square 1x1 luôn hợp lệ
        return 1
# ```

# ---

# ## 4️⃣ Phân tích độ phức tạp

# * Prefix sum: **O(m × n)**
# * Duyệt size k:

#   * Vị trí: `(m−k+1)(n−k+1)`
#   * Mỗi kiểm tra: **O(k)**

# 👉 Tổng: **O(n³)**
# ✔️ Đủ nhanh cho giới hạn bài



## 5️⃣ Cách nhớ nhanh khi đi thi

# > **Largest Magic Square**
# >
# > 1. Prefix sum (row, col, 2 diag)
# > 2. Fix size k
# > 3. Lấy hàng đầu làm chuẩn
# > 4. Check hàng → cột → chéo
# > 5. Size lớn → return sớm

# ---

# Nếu bạn muốn:

# * 🔍 **So sánh bản Java vs Python**
# * ✍️ **Viết lại phiên bản dễ nhớ hơn**
# * 🧠 **Giải thích theo tư duy ICPC**
# * 🎯 **Trace tay 1 ví dụ**

# 👉 nói mình biết, mình làm tiếp cho bạn.

# import java.util.*;

# public class b152 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         // Nhập số hàng và số cột
#         int m = sc.nextInt();
#         int n = sc.nextInt();

#         int[][] grid = new int[m][n];

#         // Nhập ma trận
#         for (int i = 0; i < m; i++) {
#             for (int j = 0; j < n; j++) {
#                 grid[i][j] = sc.nextInt();
#             }
#         }

#         int result = largestMagicSquare(grid);

#         // In kết quả
#         System.out.println(result);

#         sc.close();

#     }

#     /**
#      * Kiểm tra xem có tồn tại magic square kích thước size x size hay không
#      */
#     static boolean exist(int[][] grid, int[][] rowSum, int[][] colSum, int size) {
#         int rowSize = grid.length;
#         int colSize = grid[0].length;

#         // Giới hạn vị trí góc trên-trái của hình vuông
#         int rowMax = rowSize - size;
#         int colMax = colSize - size;

#         // Duyệt mọi hình vuông size x size
#         for (int row = 0; row <= rowMax; row++) {
#             for (int col = 0; col <= colMax; col++) {

#                 // Lấy tổng hàng đầu tiên làm magic sum chuẩn
#                 int sum = rowSum[row][col + size] - rowSum[row][col];
#                 boolean match = true;

#                 // Kiểm tra tất cả các hàng và cột
#                 for (int i = 0; match && i < size; i++) {
#                     // Tổng hàng thứ i
#                     int rowCurrent = rowSum[row + i][col + size] - rowSum[row + i][col];
#                     // Tổng cột thứ i
#                     int colCurrent = colSum[row + size][col + i] - colSum[row][col + i];

#                     if (rowCurrent != sum || colCurrent != sum) {
#                         match = false;
#                     }
#                 }

#                 // Nếu hàng và cột đều hợp lệ, kiểm tra 2 đường chéo
#                 if (match) {
#                     int diag1 = 0, diag2 = 0;
#                     for (int i = 0; i < size; i++) {
#                         diag1 += grid[row + i][col + i]; // chéo chính
#                         diag2 += grid[row + i][col + size - 1 - i]; // chéo phụ
#                     }

#                     if (diag1 == sum && diag2 == sum) {
#                         return true; // tìm được magic square
#                     }
#                 }
#             }
#         }
#         return false;
#     }

#     /**
#      * Tìm kích thước magic square lớn nhất
#      */
#     public static int largestMagicSquare(int[][] grid) {
#         int rowSize = grid.length;
#         int colSize = grid[0].length;

#         // Prefix sum cho hàng và cột
#         int[][] rowSum = new int[rowSize][colSize + 1];
#         int[][] colSum = new int[rowSize + 1][colSize];

#         // Tính prefix sum
#         for (int row = 0; row < rowSize; row++) {
#             for (int col = 0; col < colSize; col++) {
#                 rowSum[row][col + 1] = rowSum[row][col] + grid[row][col];
#                 colSum[row + 1][col] = colSum[row][col] + grid[row][col];
#             }
#         }

#         // Thử kích thước từ lớn đến nhỏ
#         for (int size = Math.min(rowSize, colSize); size > 1; size--) {
#             if (exist(grid, rowSum, colSum, size)) {
#                 return size;
#             }
#         }

#         // Magic square 1x1 luôn hợp lệ
#         return 1;
#     }

# }

# // // ---

# // // ### 1. Magic Square là gì?

# // // Một **magic square (hình vuông ma thuật)** là **ma trận vuông k × k** (k ≥
# // 1) thỏa mãn:

# // // * **Tổng mỗi hàng = nhau**
# // // * **Tổng mỗi cột = nhau**
# // // * **Tổng đường chéo chính = tổng đường chéo phụ = cùng giá trị đó**

# // // 👉 Giá trị tổng này gọi là **magic sum**.

# // // ---

# // // ### 2. Đề bài “Largest Magic Square” yêu cầu gì?

# // // * Bạn được cho một ma trận số nguyên `grid` kích thước `m × n`.
# // // * Nhiệm vụ:
# // // 👉 **Tìm kích thước lớn nhất `k` sao cho tồn tại một magic square k × k
# // trong grid.**
# // // * Trả về **k** (không cần trả về vị trí).

# // // ---

# // // ### 3. Ví dụ đơn giản

# // // #### Ví dụ 1:

# // // ```
# // // grid = [
# // // [7, 1, 4, 5, 6],
# // // [2, 5, 1, 6, 4],
# // // [1, 5, 4, 3, 2],
# // // [1, 2, 7, 3, 4]
# // // ]
# // // ```

# // // Xét ma trận con 3×3:

# // // ```
# // // [5, 1, 6]
# // // [5, 4, 3]
# // // [2, 7, 3]
# // // ```

# // // * Tổng mỗi hàng = 12
# // // * Tổng mỗi cột = 12
# // // * Tổng 2 đường chéo = 12

# // // 👉 Đây là **magic square kích thước 3**
# // // 👉 Không có magic square lớn hơn → **đáp án = 3**

# // // ---

# // // ### 4. Lưu ý quan trọng trong đề

# // // ✅ **Magic square 1×1 luôn hợp lệ**
# // // → Vì chỉ có 1 số thì hàng, cột, chéo đều giống nhau
# // // → **Đáp án tối thiểu luôn là 1**

# // // ❌ **Không yêu cầu các số phải khác nhau**
# // // → Khác với magic square cổ điển (1–9), bài này **chỉ cần tổng bằng nhau**

# // // ---

# // // ### 5. Cách hiểu đề một cách “tư duy thi cử”

# // // 1. Duyệt kích thước k từ **lớn → nhỏ**
# // // 2. Với mỗi k, xét **mọi ma trận con k×k**
# // // 3. Kiểm tra:

# // // * Tổng các hàng
# // // * Tổng các cột
# // // * 2 đường chéo
# // // 4. Chỉ cần **tìm được 1 cái hợp lệ → trả về k ngay**

# // // ---

# // // ### 6. Tóm tắt 1 dòng (để nhớ nhanh)

# // // > **Largest Magic Square = tìm hình vuông con lớn nhất mà tổng mọi hàng,
# // cột và 2 đường chéo đều bằng nhau**

# // // ---

# // // Nếu bạn muốn:

# // // * Giải thích **bằng hình vẽ từng bước**
# // // * Phân tích **tư duy thuật toán (O(n³) / prefix sum)**
# // // * Hoặc **code Java / Python**

# // // 👉 cứ nói mình sẽ làm tiếp theo 👍
# // // Mình sẽ **giải thích thuật toán theo đúng code của bạn**, đi **từng
# // khối**, đúng kiểu **đọc code là hiểu tư duy** (rất hợp luyện LeetCode / phỏng
# // vấn).

# // // ---

# // // ## 1️⃣ Ý tưởng tổng quát của thuật toán

# // // 👉 Bài toán: **Largest Magic Square**

# // // **Chiến lược:**

# // // 1. **Tiền xử lý prefix sum** cho:

# // // * Tổng theo **hàng** (`rowSum`)
# // // * Tổng theo **cột** (`colSum`)
# // // 2. Thử kích thước hình vuông `size` từ **lớn → nhỏ**
# // // 3. Với mỗi `size`, kiểm tra:

# // // * Có tồn tại **1 hình vuông size × size** thỏa mãn magic square hay không
# // // 4. Gặp cái đầu tiên → **trả về luôn**

# // // ---

# // // ## 2️⃣ Prefix Sum dùng để làm gì?

# // // ### 🔹 rowSum

# // // ```java
# // // rowSum[row][col+1] = rowSum[row][col] + grid[row][col];
# // // ```

# // // 👉 `rowSum[r][c]` = tổng từ cột `0 → c-1` của hàng `r`

# // // ➡️ Tổng đoạn `[col → col+size-1]` của **1 hàng**:

# // // ```java
# // // rowSum[row][col+size] - rowSum[row][col]
# // // ```

# // ---

# // ### 🔹 colSum

# // ```java
# // colSum[row+1][col] = colSum[row][col] + grid[row][col];
# // ```

# // 👉 `colSum[r][c]` = tổng từ hàng `0 → r-1` của cột `c`

# // ➡️ Tổng đoạn `[row → row+size-1]` của **1 cột**:

# // ```java
# // colSum[row+size][col] - colSum[row][col]
# // ```

# // ⏱️ Nhờ prefix sum → **tính tổng O(1)**

# // ---

# // ## 3️⃣ Hàm `exist(...)` – kiểm tra có magic square size hay không

# // ```java
# // boolean exist(int[][] grid, int[][] rowSum, int[][] colSum, int size)
# // ```

# // 👉 Trả về **true** nếu tồn tại **ít nhất 1** magic square `size × size`

# // ---

# // ### 3.1️⃣ Duyệt mọi vị trí hình vuông size × size

# // ```java
# // for (int row = 0; row <= rowMax; row++)
# // for (int col = 0; col <= colMax; col++)
# // ```

# // 📌 `(row, col)` là **góc trên-trái** của hình vuông

# // ---

# // ### 3.2️⃣ Lấy tổng chuẩn (magic sum)

# // ```java
# // int sum = rowSum[row][col+size] - rowSum[row][col];
# // ```

# // 👉 Lấy tổng **hàng đầu tiên** làm chuẩn

# // ---

# // ### 3.3️⃣ Kiểm tra tất cả hàng & cột

# // ```java
# // for (int ii = 0; match && ii < size; ii++) {
# // int sum1 = rowSum[row+ii][col+size] - rowSum[row+ii][col];
# // int sum2 = colSum[row+size][col+ii] - colSum[row][col+ii];
# // match = sum1 == sum && sum2 == sum;
# // }
# // ```

# // 📌 Với mỗi `ii`:

# // * `sum1` → tổng **hàng thứ ii**
# // * `sum2` → tổng **cột thứ ii**

# // ❌ Chỉ cần **1 hàng hoặc cột khác** → loại luôn

# // 👉 Đây là **early break** để tối ưu

# // ---

# // ### 3.4️⃣ Kiểm tra 2 đường chéo (nếu hàng & cột OK)

# // ```java
# // int sum1 = 0, sum2 = 0;
# // for (int ii = 0; ii < size; ii++) {
# // sum1 += grid[row+ii][col+ii];
# // sum2 += grid[row+ii][col+size-1-ii];
# // }
# // ```

# // * `sum1` → đường chéo chính
# // * `sum2` → đường chéo phụ

# // ```java
# // if (sum1 == sum && sum2 == sum) return true;
# // ```

# // ✔️ Nếu đúng → tồn tại magic square

# // ---

# // ## 4️⃣ Hàm `largestMagicSquare(...)`

# // ```java
# // for (int size = min(rowSize, colSize); size > 1; size--) {
# // if (exist(..., size)) return size;
# // }
# // return 1;
# // ```

# // ### Ý tưởng:

# // * Thử **size lớn nhất trước**
# // * Gặp cái hợp lệ → trả về luôn
# // * Nếu không có size ≥ 2 → **1×1 luôn hợp lệ**

# // ---

# // ## 5️⃣ Độ phức tạp

# // * Prefix sum: `O(m × n)`
# // * Kiểm tra mỗi size:

# // * Vị trí: `(m − size) × (n − size)`
# // * Mỗi vị trí kiểm tra `O(size)`
# // * Tổng: **O(n³)** (vừa đủ cho ràng buộc bài)

# // 👉 Prefix sum giúp **giảm từ O(n⁴) xuống O(n³)**

# // ---

# // // ## 6️⃣ Tư duy gói gọn 5 dòng (rất nên nhớ)

# // // > 1. Prefix sum để lấy tổng nhanh
# // // > 2. Fix size → duyệt mọi hình vuông
# // // > 3. Lấy hàng đầu làm chuẩn
# // // > 4. So hàng + cột + 2 chéo
# // // > 5. Size lớn → trả sớm

# // // ---

# // // Nếu bạn muốn, mình có thể:

# // // * 🔍 **Trace tay 1 ví dụ**
# // // * ✍️ **Viết lại code dễ đọc hơn**
# // // * 🎯 **Giải thích để nhớ khi đi thi**
# // // * ⚡ **So sánh với brute-force**

# // // 👉 Bạn chọn hướng nào?
