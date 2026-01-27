# # // // Minimum Cost Path with Edge Reversals(27/01/2026)
# # // // Ok, mình giải thích **đề “Minimum Cost Path with Edge Reversals”** theo kiểu **dễ hiểu – đúng bản chất – hay gặp trong thuật toán đồ thị** nha 👌
# # // // Ok,mình**giải thích thuật toán đúng theo code bạn đưa**,từng khối một,tập trung vào**ý tưởng+vì sao làm vậy**,không lan man👌
# # // Ok👍mình**thêm`main`dùng`Scanner`**và**chú thích chi tiết trực tiếp trong code**,giữ nguyên logic thuật toán của bạn để dễ học và dễ nhớ.
# Ok 👍 mình **giải thích thuật toán + thêm chú thích trực tiếp vào code Python**, bám sát đúng bài **3650. Minimum Cost Path with Edge Reversals**, để bạn nhìn code là hiểu ngay.

# ---

## 🧠 Ý tưởng thuật toán (nói ngắn gọn trước)

# * Đồ thị **có hướng**
# * Đi **đúng chiều cạnh** → cost = `w`
# * Đi **ngược chiều cạnh** → cost = `2*w` (coi như “đảo chiều”, bị phạt)

# 👉 **Biến bài toán** thành:

# > Tìm **đường đi chi phí nhỏ nhất** từ node `0` → node `n-1`

# ➡️ Dùng **Dijkstra** vì:

# * Trọng số **không âm**
# * Cần shortest path

# ---

# ## ✅ Code có chú thích chi tiết

# ```python
from collections import defaultdict
import heapq
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        # graph[u] = danh sách các (v, cost) có thể đi từ u
        graph = defaultdict(list)

        # ====== BUILD GRAPH ======
        # Với mỗi cạnh gốc u -> v có trọng số w:
        #  - đi đúng chiều: u -> v, cost = w
        #  - đi ngược chiều: v -> u, cost = 2*w
        for u, v, w in edges:
            graph[u].append((v, w))        # cạnh đúng hướng
            graph[v].append((u, 2 * w))    # cạnh ngược hướng (bị phạt)

        # dist[i] = chi phí nhỏ nhất từ node 0 đến node i
        dist = [float('inf')] * n
        dist[0] = 0   # bắt đầu tại node 0

        # Priority Queue cho Dijkstra
        # (cost, node) → luôn lấy node có cost nhỏ nhất
        pq = [(0, 0)]

        # ====== DIJKSTRA ======
        while pq:
            cost, u = heapq.heappop(pq)

            # Nếu entry này đã lỗi thời (không phải cost tốt nhất)
            if cost > dist[u]:
                continue

            # Nếu đã tới đích thì trả kết quả luôn
            # (Dijkstra đảm bảo đây là chi phí nhỏ nhất)
            if u == n - 1:
                return cost

            # Relax các cạnh kề
            for v, w in graph[u]:
                new_cost = cost + w

                # Nếu tìm được đường rẻ hơn đến v
                if new_cost < dist[v]:
                    dist[v] = new_cost
                    heapq.heappush(pq, (new_cost, v))

        # Không tồn tại đường đi từ 0 -> n-1
        return -1


## 🔍 Phân tích từng điểm quan trọng

### 1️⃣ Vì sao thêm cạnh ngược với `2*w`?

# 👉 Để **mô phỏng việc đảo chiều cạnh**

# * Không cần xử lý riêng “reversal”
# * Chỉ cần shortest path bình thường



### 2️⃣ Vì sao dùng Dijkstra?

# * Tất cả trọng số ≥ 0
# * Cần tìm **minimum cost path**
# * Dijkstra đảm bảo **đúng + tối ưu**

# ---

# ### 3️⃣ Vì sao có `stale entry`?

# ```python
# if cost > dist[u]:
#     continue
# ```

# 👉 Tránh xử lý các trạng thái **cũ, không tối ưu**
# Giúp thuật toán chạy nhanh hơn

# ---

# ### 4️⃣ Vì sao `early exit` là đúng?

# ```python
# if u == n - 1:
#     return cost
# ```

# 📌 Trong Dijkstra:

# > Lần đầu lấy node đích ra khỏi heap → **đã là chi phí nhỏ nhất**

# ---

# ## ⏱️ Độ phức tạp

# * **Time**: `O((V + E) log V)`
# * **Space**: `O(V + E)`

