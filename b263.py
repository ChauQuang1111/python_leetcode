# // Bài toán "Find the Safest Path in a Grid" (01/07/2026)

# // Đề bài

# // Cho một ma trận grid kích thước n × n.



# // grid[i][j] = 1 nghĩa là ô đó có kẻ trộm.

# // grid[i][j] = 0 nghĩa là ô bình thường.

# // Bạn bắt đầu tại ô:



# // (0, 0)

# // và cần đi đến:



# // (n-1, n-1)

# // Mỗi bước chỉ được đi:



# // lên

# // xuống

# // trái

# // phải

# // Không được đi chéo.

# // Khái niệm "Safeness Factor"

# // Đây là phần quan trọng nhất của đề.

# // Đầu tiên, với mỗi ô, ta tính:



# // Khoảng cách ngắn nhất từ ô đó đến bất kỳ kẻ trộm nào.

# // Khoảng cách được tính bằng Manhattan Distance:

# // [

# // |x_1-x_2|+|y_1-y_2|

# // ]

# // Ví dụ



# // 0 0 0

# // 0 1 0

# // 0 0 0

# // Kẻ trộm ở giữa.

# // Khoảng cách của từng ô đến tên trộm:



# // 2 1 2

# // 1 0 1

# // 2 1 2

# // Safeness của một đường đi

# // Một đường đi sẽ đi qua nhiều ô.

# // Safeness của đường đi là:



# // Giá trị nhỏ nhất trong tất cả khoảng cách của các ô trên đường đi.

# // Ví dụ đường đi đi qua các ô có khoảng cách



# // 3 → 2 → 2 → 1 → 2

# // thì



# // Safeness = min(3,2,2,1,2)=1

# // Vì có một ô chỉ cách kẻ trộm 1 bước.

# // Mục tiêu

# // Tìm đường đi sao cho



# // Safeness Factor lớn nhất có thể.

# // Hay nói cách khác:



# // Trong tất cả các đường đi từ trái trên đến phải dưới, hãy chọn đường mà ô "nguy hiểm nhất" trên đường đó vẫn an toàn nhất.

# // Đây là bài toán maximize the minimum.

# // Ví dụ 1

# // grid =



# // 0 0 1

# // 0 0 0

# // 0 0 0

# // Kẻ trộm ở góc phải trên.

# // Khoảng cách:



# // 2 1 0

# // 3 2 1

# // 4 3 2

# // Nếu đi



# // ↓

# // ↓

# // →

# // →

# // ta đi qua



# // 2

# // 3

# // 4

# // 3

# // 2

# // Safeness



# // min = 2

# // Nếu đi sát phía trên



# // →

# // →

# // ↓

# // ↓

# // ta đi qua



# // 2

# // 1

# // 0

# // 1

# // 2

# // Safeness



# // 0

# // Đường đầu tiên tốt hơn.

# // Ví dụ 2

# // 0 0

# // 1 0

# // Khoảng cách



# // 1 2

# // 0 1

# // Có hai đường.

# // Đường 1



# // ↓



# // →

# // Đi qua



# // 1

# // 0

# // 1

# // Safeness = 0

# // Đường 2



# // →



# // ↓

# // Đi qua



# // 1

# // 2

# // 1

# // Safeness = 1

# // Đáp án là



# // 1

# // Ý tưởng thuật toán

# // Bài này thường được giải theo 2 bước:



# // Bước 1: Tính khoảng cách đến kẻ trộm

# // Dùng Multi-source BFS:



# // Đưa tất cả các ô có 1 vào hàng đợi ngay từ đầu.

# // BFS lan ra toàn bộ ma trận.

# // Thu được mảng dist[i][j] là khoảng cách ngắn nhất từ mỗi ô đến kẻ trộm.

# // Độ phức tạp:



# // O(n²)

# // Bước 2: Tìm đường đi có safeness lớn nhất

# // Có nhiều cách:



# // Binary Search + BFS

# // Priority Queue (Max Heap) giống ý tưởng của Dijkstra's algorithm nhưng thay phép cộng bằng lấy min

