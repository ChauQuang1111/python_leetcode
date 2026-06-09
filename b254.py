# // ### Đề bài: Maximum Total Subarray Value I(09/06/2026)

# // Cho:

# // * Mảng số nguyên `nums`
# // * Số nguyên `k`

# // Bạn phải chọn **chính xác `k` subarray (mảng con liên tiếp)**.

# // Lưu ý:

# // * Các subarray **được phép chồng lấp**.
# // * Có thể **chọn cùng một subarray nhiều lần**.

# // Giá trị của một subarray được định nghĩa là:

# // [
# // \text{value} = \max(subarray) - \min(subarray)
# // ]

# // Tổng điểm:

# // [
# // \text{total} = \sum value\ của\ k\ subarray
# // ]

# // Mục tiêu: tìm tổng điểm lớn nhất có thể. ([LeetCode][1])

# // ---

# // ### Ví dụ 1

# // ```text
# // nums = [1,3,2]
# // k = 2
# // ```

# // Các subarray có giá trị lớn nhất:

# // ```text
# // [1,3]     -> 3 - 1 = 2
# // [1,3,2]   -> 3 - 1 = 2
# // ```

# // Tổng:

# // ```text
# // 2 + 2 = 4
# // ```

# // Kết quả:

# // ```text
# // 4
# // ```

# // ---

# // ### Ví dụ 2

# // ```text
# // nums = [4,2,5,1]
# // k = 3
# // ```

# // Chọn:

# // ```text
# // [4,2,5,1] -> 5 - 1 = 4
# // [4,2,5,1] -> 4
# // [5,1]     -> 4
# // ```

# // Tổng:

# // ```text
# // 4 + 4 + 4 = 12
# // ```

# // Kết quả:

# // ```text
# // 12
# // ```

# // ([LeetCode][1])

# // ---

# // ## Ý tưởng quan trọng

# // Vì:

# // * Được phép chọn **cùng một subarray nhiều lần**.
# // * Muốn tổng lớn nhất ⇒ chỉ cần tìm **subarray có giá trị lớn nhất** rồi chọn nó `k` lần.

# // Giá trị lớn nhất của một subarray chính là:

# // ```text
# // max(nums) - min(nums)
# // ```

# // vì ta có thể lấy cả đoạn chứa giá trị lớn nhất và nhỏ nhất của mảng. ([LeetCode Wiki][2])

# // Do đó:

# // [
# // \text{answer} = k \times (\max(nums)-\min(nums))
# // ]

# // ---

# // ### Ví dụ

# // ```text
# // nums = [4,2,5,1]
# // k = 3
# // ```

# // ```text
# // max(nums) = 5
# // min(nums) = 1
# // ```

# // Giá trị lớn nhất:

# // ```text
# // 5 - 1 = 4
# // ```

# // Chọn đoạn đó 3 lần:

# // ```text
# // 4 × 3 = 12
# // ```

# // Đáp án:

# // ```java
# // return (long)k * (max - min);
# // ```

# // Độ phức tạp:

# // ```text
# // O(n)
# // ```

# // chỉ cần duyệt một lần để tìm `max` và `min`. ([LeetCode Wiki][2])


# // Dưới đây là giải thích thuật toán từ đoạn code:



# // class Solution {

# //     public long maxTotalValue(int[] A, int k) {

# //         int min = A[0], max = A[0];



# //         for (int n : A) {

# //             min = Math.min(min, n);

# //             max = Math.max(max, n);

# //         }



# //         return (long) (max - min) * k;

# //     }

# // }

# // Bước 1: Khởi tạo giá trị nhỏ nhất và lớn nhất

# // int min = A[0], max = A[0];

# // Ban đầu:



# // min = phần tử đầu tiên của mảng

# // max = phần tử đầu tiên của mảng

# // Ví dụ:



# // A = [4, 2, 5, 1]

# // thì:



# // min = 4

# // max = 4

# // Bước 2: Duyệt toàn bộ mảng để tìm min và max

# // for (int n : A) {

# //     min = Math.min(min, n);

# //     max = Math.max(max, n);

# // }

# // Lần 1

# // n = 4

# // min = min(4,4) = 4

# // max = max(4,4) = 4

# // Lần 2

# // n = 2

# // min = min(4,2) = 2

# // max = max(4,2) = 4

# // Lần 3

# // n = 5

# // min = min(2,5) = 2

# // max = max(4,5) = 5

# // Lần 4

# // n = 1

# // min = min(2,1) = 1

# // max = max(5,1) = 5

# // Kết thúc:



# // min = 1

# // max = 5

# // Bước 3: Tính giá trị lớn nhất của một subarray

# // Theo đề:

# // [

# // value = max(subarray) - min(subarray)

# // ]

# // Giá trị lớn nhất có thể đạt được là:

# // [

# // max(A) - min(A)

# // ]

# // vì ta luôn có thể chọn một subarray chứa cả phần tử lớn nhất và nhỏ nhất.

# // Ví dụ:



