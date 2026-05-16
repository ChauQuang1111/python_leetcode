# # //  Find Minimum in Rotated Sorted Array II (16/05/2026)
# # // * sắp xếp tăng dần ban đầu
# # // * sau đó bị “xoay” (rotate) vài lần
# # // * và **có thể chứa phần tử trùng nhau**

# # // ---

# # // ## 1. Mảng xoay là gì?

# # // Ví dụ mảng tăng dần ban đầu:

# # // ```text
# # // [1,2,3,4,5]
# # // ```

# # // Nếu xoay sang phải:

# # // ```text
# # // [4,5,1,2,3]
# # // ```

# # // Hoặc:

# # // ```text
# # // [3,4,5,1,2]
# # // ```

# # // Phần tử nhỏ nhất luôn là điểm “gãy” của mảng.

# # // ---

# # // ## 2. Ví dụ đề bài

# # // ### Ví dụ 1

# # // ```text
# # // Input: nums = [1,3,5]
# # // Output: 1
# # // ```

# # // Mảng chưa xoay nên số nhỏ nhất là `1`.

# # // ---

# # // ### Ví dụ 2

# # // ```text
# # // Input: nums = [2,2,2,0,1]
# # // Output: 0
# # // ```

# # // Mảng đã xoay và có số trùng nhau.

# # // Số nhỏ nhất là `0`.

# # // ---

# # // ## 3. Điểm khó của bài

# # // Nếu **không có phần tử trùng nhau**, ta có thể dùng Binary Search rất dễ.

# # // Nhưng bài này có:

# # // ```text
# # // [2,2,2,0,1]
# # // ```

# # // hoặc

# # // ```text
# # // [1,1,1,1]
# # // ```

# # // => khó xác định bên trái hay bên phải đã được sắp xếp.

# # // ---

# # // ## 4. Ý tưởng chính

# # // Dùng Binary Search với 3 biến:

# # // ```text
# # // left, mid, right
# # // ```

# # // So sánh:

# # // ```text
# # // nums[mid] với nums[right]
# # // ```

# # // ---

# # // ## 5. Các trường hợp

# # // ### Trường hợp 1

# # // ```text
# # // nums[mid] > nums[right]
# # // ```

# # // Ví dụ:

# # // ```text
# # // [4,5,6,1,2,3]
# # //       ^
# # // ```

# # // => phần nhỏ nhất nằm bên phải `mid`

# # // Ta làm:

# # // ```text
# # // left = mid + 1
# # // ```

# # // ---

# # // ### Trường hợp 2

# # // ```text
# # // nums[mid] < nums[right]
# # // ```

# # // Ví dụ:

# # // ```text
# # // [4,5,1,2,3]
# # //     ^
# # // ```

# # // => phần nhỏ nhất nằm ở `mid` hoặc bên trái

# # // Ta làm:

# # // ```text
# # // right = mid
# # // ```

# # // ---

# # // ### Trường hợp 3 (quan trọng)

# # // ```text
# # // nums[mid] == nums[right]
# # // ```

# # // Ví dụ:

# # // ```text
# # // [2,2,2,0,1]
# # // ```

# # // Ta không biết minimum ở đâu.

# # // => giảm phạm vi:

# # // ```text
# # // right--
# # // ```

# # // ---

# # // ## 6. Minh họa trực quan

# # // Ví dụ:

# # // ```text
# # // nums = [2,2,2,0,1]
# # // ```

# # // Ban đầu:

# # // ```text
# # // left = 0
# # // right = 4
# # // mid = 2
# # // ```

# # // ```text
# # // nums[mid] = 2
# # // nums[right] = 1
# # // ```

# # // Vì:

# # // ```text
# # // 2 > 1
# # // ```

# # // => minimum ở bên phải:

# # // ```text
# # // left = mid + 1
# # // ```

# # // ---

# # // Tiếp:

# # // ```text
# # // left = 3
# # // right = 4
# # // mid = 3
# # // ```

# # // ```text
# # // nums[mid] = 0
# # // nums[right] = 1
# # // ```

# # // Vì:

# # // ```text
# # // 0 < 1
# # // ```

# # // => minimum ở bên trái hoặc chính nó:

# # // ```text
# # // right = mid
# # // ```

# # // Cuối cùng:

# # // ```text
# # // left == right == 3
# # // ```

# # // => đáp án:

# # // ```text
# # // nums[3] = 0
# # // ```

# # // ---

# # // ## 7. Code Java

# # // ```java
# # // class Solution {
# # //     public int findMin(int[] nums) {
# # //         int left = 0;
# # //         int right = nums.length - 1;

# # //         while (left < right) {
# # //             int mid = left + (right - left) / 2;

