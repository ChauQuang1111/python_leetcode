# // // Bài Minimum Score of a Path Between Two Cities (04/07/2026)
# // // Đề bài

# // // Có n thành phố được đánh số từ 1 đến n.

# // // Có một danh sách các con đường roads, trong đó:



# // // roads[i] = [a, b, distance]

# // // nghĩa là có một con đường hai chiều nối thành phố a và b với độ dài (hoặc điểm số) là distance.



# // // Định nghĩa Score của một đường đi

# // // Score của một đường đi không phải là tổng khoảng cách.

# // // Mà được định nghĩa là:



# // // Giá trị nhỏ nhất của tất cả các cạnh xuất hiện trên đường đi đó.

# // Ví dụ:



# // 1 --9-- 2 --5-- 3 --7-- 4

# // Đường đi:



# // 1 → 2 → 3 → 4

# // có các cạnh:



# // 9, 5, 7

# // Score của đường đi là



# // min(9,5,7)=5

# // Mục tiêu

# // Tìm score nhỏ nhất có thể của một đường đi từ thành phố 1 đến thành phố n.

# // Lưu ý:



# // Đường đi có thể đi qua một thành phố nhiều lần.

# // Có thể đi qua một cạnh nhiều lần.

# // Ví dụ 1

# // n = 4



# // roads =

# // [

# //  [1,2,9],

# //  [2,3,6],

# //  [2,4,5],

# //  [1,4,7]

# // ]

# // Vẽ đồ thị:



# //       9

# // 1 --------2

# // |         | \

# // |7        |6 \5

# // |         |   \

# // 4---------+

# // Có hai đường đi chính:



# // Đường 1

# // 1 → 4

# // Score



# // =7

# // Đường 2

# // 1 → 2 → 4

# // Các cạnh



# // 9

# // 5

# // Score



# // =min(9,5)=5

# // Đường 3

# // 1 → 2 → 3 → 2 → 4

# // Các cạnh



# // 9

# // 6

# // 6

# // 5

# // Score



# // =min(9,6,6,5)=5

# // Đáp án



# // 5

# // Ví dụ 2

# // 1 --2-- 2 --10--3

# //  \             /

# //   \----1------/

# // Các cạnh



# // 1-2 : 2

# // 2-3 :10

# // 1-3 : 1

# // Nếu đi



# // 1 → 3

# // Score



# // 1

# // Nếu đi



# // 1 →2→3

# // Score



# // min(2,10)=2

# // Ta cần score nhỏ nhất, nên đáp án là



# // 1

# // Điều dễ nhầm nhất

# // Nhiều người tưởng bài yêu cầu:



# // tổng khoảng cách nhỏ nhất (Shortest Path)

# // Sai.

# // Ví dụ



# // 1 --100--2--100--4



# //  \               /

# //   \------1------/

# // Đường



# // 1→4

# // Score



# // 1

# // Đường



# // 1→2→4

# // Score



# // 100

# // Mặc dù đường thứ hai có score lớn hơn, bài lại hỏi score nhỏ nhất, nên đáp án là



# // 1

# // Ý tưởng quan trọng

# // Do được phép đi lặp lại đỉnh và cạnh, nên ta không cần tìm một đường đi "đẹp" hay ngắn nhất.

# // Chỉ cần:



# // Tìm tất cả các thành phố thuộc cùng thành phần liên thông với thành phố 1 (dùng DFS hoặc BFS).

# // Trong toàn bộ các cạnh nằm trong thành phần liên thông đó, lấy trọng số nhỏ nhất.

# // Đó chính là đáp án.



# // Vì sao?

# // Nếu cạnh có trọng số nhỏ nhất nằm trong cùng thành phần liên thông với 1 và n, ta luôn có thể:



# // đi từ 1 đến một đầu của cạnh đó,

# // đi qua cạnh nhỏ nhất,

# // sau đó đi tiếp đến n.

# // Do đề cho phép đi lặp lại đỉnh/cạnh, nên luôn có thể "ghé qua" cạnh nhỏ nhất mà vẫn đến được n.

# // Tóm tắt

# // Score của đường đi = cạnh nhỏ nhất trên đường đi.

# // Không phải tổng trọng số.

# // Do được phép đi lặp lại cạnh và đỉnh, đáp án chính là trọng số nhỏ nhất của mọi cạnh trong thành phần liên thông chứa thành phố 1 (và vì có đường đi đến n, cũng chứa n).