# // A = [4,2,5,1]

# // max(A) = 5

# // min(A) = 1

# // nên:



# // value = 5 - 1 = 4

# // Bước 4: Chọn subarray đó k lần

# // Đề bài cho phép:



# // Chọn cùng một subarray nhiều lần.

# // Các subarray được phép trùng nhau.

# // Vì vậy để tổng lớn nhất:



# // chọn subarray tốt nhất k lần

# // Tổng:

# // [

# // (max-min)\times k

# // ]

# // Code:



# // return (long)(max - min) * k;

# // Tại sao phải ép kiểu long?

# // Nếu:



# // max - min = 100000

# // k = 100000

# // thì:

# // [

# // 100000 \times 100000 = 10^{10}

# // ]

# // Trong khi:



# // int tối đa ≈ 2.1 × 10^9

# // sẽ bị tràn số.

# // Nên cần:



# // (long)(max - min) * k

# // để phép nhân được thực hiện trên kiểu long.

# // Độ phức tạp

# // Duyệt mảng một lần:



# // for (int n : A)

# // Thời gian: O(n)

# // Bộ nhớ phụ: O(1)

# // Tóm tắt ý tưởng

# // Tìm phần tử nhỏ nhất min.

# // Tìm phần tử lớn nhất max.

# // Giá trị subarray lớn nhất là:

# // [

# // max - min

# // ]

# // Vì được chọn lặp lại, chọn subarray đó k lần.

# // [

# // answer = (max - min)\times k

# // ]

# // Đó là lý do lời giải chỉ cần tìm min, max rồi nhân với k, không cần xét từng subarray.


# import java.util.*;

# public class b255 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#       int n = sc.nextInt();

#       int[] A = new int[n];

#         for (int i = 0; i < n; i++) {
#             A[i] = sc.nextInt();
#         }

       
#         int k = sc.nextInt();

#         // Gọi hàm tính kết quả
#         long result = maxTotalValue(A, k);

#         // In kết quả
#         System.out.println( result);

#         sc.close();
#     }
# // Hàm tìm tổng giá trị lớn nhất
#     public static long maxTotalValue(int[] A, int k) {

#         // Khởi tạo giá trị nhỏ nhất và lớn nhất bằng phần tử đầu tiên
#         int min = A[0];
#         int max = A[0];

#         // Duyệt mảng để tìm min và max
#         for (int n : A) {
#             min = Math.min(min, n);
#             max = Math.max(max, n);
#         }

#         // Giá trị lớn nhất của một subarray là (max - min)
#         // Vì được phép chọn cùng một subarray nhiều lần,
#         // đáp án = (max - min) * k
#         return (long) (max - min) * k;
#     }
# }
    

#   Dưới đây là code đã được thêm chú thích:



from typing import List



class Solution:



    def maxTotalValue(self, nums: List[int], k: int) -> int:



        # Tìm phần tử lớn nhất trong mảng

        max_value = max(nums)



        # Tìm phần tử nhỏ nhất trong mảng

        min_value = min(nums)



        # Giá trị lớn nhất của một subarray là:

        # max_value - min_value

        #

        # Vì đề bài cho phép chọn cùng một subarray nhiều lần,

        # nên để đạt tổng lớn nhất ta chọn subarray có giá trị lớn nhất

        # đúng k lần.

        #

        # Đáp án = k * (max_value - min_value)

        return k * (max_value - min_value)

# Giải thích thuật toán

# Cho mảng:



# nums = [4, 2, 5, 1]

# k = 3

# Bước 1: Tìm phần tử lớn nhất và nhỏ nhất

# max(nums) = 5

# min(nums) = 1

# Bước 2: Tính giá trị lớn nhất của một subarray

# Theo đề:

# [

# value = \max(subarray) - \min(subarray)

# ]

# Giá trị lớn nhất có thể đạt được là:

# [

# 5 - 1 = 4

# ]

# Bước 3: Chọn subarray tốt nhất k lần

# Đề bài cho phép:



# Chọn cùng một subarray nhiều lần.

# Các subarray có thể trùng nhau.

# Vì vậy:



# 4 + 4 + 4 = 12

# hay:

# [

# 3 \times 4 = 12

# ]

# Kết quả:



# 12

# Thuật toán

# 1. Tìm phần tử lớn nhất của mảng.

# 2. Tìm phần tử nhỏ nhất của mảng.

# 3. Tính hiệu: max - min.

# 4. Nhân với k.

# 5. Trả về kết quả.

# Độ phức tạp

# max(nums) : O(n)

# min(nums) : O(n)

# Tổng cộng:



# Thời gian: O(n)

# Bộ nhớ phụ: O(1)

# Phiên bản ngắn gọn như lời giải gốc

from typing import List

class Solution:

    def maxTotalValue(self, nums: List[int], k: int) -> int:

        # Giá trị lớn nhất của một subarray là max(nums) - min(nums)

        # Chọn subarray đó k lần

        return k * (max(nums) - min(nums))