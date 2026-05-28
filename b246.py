# # Longest Common Suffix Queries(28/05/2026)

# # Ý tưởng của đề

# # Bạn có:



# # Một mảng wordsContainer

# # Một mảng wordsQuery

# # Với mỗi chuỗi trong wordsQuery, cần tìm chuỗi trong wordsContainer có hậu tố chung dài nhất với nó.

# # Hậu tố chung = các ký tự giống nhau ở cuối chuỗi.

# # Ví dụ:



# # "running" và "jogging" có suffix chung "ing" → độ dài 3

# "apple" và "people" có suffix chung "ple" → độ dài 3

# Điều cần trả về

# Với mỗi query:



# tìm index của từ trong wordsContainer

# sao cho suffix chung với query là dài nhất.

# Nếu có nhiều từ cùng độ dài suffix:



# chọn từ có độ dài nhỏ hơn

# nếu vẫn hòa → chọn index nhỏ hơn.

# Ví dụ

# wordsContainer = ["abcd","bcd","xbcd"]

# wordsQuery = ["cd","bcd","xyz"]

# Query 1: "cd"

# So sánh:



# # "abcd" ↔ "cd" → suffix chung "cd" (2)

# # "bcd" ↔ "cd" → "cd" (2)

# # "xbcd" ↔ "cd" → "cd" (2)

# Cả 3 đều bằng nhau.

# Xét tiếp độ dài chuỗi:



# "abcd" dài 4

# "bcd" dài 3

# "xbcd" dài 4

# => chọn "bcd" → index 1

# Query 2: "bcd"

# "abcd" ↔ "bcd" → "bcd" (3)

# "bcd" ↔ "bcd" → "bcd" (3)

# "xbcd" ↔ "bcd" → "bcd" (3)

# Tie tiếp.

# Độ dài:



# "abcd" = 4

# # "bcd" = 3

# # "xbcd" = 4

# # => chọn index 1

# # Query 3: "xyz"

# Không có suffix chung đáng kể.

# Mọi chuỗi chỉ match độ dài 0.

# Theo luật:



# chọn chuỗi ngắn nhất trong container.

# "bcd" ngắn nhất → index 1

# Kết quả

# [1,1,1]

# Cách nghĩ để giải

# Vì suffix nằm ở cuối chuỗi nên:

# 👉 đảo ngược chuỗi.

# Ví dụ:



# abcd -> dcba

# bcd  -> dcb

# Lúc này:

# “common suffix”

# sẽ trở thành

# “common prefix”.

# => dùng Trie để tìm nhanh.

# Ý tưởng Trie

# Insert:



# dcba

# dcb

# dcbx

# Khi query "cd":

# reverse:



# dc

# Đi theo Trie:



# d -> c

# được 2 ký tự.

# Node sâu nhất match chính là suffix dài nhất.

# Độ phức tạp

# Nếu dùng Trie:



# Build: O(total characters)

# Query: O(length of query)

# Rất nhanh cho dữ liệu lớn.

# Tóm tắt luật chọn

# Cho mỗi query:

# Ưu tiên theo thứ tự:



# suffix chung dài nhất

# word ngắn hơn

# index nhỏ hơn

# Nếu muốn mình có thể giải tiếp:



# cách cài Trie cho bài này

# ví dụ minh họa Trie từng bước

# code Java/Python/C++

# giải thích tại sao phải lưu index ở mỗi node 

from bisect import bisect_left

from math import inf

