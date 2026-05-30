# // // Bài Block Placement Queries (30/05/2026)

# // // Có 2 loại truy vấn:



# // // Loại 1: [1, x]

# // // Đặt một vật cản (obstacle) tại vị trí x.

# // // Ví dụ:



# // // [1, 2]

# // // => Có một vật cản ở vị trí 2.

# // // Loại 2: [2, x, sz]

# // // Kiểm tra xem có thể đặt một khối (block) độ dài sz trong đoạn [0, x] hay không.

# // // Điều kiện:



# // // Khối phải nằm hoàn toàn trong [0, x].

# // // Khối không được đè lên vật cản.

# // // Khối được phép chạm vật cản.

# // // Ví dụ:



# // // Obstacle ở vị trí 2

# // // 0 ---- 1 ---- 2 ---- 3

# // //              ^

# // //          obstacle

# // // Truy vấn:



# // // [2, 3, 1]

# // // Cần đặt block dài 1.

# // // Ta có thể đặt:



# // // [0,1]

# // // hoặc



# // // [2,3]

# // // (vì chỉ chạm vật cản tại đầu mút, không cắt qua nó)

# // // => Kết quả true.

# // // Giải thích Example 1

# // // queries =

# // // [

# // //  [1,2],

# // //  [2,3,3],

# // //  [2,3,1],

# // //  [2,2,2]

# // // ]

# // // Query 1

# // // [1,2]

# // // Đặt obstacle tại 2.



# // // 0 ---- 1 ---- 2 ---- 3

# // //              ^

# // // Query 2

# // // [2,3,3]

# // // Cần block dài 3 trong đoạn [0,3].

# // // Các khoảng trống là:



# // // [0,2]  dài 2

# // // [2,3]  dài 1

# // // Không có đoạn nào dài ≥ 3.

# // // => false

# // // Query 3

# // // [2,3,1]

# // // Cần block dài 1.

# // // Có nhiều chỗ đặt được.

# // // => true

# // // Query 4

# // // [2,2,2]

# // // Trong đoạn [0,2].

# // // Khoảng:



# // // [0,2]

# // // có độ dài 2.

# // // Block được phép chạm obstacle tại vị trí 2.

# // // => true

# // // Kết quả:



# // // [false, true, true]

# // // Ý tưởng chính của bài

# // // Với mỗi truy vấn loại 2:



# // // [2, x, sz]

# // // Ta chỉ cần biết:



# // // Trong đoạn [0, x], khoảng trống lớn nhất giữa các vật cản là bao nhiêu?

# // // Nếu:



# // // max_gap >= sz

# // // thì trả về true, ngược lại false.

# // // Đây là lý do bài này thường được giải bằng Sorted Set + Segment Tree/Fenwick Tree để cập nhật và truy vấn khoảng trống nhanh khi số lượng query lên tới 150000. (Walkccc)

# // // Nếu muốn, mình có thể vẽ hình từng bước của ví dụ hoặc giải thích luôn cách nghĩ ra lời giải O(n log n).

# // // Mình giải thích theo cách trực quan hơn.

# // // ### Hãy tưởng tượng một con đường

# // // ```text
# // // 0 1 2 3 4 5 6 7 8 9 ...
# // // ```

# // // Ban đầu **không có vật cản nào**.

# // // ---

# // // ## Query loại 1: `[1, x]`

# // // Nghĩa là:

# // // > Đặt một cọc chắn ở vị trí `x`.

# // // Ví dụ:

# // // ```text
# // // [1, 4]
# // // ```

# // // Sau đó đường sẽ như:

# // // ```text
# // // 0 1 2 3 4 5 6
# // //         |
# // //       obstacle
# // // ```

# // // ---

# // // ## Query loại 2: `[2, x, sz]`

# // // Nghĩa là:

# // // > Trong đoạn từ `0` đến `x`, có đặt được một thanh dài `sz` không?

# // // Thanh này không được đi xuyên qua vật cản.

# // // ---

# // // ### Ví dụ 1

# // // Đã có vật cản ở vị trí 4:

# // // ```text
# // // 0 1 2 3 4 5 6
# // //         |
# // // ```

# // // Query:

# // // ```text
# // // [2, 6, 3]
# // // ```

# // // Hỏi:

# // // > Trong đoạn `[0,6]` có đặt được thanh dài 3 không?

# // // Ta đặt được từ 0 đến 3:

# // // ```text
# // // [=========]
# // // 0 1 2 3 4 5 6
# // //         |
# // // ```

