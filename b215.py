# # The k-th Lexicographical String of All Happy Strings of Length n(14/03/2026)

# # Bài **“The k-th Lexicographical String of All Happy Strings of Length n”** (trên LeetCode 1415: The k-th Lexicographical String of All Happy Strings of Length n) có ý nghĩa như sau:

# Thuật toán này **không sinh toàn bộ chuỗi** (tránh backtracking), mà **đếm số lượng chuỗi có thể tạo ở mỗi nhánh rồi bỏ qua cả một “block”** nếu `k` lớn hơn số chuỗi trong block đó. Nhờ vậy chạy **O(n)**.

# Ý tưởng chính:

# * Tổng số happy string độ dài `n` là
#   `3 × 2^(n-1)`
# * Sau khi chọn 1 ký tự:

#   * mỗi vị trí tiếp theo chỉ có **2 lựa chọn** (không trùng ký tự trước)
# * Nếu ta cố định một ký tự ở vị trí `i`, số chuỗi còn lại sẽ là:

# ```
# 2^(remaining_len)
# ```

# vì mỗi vị trí còn lại có 2 cách chọn.

# ---

# ## Code đã thêm chú thích chi tiết

# ```python
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        # Tổng số happy string có thể tạo với độ dài n
        # vị trí đầu: 3 lựa chọn
        # mỗi vị trí sau: 2 lựa chọn
        total = 3 * (1 << (n - 1))   # 3 * 2^(n-1)

        # Nếu k lớn hơn tổng số chuỗi → không tồn tại
        if k > total:
            return ""

        ans = []      # lưu kết quả
        prev = ""     # ký tự trước đó (để tránh trùng)

        # duyệt từng vị trí trong chuỗi
        for i in range(n):

            # thử các ký tự theo thứ tự từ điển
            for ch in ['a', 'b', 'c']:

                # nếu trùng ký tự trước thì bỏ qua
                if ch == prev:
                    continue

                # số ký tự còn lại sau khi chọn ch ở vị trí i
                remaining_len = n - i - 1

                # số chuỗi có thể tạo nếu chọn ch tại đây
                # mỗi vị trí còn lại có 2 lựa chọn
                cnt = 1 << remaining_len   # 2^remaining_len

                # nếu k lớn hơn số chuỗi của nhánh này
                # nghĩa là chuỗi thứ k không nằm trong block này
                if k > cnt:
                    # bỏ qua toàn bộ block này
                    k -= cnt

                else:
                    # chuỗi thứ k nằm trong block này
                    ans.append(ch)  # chọn ký tự này
                    prev = ch       # cập nhật ký tự trước
                    break           # sang vị trí tiếp theo

        # ghép các ký tự thành chuỗi
        return "".join(ans)


# ---

# # Ví dụ minh họa trực quan

# ### Input

# ```
# n = 3
# k = 9
# ```

# Tổng chuỗi:

# ```
# 3 × 2² = 12
# ```

# Danh sách:

# ```
# 1  aba
# 2  abc
# 3  aca
# 4  acb
# 5  bab
# 6  bac
# 7  bca
# 8  bcb
# 9  cab
# 10 cac
# 11 cba
# 12 cbc
# ```

# ---

# ### Vị trí 0

# thử `'a'`

# số chuỗi nếu bắt đầu bằng `'a'`:

# ```
# 2^(3-1-0) = 4
# ```

# ```
# aba
# abc
# aca
# acb
# ```

# k = 9 > 4 → bỏ qua

# ```
# k = 9 - 4 = 5
# ```

# ---

# thử `'b'`

# ```
# 2^2 = 4
# ```

# ```
# bab
# bac
# bca
# bcb
# ```

# k = 5 > 4 → bỏ qua

# ```
# k = 5 - 4 = 1
# ```

# ---

# thử `'c'`

# ```
# 2^2 = 4
# ```

# k = 1 ≤ 4 → chọn `'c'`

# ---

# ### Vị trí 1

# prev = `'c'`

# thử `'a'`

# ```
# 2^(3-2) = 2
# ```

# k = 1 ≤ 2 → chọn `'a'`

# ---

# ### Vị trí 2

# prev = `'a'`

# thử `'b'`

# ```
# 2^0 = 1
# ```

