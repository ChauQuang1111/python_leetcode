# # // *Minimum ASCII Delete Sum for Two Strings(10/01/2026)
# # //  Mình giải thích **thuật toán + từng dòng code** của bạn theo **tư duy DP (LCS theo ASCII)**, ngắn gọn – đúng trọng tâm LeetCode 712.
# Mình sẽ **giải thích thuật toán + thêm chú thích rõ ràng ngay trong code Python** của bạn, giữ đúng **tư duy DP 1D tối ưu bộ nhớ** cho bài **712**.

# ---

# ## 1. Ý tưởng thuật toán (tóm tắt trước)

# * Ta **không tính chi phí xóa trực tiếp**
# * Mà tìm **chuỗi con chung có tổng ASCII lớn nhất**
# * Dùng **DP 1 chiều** để tối ưu bộ nhớ
# * Kết quả:

# ```
# (answer) = ASCII(s1) + ASCII(s2) − 2 × ASCII(common subsequence)
# ```

# ---

# ## 2. Code Python (đã thêm chú thích chi tiết)

# ```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        len1, len2 = len(s1), len(s2)

        """
        dp[j] = tổng ASCII lớn nhất của chuỗi con chung
                giữa s1[0..i-1] và s2[0..j-1]
        Ban đầu i = 0 → chưa xét ký tự nào của s1
        """

        # Khởi tạo DP 1 chiều
        dp = [0] * (len2 + 1)

        # Duyệt từng ký tự của s1 (từng "hàng" DP)
        for i in range(1, len1 + 1):

            # dp_new đại diện cho hàng hiện tại (i)
            # copy dp cũ để giữ giá trị khi "bỏ s1[i]"
            dp_new = dp.copy()

            # Duyệt từng ký tự của s2 (từng "cột")
            for j in range(1, len2 + 1):

                # Nếu hai ký tự trùng nhau
                if s1[i - 1] == s2[j - 1]:
                    """
                    Giữ ký tự này:
                    - ord(s2[j-1]) là ASCII của ký tự
                    - dp[j-1] là giá trị từ hàng trước, cột trước
                    """
                    dp_new[j] = ord(s2[j - 1]) + dp[j - 1]

                else:
                    """
                    Không trùng:
                    - dp[j]     : bỏ s1[i-1] (nhìn lên trên)
                    - dp_new[j-1]: bỏ s2[j-1] (nhìn sang trái)
                    → chọn phương án tốt hơn
                    """
                    dp_new[j] = max(dp[j], dp_new[j - 1])

            # Cập nhật dp cho vòng lặp tiếp theo
            dp = dp_new

        # Tổng ASCII của toàn bộ hai chuỗi
        ascii1 = sum(ord(c) for c in s1)
        ascii2 = sum(ord(c) for c in s2)

        """
        dp[len2] = tổng ASCII lớn nhất của chuỗi con chung
        Kết quả = tổng ASCII - 2 * ASCII chung
        """
        return ascii1 + ascii2 - 2 * dp[len2]
# ```

# ---

# ## 3. Diễn giải ngắn gọn DP 1D (rất hay ra phỏng vấn)

# * `dp[j]` = **LCS-ASCII** của:

#   ```
#   s1[0..i-1] và s2[0..j-1]
#   ```

# * Khi cập nhật:

#   * `dp[j]` → giá trị **hàng cũ**
#   * `dp_new[j-1]` → giá trị **hàng hiện tại**

# ➡️ Nhờ vậy chỉ cần **O(m)** bộ nhớ.

# ---

# ## 4. Ví dụ nhanh

# ```
# s1 = "sea"
# s2 = "eat"
# ```

# Chuỗi con chung tốt nhất: `"ea"`

# ```
# ASCII("e") = 101
# ASCII("a") = 97
# → dp[len2] = 198
# ```

# ```
# ASCII tổng = 627
# Kết quả = 627 − 2×198 = 231
# ```

# ---

# ## 5. Độ phức tạp

# | Loại  | Giá trị  |
# | ----- | -------- |
# | Time  | O(n × m) |
# | Space | O(m)     |

# ---

# ## 6. Một câu chốt để nhớ lâu

# > **Bài 712 = LCS nhưng tối đa hóa tổng ASCII, không phải độ dài**

# ---

# Nếu bạn muốn, mình có thể:

# * 🔁 Viết lại theo **tư duy xóa trực tiếp**
# * 📊 Vẽ bảng DP minh họa từng bước
# * ⚡ So sánh bản **2D vs 1D**

# 👉 chỉ cần nói nhé 👍

# import java.util.*;

# public class b144 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         String s1 = sc.nextLine();

#         // Nhập chuỗi thứ hai
#         String s2 = sc.nextLine();