# // Có thể giải bằng DFS, BFS, hoặc Union-Find (DSU) với độ phức tạp khoảng O(n + m), trong đó m là số lượng cạnh.

# // Đây là lời giải sử dụng Union Find (Disjoint Set Union - DSU).

# // Ý tưởng chính là:



# // Mỗi thành phố ban đầu là một tập hợp riêng.

# // Khi đọc một con đường (a, b, d) thì gộp hai tập hợp chứa a và b.

# // Với mỗi tập hợp, lưu lại cạnh có trọng số nhỏ nhất trong tập đó (minEdge).

# // Sau khi đọc hết các cạnh, thành phố 1 và n sẽ thuộc cùng một tập hợp (đề bài đảm bảo có đường đi). Khi đó chỉ cần lấy minEdge của tập chứa thành phố 1.

# // Minh họa

# // Ví dụ



# // n = 4



# // 1 -----9------2

# //        |

# //        6

# //        |

# // 3------5------4

# // Các cạnh



# // (1,2,9)

# // (2,3,6)

# // (3,4,5)

# // Ban đầu



# // parent



# // 1

# // 2

# // 3

# // 4



# // minEdge



# // ∞

# // ∞

# // ∞

# // ∞

# // Đọc cạnh



# // 1 2 9

# // gộp



# // 1

# //  \

# //   2

# // minEdge của tập



# // min(∞,∞,9)=9

# // Đọc



# // 2 3 6

# // gộp



# // 1

# //  \

# //   2

# //    \

# //     3

# // minEdge



# // min(9,∞,6)=6

# // Đọc



# // 3 4 5

# // gộp



# // 1

# //  \

# //   2

# //    \

# //     3

# //      \

# //       4

# // minEdge



# // min(6,∞,5)=5

# // Đáp án



# // 5

# // Giải thích từng hàm

# // 1. parent[]

# // parent[i]

# // Lưu cha của đỉnh i.

# // Ví dụ



# // 1

# //  \

# //   2

# //    \

# //     3

# // thì



# // parent[1]=2

# // parent[2]=3

# // parent[3]=3

# // 2. minEdge[]

# // minEdge[root]

# // Lưu cạnh nhỏ nhất của cả tập hợp.

# // Ví dụ



# // 1---9---2---6---3---5---4

# // thì



# // minEdge = 5

# // Hàm find()

# // private int find(int x)

# // Tìm gốc của tập hợp.

# // Ví dụ



# // 1

# //  \

# //  2

# //   \

# //    3

# // find(1)



# // 1→2→3

# // trả về



# // 3

# // Đồng thời path compression



# // 1

# // |

# // 3

# // để lần sau nhanh hơn.

# // Hàm union()

# // Giả sử đọc cạnh



# // a b d

# // Ví dụ



# // 2 5 8

# // Tìm



# // parentA=find(a)

# // parentB=find(b)

# // Nếu khác nhau



# // parent[parentA]=parentB;

# // gộp hai tập.

# // Sau đó cập nhật



# // minEdge[parentB]

# // =

# // min(

# //     minEdge[parentA],

# //     minEdge[parentB],

# //     d

# // )

# // để lưu cạnh nhỏ nhất của tập mới.

# // Nếu đã cùng tập



# // else

# // thì chỉ cần



# // minEdge[parentA]

# // =

# // min(minEdge[parentA],d);

# // vì xuất hiện thêm một cạnh trong cùng tập.

# // Độ phức tạp

# // Có



# // m cạnh

# // n đỉnh

# // Mỗi lần



# // find()

# // gần như



# // O(1)

# // (do Path Compression)

# // Tổng



# // O(m α(n))

# // với α(n) là hàm Ackermann nghịch đảo (rất nhỏ), gần như tuyến tính.

# // Code đầy đủ (thêm main, dùng Scanner và chú thích)

# import java.util.Scanner;

# public class b266{
  
#     static Scanner sc = new Scanner(System.in);
#     public static void main(String[] args) {
# // Nhập số thành phố

#         int n = sc.nextInt();



#         // Nhập số con đường

#         int m = sc.nextInt();



#         int[][] roads = new int[m][3];



#         // Nhập từng cạnh

#         for (int i = 0; i < m; i++) {

#             roads[i][0] = sc.nextInt(); // thành phố a

#             roads[i][1] = sc.nextInt(); // thành phố b

#             roads[i][2] = sc.nextInt(); // khoảng cách