# // // => **True**

# // // ---

# // // ### Ví dụ 2

# // // Vẫn vật cản ở 4.

# // // Query:

# // // ```text
# // // [2, 6, 5]
# // // ```

# // // Thanh dài 5.

# // // Bên trái vật cản chỉ có:

# // // ```text
# // // 0 -> 4
# // // ```

# // // độ dài 4.

# // // Bên phải:

# // // ```text
# // // 4 -> 6
# // // ```

# // // độ dài 2.

# // // Không chỗ nào dài 5.

# // // => **False**

# // // ---

# // // ## Điều gây nhầm lẫn nhất

# // // Đề nói:

# // // > Block can touch an obstacle.

# // // Nghĩa là:

# // // Thanh được phép chạm vật cản.

# // // Ví dụ:

# // // ```text
# // // Obstacle ở 4
# // // ```

# // // Thanh:

# // // ```text
# // // 0 1 2 3 4
# // // [=======]
# // //         |
# // // ```

# // // Đầu thanh chạm đúng vị trí 4.

# // // Điều này **được phép**.

# // // ---

# // // ## Ví dụ trong đề

# // // ```text
# // // [1,2]
# // // ```

# // // Đặt vật cản ở 2.

# // // ```text
# // // 0 1 2 3
# // //     |
# // // ```

# // // ---

# // // Query:

# // // ```text
# // // [2,3,3]
# // // ```

# // // Hỏi có đặt được thanh dài 3 trong đoạn `[0,3]` không?

# // // Nếu đặt từ 0 đến 3:

# // // ```text
# // // 0 1 2 3
# // // [=====]
# // //     |
# // // ```

# // // Thanh đi xuyên qua vật cản ở 2.

# // // Không được.

# // // Không còn vị trí nào khác.

# // // => **False**

# // // ---

# // // Query:

# // // ```text
# // // [2,3,1]
# // // ```

# // // Thanh dài 1.

# // // Đặt từ 0 đến 1:

# // // ```text
# // // [=]
# // // 0 1 2 3
# // //     |
# // // ```

# // // Được.

# // // => **True**

# // // ---

# // // Query:

# // // ```text
# // // [2,2,2]
# // // ```

# // // Đoạn xét là `[0,2]`.

# // // Đặt thanh từ 0 đến 2:

# // // ```text
# // // 0 1 2
# // // [===]
# // //     |
# // // ```

# // // Thanh chỉ **chạm** vật cản tại đầu mút.

# // // Đề cho phép.

# // // => **True**

# // // ---

# // // Mấu chốt của bài:

# // // * Query loại 1: thêm vật cản.
# // // * Query loại 2: tìm xem trong `[0,x]` có **khoảng trống liên tục** nào dài ít nhất `sz` hay không.
# // // * Chạm vật cản thì được, đi xuyên qua vật cản thì không được.

# // // Nếu bạn đang làm LeetCode 3161, mình có thể vẽ hình minh họa cho chính ví dụ Input của đề để thấy tại sao đáp án là `[false,true,true]`.

# // Đoạn code này dùng một Segment Tree động (Dynamic Segment Tree) để quản lý các vật cản (obstacles) và trả lời truy vấn đặt block.

# // Ý tưởng của Node

# // Mỗi node quản lý một đoạn:



# // [start, end]

# // Ví dụ:



# // [0,7]



# //       [0,7]

# //      /     \

# //  [0,3]    [4,7]

# // Mỗi node lưu:



# // int nearestObstacle;

# // Vật cản gần nhất nằm bên phải đoạn này.

# // Ví dụ:



# // Obstacle tại 10



# // Đoạn [0,3]

# // nearestObstacle = 10

# // int maxFreeSpace;

# // Khoảng trống lớn nhất có thể đặt block trong đoạn này.

# // Ví dụ:



# // Đoạn [0,3]

# // Obstacle gần nhất = 10



# // maxFreeSpace = 10 - 0 = 10

# // Hàm addObstacle()

# // Khi gặp query:



# // [1,x]

# // ta thêm vật cản tại vị trí x.

# // Ví dụ:



# // [1,5]

# // Ban đầu:



# // 0--------------------∞



# // nearestObstacle = ∞

# // Sau khi thêm obstacle 5:



# // 0-----5---------∞

# //       ^

# // mọi đoạn bên trái phải cập nhật:



# // nearestObstacle = 5

# // Đoạn này

# // if (obstaclePosition > root.end)

# // nghĩa là:



