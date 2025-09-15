
# // // 1935. Maximum Number of Words You Can Type(15/09/2025)

# Rồi 👍 mình sẽ giải thích rõ ràng thuật toán trong code Python bạn viết kèm **chú thích chi tiết** nhé.

# ---

# ### Code đã thêm chú thích

# ```python
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        counter = 0  # đếm số từ KHÔNG thể gõ được

        # tách text thành các từ
        for word in text.split():
            # kiểm tra từng chữ trong từ
            for letter in word:
                if letter in brokenLetters:
                    counter += 1   # nếu gặp chữ hỏng -> từ này bị loại
                    break          # thoát vòng lặp, không cần kiểm tra tiếp các chữ khác

        # tổng số từ gõ được = tổng số từ - số từ bị loại
        return len(text.split()) - counter
# ```

# ---

# ### 🚀 Giải thích thuật toán

# 1. **Tách câu thành từ**

#    * Dùng `text.split()` để chia câu thành danh sách các từ (ngăn cách bởi dấu cách `' '`).
#    * Ví dụ: `"leet code".split()` → `["leet", "code"]`.

# 2. **Duyệt từng từ**

#    * Với mỗi từ, duyệt từng ký tự.

# 3. **Kiểm tra ký tự hỏng**

#    * Nếu ký tự có trong `brokenLetters`, từ này **không gõ được** → tăng `counter` lên 1.
#    * Dùng `break` để dừng kiểm tra sớm (vì chỉ cần một chữ hỏng là cả từ bị loại).

# 4. **Kết quả cuối cùng**

#    * `len(text.split())` = tổng số từ trong câu.
#    * `counter` = số từ bị loại.
#    * `len(text.split()) - counter` = số từ có thể gõ được.

# ---

# ### 🔎 Ví dụ minh họa

# Input:

# ```python
# text = "leet code"
# brokenLetters = "lt"
# ```

# * `text.split()` → `["leet", "code"]`
# * `"leet"`: chứa `'l'` và `'t'` → loại → `counter = 1`
# * `"code"`: không chứa `'l'` hoặc `'t'` → giữ nguyên

# Kết quả = `2 - 1 = 1`. ✅

# ---

# ⏱️ **Độ phức tạp**

# * Thời gian: `O(n * m)` với `n = số từ`, `m = độ dài trung bình của từ` (nhưng thực tế khá nhanh).
# * Bộ nhớ: `O(1)` (chỉ dùng biến đếm).

# ---

# Bạn có muốn mình viết thêm **phiên bản tối ưu hơn (dùng `set` cho brokenLetters để tra cứu nhanh O(1))** không?

































# import java.util.*;

# public class b37 {
#     public static void main(String[] args) {
#         Scanner sc = new Scanner(System.in);

#         String text = sc.nextLine(); // nhập cả câu

#         String brokenLetters = sc.nextLine(); // nhập các chữ hỏng

#         int result = canBeTypedWords(text, brokenLetters);
#         System.out.println(result);

#         sc.close();
#     }

#     // Hàm chính giải bài toán
#     public static int canBeTypedWords(String text, String brokenLetters) {
#         int count = 1; // số từ có thể gõ được (bắt đầu với 1 từ đầu tiên)
#         boolean flag = true; // đánh dấu từ hiện tại có còn "cơ hội gõ được" không
#         boolean[] c = new boolean[26]; // lưu bảng chữ cái hỏng

#         // Đánh dấu các chữ cái bị hỏng
#         for (int i = 0; i < brokenLetters.length(); i++) {
#             c[brokenLetters.charAt(i) - 'a'] = true;
#         }

#         // Duyệt chuỗi text
#         for (char ch : text.toCharArray()) {
#             if (ch == ' ') {
#                 // Gặp khoảng trắng -> từ mới
#                 flag = true;
#                 count++;
#             } else if (c[ch - 'a'] && flag) {
#                 // Nếu gặp chữ bị hỏng trong từ này (và từ này chưa bị loại trước đó)
#                 count--;
#                 flag = false; // từ này bị loại, không check tiếp
#             }
#         }

#         return Math.max(count, 0); // đảm bảo không âm
#     }

# }
# // Rồi👍

# // mình giải
# // thích thuật
# // toán trong
# // code này
# // để bạn
# // hiểu rõ
# // cách hoạt động:

# // ##🚀
# // Ý tưởng
# // chính

# // Bài
# // toán yêu cầu:
# // đếm số
# // từ trong`text`
# // có thể
# // gõ được
# // khi một
# // số phím

# // bị hỏng (`brokenLetters`).
# // Thay vì tách chuỗi bằng `split`, code này duyệt trực tiếp từng ký tự trong
# // `text` và dùng **cờ (`flag`)** để quyết định một từ có bị loại hay không.

# // ---

# // ## 📝 Giải thích từng bước

# // ### 1. Chuẩn bị

# // ```java
# // int count = 1; // số từ có thể gõ, ban đầu giả sử có ít nhất 1 từ
# // boolean flag = true; // cờ: từ hiện tại vẫn có khả năng gõ
# // boolean[] c = new boolean[26]; // lưu chữ cái nào bị hỏng
# // ```

# // 👉 Ban đầu `count = 1` vì trong đoạn văn luôn có ít nhất một từ trước khi gặp
# // dấu cách `' '`.
# // 👉 Mảng `c[26]` lưu các chữ hỏng, ví dụ: `brokenLetters = "ad"` thì `c[0] =
# // true` (a), `c[3] = true` (d).

