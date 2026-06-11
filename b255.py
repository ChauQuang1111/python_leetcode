# Tóm tắt đề bài

# Cho một cây (tree) gồm n đỉnh, gốc là đỉnh 1.

# Mỗi cạnh ban đầu có trọng số 0, sau đó bạn phải gán cho mỗi cạnh một trọng số là 1 hoặc 2.

# Chi phí của một đường đi = tổng trọng số các cạnh trên đường đi đó. (LeetCode)

# Yêu cầu

# Tìm một đỉnh x nằm ở độ sâu lớn nhất (maximum depth).

# Chỉ xét đường đi từ gốc 1 → x.

# Đếm xem có bao nhiêu cách gán trọng số 1 hoặc 2 cho các cạnh trên đường đi này sao cho:

# [

# \text{Tổng trọng số trên đường đi là số lẻ}

# ]

# Các cạnh không nằm trên đường đi này không cần quan tâm. (LeetCode)

# Ví dụ 1

# edges = [[1,2]]

# Cây:



# 1

# |

# 2

# Đường đi 1 → 2 có 1 cạnh.

# Các cách gán:



# 1  => tổng = 1 (lẻ)   ✓

# 2  => tổng = 2 (chẵn) ✗

# => Có 1 cách.

# Kết quả:



# 1

# Ví dụ 2

# edges = [[1,2],[1,3],[3,4],[3,5]]

# Cây:



#     1

#    / \

#   2   3

#      / \

#     4   5

# Độ sâu lớn nhất là 2, các đỉnh 4 và 5 đều đạt độ sâu này.

# Chọn đường đi:



# 1 -> 3 -> 4

# Có 2 cạnh.

# Các cách gán:



# (1,1) => 2  (chẵn)

# (1,2) => 3  (lẻ)   ✓

# (2,1) => 3  (lẻ)   ✓

# (2,2) => 4  (chẵn)

# => Có 2 cách. (LeetCode)

# Ý tưởng quan trọng của bài

# Giả sử đường đi từ gốc đến đỉnh sâu nhất có d cạnh.

# Mỗi cạnh chỉ có thể là:



# 1 (số lẻ)

# 2 (số chẵn)

# Tổng cuối cùng là lẻ khi và chỉ khi số lượng cạnh mang trọng số 1 là lẻ. (LeetCode)

# Ví dụ:



# 1 + 2 + 2 = 5  (lẻ)

# 1 + 1 + 1 = 3  (lẻ)

# Đều có số lượng số 1 là lẻ.

# Bài toán thực chất trở thành

# Tìm độ sâu lớn nhất d.

# Đường đi có d cạnh.

# Mỗi cạnh có 2 lựa chọn (1 hoặc 2).

# Tổng số cách gán:

# [

# 2^d

# ]

# Một nửa trong số đó cho tổng lẻ, một nửa cho tổng chẵn.

# Do đó đáp án là:

# [

# 2^{d-1}

# ]

# (sau đó lấy modulo (10^9+7)). (LeetCode)

# Cần làm gì trong code?

# Dùng DFS/BFS tìm maximum depth của cây.

# Gọi độ sâu lớn nhất là d.

# Trả về:

# [

# 2^{d-1} \bmod (10^9+7)

# ]

# Dưới đây là code của bạn với chú thích chi tiết hơn:


from typing import List
from collections import deque
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        # Số đỉnh của cây = số cạnh + 1
        n = len(edges) + 1



        # Danh sách kề

        g = [[] for _ in range(n + 1)]



        # Xây dựng cây

        # Đề bài đảm bảo parent < child

        # nên chỉ lưu cạnh từ cha -> con

        for u, v in edges:

            if u < v:

                g[u].append(v)

            else:

                g[v].append(u)



        # d[i] = độ sâu của đỉnh i

        # -1 nghĩa là chưa được thăm

        d = [-1] * (n + 1)



        # Gốc là đỉnh 1 nên depth = 0

        d[1] = 0



        # BFS bắt đầu từ node 1

        q = deque([1])



        while q:

            # Lấy đỉnh đầu hàng đợi

            u = q.popleft()



            # Duyệt các con của u

            for v in g[u]:



                # Nếu chưa tính độ sâu

                if d[v] < 0:



                    # Độ sâu của con = độ sâu cha + 1

                    d[v] = d[u] + 1



                    # Đưa vào queue để tiếp tục BFS

                    q.append(v)



        # Tìm độ sâu lớn nhất trong cây

        m = max(d[1:])



        MOD = 10**9 + 7



        # Đường đi từ gốc đến node sâu nhất có m cạnh

        #

        # Mỗi cạnh có 2 cách gán trọng số:

        #   1 hoặc 2

        #

        # Tổng số cách gán = 2^m

        #

        # Một nửa số cách cho tổng lẻ,

        # một nửa cho tổng chẵn

        #

        # => số cách hợp lệ = 2^(m-1)

        return pow(2, m - 1, MOD)

# Ví dụ

# edges = [[1,2],[1,3],[3,4],[3,5]]

# Cây:



#     1

#    / \

#   2   3

#      / \

#     4   5

# BFS tính được:



# d[1] = 0

# d[2] = 1

# d[3] = 1

# d[4] = 2

# d[5] = 2

# m = 2

# Đường đi dài nhất có 2 cạnh.

# Mỗi cạnh có 2 lựa chọn:



# 2^2 = 4 cách

# Trong 4 cách đó:



# (1,1) -> chẵn

# (1,2) -> lẻ

# (2,1) -> lẻ

# (2,2) -> chẵn

# Có đúng:



# 2^(2-1) = 2

# cách cho tổng trọng số là số lẻ.



# Độ phức tạp

# Xây cây: O(n)

# BFS: O(n)

# Tìm max depth: O(n)

# Tổng:



# Time:  O(n)

# Space: O(n)