# // Obstacle nằm bên phải node hiện tại

# // Ví dụ:



# // Node [0,3]



# // Obstacle = 5

# // thì:



# // nearestObstacle = 5

# // Hàm isBlockPlaceable()

# // Kiểm tra query:



# // [2,x,size]

# // Ví dụ:



# // [2,7,2]

# // nghĩa là:



# // Có đặt block dài 2 trong [0,7] được không?

# // Code đổi thành:



# // int blockStart = x - size;

# // Ví dụ:



# // 7 - 2 = 5

# // Tức là:



# // Muốn biết có vị trí bắt đầu nào ≤ 5 hay không

# // Trường hợp node lá

# // if (root.leftChild == null &&

# //     root.rightChild == null)

# // Ví dụ:



# // [3,3]

# // Nếu:



# // blockSize <= root.maxFreeSpace

# // thì:



# // đặt được block

# // Ví dụ chạy chương trình

# // Input:



# // queries = {

# //     {1,5},

# //     {2,7,2},

# //     {2,6,2}

# // };

# // Query 1

# // {1,5}

# // Obstacle:



# // 0----5------∞

# // Query 2

# // {2,7,2}

# // Đặt block dài 2 trong:



# // [0,7]

# // Ta có:



# // 0----5----7

# // Khoảng:



# // [0,5]

# // dài 5.

# // Đặt được block dài 2.



# // [==]

# // 0 1

# // → true

# // Query 3

# // {2,6,2}

# // Khoảng:



# // 0----5----6

# // Vẫn có đoạn dài hơn 2.

# // → true

# // Phiên bản có Scanner + chú thích

# // import java.util.*;



# // public class Main {



# //     static class Solution {



# //         class SegmentTreeNode {



# //             // Con trái

# //             SegmentTreeNode leftChild;



# //             // Con phải

# //             SegmentTreeNode rightChild;



# //             // Đầu đoạn

# //             int start;



# //             // Cuối đoạn

# //             int end;



# //             // Khoảng trống lớn nhất trong đoạn

# //             int maxFreeSpace;



# //             // Vật cản gần nhất bên phải

# //             int nearestObstacle;



# //             SegmentTreeNode(int start, int end, int obstaclePosition) {

# //                 this.start = start;

# //                 this.end = end;



# //                 nearestObstacle = obstaclePosition;



# //                 if (obstaclePosition == Integer.MAX_VALUE)

# //                     maxFreeSpace = Integer.MAX_VALUE;

# //                 else

# //                     maxFreeSpace = obstaclePosition - start;

# //             }

# //         }



# //         public List<Boolean> getResults(int[][] queries) {



# //             int maxRange = 0;



# //             // Tìm obstacle lớn nhất

# //             for (int[] query : queries) {

# //                 if (query[0] == 1) {

# //                     maxRange = Math.max(maxRange, query[1]);

# //                 }

# //             }



# //             SegmentTreeNode root =

# //                     new SegmentTreeNode(

# //                             0,

# //                             maxRange,

# //                             Integer.MAX_VALUE);



# //             List<Boolean> result = new ArrayList<>();



# //             for (int[] query : queries) {



# //                 // Thêm obstacle

# //                 if (query[0] == 1) {



# //                     addObstacle(root, query[1]);



# //                 } else {



# //                     int x = query[1];

# //                     int size = query[2];



# //                     int blockStart = x - size;



# //                     if (blockStart >= root.end) {

# //                         result.add(true);

# //                     } else {

# //                         result.add(

# //                                 isBlockPlaceable(

# //                                         root,

# //                                         blockStart,

# //                                         size));

# //                     }

# //                 }

# //             }



# //             return result;

# //         }



# //         boolean isBlockPlaceable(

# //                 SegmentTreeNode root,

# //                 int blockStart,

# //                 int blockSize) {



# //             if (root.leftChild == null &&

# //                     root.rightChild == null) {



# //                 if (blockStart >= root.end) {



# //                     return blockSize <= root.maxFreeSpace;



# //                 } else if (blockStart < root.start) {



# //                     return false;



# //                 } else {



# //                     return blockSize <=

# //                             (root.nearestObstacle - root.start);

# //                 }

# //             }



# //             if (root.rightChild.end <= blockStart) {



# //                 if (root.rightChild.maxFreeSpace >= blockSize)

# //                     return true;

# //             }



# //             if (root.leftChild.end <= blockStart) {



# //                 if (root.leftChild.maxFreeSpace >= blockSize)

