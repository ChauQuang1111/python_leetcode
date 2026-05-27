# Count the Number of Special Characters II (27/05/2026)
# ---

# # Ý nghĩa “special character”

# Một chữ cái được gọi là **special** nếu:

# * nó xuất hiện ở dạng **chữ thường** và **chữ hoa**
# * và **mọi chữ thường phải xuất hiện trước chữ hoa**

# Ví dụ với chữ `a`:

# * hợp lệ: `"aA"` ✅
# * hợp lệ: `"aaAAA"` ✅
# * không hợp lệ: `"Aa"` ❌
#   vì chữ hoa xuất hiện trước chữ thường

# ---

# # Ví dụ

# ## Ví dụ 1

# ```text
# word = "aaAbcBC"
# ```

# Xét từng chữ:

# ### Chữ `a`

# * có `a`
# * có `A`
# * tất cả `a` đứng trước `A`

# → special ✅

# ---

# ### Chữ `b`

# * có `b`
# * có `B`
# * `b` đứng trước `B`

# → special ✅

# ---

# ### Chữ `c`

# * có `c`
# * có `C`
# * `c` đứng trước `C`

# → special ✅

# Kết quả:

# ```text
# 3
# ```

# ---

# # Ví dụ 2

# ```text
# word = "AbBCab"
# ```

# ### Chữ `a`

# * `A` xuất hiện trước `a`

# → không special ❌

# ### Chữ `b`

# * `B` xuất hiện trước `b`

# → không special ❌

# ### Chữ `c`

# * chỉ có `C`, không có `c`

# → không special ❌

# Kết quả:

# ```text
# 0
# ```

# ---

# # Ý tưởng của bài

# Ta cần kiểm tra cho mỗi chữ cái:

# 1. Có xuất hiện chữ thường không?
# 2. Có xuất hiện chữ hoa không?
# 3. Vị trí cuối của chữ thường có nằm trước vị trí đầu của chữ hoa không?

# Nếu:

# ```text
# last lowercase < first uppercase
# ```

# thì ký tự đó là special.

# ---

# # Ví dụ minh họa vị trí

# ```text
# word = "aabA"
# index: 0123
# ```

# * vị trí cuối của `a` = 2
# * vị trí đầu của `A` = 3

# ```text
# 2 < 3
# ```

# → hợp lệ ✅

# ---

# Nhưng:

# ```text
# word = "Aa"
# index: 01
# ```

# * vị trí cuối của `a` = 1
# * vị trí đầu của `A` = 0

# ```text
# 1 < 0  ❌
# ```

# → không hợp lệ.

# ---

# # Tóm tắt ngắn gọn

# Một ký tự special khi:

# ```text
# - có cả lowercase và uppercase
# - lowercase xuất hiện hoàn toàn trước uppercase
# ```

# Ví dụ:

# | Chuỗi    | Kết quả |
# | -------- | ------- |
# | `"aA"`   | ✅       |
# | `"aaAA"` | ✅       |
# | `"Aa"`   | ❌       |
# | `"aAa"`  | ❌       |




# Code của bạn:



# class Solution:

#     def numberOfSpecialChars(self, word: str, ans = 0) -> int:

        

#         for ch, CH in zip(ascii_lowercase, ascii_uppercase):



#             if ch not in word or CH not in word: 

#                 continue

  

#             ans += word.rfind(ch) < word.find(CH)



#         return ans

# Ý tưởng thuật toán

# Ta duyệt từng cặp:



# a - A

# b - B

# c - C

# ...

# Sau đó kiểm tra:



# có tồn tại cả chữ thường và chữ hoa không

# vị trí cuối của chữ thường có nằm trước vị trí đầu của chữ hoa không

# Nếu đúng → là special character.

# Giải thích từng dòng

# 1. Hàm

# def numberOfSpecialChars(self, word: str, ans = 0) -> int:

# word: chuỗi đầu vào

# ans: biến đếm số ký tự special

# trả về int

# 2. Duyệt 26 chữ cái

# for ch, CH in zip(ascii_lowercase, ascii_uppercase):

# ascii_lowercase



# abcdefghijklmnopqrstuvwxyz

# ascii_uppercase



# ABCDEFGHIJKLMNOPQRSTUVWXYZ

# zip() ghép từng cặp:

# chCHaAbBcC

# ...

# 3. Kiểm tra có tồn tại cả 2 hay không

# if ch not in word or CH not in word:

#     continue

# Ví dụ:



# word = "aaAb"

# có a

# có A

# → tiếp tục kiểm tra

# Nhưng với b:



# có b

# không có B

# → bỏ qua.

# 4. Kiểm tra điều kiện special

# ans += word.rfind(ch) < word.find(CH)

# word.rfind(ch)

# Tìm vị trí xuất hiện CUỐI của chữ thường.

# Ví dụ:



# word = "aaAb"

# word.rfind('a')

# Kết quả:



# 1

# word.find(CH)

# Tìm vị trí xuất hiện ĐẦU của chữ hoa.



# word.find('A')

# Kết quả:



# 2

# So sánh

# 1 < 2

# → True

# Vì sao dùng += được?

# Trong Python:



# True  = 1

# False = 0

# Nên:



# ans += True

# tương đương:



# ans += 1

# Ví dụ chạy thực tế

# word = "aaAbcBC"

# Với a

# word.rfind('a') = 1

# word.find('A')  = 2

# 1 < 2

# ✅ ans = 1

# Với b

# word.rfind('b') = 3

# word.find('B')  = 5

# ✅ ans = 2

# Với c

# word.rfind('c') = 4

# word.find('C')  = 6

# ✅ ans = 3

# Code có chú thích đầy đủ

from string import ascii_lowercase, ascii_uppercase
class Solution:

    def numberOfSpecialChars(self, word: str) -> int:



        # biến đếm số ký tự special

        ans = 0



        # duyệt từng cặp:

        # a-A, b-B, c-C ...

        for ch, CH in zip(ascii_lowercase, ascii_uppercase):



            # nếu thiếu chữ thường hoặc chữ hoa

            # thì bỏ qua

            if ch not in word or CH not in word:

                continue



            # vị trí cuối của chữ thường

            last_lower = word.rfind(ch)



            # vị trí đầu của chữ hoa

            first_upper = word.find(CH)



            # nếu lowercase nằm trước uppercase

            # thì đây là special character

            if last_lower < first_upper:

                ans += 1



        return ans

# Độ phức tạp

# Ta duyệt 26 chữ cái:



# O(26 * n)

# ≈



# O(n)

# vì 26 là hằng số.