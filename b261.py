# Bài 1967. Number of Strings That Appear as Substrings in Word (29/06/2026)


# Cho một mảng patterns gồm các chuỗi và một chuỗi word.

# Hãy đếm xem có bao nhiêu chuỗi trong patterns xuất hiện dưới dạng substring của word.

# Substring là gì?

# Substring là một chuỗi con liên tiếp của một chuỗi.

# Ví dụ:



# word = "abcde"

# Các substring của "abcde":



# "a" ✅

# "ab" ✅

# "abc" ✅

# "bcd" ✅

# "cde" ✅

# "de" ✅

# Không phải substring:



# "ace" ❌ (không liên tiếp)

# "ad" ❌

# Ví dụ 1

# patterns = ["a", "abc", "bc", "d"]

# word = "abc"

# Kiểm tra từng phần tử:

# PatternCó trong "abc" không?"a"✅"abc"✅"bc"✅"d"❌

# Có 3 chuỗi xuất hiện.

# Output



# 3

# Ví dụ 2

# patterns = ["a", "b", "c"]

# word = "aaaaab"

# Kiểm tra:



# "a" → có ✅

# "b" → có ✅

# "c" → không ❌

# Kết quả:



# 2

# Ví dụ 3

# patterns = ["xyz", "xy", "yz"]

# word = "xyz"

# "xyz" ✅

# "xy" ✅

# "yz" ✅

# Kết quả:



# 3

# Ý tưởng bài toán

# Ta duyệt từng chuỗi trong patterns.

# Với mỗi chuỗi:



# nếu nó xuất hiện trong word thì tăng biến đếm lên 1.

# Ví dụ:



# patterns = ["ab", "cd", "bc"]

# word = "abcd"



# "ab" -> có

# "cd" -> có

# "bc" -> có



# => đáp án = 3

# Minh họa trực quan

# word = "leetcode"



# l e e t c o d e

#       └────┘

#       "tco"



# "leet"  ✓

# "code"  ✓

# "etc"   ✓

# "edo"   ✗

# Ràng buộc

# 1 <= patterns.length <= 100

# 1 <= patterns[i].length <= 100

# 1 <= word.length <= 100

# Vì độ dài đều nhỏ (tối đa 100), nên chỉ cần kiểm tra từng chuỗi trong patterns có phải là substring của word hay không là đủ.

# Tóm tắt

# Bài toán yêu cầu:



# Duyệt qua từng chuỗi trong patterns.

# Kiểm tra xem chuỗi đó có xuất hiện liên tiếp trong word hay không.

# Nếu có thì cộng vào kết quả.

# Trả về tổng số chuỗi thỏa mãn.


# Đây là lời giải đơn giản sử dụng toán tử in của Python để kiểm tra một chuỗi có phải là substring của chuỗi khác hay không.



# Giải thích thuật toán

# Bước 1: Khởi tạo biến đếm

# c = 0

# c dùng để lưu số lượng chuỗi trong patterns xuất hiện trong word.

# Bước 2: Duyệt từng chuỗi trong patterns

# for p in patterns:

# Ví dụ:



# patterns = ["a", "abc", "bc", "d"]

# Vòng lặp sẽ lần lượt lấy:



# p = "a"

# p = "abc"

# p = "bc"

# p = "d"

# Bước 3: Kiểm tra substring

# if p in word:

# Toán tử in trong Python sẽ kiểm tra xem chuỗi p có xuất hiện liên tiếp trong word hay không.

# Ví dụ:



# word = "abc"



# "a" in word      # True

# "bc" in word     # True

# "abc" in word    # True

# "d" in word      # False

# Nếu kết quả là True thì tăng biến đếm:



# c += 1

# Bước 4: Trả về kết quả

# return c

# Sau khi kiểm tra tất cả các chuỗi trong patterns, trả về tổng số chuỗi xuất hiện trong word.

# Code có chú thích
from typing import List
class Solution:

    def numOfStrings(self, patterns: List[str], word: str) -> int:

        # Biến đếm số chuỗi xuất hiện trong word

        c = 0



        # Duyệt qua từng chuỗi trong mảng patterns

        for p in patterns:



            # Kiểm tra p có phải là substring của word hay không

            # Toán tử "in" trả về True nếu p xuất hiện trong word

            if p in word:



                # Nếu có thì tăng biến đếm lên 1

                c += 1



        # Trả về tổng số chuỗi tìm thấy

        return c

# Ví dụ chạy từng bước

# patterns = ["a", "abc", "bc", "d"]

# word = "abc"

# Lần lặppp in wordc1"a"True12"abc"True23"bc"True34"d"False3

# Kết quả cuối cùng:



# return 3

# Độ phức tạp

# Giả sử:

# n = len(patterns)

# m = len(word)

# k là độ dài trung bình của mỗi chuỗi trong patterns.

# Vòng lặp chạy n lần.

# Mỗi lần, phép kiểm tra p in word có độ phức tạp xấp xỉ O(m × k) trong trường hợp xấu nhất.

# Vì vậy, độ phức tạp tổng quát là:



# Thời gian: O(n × m × k) (với ràng buộc của bài đều ≤ 100 nên chạy rất nhanh).

# Không gian: O(1) vì chỉ sử dụng một biến đếm và không tạo thêm cấu trúc dữ liệu đáng kể.