# # //             if (nums[mid] > nums[right]) {
# # //                 left = mid + 1;
# # //             }
# # //             else if (nums[mid] < nums[right]) {
# # //                 right = mid;
# # //             }
# # //             else {
# # //                 right--;
# # //             }
# # //         }

# # //         return nums[left];
# # //     }
# # // }
# # // ```

# # // ---

# # // ## 8. Độ phức tạp

# # // * Trung bình: `O(log n)`
# # // * Tệ nhất (nhiều phần tử trùng): `O(n)`

# # // Vì có thể phải `right--` liên tục.

# # // ---

# # // ## 9. Điều cần nhớ

# # // Mấu chốt của bài:

# # // ```text
# # // So sánh nums[mid] với nums[right]
# # // ```

# # // và xử lý riêng trường hợp:

# # // ```text
# # // nums[mid] == nums[right]
# # // ```

# # // đây là điểm khác với bài:
# # // Find Minimum in Rotated Sorted Array

# # import java.util.*;

# # public class b235 {

# #     // Scanner dùng để nhập dữ liệu
# #     static Scanner sc = new Scanner(System.in);

# #     public static void main(String[] args) {
# #         int n = sc.nextInt();

# #         int[] nums = new int[n];

# #         // Nhập mảng

# #         System.out.println("Nhap cac phan tu:");

# #         for (int i = 0; i < n; i++) {

# #             nums[i] = sc.nextInt();

# #         }

# #         int ans = findMin(nums);

# #         // In kết quả

# #         System.out.println(ans);

# #         sc.close();

# #     }
# #     // Hàm tìm phần tử nhỏ nhất trong mảng rotated sorted array

# #     public static int findMin(int[] nums) {

# #         // lo: vị trí đầu mảng

# #         // hi: vị trí cuối mảng

# #         int lo = 0;

# #         int hi = nums.length - 1;

# #         /*
# #          * 
# #          * Nếu phần tử đầu nhỏ hơn phần tử cuối
# #          * 
# #          * => mảng đã được sắp xếp tăng dần bình thường
# #          * 
# #          * => phần tử nhỏ nhất nằm ở đầu mảng
# #          *
# #          * 
# #          * 
# #          * Ví dụ:
# #          * 
# #          * [1,2,3,4,5]
# #          * 
# #          */

# #         if (nums[lo] < nums[hi]) {

# #             return nums[lo];

# #         }

# #         /*
# #          * 
# #          * Dùng Binary Search
# #          * 
# #          * Khi lo == hi thì tìm được minimum
# #          * 
# #          */

# #         while (lo < hi) {

# #             // Tính mid để tránh tràn số

# #             int mid = lo + (hi - lo) / 2;

# #             /*
# #              * 
# #              * Trường hợp 1:
# #              * 
# #              * nums[mid] > nums[hi]
# #              *
# #              * 
# #              * 
# #              * Ví dụ:
# #              * 
# #              * [4,5,6,1,2,3]
# #              * 
# #              * ^
# #              *
# #              * 
# #              * 
# #              * => minimum nằm bên phải mid
# #              * 
# #              */

# #             if (nums[mid] > nums[hi]) {

# #                 // bỏ nửa bên trái

# #                 lo = mid + 1;

# #             }

# #             /*
# #              * 
# #              * Trường hợp 2:
# #              * 
# #              * nums[mid] < nums[hi]
# #              *
# #              * 
# #              * 
# #              * Ví dụ:
# #              * 
# #              * [4,5,1,2,3]
# #              * 
# #              * ^
# #              *
# #              * 
# #              * 
# #              * => minimum nằm ở mid hoặc bên trái
# #              * 
# #              */

# #             else if (nums[mid] < nums[hi]) {

# #                 // giữ lại mid vì mid có thể là minimum

# #                 hi = mid;

# #             }

# #             /*
# #              * 
# #              * Trường hợp 3:
# #              * 
# #              * nums[mid] == nums[hi]
# #              *
# #              * 
# #              * 
# #              * Ví dụ:
# #              * 
# #              * [2,2,2,0,1]
# #              *
# #              * 
# #              * 
# #              * Không xác định được minimum ở đâu
# #              * 
# #              * => giảm hi đi 1 để thu hẹp phạm vi
# #              * 
# #              */

# #             else {

# #                 hi--;

# #             }

# #         }

# #         // Khi vòng lặp kết thúc

# #         // lo == hi

# #         // đây chính là vị trí nhỏ nhất

# #         return nums[hi];
# #     }
# # }

# # // Ví dụ
# # // chạy

# # // Input

# # // Nhap so
# # // phan tu:5

# # // Nhap cac
# # // phan tu:

