# Bài "Partition Array According to Given Pivot (08/06/2026)


# Đề bài

# Cho:



# Mảng số nguyên nums

# Một số nguyên pivot

# Hãy tạo một mảng mới sao cho:



# Tất cả phần tử nhỏ hơn pivot đứng trước.

# Tất cả phần tử bằng pivot đứng ở giữa.

# Tất cả phần tử lớn hơn pivot đứng sau.

# Thứ tự tương đối của các phần tử trong cùng một nhóm phải được giữ nguyên.

# Ví dụ 1

# nums = [9,12,5,10,14,3,10]

# pivot = 10

# Các phần tử:



# Nhỏ hơn 10: [9,5,3]

# Bằng 10: [10,10]

# Lớn hơn 10: [12,14]

# Kết quả:



# [9,5,3,10,10,12,14]

# Ví dụ 2

# nums = [-3,4,3,2]

# pivot = 2

# Các phần tử:



# Nhỏ hơn 2: [-3]

# Bằng 2: [2]

# Lớn hơn 2: [4,3]

# Kết quả:



# [-3,2,4,3]

# "Giữ nguyên thứ tự tương đối" nghĩa là gì?

# Giả sử:



# nums = [5,1,3,2]

# pivot = 4

# Các phần tử nhỏ hơn 4 là:



# [1,3,2]

# Trong mảng kết quả, chúng vẫn phải theo thứ tự:



# 1 trước 3 trước 2

# Không được đổi thành:



# [2,1,3]

# Ý tưởng đơn giản nhất

# Tạo 3 danh sách:



# less     : chứa số < pivot

# equal    : chứa số = pivot

# greater  : chứa số > pivot

# Duyệt qua mảng:



# for (int num : nums) {

#     if (num < pivot)

#         less.add(num);

#     else if (num == pivot)

#         equal.add(num);

#     else

#         greater.add(num);

# }

# Ghép lại:



# less + equal + greater

# Minh họa

# nums = [9,12,5,10,14,3,10]

# pivot = 10

# Sau khi duyệt:



# less    = [9,5,3]

# equal   = [10,10]

# greater = [12,14]

# Ghép:



# [9,5,3] + [10,10] + [12,14]



# = [9,5,3,10,10,12,14]

# Độ phức tạp

# Thời gian: O(n)

# Bộ nhớ phụ: O(n)

# Đây cũng là lời giải phổ biến và dễ hiểu nhất cho bài này.

# Thuật toán này khá thông minh vì nó không cần tạo 3 danh sách (less, equal, greater) mà chỉ dùng một mảng kết quả result.

# Ý tưởng chính

# Ta biết rằng kết quả cuối cùng sẽ có dạng:



# [ các số < pivot ][ các số = pivot ][ các số > pivot ]

# Nên ta:



# Đi từ trái sang phải để đưa các số < pivot vào đầu mảng.

# Đi từ phải sang trái để đưa các số > pivot vào cuối mảng.

# Những vị trí còn trống ở giữa chắc chắn phải là pivot.

# Ví dụ

# nums = [9,12,5,10,14,3,10]

# pivot = 10

# Ban đầu:



# result = [_,_,_,_,_,_,_]



# left = 0

# right = 6

# Vòng lặp

# for (int i = 0, j = n - 1; i < n; i++, j--)

# Mỗi vòng:



# i đi từ trái sang phải.

# j đi từ phải sang trái.

# Vòng 1

# i=0, nums[i]=9

# j=6, nums[j]=10

# 9 < 10



# result[left++] = 9;

# result = [9,_,_,_,_,_,_]

# left = 1

# Vòng 2

# i=1, nums[i]=12

# j=5, nums[j]=3

# 12 > 10 nhưng điều kiện bên trái chỉ xét < pivot.

# 3 không lớn hơn pivot.

# Không làm gì.

# Vòng 3

# i=2, nums[i]=5

# j=4, nums[j]=14

# 5 < 10



# result = [9,5,_,_,_,_,_]

