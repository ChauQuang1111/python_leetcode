# // 3541. Find Most Frequent Vowel and Consonant(13/09/2025)

class Solution:
    def maxFreqSum(self, s: str) -> int:
        # Đếm tần suất ký tự bằng dictionary
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1

        vowels = "aeiou"
        max_vowel = 0
        max_consonant = 0

        for ch, count in freq.items():
            if ch in vowels:
                max_vowel = max(max_vowel, count)
            else:
                max_consonant = max(max_consonant, count)

        return max_vowel + max_consonant


# # Mình giải thích chi tiết thuật toán của hàm **`maxFreqSum`** trong Python nhé 👇

# # ---

# # ## 🎯 Bài toán

# # * Chuỗi `s` chỉ chứa chữ cái thường `a-z`.
# # * Cần tìm:

# #   1. Nguyên âm (`a, e, i, o, u`) có số lần xuất hiện nhiều nhất.
#   2. Phụ âm (các ký tự còn lại) có số lần xuất hiện nhiều nhất.
# * Kết quả = tổng của 2 giá trị trên.



## 🔎 Các bước thuật toán

### 1. Đếm tần suất xuất hiện của từng ký tự

# Dùng dictionary `freq` để lưu số lần xuất hiện:

# ```python
# freq = {}
# for c in s:
#     freq[c] = freq.get(c, 0) + 1
# ```

# * `freq.get(c, 0)` lấy giá trị hiện tại của `c`, nếu chưa có thì mặc định bằng 0.
# * Sau vòng lặp, `freq` chứa số lần xuất hiện của tất cả ký tự.

# Ví dụ:
# `s = "leetcode"` →
# `freq = {'l':1, 'e':3, 't':1, 'c':1, 'o':1, 'd':1}`

# ---

# ### 2. Xác định nguyên âm nhiều nhất và phụ âm nhiều nhất

# # Khởi tạo:

# # ```python
# # max_vowel = 0
# # max_consonant = 0
# # ```

# # Duyệt qua từng `(ch, count)` trong `freq.items()`:

# # * Nếu `ch` là nguyên âm (`ch in "aeiou"`):

# #   ```python
# #   max_vowel = max(max_vowel, count)
# #   ```
# # * Ngược lại là phụ âm:

# #   ```python
#   max_consonant = max(max_consonant, count)
#   ```

# ---

# ### 3. Trả về kết quả

# ```python
# return max_vowel + max_consonant
# ```

# ---

# ## ✅ Ví dụ minh họa

# ### Ví dụ 1

# `s = "leetcode"`

# * Nguyên âm:

#   * `'e'` xuất hiện 3 lần
#   * `'o'` xuất hiện 1 lần
#     → `max_vowel = 3`
# * Phụ âm: `'l','t','c','d'` mỗi cái 1 lần → `max_consonant = 1`
# * Kết quả = 3 + 1 = **4**

# ---

# ### Ví dụ 2

# `s = "aaaabbbcc"`

# * Nguyên âm: `'a'` = 4 → `max_vowel = 4`
# * Phụ âm: `'b'` = 3, `'c'` = 2 → `max_consonant = 3`
# * Kết quả = 4 + 3 = **7**

# ---

# ## ⏱️ Độ phức tạp

# * **Thời gian**:

#   * Đếm tần suất: O(n), với n = độ dài chuỗi.
#   * Duyệt qua dictionary: O(k), với k ≤ 26 (số ký tự khác nhau).
#   * Tổng: O(n).

# * **Bộ nhớ**: O(26) = O(1).

# ---

# 👉 Nói ngắn gọn:

# * Đếm số lần xuất hiện của mỗi chữ cái.
# * Lấy nguyên âm nhiều nhất + phụ âm nhiều nhất.
# * Trả về tổng.

# ---

# Bạn có muốn mình minh họa **từng bước đếm + so sánh max** bằng bảng chi tiết (kiểu step-by-step trace) cho ví dụ `"leetcode"` không?













# import java.util.*;

# public class b35 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {

#         System.out.print("Nhập chuỗi: ");
#         String s = sc.nextLine();

#         int result = maxFreqSum(s);
#         System.out.println("Kết quả: " + result);

#         sc.close();
#     }