# // ---

# // ### 2. Đánh dấu chữ cái hỏng

# // ```java
# // for (int i = 0; i < brokenLetters.length(); i++) {
# // c[brokenLetters.charAt(i) - 97] = true;
# // }
# // ```

# // * Trừ `97` để đưa `'a' → 0`, `'b' → 1`, ..., `'z' → 25`.
# // * Giúp kiểm tra nhanh `O(1)` xem một chữ có hỏng không.

# // ---

# // ### 3. Duyệt từng ký tự trong text

# // ```java
# // for (char ch : text.toCharArray()) {
# // if (ch == ' ') {
# // flag = true;
# // count++;
# // } else if (c[ch - 97] && flag) {
# // count--;
# // flag = false;
# // }
# // }
# // ```

# // * Nếu gặp **dấu cách `' '`**: nghĩa là kết thúc một từ → bắt đầu từ mới

# // * `flag = true` (reset trạng thái cho từ mới)
# // * `count++` (thêm 1 từ vào tổng số)

# // * Nếu gặp **chữ cái bị hỏng** và `flag = true`:

# // * Giảm `count--` (vì từ này bị loại, không thể gõ được)
# // * `flag = false` (đánh dấu từ này đã hỏng → không trừ nhiều lần khi gặp các
# // chữ hỏng khác trong cùng từ).

# // ---

# // ### 4. Kết quả cuối cùng

# // ```java
# // return count < 1 ? 0 : count;
# // ```

# // * Nếu tất cả từ đều bị loại thì `count` có thể âm hoặc 0, nên trả về `0`.
# // * Ngược lại trả về số từ hợp lệ.

# // ---

# // ## 🔎 Ví dụ minh họa

# // Input:

# // ```
# // text = "hello world"
# // brokenLetters = "ad"
# // ```

# // * `brokenLetters = {a, d}`
# // * Duyệt `"hello world"`:

# // * `"hello"`: không có `a`, `d` → giữ `count = 1`
# // * Gặp `' '` → `count = 2`
# // * `"world"`: chứa `d` → `count-- = 1`

# // // 👉 Kết quả: `1`.

# // // ---

# // // ## ⏱️ Độ phức tạp

# // // * Thời gian: **O(n)**, với `n = text.length()` (chỉ duyệt một lần).
# // // * Bộ nhớ: **O(26) ≈ O(1)** cho mảng chữ cái hỏng.

# // // ---

# // // Bạn có muốn mình vẽ **timeline từng ký tự

# // // duyệt qua (ví dụ với `"hello world"`)** để trực quan hơn không?

# // // Ok mình
# // // giải thích
# // // cho bạn
# // // rõ ràng đề**LeetCode 1935-
# // // Maximum Number
# // // of Words
# // // You Can Type**nhé👇

# // // ###**Đề bài (dịch ra dễ hiểu)**

# // // Bạn có:

# // // * Một đoạn văn bản `text` gồm nhiều từ, các từ được phân tách bằng dấu
# // cách `' '`.
# // // * Một chuỗi `brokenLetters` gồm các chữ cái bị hỏng trên bàn

# // // phím (nếu một chữ cái xuất hiện trong `brokenLetters` thì bạn **không thể
# // gõ** nó).

# // // **Nhiệm vụ**:
# // // Hãy đếm xem trong đoạn văn `text` có bao nhiêu từ bạn **có thể gõ được đầy
# // đủ** (tức là từ đó **không chứa** bất kỳ chữ cái nào nằm trong
# // `brokenLetters`).

# // // ---

# // // ### **Ví dụ**

# // // #### Ví dụ 1:

# // // ```
# // // Input: text = "hello world", brokenLetters = "ad"
# // // ```

# // // * `brokenLetters = "ad"` → bạn không thể gõ chữ `'a'` và `'d'`.
# // // * Từ `"hello"`: không chứa `'a'` hoặc `'d'` → **gõ được**.
# // // * Từ `"world"`: chứa `'d'` → **không gõ được**.

# // // 👉 Kết quả: `1`.

# // // ---

# // // #### Ví dụ 2:

# // // ```
# // // Input: text = "leet code", brokenLetters = "lt"
# // // ```

# // // * `brokenLetters = "lt"` → không gõ được `'l'` và `'t'`.
# // // * `"leet"`: có `'l'` và `'t'` → **không gõ được**.
# // // * `"code"`: không có `'l'`, `'t'` → **gõ được**.

# // // 👉 Kết quả: `1`.

# // // ---

# // // #### Ví dụ 3:

# // // ```
# // // Input: text = "leet code", brokenLetters = "e"
# // // ```

# // // * `brokenLetters = "e"` → không gõ được `'e'`.
# // // * `"leet"`: có `'e'` → **không gõ được**.
# // // * `"code"`: có `'e'` → **không gõ được**.

# // // 👉 Kết quả: `0`.

# // // ---

# // // ### **Tóm lại**

# // // * Chia `text` thành các từ.
# // // * Với mỗi từ, kiểm tra xem nó có chứa ký tự nào trong `brokenLetters`
# // không.
# // // * Nếu không chứa → đếm +1.

# // // ---

# // // 👉 Bạn có muốn mình viết luôn **pseudo code / Python code** để dễ hình
# // dung hơn không?
