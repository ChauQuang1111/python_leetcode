# // Bài “**Find the String with LCP**” (28/03/2026)

# Mình sẽ **giải thích thuật toán + thêm chú thích trực tiếp vào code Python** để bạn đọc là hiểu ngay 👍

# ---

# # 🧠 Ý tưởng cốt lõi

# Bài  gồm 2 bước:

# ### ✅ Bước 1: Xây chuỗi

# * Nếu `lcp[i][j] > 0` → `s[i] == s[j]` → cùng ký tự

# ### ✅ Bước 2: Verify

# * Nếu giống ký tự → phải thỏa:

#   ```
#   lcp[i][j] = 1 + lcp[i+1][j+1]
#   ```
# * Nếu khác ký tự → `lcp[i][j] = 0`

# ---

# # 💻 Code có chú thích chi tiết

# ```python
from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)

        # word[i] sẽ là ký tự tại vị trí i
        # ban đầu để "" nghĩa là chưa gán
        word = [""] * n

        # bắt đầu từ ký tự 'a'
        current = ord("a")

        # =========================
        # BƯỚC 1: XÂY DỰNG CHUỖI
        # =========================
        for i in range(n):

            # nếu vị trí i chưa được gán ký tự
            if not word[i]:

                # nếu vượt quá 'z' → không thể tạo chuỗi
                if current > ord("z"):
                    return ""

                # gán ký tự hiện tại cho vị trí i
                word[i] = chr(current)

                # lan sang các vị trí j > i
                for j in range(i + 1, n):

                    # nếu lcp[i][j] > 0 → 2 vị trí phải cùng ký tự
                    if lcp[i][j]:
                        word[j] = word[i]

                # tăng ký tự cho nhóm tiếp theo
                current += 1

        # =========================
        # BƯỚC 2: KIỂM TRA LẠI LCP
        # =========================
        # duyệt từ dưới lên để dùng được lcp[i+1][j+1]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                # TRƯỜNG HỢP 1: 2 ký tự khác nhau
                if word[i] != word[j]:

                    # nếu khác mà lcp > 0 → sai
                    if lcp[i][j]:
                        return ""

                else:
                    # TRƯỜNG HỢP 2: 2 ký tự giống nhau

                    # nếu ở cuối chuỗi
                    if i == n - 1 or j == n - 1:

                        # chỉ còn 1 ký tự → LCP phải = 1
                        if lcp[i][j] != 1:
                            return ""

                    else:
                        # áp dụng công thức LCP:
                        # lcp[i][j] = 1 + lcp[i+1][j+1]
                        if lcp[i][j] != lcp[i + 1][j + 1] + 1:
                            return ""

        # nếu mọi thứ đúng → trả về chuỗi
        return "".join(word)
# ```

# ---

# # 🔥 Hiểu nhanh bằng 3 dòng

# * `lcp[i][j] > 0` → **cùng ký tự**
# * `lcp[i][j] = 0` → **khác ký tự**
# * Nếu cùng ký tự → phải thỏa:

#   ```
#   lcp[i][j] = 1 + lcp[i+1][j+1]
#   ```

# ---

# # ⚠️ Lỗi hay gặp (rất quan trọng)

# 1. ❌ Gán sai nhóm → xung đột ký tự
# 2. ❌ Quên check `lcp[i+1][j+1]`
# 3. ❌ Không xét case cuối chuỗi (`=1`)

# ---

# # 🚀 Nếu bạn muốn học sâu hơn

# Mình có thể:

# * Trace từng bước với input cụ thể (rất dễ hiểu)
# * Viết bản **Union-Find tối ưu hơn**
# * Hoặc cho bạn **bài tương tự để luyện thi**

# Chỉ cần nói: *"trace cho mình"* là mình làm luôn 👍







# import java.util.*;
# public class b228 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         // nhập n (kích thước ma trận)
#         int n = sc.nextInt();

#         int[][] lcp = new int[n][n];

