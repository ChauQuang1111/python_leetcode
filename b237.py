# // Minimum Common Value (19/05/2026)

# // > Cho hai mảng số nguyên `nums1` và `nums2` đã được sắp xếp tăng dần.
# // > Hãy tìm **giá trị nhỏ nhất xuất hiện trong cả hai mảng**.
# // > Nếu không có phần tử chung thì trả về `-1`.

# // Ví dụ:

# // ```text
# // nums1 = [1,2,3]
# // nums2 = [2,4]

# // Kết quả: 2
# // ```

# // Vì số `2` xuất hiện trong cả hai mảng và đó là số chung nhỏ nhất.

# // ---

# // ## Ví dụ khác

# // ### Ví dụ 1

# // ```text
# // nums1 = [1,2,3,6]
# // nums2 = [2,3,4,5]

# // Output: 2
# // ```

# // Các số chung là: `2`, `3`
# // Số nhỏ nhất là `2`.

# // ---

# // ### Ví dụ 2

# // ```text
# // nums1 = [1,2,3]
# // nums2 = [4,5,6]

# // Output: -1
# // ```

# // Không có số nào xuất hiện ở cả hai mảng.

# // ---

# // ## Ý chính của đề

# // Ta cần tìm:

# // ```text
# // min(x)
# // ```

# // sao cho:

# // ```text
# // x thuộc nums1
# // và
# // x thuộc nums2
# // ```

# // ---

# // ## Cách suy nghĩ

# // Vì 2 mảng đã **sort tăng dần**, nên thường dùng:

# // ### Two Pointers

# // * Dùng 2 con trỏ:

# //   * `i` cho `nums1`
# //   * `j` cho `nums2`

# // So sánh:

# // * Nếu `nums1[i] == nums2[j]`
# //   → tìm được đáp án nhỏ nhất luôn.

# // * Nếu `nums1[i] < nums2[j]`
# //   → tăng `i`

# // * Nếu `nums1[i] > nums2[j]`
# //   → tăng `j`

# // ---

# // ## Minh họa

# // ```text
# // nums1 = [1,2,3,6]
# // nums2 = [2,3,4,5]

# // i=0 j=0
# // 1 < 2 → tăng i

# // i=1 j=0
# // 2 == 2 → đáp án = 2
# // ```

# // ---

# // ## Độ phức tạp

# // * Time: `O(n + m)`
# // * Space: `O(1)`

# // ---

# // ## Java code mẫu

# // ```java
# // class Solution {
# //     public int getCommon(int[] nums1, int[] nums2) {
# //         int i = 0;
# //         int j = 0;

# //         while (i < nums1.length && j < nums2.length) {

# //             if (nums1[i] == nums2[j]) {
# //                 return nums1[i];
# //             }

# //             if (nums1[i] < nums2[j]) {
# //                 i++;
# //             } else {
# //                 j++;
# //             }
# //         }

# //         return -1;
# //     }
# // }
# // ```
# // Thuật toán của bạn dùng kỹ thuật Two Pointers (hai con trỏ) để tìm số nhỏ nhất xuất hiện trong cả hai mảng đã được sắp xếp tăng dần.

# // Ý tưởng chính

# // Vì:

# // nums1 và nums2 đều đã sort tăng dần

# // nên ta không cần kiểm tra mọi cặp phần tử.

# // Ta chỉ cần:

# // so sánh 2 phần tử hiện tại

# // di chuyển con trỏ ở mảng có giá trị nhỏ hơn

# // Giải thích từng phần

# // Khởi tạo

# // int i = 0;

# // int j = 0;

# // i trỏ vào mảng nums1

# // j trỏ vào mảng nums2

# // Lưu độ dài mảng

# // int len1 = nums1.length;

# // int len2 = nums2.length;

# // // để dùng nhiều lần cho tiện.

# // // Bước tối ưu đầu tiên

# // // if (nums1[len1 - 1] < nums2[0] || nums2[len2 - 1] < nums1[0]) {

# // //     return -1;

# // }

# // Ý nghĩa:

# // Nếu:

# // phần tử lớn nhất của nums1 < phần tử nhỏ nhất của nums2

# // thì chắc chắn:

# // 2 mảng không có phần tử chung

# // Ví dụ:

# // nums1 = [1,2,3]

# // nums2 = [5,6,7]

# // vì:

# // 3 < 5

# // nên trả về -1 ngay.

# // Đây là bước tối ưu nhỏ giúp tránh chạy vòng lặp không cần thiết.

# // Vòng lặp chính

# // while (i < len1 && j < len2)

# // Lặp khi cả hai con trỏ còn nằm trong mảng.

# // Trường hợp 1: bằng nhau

# // if (nums1[i] == nums2[j]) {

# //     return nums1[i];

# // }

# // Nếu bằng nhau:

# // đã tìm được phần tử chung

# // Và vì 2 mảng tăng dần nên:

# // đây chính là giá trị chung nhỏ nhất

# // => return luôn.

# // Trường hợp 2: nums1 nhỏ hơn

# // else if (nums1[i] < nums2[j]) {

# //     i++;

# // }

# // Ví dụ:

# // nums1[i] = 2

# // nums2[j] = 5

# // Ta biết:

# // 2 không thể bằng 5

# // và vì mảng tăng dần:

# // mọi phần tử trước 5 trong nums1 đã xét rồi

# // nên phải tăng i để tìm số lớn hơn.

# // Trường hợp 3: nums2 nhỏ hơn

# // else {

# //     j++;

# // }

# // Tương tự:

# // Nếu:

# // nums2[j] < nums1[i]

# // thì tăng j.

# // Ví dụ chạy từng bước