# //                     return true;



# //             } else {



# //                 return isBlockPlaceable(

# //                         root.leftChild,

# //                         blockStart,

# //                         blockSize);

# //             }



# //             if (root.rightChild.start <= blockStart &&

# //                     root.rightChild.end >= blockStart) {



# //                 return isBlockPlaceable(

# //                         root.rightChild,

# //                         blockStart,

# //                         blockSize);

# //             }



# //             return false;

# //         }



# //         int addObstacle(

# //                 SegmentTreeNode root,

# //                 int obstaclePosition) {



# //             if (root.end == root.start) {



# //                 if (root.end < obstaclePosition &&

# //                         obstaclePosition < root.nearestObstacle) {



# //                     root.nearestObstacle =

# //                             obstaclePosition;

# //                 }



# //                 if (root.nearestObstacle ==

# //                         Integer.MAX_VALUE)



# //                     root.maxFreeSpace =

# //                             Integer.MAX_VALUE;

# //                 else



# //                     root.maxFreeSpace =

# //                             root.nearestObstacle

# //                                     - root.start;



# //                 return root.maxFreeSpace;

# //             }



# //             if (obstaclePosition <= root.start)

# //                 return root.maxFreeSpace;



# //             if (obstaclePosition > root.end) {



# //                 if (obstaclePosition

# //                         < root.nearestObstacle) {



# //                     root.nearestObstacle =

# //                             obstaclePosition;



# //                     if (root.leftChild == null) {



# //                         root.maxFreeSpace =

# //                                 obstaclePosition

# //                                         - root.start;



# //                     } else {



# //                         root.maxFreeSpace =

# //                                 Math.max(

# //                                         addObstacle(

# //                                                 root.leftChild,

# //                                                 obstaclePosition),

# //                                         addObstacle(

# //                                                 root.rightChild,

# //                                                 obstaclePosition));

# //                     }

# //                 }



# //                 return root.maxFreeSpace;

# //             }



# //             if (root.leftChild != null) {



# //                 root.maxFreeSpace =

# //                         Math.max(

# //                                 addObstacle(

# //                                         root.leftChild,

# //                                         obstaclePosition),

# //                                 addObstacle(

# //                                         root.rightChild,

# //                                         obstaclePosition));



# //                 return root.maxFreeSpace;

# //             }



# //             int mid =

# //                     (root.start + root.end) / 2;



# //             root.leftChild =

# //                     new SegmentTreeNode(

# //                             root.start,

# //                             mid,

# //                             root.nearestObstacle);



# //             root.rightChild =

# //                     new SegmentTreeNode(

# //                             mid + 1,

# //                             root.end,

# //                             root.nearestObstacle);



# //             root.maxFreeSpace =

# //                     Math.max(

# //                             addObstacle(

# //                                     root.leftChild,

# //                                     obstaclePosition),

# //                             addObstacle(

# //                                     root.rightChild,

# //                                     obstaclePosition));



# //             return root.maxFreeSpace;

# //         }

# //     }



# //     public static void main(String[] args) {



# //         Scanner sc = new Scanner(System.in);



# //         int n = sc.nextInt();



# //         int[][] queries = new int[n][];



# //         for (int i = 0; i < n; i++) {



# //             int type = sc.nextInt();



# //             if (type == 1) {



# //                 queries[i] =

# //                         new int[]{

# //                                 type,

# //                                 sc.nextInt()

# //                         };



# //             } else {



# //                 queries[i] =

# //                         new int[]{

# //                                 type,

# //                                 sc.nextInt(),

# //                                 sc.nextInt()

# //                         };

# //             }

# //         }



# //         Solution solution = new Solution();



# //         List<Boolean> answer =

# //                 solution.getResults(queries);



# //         System.out.println(answer);



# //         sc.close();

# # //     }

# # // }

# # // ⚠️ Tuy nhiên cần lưu ý: đây không phải lời giải chuẩn tối ưu của LeetCode 3161. Lời giải được chấp nhận phổ biến thường dùng TreeSet + Segment Tree/Fenwick Tree + Offline Processing với độ phức tạp O(q log q). Đoạn code này là một cách cài đặt riêng bằng Dynamic Segment Tree và khá khó hiểu vì lưu nearestObstacle thay vì lưu trực tiếp các khoảng trống.



# Đây là lời giải cho bài toán Block Placement Queries (LeetCode 3161) sử dụng kỹ thuật:



# Offline Query Processing (xử lý truy vấn ngược từ cuối lên đầu)

