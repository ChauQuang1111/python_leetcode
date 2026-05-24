# // // Jump Game Jump Game V (24/05/2026)
# // // Đề bài

# // // Cho:



# // // Một mảng arr

# // // Một số nguyên d

# // // Bạn đang đứng ở mỗi vị trí i trong mảng.

# // // Từ vị trí i, bạn có thể nhảy sang trái hoặc phải tối đa d bước.

# // // Nhưng chỉ được nhảy nếu:



# // // arr[j] < arr[i]

# // // → ô đích phải nhỏ hơn ô hiện tại

# // // Trên đường đi không có phần tử nào lớn hơn hoặc bằng arr[i]

# // // Nghĩa là:



# // // Nếu nhảy từ i → j

# // // Thì mọi phần tử ở giữa phải:

# // // [

# // // arr[k] < arr[i]

# // // ]

# // // Mục tiêu

# // // Tìm số vị trí nhiều nhất có thể ghé qua khi bắt đầu từ bất kỳ vị trí nào.

# // // Ví dụ

# // // arr = [6,4,14,6,8,13,9,7,10,6,12]

# // // d = 2

# // // Ví dụ đứng ở:



# // // i = 2

# // // arr[i] = 14

# // // Có thể nhảy:



# // // sang trái:

# // // 4 ✔

# // // 6 ✔

# // // sang phải:

# // // 6 ✔

# // // 8 ✔

# // // Vì tất cả đều nhỏ hơn 14.

# // // Ví dụ không nhảy được

# // // arr = [3,2,5,1]

# // // d = 2

# // // Đứng ở 5:

# // // Muốn nhảy tới 1



# // // 5 -> 1

# // // Nhưng giữa chúng có:



# // // 2

# // // À không sao vì 2 < 5.

# // // Nên nhảy được ✔

# // // Ví dụ khác:



# // // arr = [3,2,5,6,1]

# // // Đứng ở 5 muốn nhảy tới 1

# // // Nhưng giữa có:



# // // 6

# // // Vì:



# // // 6 >= 5

# // // nên bị chặn ❌

# // // Ý tưởng bài toán

# // // Mỗi vị trí:



# // // thử nhảy trái

# // // thử nhảy phải

# // // tìm đường đi dài nhất

# // // Bài này thường dùng:



# // // DFS + Memoization

# // // Dynamic Programming

# // // Công thức

# // // Gọi:



# // // dp[i]

# // // = số vị trí tối đa có thể đi được nếu bắt đầu từ i

# // // Ta có:



# // // dp[i] = 1 + max(dp[j])

# // // với mọi vị trí j nhảy được từ i.

# // // Hình dung trực quan

# // // Ví dụ:



# // // [7,6,5,4]

# // // d = 1

# // // Có thể:



# // // 7 -> 6 -> 5 -> 4

# // // Độ dài lớn nhất = 4

# // // Điểm khó của bài

# // // Phải dừng khi:



# // // arr[next] >= arr[current]

# // // vì nó chặn đường nhảy tiếp.

# // // Nếu muốn, mình có thể giải tiếp:



# // // DFS memo hoạt động thế nào

# // // code Java/Python

# // // dry run từng bước

# // // tại sao dùng memo

# // // độ phức tạp bài này


# // Thuật toán này dùng:



# // DFS (đệ quy) để thử nhảy

# // Memoization (DP) để lưu kết quả đã tính

# // Mục tiêu:



# // Từ mỗi vị trí i, tìm số bước nhảy nhiều nhất có thể.

# // Ý tưởng chính

# // Ta định nghĩa:



# // dp[i] = số vị trí tối đa có thể đi được nếu bắt đầu từ i

# // Ví dụ:



# // 7 -> 6 -> 5 -> 4

# // thì:



# // dp[0] = 4

# // Hàm chính

# // public int maxJumps(int[] arr, int d)

# // Khởi tạo

# // int[] maxJumpsFromHere = new int[arr.length];

# // Mảng DP:



# // maxJumpsFromHere[i] = dp[i]

# // Ban đầu toàn 0 nghĩa là chưa tính.

# // Thử bắt đầu từ mọi vị trí

# // for (int i=0; i<arr.length; i++) {

# //     maxJumps = Math.max(maxJumps,

# //         calMaxJumps(i, maxJumpsFromHere, arr, d));

# // }

# // Vì đề bài cho phép bắt đầu ở bất kỳ index nào.

# // DFS + Memo

# // Hàm:

# // calMaxJumps(i)

# // Ý nghĩa:



# // Tìm số vị trí tối đa đi được nếu bắt đầu từ i

# // Bước 1: kiểm tra memo

# // if (maxJumpsFromHere[i] != 0)

# //     return maxJumpsFromHere[i];

# // Nếu đã tính rồi thì trả về luôn.

# // Giúp tránh tính lặp.

# // Bước 2: thử nhảy sang phải

# // for (int x = i+1; x <= (i+d) && x < arr.length; x++)

