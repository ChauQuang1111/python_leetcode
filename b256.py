# // //  Process String with Special Operations II (17/06/2026)



# // // Cho chuỗi s gồm chữ thường và 3 ký tự đặc biệt:

# // // *

# // // #

# // // %

# // // Cho số nguyên k.

# // // Ta duyệt chuỗi từ trái sang phải để tạo chuỗi result theo các quy tắc: (LeetCode Wiki)

# // // Ký tựÝ nghĩaa-zThêm ký tự vào cuối result*Xóa ký tự cuối của result (nếu có)#Nhân đôi result (result += result)%Đảo ngược result

# // // Sau khi xử lý hết s, trả về ký tự ở vị trí k của result (đánh số từ 0). Nếu k vượt quá độ dài chuỗi thì trả về '.'. (LeetCode Wiki)

# // // Ví dụ 1

# // // s = "a#b%*"

# // // k = 1

# // // Bắt đầu:



# // // result = ""

# // // Bước 1: 'a'

# // // result = "a"

# // // Bước 2: '#'

# // // Nhân đôi:



# // // "a" -> "aa"

# // // Bước 3: 'b'

# // // "aa" -> "aab"

# // // Bước 4: '%'

# // // Đảo ngược:



# // // "aab" -> "baa"

# // // Bước 5: '*'

# // // Xóa ký tự cuối:



# // // "baa" -> "ba"

# // // Kết quả cuối:



# // // result = "ba"

# // // Chỉ số:



# // // 0 -> b

# // // 1 -> a

# // // k = 1

# // // ⇒ Đáp án:



# // // 'a'

# // // Ví dụ 2

# // // s = "cd%#*#"

# // // k = 3

# // // 'c'

# // // "c"

# // // 'd'

# // // "cd"

# // // '%'

# // // "dc"

# // // '#'

# // // "dcdc"

# // // '*'

# // // "dcd"

# // // '#'

# // // "dcddcd"

# // // Chỉ số:



# // // 0 d

# // // 1 c

# // // 2 d

# // // 3 d

# // // 4 c

# // // 5 d

# // // k = 3

# // // ⇒



# // // 'd'

# // // (LeetCode Wiki)

# // // Điểm khó của bài II

# // // Ở bài I, độ dài chuỗi nhỏ nên có thể mô phỏng trực tiếp.

# // // Nhưng ở bài II:



# // // |s| ≤ 100000

# // // k ≤ 10^15

# // // và độ dài kết quả có thể lên tới:



# // // 10^15

# // // Nên không thể thật sự tạo chuỗi result vì sẽ quá lớn. (LeetCode Wiki)

# // // Ý tưởng của lời giải tối ưu là:



# // // Duyệt từ trái sang phải chỉ để tính độ dài của result.

# // // Nếu k hợp lệ, duyệt ngược từ cuối về đầu.

# // // Truy ngược xem vị trí k hiện tại trước mỗi phép biến đổi tương ứng với vị trí nào trong chuỗi trước đó.

# // // Cuối cùng tìm được ký tự gốc cần trả về. (Leetcode)

# // // Nếu bạn muốn, mình có thể giải thích chi tiết ý tưởng truy vết ngược (reverse simulation) của bài Hard này bằng hình vẽ và ví dụ từng bước.



# // Thuật toán của bạn sử dụng kỹ thuật reverse simulation (truy vết ngược) để tránh phải tạo ra chuỗi kết quả rất dài.

# // Ý tưởng chính

# // Thay vì thực sự xây dựng chuỗi result, ta chỉ:



# // Tính độ dài cuối cùng của chuỗi.

# // Biết rằng ta chỉ cần ký tự ở vị trí k.

# // Đi ngược từ cuối chuỗi s về đầu để xem vị trí k hiện tại tương ứng với vị trí nào trước mỗi phép biến đổi.

# // Bước 1: Tính độ dài cuối cùng

# // long totalLen = 0;

# // Duyệt từ trái sang phải.