#         // nhập ma trận LCP
#         int i = 0;
#         while (i < n) {
#             int j = 0;
#             while (j < n) {
#                 lcp[i][j] = sc.nextInt();
#                 j++;
#             }
#             i++;
#         }

#         String result = findTheString(lcp);

#         // nếu impossible thì in ""
#         if (result.equals("")) {
#             System.out.println("Impossible");
#         } else {
#             System.out.println(result);
#         }

#         sc.close();

#     }

#     public static String findTheString(int[][] lcp) {
#         int n = lcp.length;
#         char[] word = new char[n];
#         char current = 'a';

#         // ========================
#         // BƯỚC 1: XÂY DỰNG CHUỖI
#         // ========================
#         for (int i = 0; i < n; i++) {

#             // nếu vị trí i chưa được gán ký tự
#             if (word[i] == 0) {

#                 // nếu vượt quá 'z' thì không thể tạo chuỗi
#                 if (current > 'z') {
#                     return "";
#                 }

#                 // gán ký tự hiện tại cho vị trí i
#                 word[i] = current;

#                 int j = i + 1;

#                 // lan sang các vị trí có lcp > 0 (cùng ký tự)
#                 while (j < n) {
#                     if (lcp[i][j] > 0) {
#                         word[j] = word[i];
#                     }
#                     j++;
#                 }

#                 // tăng ký tự cho nhóm tiếp theo
#                 current++;
#             }
#         }

#         // ========================
#         // BƯỚC 2: VERIFY LẠI LCP
#         // ========================
#         for (int i = n - 1; i >= 0; i--) {
#             for (int j = n - 1; j >= 0; j--) {

#                 // nếu 2 ký tự khác nhau
#                 if (word[i] != word[j]) {

#                     // LCP phải = 0
#                     if (lcp[i][j] != 0) {
#                         return "";
#                     }

#                 } else {
#                     // nếu cùng ký tự

#                     // trường hợp ở cuối chuỗi
#                     if (i == n - 1 || j == n - 1) {

#                         // chỉ còn 1 ký tự nên LCP phải = 1
#                         if (lcp[i][j] != 1) {
#                             return "";
#                         }

#                     } else {
#                         // áp dụng công thức:
#                         // lcp[i][j] = lcp[i+1][j+1] + 1
#                         if (lcp[i][j] != lcp[i + 1][j + 1] + 1) {
#                             return "";
#                         }
#                     }
#                 }
#             }
#         }

#         return new String(word);
#     }
# }

# // Mình sẽ giải thích **thuật toán trong code của bạn** theo cách dễ hiểu nhất
# // (đúng kiểu đi thi/đi interview 👍)

# // ---

# // # 🧠 Tổng quan ý tưởng

# // Bài này làm 2 bước:

# // ### ✅ Bước 1: **Xây dựng chuỗi `word`**

# // * Dựa vào `lcp[i][j] > 0` → các vị trí đó **phải cùng ký tự**

# // ### ✅ Bước 2: **Kiểm tra lại (verify)**

# // * Dùng định nghĩa LCP để kiểm tra chuỗi vừa tạo có đúng không

# // ---

# // # 🔧 PHẦN 1: Xây dựng chuỗi

# // ```java
# // char[] word = new char[n];
# // char current = 'a';
# // ```

# // * `word[i] == 0` nghĩa là **chưa được gán ký tự**
# // * `current` chạy từ `'a' → 'z'`

# // ---

# // ## 🔁 Vòng lặp chính

# // ```java
# // for (int i = 0; i < n; i++) {
# // ```

# // 👉 Duyệt từng vị trí

# // ---

# // ## 🔹 Nếu chưa gán ký tự

# // ```java
# // if (word[i] == 0) {
# // ```

# // 👉 Tức là vị trí này chưa thuộc “nhóm” nào

# // ---

# // ## 🔹 Gán ký tự mới

# // ```java
# // word[i] = current;
# // ```

# // 👉 Bắt đầu một nhóm mới (giống Union-Find)

