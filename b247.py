# Minimum Element After Replacement With Digit Sum(29/05/2026)

# Đề bài

# Cho một mảng số nguyên nums.

# Với mỗi phần tử trong mảng:



# thay số đó bằng tổng các chữ số của nó.

# Sau khi thay hết:



# tìm phần tử nhỏ nhất trong mảng mới.

# Ví dụ

# Ví dụ 1

# Input:



# nums = [10,12,13,14]

# Bước thay thế

# 10 → 1 + 0 = 1

# 12 → 1 + 2 = 3

# 13 → 1 + 3 = 4

# 14 → 1 + 4 = 5

# Mảng mới:



# [1,3,4,5]

# Phần tử nhỏ nhất:



# 1

# Output:



# 1

# “Digit Sum” là gì?

# Là tổng các chữ số của một số.

# Ví dụ:



# 456 → 4 + 5 + 6 = 15

# 98 → 9 + 8 = 17

# Nhiệm vụ của bài

# Với mỗi số:



# tách từng chữ số

# cộng các chữ số lại

# cập nhật số đó thành tổng vừa tính

# cuối cùng tìm số nhỏ nhất

# Cách tách chữ số

# Ví dụ số 538

# Ta làm:



# 538 % 10 = 8

# 538 / 10 = 53



# 53 % 10 = 3

# 53 / 10 = 5



# 5 % 10 = 5

# Tổng:



# 8 + 3 + 5 = 16

# Ý tưởng thuật toán

# min = rất lớn



# duyệt từng số trong nums:

#     tính tổng chữ số

#     cập nhật min



# trả về min

# Code Java đơn giản

# class Solution {

#     public int minElement(int[] nums) {

#         int min = Integer.MAX_VALUE;



#         for (int num : nums) {

#             int sum = 0;



#             while (num > 0) {

#                 sum += num % 10;

#                 num /= 10;

#             }



#             min = Math.min(min, sum);

#         }



#         return min;

#     }

# }

# Độ phức tạp

# n phần tử

# mỗi số có tối đa k chữ số

# Độ phức tạp:



# O(n * k)
from typing import List
class Solution:
    def minElement(self, nums: List[int]) -> int:



        # Khởi tạo giá trị nhỏ nhất ban đầu là vô cùng

        min_res = float('inf')



        # Duyệt từng số trong mảng

        for n in nums:



            # cur dùng để lưu tổng các chữ số của n

            cur = 0



            # Tách từng chữ số của n

            while n:



                # Lấy chữ số cuối cùng

                # Ví dụ: 538 % 10 = 8

                cur += n % 10



                # Xóa chữ số cuối cùng

                # Ví dụ: 538 // 10 = 53

                n //= 10



            # Cập nhật giá trị nhỏ nhất

            min_res = min(min_res, cur)



        # Trả về kết quả cuối cùng

        return min_res

# Giải thích thuật toán

# Ví dụ:



# nums = [10, 25, 38]

# Bước 1: xử lý số 10

# n = 10

# cur = 0

# Vòng lặp while

# Lần 1:



# 10 % 10 = 0

# cur = 0 + 0 = 0



# 10 // 10 = 1

# Lần 2:



# 1 % 10 = 1

# cur = 0 + 1 = 1



# 1 // 10 = 0

# Kết thúc:



# cur = 1

# Cập nhật:



# min_res = 1

# Bước 2: xử lý số 25

# 2 + 5 = 7

# min(1, 7) = 1

# Bước 3: xử lý số 38

# 3 + 8 = 11

# min(1, 11) = 1

# Kết quả

# return 1

# Ý tưởng chính

# Mỗi số:



# dùng % 10 để lấy chữ số cuối

# dùng // 10 để bỏ chữ số cuối

# cộng các chữ số lại

# tìm giá trị nhỏ nhất trong các tổng chữ số

# Độ phức tạp

# Giả sử:



# có n phần tử

# mỗi số có tối đa k chữ số

# Thì:



# Time Complexity: O(n * k)

# Space Complexity: O(1)