# Bài **“Check if Array is Good (14/05/2026)

# ```python
from typing import List
class Solution:
    def isGood(self, nums: List[int]) -> bool:

        # Sắp xếp mảng tăng dần
        nums.sort()

        # Lấy phần tử lớn nhất trong mảng
        # Vì sau khi sort, phần tử cuối cùng là lớn nhất
        max_ele = nums[-1]

        # Kiểm tra điều kiện của mảng good
        #
        # Điều kiện 1:
        # độ dài mảng phải = max_ele + 1
        #
        # Ví dụ:
        # [1,2,3,3]
        # max = 3
        # length = 4
        # => đúng vì 4 = 3 + 1
        #
        # Điều kiện 2:
        # số lớn nhất phải xuất hiện 2 lần
        # nên 2 phần tử cuối phải bằng nhau
        #
        # nums[-1]     : phần tử cuối
        # nums[-1 - 1] : phần tử kế cuối
        #
        if len(nums) != max_ele + 1 or nums[-1] != nums[-2]:
            return False

        # Kiểm tra các số từ 1 -> max_ele - 1
        #
        # Ví dụ:
        # [1,2,3,3]
        #
        # cần kiểm tra:
        # nums[0] = 1
        # nums[1] = 2
        #
        # vì số lớn nhất (3) đã được kiểm tra ở trên
        #
        for i in range(max_ele - 1):

            # Sau khi sort:
            # vị trí i phải chứa số i + 1
            #
            # i = 0 -> cần số 1
            # i = 1 -> cần số 2
            # ...
            #
            if nums[i] != i + 1:
                return False

        # Nếu vượt qua tất cả kiểm tra
        # => đây là mảng good
        return True
# ```

# ## Ý tưởng thuật toán

# Sau khi sort, mảng good luôn có dạng:

# ```text id="x0s3nm"
# [1,2,3,...,n-1,n-1]
# ```

# Ví dụ:

# ```text id="5l1sww"
# [1,2,3,3]
# [1,2,2]
# [1,1]
# ```

# Thuật toán kiểm tra:

# 1. Phần tử lớn nhất có xuất hiện 2 lần không
# 2. Các số trước đó có đúng thứ tự `1 -> max-1` không

# Nếu sai bất kỳ chỗ nào ⇒ không phải good array.

# ## Ý tưởng của đề

# Cho một mảng `nums`.

# Mảng được gọi là **good** nếu:

# * Nó chứa tất cả các số từ `1` đến `n - 1` đúng **1 lần**
# * Và số `n - 1` xuất hiện đúng **2 lần**

# Trong đó:

# * `n = nums.length`

# ---

# ## Ví dụ

# ### Ví dụ 1

# ```text
# nums = [1,2,3,3]
# ```

# * Độ dài mảng = 4
# * Vậy cần có:

# ```text
# 1,2,3
# ```

# Trong đó số lớn nhất `3` phải xuất hiện **2 lần**

# Mảng hiện tại:

# ```text
# 1 xuất hiện 1 lần
# 2 xuất hiện 1 lần
# 3 xuất hiện 2 lần
# ```

# => Đây là mảng good.

# ---

# ### Ví dụ 2

# ```text
# nums = [1,1]
# ```

# * Độ dài = 2
# * Cần:

# ```text
# 1 xuất hiện 2 lần
# ```

# Mảng đúng yêu cầu.

# => good.

# ---

# ### Ví dụ 3

# ```text
# nums = [1,2,2,4]
# ```

# * Độ dài = 4
# * Cần:

# ```text
# 1,2,3
# ```

# và `3` phải xuất hiện 2 lần.

# Nhưng mảng lại có `4`.

# => không good.

# ---

# # Quy luật tổng quát

# Nếu mảng có độ dài `n`:

# Thì sau khi sort phải thành:

# ```text
# [1, 2, 3, ..., n-1, n-1]
# ```

# ---

# # Cách làm đơn giản

# ## Bước 1

# Sort mảng.

# ## Bước 2

# Kiểm tra:

# * `nums[i] == i + 1` với mọi `i < n-1`
# * phần tử cuối cùng phải bằng `n-1`

# ---

# # Java Code

# ```java
# class Solution {
#     public boolean isGood(int[] nums) {
#         Arrays.sort(nums);

#         int n = nums.length;

#         for (int i = 0; i < n - 1; i++) {
#             if (nums[i] != i + 1) {
#                 return false;
#             }
#         }

#         return nums[n - 1] == n - 1;
#     }
# }
# ```

# ---

# # Vì sao code đúng?

# Ví dụ:

# ```text
# [1,2,3,3]
# ```

# Sau sort:

# ```text
# [1,2,3,3]
# ```

# Loop kiểm tra:

# ```text
# nums[0] = 1
# nums[1] = 2
# nums[2] = 3
# ```

# đều đúng với `i + 1`.

# Sau đó kiểm tra:

# ```text
# nums[3] == 3
# ```

# => true.

# ---

# # Độ phức tạp

# * Sort: `O(n log n)`
# * Kiểm tra: `O(n)`

# Tổng:

# ```text
# O(n log n)
# ```
