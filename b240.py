# // // Search in Rotated Sorted Array(22/05/2026)
# // // Bài “Search in Rotated Sorted Array” là một bài rất nổi tiếng trên LeetCode.

# // // Ý tưởng đề bài

# // // Ban đầu ta có một mảng tăng dần:



# // // [0,1,2,4,5,6,7]

# // // Sau đó mảng bị xoay (rotate) tại một vị trí nào đó.

# // // Ví dụ xoay tại index 3:



# // // [4,5,6,7,0,1,2]

# // // Hoặc:



# // // [6,7,0,1,2,4,5]

# // // Nhiệm vụ

# // // Cho:



# // // mảng nums

# // // số cần tìm target

# // // Hãy trả về:



# // // vị trí index của target

# // // nếu không có thì trả -1

# // // Ví dụ 1

# // // nums = [4,5,6,7,0,1,2]

# // // target = 0

# // // Kết quả:



# // // 4

# // // Vì:



# // // nums[4] = 0

# // // Ví dụ 2

# // // nums = [4,5,6,7,0,1,2]

# // // target = 3

# // // Kết quả:



# // // -1

# // // Vì không có số 3 trong mảng.

# // // Điều khó của bài này

# // // Mảng không còn tăng dần hoàn toàn nữa.

# // // Ví dụ:



# // // [4,5,6,7,0,1,2]

# // // Nếu dùng binary search bình thường sẽ bị lỗi logic vì:



# // // 7 > 0

# // // tức là mảng bị “gãy”.

# // // Điểm quan trọng

# // // Trong mỗi lần chia đôi:



# // // mid = (left + right) / 2

# // // thì sẽ luôn có:



# // // hoặc nửa trái đã được sort

# // // hoặc nửa phải đã được sort

# // // Ta tận dụng điều này để quyết định đi bên nào.

# // // Minh họa

# // // Ví dụ:



# // // [4,5,6,7,0,1,2]

# // // Tìm 0

# // // Bước 1

# // // left = 0

# // // right = 6

# // // mid = 3

# // // nums[mid] = 7

# // // Ta thấy:



# // // nums[left] <= nums[mid]

# // // 4 <= 7

# // // => nửa trái [4,5,6,7] đang tăng dần.

# // // Nhưng:



# // // 0 không nằm trong [4..7]

# // // => bỏ nửa trái.

# // // Bước 2

# // // Tìm bên phải:



# // // [0,1,2]

# // // Binary search tiếp là ra.

# // // Độ phức tạp

# // // Vì vẫn dùng binary search nên:



# // // O(log n)

# // // Ý tưởng cốt lõi

# // // Mỗi lần:



# // // tìm mid

# // // kiểm tra bên nào đang được sort

# // // xem target có nằm trong đoạn đó không

# // // loại bỏ một nửa mảng

# // // Code Java ngắn gọn

# // // class Solution {

# // //     public int search(int[] nums, int target) {

# // //         int left = 0;

# // //         int right = nums.length - 1;



# // //         while (left <= right) {



# // //             int mid = (left + right) / 2;



# // //             if (nums[mid] == target)

# // //                 return mid;



# // //             // bên trái đã sort

# // //             if (nums[left] <= nums[mid]) {



# // //                 if (target >= nums[left] && target < nums[mid]) {

# // //                     right = mid - 1;

# // //                 } else {

# // //                     left = mid + 1;

# // //                 }



# // //             }

# // //             // bên phải đã sort

# // //             else {



# // //                 if (target > nums[mid] && target <= nums[right]) {

# // //                     left = mid + 1;

# // //                 } else {

# // //                     right = mid - 1;

# // //                 }

# // //             }

# // //         }



# // //         return -1;

# // //     }

# // // }

# // // Mẹo nhớ nhanh

# // // Luôn hỏi:



# // // Nửa nào đang được sort?

# // // Sau đó:



# // // target có nằm trong nửa đó không?

# // // Nếu có → đi vào đó

# // // Nếu không → đi nửa còn lại


# // Ý tưởng thuật toán

# // Bài này yêu cầu tìm target trong một mảng đã bị rotate.

# // Ví dụ:



# // [4,5,6,7,0,1,2]

# // Ban đầu mảng thật ra là:



# // [0,1,2,4,5,6,7]

# // sau đó bị xoay tại vị trí số 0.

# // Ý tưởng chính của code

# // Code này làm 2 bước:



# // Tìm vị trí rotate

# // Binary Search trên “mảng gốc”

# // BƯỚC 1 — Tìm vị trí rotate

# // Ta cần tìm:



# // phần tử nhỏ nhất

# // Ví dụ:



# // [4,5,6,7,0,1,2]

# //            ^

# // Số nhỏ nhất là 0 tại index 4.

# // Vậy:



# // rot = 4

# // Tại sao dùng được Binary Search?

# // Quan sát:



# // [4,5,6,7,0,1,2]

# // Mảng được chia thành 2 phần:



# // [4,5,6,7] [0,1,2]

# // bên trái luôn lớn hơn phần tử cuối

