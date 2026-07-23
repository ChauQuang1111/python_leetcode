# // Bài "Number of Unique XOR Triplets" (23/07/2026)

# // You are given an array nums.
# // A XOR triplet is the value of nums[i] ^ nums[j] ^ nums[k] where i <= j <= k (hoặc có thể i < j < k tùy phiên bản đề).
# // Return the number of distinct XOR triplet values.
# // Giải thích từng phần
# // ^ là phép XOR bit.
# // Một triplet là chọn 3 phần tử trong mảng.
# // Với mỗi bộ 3, tính giá trị:

# // nums[i] ^ nums[j] ^ nums[k]
# // Cuối cùng chỉ quan tâm có bao nhiêu giá trị XOR khác nhau, không phải có bao nhiêu bộ ba.
# // Ví dụ 1
# // nums = [1,2]
# // Nếu đề cho phép i <= j <= k thì có các bộ:

# // (1,1,1): 1^1^1 = 1
# // (1,1,2): 1^1^2 = 2
# // (1,2,2): 1^2^2 = 1
# // (2,2,2): 2^2^2 = 2
# // Các giá trị XOR thu được là

# // {1,2}
# // Đáp án:

# // 2
# // Ví dụ 2
# // nums = [1,2,3]
# // Nếu i < j < k thì chỉ có

# // 1 ^ 2 ^ 3 = 0
# // Đáp án là

# // 1
# // Nếu đề cho phép lặp chỉ số (i <= j <= k) thì sẽ có nhiều bộ hơn:

# // 1^1^1 = 1
# // 1^1^2 = 2
# // 1^1^3 = 3
# // 1^2^3 = 0
# // ...
# // Khi đó tập kết quả có thể là

# // {0,1,2,3}
# // "Unique" nghĩa là gì?
# // Ví dụ ta tính được:

# // 1
# // 2
# // 2
# // 3
# // 1
# // 0
# // 0
# // Thì các giá trị khác nhau là

# // {0,1,2,3}
# // Có 4 giá trị unique.
# // Mục tiêu của bài
# // Không phải tìm XOR lớn nhất hay nhỏ nhất.
# // Mà là:

# // Sinh (hoặc suy luận) tất cả giá trị

# // nums[i] ^ nums[j] ^ nums[k]
# // Bỏ các giá trị trùng.
# // Trả về số lượng giá trị còn lại.
# // 📌 Nếu bạn đang nói đến bài LeetCode 3158 / 3193 / 3473 "Number of Unique XOR Triplets", hãy gửi link hoặc nguyên văn đề bài, vì hiện có nhiều bài LeetCode có tên gần giống nhau nhưng điều kiện chọn bộ ba (i < j < k, i <= j <= k, hay mảng là hoán vị) khác nhau. Mình sẽ giải thích đúng theo phiên bản đó.



# // Đoạn code này nhìn khá "lạ" vì không hề tính XOR của các bộ ba, mà sử dụng một tính chất toán học của bài toán (điều kiện của đề là nums là một hoán vị của các số từ 1 đến n). Vì vậy thuật toán chỉ cần trả về đáp án theo công thức.

# // Giải thích thuật toán
# // Giả sử:

# // nums = [1,2,3,...,n]
# // Sau khi phân tích tính chất XOR của mọi bộ ba, ta có:

# // Nếu n < 3
# // Không thể tạo đủ các bộ ba khác nhau theo yêu cầu.
# // Đáp án chính là n.
# // Nếu n >= 3
# // Tất cả các giá trị XOR khác nhau sẽ tạo thành dãy từ:

# // 0 đến (2^k - 1)
# // với 2^k là lũy thừa của 2 đầu tiên lớn hơn n.
# // Ví dụ
# // nLũy thừa của 2 đầu tiên > nĐáp án34448858868878881616
# // Cho nên bài toán chỉ cần tìm lũy thừa của 2 đầu tiên lớn hơn n.
# // Giải thích từng dòng code
# // class Solution {

# //     // Hàm trả về số lượng giá trị XOR khác nhau
# //     public int uniqueXorTriplets(int[] nums) {

# //         // Lấy số phần tử của mảng
# //         int n = nums.length;

# //         // Nếu mảng có ít hơn 3 phần tử
# //         // Theo tính chất của bài toán đáp án chính là n
# //         if (n < 3) {
# //             return n;
# //         }

# //         // Khởi tạo bằng 2^0 = 1
# //         int nextPowerOfTwo = 1;

# //         // Tìm lũy thừa của 2 đầu tiên lớn hơn n
# //         while (nextPowerOfTwo <= n) {
# //             nextPowerOfTwo <<= 1;
# //             // Dịch trái 1 bit tương đương nhân đôi
# //         }

# //         // Trả về kết quả
# //         return nextPowerOfTwo;
# //     }

# // }
# // Thêm hàm main dùng Scanner

# import java.util.*;

# public class b275{
#     static Scanner sc = new Scanner(System.in);
#     public static void main(String[] args) {
#         int n = sc.nextInt();

#         int[] nums = new int[n];

#         for (int i = 0; i < n; i++) {
#             nums[i] = sc.nextInt();
#         }

        

#         // Gọi hàm và in kết quả
#         int ans = uniqueXorTriplets(nums);

#         System.out.println(ans);

#         sc.close();
#     }
#   // Hàm trả về số lượng giá trị XOR khác nhau
#     public  static int uniqueXorTriplets(int[] nums) {

#         // Số phần tử của mảng
#         int n = nums.length;