# # // 2 2 2 0 1

# # // Output

# # // Phan
# # // tu nho
# # // nhat la:0

# # // Ý tưởng
# # // thuật toán
# # // ngắn gọn

# # // Ta luôn
# # // so sánh:

# # // nums[mid]và nums[hi]

# # // Nếu:

# # // nums[mid]>nums[hi]

# # // =>
# # // minimum nằm
# # // bên phải

# # // Nếu:

# # // nums[mid]<nums[hi]

# # // =>
# # // minimum nằm
# # // bên trái
# # // hoặc chính
# # // mid

# # // Nếu:

# # // nums[mid]==nums[hi]

# # // =>
# # // không biết
# # // minimum ở đâu

# # // =>giảm:

# # // hi--

# # // để tiếp
# # // tục tìm
# # // .
# from typing import List
# class Solution:
# class Solution:

#     def findMin(self, nums: List[int]) -> int:

#         # left: vị trí đầu mảng
#         # right: vị trí cuối mảng
#         left, right = 0, len(nums) - 1

#         """
#         Dùng Binary Search để tìm phần tử nhỏ nhất

#         Ý tưởng:
#         - So sánh nums[mid] với nums[right]
#         - Từ đó xác định minimum nằm bên nào
#         """

#         while left < right:

#             # Tính vị trí ở giữa
#             mid = left + (right - left) // 2

#             """
#             Trường hợp 1:
#             nums[mid] > nums[right]

#             Ví dụ:
#             [4,5,6,1,2,3]
#                   ^

#             nums[mid] lớn hơn nums[right]
#             => minimum chắc chắn nằm bên phải mid
#             """

#             if nums[mid] > nums[right]:

#                 # Bỏ nửa bên trái
#                 left = mid + 1

#             """
#             Trường hợp 2:
#             nums[mid] < nums[right]

#             Ví dụ:
#             [4,5,1,2,3]
#                 ^

#             => minimum nằm ở mid hoặc bên trái
#             """

#          elif nums[mid] < nums[right]:

#                 # Giữ lại mid
#                 # vì mid có thể là minimum
#                 right = mid

#             """
#             Trường hợp 3:
#             nums[mid] == nums[right]

#             Ví dụ:
#             [2,2,2,0,1]

#             Không thể xác định minimum nằm bên nào
#             do có phần tử trùng nhau

#             => giảm right để thu hẹp phạm vi tìm kiếm
#             """

#          else:
#                 right -= 1

#         """
#         Khi vòng lặp kết thúc:
#         left == right

#         Đây chính là vị trí của phần tử nhỏ nhất
#         """

#         return nums[right]

# # Giải thích thuật toán

# # 1. Mảng rotated sorted array

# # Ví dụ mảng ban đầu:

# # [1,2,3,4,5]

# # Sau khi rotate:

# # [4,5,1,2,3]

# # Ta cần tìm số nhỏ nhất (1).

# # 2. Ý tưởng chính

# # Ta dùng:

# # Binary Search

# # vì mảng gần như vẫn có tính chất sắp xếp.

# # 3. So sánh quan trọng

# # Thuật toán luôn so sánh:

# # nums[mid] và nums[right]

# # 4. Các trường hợp

# # TH1

# # nums[mid] > nums[right]

# # Ví dụ:

# # [4,5,6,1,2,3]

# #       ^

# # => minimum nằm bên phải.

# # Ta làm:



# # left = mid + 1

# # TH2

# # nums[mid] < nums[right]

# # Ví dụ:



# # [4,5,1,2,3]

# #     ^

# # => minimum nằm bên trái hoặc chính mid.

# # Ta làm:



# # right = mid

# # TH3 (quan trọng)

# # nums[mid] == nums[right]

# # Ví dụ:



# # [2,2,2,0,1]

# # Không biết minimum ở bên nào vì có số trùng nhau.

# # => giảm:



# # right -= 1

# # để thu hẹp phạm vi tìm kiếm.

# # 5. Độ phức tạp

# # Trung bình:

# # O(log n)

# # Tệ nhất:

# # O(n)

# # khi có quá nhiều phần tử trùng nhau.

from typing import List

class Solution:

    def findMin(self, nums: List[int]) -> int:

        # vị trí đầu và cuối
        left = 0
        right = len(nums) - 1

        # Binary Search
        while left < right:

            # tính mid
            mid = left + (right - left) // 2

            # minimum nằm bên phải
            if nums[mid] > nums[right]:
                left = mid + 1

            # minimum nằm bên trái hoặc chính mid
            elif nums[mid] < nums[right]:
                right = mid

            # không xác định được
            else:
                right -= 1

        return nums[right]


