# 966. Vowel Spellchecker(14/09/2025)
# ### Giải thích đề bài: Vowel Spellchecker
# Hay đấy 👍 mình sẽ giải thích chi tiết thuật toán trong code Python bạn đưa + thêm chú thích trực tiếp vào code để dễ review.

# ---

## 📌 Thuật toán

# Bài toán **Vowel Spellchecker (966)** yêu cầu tìm từ phù hợp nhất trong `wordlist` cho từng query theo 3 mức ưu tiên:

# 1. **Khớp chính xác (Exact match)** → trả về từ gốc.
# 2. **Khớp không phân biệt hoa thường (Case-insensitive)** → lấy từ đầu tiên trong wordlist có dạng viết thường giống query.
# 3. **Khớp lỗi nguyên âm (Vowel error)** → coi nguyên âm (`a, e, i, o, u`) là giống nhau → thay tất cả nguyên âm thành `a` (hoặc ký hiệu chung) để so sánh.
# 4. Nếu không tìm thấy → trả về chuỗi rỗng `""`.

# ## 📌 Code có chú thích

# ```python
from collections import defaultdict
from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        # Hàm băm chữ thường (case-insensitive)
        def case_hash(s):
            return s.lower()
        
        # Hàm băm bỏ qua lỗi nguyên âm:
        # Tất cả nguyên âm (e,i,o,u) đều đổi thành 'a' 
        # → ví dụ: "leet" -> "laat", "kite" -> "kat a"
        def vowel_hash(s):
            return (s.lower()
                      .replace('e', 'a')
                      .replace('i', 'a')
                      .replace('o', 'a')
                      .replace('u', 'a'))
        
        # 1. Tập hợp exact (dùng để check khớp chính xác)
        exact = set(wordlist)
        
        # 2. Map cho case-insensitive
        case = defaultdict()
        # 3. Map cho vowel-error
        vowl = defaultdict()
        
        # Xây dựng 2 map dựa trên wordlist
        for w in wordlist:
            c = case_hash(w)
            if c not in case:  # chỉ lấy từ đầu tiên
                case[c] = w
            v = vowel_hash(w)
            if v not in vowl: # chỉ lấy từ đầu tiên
                vowl[v] = w
        
        # Hàm trả về kết quả đúng cho 1 query
        def correct(w):
            # (1) Exact match
            if w in exact: 
                return w
            
            # (2) Case-insensitive match
            c = case_hash(w)
            if c in case: 
                return case[c]
            
            # (3) Vowel-error match
            v = vowel_hash(w)
            if v in vowl: 
                return vowl[v]
            
            # (4) Không khớp
            return ''
        
        # Áp dụng correct() cho tất cả queries
        return [correct(q) for q in queries]
# ```

# ---

# ## 📌 Ví dụ minh họa

# ```python
# sol = Solution()
# wordlist = ["KiTe","kite","hare","Hare"]
# queries  = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]

# print(sol.spellchecker(wordlist, queries))
# ```

# 👉 Kết quả:

# ```
# ['kite', 'kite', 'KiTe', 'Hare', 'hare', 'hare', 'hare', 'KiTe', 'KiTe', 'KiTe']
# ```

# ---

## 📌 Tóm tắt cách hoạt động

# 1. Duyệt `wordlist` để xây dựng:

#    * `exact` → check khớp tuyệt đối.
#    * `case` → ánh xạ chữ thường → từ gốc.
#    * `vowl` → ánh xạ chữ thường nhưng thay nguyên âm → từ gốc.

# 2. Với mỗi `query`:

#    * Check `exact` → nếu có thì return luôn.
#    * Nếu không → check `case`.
#    * Nếu vẫn không → check `vowl`.
#    * Nếu cả 3 không có → return `""`.

# # ---

# 👉 Điểm quan trọng dễ nhớ:

# * **`exact`** = tập hợp từ gốc.
# * **`case`** = hạ hết về lowercase.
# * **`vowl`** = lowercase + thay nguyên âm thành ký hiệu chung.

# ---

# Bạn có muốn mình viết lại phiên bản **ngắn gọn hơn bằng `dict.get()` và `Counter`** để dễ code trong interview không?

# Đề bài **966. Vowel Spellchecker** yêu cầu bạn xây dựng một công cụ kiểm tra chính tả đơn giản cho một danh sách các từ truy vấn.

# Bạn được cung cấp hai mảng:

