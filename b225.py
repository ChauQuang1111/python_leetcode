# # // Construct Product Matrix(24/03/2026)
# # // “**Construct Product Matrix**” nghĩa là: **tính (xây dựng) ma trận tích của hai ma trận đã cho**.

# Đây là phiên bản Python cực ngắn của cùng thuật toán **prefix + suffix (product except self)**. Mình sẽ:

# 1. Giải thích từng dòng
# 2. Viết lại code có **chú thích rõ ràng**

# ---

# # 🧠 Ý tưởng chính (giống Java)

# * Flatten ma trận → mảng 1D
# * Tạo:

#   * `pref[i]` = tích các phần tử trước i
#   * `suff[i]` = tích các phần tử sau i
# * Kết quả = `pref[i] * suff[i]`

# ---

# # 🔍 Giải thích code của bạn

# ```python
# f = lambda a:[1,*accumulate(a,lambda q,v:q*v%12345)]
# ```

# 👉 Hàm `f` tạo prefix product

# * `accumulate` = tích dồn
# * `[1, ...]` để thêm phần tử đầu = 1

# ---

# ```python
# pref = f(chain(*g))
# ```

# 👉 Flatten ma trận:

# * `chain(*g)` → biến 2D thành 1D
# * rồi tính prefix

# ---

# ```python
# suff = f(chain(*map(reversed,reversed(g))))[::-1]
# ```

# 👉 Trick hơi “hack não”:

# * `reversed(g)` → đảo thứ tự hàng

# * `reversed(row)` → đảo từng hàng
#   → mục đích: tạo **suffix nhưng dùng lại prefix**

# * `[::-1]` → đảo lại để đúng vị trí

# ---

# ```python
# b = (v*u%12345 for v,u in zip(pref,suff[1:]))
# ```

# 👉 Tính kết quả:

# * `pref[i] * suff[i+1]`
# * bỏ chính nó

# ---

# ```python
# return [*zip(*[iter(b)]*len(g[0]))]
# ```

# 👉 Convert lại 1D → 2D

# * chia mảng thành từng dòng dài `n`

# ---

# # ✅ Code có chú thích rõ ràng

# ```python
from itertools import accumulate, chain
from typing import List

class Solution:
    def constructProductMatrix(self, g: List[List[int]]) -> List[List[int]]:
        mod = 12345

        # Hàm tính prefix product
        # Ví dụ: [1,2,3] -> [1,1,2,6]
        f = lambda a: [1, *accumulate(a, lambda q, v: q * v % mod)]

        # Bước 1: Flatten ma trận (2D -> 1D)
        flat = list(chain(*g))

        # Bước 2: Prefix product
        pref = f(flat)

        # Bước 3: Suffix product (dùng trick đảo ngược)
        # Đảo ma trận + đảo từng hàng để flatten ngược
        reversed_flat = list(chain(*map(reversed, reversed(g))))
        
        # Tính prefix trên mảng đảo (tương đương suffix)
        suff = f(reversed_flat)[::-1]  # đảo lại cho đúng thứ tự

        # Bước 4: Tính kết quả (product except self)
        # pref[i] * suff[i+1]
        result_1d = (p * s % mod for p, s in zip(pref, suff[1:]))

        # Bước 5: Chuyển lại thành ma trận 2D
        n = len(g[0])
        result_2d = [list(row) for row in zip(*[iter(result_1d)] * n)]

        return result_2d
# ```

# ---

# # ⚡ Tóm tắt dễ nhớ

# 👉 Code Python này làm 4 việc:

# 1. Flatten ma trận
# 2. Prefix product
# 3. “Fake suffix” bằng reverse
# 4. Zip lại thành matrix

# ---

# # 🚨 Điểm khó nhất

# 👉 Dòng này:

# ```python
# map(reversed, reversed(g))
# ```

# = **đảo toàn bộ ma trận theo thứ tự ngược**

# ---

# Nếu bạn muốn, mình có thể:

# * viết lại version Python **dễ đọc hơn (không hack)**
# * hoặc so sánh Python vs Java để bạn hiểu sâu hơn 👍





# import java.util.*;