# // ---

# // ## 🔹 Lan sang các vị trí khác

# // ```java
# // for (int j = i + 1; j < n; j++) {
# // if (lcp[i][j] > 0) {
# // word[j] = word[i];
# // }
# // }
# // ```

# // 👉 Ý nghĩa cực kỳ quan trọng:

# // * Nếu `lcp[i][j] > 0`
# // → `s[i] == s[j]`

# // ➡️ nên gán luôn:

# // ```
# // word[j] = word[i]
# // ```

# // ---

# // ## 🔹 Tăng ký tự

# // ```java
# // current++;
# // ```

# // 👉 Dùng ký tự mới cho nhóm tiếp theo

# // ---

# // ## ❗ Check quá 26 ký tự

# // ```java
# // if (current > 'z') return "";
# // ```

# // 👉 Không đủ chữ cái → impossible

# // ---

# // # 💡 Tóm lại bước 1

# // 👉 Bạn đang:

# // * Gom các vị trí có `lcp > 0` thành **cùng nhóm**
# // * Mỗi nhóm dùng 1 chữ cái

# // ---

# // # 🔍 PHẦN 2: Verify lại LCP

# // Đây là phần **quan trọng nhất để đảm bảo đúng**

# // ---

# // ## 🔁 Duyệt ngược

# // ```java
# // for (int i = n - 1; i >= 0; i--) {
# // for (int j = n - 1; j >= 0; j--) {
# // ```

# // 👉 Vì `lcp[i][j]` phụ thuộc `lcp[i+1][j+1]`

# // ---

# // ## 🔹 Trường hợp 1: khác ký tự

# // ```java
# // if (word[i] != word[j]) {
# // if (lcp[i][j] != 0) return "";
# // }
# // ```

# // 👉 Nếu khác ký tự mà LCP ≠ 0 → sai ngay

# // ---

# // ## 🔹 Trường hợp 2: giống ký tự

# // ```java
# // else {
# // ```

# // ---

# // ### 📌 Case đặc biệt: cuối chuỗi

# // ```java
# // if (i == n - 1 || j == n - 1) {
# // if (lcp[i][j] != 1) return "";
# // }
# // ```

# // 👉 Vì:

# // * chỉ còn 1 ký tự
# // * nếu giống → LCP = 1

# // ---

# // ### 📌 Case tổng quát

# // ```java
# // if (lcp[i][j] != lcp[i + 1][j + 1] + 1) return "";
# // ```

# // 👉 Đây là công thức quan trọng:

# // ## 💥 Công thức LCP:

# // ```
# // Nếu s[i] == s[j]:
# // lcp[i][j] = 1 + lcp[i+1][j+1]
# // ```

# // ---

# // # 🎯 Ví dụ trực quan

# // Giả sử:

# // ```
# // s = "aba"
# // ```

# // LCP matrix:

# // ```
# // 3 0 1
# // 0 2 0
# // 1 0 1
# // ```

# // ---

# // # 🚨 Khi nào return "" (Impossible)?

# // 1. Dùng quá 26 chữ cái
# // 2. Có `lcp > 0` nhưng ký tự khác
# // 3. Vi phạm công thức:

# // ```
# // lcp[i][j] != lcp[i+1][j+1] + 1
# // ```

# // ---

# // # 🧩 Tóm tắt cực ngắn

# // 👉 Build:

# // * `lcp[i][j] > 0` → cùng nhóm

# // 👉 Check:

# // * khác ký tự → LCP phải = 0
# // * giống ký tự → LCP = 1 + LCP phía sau

# // ---

# // # 🚀 Nếu bạn muốn hiểu sâu hơn

# // Mình có thể:

# // * Trace từng dòng code với input cụ thể
# // * Hoặc viết lại version **dễ hiểu hơn (ít bug hơn)**
# // * Hoặc chuyển sang kiểu **Union-Find chuẩn**

# // Bạn muốn mình giải kiểu nào tiếp?

