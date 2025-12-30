# # // Magic Squares In Grid(30/12/2025)
# Dưới đây là **giải thích thuật toán + code Python có chú thích chi tiết**, bám **đúng lời giải LeetCode 840** bạn đưa ra (tối ưu bằng **center = 5**).

# ---

# ## 1. Ý tưởng thuật toán (tư duy cốt lõi)

# ### Nhận xét quan trọng (mấu chốt tối ưu)

# Với **magic square 3×3 dùng các số 1–9**:

# 1. **Ô chính giữa luôn = 5**
# 2. **Tổng mỗi hàng / cột / đường chéo = 15**
# 3. Hai cặp ô đối diện qua tâm có tổng = **10**

# 👉 Nhờ đó:

# * Chỉ cần xét các ô `(i, j)` sao cho `grid[i][j] == 5`
# * Giảm rất nhiều số lượng kiểm tra

# ---

# ## 2. Luồng thuật toán tổng quát

# 1. Duyệt từng ô `(i, j)` **không nằm ở biên**
# 2. Nếu `grid[i][j] != 5` → bỏ qua
# 3. Kiểm tra ma trận 3×3 xung quanh `(i, j)`:

#    * Các số thuộc `[1..9]`, không trùng
#    * Mỗi hàng = 15
#    * Mỗi cột = 15
#    * Hai cặp đối diện qua tâm có tổng = 10
# 4. Nếu thỏa → đếm +1

# ---

# ## 3. Giải thích chi tiết hàm `isMagic(i, j)`

# ### 3.1. Khởi tạo

# ```python
# once = [False] * 10      # Đánh dấu số đã xuất hiện (1..9)
# rowSum = [0] * 3         # Tổng của 3 hàng
# colSum = [0] * 3         # Tổng của 3 cột
# ```

# ---

# ### 3.2. Duyệt 9 ô của ma trận 3×3

# ```python
# for a in range(i-1, i+2):
#     for b in range(j-1, j+2):
# ```

# * `(i, j)` là **ô trung tâm**
# * `(a, b)` duyệt từ góc trên trái đến dưới phải

# ---

# ### 3.3. Kiểm tra giá trị hợp lệ và tính tổng

# ```python
# x = grid[a][b]
# if x < 1 or x > 9:
#     return False
# ```

# 👉 Magic square **chỉ dùng số 1–9**

# ```python
# rowSum[a - i + 1] += x
# colSum[b - j + 1] += x
# ```

# * Quy đổi chỉ số hàng / cột về `[0..2]`

# ```python
# if once[x]:
#     return False   # Số bị lặp
# once[x] = True
# ```

# ---

# ### 3.4. Đảm bảo đủ cả 9 số từ 1 đến 9

# ```python
# for b in once[1:]:
#     if not b:
#         return False
# ```

# 👉 Nếu thiếu bất kỳ số nào → không hợp lệ

# ---

# ### 3.5. Kiểm tra tổng hàng và cột

# ```python
# for sum in rowSum:
#     if sum != 15:
#         return False

# for sum in colSum:
#     if sum != 15:
#         return False
# ```

# ---

# ### 3.6. Kiểm tra đường chéo (tối ưu)

# ```python
# return grid[i-1][j-1] + grid[i+1][j+1] == 10 \
#    and grid[i+1][j-1] + grid[i-1][j+1] == 10
# ```

# 👉 Vì:

# * Trung tâm = 5
# * Tổng đường chéo = 15
# * ⇒ Hai đầu chéo phải có tổng = **10**

# ---

# ## 4. Code Python có chú thích đầy đủ

# ```python
from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        # Kiểm tra magic square 3x3 với tâm tại (i, j)
        def isMagic(i, j):
            once = [False] * 10    # Đánh dấu số 1..9
            rowSum = [0] * 3       # Tổng 3 hàng
            colSum = [0] * 3       # Tổng 3 cột

            # Duyệt 9 ô xung quanh tâm
            for a in range(i - 1, i + 2):
                for b in range(j - 1, j + 2):
                    x = grid[a][b]

                    # Giá trị phải từ 1 đến 9
                    if x < 1 or x > 9:
                        return False

                    # Cộng tổng hàng và cột
                    rowSum[a - i + 1] += x
                    colSum[b - j + 1] += x

                    # Kiểm tra trùng số
                    if once[x]:
                        return False
                    once[x] = True

            # Đảm bảo đủ 9 số từ 1 đến 9
            for used in once[1:]:
                if not used:
                    return False

            # Mỗi hàng phải có tổng 15
            for s in rowSum:
                if s != 15:
                    return False

            # Mỗi cột phải có tổng 15
            for s in colSum:
                if s != 15:
                    return False

            # Kiểm tra 2 đường chéo (vì tâm = 5 → cặp đối diện = 10)
            return (grid[i - 1][j - 1] + grid[i + 1][j + 1] == 10 and
                    grid[i + 1][j - 1] + grid[i - 1][j + 1] == 10)

        r, c = len(grid), len(grid[0])
        if r < 3 or c < 3:
            return 0

        cnt = 0
        # Chỉ duyệt các ô có thể làm tâm
        for i in range(1, r - 1):
            for j in range(1, c - 1):
                # Trung tâm magic square luôn là 5
                if grid[i][j] == 5 and isMagic(i, j):
                    cnt += 1

        return cnt
