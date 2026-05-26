# Bài **“Count the Number of Special Characters I”** là bài đếm số ký tự “đặc biệt” trong một chuỗi.

# ---

# ## Đề bài

# Cho một chuỗi `word` gồm chữ cái tiếng Anh viết thường và viết hoa.

# Một ký tự được gọi là **special** nếu:

# * ký tự viết thường của nó xuất hiện trong chuỗi
# * và ký tự viết hoa tương ứng cũng xuất hiện trong chuỗi.

# Ví dụ:

# * `'a'` và `'A'` cùng xuất hiện → `a` là special
# * `'b'` có nhưng `'B'` không có → không special

# Yêu cầu:
# Trả về số lượng ký tự special.

# ---

# ## Ví dụ 1

# Input:

# ```text
# word = "aaAbcBC"
# ```

# Phân tích:

# * `a` và `A` đều có → special
# * `b` và `B` đều có → special
# * `c` và `C` đều có → special

# Kết quả:

# ```text
# 3
# ```

# ---

# ## Ví dụ 2

# Input:

# ```text
# word = "abc"
# ```

# * chỉ có chữ thường
# * không có chữ hoa tương ứng

# Kết quả:

# ```text
# 0
# ```

# ---

# ## Ví dụ 3

# Input:

# ```text
# word = "abBCab"
# ```

# * `a` không có `A`
# * `b` có `B` → special
# * `c` có `C` không? không có

# Kết quả:

# ```text
# 1
# ```

# ---

# ## Ý tưởng

# Ta cần kiểm tra với mỗi chữ cái:

# * nếu có cả:

#   * chữ thường
#   * chữ hoa

# thì tăng đáp án.

# ---

# ## Cách làm bằng set

# ```python
# class Solution:
#     def numberOfSpecialChars(self, word: str) -> int:
#         s = set(word)
#         ans = 0

#         for c in 'abcdefghijklmnopqrstuvwxyz':
#             if c in s and c.upper() in s:
#                 ans += 1

#         return ans
# ```

# ---

# ## Giải thích code

# ### Bước 1

# ```python
# s = set(word)
# ```

# Lưu toàn bộ ký tự vào set để tìm nhanh.

# Ví dụ:

# ```python
# word = "aaAbcBC"
# ```

# thì:

# ```python
# s = {'a', 'A', 'b', 'B', 'c', 'C'}
# ```

# ---

# ### Bước 2

# Duyệt từng chữ cái từ `a -> z`

# ```python
# for c in 'abcdefghijklmnopqrstuvwxyz':
# ```

# ---

# ### Bước 3

# Kiểm tra:

# ```python
# if c in s and c.upper() in s:
# ```

# Ví dụ:

# ```python
# c = 'b'
# ```

# * `'b' in s` → True
# * `'B' in s` → True

# => special.

# ---

# ## Độ phức tạp

# * Time: `O(n)`
# * Space: `O(n)`

# với `n` là độ dài chuỗi.


class Solution(object):



    # Hàm đếm số ký tự special

    def numberOfSpecialChars(self, word):



        # Set lưu chữ thường xuất hiện trong chuỗi

        smallSet = set()



        # Set lưu chữ hoa xuất hiện trong chuỗi

        capitalSet = set()



        # Duyệt từng ký tự trong chuỗi

        for char in word:



            # Nếu là chữ thường từ a -> z

            if char >= 'a' and char <= 'z':



                # Thêm vào set chữ thường

                smallSet.add(char)



            # Ngược lại là chữ hoa

            else:



                # Thêm vào set chữ hoa

                capitalSet.add(char)



        count = 0



        # Duyệt các chữ thường đã xuất hiện

        for char in smallSet:



            # Kiểm tra chữ hoa tương ứng có tồn tại không

            if char.upper() in capitalSet:



                # Nếu có thì đây là ký tự special

                count += 1



        # Trả về kết quả

        return count

# Giải thích thuật toán

# Ý tưởng

# Một ký tự được gọi là special nếu:



# có chữ thường

# và có chữ hoa tương ứng.

# Ví dụ:



# a và A

# → special.

# Bước 1: Tạo 2 set

# smallSet = set()

# capitalSet = set()

# smallSet

# lưu chữ thường.

# capitalSet

# lưu chữ hoa.

# Set giúp:



# không lưu trùng

# tìm kiếm rất nhanh O(1).

# Bước 2: Duyệt chuỗi

# for char in word:

# Ví dụ:



# word = "aaAbcBC"

# Ta duyệt:



# a, a, A, b, c, B, C

# Bước 3: Phân loại chữ thường và chữ hoa

# Nếu là chữ thường

# if char >= 'a' and char <= 'z':

# Ví dụ:



# char = 'b'

# → thêm vào:



# smallSet.add(char)

# Kết quả:



# smallSet = {'a', 'b', 'c'}

# Nếu là chữ hoa

# capitalSet.add(char)

# Ví dụ:



# capitalSet = {'A', 'B', 'C'}

# Bước 4: Kiểm tra ký tự special

# for char in smallSet:

# Duyệt từng chữ thường.

# Ví dụ:



# char = 'b'

# Ta chuyển sang chữ hoa:



# char.upper()

# Kết quả:



# 'B'

# Kiểm tra:



# if char.upper() in capitalSet:

# Nếu tồn tại:

# → đây là ký tự special.

# → tăng biến đếm.

# Ví dụ chạy thực tế

# Input:



# word = "abBC"

# Sau khi duyệt:



# smallSet = {'a', 'b'}

# capitalSet = {'B', 'C'}

# Kiểm tra:



# a → A không có

# b → B có

# → kết quả:



# 1

# Độ phức tạp

# Time Complexity

# Duyệt chuỗi:



# O(n)

# Duyệt set:



# O(26)

# Tổng:



# O(n)

# Space Complexity

# Dùng 2 set:



# O(26)

# tức là:



# O(1)

# vì bảng chữ cái chỉ có 26 ký tự.