# // bên phải luôn nhỏ hơn hoặc bằng phần tử cuối

# // Phần tử cuối:



# // nums[n - 1] = 2

# // Logic

# // Nếu:

# // nums[mid] > nums[n - 1]

# // Ví dụ:



# // mid = 7

# // 7 > 2

# // => mid đang nằm bên trái

# // => điểm rotate nằm bên phải



# // lo = mid + 1;

# // Ngược lại

# // nums[mid] <= nums[n - 1]

# // Ví dụ:



# // mid = 1

# // 1 <= 2

# // => mid đang ở nửa phải

# // => điểm rotate nằm ở:



# // mid

# // hoặc bên trái

# // hi = mid;

# // Sau vòng lặp

# // int rot = lo;

# // Ta tìm được:



# // rot = vị trí phần tử nhỏ nhất

# // BƯỚC 2 — Binary Search

# // Bây giờ ta coi như mảng chưa rotate:



# // [0,1,2,4,5,6,7]

# // Ta dùng binary search bình thường.

# // Nhưng index thật trong mảng rotate phải đổi bằng:



# // real = (mid + rot) % n;

# // Ví dụ

# // nums = [4,5,6,7,0,1,2]

# // rot = 4

# // mid = 0

# // real = (0 + 4) % 7 = 4

# // => phần tử thật:



# // nums[4] = 0

# // mid = 1

# // real = (1 + 4) % 7 = 5

# // => phần tử thật:



# // nums[5] = 1

# // Ý nghĩa công thức

# // (mid + rot) % n

# // giúp:



# // dịch index sang đúng vị trí trong mảng rotate

# // Ví dụ chạy toàn bộ

# // Input

# // nums = [4,5,6,7,0,1,2]

# // target = 0

# // Tìm rotate

# // Lần 1

# // lo = 0

# // hi = 6

# // mid = 3

# // nums[mid] = 7

# // 7 > 2

# // => sang phải



# // lo = 4

# // Lần 2

# // lo = 4

# // hi = 6

# // mid = 5

# // nums[mid] = 1

# // 1 <= 2

# // => sang trái



# // hi = 5

# // Lần 3

# // lo = 4

# // hi = 5

# // mid = 4

# // nums[mid] = 0

# // 0 <= 2

# // => hi = 4

# // Kết thúc:



# // rot = 4

# // Binary Search

# // mid = 3

# // real = (3 + 4) % 7 = 0

# // nums[0] = 4

# // 0 nhỏ hơn 4 → đi trái.

# // mid = 1

# // real = (1 + 4) % 7 = 5

# // nums[5] = 1

# // 0 nhỏ hơn 1 → đi trái.

# // mid = 0

# // real = (0 + 4) % 7 = 4

# // nums[4] = 0

# // Tìm thấy.

# // Độ phức tạp

# // Time

# // tìm rotate: O(log n)

# // binary search: O(log n)

# // Tổng:



# // O(log n)

# // Điểm hay của thuật toán

# // Thay vì xử lý mảng rotate trực tiếp, thuật toán:



# // tìm điểm xoay

# // biến mảng rotate thành “mảng bình thường” bằng phép modulo

# // => code gọn và dễ binary search hơn.



# import java.util.*;


# public class b241 {

#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#       int n = sc.nextInt();

#         // tạo mảng
#         int[] nums = new int[n];

#         /*
#             Nhập các phần tử của mảng
#         */
#         for (int i = 0; i < n; i++) {
#             nums[i] = sc.nextInt();
#         }

#         /*
#             Nhập target cần tìm
#         */
#         int target = sc.nextInt();

#         /*
#             Gọi hàm search
#         */
#         int result = search(nums, target);

#         /*
#             In kết quả
#         */
#         System.out.println(result);

#         sc.close();
#     }
# public static int search(int[] nums, int target) {

#         int n = nums.length;

#         // lo và hi dùng để tìm vị trí rotate
#         int lo = 0;
#         int hi = n - 1;

#         /*
#             ===================================
#             BƯỚC 1: TÌM VỊ TRÍ ROTATE
#             ===================================

#             Ví dụ:
#             [4,5,6,7,0,1,2]

#             phần tử nhỏ nhất là 0
#             => rot = 4

#             Ý tưởng:
#             - phần bên trái luôn lớn hơn nums[n - 1]
#             - phần bên phải luôn nhỏ hơn hoặc bằng nums[n - 1]
#         */
#         while (lo < hi) {

#             // lấy phần tử giữa
#             int mid = (lo + hi) / 2;

#             /*
#                 Nếu nums[mid] > nums[n - 1]

#                 Ví dụ:
#                 nums[mid] = 7
#                 nums[n - 1] = 2

#                 => mid đang ở nửa trái
#                 => điểm rotate nằm bên phải
#             */
#             if (nums[mid] > nums[n - 1]) {
#                 lo = mid + 1;
#             }

#             /*
#                 Ngược lại:

#                 nums[mid] <= nums[n - 1]

#                 => mid đang ở nửa phải
#                 => vị trí rotate ở mid hoặc bên trái
#             */
#             else {
#                 hi = mid;
#             }
#         }