# ```

# ---

# ## 5. Độ phức tạp

# * Duyệt grid: **O(m × n)**
# * Mỗi lần kiểm tra 3×3: **O(1)**

# 👉 **Tổng:** `O(m × n)`
# 👉 **Bộ nhớ:** `O(1)`

# ---

## 6. Ghi nhớ nhanh để đi thi

# * Magic square 3×3:

#   * Center = **5**
#   * Tổng = **15**
#   * Cặp đối diện = **10**
# * Duyệt từ **ô trung tâm**, không duyệt góc
# * Early return để tối ưu

# ---

# Nếu bạn muốn, mình có thể:

# * ✂️ Viết **phiên bản siêu ngắn (10–12 dòng)**
# * 🧠 Chuyển sang **pseudocode**
# * 🧪 Phân tích test case dễ sai

# 👉 Cứ nói, mình làm tiếp.

# // **Magic Squares In Grid – Giải thích đề bài (bằng tiếng Việt)**
# import java.util.*;

# public class b133 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         // Nhập số hàng và số cột
#         int rows = sc.nextInt();
#         int cols = sc.nextInt();

#         int[][] grid = new int[rows][cols];

#         // Nhập ma trận
#         for (int i = 0; i < rows; i++) {
#             for (int j = 0; j < cols; j++) {
#                 grid[i][j] = sc.nextInt();
#             }
#         }

#         int result = numMagicSquaresInside(grid);

#         // In kết quả
#         System.out.println(result);

#         sc.close();

#     }

#     public static int numMagicSquaresInside(int[][] grid) {
#         int count = 0;
#         int rows = grid.length;
#         int cols = grid[0].length;

#         // Duyệt tất cả các ma trận con 3x3
#         for (int i = 0; i <= rows - 3; i++) {
#             for (int j = 0; j <= cols - 3; j++) {
#                 if (isMagicSquare(grid, i, j)) {
#                     count++;
#                 }
#             }
#         }

#         return count;
#     }

#     /**
#      * Hàm kiểm tra ma trận con 3x3 bắt đầu tại vị trí (i, j)
#      * có phải là Magic Square hay không
#      */
#     public static boolean isMagicSquare(int[][] grid, int i, int j) {

#         // Mảng đánh dấu các số đã xuất hiện (chỉ dùng index 1 -> 9)
#         boolean[] seen = new boolean[10];

#         // 1. Kiểm tra 9 số có nằm trong [1..9] và không bị trùng
#         for (int x = 0; x < 3; x++) {
#             for (int y = 0; y < 3; y++) {
#                 int num = grid[i + x][j + y];

#                 // Nếu số không hợp lệ hoặc bị lặp thì không phải magic square
#                 if (num < 1 || num > 9 || seen[num]) {
#                     return false;
#                 }
#                 seen[num] = true;
#             }
#         }

#         // 2. Lấy tổng chuẩn (tổng của hàng đầu tiên)
#         int sum = grid[i][j] + grid[i][j + 1] + grid[i][j + 2];

#         // 3. Kiểm tra tổng của 3 hàng
#         for (int x = 0; x < 3; x++) {
#             int rowSum = grid[i + x][j]
#                     + grid[i + x][j + 1]
#                     + grid[i + x][j + 2];
#             if (rowSum != sum) {
#                 return false;
#             }
#         }

#         // 4. Kiểm tra tổng của 3 cột
#         for (int y = 0; y < 3; y++) {
#             int colSum = grid[i][j + y]
#                     + grid[i + 1][j + y]
#                     + grid[i + 2][j + y];
#             if (colSum != sum) {
#                 return false;
#             }
#         }

#         // 5. Kiểm tra 2 đường chéo
#         int diag1 = grid[i][j]
#                 + grid[i + 1][j + 1]
#                 + grid[i + 2][j + 2];

#         int diag2 = grid[i + 2][j]
#                 + grid[i + 1][j + 1]
#                 + grid[i][j + 2];