# public class b226 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         // Nhập số hàng và cột
#         int m = sc.nextInt();
#         int n = sc.nextInt();

#         int[][] g = new int[m][n];

#         // Nhập ma trận
#         for (int i = 0; i < m; i++) {
#             for (int j = 0; j < n; j++) {
#                 g[i][j] = sc.nextInt();
#             }
#         }

#         int[][] result = constructProductMatrix(g);

#         // In kết quả
#         for (int i = 0; i < m; i++) {
#             for (int j = 0; j < n; j++) {
#                 System.out.print(result[i][j] + " ");
#             }
#             System.out.println();
#         }

#         sc.close();
#     }

#     // Hàm chính xử lý bài toán
#     public static int[][] constructProductMatrix(int[][] g) {
#         int m = g.length;
#         int n = g[0].length;
#         int size = m * n;
#         int mod = 12345;

#         // Mảng 1D để lưu toàn bộ phần tử
#         int[] a = new int[size];

#         // Prefix product
#         long[] p = new long[size];

#         // Suffix product
#         long[] s = new long[size];

#         // Bước 1: Flatten ma trận 2D -> 1D
#         int idx = 0;
#         for (int i = 0; i < m; i++) {
#             for (int j = 0; j < n; j++) {
#                 a[idx++] = g[i][j];
#             }
#         }

#         // Bước 2: Tính prefix product
#         // p[i] = tích các phần tử trước i
#         p[0] = 1;
#         for (int i = 1; i < size; i++) {
#             p[i] = (p[i - 1] * a[i - 1]) % mod;
#         }

#         // Bước 3: Tính suffix product
#         // s[i] = tích các phần tử sau i
#         s[size - 1] = 1;
#         for (int i = size - 2; i >= 0; i--) {
#             s[i] = (a[i + 1] * s[i + 1]) % mod;
#         }

#         // Bước 4: Gán lại kết quả vào ma trận
#         idx = 0;
#         for (int i = 0; i < m; i++) {
#             for (int j = 0; j < n; j++) {
#                 // product except self = prefix * suffix
#                 g[i][j] = (int) ((p[idx] * s[idx]) % mod);
#                 idx++;
#             }
#         }

#         return g;
#     }
# }

# // ---

# // ## 📌 1. Hiểu đề bài

# // Giả sử đề cho:

# // * Ma trận (A) kích thước (m \times n)
# // * Ma trận (B) kích thước (n \times p)

# // 👉 Điều kiện để nhân được:

# // * **Số cột của A = số hàng của B**

# // ---

# // ## 📌 2. Công thức nhân ma trận

# // Kết quả (C = A \times B) sẽ có kích thước (m \times p)

# // Cách tính từng phần tử:

# // c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}

# // 👉 Hiểu đơn giản:

# // * Lấy **hàng i của A**
# // * Nhân với **cột j của B**
# // * Rồi cộng lại

# // ---

# // ## 📌 3. Ví dụ cụ thể

# // Cho:
# // [
# // A = \begin{bmatrix}
# // 1 & 2 \
# // 3 & 4
# // \end{bmatrix}, \quad
# // B = \begin{bmatrix}
# // 5 & 6 \
# // 7 & 8
# // \end{bmatrix}
# // ]

# // Tính (C = A \times B):

# // * (C_{11} = 1×5 + 2×7 = 19)
# // * (C_{12} = 1×6 + 2×8 = 22)
# // * (C_{21} = 3×5 + 4×7 = 43)
# // * (C_{22} = 3×6 + 4×8 = 50)

# // 👉 Kết quả:
# // [
# // C = \begin{bmatrix}
# // 19 & 22 \
# // 43 & 50
# // \end{bmatrix}
# // ]

# // ---

# // ## 📌 4. Cách làm nhanh khi đi thi

# // 1. Kiểm tra có nhân được không
# // 2. Xác định kích thước ma trận kết quả
# // 3. Lấy **hàng × cột** (row × column)
# // 4. Tính lần lượt từng phần tử

# // ---

# // ## 📌 5. Mẹo tránh sai

# // * ❌ Nhân nhầm hàng với hàng
# // * ❌ Quên điều kiện số cột = số hàng
# // * ❌ Cộng thiếu phần tử