# left = 2

# 14 > 10



# result = [9,5,_,_,_,_,14]

# right = 5

# Vòng 4

# i=3, nums[i]=10

# j=3, nums[j]=10

# Không làm gì.

# Vòng 5

# i=4, nums[i]=14

# j=2, nums[j]=5

# Không làm gì.

# Vòng 6

# i=5, nums[i]=3

# j=1, nums[j]=12

# 3 < 10



# result = [9,5,3,_,_,_,14]

# left = 3

# 12 > 10



# result = [9,5,3,_,_,12,14]

# right = 4

# Vòng 7

# i=6, nums[i]=10

# j=0, nums[j]=9

# Không làm gì.

# Sau vòng lặp

# result = [9,5,3,_,_,12,14]

# left = 3

# right = 4

# Những vị trí còn trống:



# index 3,4

# chính là nơi dành cho các phần tử bằng pivot.

# Fill pivot

# while(left <= right){

#     result[left++] = pivot;

# }

# Sau khi điền:



# result = [9,5,3,10,10,12,14]

# Tại sao vẫn giữ đúng thứ tự?

# Nhóm < pivot

# Ta duyệt từ trái sang phải:



# if(nums[i] < pivot)

#     result[left++] = nums[i];

# Ví dụ:



# 9 → 5 → 3

# được ghi theo đúng thứ tự xuất hiện.

# Nhóm > pivot

# Ta duyệt:



# j = n-1 → 0

# và ghi:



# result[right--] = nums[j];

# Ví dụ:



# 12,14

# Trong quá trình duyệt ngược:



# 14 được ghi cuối cùng

# 12 được ghi trước 14

# Kết quả cuối cùng:



# ...,12,14

# vẫn giữ nguyên thứ tự ban đầu.

# Chứng minh nhóm > pivot vẫn đúng thứ tự

# Ví dụ:



# nums = [12,14,20]

# Duyệt từ phải:



# 20 -> result[2]

# 14 -> result[1]

# 12 -> result[0]

# Kết quả:



# [12,14,20]

# Thứ tự được bảo toàn.

# Độ phức tạp

# Thời gian: O(n)

# Bộ nhớ: O(n) (mảng result)

# Ý nghĩa của đoạn static

# static{

#     for(int i=0;i<300;i++)

#         pivotArray(new int[2],0);

# }

# Đoạn này không liên quan đến thuật toán. Một số người trên LeetCode thêm các đoạn như vậy để tác động đến cách JVM khởi tạo hoặc tối ưu benchmark. Bạn có thể bỏ hoàn toàn mà kết quả thuật toán không thay đổi.

# import java.util.*;

# public class Main {

#     // Hàm partition mảng theo pivot
#     public static int[] pivotArray(int[] nums, int pivot) {
#         int n = nums.length;
#         int[] result = new int[n];

#         // left: vị trí tiếp theo để đặt phần tử < pivot
#         int left = 0;

#         // right: vị trí tiếp theo để đặt phần tử > pivot
#         int right = n - 1;

#         // Duyệt đồng thời từ trái và phải
#         for (int i = 0, j = n - 1; i < n; i++, j--) {

#             // Đưa các phần tử nhỏ hơn pivot vào đầu mảng
#             if (nums[i] < pivot) {
#                 result[left++] = nums[i];
#             }

#             // Đưa các phần tử lớn hơn pivot vào cuối mảng
#             if (nums[j] > pivot) {
#                 result[right--] = nums[j];
#             }
#         }

#         // Các vị trí còn lại ở giữa sẽ là pivot
#         while (left <= right) {
#             result[left++] = pivot;
#         }

#         return result;
#     }

#     public static void main(String[] args) {
#         Scanner sc = new Scanner(System.in);

#         // Nhập số phần tử của mảng
#         System.out.print("Nhap so phan tu n: ");
#         int n = sc.nextInt();

#         int[] nums = new int[n];

