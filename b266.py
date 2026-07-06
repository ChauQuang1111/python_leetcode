# Bài toán Remove Covered Intervals (06/07/2026)


# Đề bài

# Cho một mảng intervals, trong đó mỗi phần tử là một khoảng:



# intervals[i] = [li, ri]

# li: điểm bắt đầu

# ri: điểm kết thúc

# Nếu một khoảng nằm hoàn toàn bên trong một khoảng khác thì nó được gọi là covered (bị bao phủ).

# Nhiệm vụ là:



# Xóa tất cả các khoảng bị bao phủ và trả về số lượng khoảng còn lại.

# Khi nào một khoảng bị bao phủ?

# Khoảng A = [a, b] bị bao phủ bởi khoảng B = [c, d] nếu:



# c <= a

# và

# b <= d

# Nghĩa là:



# B bắt đầu trước hoặc đúng lúc A bắt đầu.

# B kết thúc sau hoặc đúng lúc A kết thúc.

# Hay nói cách khác:



# B chứa hoàn toàn A.

# Ví dụ 1

# intervals = [[1,4],[3,6],[2,8]]

# Vẽ trên trục số:



# [1----------------4]



#       [3---------------6]



#    [2-------------------------8]

# Khoảng [3,6]



# bắt đầu sau 2

# kết thúc trước 8

# nên



# [3,6]

# được bao phủ bởi



# [2,8]

# Sau khi xóa:



# [[1,4],[2,8]]

# Đáp án:



# 2

# Ví dụ 2

# [[1,4],[2,3]]

# [1----------------4]



#    [2------3]

# [2,3] nằm hoàn toàn trong [1,4].

# Xóa [2,3].

# Còn:



# [[1,4]]

# Đáp án:



# 1

# Ví dụ 3

# [[1,2],[2,3]]

# [1-----2]



#       [2------3]

# Không khoảng nào chứa hoàn toàn khoảng còn lại.

# Mặc dù chúng chạm nhau tại điểm 2, nhưng:



# [1,2] không chứa [2,3]

# [2,3] cũng không chứa [1,2]

# Đáp án:



# 2

# Ví dụ 4

# [[1,10],[2,5],[3,4],[6,9]]

# [1--------------------------------10]



#     [2-----------5]



#        [3----4]



#                  [6-------9]

# Các khoảng:



# [2,5]

# [3,4]

# [6,9]

# đều nằm hoàn toàn trong [1,10].

# Sau khi xóa chỉ còn:



# [[1,10]]

# Đáp án:



# 1

# Điều đề bài thực sự hỏi

# Đề bài không yêu cầu bạn hợp nhất (merge) các khoảng hay tìm giao nhau.

# Nó chỉ hỏi:



# Có bao nhiêu khoảng không bị chứa hoàn toàn trong bất kỳ khoảng nào khác?

# Hay nói cách khác:



# Duyệt qua các khoảng.

# Nếu tìm thấy một khoảng khác chứa hoàn toàn nó thì xóa nó.

# Cuối cùng đếm số khoảng còn lại.

# Tóm tắt

# Một khoảng [a, b] bị bao phủ nếu tồn tại một khoảng [c, d] sao cho:



# c <= a

# và

# b <= d

# Ví dụ:



# [1,8] chứa [2,5]     ✓

# [1,8] chứa [1,8]     ✓ (hai khoảng trùng nhau cũng được xem là covered theo điều kiện)

# [1,8] chứa [0,5]     ✗

# [1,8] chứa [3,10]    ✗

# [1,8] chứa [8,9]     ✗

# Mục tiêu cuối cùng là đếm số khoảng không bị khoảng nào khác bao phủ.


# Ý tưởng của thuật toán là sắp xếp các khoảng theo điểm bắt đầu tăng dần, nếu cùng điểm bắt đầu thì khoảng dài hơn đứng trước. Sau khi sắp xếp như vậy, ta chỉ cần theo dõi khoảng lớn nhất hiện tại để biết các khoảng phía sau có bị bao phủ hay không.