# // Ký tự thường

# // totalLen++;

# // Ví dụ:



# // "a"

# // Độ dài:



# // 0 → 1

# // '*'

# // Xóa ký tự cuối



# // if (totalLen >= 1)

# //     totalLen--;

# // Ví dụ:



# // "abc*"

# // 3 → 2

# // '#'

# // Nhân đôi chuỗi



# // totalLen = totalLen + totalLen;

# // Ví dụ:



# // "abc"

# // thành



# // "abcabc"

# // Độ dài:



# // 3 → 6

# // '%'

# // Đảo ngược



# // length không đổi

# // Ví dụ:



# // "abc" → "cba"

# // Độ dài vẫn là:



# // 3

# // Bước 2: Kiểm tra k

# // if (k >= totalLen)

# //     return '.';

# // Nếu vị trí cần tìm vượt ngoài độ dài chuỗi cuối cùng thì không tồn tại.

# // Bước 3: Truy ngược

# // Bắt đầu từ cuối chuỗi:



# // for (int i = a.length - 1; i >= 0; i--)

# // Lúc này:



# // totalLen

# // là độ dài chuỗi sau khi thực hiện các thao tác từ đầu đến vị trí i.

# // Ta cần tìm xem vị trí k ở hiện tại xuất phát từ đâu trước phép biến đổi này.

# // Trường hợp 1: '#'

# // Giả sử:



# // ABCDE

# // sau '#'



# // ABCDEABCDE

# // Độ dài:



# // 5 → 10

# // Nếu



# // k = 7

# // thì ký tự đó nằm ở nửa sau.

# // Ta đưa nó về nửa đầu:



# // if (k >= totalLen / 2)

# //     k -= totalLen / 2;

# // Ví dụ:



# // 7 -> 2

# // Sau đó quay lại độ dài trước '#'



# // totalLen /= 2;

# // Trường hợp 2: '%'

# // Giả sử



# // ABCDE

# // sau '%'



# // EDCBA

# // Chỉ số:



# // 0 1 2 3 4

# // E D C B A

# // Muốn biết vị trí 1 đến từ đâu:



# // D

# // Trong chuỗi cũ:



# // ABCDE

# // D ở vị trí:



# // 3

# // Công thức:



# // k = (totalLen - 1) - k;

# // Ví dụ:



# // 5 ký tự



# // k=1



# // => 4-1=3

# // Trường hợp 3: ký tự thường

# // Giả sử đang xét:



# // ...

# // 'a'

# // Ký tự này được thêm vào cuối chuỗi.

# // Trước khi thêm:



# // độ dài = totalLen - 1

# // Sau khi thêm:



# // độ dài = totalLen

# // Nếu:



# // k == totalLen - 1

# // thì vị trí cần tìm chính là ký tự vừa được thêm.



# // if (k == totalLen - 1)

# //     return a[i];

# // Ngược lại:



# // totalLen--;

# // quay về trạng thái trước khi thêm ký tự.

# // Trường hợp 4: '*'

# // Đây là phần khó nhất.

# // Ví dụ:



# // abc*

# // Trước '*'



# // abc

# // Sau '*'



# // ab

# // Khi đi ngược:



# // ab

# // không cho ta biết ký tự bị xóa là gì.

# // Tuy nhiên điều đó không quan trọng.

# // Vì nếu đáp án nằm ở ký tự bị xóa thì chắc chắn nó không tồn tại trong chuỗi cuối cùng.

# // Nên ta chỉ cần khôi phục độ dài:



# // totalLen += 1;

# // Ví dụ hoàn chỉnh

# // s = "ab#"

# // k = 3

# // Forward:



# // a      -> "a"       len=1

# // b      -> "ab"      len=2

# // #      -> "abab"    len=4

# // Reverse



# # // len=4a

# // k=3

# // Gặp '#'



# // k >= 2



# // k = 3 - 2 = 1



# // len = 2

# // Gặp 'b'



# // k == len-1



