# # Đề bài: Minimum Initial Energy to Finish Tasks(12/05/2026)
# ```python
from typing import List
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:

        # Sắp xếp theo:
        # minimum - actual
        # Task nào cần "dự trữ energy" nhiều hơn sẽ ưu tiên làm trước
        tasks.sort(key=lambda x: x[1] - x[0])

        # ans = lượng energy nhỏ nhất cần có
        ans = 0

        # Duyệt từng task
        for task in tasks:

            # task[0] = actual
            # năng lượng thực sự bị mất
            actual = task[0]

            # task[1] = minimum
            # năng lượng tối thiểu cần có để bắt đầu
            minimum = task[1]

            # Có 2 trường hợp:
            #
            # 1. ans + actual
            #    -> energy cần để sau khi làm task
            #       vẫn đủ cho các task trước đó
            #
            # 2. minimum
            #    -> phải đủ điều kiện bắt đầu task hiện tại
            #
            # Lấy giá trị lớn hơn
            ans = max(ans + actual, minimum)

        return ans
# ```

# # Giải thích ý tưởng

# Ta đi ngược.

# ---

## Ý nghĩa của `ans`

# ```python
# ans
# ```

# không phải energy hiện tại,

# mà là:

# ```text
# energy nhỏ nhất cần có
# để hoàn thành các task đã xét
# ```

# ---

# # Ví dụ

# ```python
# tasks = [[1,2],[2,4],[4,8]]
# ```

# Sau sort:

# ```python
# [[1,2],[2,4],[4,8]]
# ```

# ---

# # Task [1,2]

# ```python
# ans = max(0 + 1, 2)
# ```

# ```python
# ans = 2
# ```

# Cần ít nhất 2 để bắt đầu.

# ---

# # Task [2,4]

# ```python
# ans = max(2 + 2, 4)
# ```

# ```python
# ans = 4
# ```

# ---

# # Task [4,8]

# ```python
# ans = max(4 + 4, 8)
# ```

# ```python
# ans = 8
# ```

# ---

# # Kết quả

# ```python
# 8
# ```

# ---

# # Công thức quan trọng

# ```python
# ans = max(ans + actual, minimum)
# ```

# Ý nghĩa:

# Ta cần đủ energy để:

# 1. Bắt đầu task hiện tại (`minimum`)
# 2. Sau khi mất `actual`, vẫn còn đủ cho các task sau (`ans + actual`)

# Bạn có nhiều task.

# Mỗi task gồm 2 số:

# ```java
# [a, m]
# ```

# Trong đó:

# * `a` = năng lượng thực sự bị mất sau khi làm task
# * `m` = năng lượng tối thiểu cần có để bắt đầu task

# ---

# # Ví dụ

# ```java
# [2, 5]
# ```

# Nghĩa là:

# * Muốn làm task này, bạn phải có ít nhất `5 energy`
# * Sau khi làm xong, energy giảm `2`

# ---

# # Yêu cầu bài toán

# Tìm:

# ```text
# Lượng energy ban đầu nhỏ nhất
# ```

# để có thể hoàn thành tất cả task.

# ---

# # Ví dụ 1

# ```java
# tasks = [[1,2],[2,4],[4,8]]
# ```

# ---

# ## Bắt đầu với 8 energy

# ### Task [4,8]

# * có 8 → đủ làm
# * làm xong còn:

# ```text
# 8 - 4 = 4
# ```

# ---

# ### Task [2,4]

# * có 4 → đủ
# * làm xong còn:

# ```text
# 4 - 2 = 2
# ```

# ---

# ### Task [1,2]

# * có 2 → đủ
# * làm xong còn:

# ```text
# 2 - 1 = 1
# ```

# => hoàn thành hết.

# ---

# # Nếu bắt đầu với 7?

# Task đầu cần 8.

# => thất bại ngay.

# ---

# # Mục tiêu chính

# Không phải:

# ```text
# energy còn lại lớn nhất
# ```

# Mà là:

# ```text
# energy ban đầu nhỏ nhất
# ```

# ---

# # Ý tưởng khó của bài

# Thứ tự làm task rất quan trọng.

# Ví dụ:

# ```java
# [1,10]
# ```

# Task này:

# * cần tới 10 energy để bắt đầu
# * nhưng chỉ mất 1

# => nên làm sớm.

# ---

# # Vì vậy solution sẽ:

# Sắp xếp task theo:

# ```text
# minimum - actual
# ```

# Task nào “khó bắt đầu” hơn sẽ làm trước.
