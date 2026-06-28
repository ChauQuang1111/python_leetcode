# // Bài Maximum Element After Decreasing and Rearranging (28/06/2026)

# // Cho một mảng số nguyên dương arr.

# // Bạn được phép thực hiện hai thao tác không giới hạn số lần:



# // Giảm giá trị của một phần tử xuống bất kỳ số nguyên dương nào nhỏ hơn hoặc bằng nó.

# // Hoán đổi (rearrange) các phần tử trong mảng theo bất kỳ thứ tự nào.

# // Sau khi thực hiện các thao tác trên, mảng phải thỏa mãn:



# // Phần tử đầu tiên bằng 1.

# // Hiệu tuyệt đối giữa hai phần tử kề nhau không vượt quá 1.

# // Hãy tìm giá trị lớn nhất có thể của phần tử lớn nhất trong mảng.

# // Ví dụ 1

# // Input: arr = [2,2,1,2,1]

# // Output: 2

# // Một cách sắp xếp:



# // [1,1,2,2,2]

# // Kiểm tra:



# // phần tử đầu = 1 ✅

# // |1-1| = 0

# // |1-2| = 1

# // |2-2| = 0

# // |2-2| = 0

# // Giá trị lớn nhất = 2.

# // Ví dụ 2

# // Input: arr = [100,1,1000]

# // Output: 3

# // Ta có thể:



# // [1,100,1000]

# // Giảm:



# // [1,2,3]

# // Điều này hợp lệ vì:



# // bắt đầu bằng 1

# // chênh lệch từng cặp là 1

# // Kết quả lớn nhất là 3.

# // Ví dụ 3

# // Input: arr = [1,2,3,4,5]

# // Output: 5

# // Mảng đã hợp lệ nên đáp án là 5.

# // Điều kiện quan trọng nhất

# // Sau khi hoàn thành, mảng phải có dạng gần giống:



# // 1

# // 1 2

# // 1 2 3

# // 1 2 3 4

# // ...

# // Không nhất thiết tăng đúng 1 mỗi lần, nhưng không được nhảy quá 1.

# // Ví dụ



# // 1 2 2 3 4

# // hợp lệ.

# // Còn



# // 1 2 4

# // không hợp lệ vì



# // |4-2| = 2 > 1

# // Tại sao được giảm số?

# // Ví dụ



# // [1,5,9]

# // Ta không được tăng số.

# // Chỉ được giảm.

# // Có thể biến thành



# // [1,2,3]

# // Nhưng không thể biến thành



# // [1,5,6]

# // vì không được tăng 5 lên 6, cũng không thể giữ 9 vì khoảng cách với 5 là quá lớn.

# // Mục tiêu thực sự

# // Sau khi sắp xếp tăng dần, ta muốn tạo dãy càng dài càng tốt:



# // 1,2,3,4,5,...

# // nhưng không được tăng bất kỳ số nào, chỉ được giảm.

# // Ví dụ



# // arr = [4,2,6,8]

# // Sắp xếp:



# // [2,4,6,8]

# // Ta cần phần tử đầu bằng 1 nên giảm 2 xuống 1:



# // [1,4,6,8]

# // Sau đó:



# // 4 có thể giảm xuống 2

# // 6 có thể giảm xuống 3

# // 8 có thể giảm xuống 4

# // Kết quả:



# // [1,2,3,4]

# // Đáp án là 4.

# // Ý tưởng của thuật toán

# // Sắp xếp mảng theo thứ tự tăng dần.

# // Đặt phần tử đầu tiên bằng 1.

# // Với mỗi phần tử tiếp theo:

# // Nếu nó lớn hơn previous + 1, ta giảm nó xuống previous + 1.

# // Nếu nó nhỏ hơn hoặc bằng previous + 1, giữ nguyên (vì không thể tăng nó).

# // Giá trị cuối cùng sau khi xử lý chính là đáp án.

# // Độ phức tạp:



# // Sắp xếp: O(n log n)

# // Duyệt mảng: O(n)

# // Tổng: O(n log n).




# // Đây là một lời giải Counting Sort (đếm tần suất) có độ phức tạp O(n) thay vì phải sắp xếp O(n log n).

# // Ý tưởng của thuật toán

# // Giả sử có:



# // arr = [2,2,1,2,1]

# // Sau khi sắp xếp ta được



# // 1 1 2 2 2

# // Đáp án là 2.

# // Nhưng thuật toán này không sắp xếp, mà chỉ đếm xem mỗi số xuất hiện bao nhiêu lần.

# // Bước 1: Đếm số lần xuất hiện

# // for (int v : arr) {

# //     if (v <= n)

# //         freqs[v - 1]++;

# // }

# // Ví dụ



# // arr = [2,2,1,2,1]

# // n = 5

# // Sau vòng lặp



# // freqs



# // giá trị : 1 2 3 4 5

# // tần suất: 2 3 0 0 0

# // Tại sao chỉ đếm số ≤ n ?