# // 1 == 1

# // ⇒ trả về



# // 'b'

# // Chuỗi thật:



# // abab

# // vị trí 3 đúng là



# // 'b'

# // Độ phức tạp

# // Thời gian

# // Lần 1 tính độ dài: O(n)

# // Lần 2 truy ngược: O(n)

# // Tổng:



# // O(n)

# // Bộ nhớ

# // Chỉ dùng vài biến:



# // O(1)

# // Đây là lý do bài Hard này xử lý được khi độ dài chuỗi kết quả có thể lên tới 10^15 hoặc lớn hơn mà không cần xây dựng chuỗi thực tế.


# import java.util.*;

# public class b257 {
  
#     static Scanner sc = new Scanner(System.in);
#     public static void main(String[] args) {
#        // Nhập chuỗi thao tác
#         String s = sc.nextLine();

#         // Nhập vị trí k
#         long k = sc.nextLong();

        

#         char result = processStr(s, k);

#         System.out.println(result);

#         sc.close();  
#     }
# public static char processStr(String s, long k) {

#         char[] a = s.toCharArray();

#         // Tính độ dài cuối cùng của chuỗi sau khi thực hiện tất cả thao tác
#         long totalLen = 0;

#         for (int i = 0; i < a.length; i++) {

#             if (a[i] == '*') {

#                 // Xóa ký tự cuối nếu chuỗi không rỗng
#                 if (totalLen > 0) {
#                     totalLen--;
#                 }

#             } else if (a[i] == '#') {

#                 // Nhân đôi chuỗi
#                 totalLen = totalLen * 2;

#             } else if (a[i] == '%') {

#                 // Đảo ngược chuỗi nhưng độ dài không đổi
#                 continue;

#             } else {

#                 // Thêm một ký tự thường
#                 totalLen++;
#             }
#         }

#         // Nếu k vượt quá độ dài chuỗi cuối cùng
#         if (k >= totalLen) {
#             return '.';
#         }

#         // Truy ngược từ cuối chuỗi s về đầu
#         for (int i = a.length - 1; i >= 0; i--) {

#             if (a[i] == '*') {

#                 /*
#                  * Đi ngược qua dấu *
#                  * Trước khi xóa có nhiều hơn 1 ký tự
#                  * Chỉ cần khôi phục độ dài
#                  */
#                 totalLen++;

#             } else if (a[i] == '#') {

#                 /*
#                  * Sau dấu #:
#                  * ABC -> ABCABC
#                  *
#                  * Nếu k nằm ở nửa sau
#                  * đưa về vị trí tương ứng ở nửa đầu
#                  */
#                 if (k >= totalLen / 2) {
#                     k -= totalLen / 2;
#                 }

#                 // Quay lại độ dài trước dấu #
#                 totalLen /= 2;

#             } else if (a[i] == '%') {

#                 /*
#                  * ABCDE -> EDCBA
#                  *
#                  * Vị trí k mới tương ứng:
#                  * k = (len - 1) - k
#                  */
#                 k = (totalLen - 1) - k;

#             } else {

#                 /*
#                  * Ký tự thường được thêm vào cuối chuỗi
#                  *
#                  * Nếu k đúng bằng vị trí cuối cùng
#                  * thì đây chính là đáp án
#                  */
#                 if (k == totalLen - 1) {
#                     return a[i];
#                 }

#                 // Quay về trạng thái trước khi thêm ký tự
#                 totalLen--;
#             }
#         }

#         return '.';

# }
# }

# Đây là cùng một ý tưởng reverse simulation (truy vết ngược) như code Java của bạn.

# Ý tưởng

# Thay vì tạo chuỗi kết quả (có thể dài tới 10^15 ký tự), ta:



# Bước 1

# Tính độ dài cuối cùng của chuỗi.



# length = 0

# Bước 2

# Nếu:



# k >= length

# thì vị trí cần tìm không tồn tại.

# Bước 3

# Duyệt ngược chuỗi s.