# // ## 🧠 1. LCP là gì?

# // **LCP (Longest Common Prefix)** = độ dài tiền tố chung dài nhất của 2 chuỗi
# // con.

# // Ví dụ với chuỗi `s = "ababa"`:

# // * LCP(0,2): so sánh `"ababa"` và `"aba"` → giống `"aba"` → LCP = 3
# // * LCP(1,3): `"baba"` vs `"ba"` → giống `"ba"` → LCP = 2

# // ---

# // ## 📥 2. Đề bài cho gì?

# // Bạn được cho một **ma trận `lcp[n][n]`**, trong đó:

# // * `lcp[i][j]` = độ dài tiền tố chung dài nhất của:

# // * chuỗi con bắt đầu tại i
# // * chuỗi con bắt đầu tại j

# // 👉 Nói đơn giản:
# // `lcp[i][j] = LCP(s[i:], s[j:])`

# // ---

# // ## 🎯 3. Nhiệm vụ

# // 👉 **Tìm một chuỗi s** (chỉ gồm ký tự `'a' → 'z'`) sao cho tạo ra đúng ma
# // trận LCP đã cho.

# // * Nếu **không tồn tại** → trả về `"Impossible"`

# // ---

# // ## 🔍 4. Ý nghĩa quan trọng

# // Từ định nghĩa LCP:

# // ### Nếu `lcp[i][j] > 0` thì:

# // 👉 `s[i] == s[j]`

# // Vì có ít nhất 1 ký tự đầu giống nhau

# // ---

# // ### Nếu `lcp[i][j] = k > 0` thì:

# // 👉

# // * `s[i] == s[j]`
# // * `lcp[i+1][j+1] = k - 1`

# // ---

# // ### Nếu `lcp[i][j] = 0` thì:

# // 👉 `s[i] != s[j]`

# // ---

# // ## ⚙️ 5. Cách giải (ý tưởng chính)

# // ### 🔹 Bước 1: Gán ký tự cho chuỗi

# // * Duyệt từ trái → phải
# // * Nếu `s[i]` chưa gán:

# // * gán `'a'`, `'b'`, `'c'`... (tối đa 26 chữ cái)
# // * với mọi `j` mà `lcp[i][j] > 0` → gán `s[j] = s[i]`

# // 👉 giống kiểu **Union-Find / grouping**

# // ---

# // ### 🔹 Bước 2: Kiểm tra lại ma trận

# // Sau khi có chuỗi `s`, ta **tính lại LCP** và so sánh với input:

# // * Nếu khác → `"Impossible"`
# // * Nếu đúng → in chuỗi

# // ---

# // ## 📌 6. Ví dụ

# // ### Input:

# // ```
# // lcp =
# // [3 0 1
# // 0 2 0
# // 1 0 1]
# // ```

# // ### Phân tích:

# // * `lcp[0][2] = 1` → s[0] = s[2]
# // * `lcp[0][1] = 0` → s[0] != s[1]

# // 👉 Có thể là:

# // ```
# // s = "aba"
# // ```

# // ---

# // ## ❌ Trường hợp Impossible

# // Nếu mâu thuẫn, ví dụ:

# // * `lcp[i][j] > 0` nhưng `lcp[i+1][j+1] != lcp[i][j] - 1`
# // * hoặc bắt buộc vừa bằng vừa khác

# // → Không thể tạo chuỗi

# // ---

# // ## 🧩 7. Tóm tắt dễ nhớ

# // * `lcp[i][j] > 0` → cùng ký tự
# // * `lcp[i][j] = 0` → khác ký tự
# // * Build chuỗi bằng grouping
# // * Verify lại toàn bộ matrix

# // ---

# // ## 🚀 Nếu bạn muốn

# // Mình có thể:

# // * Viết code Java (chuẩn theo style bạn đang dùng)
# // * Hoặc giải từng dòng test cụ thể cho bạn hiểu sâu hơn

# // Chỉ cần gửi đề full hoặc input 👍