# // Union-Find

# // Cách dùng Max Heap rất phổ biến:



# // Luôn ưu tiên mở rộng ô có giá trị dist lớn hơn.

# // Khi đi sang ô mới:

# // newSafeness =

# // min(currentSafeness,

# //     dist[next])

# // Khi tới đích, giá trị thu được là đáp án tối ưu.

# // Tóm tắt trực quan

# // Giả sử ma trận khoảng cách đã được tính là:



# // 4 3 2

# // 3 2 1

# // 2 1 0

# // Đường A:



# // 4 → 3 → 2 → 1 → 0

# // Safeness



# // 0

# // Đường B:



# // 4

# // ↓

# // 3

# // ↓

# // 2

# // →

# // 1

# // →

# // 0

# // Safeness vẫn là



# // 0

# // Nếu tồn tại một đường khác chỉ đi qua các ô có khoảng cách:



# // 4 → 4 → 3 → 3 → 2

# // thì



# // Safeness = 2

# // Đây sẽ là đường được chọn vì 2 lớn hơn 0.

# // Tóm lại, bài toán gồm hai ý chính:



# // Tính với mỗi ô khoảng cách ngắn nhất đến kẻ trộm bằng Multi-source BFS.

# // Tìm đường đi từ (0,0) đến (n-1,n-1) sao cho giá trị nhỏ nhất của dist trên đường đi là lớn nhất (maximize the minimum).


# // Đoạn code trên giải bài 2812. Find the Safest Path in a Grid bằng 2 bước:



# // Multi-source BFS để tính khoảng cách từ mỗi ô đến tên trộm gần nhất.

# // 0-1 BFS (Deque BFS) để tìm đường đi có Safeness Factor lớn nhất.

# // Ý tưởng thuật toán

# // Bước 1: Tính khoảng cách đến tên trộm gần nhất

# // Ví dụ



# // 0 0 0

# // 0 1 0

# // 0 0 0

# // Tên trộm ở giữa.

# // Khởi tạo



# // mDist



# // -1 -1 -1

# // -1  0 -1

# // -1 -1 -1

# // Ta đưa tất cả vị trí có 1 vào Queue.



# // Queue



# // (1,1)

# // Sau đó BFS.

# // Lần đầu



# // 2 1 2

# // 1 0 1

# // 2 1 2

# // Ý nghĩa

# // Ví dụ



# // mDist[0][1] = 1

# // nghĩa là ô (0,1) cách tên trộm gần nhất đúng 1 bước.

# // Vì sao dùng Multi-source BFS?

# // Nếu BFS từng tên trộm thì



# // k thieves



# // => O(k*n²)

# // Trong khi đưa tất cả thief vào Queue ngay từ đầu chỉ cần



# // O(n²)

# // Bước 2

# // Sau khi có



# // mDist



# // 4 3 2

# // 3 2 1

# // 2 1 0

# // Ta cần tìm đường đi.

# // Giả sử đi



# // 4 ->3 ->2 ->1 ->0

# // Safeness



# // min=0

# // Nếu đi



# // 4

# // ↓

# // 3

# // ↓

# // 2

# // →

# // 2

# // →

# // 2

# // Safeness



# // 2

# // Đường này tốt hơn.

# // Tại sao dùng deque?

# // Ở mỗi bước



# // nextSafety=min(currentSafety,mDist[next])

# // Có hai trường hợp.



# // Trường hợp 1

# // currentSafety=4



# // next=4

# // nextSafety=4

# // Đường đi vẫn rất tốt.

# // => ưu tiên xử lý trước.



# // appendleft()

# // Trường hợp 2

# // currentSafety=4



# // next=1

# // nextSafety=1

# // Đường này xấu hơn.

# // => xử lý sau.



# // append()

# // Ý tưởng giống 0-1 BFS

# // Giải thích từng đoạn code

# // Khởi tạo

# // n = len(grid)

# // Lấy kích thước ma trận.

# // Queue chứa thief

# // thieves = deque([])