# ---

# ## 🧾 Tóm tắt để đi thi / phỏng vấn

# # > Chuyển mỗi cạnh có hướng thành:
# # >
# # > * xuôi chiều: cost = w
# # > * ngược chiều: cost = 2w
# # >   rồi chạy Dijkstra từ node 0 đến node n−1.

# # ---

# Nếu bạn muốn:

# * 🔄 **viết lại bằng 0–1 BFS**
# * 🧪 **chạy tay 1 test mẫu**
# * ⚖️ **so sánh Python vs Java version**

# 👉 cứ nói, mình làm tiếp cho bạn 💪

# // ---

# // ###✅Code hoàn chỉnh(có`main`+chú thích)

# // ```java

# import java.util.*;

# public class b161 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int n = sc.nextInt(); // số đỉnh
#         int m = sc.nextInt(); // số cạnh

#         int[][] edges = new int[m][3];

#         for (int i = 0; i < m; i++) {
#             edges[i][0] = sc.nextInt(); // u
#             edges[i][1] = sc.nextInt(); // v
#             edges[i][2] = sc.nextInt(); // w
#         }

#         int result = minCost(n, edges);

#         System.out.println(result);
#         sc.close();

#     }

#     // Lớp Edge biểu diễn 1 cạnh trong đồ thị
#     static class Edge {
#         int to; // đỉnh đi tới
#         int weight; // trọng số (chi phí)

#         Edge(int to, int weight) {
#             this.to = to;
#             this.weight = weight;
#         }
#     }

#     // Hàm tìm chi phí nhỏ nhất từ node 0 -> node n-1
#     public static int minCost(int n, int[][] edges) {

#         // Danh sách kề
#         @SuppressWarnings("unchecked")
#         List<Edge>[] graph = new ArrayList[n];

#         // Khởi tạo danh sách kề
#         for (int i = 0; i < n; i++) {
#             graph[i] = new ArrayList<>();
#         }

#         /*
#          * Với mỗi cạnh u -> v có trọng số w:
#          * - đi xuôi: u -> v, cost = w
#          * - đi ngược: v -> u, cost = 2w
#          */
#         for (int[] edge : edges) {
#             int u = edge[0];
#             int v = edge[1];
#             int w = edge[2];

#             graph[u].add(new Edge(v, w)); // đúng chiều
#             graph[v].add(new Edge(u, 2 * w)); // ngược chiều (bị phạt)
#         }

#         // dist[i] = chi phí nhỏ nhất từ node 0 đến node i
#         int[] dist = new int[n];
#         Arrays.fill(dist, Integer.MAX_VALUE);
#         dist[0] = 0;

#         // PriorityQueue cho Dijkstra (node, distance)
#         PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);

#         // Bắt đầu từ node 0
#         pq.add(new int[] { 0, 0 });

#         // Dijkstra
#         while (!pq.isEmpty()) {
#             int[] current = pq.poll();
#             int currentNode = current[0];
#             int currentDist = current[1];

#             // Nếu đã tới đích thì trả kết quả luôn
#             if (currentNode == n - 1) {
#                 return currentDist;
#             }

#             // Nếu khoảng cách này không tối ưu thì bỏ qua
#             if (currentDist > dist[currentNode])
#                 continue;

#             // Relax các cạnh kề
#             for (Edge edge : graph[currentNode]) {
#                 int nextNode = edge.to;
#                 int weight = edge.weight;

#                 if (dist[nextNode] > currentDist + weight) {
#                     dist[nextNode] = currentDist + weight;
#                     pq.add(new int[] { nextNode, dist[nextNode] });
#                 }
#             }
#         }

#         // Nếu không đi được tới n-1
#         return -1;
#     }
# }

# // 👉 Biến mỗi cạnh có hướng thành **2 cạnh có trọng số khác nhau**
# // * **Thuật toán**: Dijkstra
# // * **Ứng dụng**:

# // * Edge reversal
# // * Direction cost
# // * Penalize reverse edges

# // ---

# // Nếu bạn muốn mình:

# // * ✍️ **viết lại theo 0–1 BFS**
# // * 🔄 **đổi sang dùng while thay for**
# // * 🧪 **chạy tay test để debug từng bước**

# // 👉 cứ nói, mình làm tiếp cho bạn 👌

# // ---

# // #1 ️⃣Bài toán mà code này đang giải

