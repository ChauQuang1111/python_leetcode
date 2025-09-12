# 3227. Vowels Game in a String(12/09/2025)
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u") > 0

# Mình giải thích chi tiết nhé 👇

# ### Code của bạn:

# ```python
# class Solution:
#     def doesAliceWin(self, s: str) -> bool:
#         return s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u") > 0
# ```

# ---

# ### 🔎 Giải thích thuật toán

# 1. **`s.count("a")`**

#    * Phương thức `.count(substring)` trong Python trả về **số lần xuất hiện** của chuỗi con `substring` trong chuỗi `s`.
#    * Ví dụ:

#      ```python
#      "banana".count("a")  # 3
#      "banana".count("b")  # 1
#      "banana".count("z")  # 0
#      ```

# 2. **Tính tổng các nguyên âm**

#    * `s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u")`
#    * Đây chính là **tổng số nguyên âm trong chuỗi** (chỉ tính chữ thường).
#    * Ví dụ:

#      * `s = "leetcode"` → `"e"` xuất hiện 3 lần, `"o"` xuất hiện 1 lần → tổng = 4
#      * `s = "rhythm"` → không có nguyên âm nào → tổng = 0

# 3. **So sánh với 0**

#    * Biểu thức `> 0` kiểm tra xem tổng có lớn hơn 0 hay không.
#    * Nếu **có ít nhất một nguyên âm** → tổng > 0 → trả về `True`.
#    * Nếu **không có nguyên âm nào** → tổng = 0 → trả về `False`.

# ---

# ### ✅ Ví dụ chạy:

# ```python
# sol = Solution()
# print(sol.doesAliceWin("leetcode"))  # True (có nguyên âm e, o)
# print(sol.doesAliceWin("rhythm"))    # False (không có nguyên âm)
# ```

# ---

# 👉 Tóm lại:

# * `.count(x)` đếm số lần xuất hiện của ký tự `x`.
# * Cộng tất cả `.count` của nguyên âm lại → tổng số nguyên âm.
# * Nếu tổng > 0, tức là có ít nhất một nguyên âm → Alice thắng (`True`).

# Bạn có muốn mình viết lại phiên bản Python **ngắn hơn** dùng `any()` thay vì cộng `.count()` không?
















# // Đoạn mã của bạn giải quyết bài toán một cách rất thông minh và hiệu quả.
# // Thuật toán của nó dựa trên chiến lược chơi tối ưu và một quan sát then chốt.

# // ---

# // ### Phân tích Thuật toán

# // Thuật toán của bạn hoạt động theo một logic đơn giản nhưng hoàn toàn chính
# // xác:

# // 1. **Duyệt qua chuỗi**: Vòng lặp `for` duyệt qua từng ký tự của chuỗi đầu vào
# // `s` từ đầu đến cuối.

# // 2. **Kiểm tra nguyên âm**: Trong mỗi lần lặp, bạn kiểm tra xem ký tự hiện tại
# // (`c`) có phải là một nguyên âm hay không bằng cách sử dụng câu lệnh `switch`.

# // 3. **Chiến lược tối ưu**:
# // * **Nếu tìm thấy nguyên âm**: Ngay khi tìm thấy một nguyên âm bất kỳ, thuật
# // toán sẽ ngay lập tức trả về **`true`** và kết thúc.
# // * **Nếu không tìm thấy nguyên âm**: Vòng lặp sẽ chạy hết chuỗi. Nếu không có
# // nguyên âm nào được tìm thấy sau khi duyệt xong, thuật toán sẽ trả về
# // **`false`**.

# // ### Tại sao thuật toán này lại đúng?

# // Thuật toán này hoạt động dựa trên logic của trò chơi:

# // * **Alice** luôn đi trước.
# // * Điểm chỉ có thể được ghi bằng cách chọn một nguyên âm.

# // Nếu trong chuỗi có **ít nhất một nguyên âm**, Alice sẽ đi trước và chọn
# // nguyên âm đó. Cô ấy sẽ có ít nhất 1 điểm, trong khi điểm của Bob là 0. Sau
# // đó, trò chơi có thể tiếp tục, nhưng Alice đã đảm bảo rằng điểm của mình sẽ
# // luôn lớn hơn hoặc bằng điểm của Bob. Do đó, Alice sẽ thắng hoặc hòa, và theo
# // yêu cầu của đề bài, bạn cần trả về `true` trong trường hợp này.

# // Nếu trong chuỗi **không có nguyên âm nào**, cả Alice và Bob sẽ chỉ có thể
# // chọn các phụ âm. Kết quả là cả hai đều có 0 điểm, dẫn đến một trận hòa. Theo
# // yêu cầu, trong trường hợp hòa, bạn cần trả về `false`.