# SortedDict để tìm obstacle gần nhất bên trái trong O(log n)

# Linked List để cập nhật nhanh khi xóa obstacle

# Maximum Gap Structure để lưu các khoảng trống lớn nhất đã xuất hiện

# Ý tưởng tổng quát

# Giả sử có các obstacle:



# 0    3      8      15

# |----|------|------|

# Các khoảng trống:



# 0 -> 3  = 3

# 3 -> 8  = 5

# 8 -> 15 = 7

# Nếu muốn đặt block kích thước size trong đoạn [0,x]:

# Ta chỉ cần biết:



# Có khoảng trống nào trước x có độ dài ≥ size không?

# Hoặc khoảng từ obstacle gần nhất đến x có đủ lớn không?

# Tại sao xử lý ngược?

# Query loại 1:



# [1, x]

# là thêm obstacle.

# Thay vì thêm obstacle rất khó cập nhật max gap.

# Ta:



# Thu thập toàn bộ obstacle trước.

# Xây cấu trúc với tất cả obstacle đã tồn tại.

# Duyệt ngược query.

# Lúc này:



# add obstacle

# trở thành



# remove obstacle

# dễ xử lý hơn.

# Lớp Obstacle

# class Obstacle:

# Mỗi node vừa dùng cho:



# obstacles_tree

# vừa dùng cho:



# obstacles_max_gaps

# Constructor

# def __init__(self, x, max_gap, previous):

# self.x = x

# tọa độ obstacle



# self.max_gap = max_gap

# max gap tính đến obstacle này



# self.previous

# self.next

# tạo doubly linked list.

# remove()

# def remove(self):

# Xóa node khỏi linked list.

# Trước:



# A <-> B <-> C

# Xóa B:



# A <-> C

# self.previous.next = self.next

# if self.next:

#     self.next.previous = self.previous

# Khởi tạo dữ liệu

# obstacles.sort()

# Sắp xếp tất cả obstacle.

# obstacle list

# 0 -> 3 -> 8 -> 15

# được lưu trong



# obstacles_tree

# để tìm predecessor bằng:



# irange(maximum=x, reverse=True)

# max gap list

# Ví dụ:



# 0 3 8 15

# Gap:



# 3,5,7

# Các mốc tạo max gap mới:



# 3

# 5

# 7

# Ta lưu:



# [0:0] -> [3:3] -> [8:5] -> [15:7]

# trong



# obstacles_max_gaps

# Hàm can_place()

# def can_place(...)

# Kiểm tra query:



# [2, x, size]

# Bước 1

# Tìm obstacle max-gap gần nhất bên trái của x



# previous_obstacle_max_gap =

#     obstacles_max_gaps.get(

#         next(

#             obstacles_max_gaps.irange(

#                 maximum=x,

#                 reverse=True

#             ),

#             None

#         )

#     )

# Ví dụ:



# [3:3] -> [8:5] -> [15:7]

# Nếu:



# x = 12

# ta lấy:



# [8:5]

# Bước 2

# Nếu max gap trước đó đủ lớn



# if previous_obstacle_max_gap.max_gap >= size:

#     return True

# thì chắc chắn đặt được.

# Bước 3

# Kiểm tra đoạn cuối cùng



# previous_obstacle =

#     obstacle_tree.get(...)

# Obstacle gần nhất bên trái x.

# Ví dụ:



# 0---3-----8----12

# Obstacle gần nhất:



# 8

# Gap cuối:



# 12 - 8 = 4

# Nếu



# 4 >= size

# thì đặt được.

# Hàm remove()

# Khi duyệt ngược.

# Ví dụ ban đầu:



# 0 --- 3 --- 8 --- 15

# Xóa obstacle:



# 8

# thành:



# 0 --- 3 -------- 15

# Gap mới:



# 15 - 3 = 12

# Xóa khỏi obstacle tree

# obstacle_to_remove =

#     obstacle_treemap.pop(x)

# Xóa khỏi linked list

# next_obstacle =

#     obstacle_to_remove.remove()

# Xóa khỏi max-gap tree

# obstacles_max_gaps.pop(x, None)

# Nếu obstacle đó là một mốc max-gap.

# Tính gap mới

# new_gap =

#     next_obstacle.x -

#     next_obstacle.previous.x

# Ví dụ:



# 3 ----- 15

# new_gap = 12

# Nếu gap mới lớn hơn max gap trước đó

# if previous_obstacle_max_gap.max_gap < new_gap:

