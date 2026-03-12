# ## Maximize Spanning Tree Stability with Upgrades (12/03/2026)

# Mình sẽ **giải thích thuật toán + thêm chú thích trực tiếp vào code** để bạn hiểu từng bước.
# Bài này dùng **Disjoint Set Union (Union-Find) + Greedy kiểu Kruskal**.

# Ý tưởng chính:

# 1. Một số cạnh **bắt buộc phải dùng** (`edge[3] = True`)
# 2. Nếu các cạnh bắt buộc **tạo chu trình → không thể tạo spanning tree → return -1**
# 3. Sau đó dùng **các cạnh optional** để nối các component còn lại (giống Kruskal)
# 4. Chọn cạnh **stability lớn trước**
# 5. Khi đã tạo được spanning tree → **upgrade k cạnh có stability nhỏ nhất**
# 6. Kết quả của bài là **stability nhỏ nhất trong tree** (vì tree stability = bottleneck edge)

# ---

# # Code đã thêm chú thích chi tiết

# ```python
from typing import List
class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:

        # DSU initialization
        parent = list(range(n))
        size = [1] * n

        # find root của node v (path compression)
        def find_set(v):
            if parent[v] == v:
                return v
            parent[v] = find_set(parent[v])
            return parent[v]
        
        # union 2 tập hợp
        def union_sets(a, b):
            a = find_set(a)
            b = find_set(b)

            if a != b:
                # union by size
                if size[a] < size[b]:
                    a, b = b, a
                parent[b] = a
                size[a] += size[b]
                return True  # union thành công
            else:
                return False  # đã cùng 1 component

        # kiểm tra hai node có cùng component không
        def same_set(a, b):
            a = find_set(a)
            b = find_set(b)
            return a != b
        
        components = n

        # stability nhỏ nhất của các cạnh bắt buộc
        min_stability = float("inf")
        
        optional = []

        # duyệt toàn bộ edges
        for index, edge in enumerate(edges):

            if edge[3]:  
                # edge bắt buộc phải dùng

                if union_sets(edge[0], edge[1]):
                    # nối thành công
                    components -= 1

                    # cập nhật stability nhỏ nhất
                    min_stability = min(min_stability, edge[2])

                else:
                    # nếu union fail -> tạo cycle
                    # nghĩa là các cạnh bắt buộc tạo chu trình
                    return -1

            else:
                # edge optional
                optional.append(index)

        # nếu các cạnh bắt buộc đã tạo thành spanning tree
        if components == 1:
            return min_stability

        # sort optional edges theo stability giảm dần
        optional.sort(key=lambda x: edges[x][2], reverse=True)

        stabilities = []

        # giống thuật toán Kruskal
        for index in optional:

            edge = edges[index]

            if union_sets(edge[0], edge[1]):

                # cạnh được thêm vào tree
                components -= 1
                stabilities.append(edge[2])

                if components == 1:
                    break

        # nếu vẫn chưa connect hết graph
        if components > 1:
            return -1

        # upgrade k cạnh có stability nhỏ nhất
        for i in range(1, min(len(stabilities), k) + 1):
            stabilities[-i] *= 2

        # stability của tree = cạnh yếu nhất
        return min(min(stabilities), min_stability)
# ```

# ---

# # Tóm tắt thuật toán

# ### Bước 1 — DSU

# Dùng **Union Find** để xây spanning tree.

# ---

# ### Bước 2 — Thêm cạnh bắt buộc

# ```
# edge[3] = True
# ```

# → phải dùng

# Nếu tạo **cycle → return -1**

# ---

# ### Bước 3 — Thêm cạnh optional

# Sort theo:

# ```
# stability giảm dần
# ```

# giống **Maximum Spanning Tree (Kruskal)**

# ---

### Bước 4 — Khi đủ n-1 cạnh

# Ta có **spanning tree**

# ---

# ### Bước 5 — Upgrade k cạnh yếu nhất

# ```
# stabilities[-i] *= 2
# ```

# vì list đang **giảm dần**

# → cuối list = nhỏ nhất

# ---

# ### Bước 6 — Kết quả

# Stability của cây =

# ```
# min(edge weight trong tree)
# ```

# vì **bottleneck edge quyết định stability**

# ---

# # Độ phức tạp

# Time complexity:

# ```
# Sort edges: O(E log E)

# Union Find: O(E α(N))
# ```

# → Tổng:

# ```
# O(E log E)
# ```

# ---

