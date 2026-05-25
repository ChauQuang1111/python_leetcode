# Bài Jump Game VII (25/05/2026)
# Đề bài nói gì?

# Cho:



# Một chuỗi nhị phân s

# '0' = có thể đứng

# '1' = không thể đứng

# Hai số:

# minJump

# maxJump

# Ban đầu đứng ở index 0.

# Từ vị trí i, bạn được nhảy tới j nếu:

# [

# i + minJump \le j \le i + maxJump

# ]

# và:



# s[j] == '0'

# Mục tiêu:



# Kiểm tra xem có đi tới index cuối cùng được không.

# Ví dụ 1

# s = "011010"

# minJump = 2

# maxJump = 3

# Đánh index:



# index: 0 1 2 3 4 5

# s:     0 1 1 0 1 0

# Bắt đầu ở 0.



# Từ index 0:

# Được nhảy từ:

# [

# 0 + 2 = 2

# ]

# đến

# [

# 0 + 3 = 3

# ]

# => Có thể xét index 2 và 3.



# index 2 = '1' ❌

# index 3 = '0' ✅

# => Nhảy tới 3.

# Từ index 3:

# Được nhảy từ:

# [

# 3 + 2 = 5

# ]

# đến

# [

# 3 + 3 = 6

# ]

# nhưng chuỗi chỉ tới index 5.

# => xét index 5:



# index 5 = '0'

# => tới đích.

# Kết quả:



# true

# Ví dụ 2

# s = "01101110"

# minJump = 2

# maxJump = 3

# index: 0 1 2 3 4 5 6 7

# s:     0 1 1 0 1 1 1 0

# Từ 0:



# có thể tới 2 hoặc 3

# 2 = 1

# 3 = 0

# => tới 3.

# Từ 3:



# có thể tới 5 hoặc 6

# cả hai đều là 1

# => bị kẹt.

# Không tới cuối được.

# Kết quả:



# false

# Ý tưởng bài này

# Đây là bài:



# BFS

# DP

# Sliding Window

# vì cần kiểm tra:



# “Từ vị trí hiện tại có thể đi tiếp tới đâu?”

# Điều quan trọng nhất

# Nếu đang ở vị trí i:

# Ta chỉ được nhảy trong đoạn:

# [

# [i + minJump,\ i + maxJump]

# ]

# và chỉ nhảy tới nơi có '0'.

# Constraint quan trọng

# s.length <= 10^5

# => Không thể brute force thử mọi đường đi kiểu DFS thường.

# Cần tối ưu xuống:



# O(n)

# Tư duy đơn giản nhất

# Tạo mảng:

# reachable[i]

# true nếu tới được index i

# false nếu không

# Ban đầu:

# reachable[0] = true

# Sau đó duyệt từng vị trí để xem có thể nhảy tiếp không. (neetcode.io)


# Thuật toán này dùng ý tưởng:



# DFS/BFS để duyệt các vị trí có thể tới

# visited để tránh duyệt lại

# Chỉ xét các vị trí trong khoảng:

# [

# [i + minJump,\ i + maxJump]

# ]

# và phải là '0'.

# Dưới đây là code đã thêm chú thích chi tiết:



class Solution:

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        

        # Nếu vị trí cuối là '1'

        # => không thể đứng ở đích

        #

        # Hoặc tồn tại đoạn liên tiếp toàn '1'

        # dài bằng maxJump

        # => có thể bị chặn hoàn toàn

        if s[-1] == '1' or '1' * maxJump in s:

            return False



        n = len(s)



        # Trường hợp đặc biệt:

        # chỉ được nhảy đúng 1 khoảng cố định

        #

        # Ví dụ:

        # minJump = maxJump = 3

        #

        # Khi đó chỉ có thể đi:

        # 0 -> 3 -> 6 -> 9 ...

        if minJump == maxJump:



            # (n - 1) phải chia hết cho minJump

            # để có thể tới đúng vị trí cuối

            #

            # đồng thời các vị trí nhảy tới

            # đều phải là '0'

            return (

                (n - 1) % minJump == 0

                and '1' not in s[::minJump]

            )



        # maxJump + 1

        # dùng để tránh cộng nhiều lần

        maxJump_1 = maxJump + 1



        # index lớn nhất mà từ đó

        # có thể nhảy tới cuối

        #

        # nếu j >= n - (maxJump + 1)

        # thì từ j có thể tới đích

        n_maxJump_1 = n - maxJump_1



        # index cuối cùng có thể bắt đầu nhảy

        n_minJump = n - minJump



        # visited:

        # lưu các vị trí đã xét

        visited = set([0])



        # stack dùng cho DFS

        stack = [0]



        while stack:



            # lấy vị trí hiện tại

            i = stack.pop()



            # vị trí nhỏ nhất có thể nhảy tới

            lower = i + minJump



            # duyệt toàn bộ vị trí có thể nhảy

            #

            # từ:

            # i + minJump

            #

            # tới:

            # i + maxJump

            #

            # enumerate giúp lấy:

            # j = index thực

            # c = ký tự tại index đó

            for j, c in enumerate(

                s[lower:min(n_minJump, i + maxJump_1)],

                start=lower

            ):



                # nếu chưa thăm

                # và là vị trí hợp lệ ('0')

                if j not in visited and c == '0':



                    # nếu từ j có thể nhảy tới cuối

                    # => return True ngay

                    if j >= n_maxJump_1:

                        return True



                    # thêm vào stack để DFS tiếp

                    stack.append(j)



                    # đánh dấu đã thăm

                    visited.add(j)



        # duyệt xong mà không tới được cuối

        return False

# Minh hoạ hoạt động

# Ví dụ:



# s = "011010"

# minJump = 2

# maxJump = 3

# Bước 1

# Đang ở:



# 0

# Có thể nhảy tới:



# [2, 3]

# index 2 = '1' ❌

# index 3 = '0' ✅

# => push 3 vào stack

# Bước 2

# Đang ở:



# 3

# Có thể nhảy tới:



# [5, 6]

# 5 tồn tại và là '0'

# => tới đích.

# Độ phức tạp

# Time

# Gần:



# O(n)

# vì mỗi node chỉ được visited 1 lần.

# Space

# O(n)

# do dùng:



# visited

# stack