# // Do đó, chỉ cần kiểm tra sự tồn tại của bất kỳ nguyên âm nào trong chuỗi là đủ
# // để xác định kết quả. Thuật toán của bạn đã làm chính xác điều đó một cách
# // hiệu quả.
# // ### Giải thích đề bài: Vowels Game in a String

# // Đề bài **3227. Vowels Game in a String** mô tả một trò chơi giữa Alice và
# // Bob, và bạn cần xác định ai là người chiến thắng.

# // #### Các quy tắc của trò chơi

# // 1. **Người chơi**: Có hai người chơi: Alice và Bob. Alice luôn là người đi
# // trước.
# // 2. **Chuỗi và Lượt chơi**:
# // * Trò chơi bắt đầu với một chuỗi `s` và một số nguyên `n` (độ dài của chuỗi).
# // * Trong mỗi lượt của mình, một người chơi chọn một ký tự bất kỳ trong chuỗi
# // `s` mà chưa được chọn và gán điểm cho nó.
# // 3. **Cách tính điểm**:
# // * Nếu ký tự được chọn là một **nguyên âm** (`'a', 'e', 'i', 'o', 'u'`), người
# // chơi được cộng thêm `1` điểm.
# // * Nếu ký tự được chọn là một **phụ âm**, người chơi không được điểm nào.
# // 4. **Điều kiện chiến thắng**:
# // * Trò chơi kết thúc khi tất cả các ký tự trong chuỗi đã được chọn.
# // * Người chiến thắng là người có tổng điểm **lớn hơn hoặc bằng** điểm của đối
# // thủ.
# // * Nếu cả hai người có tổng điểm bằng nhau, trận đấu kết thúc với kết quả hòa.

# // #### Yêu cầu

# // Dựa trên chuỗi `s` đã cho, bạn cần xác định người chiến thắng:
# // * Nếu Alice thắng, trả về `True`.
# // * Nếu Bob thắng hoặc hòa, trả về `False`.

# // ---

# // ### Phân tích chiến lược chơi tối ưu

# // Đây là một trò chơi có tổng bằng 0 (zero-sum game) và có thông tin đầy đủ,
# // nghĩa là cả hai người chơi đều biết tất cả các thông tin cần thiết. Với loại
# // trò chơi này, người chơi sẽ luôn chọn một nước đi tối ưu nhất để thắng hoặc
# // đạt kết quả tốt nhất có thể.

# // * **Mục tiêu của Alice**: Alice muốn tối đa hóa điểm của mình để đảm bảo
# // `điểm_Alice >= điểm_Bob`.
# // * **Mục tiêu của Bob**: Bob cũng muốn tối đa hóa điểm của mình.

# // Vì cả hai người đều chơi tối ưu, họ sẽ luôn cố gắng lấy các điểm có sẵn. Điểm
# // chỉ đến từ các nguyên âm.

# // * **Lượt 1 (Alice)**: Alice sẽ luôn chọn một nguyên âm để được `1` điểm.
# // * **Lượt 2 (Bob)**: Bob cũng sẽ luôn chọn một nguyên âm để được `1` điểm.
# // * ... và cứ thế tiếp tục.

# // Điều này có nghĩa là, miễn là còn nguyên âm, cả Alice và Bob sẽ lần lượt chọn
# // chúng. Tổng số nguyên âm sẽ được chia đều cho hai người chơi.

# // * **Gọi `count_vowels` là tổng số nguyên âm trong chuỗi.**
# // * **Alice** sẽ chọn các nguyên âm trong các lượt: 1, 3, 5, ...
# // * **Bob** sẽ chọn các nguyên âm trong các lượt: 2, 4, 6, ...

# # // Tổng số nguyên âm mà Alice chọn được là `ceil(count_vowels / 2)`.
# // Tổng số nguyên âm mà Bob chọn được là `floor(count_vowels / 2)`.

# // Ví dụ, nếu có 5 nguyên âm:
# // * Alice lấy nguyên âm thứ 1, 3, 5 -> 3 điểm.
# // * Bob lấy nguyên âm thứ 2, 4 -> 2 điểm.
# // * `điểm_Alice = 3`, `điểm_Bob = 2`. Alice thắng.

# // #### Điều kiện chiến thắng

# // Để Alice thắng, điểm của cô ấy phải lớn hơn hoặc bằng điểm của Bob.
# // * `điểm_Alice >= điểm_Bob`

# // Nếu `count_vowels` là số lẻ, `điểm_Alice` sẽ lớn hơn `điểm_Bob`.
# # // Nếu `count_vowels` là số chẵn, `điểm_Alice` sẽ bằng `điểm_Bob`.