#         int result = minimumDeleteSum(s1, s2);

#         // In kết quả
#         System.out.println(result);

#         sc.close();
#     }

#     static int minimumDeleteSum(String s1, String s2) {
#         // Chuyển chuỗi sang mảng ký tự để xử lý nhanh hơn
#         char[] a = s1.toCharArray();
#         char[] b = s2.toCharArray();

#         int n = a.length;
#         int m = b.length;

#         /*
#          * dp[i][j]: tổng ASCII lớn nhất của
#          * chuỗi con chung giữa s1[i..n-1] và s2[j..m-1]
#          */
#         int[][] dp = new int[n + 1][m + 1];

#         // Tính tổng ASCII của toàn bộ ký tự trong s1 và s2
#         int total = 0;
#         for (char c : a)
#             total += (int) c;
#         for (char c : b)
#             total += (int) c;

#         // Quy hoạch động từ dưới lên
#         for (int i = n - 1; i >= 0; i--) {
#             for (int j = m - 1; j >= 0; j--) {

#                 // Nếu hai ký tự giống nhau
#                 if (a[i] == b[j]) {
#                     // Giữ ký tự này, cộng ASCII của nó
#                     dp[i][j] = dp[i + 1][j + 1] + (int) a[i];
#                 } else {
#                     // Nếu khác nhau, chọn phương án có tổng ASCII lớn hơn
#                     dp[i][j] = Math.max(dp[i + 1][j], dp[i][j + 1]);
#                 }
#             }
#         }

#         /*
#          * dp[0][0]: tổng ASCII lớn nhất của chuỗi con chung
#          * Chi phí xóa nhỏ nhất =
#          * total - 2 * dp[0][0]
#          */
#         return total - 2 * dp[0][0];

#     }
# }

# // ## 1. Ý tưởng chính của thuật toán

# // 👉 Thay vì **tính chi phí xóa trực tiếp**, ta làm ngược lại:

# // * **Giữ lại** một **chuỗi con chung** giữa `s1` và `s2`
# // * Chuỗi con chung này phải có **tổng ASCII lớn nhất**
# // * Sau đó:

# // ```
# // Chi phí xóa nhỏ nhất
# // = (ASCII(s1) + ASCII(s2)) − 2 × ASCII(chuỗi chung)
# // ```

# // 📌 Vì ký tự được giữ lại xuất hiện ở **cả hai chuỗi**, nên phải trừ **2
# // lần**.

# // ---

# // ## 2. Ý nghĩa của mảng `dp`

# // ```java
# // int[][] dp = new int[n + 1][m + 1];
# // ```

# // ### dp[i][j] nghĩa là gì?

# // > **Tổng ASCII lớn nhất của chuỗi con chung** giữa
# // > `s1[i…n-1]` và `s2[j…m-1]`

# // ➡️ Đây chính là **LCS nhưng thay “độ dài” bằng “tổng ASCII”**

# // ---

# // ## 3. Tính tổng ASCII ban đầu

# // ```java
# // int total = 0;
# // for(char c: a) total += (int) c;
# // for(char c: b) total += (int) c;
# // ```

# // ✔ `total` = tổng ASCII của **toàn bộ ký tự trong s1 và s2**

# // Sau này:

# // ```
# // total − 2 × dp[0][0]
# // ```

# // ---

# // ## 4. Quy hoạch động (DP)

# // ```java
# // for(int i = n - 1; i >= 0; i--){
# // for(int j = m - 1; j >= 0; j--){
# // ```

# // 🔹 Duyệt ngược để đảm bảo:

# // * `dp[i+1][j]`
# // * `dp[i][j+1]`
# // * `dp[i+1][j+1]`
# // đã được tính

# // ---

# // ### Trường hợp 1: Hai ký tự giống nhau

# // ```java
# // if(a[i] == b[j]){
# // dp[i][j] = dp[i + 1][j + 1] + (int) a[i];
# // }
# // ```

# // 📌 Khi `a[i] == b[j]`:

# // * Ta **giữ ký tự này**
# // * Cộng ASCII của nó vào kết quả tốt nhất phía sau

# // ➡️ Giống LCS:

# // ```
# // dp[i][j] = dp[i+1][j+1] + giá trị ký tự
# // ```

# // ---

# // ### Trường hợp 2: Hai ký tự khác nhau

# // ```java
# // else {
# // dp[i][j] = Math.max(dp[i +1][j], dp[i][j + 1]);
# // }
# // ```

# // 📌 Ta có 2 lựa chọn:

# // * Bỏ `a[i]`
# // * Hoặc bỏ `b[j]`

# // ➡️ Chọn cách nào giữ được **tổng ASCII lớn hơn**

# // ---

# // ## 5. Kết quả cuối cùng

