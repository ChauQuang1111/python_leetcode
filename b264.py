# Bài Find a Safe Walk Through a Grid (02/07/2026)
# # Đề bài

# # Cho ma trận grid.



# # 0: ô an toàn.

# # 1: ô nguy hiểm, đi vào sẽ mất 1 máu.

# # Bắt đầu ở (0,0) với health.

# # Được đi 4 hướng.

# # Muốn đến (m-1,n-1).

# # # Trong suốt quá trình:

# # # health luôn phải > 0

# # # nếu đi vào ô nguy hiểm thì health giảm ngay.

# # # Hỏi có thể đến đích không.

# # # Ví dụ



# # grid =

# # 0 1 0

# # 0 1 0

# # 0 0 0



# # health = 2

# # Có đường:



# # ↓ ↓ → → 

# # Không đi qua ô nguy hiểm nên còn 2 máu.

# # Ý tưởng đầu tiên

# Ta nghĩ tới BFS.

# Mỗi trạng thái gồm



# (x, y, remainingHealth)

# Ví dụ



# (0,0,5)

# sang



# (0,1,4)

# nếu ô đó nguy hiểm.

# Nhưng có vấn đề

# Có thể đến cùng một ô với lượng máu khác nhau.

# Ví dụ



# A

# ↘

#  B

# ↗

# Có thể tới B



# health = 5

# hoặc



# health = 2

# Nếu chỉ đánh dấu



# visited[x][y]

# thì sai.

# Cách đúng

# Lưu



# best[x][y]

# = lượng máu lớn nhất từng tới ô đó.

# Ví dụ



# best[2][3]=6

# nghĩa là từng tới (2,3) với 6 máu.

# Nếu lần sau tới



# (2,3,4)

# thì bỏ.

# Vì



# 6 > 4

# Mọi đường từ đây đi tiếp thì 6 luôn tốt hơn 4.

# Nếu tới



# (2,3,8)

# thì cập nhật



# best=8

# và BFS tiếp.

# Vì sao đúng?

# Giả sử



# A

# đã tới với



# health = 7

# Sau này lại tới



# health = 5

# Từ A về sau mọi bước đều giống nhau.

# Nếu 5 đi được



# A -> ... -> End

# thì

# 7 cũng đi được.

# Nên trạng thái



# health = 5

# không bao giờ tốt hơn.

# Do đó chỉ giữ lượng máu lớn nhất.

# BFS

# Khởi tạo



# startHealth = health - grid[0][0]

# vì nếu ô đầu tiên nguy hiểm cũng mất máu.

# Nếu



# startHealth <=0

# trả về false.

# Đưa vào queue



# (0,0,startHealth)

# Lấy ra



# (x,y,h)

# Xét 4 hướng.



# newHealth = h - grid[nx][ny]

# Nếu



# newHealth<=0

# không đi.

# Nếu



# newHealth > best[nx][ny]

# thì



# best[nx][ny]=newHealth

# enqueue

# Minh họa

# Giả sử



# health = 4



# # 0 1 0

# # 0 1 1

# # 0 0 0

# # Ban đầu



# # best



# 4 - -

# - - -

# - - -

# Queue



# (0,0,4)

# Lấy ra



# (0,0,4)

# Đi xuống



# (1,0)



# newHealth=4

# Đi phải



# (0,1)



# newHealth=3

# Queue



# (1,0,4)

# (0,1,3)

# best



# 4 3 -

# 4 - -

# - - -

# Lấy



# (1,0,4)

# Đi xuống



# (2,0)



# 4

# Đi phải



# (1,1)



# # 3

# # Sau này nếu lại tới



# # (1,1)



# # health=2

# thì



# best=3

# nên bỏ.

# Không cần khám phá nữa.

# Độ phức tạp

# Giả sử



# m hàng

# n cột

# Mỗi ô chỉ được cập nhật khi tìm thấy lượng máu lớn hơn giá trị trước đó. Vì lượng máu chỉ giảm khi di chuyển và không thể vượt quá health, số lần cập nhật cho mỗi ô bị chặn bởi health.