#         // rot là vị trí nhỏ nhất trong mảng
#         int rot = lo;

#         /*
#             ===================================
#             BƯỚC 2: BINARY SEARCH
#             ===================================

#             Sau khi biết rot,
#             ta giả lập mảng trở về dạng tăng dần.

#             Dùng công thức:

#             real = (mid + rot) % n

#             để đổi index giả -> index thật
#         */

#         // reset lại lo và hi
#         lo = 0;
#         hi = n - 1;

#         while (lo <= hi) {

#             // mid của mảng đã "chuẩn hóa"
#             int mid = (lo + hi) / 2;

#             /*
#                 real là index thật trong mảng rotate

#                 Ví dụ:
#                 nums = [4,5,6,7,0,1,2]
#                 rot = 4

#                 mid = 0
#                 real = (0 + 4) % 7 = 4

#                 => nums[4] = 0
#             */
#             int real = (mid + rot) % n;

#             // tìm thấy target
#             if (nums[real] == target) {
#                 return real;
#             }

#             // target lớn hơn -> tìm bên phải
#             if (nums[real] < target) {
#                 lo = mid + 1;
#             }

#             // target nhỏ hơn -> tìm bên trái
#             else {
#                 hi = mid - 1;
#             }
#         }

#         // không tìm thấy
#         return -1;
# }
#  }



from typing import List
from bitsets import bitset
from bisect import bisect_left
class Solution:
    def search(self, nums: List[int], target: int) -> int:



        # số lượng phần tử

        n = len(nums)



        """

        =====================================

        BƯỚC 1: TÌM VỊ TRÍ ROTATE

        =====================================



        Ví dụ:

        nums = [4,5,6,7,0,1,2]



        phần tử nhỏ nhất là 0

        => rot = 4



        bisect_left sẽ tìm vị trí đầu tiên mà:



            n <= nums[-1]



        đúng.



        nums[-1] = 2



        kiểm tra từng phần tử:



        4 <= 2 -> False

        5 <= 2 -> False

        6 <= 2 -> False

        7 <= 2 -> False

        0 <= 2 -> True   <- vị trí đầu tiên

        1 <= 2 -> True

        2 <= 2 -> True



        => rot = 4

        """



        rot = bisect_left(

            nums,

            True,

            key=lambda n: n <= nums[-1]

        )



        """

        =====================================

        BƯỚC 2: BINARY SEARCH

        =====================================



        Sau khi biết rot,

        ta giả lập mảng trở về dạng tăng dần.



        Dùng công thức:



            real = (mid + rot) % n



        để đổi index giả -> index thật

        """



        lo = 0

        hi = n - 1



        while lo <= hi:



            # vị trí giữa

            mid = (lo + hi) // 2



            """

            real là vị trí thật trong mảng rotate



            Ví dụ:

            nums = [4,5,6,7,0,1,2]

            rot = 4



            mid = 0



            real = (0 + 4) % 7 = 4



            => nums[4] = 0

            """

            real = (mid + rot) % n



            # tìm thấy target

            if nums[real] == target:

                return real



            # target lớn hơn -> tìm bên phải

            if nums[real] < target:

                lo = mid + 1



            # target nhỏ hơn -> tìm bên trái

            else:

                hi = mid - 1



        # không tìm thấy

        return -1

# Giải thích thuật toán

# Ý tưởng bài toán

# Ban đầu mảng được sắp xếp tăng dần:



# [0,1,2,4,5,6,7]

# Sau đó bị rotate:



# # [4,5,6,7,0,1,2]

# Nhiệm vụ:



# tìm index của target

# với độ phức tạp:



# O(log n)

# Thuật toán gồm 2 bước

# BƯỚC 1 — Tìm vị trí rotate

# Ta cần tìm:



# index của phần tử nhỏ nhất

# Ví dụ:



# [4,5,6,7,0,1,2]

#            ^

#           rot = 4

# Code:



# rot = bisect_left(

#     nums,

#     True,

#     key=lambda n: n <= nums[-1]

# )

# # Ý nghĩa

# nums[-1] = 2

# Ta kiểm tra:



# 4 <= 2 -> False

# 5 <= 2 -> False

# 6 <= 2 -> False

# 7 <= 2 -> False

# 0 <= 2 -> True

# bisect_left tìm vị trí đầu tiên có giá trị True.

# => rot = 4.

# BƯỚC 2 — Binary Search

# Sau khi biết rot,

# ta coi như mảng đã trở lại bình thường:

# [0,1,2,4,5,6,7]

# Nhưng index thật trong mảng rotate phải đổi bằng:



# real = (mid + rot) % n

# Ví dụ

# nums = [4,5,6,7,0,1,2]

# rot = 4

# Nếu:



# mid = 0

# thì:



# real = (0 + 4) % 7 = 4

# => phần tử thật:



# nums[4] = 0

# Độ phức tạp

# Time Complexity

# tìm rotate: O(log n)

# binary search: O(log n)

# Tổng:



# O(log n)

# Space Complexity

# O(1)