# k = 1 → chọn `'b'`

# ---

# ### kết quả

# ```
# cab
# ```

# ---

# ✅ **Tóm lại tư duy thuật toán**

# 1. Không sinh tất cả chuỗi.
# 2. Ở mỗi vị trí:

#    * thử `'a' → 'b' → 'c'`
# 3. Tính **bao nhiêu chuỗi bắt đầu bằng lựa chọn đó**
# 4. Nếu `k` lớn hơn → **bỏ qua cả block**
# 5. Nếu không → **chọn ký tự đó**

# ---

# Nếu bạn muốn, tôi có thể giải thích thêm **vì sao `cnt = 2^(remaining_len)` đúng** (đây là chỗ quan trọng nhất của bài này).




# ---

# ## 1. Khái niệm **Happy String**

# Một **happy string** là chuỗi:

# * Chỉ gồm 3 ký tự: **'a', 'b', 'c'**
# * **Hai ký tự liền nhau không được giống nhau**

# Ví dụ:

# * `"ab"` ✔ hợp lệ
# * `"acb"` ✔ hợp lệ
# * `"aa"` ❌ không hợp lệ (vì 2 chữ `a` cạnh nhau)

# ---

# ## 2. Ý nghĩa đề bài

# Bạn được cho:

# * **n** → độ dài chuỗi
# * **k** → vị trí trong thứ tự từ điển

# Nhiệm vụ:

# 1. **Liệt kê tất cả happy string có độ dài n**
# 2. **Sắp xếp chúng theo thứ tự từ điển (lexicographical order)**
# 3. **Lấy chuỗi đứng thứ k**

# Nếu **không có đủ k chuỗi** → trả về **"" (chuỗi rỗng)**

# ---

# ## 3. Thứ tự từ điển (Lexicographical)

# Giống như **từ điển tiếng Anh**.

# Ví dụ:

# ```
# a < b < c
# ```

# So sánh chuỗi:

# ```
# ab < ac < ba
# ```

# ---

# ## 4. Ví dụ

# ### Ví dụ 1

# ```
# n = 1
# k = 3
# ```

# Các happy string:

# ```
# a
# b
# c
# ```

# Thứ tự:

# ```
# 1: a
# 2: b
# 3: c
# ```

# → **k = 3 → "c"**

# ---

# ### Ví dụ 2

# ```
# n = 3
# k = 9
# ```

# Tất cả happy string độ dài 3:

# ```
# aba
# abc
# aca
# acb
# bab
# bac
# bca
# bcb
# cab
# cac
# cba
# cbc
# ```

# Thứ tự:

# ```
# 1  aba
# 2  abc
# 3  aca
# 4  acb
# 5  bab
# 6  bac
# 7  bca
# 8  bcb
# 9  cab   ← k = 9
# ```

# → kết quả:

# ```
# "cab"
# ```

# ---

# ## 5. Bản chất bài toán

# Bạn cần:

# * **Sinh tất cả chuỗi độ dài n**
# * **Không cho 2 ký tự liên tiếp giống nhau**
# * **Sắp xếp theo từ điển**
# * **Lấy phần tử thứ k**

# Thường giải bằng:

# * **Backtracking / DFS**

# ---

# ## 6. Quy luật số lượng chuỗi

# Số happy string độ dài **n**:

# ```
# 3 × 2^(n-1)
# ```

# Vì:

# * vị trí đầu: **3 lựa chọn**
# * mỗi vị trí sau: **2 lựa chọn** (không trùng ký tự trước)

# Ví dụ:

# ```
# n = 3
# 3 × 2² = 12 chuỗi
# ```

# ---

# ✅ **Tóm lại đề bài:**

# > Tạo tất cả chuỗi độ dài **n** từ `{a,b,c}` sao cho **không có hai ký tự liền nhau giống nhau**, sắp xếp theo **thứ tự từ điển**, rồi trả về **chuỗi đứng thứ k**.

# ---

# Nếu bạn muốn, tôi có thể giải tiếp:

# * **Cách nghĩ ra thuật toán rất nhanh (O(n)) thay vì sinh hết chuỗi**
# * Hoặc **code Java DFS/backtracking rất ngắn cho bài này**.