# Mỗi lần gặp một phép biến đổi (*, #, %) ta tìm xem vị trí k hiện tại xuất phát từ đâu trước phép biến đổi đó.

# Giải thích từng trường hợp

# 1. Ký tự thường

# Ví dụ:



# AB

# thêm:



# c

# thành:



# ABc

# Nếu:



# k = vị trí cuối

# thì đáp án chính là:



# c

# 2. '#'

# Ví dụ:



# ABC

# sau '#'



# ABCABC

# Nếu:



# k nằm ở nửa sau

# thì đưa về vị trí tương ứng ở nửa đầu.

# Ví dụ:



# ABCABC

# 012345



# k = 4

# ↓



# 4 - 3 = 1

# 3. '%'

# Ví dụ:



# ABCDE

# ↓



# EDCBA

# Vị trí được đảo:



# new_index = len - old_index - 1

# nên khi đi ngược:



# k = length - k - 1

# 4. '*'

# Ví dụ:



# ABC

# ↓



# AB

# Khi đi ngược ta chỉ cần khôi phục:



# length += 1

# Không cần biết ký tự nào bị xóa.

# Code có chú thích

class Solution:

    def processStr(self, s: str, k: int) -> str:



        # ==================================================

        # BƯỚC 1: TÍNH ĐỘ DÀI CUỐI CÙNG CỦA CHUỖI

        # ==================================================

        length = 0



        for c in s:



            # Xóa ký tự cuối

            if c == "*":

                if length:

                    length -= 1



            # Nhân đôi chuỗi

            elif c == "#":

                length *= 2



            # Đảo ngược chuỗi

            # Độ dài không đổi

            elif c == "%":

                pass



            # Ký tự thường

            else:

                length += 1



        # ==================================================

        # Nếu vị trí k nằm ngoài chuỗi cuối cùng

        # ==================================================

        if k + 1 > length:

            return "."



        # ==================================================

        # BƯỚC 2: TRUY VẾT NGƯỢC

        # ==================================================

        for c in reversed(s):



            # ----------------------------------------------

            # Gặp *

            # Ví dụ:

            # ABC -> AB

            #

            # Đi ngược:

            # AB -> ABC

            #

            # Chỉ cần khôi phục độ dài

            # ----------------------------------------------

            if c == "*":

                length += 1



            # ----------------------------------------------

            # Gặp #

            #

            # ABC -> ABCABC

            #

            # Nếu k nằm ở nửa sau

            # đưa nó về nửa đầu

            # ----------------------------------------------

            elif c == "#":



                if k + 1 > (length + 1) // 2:

                    k -= length // 2



                # Quay về độ dài trước khi nhân đôi

                length = (length + 1) // 2



            # ----------------------------------------------

            # Gặp %

            #

            # ABCDE -> EDCBA

            #

            # old_index = len - new_index - 1

            # ----------------------------------------------

            elif c == "%":

                k = length - k - 1



            # ----------------------------------------------

            # Ký tự thường

            #

            # Ký tự này được thêm vào cuối chuỗi

            # ----------------------------------------------

            else:



                # Nếu k chính là vị trí cuối

                # thì đây là ký tự cần tìm

                if k + 1 == length:

                    return c



                # Quay về trạng thái trước khi thêm ký tự

                length -= 1



        return "."

# Ví dụ trực quan

# s = "ab#"

# k = 3

# Forward:



# a      -> a

# b      -> ab

# #      -> abab

# Kết quả:



# abab

# 0123

# Cần tìm:



# k = 3

# Reverse:



# Gặp '#'

# length = 4

# Vì:



# k = 3 nằm ở nửa sau

# nên:



# k = 3 - 2 = 1

# length = 2

# Gặp 'b'

# length = 2

# Kiểm tra:



# k + 1 = 2

# length = 2

# Đúng.

# ⇒ Trả về:



# 'b'

# Đáp án chính xác là ký tự ở vị trí 3 của "abab".