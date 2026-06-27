# Find the Maximum Number of Elements in Subset.(27/06/2026)
# Nếu bạn đang nói đến phiên bản phổ biến thì ý tưởng của đề như sau:

# Mô tả

# Cho một mảng gồm N số nguyên.

# Hãy tìm một tập con (subset) của mảng sao cho thỏa mãn điều kiện nào đó (điều kiện sẽ được nêu trong đề), và số lượng phần tử trong tập con là lớn nhất.

# Lưu ý:



# Subset là tập con của các phần tử trong mảng.

# Không cần các phần tử phải đứng liền nhau.

# Có thể chọn hoặc không chọn mỗi phần tử.

# Ví dụ:



# A = [1, 2, 3]

# Các subset có thể là:



# {}

# {1}

# {2}

# {3}

# {1,2}

# {1,3}

# {2,3}

# {1,2,3}

# "Maximum Number of Elements"

# Cụm này có nghĩa là:



# Hãy chọn được nhiều phần tử nhất có thể nhưng vẫn thỏa mãn điều kiện của đề.

# Ví dụ nếu điều kiện là:



# Hiệu giữa phần tử lớn nhất và nhỏ nhất không vượt quá 1.

# Cho:



# A = [1,2,2,3,1,2]

# Các tập con hợp lệ:



# {1,1,2,2,2}  (5 phần tử)

# {2,2,2,3}    (4 phần tử)

# Đáp án sẽ là



# 5

# vì 5 là số lượng phần tử lớn nhất.

# Nếu đây là bài trên HackerRank

# Đề đầy đủ thường là:



# Given an array of integers, find the size of the largest subset where the absolute difference between any two elements is less than or equal to 1.

# Nghĩa là:



# Chọn một tập con.

# Với mọi cặp phần tử trong tập con:

# |a - b| ≤ 1

# In ra kích thước lớn nhất của tập con đó.

# Ví dụ



# 6

# 4 6 5 3 3 1

# Ta có tần suất:



# 1 : 1

# 3 : 2

# 4 : 1

# 5 : 1

# 6 : 1

# Xét từng cặp số liên tiếp:



# 1 và 2 → 1

# 2 và 3 → 2

# 3 và 4 → 3

# 4 và 5 → 2

# 5 và 6 → 2

# Lớn nhất là



# 3

# tương ứng với tập



# {3,3,4}

# Đoạn code này là lời giải cho bài Find the Maximum Number of Elements in Subset trên LeetCode. Ý tưởng của thuật toán khá khó hiểu nếu chỉ nhìn code, nên mình sẽ giải thích từng bước.

# Ý tưởng của bài toán

# Ta cần tạo một tập con có dạng:



# x, x,

# x², x²,

# x⁴, x⁴,

# x⁸, x⁸,

# ...

# cuối cùng chỉ còn 1 phần tử

# Nghĩa là:



# Mỗi số (trừ số cuối) phải xuất hiện ít nhất 2 lần.

# Vì khi chuyển sang số bình phương tiếp theo thì ta "tiêu thụ" 2 phần tử.

# Riêng số cuối cùng chỉ cần 1 lần.

# Ví dụ



# 2 2 4 4 16

# Ta có



# 2² = 4

# 4² = 16

# Độ dài là



# 5

# Bước 1

# count = Counter(nums)

# Đếm số lần xuất hiện của mỗi số.

# Ví dụ



# nums = [2,2,4,4,16]

# thì



# count =

# {

# 2:2,

# 4:2,

# 16:1

# }

# Bước 2

# for key in count.keys():

# Thử mỗi số làm điểm bắt đầu.

# Ví dụ



# bắt đầu từ 2

# hoặc



# bắt đầu từ 4

# hoặc



# bắt đầu từ 16

# Sau đó lấy kết quả lớn nhất.

# Trường hợp đặc biệt của số 1

# if key == 1:

# Vì



# 1² = 1

# nên sẽ bị lặp vô hạn.

# Do đó phải xử lý riêng.

# Ví dụ



# 1 1 1 1 1

# Ta dùng được



# 1 1

# 1 1

# 1

# Độ dài