# 1.  **`wordlist`**: Một danh sách các từ hợp lệ, được coi là từ điển của bạn.
# 2.  **`queries`**: Một danh sách các từ mà bạn cần kiểm tra chính tả.

# Đối với mỗi từ trong `queries`, bạn phải tìm một từ phù hợp trong `wordlist` theo một bộ quy tắc ưu tiên.

# #### Các quy tắc tìm kiếm và ưu tiên

# Bạn cần kiểm tra `queries[i]` theo thứ tự sau. Ngay khi tìm thấy một từ khớp, bạn sẽ dùng từ đó làm kết quả và không kiểm tra thêm các quy tắc sau nữa.

# 1.  **Khớp chính xác (Exact Match)**:
#     * Nếu `queries[i]` tồn tại trong `wordlist` (phân biệt chữ hoa/thường), trả về `queries[i]`.
#     * **Ví dụ:** `wordlist = ["Kiwi"]`, `queries = ["Kiwi"]` -> trả về `"Kiwi"`.

# 2.  **Khớp không phân biệt chữ hoa/thường (Case-Insensitive Match)**:
#     * Nếu không có khớp chính xác, hãy tìm một từ trong `wordlist` khớp với `queries[i]` khi chuyển cả hai về chữ thường.
#     * Nếu có nhiều từ như vậy, bạn phải trả về từ **đầu tiên** trong `wordlist` khớp với điều kiện này.
#     * **Ví dụ:** `wordlist = ["kite", "Kite", "KiTe"]`, `queries = ["kite"]`. Cả ba từ đều khớp khi chuyển về chữ thường. Bạn phải trả về `"kite"`, là từ đầu tiên.
#     * **Ví dụ khác:** `wordlist = ["Kiwi"]`, `queries = ["kiwi"]` -> trả về `"Kiwi"`.

# 3.  **Khớp khi thay thế nguyên âm (Vowel-Error Match)**:
#     * Nếu không có khớp ở hai quy tắc trên, hãy kiểm tra khi thay thế tất cả nguyên âm (`a`, `e`, `i`, `o`, `u`) bằng một ký tự duy nhất (ví dụ: `*`).
#     * Nếu `queries[i]` sau khi thay thế nguyên âm khớp với một từ trong `wordlist` sau khi thay thế nguyên âm, bạn phải trả về từ **đầu tiên** trong `wordlist` khớp với điều kiện này.
#     * **Ví dụ:** `wordlist = ["apple", "pleas"]`, `queries = ["apPlE"]`.
#         * Thay thế nguyên âm: `apPlE` -> `*ppl*`, `apple` -> `*ppl*`, `pleas` -> `pl***`.
#         * `*ppl*` khớp với `*ppl*`.
#         * Trả về `"apple"`, là từ đầu tiên khớp.
#     * **Ví dụ khác:** `wordlist = ["a", "A", "b", "c"]`, `queries = ["e"]`.
#         * Thay thế nguyên âm: `e` -> `*`, `a` -> `*`, `A` -> `*`. Cả `a` và `A` đều khớp. Bạn phải trả về `"a"`, là từ đầu tiên khớp.

# 4.  **Không có từ khớp**:
#     * Nếu không tìm thấy từ nào khớp với bất kỳ quy tắc nào, trả về một chuỗi rỗng (`""`).

# ---

# ### Phân tích chiến lược giải quyết

# Để xử lý các quy tắc ưu tiên này một cách hiệu quả, bạn nên sử dụng các cấu trúc dữ liệu để lưu trữ các dạng biến thể của từ trong `wordlist`.

# 1.  **Lưu trữ các dạng của `wordlist`**:
#     * **Bộ `set` chính xác**: Lưu tất cả các từ trong `wordlist` vào một `HashSet` để kiểm tra sự tồn tại nhanh chóng (O(1)).
#     * **Từ điển không phân biệt chữ hoa/thường**: Tạo một `HashMap` để ánh xạ dạng viết thường của một từ tới từ gốc ban đầu của nó trong `wordlist`.
#         * Key: dạng chữ thường của từ (`"kite"`).
#         * Value: từ gốc (`"kite"` hoặc `"Kite"`).
#         * Quan trọng: Vì bạn cần từ đầu tiên, bạn chỉ thêm vào `HashMap` nếu key đó chưa tồn tại.
#     * **Từ điển thay thế nguyên âm**: Tương tự, tạo một `HashMap` để ánh xạ dạng thay thế nguyên âm của một từ tới từ gốc của nó.
#         * Key: dạng thay thế nguyên âm của từ (`"k*t*"`).
#         * Value: từ gốc (`"kite"`).
#         * Tương tự, chỉ thêm vào `HashMap` nếu key đó chưa tồn tại.