#         }



        



#         System.out.println(minScore(n, roads));



#         sc.close();

    
#     }
#  public static int[] parent;



#     // minEdge[i] lưu cạnh nhỏ nhất của tập có gốc là i

#     public static int[] minEdge;



#     // Hàm chính giải bài toán

#     public static int minScore(int n, int[][] roads) {



#         parent = new int[n + 1];

#         minEdge = new int[n + 1];



#         // Khởi tạo

#         for (int i = 1; i <= n; i++) {

#             parent[i] = i;                  // mỗi đỉnh là cha của chính nó

#             minEdge[i] = Integer.MAX_VALUE; // chưa có cạnh nào

#         }



#         // Đọc từng cạnh và gộp tập hợp

#         for (int[] road : roads) {

#             union(road[0], road[1], road[2]);

#         }



#         // Lấy gốc của thành phố 1

#         int root = find(1);



#         // Trả về cạnh nhỏ nhất của tập chứa thành phố 1

#         return minEdge[root];

#     }



#     // Tìm gốc của tập hợp (Path Compression)

#     public static int find(int x) {



#         while (parent[x] != x) {

#             // Nén đường đi

#             parent[x] = parent[parent[x]];

#             x = parent[x];

#         }



#         return x;

#     }



#     // Gộp hai tập hợp

#     public static void union(int a, int b, int d) {



#         int rootA = find(a);

#         int rootB = find(b);



#         // Nếu khác tập thì gộp

#         if (rootA != rootB) {



#             parent[rootA] = rootB;



#             // Cập nhật cạnh nhỏ nhất của tập mới

#             minEdge[rootB] = Math.min(

#                     minEdge[rootB],

#                     Math.min(minEdge[rootA], d)

#             );



#         } else {

#             // Nếu đã cùng tập thì chỉ cập nhật cạnh nhỏ nhất

#             minEdge[rootA] = Math.min(minEdge[rootA], d);

#         }

#     }
# }





# // Ví dụ nhập

# // 4

# // 4

# // 1 2 9

# // 2 3 6

# // 2 4 5

# // 1 4 7

# // Kết quả

# // 5

# // Đây là phiên bản có đầy đủ chú thích để bạn dễ theo dõi từng bước của thuật toán DSU (Union-Find).

# Đoạn code trên sử dụng Union-Find (Disjoint Set Union - DSU) để giải bài toán. Ý tưởng giống với phiên bản Java, nhưng Python viết ngắn gọn hơn.

# Ý tưởng thuật toán

# Ta cần tìm:



# Cạnh có trọng số nhỏ nhất trong thành phần liên thông chứa thành phố 1.

# Vì đề bài cho phép đi lặp lại đỉnh và cạnh, nên chỉ cần biết trọng số nhỏ nhất trong toàn bộ thành phần liên thông, không cần tìm đường đi cụ thể.

# Thuật toán gồm các bước:



# Khởi tạo mỗi thành phố là một tập hợp riêng.

# Duyệt tất cả các con đường.

# Với mỗi con đường (u, v, w):

# Gộp hai tập chứa u và v.

# Cập nhật cạnh nhỏ nhất của tập mới.

# Sau khi xử lý xong, lấy gốc của thành phố 1 và trả về cạnh nhỏ nhất của tập đó.

# Giải thích từng phần

# 1. Hàm __init__

# def __init__(self, n):

# Khởi tạo DSU.



# self.parents = list(range(n+1))

# Ban đầu mỗi đỉnh là cha của chính nó.

# Ví dụ



# 1 2 3 4



# parents



# 1

# 2

# 3

# 4

# self.min_weights = [float("inf")] * (n+1)

# Lưu cạnh nhỏ nhất của mỗi tập.

# Lúc đầu chưa có cạnh nên đều là



# ∞

# 2. Hàm find()

# def find(self, x):

# Tìm gốc của tập chứa x.

# Nếu



# 1

#  \

#  2

#   \

#    3

# thì



# find(1)

# sẽ trả về



# 3

# Path Compression

# self.parents[x] = self.find(self.parents[x])

# Sau khi tìm được gốc thì cập nhật luôn cha.

# Ví dụ

# Trước



# 1

#  \

#  2

#   \

#    3

# Sau khi gọi find(1)



# 1

# |

# 3



# 2

# |

# 3

# Lần sau tìm sẽ nhanh hơn.

# 3. Hàm union()