#     public static int maxFreqSum(String s) {
#         // Mảng đếm tần suất các chữ cái a-z
#         int[] cnt = new int[26];
#         for (char c : s.toCharArray()) {
#             cnt[c - 'a']++;
#         }

#         int maxVowel = 0;
#         int maxConsonant = 0;

#         for (int i = 0; i < 26; i++) {
#             char ch = (char) (i + 'a');
#             if (isVowel(ch)) {
#                 // nếu là nguyên âm, cập nhật tần suất nguyên âm lớn nhất
#                 if (cnt[i] > maxVowel) {
#                     maxVowel = cnt[i];
#                 }
#             } else {
#                 // nếu là phụ âm
#                 if (cnt[i] > maxConsonant) {
#                     maxConsonant = cnt[i];
#                 }
#             }
#         }

#         return maxVowel + maxConsonant;
#     }

#     // Hàm phụ kiểm tra nguyên âm
#     public static boolean isVowel(char c) {
#         return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
#     }
# }
# // Ok,

# // mình sẽ
# // giải thích
# // chi tiết
# // thuật toán
# // của hàm**`maxFreqSum(String s)`** nhé 👇

# // ---

# // ## 🎯 Mục tiêu

# // * Tìm **nguyên âm xuất hiện nhiều nhất** trong chuỗi.
# // * Tìm **phụ âm xuất hiện nhiều nhất** trong chuỗi.
# // * Trả về **tổng hai giá trị đó**.

# // Ví dụ:

# // * `s = "leetcode"`

# // * Nguyên âm: `e (3 lần)`, `o (1 lần)` → maxVowel = 3
# // * Phụ âm: `l (1)`, `t (1)`, `c (1), d(1)` → maxConsonant = 1
# // * Kết quả = 3 + 1 = **4**

# // ---

# // ## 🔎 Các bước của thuật toán

# // 1. **Đếm tần suất xuất hiện của từng chữ cái**

# // * Tạo mảng `cnt[26]` để lưu số lần xuất hiện của các ký tự `'a'` → `'z'`.
# // * Duyệt qua chuỗi `s`, mỗi khi gặp ký tự `c`, tăng `cnt[c - 'a']++`.

# // Ví dụ:
# // `s = "leetcode"` →

# // * `'l'` tăng ở `cnt[11]`
# // * `'e'` tăng ở `cnt[4]`
# // * `'t'` tăng ở `cnt[19]`
# // * `'c'` tăng ở `cnt[2]`
# // * `'o'` tăng ở `cnt[14]`
# // * `'d'` tăng ở `cnt[3]`

# // Sau vòng lặp → mảng `cnt` có số lần xuất hiện của từng ký tự.

# // ---

# // 2. **Tìm tần suất lớn nhất của nguyên âm và phụ âm**

# // * Duyệt qua `cnt[0..25]`.
# // * Với mỗi ký tự `ch = (char)(i + 'a')`:

# // * Nếu `ch` ∈ {`a,e,i,o,u`} → cập nhật `maxVowel = max(maxVowel, cnt[i])`.
# // * Ngược lại → cập nhật `maxConsonant = max(maxConsonant, cnt[i])`.

# // Như vậy sau vòng lặp:

# // * `maxVowel` chứa số lần xuất hiện **nhiều nhất của một nguyên âm**.
# // * `maxConsonant` chứa số lần xuất hiện **nhiều nhất của một phụ âm**.

# // 3. **Tính tổng và trả về kết quả**

# // * Kết quả = `maxVowel + maxConsonant`.

# // ---

# // ## ⏱️ Độ phức tạp

# // * **Thời gian**:

# // * Duyệt chuỗi để đếm tần suất → O(n), với n = độ dài chuỗi.
# // * Duyệt 26 chữ cái để tìm max → O(26) = O(1).
# // * Tổng = O(n).

# // * **Bộ nhớ**: O(26) = O(1).

# // ---

# // 👉 Nói ngắn gọn:

# // * Đếm số lần xuất hiện của từng ký tự.
# // * Lấy **nguyên âm nhiều nhất** + **phụ âm nhiều nhất**.
# // * Trả về tổng.

# // ---

# // Bạn có muốn mình minh họa thuật toán này bằng **bảng đếm tần suất trên ví dụ
# // cụ thể** để dễ hình dung không?

# // ###