# Thời gian: O(m × n × health) trong trường hợp xấu nhất.

# # Bộ nhớ: O(m × n) cho mảng best và O(m × n) cho hàng đợi.

# # Trong thực tế, số lần cập nhật thường ít hơn nhiều nên thuật toán chạy rất nhanh.

# # Code giả (Pseudo-code)

# # best[][] = -1



# # start = health - grid[0][0]



# if start <= 0

#     return false



# queue.push(0,0,start)

# best[0][0]=start



# while queue không rỗng



#     (x,y,h)=queue.pop()



#     if là đích

#         return true



#     for mỗi hướng



#         nx,ny



#         nếu ngoài lưới

#             continue



#         nh = h - grid[nx][ny]



#         if nh <= 0

#             continue



#         if nh > best[nx][ny]

#             best[nx][ny]=nh

#             queue.push(nx,ny,nh)



# return false

# Tại sao không cần dùng Dijkstra?

# Bài toán không yêu cầu tìm đường đi ngắn nhất hay chi phí nhỏ nhất, mà chỉ cần kiểm tra có tồn tại một đường đi hợp lệ hay không. Do đó, BFS kết hợp mảng best là đủ. Ý tưởng cốt lõi là ưu tiên giữ trạng thái có nhiều máu nhất tại mỗi ô; bất kỳ trạng thái nào đến cùng ô với ít máu hơn đều bị chi phối (dominated) và có thể loại bỏ an toàn. Đây chính là lý do thuật toán hoạt động hiệu quả mà không cần đến hàng đợi ưu tiên như Dijkstra.


# Code của bạn sử dụng ý tưởng 0-1 BFS (Zero-One BFS) thay vì BFS thông thường.

# Lý do là:



# Đi vào ô 0 → không mất máu (cost = 0)

# Đi vào ô 1 → mất 1 máu (cost = 1)

# Chi phí mỗi cạnh chỉ có 0 hoặc 1, nên có thể dùng 0-1 BFS để ưu tiên xử lý các cạnh có cost = 0 trước.

# Ý tưởng của thuật toán

# Bước 1. dist[i][j] lưu gì?

# Khác với Dijkstra thông thường lưu khoảng cách nhỏ nhất.

# Ở đây



# dist[i][j]

# lưu



# Lượng máu lớn nhất còn lại khi tới ô (i,j).

# Ví dụ



# dist



# 5 5 4

# 4 3 3

# 2 2 2

# nghĩa là



# tới (0,0) còn 5 máu

# tới (0,2) còn 4 máu

# Ta luôn muốn máu càng lớn càng tốt.

# Bước 2. Khởi tạo

# if grid[0][0] == 1:

#     dist[0][0] = health - 1

# else:

#     dist[0][0] = health

# Nếu ô đầu tiên nguy hiểm thì vừa đứng vào đã mất 1 máu.

# Ví dụ



# health = 3



# 1 0

# 0 0

# Bắt đầu



# dist[0][0] = 2

# Nếu



# dist<=0

# thì chết ngay.

# Bước 3. BFS

# Queue ban đầu



# [(0,0)]

# Lấy từng ô ra



# i,j = q.popleft()

# Bước 4. Xét 4 hướng

# for x,y in ...

# Ví dụ



# i,j



# ↓



# 0 1 0

# 0 X 0

# 0 0 0

# sẽ xét



# trên

# dưới

# trái

# phải

# Bước 5. Cost

# Nếu ô tiếp theo là



# 0

# thì



# cost = 0

# Nếu



# 1

# thì



# cost = 1

# Bước 6. Máu mới

# new_health = dist[i][j] - cost

# Ví dụ



# dist = 5

# đi sang



# 1

# thì



# new_health = 4

# Bước 7. Tại sao phải so sánh

# new_health > dist[x][y]

# Ví dụ

# Đã từng đến



# (2,3)

# với



# dist = 4

# Lần sau lại tới



# dist = 2

# thì bỏ.

# Vì