# // Đây là**bài shortest path trên đồ thị có hướng**,cho phép:

# // *Đi**đúng chiều**cạnh:tốn`w`*Đi**ngược chiều**cạnh:tốn**gấp đôi**→`2*w`

# // 👉Mục tiêu:**Tìm chi phí nhỏ nhất để đi từ node`0`đến node`n-1`**

# // 📌*Nó là biến thể của“Edge Reversal/Edge Direction Cost”*

# // ---

# // #2 ️⃣Cấu trúc`Edge`

# // ```java
# // static class Edge {
# // int to;
# // int weight;}```

# // 👉
# // Mỗi cạnh lưu:

# // *`to`:
# // đỉnh đi tới*`weight`:
# // chi phí
# // khi đi
# // cạnh đó

# // ---

# // #3 ️⃣
# // Xây dựng

# // đồ thị (phần QUAN TRỌNG NHẤT)

# // ```java
# // for(int[] edge : edges) {
# // int u = edge[0];
# // int v = edge[1];
# // int w = edge[2];

# // graph[u].add(new Edge(v, w)); // đi đúng hướng
# // graph[v].add(new Edge(u, 2*w)); // đi ngược hướng
# // }
# // ```

# // ### Ý tưởng cốt lõi ở đây 👇

# // Mỗi cạnh gốc:

# // ```
# // u → v (cost = w)
# // ```

# // Ta biến thành:

# // ```
# // u → v (cost = w)
# // v → u (cost = 2w)
# // ```

# // 📌 Như vậy:

# // * Đi **xuôi chiều** → chi phí thấp
# // * Đi **ngược chiều** → bị phạt nặng hơn

# // ➡️ **Biến bài toán có đảo chiều thành bài toán shortest path chuẩn**

# // ---

# // # 4️⃣ Mảng `dist[]`

# // ```java
# // int[] dist = new int[n];
# // Arrays.fill(dist, Integer.MAX_VALUE);
# // dist[0] = 0;
# // ```

# // 👉 `dist[i]` = **chi phí nhỏ nhất từ node 0 → node i**

# // Ban đầu:

# // * Chưa đi đâu → ∞
# // * Node bắt đầu (`0`) → 0

# // ---

# // # 5️⃣ PriorityQueue (Dijkstra)

# // ```java
# // PriorityQueue<int[]> pq =
# // new PriorityQueue<>((a, b) -> a[1] - b[1]);

# // pq.add(new int[]{0, 0});
# // ```

# // Mỗi phần tử:

# // ```
# // {node, distance}
# // ```

# // 👉 PQ luôn lấy **node có distance nhỏ nhất trước**

# // ---

# // # 6️⃣ Vòng lặp Dijkstra

# // ```java
# // while(!pq.isEmpty()) {
# // int[] current = pq.poll();
# // int currentNode = current[0];
# // int distanceToCurrentNode = current[1];
# // ```

# // 📌 Lấy node đang có **đường đi ngắn nhất tạm thời**

# // ---

# // ## 🚀 Điều kiện

# // dừng sớm (tối ưu)

# // ```java
# // if(currentNode == n - 1)
# // return distanceToCurrentNode;
# // ```

# // 👉 Vì Dijkstra đảm bảo:

# // * **Lần đầu lấy ra `n-1` là đường đi ngắn nhất**

# // ---

# // # 7️⃣

# // Relax cạnh (bước cốt lõi của Dijkstra)

# // ```java
# // for(Edge edge : graph[currentNode]) {
# // int nextNode = edge.to;
# // int weight = edge.weight;

# // if(dist[nextNode] > distanceToCurrentNode + weight) {
# // dist[nextNode] = distanceToCurrentNode + weight;
# // pq.add(new int[]{nextNode, dist[nextNode]});
# // }
# // }
# // ```

# // 👉 Kiểm tra:

# // * Nếu đi qua `currentNode` → `nextNode` **rẻ hơn đường cũ**
# // * Cập nhật lại `dist`
# // * Đẩy vào PQ để xét tiếp

# // 📌 Đây gọi là **relaxation**

# // ---

# // # 8️⃣ Kết luận thuật toán

# // ### 🔹 Thuật toán dùng:

# // 👉 **Dijkstra**

# // ### 🔹 Vì sao đúng?