#         // Nếu có ít hơn 3 phần tử
#         // Đáp án chính là n
#         if (n < 3) {
#             return n;
#         }

#         // Bắt đầu từ 2^0 = 1
#         int nextPowerOfTwo = 1;

#         // Tìm lũy thừa của 2 đầu tiên lớn hơn n
#         while (nextPowerOfTwo <= n) {
#             nextPowerOfTwo <<= 1; // Nhân đôi
#         }

#         return nextPowerOfTwo;
#     }

# }

# // Ví dụ chạy
# // Input
# // Nhap n: 5
# // Nhap mang:
# // 1 2 3 4 5
# // Quá trình
# // n = 5

# // nextPowerOfTwo = 1
# // 1 <= 5  => 2
# // 2 <= 5  => 4
# // 4 <= 5  => 8
# // 8 > 5   => dừng
# // Output
# // So luong gia tri XOR khac nhau: 8
# // Độ phức tạp
# // Thời gian: O(log n) vì mỗi vòng lặp nhân đôi giá trị (1 → 2 → 4 → 8 → ...).
# // Bộ nhớ: O(1) vì chỉ sử dụng một vài biến.
# // Lưu ý quan trọng: Thuật toán này chỉ đúng với phiên bản LeetCode mà nums là một hoán vị của các số từ 1 đến n. Nếu nums là một mảng bất kỳ, công thức này sẽ không đúng, và phải dùng thuật toán khác để tính các giá trị XOR của các bộ ba.

# Đây là lời giải Python của cùng bài toán. Thuật toán không duyệt qua các bộ ba, mà dựa trên tính chất toán học của bài toán.
# Ý tưởng thuật toán
# Giả sử:

# nums = [1,2,3,...,n]
# (vì đề bài cho nums là hoán vị của các số từ 1 đến n)
# Sau khi chứng minh tính chất XOR, ta có:

# Nếu n = 1
# Chỉ có một giá trị XOR.
# Kết quả là 1.
# Nếu n = 2
# Có hai giá trị XOR khác nhau.
# Kết quả là 2.
# Nếu n >= 3
# Các giá trị XOR có thể tạo thành toàn bộ các số từ:

# 0 → 2^k - 1
# trong đó 2^k là lũy thừa của 2 đầu tiên lớn hơn hoặc bằng n + 1.
# Do đó chỉ cần tìm k.
# Ví dụ
# ngb2^gbĐáp án32444388538863887388841616Giải thích từng dòng code
# class Solution:

#     # Hàm trả về số lượng giá trị XOR khác nhau
#     def uniqueXorTriplets(self, nums: List[int]) -> int:

#         # Lấy số phần tử của mảng
#         n = len(nums)

#         # Trường hợp chỉ có 2 phần tử
#         if n == 2:
#             return 2

#         # Trường hợp chỉ có 1 phần tử
#         if n == 1:
#             return 1

#         # gb là số mũ của lũy thừa 2
#         gb = 0

#         # Tìm số mũ nhỏ nhất sao cho 2^gb > n
#         while n >= (1 << gb):
#             gb += 1

#         # (1 << gb) = 2^gb
#         # (1 << gb) - 1 = giá trị lớn nhất có gb bit đều bằng 1
#         #
#         # Đáp án cuối cùng là 2^gb
#         return max((1 << gb) - 1, n) + 1
# Code có đầy đủ chú thích
from typing import List

class Solution:

    # Hàm trả về số lượng giá trị XOR khác nhau
    def uniqueXorTriplets(self, nums: List[int]) -> int:

        # Lấy số phần tử của mảng
        n = len(nums)

        # Nếu chỉ có 2 phần tử
        # Theo tính chất bài toán đáp án là 2
        if n == 2:
            return 2

        # Nếu chỉ có 1 phần tử
        # Chỉ có đúng 1 giá trị XOR
        if n == 1:
            return 1

        # gb sẽ là số mũ của lũy thừa 2
        gb = 0

        # Tìm số mũ nhỏ nhất sao cho
        # 2^gb > n
        while n >= (1 << gb):
            gb += 1

        # (1 << gb) = 2^gb
        #
        # Ví dụ:
        # gb = 3
        # 1 << 3 = 8
        #
        # (1 << gb) - 1
        # = 7 (111₂)
        #
        # max(..., n) chỉ để đảm bảo giá trị không nhỏ hơn n.
        # Vì 2^gb > n nên biểu thức luôn trả về:
        #
        # (2^gb - 1) + 1 = 2^gb
        return max((1 << gb) - 1, n) + 1
# Ví dụ chạy
# Giả sử

# nums = [1,2,3,4,5]
# Khi đó

# n = 5

# gb = 0

# 5 >= 1  -> gb = 1
# 5 >= 2  -> gb = 2
# 5 >= 4  -> gb = 3
# 5 >= 8  -> Sai -> dừng
# Lúc này

# 1 << 3 = 8

# (1 << 3) - 1 = 7

# max(7,5) = 7

# 7 + 1 = 8
# Kết quả:

# 8
# Có thể rút gọn dòng cuối
# Vì sau vòng lặp luôn có:

# 2^gb > n
# nên:

# (1 << gb) - 1 >= n
# Do đó:

# max((1 << gb) - 1, n)
# luôn bằng

# (1 << gb) - 1
# Vì vậy dòng:

# return max((1 << gb) - 1, n) + 1
# có thể viết ngắn gọn thành:

# return 1 << gb
# Hai cách viết này cho kết quả hoàn toàn giống nhau, nhưng cách return 1 << gb ngắn gọn và dễ hiểu hơn.