# // nums1 = [1,2,3,6]

# // nums2 = [2,3,4,5]

# // Ban đầu:

# // i = 0 → 1

# // j = 0 → 2

# // Bước 1

# // 1 < 2

# // → tăng i

# // Bước 2

# // i = 1 → 2

# // j = 0 → 2

# // 2 == 2

# // → return 2

# // Độ phức tạp

# // Time Complexity

# // O(n + m)

# // Vì mỗi con trỏ chỉ chạy tối đa 1 lần qua mảng.

# // Space Complexity

# // O(1)

# // Chỉ dùng vài biến phụ.

# // Tại sao thuật toán đúng?

# // Vì:

# // khi một giá trị nhỏ hơn giá trị còn lại,

# // nó không thể là đáp án

# // nên ta loại bỏ nó bằng cách tăng con trỏ tương ứng.

# // Do mảng đã sort nên không bỏ sót đáp án.

# import java.util.Scanner;

# public class b238 {

#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         // Nhập số phần tử mảng 1
#         int n = sc.nextInt();

#         // Tạo mảng 1
#         int[] nums1 = new int[n];

#         // Nhập phần tử mảng 1
#         int i = 0;
#         while (i < n) {

#             nums1[i] = sc.nextInt();
#             i++;
#         }

#         // Nhập số phần tử mảng 2
#         int m = sc.nextInt();

#         // Tạo mảng 2
#         int[] nums2 = new int[m];

#         // Nhập phần tử mảng 2
#         int j = 0;
#         while (j < m) {

#             nums2[j] = sc.nextInt();
#             j++;
#         }

#         int result = getCommon(nums1, nums2);

#         // In kết quả
#         System.out.println(result);

#         sc.close();
#     }

#     // Hàm tìm giá trị chung nhỏ nhất của 2 mảng
#     public static int getCommon(int[] nums1, int[] nums2) {

#         // Con trỏ cho mảng nums1
#         int i = 0;

#         // Con trỏ cho mảng nums2
#         int j = 0;

#         // Độ dài mảng nums1
#         int len1 = nums1.length;

#         // Độ dài mảng nums2
#         int len2 = nums2.length;

#         /*
#          * Kiểm tra nhanh:
#          * Nếu phần tử lớn nhất của nums1 nhỏ hơn
#          * phần tử nhỏ nhất của nums2
#          * HOẶC ngược lại
#          * => không có phần tử chung
#          */
#         if (nums1[len1 - 1] < nums2[0] ||
#                 nums2[len2 - 1] < nums1[0]) {

#             return -1;
#         }

#         // Duyệt khi cả 2 con trỏ chưa vượt mảng
#         while (i < len1 && j < len2) {

#             // Nếu tìm thấy phần tử chung
#             if (nums1[i] == nums2[j]) {

#                 return nums1[i];
#             }

#             // Nếu nums1 nhỏ hơn -> tăng i
#             else if (nums1[i] < nums2[j]) {

#                 i++;
#             }

#             // Nếu nums2 nhỏ hơn -> tăng j
#             else {

#                 j++;
#             }
#         }

#         // Không tìm thấy phần tử chung
#         return -1;
#     }
# }


# Ý tưởng thuật toán

# Bài toán yêu cầu tìm:



# giá trị nhỏ nhất xuất hiện trong cả nums1 và nums2

# Hai mảng đã được:



# sắp xếp tăng dần

# nên ta dùng kỹ thuật:



# Two Pointers (hai con trỏ)

# Cách hoạt động

# Ta dùng:



# p1 duyệt nums1

# p2 duyệt nums2

# Quy tắc

# Nếu bằng nhau

# nums1[p1] == nums2[p2]

# → tìm được số chung nhỏ nhất

# → return luôn.

# Nếu nums1 nhỏ hơn

# nums1[p1] < nums2[p2]

# → tăng p1

# Vì:



# giá trị nhỏ hơn không thể là đáp án

# Nếu nums2 nhỏ hơn

# → tăng p2

# Ví dụ

# nums1 = [1,2,3,6]

# nums2 = [2,3,4,5]

# Ban đầu:



# p1 = 0 → 1

# p2 = 0 → 2

# Vì:



# 1 < 2

# → tăng p1

# Tiếp theo:



# p1 = 1 → 2

# p2 = 0 → 2

# 2 == 2

# → return 2

# Độ phức tạp

# Time Complexity

# O(n + m)

# Mỗi con trỏ chỉ đi qua mảng 1 lần.

# Space Complexity

# O(1)

# Không dùng thêm bộ nhớ đáng kể.

# Code có chú thích
from typing import List
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:



        # Nếu phần tử lớn nhất của nums1

        # nhỏ hơn phần tử nhỏ nhất của nums2

        # => không có phần tử chung

        if nums1[-1] < nums2[0]:

            return -1



        # Trường hợp ngược lại

        if nums2[-1] < nums1[0]:

            return -1



        # Con trỏ cho nums1

        p1 = 0



        # Con trỏ cho nums2

        p2 = 0



        # Duyệt khi cả hai con trỏ chưa vượt mảng

        while p1 < len(nums1) and p2 < len(nums2):



            # Nếu tìm thấy phần tử chung

            if nums1[p1] == nums2[p2]:



                # Đây là giá trị chung nhỏ nhất

                return nums1[p1]



            # Nếu phần tử nums1 nhỏ hơn

            # tăng p1 để tìm giá trị lớn hơn

            elif nums1[p1] < nums2[p2]:



                p1 += 1



            # Nếu phần tử nums2 nhỏ hơn

            # tăng p2

            else:



                p2 += 1



        # Không tìm thấy phần tử chung

        return -1