# // Giả sử



# // n = 5



# // arr = [100,1000,2,1,4]

# // Muốn tạo dãy hợp lệ thì giá trị lớn nhất không bao giờ vượt quá n.

# // Ví dụ



# // 1 2 3 4 5

# // đã là lớn nhất rồi.

# // Nên



# // 100

# // 1000

# // không cần phân biệt.

# // Biến c

# // int c = -1;

# // c biểu diễn



# // số phần tử dư sau khi lấp đầy các vị trí từ 1 đến giá trị hiện tại.

# // Ví dụ



# // freqs



# // 1 : 3 lần

# // 2 : 1 lần

# // 3 : 0

# // Ta duyệt.

# // v = 0 (giá trị 1)

# // c += freqs[0];

# // Ban đầu



# // c = -1



# // freqs[0]=3

# // sau đó



# // c=2

# // Nghĩa là

# // Có 3 số 1.

# // Ta chỉ cần



# // 1

# // một số.

# // Còn dư



# // 2

# // Kiểm tra



# // if (c > v)

# // Ở đây



# // 2 > 0

# // Đúng.

# // maxe

# // maxe -= c-v;

# // Ở đây



# // c-v



# // =



# // 2-0



# // =



# // 2

# // Nghĩa là có 2 số bị dư, nên đáp án lớn nhất phải giảm đi 2.

# // Ý nghĩa

# // Nếu có quá nhiều số nhỏ

# // Ví dụ



# // 1 1 1 1 1

# // thì không thể tạo



# // 1 2 3 4 5

# // được.

# // Chỉ tạo được



# // 1 2

# // Đáp án giảm.

# // Vì sao

# // c=v;

# // ?

# // Sau khi bỏ bớt phần dư,

# // ta giữ lại đúng số lượng phần tử cần thiết.

# // Ví dụ đầy đủ

# // arr



# // 1 1 1 4 5

# // n=5

# // Đếm



# // freq



# // 1 :3

# // 2 :0

# // 3 :0

# // 4 :1

# // 5 :1

# // v=0

# // c=-1+3=2

# // Có dư 2.



# // maxe=5



# // maxe-=2



# // =3

# // Đáp án tối đa còn 3.

# // v=1

# // freq=0



# // c=0

# // Không dư.

# // v=2

# // freq=0



# // c=0

# // Kết quả



# // maxe=3

# // Thật vậy



# // 1 1 1 4 5



# // ↓



# // 1 2 3

# // Đáp án là 3.

# // Ý nghĩa của vòng for

# // for (int v = 0; v < maxe; v++)

# // v không phải giá trị trong mảng.

# // Nó biểu diễn:



# // v = 0 → số 1



# // v = 1 → số 2



# // v = 2 → số 3



# // ...

# // Giải thích từng dòng code

# import java.util.*;

# public class b261{
  
#     // Mảng đếm tần suất xuất hiện của các giá trị.

#     // freqs[i] lưu số lần xuất hiện của giá trị (i + 1).

#     public  static final int MAXN = 100000;
#     public static int[] freqs = new int[MAXN];
#     static Scanner sc = new Scanner(System.in);
#     public static void main(String[] args) {
#         int n = sc.nextInt();
#         int[] arr = new int[n];
#         for (int i = 0; i < n; i++) {

#             arr[i] = sc.nextInt();

#         }
#         System.out.println(maximumElementAfterDecrementingAndRearranging(arr));
#         sc.close();
#     }
#  public static int maximumElementAfterDecrementingAndRearranging(int[] arr) {
#         int n = arr.length;
#         // Nếu chỉ có 1 phần tử thì luôn có thể giảm về 1.
#         if (n == 1)

#             return 1;
#         // Đếm tần suất của các số <= n.

#         // Các số lớn hơn n không cần quan tâm vì đáp án tối đa không vượt quá n.

#         for (int v : arr) {

#             if (v <= n)

#                 freqs[v - 1]++;

#         }
#         // maxe là đáp án lớn nhất hiện tại.
#         int maxe = n;
#         // c lưu số lượng phần tử dư sau khi lấp đầy các giá trị nhỏ hơn hoặc bằng hiện tại.
#         int c = -1;
#         // Duyệt qua từng giá trị từ 1 đến maxe.
#         for (int v = 0; v < maxe; v++) {
#             // Cộng số lượng phần tử có giá trị (v + 1).
#             c += freqs[v];
#             // Nếu số phần tử nhiều hơn số vị trí có thể chứa

#             if (c > v) {
#                 // Giảm đáp án đi đúng số phần tử dư.
#                 maxe -= (c - v);
#                 // Sau khi loại phần dư thì chỉ còn vừa đủ.
#                 c = v;

#             }
#             // Reset để lần gọi hàm sau không bị ảnh hưởng.
#             freqs[v] = 0;

#         }
#         // Xóa nốt phần còn lại trong mảng tần suất.
#         Arrays.fill(freqs, maxe, n, 0);
#         return maxe;
# }
# }