class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):



        # ============================================================

        # Ý tưởng chính

        #

        # Ta cần tìm:

        # word trong wordsContainer có LONGEST COMMON SUFFIX

        #

        # Trick:

        # Reverse chuỗi.

        #

        # suffix -> prefix

        #

        # Ví dụ:

        # "abcd" -> "dcba"

        # "xbcd" -> "dcbx"

        #

        # suffix chung "bcd"

        # sẽ trở thành

        # prefix chung "dcb"

        # ============================================================



        # ============================================================

        # BƯỚC 1:

        # Reverse toàn bộ wordsContainer

        #

        # Lưu:

        # (reversed_word, original_length, original_index)

        # ============================================================



        container = []



        for idx, w in enumerate(wordsContainer):



            # w[::-1] = đảo ngược chuỗi

            container.append((w[::-1], len(w), idx))



        # ============================================================

        # Sort theo reversed string

        #

        # Những string có prefix giống nhau

        # sẽ đứng gần nhau sau khi sort.

        # ============================================================



        container.sort(key=lambda x: x[0])



        # Chỉ lấy reversed string

        rev_words = [x[0] for x in container]



        # best_info[i] = (độ dài, original_index)

        #

        # Python so sánh tuple:

        #

        # (3,1) < (4,0)

        #

        # ưu tiên:

        # 1) length nhỏ hơn

        # 2) index nhỏ hơn

        #

        # đúng yêu cầu đề bài.

        best_info = [(x[1], x[2]) for x in container]



        n = len(container)



        # ============================================================

        # BƯỚC 2:

        # Build Segment Tree

        #

        # Segment Tree dùng để:

        #

        # query đoạn [L,R]

        # tìm word tốt nhất:

        #

        # 1) độ dài nhỏ nhất

        # 2) nếu bằng nhau -> index nhỏ nhất

        # ============================================================



        size = 1



        # tìm power of 2 >= n

        while size < n:

            size *= 2



        # khởi tạo segment tree

        seg = [(inf, inf)] * (2 * size)



        # đưa dữ liệu xuống lá

        for i in range(n):

            seg[size + i] = best_info[i]



        # build tree bottom-up

        for i in range(size - 1, 0, -1):



            # node cha = min(node trái, node phải)

            seg[i] = min(seg[2 * i], seg[2 * i + 1])



        # ============================================================

        # Hàm query segment tree

        #

        # Trả về:

        # best (length, index)

        # trong đoạn [l, r]

        # ============================================================



        def query(l, r):



            l += size

            r += size



            ans = (inf, inf)



            while l <= r:



                # l là con phải

                if l % 2 == 1:

                    ans = min(ans, seg[l])

                    l += 1



                # r là con trái

                if r % 2 == 0:

                    ans = min(ans, seg[r])

                    r -= 1



                # đi lên cha

                l //= 2

                r //= 2



            return ans



        # ============================================================

        # Hàm tính LCP

        #

        # Longest Common Prefix

        #

        # Ví dụ:

        # "dcbx"

        # "dcba"

        #

        # LCP = 3 ("dcb")

        # ============================================================



        def lcp(a, b):



            i = 0



            limit = min(len(a), len(b))



            while i < limit and a[i] == b[i]:

                i += 1



            return i



        # ============================================================

        # BƯỚC 3:

        # Xử lý từng query

        # ============================================================



        ans = []



        for q in wordsQuery:



            # reverse query

            rq = q[::-1]



            # ========================================================

            # Tìm vị trí insert của rq

            #

            # Vì rev_words đã sort.

            # ========================================================



            pos = bisect_left(rev_words, rq)



            # ========================================================

            # Maximum LCP chỉ cần check:

            #

            # - pos

            # - pos - 1

            #

            # vì các string gần nhau trong sorted order

            # sẽ có prefix giống nhau nhiều nhất.

            # ========================================================



            best_l = 0



            # check bên phải

            if pos < n:

                best_l = max(best_l, lcp(rev_words[pos], rq))



            # check bên trái

            if pos > 0:

                best_l = max(best_l, lcp(rev_words[pos - 1], rq))



            # ========================================================

            # Prefix match dài nhất

            # ========================================================



            prefix = rq[:best_l]



            # ========================================================

            # Các string có cùng prefix

            # sẽ tạo thành 1 block liên tiếp.

            #

            # Ta dùng binary search để tìm:

            #

            # left  = vị trí đầu tiên

            # right = vị trí cuối cùng

            # ========================================================



            left = bisect_left(rev_words, prefix)



            # prefix + "{"

            #

            # '{' nằm sau 'z' trong ASCII

            #

            # nên:

            #

            # prefix + "{"

            #

            # sẽ là string đầu tiên lớn hơn

            # mọi string bắt đầu bằng prefix.

            right = bisect_left(rev_words, prefix + "{") - 1



            # ========================================================

            # Query segment tree

            #

            # lấy:

            # 1) length nhỏ nhất

            # 2) index nhỏ nhất

            # ========================================================



            _, idx = query(left, right)



            ans.append(idx)



        return ans

# Tóm tắt thuật toán

# Bước 1

# Reverse tất cả chuỗi.



# suffix -> prefix

# Bước 2

# Sort reversed strings.

# Các string có prefix giống nhau sẽ đứng cạnh nhau.

# Bước 3

# Với mỗi query:



# reverse query

# dùng binary search tìm vị trí gần nhất

# tính longest common prefix

# tìm block có cùng prefix

# segment tree chọn word tốt nhất.

# Độ phức tạp

# Sort

# O(n log n)

# Mỗi query

# Binary search:



# O(log n)

# LCP:



# O(length)

# Segment tree:



# O(log n)

# Điểm hay của thuật toán

# Không dùng Trie.

# Dùng:



# reverse

# sorting

# binary search

# segment tree

# để giải bài suffix efficiently.