# 5

# Nếu có



# 1 1 1 1

# thì chỉ dùng được



# 1 1

# 1

# Độ dài



# 3

# Cho nên



# total = count[1] if count[1] % 2 else count[1]-1

# Nghĩa là

# Nếu số lượng là lẻ



# 5

# thì lấy luôn



# 5

# Nếu là chẵn



# 4

# thì phải bỏ đi một số



# 3

# để còn đúng dạng



# 2 + 2 + 1

# Các số khác

# total = 0

# Đếm chiều dài dãy.

# Vòng while

# while count[key] >= 2 and key*key in count:

# Ý nghĩa

# Muốn đi tiếp sang tầng tiếp theo thì cần



# Điều kiện 1

# count[key] >=2

# Tức là số hiện tại phải có ít nhất 2 bản.

# Ví dụ



# 2 2

# mới đủ.

# Điều kiện 2

# key*key in count

# Ví dụ



# 2²=4

# thì phải tồn tại số 4.

# Nếu không có 4 thì không đi tiếp được.

# Khi đủ điều kiện

# total +=2

# Ta dùng



# 2

# 2

# nên cộng thêm 2 phần tử.

# Sau đó



# key = key*key

# Chuyển sang xét



# 4

# rồi



# 16

# rồi



# 256

# ...

# Sau khi while kết thúc

# total+=1

# Vì tầng cuối chỉ cần



# 1

# phần tử.

# Ví dụ



# 2 2

# 4 4

# 16

# Ta có



# 2+2+1

# =



# 5

# Cập nhật đáp án

# res=max(res,total)

# Lấy kết quả lớn nhất trong tất cả các điểm bắt đầu.

# Ví dụ chạy

# nums



# 2 2 4 4 16

# Counter



# 2 : 2

# 4 : 2

# 16 : 1

# Bắt đầu từ



# key=2

# Lần 1



# count[2]=2



# 4 có tồn tại



# total=2

# key=4

# Lần 2



# count[4]=2



# 16 có



# total=4



# key=16

# Lần 3



# count[16]=1



# không đủ 2



# dừng

# Sau đó



# total+=1

# =



# 5

# Code có chú thích
from typing import List
from collections import Counter
class Solution:

    def maximumLength(self, nums: List[int]) -> int:

        # Đếm số lần xuất hiện của từng số

        count = Counter(nums)



        # Lưu kết quả lớn nhất

        res = 0



        # Thử mỗi giá trị làm điểm bắt đầu của chuỗi

        for key in count.keys():



            # Trường hợp đặc biệt: 1^2 = 1 nên phải xử lý riêng

            if key == 1:

                # Nếu số lượng 1 là lẻ thì dùng hết

                # Nếu chẵn thì bỏ 1 phần tử để kết thúc bằng đúng 1 số

                total = count[key] if count[key] % 2 else count[key] - 1



            else:

                # Độ dài chuỗi hiện tại

                total = 0



                # Muốn đi sang tầng tiếp theo cần:

                # 1. key xuất hiện ít nhất 2 lần

                # 2. key^2 tồn tại trong mảng

                while count[key] >= 2 and key * key in count:



                    # Dùng 2 phần tử của key

                    total += 2



                    # Sang tầng tiếp theo (bình phương)

                    key = key * key



                # Tầng cuối chỉ cần 1 phần tử

                total += 1



            # Cập nhật đáp án lớn nhất

            res = max(res, total)



        return res

# Độ phức tạp

# Time: O(n + m log log V) (thường được xem gần như O(n)), trong đó m là số lượng giá trị khác nhau và V là giá trị lớn nhất. Mỗi lần lặp while, key được bình phương (x → x² → x⁴ → ...), nên số bước tăng rất chậm.

# Space: O(m) để lưu bảng đếm tần suất (Counter).

# Mấu chốt của thuật toán là không duyệt mọi tập con, mà chỉ thử mỗi giá trị khác nhau làm điểm bắt đầu và lần theo chuỗi x → x² → x⁴ → ..., miễn là mỗi tầng (trừ tầng cuối) có ít nhất 2 phần tử để ghép.