# 💡 Nếu bạn muốn mình có thể giải thích thêm **3 phần quan trọng giúp bạn hiểu sâu bài này**:

# 1️⃣ **Tại sao kết quả là cạnh nhỏ nhất của tree**
# 2️⃣ **Vì sao phải sort giảm dần (Maximum Spanning Tree)**
# 3️⃣ **Vì sao upgrade cạnh nhỏ nhất là tối ưu**

# Ba ý này là **trick chính của bài**.


# Bài này thường thuộc dạng **graph + spanning tree + tối ưu hóa**. Mình sẽ giải thích từng phần để bạn hiểu rõ.

# ---

# ## 1. Bối cảnh bài toán

# Bạn có một **mạng lưới gồm các thành phố / máy chủ / điểm** được nối với nhau bằng các **đường (edges)**.

# * Có **N đỉnh (nodes)**
# * Có **M cạnh (edges)**

# Mỗi cạnh có một giá trị gọi là:

# 👉 **stability (độ ổn định)**

# Giá trị này thể hiện **độ tốt / độ mạnh của kết nối**.

# ---

# ## 2. Spanning Tree là gì?

# **Spanning Tree** là một tập cạnh thỏa:

# * Kết nối **tất cả N đỉnh**
# * **Không có chu trình**
# * Có đúng **N − 1 cạnh**

# Ví dụ mạng 5 đỉnh → spanning tree sẽ có **4 cạnh**.

# ---

# ## 3. Maximum Spanning Tree

# Thông thường ta có:

# * **Minimum Spanning Tree (MST)** → tổng weight nhỏ nhất

# Nhưng bài này là:

# 👉 **Maximum Spanning Tree**

# Tức là:

# Chọn **N − 1 cạnh** sao cho:

# **tổng stability lớn nhất**

# ---

# ## 4. Phần "Upgrades"

# Một số cạnh có thể **nâng cấp (upgrade)**.

# Khi nâng cấp:

# * stability của cạnh **tăng lên**

# Nhưng:

# * số lần upgrade **bị giới hạn** (ví dụ: chỉ upgrade tối đa K cạnh)

# ---

# ## 5. Mục tiêu bài toán

# Bạn cần:

# 1️⃣ Chọn các cạnh để tạo **spanning tree**

# 2️⃣ Có thể **upgrade tối đa K cạnh**

# 3️⃣ Sau khi upgrade, **tổng stability của spanning tree phải lớn nhất**

# ---

# ## 6. Tóm tắt đề bài bằng ngôn ngữ đơn giản

# Bạn có:

# * N đỉnh
# * M cạnh
# * mỗi cạnh có stability
# * có thể **upgrade tối đa K cạnh**

# Hãy:

# 👉 tạo **Maximum Spanning Tree**

# sao cho:

# **tổng stability sau khi upgrade là lớn nhất**

# ---

# ## 7. Input thường gặp

# Ví dụ:

# ```
# N M K
# u v w
# u v w
# ...
# ```

# Trong đó:

# * `u v` : hai đỉnh nối với nhau
# * `w` : stability ban đầu
# * `K` : số cạnh có thể upgrade

# Upgrade có thể:

# ```
# w -> w + x
# ```

# hoặc

# ```
# w -> w * 2
# ```

# (tùy đề)

# ---

# ## 8. Output

# In ra:

# ```
# maximum total stability
# ```

# ---

# ## 9. Ý tưởng thuật toán (tổng quan)

# Thường sẽ dùng:

# **Kruskal + Greedy**

# Bước cơ bản:

# 1️⃣ Sắp xếp cạnh theo **stability giảm dần**

# 2️⃣ Dùng **Union-Find (DSU)**

# 3️⃣ Xây **Maximum Spanning Tree**

# 4️⃣ Tính xem **upgrade cạnh nào giúp tăng tổng nhiều nhất**

# ---

# ## 10. Độ khó thật sự của bài

# Phần khó là:

# * chọn **cạnh nào upgrade**
# * upgrade **trước hay sau khi vào MST**

# Một số bài cần:

# * **Kruskal + priority queue**
# * hoặc **DP trên cạnh**

# ---

# 💡 Nếu bạn muốn, mình có thể:

# * **vẽ hình minh họa spanning tree**
# * **giải từng bước bằng ví dụ nhỏ**
# * **viết code Java/Python cho bài này**

# Chỉ cần gửi **toàn bộ đề bài hoặc input sample** mình sẽ giải chi tiết.