# // ---

# // Nếu bạn muốn, gửi mình đề cụ thể (ảnh hoặc text), mình giải từng bước cho bạn
# // luôn 👍
# // Bài **2906. Construct Product Matrix** yêu cầu:

# // 👉 Với mỗi ô (g[i][j]), bạn phải tính:

# // * **tích của tất cả phần tử trong ma trận TRỪ chính nó**
# // * và lấy **mod 12345**

# // ---

# // ## 🔥 Ý tưởng chính của thuật toán bạn viết

# // Nếu làm brute force:

# // * Với mỗi phần tử → duyệt toàn bộ ma trận → (O((mn)^2)) ❌ quá chậm

# // 👉 Bạn đã dùng kỹ thuật **Prefix Product + Suffix Product** (giống bài
# // “product of array except self”) → **O(mn)** ✅

# // ---

# // ## 📌 Bước 1: Flatten ma trận

# // ```java
# // int a[] = new int[size];
# // ```

# // 👉 Biến ma trận 2D thành mảng 1D:

# // Ví dụ:

# // ```
# // g = [[1,2],
# // [3,4]]

# // → a = [1,2,3,4]
# // ```

# // ---

# // ## 📌 Bước 2: Prefix product (p)

# // ```java
# // p[0] = 1;
# // for(int i=1;i<p.length;i++){
# // p[i] =(p[i-1]*a[i-1])%mod;
# // }
# // ```

# // 👉 `p[i]` = tích các phần tử **trước i**

# // Ví dụ:

# // ```
# // a = [1,2,3,4]

# // p = [1, 1, 2, 6]
# // ```

# // ---

# // ## 📌 Bước 3: Suffix product (s)

# // ```java
# // s[s.length-1]= 1;
# // for(int i=a.length-2;i>=0;i--){
# // s[i]= (a[i+1]*s[i+1])%mod;
# // }
# // ```

# // 👉 `s[i]` = tích các phần tử **sau i**

# // Ví dụ:

# // ```
# // s = [24, 12, 4, 1]
# // ```

# // ---

# // ## 📌 Bước 4: Kết hợp

# // ```java
# // g[i][j]=(int)(p[idx]*s[idx])%mod;
# // ```

# // 👉 Với mỗi vị trí:

# // * **kết quả = prefix × suffix**
# // * tức là:
# // [
# // \text{product except self}
# // ]

# // ---

# // ## 🧠 Tại sao đúng?

# // Tại vị trí `i`:

# // * `p[i]` = a[0] * a[1] * ... * a[i-1]
# // * `s[i]` = a[i+1] * ... * a[n-1]

# // 👉 Nhân lại:
# // [
# // p[i] \times s[i] = \text{tất cả phần tử trừ a[i]}
# // ]

# // ---

# // ## 📌 Ví dụ full

# // ```
# // a = [1,2,3,4]

# // p = [1,1,2,6]
# // s = [24,12,4,1]

# // kq:
# // [24,12,8,6]
# // ```

# // ---

# // ## ⚡ Độ phức tạp

# // * Time: **O(m × n)**
# // * Space: **O(m × n)**

# // ---

# // ## 🚨 Điểm quan trọng bạn làm đúng

# // ✔ Không dùng chia (tránh lỗi khi có số 0)
# // ✔ Dùng mod để tránh overflow
# // ✔ Duyệt 1 lần prefix + 1 lần suffix

# // ---

# // ## ❗ Lưu ý nhỏ

# // Dòng này hơi thừa:

# // ```java
# // p[0]= g[0][0];
# // ```

# // 👉 Sau đó bạn gán lại:

# // ```java
# // p[0]=1;
# // ```

# // → Có thể xóa dòng đầu

# // ---

# // ## 🎯 Tóm tắt cực ngắn

# // 👉 Bài này là:

# // * Biến 2D → 1D
# // * Dùng prefix + suffix
# // * Nhân lại để loại chính nó

# // ---

# // Nếu bạn muốn, mình có thể:

# // * vẽ hình minh họa cho dễ hiểu hơn
# // * hoặc tối ưu code xuống **O(1) space** luôn 👍