# // Giải thích
# // đề bài:
# // Find Most
# // Frequent Vowel
# // and Consonant

# // Đề bài**3541.
# // Find Most
# // Frequent Vowel
# // and Consonant**
# // yêu cầu
# // bạn tìm
# // nguyên âm
# // và phụ
# // âm xuất
# // hiện nhiều
# // nhất trong
# // một chuỗi.

# // Bạn được
# // cung cấp
# // một chuỗi`s`
# // chỉ chứa
# // các chữ
# // cái tiếng

# // Anh (hoa và thường).

# // #### Yêu cầu

# // Bạn phải trả về một mảng chứa hai phần tử:
# // 1. Ký tự nguyên âm xuất hiện nhiều nhất.
# // 2. Ký tự phụ âm xuất hiện nhiều nhất.

# // Nếu có nhiều hơn một ký tự có cùng tần suất xuất hiện cao nhất, bạn cần chọn
# // ký tự có thứ tự bảng chữ cái nhỏ nhất.

# // #### Các quy tắc chính

# // 1. **Nguyên âm (Vowels)**: `'a', 'e', 'i', 'o', 'u'`. Đề bài không nói rõ,
# // nhưng mặc định, bạn cũng cần xét các chữ cái viết hoa tương ứng.
# // 2. **Phụ âm (Consonants)**: Tất cả các chữ cái tiếng Anh khác không phải
# // nguyên âm.
# // 3. **Tính tần suất**: Bạn cần đếm số lần xuất hiện của mỗi nguyên âm và mỗi
# // phụ âm.
# // 4. **Điều kiện tie-breaker (phá vỡ thế hòa)**:
# // * Khi có nhiều nguyên âm có cùng tần suất cao nhất, bạn chọn nguyên âm có thứ
# // tự bảng chữ cái

# // nhỏ nhất (ví dụ: `'a'` < `'e'`).
# // * Tương tự, khi có nhiều phụ âm có cùng tần suất cao nhất, bạn chọn phụ âm có
# // thứ tự bảng chữ cái nhỏ nhất.

# // #### Ví dụ minh họa

# // Hãy xem xét chuỗi đầu vào: `"AbcdeFg"`

# // 1. **Phân loại và đếm tần suất**:
# // * **Nguyên âm**:
# // * `'A'` -> 1 lần
# // * `'e'` -> 1 lần
# // * **Phụ âm**:
# // * `'b'` -> 1 lần
# // * `'c'` -> 1 lần
# // * `'d'` -> 1 lần
# // * `'F'` -> 1 lần
# // * `'g'` -> 1 lần

# // 2. **Tìm nguyên âm xuất hiện nhiều nhất**:
# // * `A` và `e` đều có tần suất là 1.
# // * Áp dụng quy tắc phá vỡ thế hòa: `A` có thứ tự bảng chữ cái nhỏ hơn `e`.
# // * Nguyên âm xuất hiện nhiều nhất là `'A'`.

# // 3. **Tìm phụ âm xuất hiện nhiều nhất**:
# // * `b`, `c`, `d`, `F`, `g` đều có tần suất là 1.
# // * Áp dụng quy tắc phá vỡ thế hòa: `b` có thứ tự bảng chữ cái nhỏ nhất.
# // * Phụ âm xuất hiện nhiều nhất là `'b'`.

# // 4. **Kết quả**:
# // * Mảng kết quả là: `['A', 'b']`.

# // ### Tóm tắt các bước cần thực hiện để giải quyết bài toán

# // 1. Tạo hai danh sách/từ điển trống để lưu tần suất của nguyên âm và phụ âm.
# // 2. Duyệt qua từng ký tự trong chuỗi đầu vào.
# // 3. Với mỗi ký tự, xác định xem đó là nguyên âm hay phụ âm, sau đó tăng bộ đếm
# // tần suất tương ứng.
# // 4. Sau khi duyệt xong, tìm ký tự có tần suất cao nhất trong danh sách/từ điển
# // của nguyên âm.
# // 5. Thực hiện tương tự cho phụ âm.
# // 6. Xử lý trường hợp có nhiều ký tự cùng tần suất cao nhất bằng cách chọn ký
# // tự có thứ tự bảng chữ cái nhỏ nhất.
# // 7. Trả về mảng kết quả.