# // ```java
# // return -dp[0][0] * 2 + total;
# // ```

# // ### Ý nghĩa:

# // * `dp[0][0]` = tổng ASCII lớn nhất của chuỗi con chung
# // * Chuỗi con này xuất hiện **2 lần**
# // * Nên:

# // ```
# // Chi phí xóa = total − 2 × dp[0][0]
# // ```

# // ---

# // ## 6. Ví dụ minh họa nhanh

# // ```
# // s1 = "sea"
# // s2 = "eat"
# // ```

# // * Chuỗi chung tốt nhất: `"ea"`

# // * ASCII("e") = 101, ASCII("a") = 97
# // → dp[0][0] = 198

# // * total = (s+e+a) + (e+a+t)
# // = 313 + 314 = 627

# // 👉 Kết quả:

# // ```
# // 627 − 2×198 = 231
# // ```

# // ---

# // ## 7. Độ phức tạp

# // * **Time:** `O(n × m)`
# // * **Space:** `O(n × m)`

# // ---

# // ## 8. Tóm tắt 1 câu (rất quan trọng khi đi thi)

# // > Bài 712 = **LCS nhưng tối đa hóa tổng ASCII**,
# // > sau đó dùng: `total − 2 × LCS_ASCII`

# // ---

# // Nếu bạn muốn:

# // * 🔁 Viết lại theo **tư duy xóa trực tiếp**
# // * 💡 Tối ưu xuống **1D DP**
# // * ✍️ Giải thích kiểu **ghi nhớ khi phỏng vấn**

# // 👉 cứ nói, mình làm tiếp cho bạn 👍

# // ---

# // ### 1. Đề bài nói gì?

# // Bạn được cho **hai chuỗi** `s1` và `s2`.

# // 👉 Mỗi lần **xóa một ký tự**, bạn phải trả **chi phí = mã ASCII của ký tự
# // đó**.

# // 👉 Bạn có thể xóa ký tự ở **cả s1 hoặc s2**.

# // 🎯 **Mục tiêu:**
# // Xóa một số ký tự (có thể là 0) sao cho **hai chuỗi trở nên giống hệt nhau**,
# // và **tổng chi phí xóa là nhỏ nhất**.

# // ---

# // ### 2. ASCII là gì?

# // * Mỗi ký tự có một mã số:

# // * `'a'` → 97
# // * `'b'` → 98
# // * `'c'` → 99
# // * `'A'` → 65

# // Ví dụ:
# // Xóa `'a'` tốn 97 điểm, xóa `'b'` tốn 98 điểm.

# // ---

# // ### 3. Ví dụ đơn giản

# // #### Ví dụ 1

# // ```
# // s1 = "sea"
# // s2 = "eat"
# // ```

# // Ta muốn hai chuỗi **giống nhau**.

# // * Giữ lại `"ea"`
# // * Xóa:

# // * `'s'` trong s1 → 115
# // * `'t'` trong s2 → 116

# // 👉 Tổng chi phí = **115 + 116 = 231**

# // **Kết quả:** `231`

# // ---

# // ### 4. Hiểu bản chất bài toán

# // Bài này **không phải** hỏi:

# // * Xóa ít ký tự nhất ❌
# // * Mà là: **xóa sao cho tổng ASCII nhỏ nhất** ✅

# // 💡 Cách nhìn quan trọng:

# // * Ta muốn **giữ lại** một chuỗi con chung (common subsequence)
# // * Chuỗi con chung đó nên có **tổng ASCII lớn nhất**
# // * Vì:

# // ```
# // Tổng xóa = (ASCII s1 + ASCII s2) − 2 × (ASCII chuỗi chung)
# // ```

# // ➡️ Giữ được chuỗi chung càng “đắt tiền” (ASCII cao) thì xóa càng ít tiền.

# // ---

# // ### 5. So sánh với bài quen thuộc

# // Bài này giống:

# // * **Longest Common Subsequence (LCS)**
# // ❌ nhưng **không đếm độ dài**
# // ✅ mà **tối đa hóa tổng ASCII**

# // ---

# // ### 6. Tóm tắt ngắn gọn để nhớ

# // * Được phép xóa ký tự ở cả 2 chuỗi
# // * Chi phí xóa = mã ASCII
# // * Mục tiêu: 2 chuỗi giống nhau, chi phí xóa **nhỏ nhất**
# // * Bản chất: tìm **chuỗi con chung có tổng ASCII lớn nhất**

# // ---

# // Nếu bạn muốn, mình có thể:

# // * ✍️ Giải bằng **DP từng bước**
# // * 🧠 So sánh với **LCS thường**
# // * 💻 Giải thích code Java / Python
# // Chỉ cần nói nhé 👍
