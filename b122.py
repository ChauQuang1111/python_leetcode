
# // Delete Columns to Make Sorted(20/12/2025)
# // **Delete Columns to Make Sorted – Giải thích đề bài (tiếng Việt)**
# Mình sẽ **giải thích thuật toán + thêm chú thích trực tiếp vào code Python** cho bài **LeetCode 944 – Delete Columns to Make Sorted**, theo đúng mức dễ hiểu 👍

# ---

# ## 🧠 Ý tưởng thuật toán

# * Mỗi **cột** của các chuỗi được kiểm tra **độc lập**
# * Nếu các ký tự trong cột **không tăng dần từ trên xuống**
#   → cột đó phải bị **xóa**
# * Đếm số cột bị xóa

# ---

# ## 🔍 Giải thích chi tiết từng phần

# ### 1️⃣ `zip(*strs)` làm gì?

# Giả sử:

# ```python
# strs = ["cba", "daf", "ghi"]
# ```

# ```python
# zip(*strs)
# ```

# sẽ tạo ra:

# ```
# ('c','d','g')   # cột 0
# ('b','a','h')   # cột 1
# ('a','f','i')   # cột 2
# ```

# 👉 Mỗi tuple chính là **một cột**

# ---

# ### 2️⃣ Kiểm tra cột có được sắp xếp không

# * `sorted(i)` → danh sách ký tự tăng dần
# * Nếu `list(i) != sorted(i)`
#   → cột **không tăng dần** → phải xóa

# ---

# ## ✅ Code có chú thích chi tiết

# ```python
from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        counter = 0  # đếm số cột cần xóa

        # zip(*strs) gom các ký tự cùng vị trí của mỗi chuỗi thành 1 cột
        for col in zip(*strs):

            # Nếu cột hiện tại không được sắp xếp tăng dần
            # (tức là tồn tại ký tự phía trên > ký tự phía dưới)
            if list(col) != sorted(col):
                counter += 1  # phải xóa cột này

        return counter
# ```

# ---

# ## 📌 Ví dụ minh họa

# ```python
# strs = ["cba", "daf", "ghi"]
# ```

# | Cột | Giá trị       | sorted        | Xóa? |
# | --- | ------------- | ------------- | ---- |
# | 0   | ('c','d','g') | ['c','d','g'] | ❌    |
# | 1   | ('b','a','h') | ['a','b','h'] | ✅    |
# | 2   | ('a','f','i') | ['a','f','i'] | ❌    |

# ➡️ Kết quả: `1`

# ---

# ## ⏱ Độ phức tạp

# * **Thời gian**: `O(m × n log m)`

#   * `m`: số chuỗi
#   * `n`: độ dài chuỗi
# * **Bộ nhớ**: `O(m)` cho mỗi cột

# > 💡 Java thường dùng so sánh từng cặp để đạt `O(m × n)`,
# > Python dùng `sorted()` nên code gọn hơn nhưng chậm hơn chút.

# ---

# Nếu bạn muốn:

# * 🔹 Phiên bản **Python tối ưu không dùng `sorted`**
# * 🔹 So sánh Python vs Java
# * 🔹 Giải thích lại theo phong cách **phỏng vấn**

# 👉 Cứ nói, mình làm tiếp cho bạn nhé 🚀

# import java.util.*;

# public class b123 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int m = sc.nextInt();
#         sc.nextLine(); // bỏ dòng thừa sau khi nhập số

#         String[] strs = new String[m];

#         // Nhập từng chuỗi
#         for (int i = 0; i < m; i++) {
#             strs[i] = sc.nextLine();
#         }

#         // Gọi hàm giải
#         int result = minDeletionSize(strs);

#         // In kết quả
#         System.out.println(result);

#         sc.close();
#     }

#     // Hàm chính giải bài toán
#     public static int minDeletionSize(String[] strs) {
#         int m = strs.length; // số hàng (số chuỗi)
#         int count = 0; // đếm số cột cần xóa

#         // Chuyển String[] sang char[][] để dễ xử lý
#         char[][] matrix = new char[m][];
#         for (int i = 0; i < m; i++) {
#             matrix[i] = strs[i].toCharArray();
#         }

#         int n = matrix[0].length; // số cột

#         // Duyệt từng cột
#         for (int col = 0; col < n; col++) {
#             // Nếu cột không được sắp xếp tăng dần → phải xóa
#             if (!isSort(matrix, col)) {
#                 count++;
#             }
#         }