# // Tuy nhiên, đề bài có một điểm quan trọng: Alice thắng nếu `điểm_Alice >=
# // điểm_Bob`.
# // * Khi `count_vowels` là số lẻ, `điểm_Alice > điểm_Bob`. Điều kiện `điểm_Alice
# // >= điểm_Bob` đúng.
# // * Khi `count_vowels` là số chẵn, `điểm_Alice = điểm_Bob`. Điều kiện
# // `điểm_Alice >= điểm_Bob` cũng đúng.

# // Điều này có nghĩa là Alice sẽ **luôn luôn** không thua. Cô ấy luôn có thể
# // thắng hoặc hòa.

# // Vậy, có một trường hợp duy nhất mà Alice thua: khi không có nguyên âm nào.

# // * Nếu `count_vowels = 0`, cả hai người chơi đều không có điểm nào.
# // `điểm_Alice = 0`, `điểm_Bob = 0`. `điểm_Alice = điểm_Bob`, kết quả là hòa.
# // Theo yêu cầu, Bob thắng hoặc hòa thì trả về `False`.
# // * Nếu `count_vowels > 0`, Alice sẽ luôn giành được ít nhất một nguyên âm, và
# // Bob cũng vậy (nếu có đủ).

# // Do đó, thuật toán đơn giản nhất là:
# // 1. Đếm tổng số nguyên âm trong chuỗi `s`.
# // 2. Nếu số lượng nguyên âm lớn hơn 0, Alice sẽ có cơ hội ghi điểm và không
# // thua. Trả về `True`.
# // 3. Nếu số lượng nguyên âm bằng 0, cả hai đều có 0 điểm, kết quả hòa. Trả về
# // `False`.
# // Đúng như phân tích, ví dụ dưới đây sẽ minh họa cách quyết định người thắng
# // cuộc chỉ dựa vào số lượng nguyên âm.

# // ### Ví dụ 1: Chuỗi `"leEe"`

# // 1. **Đếm nguyên âm**:
# // * Chuỗi `"leEe"` có 3 nguyên âm: `'e'`, `'E'`, `'e'`.
# // * Tổng số nguyên âm = 3.

# // 2. **Lượt chơi**:
# // * Alice đi trước và chọn một nguyên âm (`'e'`). Điểm của cô ấy là 1. Còn lại
# // 2 nguyên âm.
# // * Bob đi lượt hai và chọn một nguyên âm (`'E'`). Điểm của anh ấy là 1. Còn
# // lại 1 nguyên âm.
# // * Alice đi lượt ba và chọn nguyên âm cuối cùng (`'e'`). Điểm của cô ấy là 2.
# // * Tất cả các ký tự đã được chọn.

# // 3. **Kết quả**:
# // * Điểm của Alice = 2.
# // * Điểm của Bob = 1.
# // * `2 >= 1`, nên Alice thắng.

# // Theo thuật toán đã phân tích: `số_nguyên_âm = 3 > 0`, nên trả về `True`,
# // chính xác.

# // ---

# // ### Ví dụ 2: Chuỗi `"bbba"`

# # // 1. **Đếm nguyên âm**:
# # // * Chuỗi `"bbba"` có 1 nguyên âm: `'a'`.
# # // * Tổng số nguyên âm = 1.

# # // 2. **Lượt chơi**:
# # // * Alice đi trước và chọn nguyên âm duy nhất (`'a'`). Điểm của cô ấy là 1.
# # // * Bob đi lượt hai. Không còn nguyên âm nào, anh ấy phải chọn một phụ âm
# # // (`'b'`). Điểm của anh ấy là 0.
# # // * Trò chơi tiếp tục cho đến khi tất cả các ký tự được chọn.

# # // 3. **Kết quả**:
# # // * Điểm của Alice = 1.
# # // * Điểm của Bob = 0.
# # // * `1 >= 0`, nên Alice thắng.

# # // Theo thuật toán đã phân tích: `số_nguyên_âm = 1 > 0`, nên trả về `True`,
# # // chính xác.

# # // ---

# # // ### Ví dụ 3: Chuỗi `"bcdf"`

# # // 1. **Đếm nguyên âm**:
# # // * Chuỗi `"bcdf"` không có nguyên âm nào.
# # // * Tổng số nguyên âm = 0.

# # // 2. **Lượt chơi**:
# # // * Alice chọn một phụ âm (`'b'`). Điểm của cô ấy là 0.
# # // * Bob chọn một phụ âm (`'c'`). Điểm của anh ấy là 0.
# # // * ...

# # // 3. **Kết quả**:
# # // * Điểm của Alice = 0.
# # // * Điểm của Bob = 0.
# # // * `0 >= 0`. Kết quả hòa.

# # // Theo yêu cầu của đề bài, nếu Bob thắng hoặc hòa, ta trả về `False`. Thuật
# # // toán sẽ đếm `số_nguyên_âm = 0`, nên trả về `False`, chính xác.