# def union(self, x, y, weight):

# Ví dụ đọc cạnh



# 2 5 8

# Bước 1

# Tìm gốc



# x = self.find(x)

# y = self.find(y)

# Giả sử



# 2 thuộc tập A



# 5 thuộc tập B

# Bước 2

# Tính cạnh nhỏ nhất sau khi gộp



# new_weight = min(

#     self.min_weights[x],

#     self.min_weights[y],

#     weight

# )

# Ví dụ



# Tập A nhỏ nhất = 9



# Tập B nhỏ nhất = 6



# Cạnh mới = 8

# thì



# new_weight



# =min(9,6,8)



# =6

# Nếu khác tập

# if x != y:

# Gộp



# self.parents[x] = y

# Ví dụ



# 1



# 2

# thành



# 1

#  \

#   2

# Cập nhật



# self.min_weights[y] = new_weight

# Tập mới có cạnh nhỏ nhất.

# Nếu cùng tập

# else:

# Không cần gộp nữa.

# Chỉ cập nhật



# self.min_weights[x] = new_weight

# vì xuất hiện thêm một cạnh nhỏ hơn.

# 4. Hàm minScore()

# uf = UnionFind(n)

# Tạo DSU.

# Duyệt toàn bộ cạnh



# for u, v, w in roads:

#     uf.union(u, v, w)

# Ví dụ



# 1 2 9



# 2 3 6



# 3 4 5

# sau khi chạy



# 1

#  \

#  2

#   \

#    3

#     \

#      4

# và



# minWeight



# 5

# Cuối cùng



# return uf.min_weights[uf.find(1)]

# Tìm gốc của thành phố 1.

# Lấy cạnh nhỏ nhất của tập đó.

# Minh họa

# Ví dụ



# 1 --9--2



# 2 --6--3



# 3 --5--4

# Ban đầu



# parents



# 1

# 2

# 3

# 4



# min



# ∞

# ∞

# ∞

# ∞

# Sau cạnh



# 1 2 9

# 1

#  \

#  2



# min = 9

# Sau cạnh



# 2 3 6

# 1

#  \

#  2

#   \

#    3



# min = 6

# Sau cạnh



# 3 4 5

# 1

#  \

#  2

#   \

#    3

#     \

#      4



# min = 5

# Đáp án



# 5

# Code có chú thích

class UnionFind:



    def __init__(self, n):

        # Ban đầu mỗi đỉnh là cha của chính nó

        self.parents = list(range(n + 1))



        # min_weights[i] lưu cạnh nhỏ nhất của tập có gốc là i

        self.min_weights = [float("inf")] * (n + 1)



    def find(self, x):

        """

        Tìm gốc của tập chứa x.

        Áp dụng Path Compression để tăng tốc.

        """

        if x != self.parents[x]:

            self.parents[x] = self.find(self.parents[x])

        return self.parents[x]



    def union(self, x, y, weight):

        """

        Gộp hai tập chứa x và y.

        Đồng thời cập nhật cạnh nhỏ nhất của tập mới.

        """



        # Tìm gốc của hai tập

        x = self.find(x)

        y = self.find(y)



        # Cạnh nhỏ nhất sau khi gộp

        new_weight = min(

            self.min_weights[x],

            self.min_weights[y],

            weight

        )



        # Nếu hai đỉnh thuộc hai tập khác nhau

        if x != y:



            # Gộp tập x vào tập y

            self.parents[x] = y



            # Cập nhật cạnh nhỏ nhất

            self.min_weights[y] = new_weight



            return True



        else:

            # Nếu đã cùng tập thì chỉ cập nhật cạnh nhỏ nhất

            self.min_weights[x] = new_weight



            return False





class Solution:



    def minScore(self, n: int, roads: list[list[int]]) -> int:



        # Khởi tạo Union Find

        uf = UnionFind(n)



        # Duyệt tất cả các con đường

        for u, v, w in roads:

            uf.union(u, v, w)



        # Lấy gốc của thành phố 1

        root = uf.find(1)



        # Trả về cạnh nhỏ nhất của thành phần liên thông chứa thành phố 1

        return uf.min_weights[root]

# Độ phức tạp

# Thời gian: (O(m \cdot \alpha(n))), với m là số cạnh và (\alpha(n)) là hàm Ackermann nghịch đảo (rất nhỏ, gần như hằng số).

# Bộ nhớ: (O(n)) cho hai mảng parents và min_weights.