# 4 > 2

# Có nhiều máu hơn luôn tốt hơn.

# Bước 8. 0-1 BFS

# Đây là phần quan trọng nhất.



# if cost == 0:

#     q.appendleft(...)

# else:

#     q.append(...)

# Giả sử queue là



# A B C

# Nếu cạnh có cost = 0



# appendleft

# thì



# X A B C

# X được xử lý ngay.

# Nếu cost = 1



# append

# thì



# A B C X

# Để xử lý sau.

# Đây chính là nguyên lý của 0-1 BFS.

# Ví dụ

# 0 0 1

# 1 0 0

# Queue



# [(0,0)]

# Từ (0,0)

# đi phải



# cost = 0

# đi xuống



# cost = 1

# Queue trở thành



# [(0,1),(1,0)]

# Ta ưu tiên đường không mất máu trước.

# Tại sao nhanh?

# Thông thường nếu dùng Dijkstra



# Priority Queue



# O(E logV)

# Nhưng vì chỉ có



# cost = 0

# hoặc

# cost = 1

# nên deque đủ để thay Priority Queue.

# Độ phức tạp



# O(m × n)

# Code có chú thích

from collections import deque
from typing import List
class Solution:

    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:



        m = len(grid)

        n = len(grid[0])



        # dist[i][j] = lượng máu lớn nhất còn lại khi đến ô (i, j)

        # -2 nghĩa là chưa từng đến ô này

        dist = [[-2] * n for _ in range(m)]



        # Hàng đợi của thuật toán 0-1 BFS

        q = deque([(0, 0)])



        # Nếu ô bắt đầu là ô nguy hiểm thì mất 1 máu ngay

        if grid[0][0] == 1:

            dist[0][0] = health - 1



            # Chết ngay khi vừa bắt đầu

            if dist[0][0] <= 0:

                return False

        else:

            dist[0][0] = health



        while q:



            # Lấy ô ở đầu hàng đợi

            i, j = q.popleft()



            # Đến đích thì thành công

            if i == m - 1 and j == n - 1:

                return True



            # Xét 4 ô kề

            for x, y in (

                (i - 1, j),

                (i + 1, j),

                (i, j - 1),

                (i, j + 1)

            ):



                # Kiểm tra còn nằm trong lưới

                if 0 <= x < m and 0 <= y < n and dist[x][y] == -2:



                    # Cost khi đi vào ô mới

                    # Ô nguy hiểm mất 1 máu, ô an toàn không mất máu

                    cost = 1 if grid[x][y] == 1 else 0



                    # Máu còn lại sau khi bước vào ô mới

                    new_health = dist[i][j] - cost



                    # Chỉ đi tiếp nếu vẫn còn sống

                    if new_health > 0 and new_health > dist[x][y]:



                        # Cập nhật lượng máu tốt nhất tại ô mới

                        dist[x][y] = new_health



                        # ===== 0-1 BFS =====

                        # Cost = 0: đưa lên đầu deque để xử lý trước

                        if cost == 0:

                            q.appendleft((x, y))

                        # Cost = 1: đưa xuống cuối deque

                        else:

                            q.append((x, y))



        # Không thể đi tới đích

        return False

# Lưu ý quan trọng

# Đoạn code này hoạt động vì sử dụng 0-1 BFS, nhưng điều kiện:



# and dist[x][y] == -2

# có nghĩa là mỗi ô chỉ được thăm đúng một lần. Cách này đúng khi thứ tự xử lý của 0-1 BFS đảm bảo lần đầu đến một ô cũng là trạng thái tốt nhất (nhiều máu nhất). Nếu bỏ tính chất này hoặc dùng BFS thông thường thì có thể cần cho phép cập nhật lại một ô khi tìm được đường đến với nhiều máu hơn. Trong nhiều lời giải, điều kiện này được thay bằng:



# if new_health > dist[x][y]:

#     dist[x][y] = new_health

#     ...

# để đảm bảo không bỏ lỡ một trạng thái tốt hơn đến cùng một ô.