# thì cần cập nhật.

# Loại bỏ các max-gap nhỏ hơn

# while (

#     next_obstacle_max_gap is not None

#     and

#     next_obstacle_max_gap.max_gap <= new_gap

# ):

# Ví dụ:



# 3

# 5

# 7

# 10

# Gap mới:



# 12

# thì:



# 5

# 7

# 10

# đều vô dụng.

# Xóa hết.

# Chèn node mới

# new_node =

#     Obstacle(

#         gap_x,

#         new_gap,

#         previous_node

#     )

# Ví dụ:



# [3:3] -> [15:12]

# Code đã thêm chú thích


class Obstacle:

    def __init__(self, x: int, max_gap: int, previous):

        # Tọa độ obstacle

        self.x = x



        # Max gap tính đến obstacle này

        self.max_gap = max_gap



        # Node trước trong linked list

        self.previous = previous



        # Node sau trong linked list

        self.next = None



    def deep_print(self):

        if self.next is not None:

            print(f"[{self.x}:{self.max_gap}] ->", end=" ")

            self.next.deep_print()

        else:

            print(f"[{self.x}:{self.max_gap}]")



    def remove(self):

        # Xóa node khỏi doubly linked list

        self.previous.next = self.next



        if self.next is not None:

            self.next.previous = self.previous



        return self.next





class Solution:
    def can_place(

        self,

        obstacles_tree,

        obstacles_max_gaps,

        x,

        size

    ):

        # Lấy max-gap node gần nhất bên trái x

        previous_obstacle_max_gap = obstacles_max_gaps.get(

            next(

                obstacles_max_gaps.irange(

                    maximum=x,

                    reverse=True

                ),

                None

            )

        )



        # Nếu đã có gap đủ lớn

        if previous_obstacle_max_gap.max_gap >= size:

            return True



        # Tìm obstacle gần nhất bên trái x

        previous_obstacle = obstacles_tree.get(

            next(

                obstacles_tree.irange(

                    maximum=x,

                    reverse=True

                ),

                None

            )

        )



        # Kiểm tra đoạn cuối cùng

        if x - previous_obstacle.x >= size:

            return True



        return False



    def remove(

        self,

        obstacle_treemap,

        obstacles_max_gaps,

        x

    ):

        # Lấy obstacle cần xóa

        obstacle_to_remove = obstacle_treemap.pop(x)



        # Xóa khỏi linked list

        next_obstacle = obstacle_to_remove.remove()



        # Xóa khỏi max-gap tree nếu tồn tại

        obstacle_max_gap_to_remove = obstacles_max_gaps.pop(x, None)



        if obstacle_max_gap_to_remove is not None:

            obstacle_max_gap_to_remove.remove()



        # Nếu còn obstacle bên phải

        if next_obstacle is not None:



            # Gap mới sau khi xóa

            new_gap = (

                next_obstacle.x

                - next_obstacle.previous.x

            )



            gap_x = next_obstacle.x



            # Max gap gần nhất bên trái

            previous_obstacle_max_gap = obstacles_max_gaps.get(

                next(

                    obstacles_max_gaps.irange(

                        maximum=x,

                        reverse=True

                    ),

                    None

                )

            )



            # Nếu tạo max-gap mới

            if previous_obstacle_max_gap.max_gap < new_gap:



                next_obstacle_max_gap = (

                    previous_obstacle_max_gap.next

                )



                # Xóa các max-gap nhỏ hơn

                while (

                    next_obstacle_max_gap is not None

                    and

                    next_obstacle_max_gap.max_gap <= new_gap

                ):

                    obstacles_max_gaps.pop(

                        next_obstacle_max_gap.x

                    )



                    next_obstacle_max_gap = (

                        next_obstacle_max_gap.remove()

                    )



                # Chèn node max-gap mới

                previous_node = previous_obstacle_max_gap

                next_node = next_obstacle_max_gap



                new_node = Obstacle(

                    gap_x,

                    new_gap,

                    previous_node

                )



                previous_node.next = new_node

                new_node.next = next_node



                if next_node is not None:

                    next_node.previous = new_node



                obstacles_max_gaps[

                    new_node.x

                ] = new_node

# Độ phức tạp

# Khởi tạo: O(n log n)

# Query loại 2: O(log n)

# Query loại 1 (xử lý ngược = remove): O(log n) amortized

# Tổng: O((n + q) log n)

# Đây là lời giải tối ưu để vượt giới hạn của bài LeetCode 3161 - Block Placement Queries.