#         // Nhập các phần tử của mảng
#         System.out.println("Nhap cac phan tu:");
#         for (int i = 0; i < n; i++) {
#             nums[i] = sc.nextInt();
#         }

#         // Nhập pivot
#         System.out.print("Nhap pivot: ");
#         int pivot = sc.nextInt();

#         // Gọi hàm xử lý
#         int[] result = pivotArray(nums, pivot);

#         // In kết quả
#         System.out.println("Mang sau khi partition:");
#         for (int num : result) {
#             System.out.print(num + " ");
#         }

#         sc.close();
#     }
# }

# Đây là một lời giải Python rất ngắn gọn và hiệu quả.



# Ý tưởng

# Thay vì tạo 3 danh sách:



# less = []

# equal = []

# greater = []

# ta chỉ dùng:



# Phần đầu của nums để lưu các số < pivot

# R để lưu các số > pivot

# m để đếm số lượng phần tử == pivot

# Cuối cùng ghép lại:



# nums[:l] + [pivot] * m + R

# Phân tích từng biến

# l = 0

# Vị trí tiếp theo để ghi phần tử < pivot

# m = 0

# Đếm số phần tử bằng pivot

# R = []

# Chứa các phần tử > pivot

# Ví dụ

# nums = [9,12,5,10,14,3,10]

# pivot = 10

# Ban đầu:



# l = 0

# m = 0

# R = []

# x = 9

# 9 < 10

# Ghi vào đầu mảng:



# nums[0] = 9

# l = 1

# x = 12

# 12 > 10

# # Đưa vào R:



# R = [12]

# x = 5

# 5 < 10

# nums[1] = 5

# l = 2

# x = 10

# 10 == pivot

# m = 1

# x = 14

# R = [12,14]

# x = 3

# nums[2] = 3

# l = 3

# x = 10

# m = 2

# Sau vòng lặp

# nums = [9,5,3,...]

# l = 3

# m = 2

# R = [12,14]

# Ghép kết quả

# nums[:l]

# lấy:



# [9,5,3]

# [pivot] * m

# là:



# [10,10]

# Ghép với:



# R = [12,14]

# Kết quả:



# [9,5,3,10,10,12,14]

# Tại sao giữ nguyên thứ tự?

# Nhóm < pivot

# Ta duyệt từ trái sang phải:



# for x in nums:

# và ghi lần lượt:



# nums[l] = x

# l += 1

# nên:



# 9 → 5 → 3

# vẫn giữ nguyên thứ tự.

# Nhóm == pivot

# Chỉ đếm số lượng:



# m += 1

# sau đó tạo:



# [pivot] * m

# Nhóm > pivot

# Ta append:



# R.append(x)

# theo đúng thứ tự xuất hiện.

# Ví dụ:



# 12

# 14

# sẽ thành:



# [12,14]

# Code có chú thích

from typing import List

class Solution:

    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:



        n = len(nums)



        # Nếu chỉ có 1 phần tử thì trả về luôn

        if n == 1:

            return nums



        # Chứa các phần tử > pivot

        R = []



        # l: số lượng phần tử < pivot

        l = 0



        # m: số lượng phần tử == pivot

        m = 0



        # Duyệt toàn bộ mảng

        for x in nums:



            # Nếu nhỏ hơn pivot

            if x < pivot:



                # Ghi vào đầu mảng

                nums[l] = x

                l += 1



            # Nếu lớn hơn pivot

            elif x > pivot:



                # Đưa vào danh sách R

                R.append(x)



            # Nếu bằng pivot

            else:

                m += 1



        # Ghép:

        # [các phần tử < pivot]

        # + [pivot lặp lại m lần]

        # + [các phần tử > pivot]

        return nums[:l] + [pivot] * m + R

# Độ phức tạp

# Thời gian: O(n)

# Bộ nhớ phụ:

# R chứa tối đa n phần tử

# Tổng cộng: O(n)

# Đây là một cách viết rất Pythonic vì không cần tạo riêng cả ba mảng less, equal, greater mà chỉ dùng một danh sách phụ R và một biến đếm m.