#         return count;
#     }

#     // Hàm kiểm tra 1 cột có được sắp xếp tăng dần không
#     public static boolean isSort(char[][] mat, int col) {
#         // So sánh các hàng liên tiếp trong cùng một cột
#         for (int row = 0; row < mat.length - 1; row++) {
#             if (mat[row][col] > mat[row + 1][col]) {
#                 return false; // phát hiện cột "xấu"
#             }
#         }
#         return true; // cột hợp lệ
#     }

# }

# // **Mô tả ngắn gọn:**
# // Bạn được cho một mảng các chuỗi `strs`, **tất cả các chuỗi có cùng độ dài**.
# // Mỗi chuỗi là **một hàng**, các ký tự cùng vị trí tạo thành **một cột**.
# // Nhiệm vụ của bạn là **xóa ít nhất bao nhiêu cột** sao cho **sau khi xóa**,
# // các chuỗi còn lại **được sắp xếp theo thứ tự từ điển (lexicographically)
# // không giảm**.

# // ---

# // ### Hiểu đơn giản hơn

# // * Hãy tưởng tượng các chuỗi xếp thành bảng:

# // * Mỗi **hàng** = 1 chuỗi
# // * Mỗi **cột** = các ký tự ở cùng vị trí
# // * Bạn được **xóa cả cột** (xóa cùng một vị trí ở tất cả chuỗi)
# // * Mục tiêu: sau khi xóa, danh sách chuỗi phải **tăng dần theo từ điển**

# // ---

# // ### Khi nào một cột “xấu”?

# // Một cột là **xấu** nếu **từ trên xuống dưới**, ký tự **không tăng dần** (tức
# // là có ký tự phía dưới **nhỏ hơn** ký tự phía trên).

# // 📌 Nếu tồn tại `i < j` mà
# // `strs[i][col] > strs[j][col]`
# // → cột đó phải bị xóa.

# // ---

# // ### Ví dụ 1

# // ```
# // strs = ["cba", "daf", "ghi"]
# // ```

# // Xét từng cột:

# // * **Cột 0**: `c, d, g` → tăng dần ✅
# // * **Cột 1**: `b, a, h` → `b > a` ❌ (không tăng)
# // * **Cột 2**: `a, f, i` → tăng dần ✅

# // ➡️ Cột 1 là cột xấu → **xóa 1 cột**

# // **Kết quả:** `1`

# // ---

# // ### Ví dụ 2

# // ```
# // strs = ["a", "b"]
# // ```

# // * Cột 0: `a, b` → tăng dần ✅
# // ➡️ Không cần xóa cột nào

# // **Kết quả:** `0`

# // ---

# // ### Ví dụ 3

# // ```
# // strs = ["zyx", "wvu", "tsr"]
# // ```

# // * Cột 0: `z, w, t` → giảm ❌
# // * Cột 1: `y, v, s` → giảm ❌
# // * Cột 2: `x, u, r` → giảm ❌

# // ➡️ Phải xóa **tất cả 3 cột**

# // **Kết quả:** `3`

# // ---

# // ### Ý tưởng giải (tư duy)

# // 1. Duyệt từng **cột**
# // 2. So sánh các ký tự **theo hàng từ trên xuống**
# // 3. Nếu phát hiện **giảm**, tăng biến đếm và bỏ qua cột đó

# // ---

# // Nếu bạn muốn:

# // * Mình có thể **viết code Java / Python**
# // * Hoặc **giải thích lại bằng hình minh họa bảng**
# // * Hoặc **so sánh với bài tương tự trên LeetCode**

# // 👉 Cứ nói nhé!

# // Mình sẽ **giải thích thuật toán của đoạn code này từng bước, đúng theo tư duy
# // LeetCode 944 – Delete Columns to Make Sorted**, dùng tiếng Việt dễ hiểu.

# // ---

# // ## 1️⃣ Ý tưởng tổng quát của thuật toán

# // 👉 **Mỗi cột được kiểm tra độc lập**

# // * Nếu **cột đó không được sắp xếp tăng dần từ trên xuống**, ta **phải xóa cột
# // đó**
# // * Đếm xem có bao nhiêu cột “xấu”

# // ⏱ **Độ phức tạp**:

# // * Thời gian: `O(m × n)`