# // Ma trận khoảng cách

# // mDist = [[-1]*n for i in range(n)]

# // Ví dụ



# // -1 -1 -1

# // -1 -1 -1

# // -1 -1 -1

# // Đưa thief vào Queue

# // for i in range(n):

# //     for j in range(n):

# //         if grid[i][j]==1:

# //             thieves.append((i,j))

# //             mDist[i][j]=0

# // Ví dụ



# // 0 1 0

# // 0 0 1

# // Queue



# // (0,1)

# // (1,2)

# // Nếu đầu hoặc cuối có thief

# // if mDist[0][0]==0 or mDist[-1][-1]==0:

# //     return 0

# // Không thể an toàn.

# // BFS

# // while thieves:

# // Lấy



# // r,c=thieves.popleft()

# // Duyệt 4 hướng



# // for rOS,cOS in dirs:

# // Ô chưa thăm



# // if mDist[adjR][adjC]==-1

# // Cập nhật



# // mDist[adjR][adjC]=mDist[r][c]+1

# // Ví dụ



# // 0



# // ↓



# // 1



# // ↓



# // 2

# // Bắt đầu tìm đường

# // travel=deque([(mDist[0][0],0,0)])

# // Lưu



# // (safety,row,col)

# // Ví dụ



# // (5,0,0)

# // nghĩa là



# // Đang ở (0,0)



# // Safeness=5

# // visited

# // visited[0][0]=True

# // Không đi lại.

# // ans

# // ans=min(mDist[0][0],mDist[-1][-1])

# // Vì đường nào cũng phải đi qua



# // đầu



# // và



# // cuối

# // nên safeness không thể lớn hơn giá trị nhỏ nhất của hai ô này.

# // BFS tìm đường

# // while travel:

# // Lấy



# // safety,r,c

# // Nếu đến đích



# // return ans

# // Tính safeness mới

# // nextSafety=min(

# //     mDist[adjR][adjC],

# //     safety

# // )

# // Ví dụ



# // Đường hiện tại



# // 5



# // ↓



# // 4



# // ↓



# // 4

# // Đi tiếp sang ô



# // 2

# // thì



# // nextSafety



# // =min(4,2)



# // =2

# // Quyết định append hay appendleft

# // if nextSafety<ans:

# // Đường xấu



# // append()

# // Ngược lại



# // appendleft()

# // Đường tốt



# // appendleft()

# // Để xử lý sớm.

# // Độ phức tạp

# // BFS đầu

# // O(n²)

# // BFS tìm đường

# // Mỗi ô đi đúng 1 lần



# // O(n²)

# // Tổng

# // Time



# // O(n²)

# // Space



# // O(n²)

# // Code Java (Scanner) có chú thích

# import java.util.*;
# public class b264{

#   // 4 hướng di chuyển
#     static int[] dr = {1, -1, 0, 0};
#     static int[] dc = {0, 0, 1, -1};
#     static Scanner sc = new Scanner(System.in);
#     public static void main(String[] args) {
#         int n = sc.nextInt();
#         int[][] grid = new int[n][n];
#         // Nhập ma trận
#         for (int i = 0; i < n; i++) {

#             for (int j = 0; j < n; j++) {

#                 grid[i][j] = sc.nextInt();

#             }

#         }
#         System.out.println(maximumSafenessFactor(grid));

    
#     }
#  public static int maximumSafenessFactor(int[][] grid) {



#         int n = grid.length;



#         // Lưu khoảng cách đến thief gần nhất

#         int[][] dist = new int[n][n];

#         for (int i = 0; i < n; i++)

#             Arrays.fill(dist[i], -1);



#         // Queue cho Multi-source BFS

#         Deque<int[]> thieves = new ArrayDeque<>();



#         // Đưa tất cả thief vào queue

#         for (int i = 0; i < n; i++) {

#             for (int j = 0; j < n; j++) {



#                 if (grid[i][j] == 1) {

#                     thieves.offer(new int[]{i, j});

#                     dist[i][j] = 0;

#                 }



#             }

#         }