# // Tóm tắt ý tưởng

# # // Đếm tần suất các số từ 1 đến n.

# # // Duyệt từ giá trị nhỏ đến lớn để xem có thừa phần tử ở mỗi mức hay không.

# # // Nếu thừa, không thể sắp xếp thành dãy hợp lệ 1, 2, 3, ..., nên phải giảm giá trị lớn nhất (maxe) tương ứng với số phần tử dư.

# # // Không cần sắp xếp mảng, nên thuật toán chạy trong O(n) với O(n) bộ nhớ.

# Đây là lời giải Greedy + Sorting với độ phức tạp O(n log n) do phải sắp xếp mảng.

# Ý tưởng của thuật toán

# Sau khi được phép:



# Sắp xếp lại mảng.

# Giảm bất kỳ phần tử nào xuống số nhỏ hơn hoặc bằng nó.

# Ta luôn muốn tạo dãy:



# 1, 2, 3, 4, 5, ...

# vì khi tạo được dãy càng dài thì phần tử lớn nhất càng lớn.

# Biến target chính là giá trị tiếp theo mà ta muốn tạo được.

# Bước 1: Sắp xếp

# arr.sort()

# Ví dụ



# arr = [2,2,1,2,1]

# Sau khi sắp xếp



# 1 1 2 2 2

# Ta sẽ duyệt từ nhỏ đến lớn.

# Bước 2: Khởi tạo

# target = 1

# Ban đầu ta muốn tạo số



# 1

# Bước 3: Duyệt từng phần tử

# for v in arr:

# Nếu



# v >= target

# thì có nghĩa là:

# Phần tử này có thể giảm xuống thành target.

# Ví dụ



# target = 3



# v = 5

# Ta giảm



# 5 → 3

# được.

# Khi đã tạo được số 3 thì tiếp tục muốn tạo số 4.



# target += 1

# Ví dụ 1

# arr = [2,2,1,2,1]

# Sau khi sort



# 1 1 2 2 2

# vtarget trướcĐiều kiệntarget sau11Đúng212Sai222Đúng323Sai323Sai3

# Kết thúc



# target = 3

# Đáp án



# target-1=2

# Ví dụ 2

# arr = [100,1,1000]

# Sort



# 1 100 1000

# vtarget11→21002→310003→4

# Kết quả



# target=4



# return 3

# Ta tạo được



# 1 2 3

# Ví dụ 3

# arr = [1,2,3,4]

# vtarget11→222→333→444→5

# Đáp án



# 5-1=4

# Tại sao điều kiện là

# if v >= target:

# Ví dụ



# target = 4



# v = 6

# Ta có thể giảm



# 6 → 4

# được.

# Nếu



# v = 2



# target = 4

# thì không thể tăng



# 2 → 4

# nên bỏ qua.

# Tại sao trả về

# target-1

# Giả sử



# target = 6

# Điều này nghĩa là

# Ta đã tạo thành công



# 1 2 3 4 5

# và đang muốn tạo tiếp số 6.

# Vậy số lớn nhất đã tạo được là



# 5

# nên trả về



# target-1

# Code có chú thích

class Solution:

    def maximumElementAfterDecrementingAndRearranging(self, arr):



        # Bước 1: Sắp xếp mảng theo thứ tự tăng dần

        arr.sort()



        # target là giá trị tiếp theo mà ta muốn tạo.

        # Ban đầu luôn phải tạo được số 1.

        target = 1



        # Duyệt từng phần tử từ nhỏ đến lớn

        for v in arr:



            # Nếu phần tử hiện tại >= target,

            # ta có thể giảm nó xuống đúng bằng target.

            if v >= target:



                # Đã tạo được target,

                # tiếp tục muốn tạo giá trị tiếp theo.

                target += 1



        # target hiện đang là giá trị muốn tạo tiếp theo,

        # nên giá trị lớn nhất đã tạo được là target - 1.

        return target - 1

# Trực quan thuật toán

# Ví dụ:



# arr = [4,2,6,8]

# Sau khi sắp xếp:



# 2 4 6 8

# Quá trình duyệt:

# Phần tử (v)target trướcCó tạo được không?target sau21Có (2 → 1)242Có (4 → 2)363Có (6 → 3)484Có (8 → 4)5

# Cuối cùng:



# Đã tạo được dãy 1, 2, 3, 4.

# target = 5, nên đáp án là 5 - 1 = 4.

# Ý tưởng cốt lõi

# Biến target luôn đại diện cho giá trị nhỏ nhất tiếp theo mà ta cần tạo. Mỗi khi gặp một phần tử v đủ lớn (v >= target), ta "dùng" nó để tạo đúng target (bằng cách giữ nguyên hoặc giảm xuống), rồi tăng target lên. Đây là chiến lược tham lam (greedy): luôn tạo giá trị nhỏ nhất còn thiếu trước để có cơ hội tạo được dãy dài nhất.