# // * `m` = số chuỗi (số hàng)
# // * `n` = độ dài mỗi chuỗi (số cột)
# // * Bộ nhớ: `O(m × n)` (do chuyển sang `char[][]`)

# // ---

# // ## 2️⃣ Phân tích chi tiết từng phần code

# // ---

# // ### 🔹 Hàm `minDeletionSize`

# // ```java
# // public int minDeletionSize(String[] strs) {
# // ```

# // 📌 Hàm chính: trả về **số cột cần xóa**

# // ---

# // ### 🔹 Lấy số hàng & chuẩn bị biến đếm

# // ```java
# // int m = strs.length, count = 0;
# // ```

# // * `m`: số chuỗi (số hàng)
# // * `count`: số cột cần xóa

# // ---

# // ### 🔹 Chuyển String[] → char[][]

# // ```java
# // char[][] matrix = new char[m][];

# // for (int i = 0; i < m; i++) {
# // matrix[i] = strs[i].toCharArray();
# // }
# // ```

# // 📌 Mục đích:

# // * Dễ truy cập ký tự theo **hàng & cột**: `matrix[row][col]`

# // Ví dụ:

# // ```
# // strs = ["cba", "daf", "ghi"]

# // matrix =
# // c b a
# // d a f
# // g h i
# // ```

# // ---

# // ### 🔹 Lấy số cột

# // ```java
# // int n = matrix[0].length;
# // ```

# // * Vì đề bài đảm bảo **mọi chuỗi cùng độ dài**
# // * `n` = số cột

# // ---

# // ### 🔹 Duyệt từng cột

# // ```java
# // for (int i = 0; i < n; i++) {
# // if (!isSort(matrix, i)) count++;
# // }
# // ```

# // 👉 Với mỗi cột `i`:

# // * Gọi `isSort(matrix, i)`
# // * Nếu **cột KHÔNG tăng dần** → `count++`

# // ---

# // ## 3️⃣ Hàm `isSort` – Trái tim của thuật toán ❤️

# // ```java
# // private boolean isSort(char[][] mat, int col) {
# // ```

# // 📌 Kiểm tra **cột `col` có được sắp xếp không**

# // ---

# // ### 🔹 So sánh từng cặp hàng liên tiếp

# // ```java
# // for (int i = 0; i < mat.length - 1; i++) {
# // ```

# // * So sánh:

# // ```
# // mat[0][col] với mat[1][col]
# // mat[1][col] với mat[2][col]
# // ...
# // ```

# // ---

# // ### 🔹 Phát hiện cột “xấu”

# // ```java
# // if (mat[i][col] > mat[i + 1][col]) {
# // return false;
# // }
# // ```

# // 📌 Nếu:

# // ```
# // ký tự phía trên > ký tự phía dưới
# // ```

# // ➡️ Cột **không tăng dần**
# // ➡️ Phải xóa → `return false`

# // ---

# // ### 🔹 Nếu duyệt xong không lỗi

# // ```java
# // return true;
# // ```

# // ➡️ Cột hợp lệ, **giữ lại được**

# // ---

# // ## 4️⃣ Ví dụ minh họa chạy code

# // ### Input

# // ```java
# // strs = ["cba", "daf", "ghi"]
# // ```

# // ### Kiểm tra từng cột:

# // | Cột | Ký tự | isSort |
# // | --- | ----- | ------- |
# // | 0 | c d g | true |
# // | 1 | b a h | false ❌ |
# // | 2 | a f i | true |

# // ➡️ `count = 1`

# // ---

# // ## 5️⃣ Kết luận thuật toán

# // ✅ **Chiến lược:**

# // * Duyệt từng cột
# // * Nếu cột không tăng dần → xóa

# // ✅ **Ưu điểm:**

# // * Code gọn
# // * Dễ hiểu
# // * Đúng chuẩn tư duy LeetCode

# // ## 6️⃣ Gợi ý tối ưu (nâng cao)

# // 👉 Không cần tạo `char[][]`, có thể dùng trực tiếp:

# // ```java
# // strs[i].charAt(col)
# // ```

# // → tiết kiệm bộ nhớ

# // Nếu bạn muốn:

# // * 🔹 Phiên bản tối ưu
# // * 🔹 Vẽ bảng mô phỏng từng bước
# // * 🔹 So sánh với bài **Delete Columns to Make Sorted II**

# // 👉 Cứ nói, mình giải tiếp cho bạn 👍
