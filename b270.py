# // Bài Sequential Digits (13/07/2026)
# // Ý nghĩa của đề bài

# // Cho hai số nguyên low và high, hãy trả về danh sách tất cả các số có chữ số tuần tự trong khoảng [low, high], theo thứ tự tăng dần.



# // Số có chữ số tuần tự là gì?

# // Một số được gọi là sequential digits nếu:



# // Mỗi chữ số đứng sau bằng chữ số đứng trước + 1.

# // Các chữ số phải nằm sát nhau theo đúng thứ tự tăng dần.

# // Ví dụ

# // SốCó phải sequential digits?Giải thích123✔️1 → 2 → 3, mỗi bước tăng 14567✔️4 → 5 → 6 → 72345✔️2 → 3 → 4 → 5124❌2 không bằng 1 + 1, 4 không bằng 2 + 1135❌Các chữ số không liên tiếp98❌9 → 8 là giảm, không phải tăng liên tiếp

# // Ví dụ đầu vào và đầu ra

# // Giải thích:



# // 123 nằm trong khoảng 100 đến 300 và các chữ số tăng liên tiếp.

# // 234 cũng thỏa mãn điều kiện.

# // Các số như 345, 456 lớn hơn 300 nên không được lấy.

# // Một ví dụ khác

# // Ở đây:



# // 1234, 2345, …, 6789 đều có chữ số tăng liên tiếp.

# // 12345 cũng hợp lệ và nằm trong khoảng ≤ 13000.

# // 23456 lớn hơn 13000 nên không được lấy.

# // Điểm cần chú ý

# // Các chữ số phải tăng dần liên tiếp, không được bỏ số ở giữa.

# // Số phải nằm trong khoảng low ≤ number ≤ high.

# // Kết quả trả về là một mảng các số theo thứ tự tăng dần.

# // Ý tưởng sinh các số sequential digits

# // Ta có thể bắt đầu từ chuỗi "123456789", rồi lấy các đoạn con liên tiếp:



# // Độ dài 2: 12, 23, 34, …, 89.

# // Độ dài 3: 123, 234, 345, …, 789.

# // Độ dài 4: 1234, 2345, …, 6789.

# // Với mỗi số tạo được, chỉ cần kiểm tra xem nó có nằm trong khoảng [low, high] hay không.

# // Tóm lại: Sequential Digits là các số có các chữ số đứng cạnh nhau và mỗi chữ số sau lớn hơn chữ số trước đúng 1 đơn vị.





# import java.util.*;

# public class b271{

#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#        int low = sc.nextInt();

#         int high = sc.nextInt();






#         // Gọi hàm tìm kết quả

#         List<Integer> result = sequentialDigits(low, high);



#         // In kết quả

#         System.out.println("Cac so co chu so lien tiep:");

#         for (int num : result) {

#             System.out.print(num + " ");

#         }
#         sc.close();
#     }
#  public static List<Integer> sequentialDigits(int low, int high) {

#         // Danh sách lưu kết quả

#         List<Integer> ans = new ArrayList<>();



#         // Chuỗi chứa các chữ số liên tiếp từ 1 đến 9

#         String s = "123456789";



#         // Chuyển low và high sang String để lấy số lượng chữ số

#         String l = String.valueOf(low);

#         String h = String.valueOf(high);



#         // Duyệt theo độ dài của số

#         for (int len = l.length(); len <= h.length(); len++) {



#             // Vị trí bắt đầu lấy chuỗi con

#             // Ví dụ len = 3 thì start chạy từ 0 đến 6

#             for (int start = 0; start <= 9 - len; start++) {



#                 // Lấy chuỗi con và chuyển thành số nguyên

#                 int num = Integer.parseInt(s.substring(start, start + len));



#                 // Nếu số nằm trong khoảng yêu cầu thì thêm vào kết quả

#                 if (num >= low && num <= high) {

#                     ans.add(num);

#                 }

#             }

#         }



#         return ans;

# }}




#     // Hàm main


# // Ví dụ chạy

# // Input



# // Nhap low: 100

# // Nhap high: 300

# // Output



# // Cac so co chu so lien tiep:

# // 123 234

# // Ý tưởng thuật toán

# // Tạo chuỗi "123456789".

# // Với mỗi độ dài từ số chữ số của low đến số chữ số của high:

# // Lấy tất cả các chuỗi con có độ dài đó.

# // Chuyển chuỗi con thành số nguyên.

# // Nếu số nằm trong đoạn [low, high] thì thêm vào danh sách kết quả.

# // Độ phức tạp:



# // Thời gian: O(1) (tối đa chỉ sinh ra 36 số ứng viên).

# // Không gian: O(1) (không tính danh sách kết quả).

# Optimized tool selectionI will explain the solution in Vietnamese and annotate the code directly so it is easier to follow.

# ## Giải thích thuật toán

# Ý tưởng rất đơn giản:

# - Tất cả số “sequential digits” đều có dạng như:
#   - 12, 23, 34, 45, ...
#   - 123, 234, 345, ...
#   - 1234, 2345, ...
# - Những số này đều là các chuỗi con liên tiếp của chuỗi "123456789".

# Do đó, ta chỉ cần:
# 1. Duyệt qua tất cả các độ dài có thể từ số chữ số của low đến số chữ số của high.
# 2. Với mỗi độ dài, duyệt qua các vị trí bắt đầu từ 0 đến 9 - length.
# 3. Cắt chuỗi con tương ứng, chuyển thành số, rồi kiểm tra xem nó có nằm trong khoảng [low, high] hay không.
# 4. Nếu phù hợp thì thêm vào kết quả.

# ## Code đã được chú thích

# ```python
from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []

        # Chuỗi chứa tất cả các số tăng dần từng chữ số
        # Ví dụ: "123456789" -> có thể tạo ra 12, 23, 34, ..., 123, 234, ...
        s = "123456789"

        # Chuyển low và high thành chuỗi để lấy số chữ số
        l = str(low)
        h = str(high)

        # Duyệt qua mọi độ dài có thể từ số chữ số của low đến số chữ số của high
        for length in range(len(l), len(h) + 1):

            # Với mỗi độ dài, xét các vị trí bắt đầu khác nhau
            # Ví dụ length = 3 thì start có thể là 0,1,2,3,4,5,6
            for start in range(0, 10 - length):

                # Cắt chuỗi con có độ dài = length từ vị trí start
                num = int(s[start:start + length])

                # Nếu số này nằm trong khoảng [low, high] thì thêm vào kết quả
                if low <= num <= high:
                    ans.append(num)

        return ans
# ```

# ## Ví dụ

# Nếu:
# - low = 100
# - high = 300

# Thì các số hợp lệ sẽ là:
# - 123
# - 234

# ## Độ phức tạp

# - Khoảng cách duyệt khá nhỏ vì chỉ xét các chuỗi con của "123456789".
# - Vì vậy, thuật toán chạy rất nhanh.