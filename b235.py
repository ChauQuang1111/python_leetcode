# Bài **Jump Game III** trên LeetCode yêu cầu như sau:

# ## Đề bài

# Cho một mảng số nguyên không âm `arr`.

# Bạn đứng ở vị trí `start`.

# Từ vị trí `i`, bạn có thể nhảy tới:

# * `i + arr[i]`
# * hoặc `i - arr[i]`

# Miễn là vị trí mới vẫn nằm trong mảng.

# Nhiệm vụ:
# Kiểm tra xem có thể đi tới **một ô có giá trị bằng 0** hay không.

# Trả về:

# * `true` nếu tới được số `0`
# * `false` nếu không thể

# ---

# ## Ví dụ 1

# ```text
# arr = [4,2,3,0,3,1,2]
# start = 5
# ```

# ### Di chuyển

# Đang ở index `5`

# ```text
# arr[5] = 1
# ```

# Có thể đi:

# * `5 + 1 = 6`
# * `5 - 1 = 4`

# Ví dụ đường đi:

# ```text
# 5 -> 4 -> 1 -> 3
# ```

# Giá trị tại index `3` là:

# ```text
# arr[3] = 0
# ```

# => Kết quả `true`

# ---

# ## Ví dụ 2

# ```text
# arr = [4,2,3,0,3,1,2]
# start = 0
# ```

# Đi được:

# ```text
# 0 -> 4 -> 1 -> 3
# ```

# Tới số `0`

# => `true`

# ---

# ## Ví dụ 3

# ```text
# arr = [3,0,2,1,2]
# start = 2
# ```

# Từ index `2`:

# ```text
# 2 + arr[2] = 4
# 2 - arr[2] = 0
# ```

# Nhưng sau đó sẽ bị lặp và không tới được index có giá trị `0`.

# => `false`

# ---

# # Ý tưởng bài này

# Đây là bài:

# * DFS
# * hoặc BFS
# * Graph traversal

# Mỗi index được xem như một node.

# Từ một node có tối đa 2 cạnh:

# ```text
# i + arr[i]
# i - arr[i]
# ```

# ---

# # Điều quan trọng nhất

# Phải có mảng `visited`

# Vì có thể bị lặp vô hạn.

# Ví dụ:

# ```text
# 1 -> 3 -> 1 -> 3 ...
# ```

# ---

# # Khi nào dừng?

# ## Thành công

# Nếu:

# ```text
# arr[i] == 0
# ```

# => return `true`

# ---

# ## Thất bại

# Nếu:

# * index ra ngoài mảng
# * hoặc đã thăm rồi

# => return `false`

# ---

# # Minh họa

# Ví dụ:

# ```text
# arr = [4,2,3,0,3,1,2]
# start = 5
# ```

# Sơ đồ:

# ```text
# 5
# ├── 6
# └── 4
#      ├── 1
#      │    ├── 3 (0) ✅
# ```

# ---

# # Độ phức tạp

# * Mỗi index thăm tối đa 1 lần

# Time:

# ```text
# O(n)
# ```

# Space:

# ```text
# O(n)
# ```

# ---

# # DFS Concept

# Có thể hình dung như:

# ```text
# canReach(i):
#     nếu arr[i] == 0:
#         return true

#     visited[i] = true

#     thử đi trái
#     thử đi phải
# ```

# ---

# # Chủ đề liên quan

# * Graph
# * DFS
# * BFS
# * Recursion
# * Visited array
# Code của bạn dùng thuật toán BFS (Breadth First Search) để kiểm tra xem có đi tới ô chứa 0 hay không.

# Mình sẽ thêm chú thích từng dòng và giải thích thuật toán chi tiết.

from collections import deque
from typing import List
class Solution:

    def canReach(self, arr: List[int], start: int) -> bool: 
        # Số phần tử của mảng

        n = len(arr)



        # Queue dùng cho BFS

        # Ban đầu đưa vị trí start vào queue

        q = deque([start])



        # Mảng đánh dấu đã thăm

        # Tránh lặp vô hạn

        visited = [False] * n



        # Đánh dấu start đã được thăm

        visited[start] = True



        # BFS

        while q:

            # Lấy phần tử đầu queue

            node = q.popleft()

            # Nếu tới ô có giá trị 0

            # => thành công

            if arr[node] == 0:

                return True

            # Tính vị trí có thể nhảy sang trái và phải

            left = node - arr[node]

            right = node + arr[node]

            # Nếu vị trí left hợp lệ

            # và chưa được thăm

            if left >= 0 and not visited[left]:

                # Đưa vào queue để tiếp tục BFS

                q.append(left)

                # Đánh dấu đã thăm

                visited[left] = True

            # Nếu vị trí right hợp lệ

            # và chưa được thăm

            if right < n and not visited[right]:

                # Đưa vào queue

                q.append(right)

                # Đánh dấu đã thăm

                visited[right] = True

        # Nếu BFS kết thúc mà không gặp số 0

        return False

# Ý tưởng thuật toán

# Mỗi index là một node.

# Từ node i:

# Có thể đi:



# i - arr[i]

# i + arr[i]

# => Đây giống bài graph traversal.

# BFS hoạt động như thế nào?

# Ví dụ:



# arr = [4,2,3,0,3,1,2]

# start = 5

# Bước 1

# Queue:



# [5]

# Bước 2

# Lấy 5



# arr[5] = 1

# Đi được:



# 5 - 1 = 4

# 5 + 1 = 6

# Queue:



# [4, 6]

# Bước 3

# Lấy 4



# arr[4] = 3

# Đi được:



# 4 - 3 = 1

# 4 + 3 = 7 (invalid)

# Queue:



# [6, 1]

# Bước 4

# Lấy 1



# arr[1] = 2

# Đi được:



# 1 - 2 = -1 (invalid)

# 1 + 2 = 3

# Queue:



# [3]

# Bước 5

# Lấy 3



# arr[3] = 0

# => return True

# Vì sao cần visited?

# Ví dụ:



# 1 -> 3 -> 1 -> 3 ...

# Nếu không có visited:



# chương trình sẽ chạy vô hạn

# Độ phức tạp

# Time Complexity

# Mỗi node thăm tối đa 1 lần:



# O(n)

# Space Complexity

# Queue + visited:



# O(n)

# BFS vs DFS

# Bài này dùng:



# BFS ✅

# DFS ✅

# đều được.

# Code BFS của bạn rất chuẩn và tối ưu rồi.