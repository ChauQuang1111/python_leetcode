# Find Minimum in Rotated Sorted Array(15/05/2026)

# Bạn có một mảng ban đầu **được sắp xếp tăng dần**, nhưng sau đó bị **xoay (rotate)** vài lần.

# Ví dụ:

# ```text
# [0,1,2,4,5,6,7]
# ```

# xoay thành:

# ```text
# [4,5,6,7,0,1,2]
# ```

# Nhiệm vụ là:

# 👉 **Tìm phần tử nhỏ nhất trong mảng.**

# ---

# # Ví dụ

# ## Ví dụ 1

# Input:

# ```text
# nums = [3,4,5,1,2]
# ```

# Output:

# ```text
# 1
# ```

# Giải thích:

# * Mảng ban đầu có thể là:

# ```text
# [1,2,3,4,5]
# ```

# * Sau khi xoay:

# ```text
# [3,4,5,1,2]
# ```

# * Số nhỏ nhất là `1`.

# ---

# ## Ví dụ 2

# Input:

# ```text
# nums = [4,5,6,7,0,1,2]
# ```

# Output:

# ```text
# 0
# ```

# ---

# ## Ví dụ 3

# Input:

# ```text
# nums = [11,13,15,17]
# ```

# Output:

# ```text
# 11
# ```

# Giải thích:

# * Mảng chưa bị xoay.
# * Phần tử nhỏ nhất vẫn là phần tử đầu.

# ---

# # “Rotated Sorted Array” là gì?

# Ví dụ mảng tăng dần:

# ```text
# [1,2,3,4,5,6,7]
# ```

# Xoay 3 lần:

# ```text
# [5,6,7,1,2,3,4]
# ```

# Ta thấy:

# * Mảng vẫn gần như tăng dần
# * Nhưng có một “điểm gãy”
# * Sau điểm gãy chính là phần tử nhỏ nhất

# ---

# # Ý tưởng chính

# Ta cần tìm:

# ```text
# phần tử nhỏ nhất
# ```

# Quan sát:

# * Nửa bên trái hoặc bên phải luôn còn tính chất tăng dần
# * Có thể dùng **Binary Search**

# Độ phức tạp yêu cầu:

# ```text
# O(log n)
# ```

# nên không nên duyệt toàn bộ mảng.

# ---

# # Minh họa Binary Search

# Ví dụ:

# ```text
# [4,5,6,7,0,1,2]
# ```

# Ta lấy giữa:

# ```text
# mid = 7
# right = 2
# ```

# So sánh:

# ```text
# nums[mid] > nums[right]
# ```

# => phần nhỏ nhất nằm bên phải.

# ---

# Tiếp tục:

# ```text
# [0,1,2]
# ```

# Lấy giữa:

# ```text
# 1
# ```

# So sánh với `2`:

# ```text
# 1 < 2
# ```

# => phần nhỏ nhất nằm bên trái (bao gồm mid).

# Cuối cùng tìm được:

# ```text
# 0
# ```

# ---

# # Code Java

# ```java
# class Solution {
#     public int findMin(int[] nums) {
#         int left = 0;
#         int right = nums.length - 1;

#         while (left < right) {
#             int mid = left + (right - left) / 2;

#             if (nums[mid] > nums[right]) {
#                 left = mid + 1;
#             } else {
#                 right = mid;
#             }
#         }

#         return nums[left];
#     }
# }
# ```

# ---

# # Giải thích code

# ## Trường hợp 1

# ```java
# nums[mid] > nums[right]
# ```

# Ví dụ:

# ```text
# [4,5,6,7,0,1,2]
#         ^
# ```

# * `mid` nằm ở phần lớn
# * Minimum nằm bên phải

# Nên:

# ```java
# left = mid + 1;
# ```

# ---

# ## Trường hợp 2

# ```java
# nums[mid] <= nums[right]
# ```

# Ví dụ:

# ```text
# [0,1,2]
#  ^
# ```

# * Minimum nằm bên trái hoặc chính `mid`

# Nên:

# ```java
# right = mid;
# ```

# ---

# # Độ phức tạp

# * Time: `O(log n)`
# * Space: `O(1)`

# ---

# # Mấu chốt cần nhớ

# Ta luôn so sánh:

# ```text
# nums[mid] với nums[right]
# ```

# * Nếu `mid > right` → minimum ở bên phải
# * Ngược lại → minimum ở bên trái (kể cả mid)

# ---

# Ví dụ trực quan:

# ```text
# # [4,5,6,7,0,1,2]
# #          ^
# #         min
# # ```

# # Điểm gãy chính là nơi xuất hiện phần tử nhỏ nhất.
# Code của bạn dùng bisect_left theo cách khá “hack não” 😄

# Ý tưởng là dùng binary search để tìm vị trí đầu tiên thỏa điều kiện:

# n <= nums[-1]

# Tức là:



# Các phần tử bên trái điểm xoay sẽ lớn hơn nums[-1]

# Các phần tử từ minimum trở đi sẽ nhỏ hơn hoặc bằng nums[-1]

# Ví dụ:



# nums = [4,5,6,7,0,1,2]

# nums[-1] = 2

# Ta xét:



# 4 <= 2 -> False

# 5 <= 2 -> False

# 6 <= 2 -> False

# 7 <= 2 -> False

# 0 <= 2 -> True

# 1 <= 2 -> True

# 2 <= 2 -> True

# Ta có dãy:



# [False, False, False, False, True, True, True]

# 👉 Minimum nằm ở vị trí đầu tiên xuất hiện True.

# bisect_left(..., True) sẽ tìm vị trí đầu tiên của True.

# Code có chú thích

from bisect import bisect_left
from typing import List
class Solution:

    def findMin(self, nums: List[int]) -> int:

        

        # nums[-1] là phần tử cuối cùng

        # Ví dụ:

        # nums = [4,5,6,7,0,1,2]

        # nums[-1] = 2

        

        # Ta kiểm tra:

        # n <= nums[-1]

        #

        # Kết quả:

        # 4 <= 2 -> False

        # 5 <= 2 -> False

        # 6 <= 2 -> False

        # 7 <= 2 -> False

        # 0 <= 2 -> True

        # 1 <= 2 -> True

        # 2 <= 2 -> True

        #

        # => [False, False, False, True, True, True]

        

        # bisect_left tìm vị trí đầu tiên xuất hiện True

        # chính là vị trí của phần tử nhỏ nhất

        

        index = bisect_left(

            nums,                       # mảng cần tìm

            True,                       # giá trị cần tìm

            key=lambda n: n <= nums[-1]

        )



        return nums[index]

# Bản chất thuật toán

# Ta đang chia mảng thành 2 phần:

# Ví dụ:



# [4,5,6,7 | 0,1,2]

# Bên trái:

# > nums[-1]

# Bên phải:

# <= nums[-1]

# Minimum chính là phần tử đầu tiên thuộc nhóm thứ 2.

# Độ phức tạp

# Binary Search:



# Time: O(log n)

# Space: O(1)

# Lưu ý quan trọng

# Cách viết này dùng:



# bisect_left(..., key=...)

# chỉ có từ:



# Python 3.10+

# Nếu dùng Python cũ hơn sẽ bị lỗi.