# // * Mọi cạnh đều có trọng số **không âm**
# // * Đồ thị đã được **chuyển đổi để mô phỏng đảo chiều**

# // ### 🔹 Độ phức tạp:

# // ```
# // O((V + E) log V)
# // ```

# // ---

# // # 9️⃣ Tóm tắt 1

# // dòng (rất hay dùng khi đi thi)

# // > Chuyển mỗi cạnh có hướng thành 2 cạnh:
# // >
# // > * xuôi chiều: cost = w
# // > * ngược chiều: cost = 2w
# // > rồi chạy **Dijkstra** từ node 0 đến node n−1.

# // ---

# // Nếu bạn muốn mình:

# // * 🔍 **so sánh code này với 0–1 BFS**
# // * 🧠 **chứng minh vì sao dừng sớm là đúng**
# // * 🧪 **chạy tay 1 test để bạn “ngộ” thuật toán**

# // 👉 nói mình chọn cái nào nha 😄

# // ---

# // ## 1️⃣ Mô tả bài toán (hiểu đề trước đã)

# // Bạn được cho:

# // * Một **đồ thị có hướng** (directed graph)
# // * Các đỉnh: `1 → n`
# // * Các cạnh có hướng **u → v**

# // 👉 **Mục tiêu**:
# // Tìm **chi phí nhỏ nhất** để đi từ **đỉnh 1 đến đỉnh n**

# // ---

# // ## 2️⃣ “Edge Reversal” là gì?

# // * Nếu **cạnh tồn tại đúng hướng** `u → v`
# // → đi **miễn phí (cost = 0)**

# // * Nếu bạn muốn đi **ngược hướng** `v → u`
# // → phải **đảo chiều cạnh**, tốn **cost = 1**

# // 👉 Mỗi lần **đảo chiều 1 cạnh = +1 chi phí**

# // ---

# // ## 3️⃣ Nói cách khác (cực quan trọng)

# // Bài này hỏi:

# // > ❓ *Cần đảo chiều ít cạnh nhất để tồn tại đường đi từ 1 → n?*

# // 🔑 **Bài toán = tìm đường đi với số lần đảo cạnh nhỏ nhất**

# // ---

# // ## 4️⃣ Ví dụ minh họa đơn giản

# // Giả sử có đồ thị:

# // ```
# // 1 → 2
# // 3 → 2
# // 3 → 4
# // ```

# // Muốn đi từ `1 → 4`

# // ### Phân tích:

# // * `1 → 2` ✅ đúng hướng (cost 0)
# // * `2 → 3` ❌ không có → phải **đảo** `3 → 2` (cost +1)
# // * `3 → 4` ✅ đúng hướng (cost 0)

# // ➡️ **Tổng cost = 1**

# // ---

# // ## 5️⃣ Biến đổi bài toán (mấu chốt)

# // Ta **biến đồ thị ban đầu** thành **đồ thị mới**:

# // * Với mỗi cạnh `u → v`:

# // * Thêm cạnh `u → v` với **cost = 0**
# // * Thêm cạnh `v → u` với **cost = 1**

# // 📌 Sau đó:
# // ➡️ **Tìm đường đi chi phí nhỏ nhất từ 1 → n**

# // ---

# // ## 6️⃣ Dùng thuật toán gì?

# // Vì:

# // * Trọng số chỉ có **0 hoặc 1**

# // 👉 **Dùng 0–1 BFS** (nhanh hơn Dijkstra)

# // ### Ý tưởng 0–1 BFS:

# // * Nếu đi cạnh **cost 0** → cho vào **đầu deque**
# // * Nếu đi cạnh **cost 1** → cho vào **cuối deque**

# // ⏱️ Thời gian: **O(V + E)**

# // ---

# // ## 7️⃣ Tóm tắt cực ngắn (để nhớ khi đi thi)

# // 📌 **Minimum Cost Path with Edge Reversals**

# // * Đồ thị có hướng
# // * Đi đúng hướng: 0
# // * Đi ngược hướng: +1
# // * Biến thành đồ thị trọng số {0,1}
# // * Dùng **0–1 BFS**
# // * Kết quả = số cạnh cần đảo ít nhất

# // ---

# // Nếu bạn muốn:

# // * Mình **giải mẫu 1 test cụ thể**
# // * Hoặc **code Java / C++ / Python**
# // * Hoặc **so sánh với Dijkstra**

# // 👉 nói mình biết nha 👍