#         if (diag1 != sum || diag2 != sum) {
#             return false;
#         }

#         // Nếu thỏa tất cả điều kiện → là magic square
#         return true;
#     }

#     /**
#      * Hàm đếm số Magic Square 3x3 trong grid
#      */

# }

# // Đề bài thường gặp trên LeetCode với tên **“Magic Squares In Grid”**. Nội dung
# // chính như sau:

# // ---

# // ### 1. Magic Square (Ma phương) là gì?

# // Một **magic square 3×3** là một bảng 3 hàng × 3 cột thỏa mãn **tất cả** các
# // điều kiện:

# // 1. **Chỉ chứa các số từ 1 đến 9**, mỗi số **xuất hiện đúng 1 lần**
# // → Không được trùng số, không được thiếu số.

# // 2. **Tổng các số của mỗi hàng bằng nhau**

# // 3. **Tổng các số của mỗi cột bằng nhau**

# // 4. **Tổng của 2 đường chéo cũng bằng nhau**

# // 👉 Với ma phương 3×3 chuẩn (dùng số 1–9), tổng đó **luôn là 15**.

# // Ví dụ một magic square hợp lệ:

# // ```
# // 8 1 6
# // 3 5 7
# // 4 9 2
# // ```

# // ---

# // ### 2. Grid (lưới) trong đề bài

# // * Bạn được cho một **ma trận grid kích thước m × n** (m hàng, n cột).
# // * Mỗi ô chứa **một số nguyên**.

# // ---

# // ### 3. Yêu cầu của bài toán

# // 👉 **Đếm số lượng magic square 3×3 xuất hiện trong grid.**

# // Cụ thể:

# // * Xét **mọi ma trận con 3×3** có thể lấy từ grid
# // * Kiểm tra xem ma trận con đó có phải là **magic square** hay không
# // * Nếu đúng → đếm +1

# // ---

# // ### 4. Cách hiểu đơn giản

# // * Trượt một “cửa sổ” 3×3 trên toàn bộ grid
# // * Với mỗi vị trí:

# // * Lấy 9 ô
# // * Kiểm tra:

# // * Có đủ số từ 1 đến 9 không?
# // * Tổng hàng = tổng cột = tổng chéo = 15?
# // * Cuối cùng trả về **số magic square tìm được**

# // ---

# // ### 5. Ví dụ minh họa

# // Giả sử grid:

# // ```
# // 4 3 8 4
# // 9 5 1 9
# // 2 7 6 2
# // ```

# // Các ma trận con 3×3:

# // * Lấy từ cột 0 → 2:

# // ```
# // 4 3 8
# // 9 5 1
# // 2 7 6
# // ```

# // → Đây là **magic square hợp lệ** ✅

# // * Lấy từ cột 1 → 3:

# // ```
# // 3 8 4
# // 5 1 9
# // 7 6 2
# // ```

# // → Không thỏa → ❌

# // 👉 Kết quả: **1**

# // ---

# // ### 6. Tóm tắt ngắn gọn

# // * Input: ma trận số
# // * Output: số lượng ma phương 3×3
# // * Điều kiện quan trọng:

# // * Số từ **1–9, không trùng**
# // * Tổng hàng, cột, chéo = **15**

# // ---

# // Nếu bạn muốn, mình có thể:

# // * ✅ Giải thích **tư duy thuật toán**
# // * ✅ Viết **code Java / Python**
# // * ✅ Phân tích **độ phức tạp**
# // * ✅ Giải thích theo kiểu **dễ nhớ cho thi cử**

# // Bạn muốn tiếp theo phần nào?
# // Mình **giải thích thuật toán từng bước**, bám **đúng code của bạn**, theo
# // kiểu dễ hiểu – đúng phong cách đi thi / phỏng vấn.

# // ---

# // ## 1. Ý tưởng tổng quát của thuật toán

# // Bài toán yêu cầu:

# // > **Đếm số ma phương 3×3 trong một ma trận lớn**

# // 👉 Chiến lược:

# // * Duyệt **tất cả các ma trận con 3×3**
# // * Với mỗi ma trận con:

# // * Kiểm tra xem nó có phải **Magic Square** hay không
# // * Nếu đúng → tăng biến đếm

# // ---

# // ## 2. Hàm `numMagicSquaresInside`

# // ```java
# // public int numMagicSquaresInside(int[][] grid) {
# // int count = 0;
# // int rows = grid.length;
# // int cols = grid[0].length;
# // ```

# // ### Vai trò

# // * `rows`, `cols`: kích thước của grid
# // * `count`: số magic square tìm được