# Dưới đây là code đã được thêm chú thích:


from typing import List
class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]):



        # Sắp xếp:

        # 1. start tăng dần

        # 2. Nếu cùng start thì end giảm dần

        #

        # Ví dụ:

        # [[1,4],[1,5],[2,3]]

        # =>

        # [[1,5],[1,4],[2,3]]

        #

        # Làm như vậy để khoảng lớn hơn luôn đứng trước khoảng nhỏ hơn.

        intervals.sort(key=lambda x: (x[0], -x[1]))



        # Ban đầu giả sử tất cả khoảng đều được giữ lại.

        ans = len(intervals)



        # Khoảng đầu tiên chắc chắn chưa bị khoảng nào trước nó bao phủ.

        low = intervals[0][0]

        high = intervals[0][1]



        # Duyệt từ khoảng thứ hai.

        for i in range(1, len(intervals)):



            # Nếu cùng điểm bắt đầu

            #

            # Ví dụ:

            # [1,6]

            # [1,4]

            #

            # Vì đã sort end giảm dần nên [1,6] đứng trước.

            # => [1,4] chắc chắn bị bao phủ.

            if intervals[i][0] == low:

                ans -= 1



            # Hoặc khoảng hiện tại kết thúc trước hoặc bằng khoảng đang giữ.

            #

            # Ví dụ:

            # current: [2,5]

            # previous: [1,8]

            #

            # 5 <= 8

            # => [2,5] nằm hoàn toàn trong [1,8]

            elif intervals[i][1] <= high:

                ans -= 1



            # Nếu không rơi vào hai trường hợp trên

            # nghĩa là khoảng này không bị bao phủ.

            #

            # Ví dụ:

            # previous: [1,4]

            # current : [2,8]

            #

            # current kéo dài hơn nên trở thành khoảng lớn nhất mới.

            else:

                low = intervals[i][0]

                high = intervals[i][1]



        return ans

# Minh họa bằng ví dụ

# Ví dụ

# intervals = [[1,4],[3,6],[2,8]]

# Bước 1: Sort

# [[1,4],[2,8],[3,6]]

# Ban đầu

# low = 1

# high = 4

# ans = 3

# Xét [2,8]

# start = 2 != low

# end = 8 > high(4)

# Không bị bao phủ.

# Cập nhật



# low = 2

# high = 8

# ans = 3

# Xét [3,6]

# start = 3 != low

# end = 6 <= 8

# Bị bao phủ bởi [2,8]



# ans = 2

# Kết quả:



# 2

# Tại sao chỉ cần lưu high?

# Sau khi sort:



# Các khoảng luôn có start không giảm.

# Khi gặp một khoảng có end lớn hơn high, nó sẽ là khoảng "mạnh" nhất (bao phủ được nhiều khoảng nhất) trong số các khoảng đã duyệt.

# Vì vậy, chỉ cần nhớ khoảng có end lớn nhất hiện tại (được biểu diễn bởi high). Mọi khoảng phía sau có end <= high sẽ chắc chắn bị khoảng đó bao phủ.

# Có thể đơn giản hóa code hơn bằng cách không cần lưu low, vì điều kiện intervals[i][1] <= high đã bao gồm cả trường hợp hai khoảng có cùng điểm bắt đầu (do đã sắp xếp end giảm dần):



class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]):

        intervals.sort(key=lambda x: (x[0], -x[1]))



        ans = len(intervals)

        high = intervals[0][1]



        for i in range(1, len(intervals)):

            if intervals[i][1] <= high:

                ans -= 1

            else:

                high = intervals[i][1]



        return ans

# Phiên bản này ngắn gọn hơn nhưng vẫn đúng vì cách sắp xếp đã đảm bảo các khoảng có cùng điểm bắt đầu sẽ được xử lý chính xác.