# // Thử mọi vị trí bên phải trong khoảng d.

# // Điều kiện chặn

# // if (arr[x] >= arr[i])

# //     break;

# // Theo đề:



# // Không được nhảy qua hoặc nhảy tới phần tử >= arr[i]

# // Nên gặp phần tử lớn hơn hoặc bằng thì:



# // không nhảy được

# // các vị trí phía sau cũng bị chặn luôn

# // => break

# // Nếu nhảy được

# // maxJumpsCount = Math.max(

# //     maxJumpsCount,

# //     calMaxJumps(x, ...)

# // );

# // Ta DFS tiếp từ vị trí mới.

# // Lấy đường dài nhất.

# // Bước 3: thử nhảy sang trái

# // Tương tự:



# // for (int x = i-1; x >= (i-d) && x >= 0; x--)

# // Bước 4: lưu kết quả

# // maxJumpsFromHere[i] = 1 + maxJumpsCount;

# // 1 là tính luôn vị trí hiện tại.

# // Ví dụ:



# // i -> a -> b

# // thì số vị trí là:



# // 1 + dp[a]

# // Ví dụ Dry Run

# // arr = [6,4,14,6,8]

# // d = 2

# // Tính dp[0]

# // 6

# // // Có thể nhảy tới:



# // // 4

# // // nên:



# // // dp[0] = 1 + dp[1]

# // // Tính dp[1]

# // // 4

# // // Không nhảy đâu được.

# // // Nên:



# // // dp[1] = 1

# // // Quay lại:



# // // dp[0] = 1 + 1 = 2

# // // Vì sao dùng DFS?

# // // Vì:



# // // Từ i phụ thuộc vào các vị trí tiếp theo

# // // Đây là dạng:



# // // explore all paths

# // // rất hợp với DFS.

# // // Vì sao cần memo?

# // // Nếu không memo:



# // // dp[x]

# // // sẽ bị tính đi tính lại rất nhiều lần.

# // // Memo giúp:



# // // Mỗi index chỉ tính đúng 1 lần

# // // Độ phức tạp

# // // Có n vị trí.

# // // Mỗi vị trí thử tối đa 2d bước.

# // // Nên:



# // // Time: O(n * d)

# // // Space:



# // // O(n)

# // // Công thức DP

# // // [

# // // dp[i] = 1 + \max(dp[j])

# // // ]

# // // với mọi j:



# // // nằm trong khoảng d

# // // arr[j] < arr[i]

# // // không bị chặn bởi phần tử lớn hơn hoặc bằng arr[i]

# // // Điểm quan trọng nhất

# // // Dòng này:



# // // if (arr[x] >= arr[i])

# // //     break;

# // // là linh hồn bài toán.

# // // Vì đề nói:



# // // Không được nhảy qua phần tử >= arr[i]

# // // nên phải dừng luôn.



# import java.util.*;

# public class b243 {

#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#  int n = sc.nextInt();

#         // Tạo mảng
#         int[] arr = new int[n];

#         // Nhập các phần tử
#         System.out.println("Nhap mang:");

#         for (int i = 0; i < n; i++) {
#             arr[i] = sc.nextInt();
#         }

#         // Nhập d
#         System.out.print("Nhap d: ");
#         int d = sc.nextInt();

       

#         // Gọi hàm giải
#         int result = maxJumps(arr, d);

#         // In kết quả
#         System.out.println( result);

#         sc.close();
#     }
#  // Hàm chính để tìm số vị trí tối đa có thể nhảy
#     public static int maxJumps(int[] arr, int d) {

#         // Mảng memo dùng để lưu kết quả đã tính
#         // maxJumpsFromHere[i] = số bước tối đa bắt đầu từ i
#         int[] maxJumpsFromHere = new int[arr.length];

#         // Lưu kết quả lớn nhất toàn bộ mảng
#         int maxJumps = 0;

#         // Thử bắt đầu từ từng vị trí
#         for (int i = 0; i < arr.length; i++) {

#             // Tính số bước tối đa từ i
#             maxJumps = Math.max(
#                     maxJumps,
#                     calMaxJumps(i, maxJumpsFromHere, arr, d)
#             );
#         }

#         return maxJumps;
#     }

#     // Hàm DFS + Memoization
#     public static int calMaxJumps(int i,
#                             int[] maxJumpsFromHere,
#                             int[] arr,
#                             int d) {

#         // Nếu đã tính rồi thì trả về luôn
#         if (maxJumpsFromHere[i] != 0) {
#             return maxJumpsFromHere[i];
#         }

#         // Lưu số bước lớn nhất có thể nhảy tiếp
#         int maxJumpsCount = 0;

#         // =========================
#         // Nhảy sang phải
#         // =========================
#         for (int x = i + 1;
#              x <= i + d && x < arr.length;
#              x++) {