# 2.  **Xử lý từng truy vấn**:
#     * Duyệt qua từng từ trong `queries`.
#     * Áp dụng ba quy tắc theo thứ tự bằng cách kiểm tra các từ điển bạn đã tạo.
#         * **Quy tắc 1**: Kiểm tra trong `set` chính xác.
#         * **Quy tắc 2**: Nếu không khớp, chuyển từ truy vấn về chữ thường và kiểm tra trong `HashMap` không phân biệt chữ hoa/thường.
#         * **Quy tắc 3**: Nếu vẫn không khớp, thay thế nguyên âm trong từ truy vấn và kiểm tra trong `HashMap` thay thế nguyên âm.
#         * **Quy tắc 4**: Nếu tất cả đều thất bại, trả về `""`.
#     * Lưu kết quả của mỗi truy vấn vào một danh sách kết quả.
#     Ok mình giải thích LeetCode **966. Vowel Spellchecker** cho bạn nhé 👇

# ---

# ## 📌 Đề bài:

# Bạn được cho:

# 1. **`wordlist`** (danh sách từ điển).
# 2. **`queries`** (danh sách các từ cần kiểm tra).

# Với mỗi từ trong `queries`, bạn phải tìm từ **phù hợp nhất** trong `wordlist` theo quy tắc sau:

# ### Quy tắc khớp:

# 1. **Exact match (khớp chính xác, phân biệt hoa thường)**

#    * Nếu từ trong `queries` xuất hiện y hệt trong `wordlist` → trả về nó luôn.

# 2. **Case-insensitive match (không phân biệt hoa thường)**

#    * Nếu không khớp chính xác, thì tìm từ trong `wordlist` giống nhưng **không phân biệt chữ hoa/thường**.
#    * Trả về từ xuất hiện **đầu tiên** trong `wordlist`.

# 3. **Vowel error match (lỗi nguyên âm)**

#    * Nếu vẫn chưa tìm thấy, thì coi các nguyên âm (`a, e, i, o, u`) là **tương đương nhau**.
#    * Ví dụ: `"leet"` và `"l**aat**t"` được coi là giống nhau vì nguyên âm được thay thế.
#    * Trả về từ đầu tiên trong `wordlist` khớp theo quy tắc này.

# 4. **No match**

#    * Nếu không có từ nào thỏa → trả về chuỗi rỗng `""`.

# ---

# ## 📌 Ví dụ:

# ```text
# wordlist = ["KiTe","kite","hare","Hare"]
# queries  = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
# ```

# ### Xử lý từng query:

# 1. `"kite"` → exact match → `"kite"`
# 2. `"Kite"` → case-insensitive match với `"kite"` → `"kite"`
# 3. `"KiTe"` → exact match → `"KiTe"`
# 4. `"Hare"` → exact match → `"Hare"`
# 5. `"HARE"` → case-insensitive match với `"hare"` → `"hare"`
# 6. `"Hear"` → vowel error: `"H**a**re"` vs `"H**ea**r"` → `"hare"`
# 7. `"hear"` → vowel error → `"hare"`
# 8. `"keti"` → vowel error: `"k**i**te"` → `"KiTe"`
# 9. `"keet"` → vowel error: `"k**i**te"` → `"KiTe"`
# 10. `"keto"` → vowel error: `"k**i**te"` → `"KiTe"`

# 👉 Kết quả:

# ```
# ["kite","kite","KiTe","Hare","hare","hare","hare","KiTe","KiTe","KiTe"]
# ```

# ---

# ## 📌 Ý tưởng thuật toán:

# * Dùng **3 hash maps** để hỗ trợ tra cứu nhanh:

#   1. **Exact set**: chứa từ gốc để check khớp chính xác.
#   2. **Case map**: key = từ viết thường, value = từ đầu tiên gặp trong `wordlist`.
#   3. **Vowel map**: key = từ viết thường nhưng thay nguyên âm thành ký tự chung (ví dụ `"leet"` → `"l#t"`), value = từ đầu tiên gặp trong `wordlist`.

# * Với mỗi query:

#   1. Check exact.
#   2. Check case-insensitive.
#   3. Check vowel-error.
#   4. Nếu không có thì return `""`.

# ---

# Bạn có muốn mình viết luôn **code Python giải bài này** kèm giải thích từng bước không?
