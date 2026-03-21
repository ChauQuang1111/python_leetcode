# // Bài **“Flip Square Submatrix Vertically”** (21/03/2026)

# Mình sẽ giải thích **thuật toán + thêm chú thích trực tiếp vào code Python** cho bạn 👇

# ---

# # 🧠 Ý tưởng thuật toán

# * Bạn có một **submatrix vuông (k \times k)** bắt đầu tại `(x, y)`
# * “Flip vertically” = **đổi chỗ các hàng trên ↔ dưới**

# 👉 Tức là:

# * Hàng `x + 0` ↔ `x + k - 1`
# * Hàng `x + 1` ↔ `x + k - 2`
# * ...

# 📌 Chỉ cần duyệt **nửa số hàng (`k // 2`)** là đủ

# ---

# # ✅ Code có chú thích chi tiết

# ```python
class Solution:
    def reverseSubmatrix(self, grid, x, y, k):
        
        # Duyệt nửa số hàng của submatrix (để tránh swap lại lần 2)
        for i in range(k // 2):
            
            # Duyệt từng cột trong submatrix
            for j in range(k):
                
                # Swap phần tử ở hàng trên với hàng đối xứng phía dưới
                # (x + i)          : hàng trên
                # (x + k - 1 - i)  : hàng dưới (đối xứng)
                # (y + j)          : cột giữ nguyên
                
                grid[x + i][y + j], grid[x + k - 1 - i][y + j] = \
                grid[x + k - 1 - i][y + j], grid[x + i][y + j]

        return grid


# 🔍 Giải thích dòng quan trọng nhất

# ```python
# grid[x + i][y + j], grid[x + k - 1 - i][y + j] = ...


# 👉 Đây là **swap trong Python**

# Tương đương với:

# ```python
# temp = grid[x + i][y + j]
# grid[x + i][y + j] = grid[x + k - 1 - i][y + j]
# grid[x + k - 1 - i][y + j] = temp
# ```

# ---

# # 📊 Minh họa nhanh

# Submatrix:

# ```
# 1 2 3
# 4 5 6
# 7 8 9
# ```

# Sau khi flip:

# ```
# 7 8 9
# 4 5 6
# 1 2 3
# ```

# ---

# ⚡ Độ phức tạp

# * Time: **O(k²)**
# * Space: **O(1)** (không dùng thêm bộ nhớ)

# ---

# # 💡 Tóm tắt cực ngắn

# 👉 Thuật toán =
# **Swap từng phần tử giữa 2 hàng đối xứng trong submatrix**

# ---

# Nếu bạn muốn nâng trình hơn, mình có thể:

# * So sánh với **flip ngang (left ↔ right)** để tránh nhầm
# * Hoặc hướng dẫn cách **rotate matrix 90° (hard hơn, rất hay gặp)**



# import java.util.*;

# public class b223 {

#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         // Nhập kích thước ma trận
#         int n = sc.nextInt(); // số hàng
#         int m = sc.nextInt(); // số cột

#         int[][] grid = new int[n][m];

#         // Nhập ma trận
#         int i = 0;
#         while (i < n) {
#             int j = 0;
#             while (j < m) {
#                 grid[i][j] = sc.nextInt();
#                 j++;
#             }
#             i++;
#         }

#         // Nhập vị trí và kích thước submatrix
#         int x = sc.nextInt(); // hàng bắt đầu
#         int y = sc.nextInt(); // cột bắt đầu
#         int k = sc.nextInt(); // kích thước k x k

#         // Gọi hàm xử lý
#         grid = reverseSubmatrix(grid, x, y, k);

#         // In kết quả
#         i = 0;
#         while (i < n) {
#             int j = 0;
#             while (j < m) {
#                 System.out.print(grid[i][j] + " ");
#                 j++;
#             }
#             System.out.println();
#             i++;
#         }

#         sc.close();
#     }

#     // Hàm lật submatrix k x k theo chiều dọc (trên ↔ dưới)
#     public static int[][] reverseSubmatrix(int[][] grid, int x, int y, int k) {

#         // Duyệt nửa số hàng của submatrix
#         int i = 0;
#         while (i < k / 2) {

#             int j = 0;
#             // Duyệt từng cột trong submatrix
#             while (j < k) {

#                 // Lưu giá trị hàng trên
#                 int temp = grid[x + i][y + j];

#                 // Gán hàng dưới lên hàng trên
#                 grid[x + i][y + j] = grid[x + k - 1 - i][y + j];

#                 // Gán lại giá trị cũ xuống hàng dưới
#                 grid[x + k - 1 - i][y + j] = temp;

#                 j++;
#             }
#             i++;
#         }

#         return grid;
#     }
# }

# // Đoạn code của bạn đang làm đúng ý bài **Flip Square Submatrix Vertically**.
# // Mình sẽ giải thích **thuật toán + tư duy** cho bạn thật rõ 👇

# // ---

# // # 🧠 Ý tưởng chính

# // Bạn có:

# // * `grid`: ma trận
# // * `(x, y)`: góc trên bên trái của submatrix
# // * `k`: kích thước hình vuông (k \times k)

# // 👉 Nhiệm vụ:
# // **Lật hình vuông này theo chiều dọc (trên ↔ dưới)**

# // ---

# // # 🔄 Tư duy cốt lõi

# // Lật dọc = **đổi chỗ các hàng đối xứng**

# // Ví dụ:

# // ```
# // Hàng 0 ↔ Hàng k-1
# // Hàng 1 ↔ Hàng k-2
# // ...
# // ```

# // 👉 Chỉ cần xử lý **nửa trên** là đủ → `k / 2`

# // ---

# // # 🔍 Giải thích từng dòng code

# // ```java
# // for(int i = 0; i < k / 2; i++)
# // ```

# // 👉 Duyệt từng cặp hàng cần swap:

# // * `i = 0` → hàng đầu
# // * `i = 1` → hàng thứ 2
# // * ...
# // * chỉ đến `k/2` để tránh swap lại lần 2

# // ---

# // ```java
# // for(int j = 0; j < k; j++)
# // ```

# // 👉 Duyệt từng cột trong submatrix (từ trái sang phải)

# // ---

# // ```java
# // int temp = grid[x + i][y + j];
# // ```

# // 👉 Lưu giá trị ở **hàng trên**

# // ---

# // ```java
# // grid[x + i][y + j] = grid[x + k - 1 - i][y + j];
# // ```

# // 👉 Gán giá trị hàng dưới lên hàng trên

# // ---

# // ```java
# // grid[x + k - 1 - i][y + j] = temp;
# // ```

# // 👉 Gán lại giá trị cũ xuống hàng dưới

# // ---

# // # 📌 Mapping chỉ số (quan trọng nhất)

# // | Vị trí | Ý nghĩa |
# // | --------------- | ----------------------- |
# // | `x + i` | hàng phía trên |
# // | `x + k - 1 - i` | hàng đối xứng phía dưới |
# // | `y + j` | cột giữ nguyên |

# // 👉 Đây chính là **trục lật theo chiều ngang**

# // ---

# // # 📊 Ví dụ minh họa

# // Submatrix:

# // ```
# // a b c
# // d e f
# // g h i
# // ```

# // Sau khi chạy:

# // ```
# // g h i
# // d e f
# // a b c
# // ```

# // ---

# // # ⚡ Độ phức tạp

# // * Thời gian:
# // [
# // O(k^2)
# // ]
# // (vì duyệt nửa số hàng × toàn bộ cột)

# // * Bộ nhớ:
# // [
# // O(1)
# // ]
# // (in-place, không dùng thêm mảng)

# // ---

# // # 💡 Tóm lại (rất quan trọng)

# // Thuật toán của bạn thực chất là:

# // 👉 **Swap từng phần tử của 2 hàng đối xứng trong submatrix**

# // ---

# // # 🚀 Nhận xét code của bạn

# // ✔ Đúng hoàn toàn
# // ✔ Tối ưu (in-place)
# // ✔ Không dư thừa

# // ---

# // Nếu bạn muốn nâng level hơn, mình có thể:

# // * So sánh với **flip ngang (horizontal)** để bạn không nhầm
# // * Hoặc biến bài này thành dạng **rotate matrix 90°** (hay ra thi hơn)

# // ---

# // ## 🧠 Ý nghĩa đề bài

# // Bạn được cho:

# // * Một ma trận (matrix) kích thước ( n \times m )
# // * Một hình vuông con (square submatrix) nằm bên trong ma trận đó

# // Yêu cầu:
# // 👉 **Lật (flip) hình vuông con đó theo chiều dọc (vertically)**

# // ---

# // ## 🔄 “Flip vertically” là gì?

# // “Flip vertically” = **lật trên ↔ dưới (theo trục ngang)**

# // Tức là:

# // * Hàng trên cùng ↔ hàng dưới cùng
# // * Hàng thứ 2 ↔ hàng thứ n-1
# // * ...

# // ---

# // ## 📌 Ví dụ đơn giản

# // ### Ma trận ban đầu:

# // ```
# // 1 2 3 4
# // 5 6 7 8
# // 9 10 11 12
# // 13 14 15 16
# // ```

# // Giả sử chọn submatrix vuông 3x3 từ (1,1) đến (3,3):

# // ```
# // 6 7 8
# // 10 11 12
# // 14 15 16
# // ```

# // ---

# // ### Sau khi flip vertically:

# // ```
# // 14 15 16
# // 10 11 12
# // 6 7 8
# // ```

# // ---

# // ## 🔧 Ý tưởng làm bài

# // Giả sử:

# // * submatrix bắt đầu tại `(r, c)`
# // * kích thước là `k`

# // 👉 Ta chỉ cần:

# // ```
# // for i từ 0 → k/2:
# // swap hàng (r+i) với hàng (r+k-1-i)
# // ```

# // ⚠️ Nhưng chỉ swap **trong phạm vi c → c+k-1**

# // ---

# // ## 💡 Tóm tắt ngắn gọn

# // * Chọn hình vuông con kích thước ( k \times k )
# // * Đảo thứ tự các hàng trong hình vuông đó
# // * Không thay đổi vị trí cột

# // ---

# // ## 🚀 Nếu bạn đang làm bài code

# // Mình có thể:

# // * Viết code Java (chuẩn theo style bạn thích dùng Scanner)
# // * Hoặc giải chi tiết theo input/output cụ thể của đề bạn đang làm

# // 👉 Bạn gửi đề đầy đủ hoặc input mẫu, mình sẽ giải step-by-step cho bạn luôn.