#         // Nếu đầu hoặc cuối là thief

#         if (dist[0][0] == 0 || dist[n - 1][n - 1] == 0)

#             return 0;



#         // Multi-source BFS

#         while (!thieves.isEmpty()) {



#             int[] cur = thieves.poll();



#             int r = cur[0];

#             int c = cur[1];



#             for (int k = 0; k < 4; k++) {



#                 int nr = r + dr[k];

#                 int nc = c + dc[k];



#                 if (nr >= 0 && nr < n &&

#                     nc >= 0 && nc < n &&

#                     dist[nr][nc] == -1) {



#                     dist[nr][nc] = dist[r][c] + 1;

#                     thieves.offer(new int[]{nr, nc});

#                 }

#             }

#         }



#         // deque tìm đường

#         Deque<int[]> travel = new ArrayDeque<>();



#         // {safety,row,col}

#         travel.offer(new int[]{dist[0][0], 0, 0});



#         boolean[][] visited = new boolean[n][n];

#         visited[0][0] = true;



#         int ans = Math.min(dist[0][0], dist[n - 1][n - 1]);



#         while (!travel.isEmpty()) {



#             int[] cur = travel.pollFirst();



#             int safety = cur[0];

#             int r = cur[1];

#             int c = cur[2];



#             ans = Math.min(ans, safety);



#             // Đến đích

#             if (r == n - 1 && c == n - 1)

#                 return ans;



#             for (int k = 0; k < 4; k++) {



#                 int nr = r + dr[k];

#                 int nc = c + dc[k];



#                 if (nr >= 0 && nr < n &&

#                     nc >= 0 && nc < n &&

#                     !visited[nr][nc]) {



#                     visited[nr][nc] = true;



#                     // Safeness mới của đường đi

#                     int nextSafety = Math.min(safety, dist[nr][nc]);



#                     // Đường tốt -> xử lý trước

#                     if (nextSafety >= ans)

#                         travel.offerFirst(new int[]{nextSafety, nr, nc});

#                     else

#                         travel.offerLast(new int[]{nextSafety, nr, nc});

#                 }

#             }

#         }



#         return -1;

# }




    



   
#     }



   

# // Ví dụ nhập

# // 3

# // 0 0 1

# // 0 0 0

# // 0 0 0

# // Kết quả

# // 2

# // Đoạn Java trên bám sát từng dòng của mã Python, chỉ chuyển sang cú pháp Java và bổ sung chú thích để dễ theo dõi thuật toán.

# Đây là phiên bản Python tương đương với code Java của bạn, kèm chú thích chi tiết giải thích từng bước của thuật toán.