# // ---

# // ### Duyệt tất cả các ma trận con 3×3

# // ```java
# // for (int i = 0; i <= rows - 3; i++) {
# // for (int j = 0; j <= cols - 3; j++) {
# // if (isMagicSquare(grid, i, j)) {
# // count++;
# // }
# // }
# // }
# // ```

# // 🔹 `(i, j)` là **góc trên bên trái** của ma trận 3×3
# // 🔹 `rows - 3`, `cols - 3` để **không bị vượt biên**

# // 👉 Với mỗi vị trí `(i, j)` → gọi hàm `isMagicSquare`

# // ---

# // ## 3. Hàm `isMagicSquare(grid, i, j)`

# // Hàm này kiểm tra **ma trận 3×3 bắt đầu tại (i, j)** có phải ma phương hay
# // không.

# // ---

# // ### 3.1. Kiểm tra các số từ 1 đến 9, không trùng

# // ```java
# // boolean[] seen = new boolean[10];
# // ```

# // * Mảng `seen` để đánh dấu số đã xuất hiện
# // * Chỉ dùng index từ `1 → 9`

# // ```java
# // for (int x = 0; x < 3; x++) {
# // for (int y = 0; y < 3; y++) {
# // int num = grid[i + x][j + y];
# // if (num < 1 || num > 9 || seen[num]) return false;
# // seen[num] = true;
# // }
# // }
# // ```

# // 👉 Mục đích:

# // * ❌ Loại nếu:

# // * Số < 1 hoặc > 9
# // * Số bị lặp
# // * ✅ Đảm bảo đủ **9 số khác nhau từ 1–9**

# // ⏱️ Tối ưu: nếu sai → return ngay

# // ---

# // ### 3.2. Lấy tổng chuẩn (tổng hàng đầu tiên)

# // ```java
# // int sum = grid[i][j] + grid[i][j+1] + grid[i][j+2];
# // ```

# // 👉 Đây là **tổng chuẩn**
# // Mọi hàng, cột, chéo đều phải bằng `sum`

# // ---

# // ### 3.3. Kiểm tra 3 hàng

# // ```java
# // for (int x = 0; x < 3; x++) {
# // if (sum != grid[i + x][j] + grid[i + x][j + 1] + grid[i + x][j + 2])
# // return false;
# // }
# // ```

# // * Mỗi hàng phải có tổng = `sum`
# // * Chỉ cần **1 hàng sai → loại ngay**

# // ---

# // ### 3.4. Kiểm tra 3 cột

# // ```java
# // for (int y = 0; y < 3; y++) {
# // if (sum != grid[i][j + y] + grid[i + 1][j + y] + grid[i + 2][j + y])
# // return false;
# // }
# // ```

# // * Tương tự hàng
# // * Kiểm tra từng cột

# // ---

# // ### 3.5. Kiểm tra 2 đường chéo

# // ```java
# // if (sum != grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]) return false;
# // if (sum != grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2]) return false;
# // ```

# // * Chéo chính
# // * Chéo phụ

# // 👉 Nếu **bất kỳ chéo nào sai** → không phải ma phương

# // ---

# // ### 3.6. Nếu vượt qua hết → là magic square

# // ```java
# // return true;
# // ```

# // ---

# // ## 4. Tóm tắt thuật toán (ngắn gọn để nhớ)

# // **Thuật toán:**

# // 1. Duyệt mọi ma trận con 3×3
# // 2. Với mỗi ma trận:

# // * Kiểm tra có đủ số **1–9, không trùng**
# // * Lấy tổng hàng đầu tiên
# // * So sánh tổng:

# // * 3 hàng
# // * 3 cột
# // * 2 đường chéo
# // 3. Nếu hợp lệ → tăng biến đếm

# // ---

# // ## 5. Độ phức tạp

# // * Số ma trận con: `(rows − 2) × (cols − 2)`
# // * Mỗi ma trận 3×3:

# // * Kiểm tra tối đa **9 + 8 phép cộng**
# // * Thời gian **O(1)**

# // 👉 **Tổng độ phức tạp:**
# // [
# // O(m \times n)
# // ]

# // 👉 **Bộ nhớ:**
# // [
# // O(1)
# // ]

# // ---

# // Nếu bạn muốn, mình có thể:

# // * 🔥 Giải thích **vì sao ma phương 3×3 luôn có tổng = 15**
# // * 🔥 Chỉ ra **tối ưu nâng cao (center = 5)**
# // * 🔥 Viết lại code theo phong cách **ngắn – sạch – dễ nhớ**

# // Bạn muốn tiếp phần nào?