#             // Nếu gặp phần tử lớn hơn hoặc bằng
#             // thì bị chặn -> dừng luôn
#             if (arr[x] >= arr[i]) {
#                 break;
#             }

#             // DFS tiếp từ vị trí x
#             maxJumpsCount = Math.max(
#                     maxJumpsCount,
#                     calMaxJumps(x, maxJumpsFromHere, arr, d)
#             );
#         }

#         // =========================
#         // Nhảy sang trái
#         // =========================
#         for (int x = i - 1;
#              x >= i - d && x >= 0;
#              x--) {

#             // Nếu gặp phần tử lớn hơn hoặc bằng
#             // thì bị chặn -> dừng
#             if (arr[x] >= arr[i]) {
#                 break;
#             }

#             // DFS tiếp
# #             maxJumpsCount = Math.max(
# #                     maxJumpsCount,
# #                     calMaxJumps(x, maxJumpsFromHere, arr, d)
# #             );
# #         }

# #         // +1 để tính luôn vị trí hiện tại
# #         maxJumpsFromHere[i] = 1 + maxJumpsCount;

# #         return maxJumpsFromHere[i];
# # }}

# Thuật toán này dùng:



# Monotonic Stack

# Dynamic Programming

# Thay vì DFS như cách trước, cách này xử lý theo thứ tự chiều cao.

# Ý tưởng chính

# Ta có:



# maxSteps[i]

# = số vị trí tối đa có thể đi được nếu bắt đầu từ i

# Ban đầu:



# maxSteps = [1,1,1,...]

# Vì đứng yên tại chỗ cũng tính là 1.

# Monotonic Stack là gì?

# Stack này lưu các index sao cho:



# arr[stack[0]] >= arr[stack[1]] >= arr[stack[2]]

# Tức là:



# giảm dần

# Ý tưởng quan trọng

# Khi gặp phần tử lớn hơn:



# arr[i] > arr[stack[-1]]

# ta pop ra.

# Lúc đó ta biết:



# phần tử bị pop có thể nhảy tới phần tử lớn hơn gần nhất bên trái/phải

# Code có chú thích
from typing import List
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:



        # maxSteps[i]

        # = số vị trí tối đa có thể đi được bắt đầu từ i

        # Ban đầu = 1 vì tính luôn chính nó

        maxSteps = [1 for i in range(len(arr))]



        # Monotonic decreasing stack

        # Lưu index

        stack = []



        n = len(arr)



        # Duyệt từ trái sang phải

        # i = n dùng để ép pop hết stack

        for i in range(n + 1):



            # Khi:

            # - đã tới cuối mảng

            # HOẶC

            # - phần tử hiện tại lớn hơn đỉnh stack

            while len(stack) > 0 and (

                    i == n or arr[stack[-1]] < arr[i]

            ):



                # Lấy phần tử cần pop

                popped_indices = [stack.pop()]



                # Gom các phần tử bằng nhau

                while stack and arr[stack[-1]] == arr[popped_indices[0]]:

                    popped_indices.append(stack.pop())



                # Xử lý từng index bị pop

                for j in popped_indices:



                    # =========================

                    # Kiểm tra nhảy sang phải

                    # =========================



                    # i là phần tử lớn hơn gần nhất bên phải

                    # Nếu khoảng cách <= d

                    if i < n and i - j <= d:



                        # Từ j có thể đi tới i

                        maxSteps[i] = max(

                            maxSteps[i],

                            maxSteps[j] + 1

                        )



                    # =========================

                    # Kiểm tra nhảy sang trái

                    # =========================



                    # stack[-1]

                    # là phần tử lớn hơn gần nhất bên trái

                    if len(stack) > 0 and j - stack[-1] <= d:



                        maxSteps[stack[-1]] = max(

                            maxSteps[stack[-1]],

                            maxSteps[j] + 1

                        )



            # Thêm index hiện tại vào stack

            if i < n:

                stack.append(i)



        # Trả về kết quả lớn nhất

        return max(maxSteps)

# Ví dụ trực quan

# arr = [6,4,14]

# d = 2

# i = 0

# stack = [0]

# i = 1

# 4 < 6

# nên push:



# stack = [0,1]

# i = 2

# 14 > 4

# => pop 1

# Ta biết:



# 4 có thể nối tới 14

# Sau đó:



# 14 > 6

# => pop 0

# Vì sao stack hoạt động?

# Stack giúp tìm:



# phần tử lớn hơn gần nhất bên trái/phải

# rất nhanh.

# Độ phức tạp

# Mỗi phần tử:



# push 1 lần

# pop 1 lần

# Nên:



# Time: O(n)

# Nhanh hơn DFS:



# O(n * d)

# Điểm khó nhất

# Đoạn này:



# while stack and arr[stack[-1]] == arr[popped_indices[0]]:

# để xử lý các phần tử bằng nhau cùng lúc.

# Vì:



# các phần tử bằng nhau không được nhảy qua nhau

# nên phải gom chung để tránh cập nhật sai.