from typing import List
class Solution:

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        n = len(grid)



        # Nếu ô bắt đầu hoặc ô kết thúc là thief

        # hoặc ma trận chỉ có 1 ô thì đáp án là 0

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1 or n == 1:

            return 0



        # Sao chép grid để không làm thay đổi dữ liệu ban đầu

        arr = [row[:] for row in grid]



        # Bước 1:

        # Tính khoảng cách từ mỗi ô đến thief gần nhất

        arr = self.updateMatrix(arr)



        # Binary Search trên đáp án

        low = 0

        high = (n - 1) * 2          # Khoảng cách Manhattan lớn nhất



        result = 0



        while low <= high:



            mid = (low + high) // 2



            # Kiểm tra xem có đường đi mà

            # mọi ô đều có khoảng cách >= mid hay không

            visited = [[False] * n for _ in range(n)]



            if self.dfs(arr, 0, 0, mid, n, visited):

                result = mid          # Có đường đi

                low = mid + 1         # Thử tăng safeness

            else:

                high = mid - 1        # Giảm safeness



        return result



    ####################################################

    # Tính khoảng cách tới thief gần nhất

    ####################################################

    def updateMatrix(self, matrix):



        n = len(matrix)



        # Đổi:

        # thief (1) -> 0

        # ô thường (0) -> INF

        for r in range(n):

            for c in range(n):



                matrix[r][c] ^= 1



                if matrix[r][c] == 1:

                    matrix[r][c] = 10 ** 9



        ####################################################

        # Quét theo hàng

        ####################################################



        # Trái -> phải

        for r in range(n):

            for c in range(1, n):

                matrix[r][c] = min(

                    matrix[r][c],

                    matrix[r][c - 1] + 1

                )



            # Phải -> trái

            for c in range(n - 2, -1, -1):

                matrix[r][c] = min(

                    matrix[r][c],

                    matrix[r][c + 1] + 1

                )



        ####################################################

        # Quét theo cột

        ####################################################



        # Trên -> dưới

        for c in range(n):



            for r in range(1, n):

                matrix[r][c] = min(

                    matrix[r][c],

                    matrix[r - 1][c] + 1

                )



            # Dưới -> trên

            for r in range(n - 2, -1, -1):

                matrix[r][c] = min(

                    matrix[r][c],

                    matrix[r + 1][c] + 1

                )



        return matrix



    ####################################################

    # DFS kiểm tra có đường đi với safeness >= limit

    ####################################################

    def dfs(self, arr, r, c, limit, n, visited):



        # Đã thăm hoặc ô không đủ an toàn

        if visited[r][c] or arr[r][c] < limit:

            return False



        # Đến đích

        if r == n - 1 and c == n - 1:

            return True



        visited[r][c] = True



        dx = [-1, 1, 0, 0]

        dy = [0, 0, 1, -1]



        for i in range(4):



            nr = r + dx[i]

            nc = c + dy[i]



            # Ngoài ma trận

            if nr < 0 or nc < 0 or nr >= n or nc >= n:

                continue



            if self.dfs(arr, nr, nc, limit, n, visited):

                return True



        return False

# Ý tưởng của thuật toán

# Thuật toán gồm 3 bước:



# Bước 1. Tính khoảng cách đến thief gần nhất (updateMatrix)

# Ví dụ:



# 0 0 1

# 0 0 0

# 0 0 0

# Sau khi tính khoảng cách:



# 2 1 0

# 3 2 1

# 4 3 2

# Mỗi ô lưu khoảng cách Manhattan ngắn nhất đến một thief.

# Bước 2. Binary Search

# Giả sử thử:



# mid = 2

# Ý nghĩa:



# Có tồn tại đường đi mà mọi ô trên đường đều có khoảng cách ≥ 2 không?

# Nếu có:



# => thử tăng lên 3

# Nếu không:



# => giảm xuống 1

# Do tính chất "nếu đi được với k thì chắc chắn đi được với mọi giá trị nhỏ hơn k", ta có thể dùng Binary Search trên đáp án.

# Bước 3. DFS

# DFS chỉ đi qua các ô:



# arr[r][c] >= mid

# Ví dụ với:



# mid = 3

# Từ ma trận khoảng cách:



# 4 3 2

# 3 2 1

# 2 1 0

# Ta chỉ được đi trên:



# 4 3 X

# 3 X X

# X X X

# (X là ô không đủ an toàn nên bị bỏ qua.)

# Nếu DFS tới được đích thì mid là khả thi.

# Độ phức tạp

# updateMatrix: khoảng O(n²) (bốn lượt quét ma trận).

# Mỗi lần DFS: O(n²) trong trường hợp xấu nhất.

# Binary Search: tìm trên khoảng giá trị từ 0 đến 2(n−1), nên có khoảng O(log n) lần kiểm tra.

# Tổng độ phức tạp xấp xỉ:

# [

# O(n^2 \log n)

# ]

# với bộ nhớ phụ:

# [

# O(n^2)

# ]

# Lưu ý: Cách updateMatrix trong đoạn mã này sử dụng nhiều lượt quét (dynamic programming relaxation), khác với lời giải chuẩn của bài là Multi-source BFS. Mặc dù có thể hoạt động với nhiều trường hợp, cách chuẩn và được khuyến nghị trên LeetCode là dùng Multi-source BFS để đảm bảo tính đúng đắn cho khoảng cách Manhattan trong mọi cấu hình của ma trận.