# # // // Bài **“Minimum Number of Flips to Make the Binary String Alternating(07/03/2026)

# Đây là **một cách giải khác** cho bài **Minimum Number of Flips to Make the Binary String Alternating**.
# Ý tưởng chính vẫn là so sánh chuỗi với **2 pattern alternating**:

# ```
# Pattern A: 010101...
# Pattern B: 101010...
# ```

# Nhưng code này **xử lý luôn cả trường hợp rotation khi n lẻ** bằng cách dùng **4 biến đếm**.

# ---

# # 1️⃣ Ý nghĩa các biến

# ```python
# prev = 0
# ```

# `prev` dùng để **mô phỏng pattern bắt đầu bằng 0**

# ```
# 0 1 0 1 0 1 ...
# ```

# Mỗi vòng lặp:

# ```
# prev = 1 - prev
# ```

# để đảo:

# ```
# 0 → 1 → 0 → 1 ...
# ```

# ---

# ### 4 biến đếm

# ```python
# start_1
# start_0
# start_1_odd
# start_0_odd
# ```

# | Biến          | Ý nghĩa                                            |
# | ------------- | -------------------------------------------------- |
# | `start_1`     | số flip nếu pattern bắt đầu bằng **1**             |
# | `start_0`     | số flip nếu pattern bắt đầu bằng **0**             |
# | `start_1_odd` | trường hợp **rotation khi n lẻ** và bắt đầu bằng 1 |
# | `start_0_odd` | trường hợp **rotation khi n lẻ** và bắt đầu bằng 0 |

# ---

# # 2️⃣ Tại sao cần xử lý riêng khi n lẻ?

# Nếu `n` **chẵn**

# ```
# 010101
# ```

# xoay chuỗi không làm thay đổi pattern.

# Nhưng nếu `n` **lẻ**

# ```
# 01010
# ```

# xoay sẽ thành

# ```
# 10100
# ```

# pattern bị **đảo vị trí chẵn lẻ**.

# Vì vậy cần thêm:

# ```
# start_1_odd
# start_0_odd
# ```

# ---

# # 3️⃣ Thuật toán chạy thế nào

# Ví dụ

# ```
# s = 111000
# ```

# pattern mong muốn

# ```
# 0 1 0 1 0 1
# ```

# so từng ký tự.

# ---

# ### Nếu `val == prev`

# tức là **khớp pattern bắt đầu bằng 0**

# → pattern bắt đầu bằng **1 sẽ sai**

# → cần flip.

# ---

# ### Nếu `val != prev`

# tức là **khớp pattern bắt đầu bằng 1**

# → pattern bắt đầu bằng **0 sẽ sai**

# ---

# # 4️⃣ Code đã thêm chú thích

# ```python
import sys

class Solution:
    def minFlips(self, s: str) -> int:

        # prev dùng để mô phỏng pattern 0 1 0 1 ...
        prev = 0

        # số flip nếu bắt đầu pattern bằng 1
        start_1 = 0

        # số flip nếu bắt đầu pattern bằng 0
        start_0 = 0

        # xử lý rotation khi n là số lẻ
        start_1_odd = sys.maxsize
        start_0_odd = sys.maxsize

        # kiểm tra chuỗi có độ dài lẻ không
        odd = len(s) % 2

        # duyệt từng ký tự trong chuỗi
        for val in s:

            # chuyển ký tự sang số
            val = int(val)

            # nếu ký tự hiện tại giống pattern bắt đầu bằng 0
            if val == prev:

                # nếu n lẻ thì cần cập nhật trường hợp rotation
                if odd:
                    start_0_odd = min(start_0_odd, start_1)
                    start_1_odd += 1

                # pattern bắt đầu bằng 1 sẽ sai → cần flip
                start_1 += 1

            else:

                # nếu n lẻ thì cập nhật rotation
                if odd:
                    start_1_odd = min(start_1_odd, start_0)
                    start_0_odd += 1

                # pattern bắt đầu bằng 0 sẽ sai → cần flip
                start_0 += 1

            # đổi pattern cho vị trí tiếp theo
            prev = 1 - prev

        # trả về số flip nhỏ nhất
        return min([start_1, start_0, start_1_odd, start_0_odd])


# ---

# # 5️⃣ Ví dụ chạy

# Input

# ```
# s = "111000"
# ```

# Pattern:

# ```
# 010101
# 101010
# ```

# Số flip

# ```
# pattern 010101 → 3
# pattern 101010 → 3
# ```

# Nhưng sau rotation có thể giảm còn

# ```
# 2
# ```

# ---

# 6️⃣ Độ phức tạp

# Time Complexity

# ```
# O(n)
# ```

# Space Complexity

# ```
# O(1)
# ```

# ---

# ✅ Nếu bạn muốn, mình có thể giải thích thêm **1 điều cực quan trọng của bài này**:

# 👉 **tại sao solution Java dùng sliding window nhưng Python này không cần**

# (đây là trick rất hay trong interview Google / Meta).



# // Mình sẽ giải thích**từng phần của thuật toán**,sau đó viết lại**code đầy đủ có`main`,`Scanner`và chú thích**để bạn dễ hiểu.

# // ---

# // #1 ️⃣Ý tưởng của thuật toán

# // Bài này có**2 chuỗi alternating hợp lệ**:

# // ```Pattern A:010101...Pattern B:101010...```

# // Ta cần đếm**số flip ít nhất để biến`s`thành 1 trong 2 pattern này**.

# // ---

# // #2 ️⃣Hai biến quan trọng

# // ```java int cost1=0;int cost2=0;```

# // *`cost1`:số flip để biến`s`thành

# // ```010101...```

# // *`cost2`:số flip để biến`s`thành

# // ```101010...```

# // ---

# // #3 ️⃣Vòng lặp tính chi phí

# // ```java for(int i=0;i<n;i++)```

# // Ta kiểm tra từng vị trí.

# // ---

# // ###Nếu i là số chẵn

# // ```pattern A:phải là 0 pattern B:phải là 1```

# // Ví dụ:

# // ```index:0 1 2 3 patternA 0 1 0 1 patternB 1 0 1 0```

# // ---

# // ###Code

# // ```java if(i%2==0)```

# // nếu ký tự hiện tại**không đúng pattern**thì phải flip.

# // ---

# // #4 ️⃣Trường hợp chuỗi có độ dài lẻ

# // ```java if(n%2==1)```

# // Đây là phần**khó nhất của bài**.

# // Khi`n`lẻ:

# // Nếu ta**rotate chuỗi**(dịch vòng):

# // ```s=111000```

# // có thể trở thành:

# // ```110001 100011 000111```

# // Nên ta phải kiểm tra**mọi rotation**.

# // ---

# // #5 ️⃣Trick quan trọng

# // Ta nhân đôi chuỗi:

# // ```java String doubled=s+s;```

# // Ví dụ:

# // ```s=111000 doubled=111000111000```

# // Sau đó dùng**sliding window kích thước n**.

# // ---

# // #6 ️⃣Sliding Window

# // Mỗi lần dịch cửa sổ:

# // *1 ký tự**rời khỏi cửa sổ**→`leaving`*1 ký tự**đi vào cửa sổ**→`entering`

# // Ta cập nhật lại`cost1`và`cost2`.

# // ---

# // #7 ️⃣Code đầy đủ(có main+Scanner+chú thích)

# // ```java

# import java.util.*;

# public class b209 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         // nhập chuỗi nhị phân
#         String s = sc.next();

#         // gọi hàm tính số flip tối thiểu
#         int answer = minFlips(s);

#         // in kết quả
#         System.out.println(answer);
#     }

#     public static int minFlips(String s) {

#         int n = s.length();

#         // cost1: số flip để biến thành pattern 010101...
#         // cost2: số flip để biến thành pattern 101010...
#         int cost1 = 0;
#         int cost2 = 0;

#         // Tính chi phí ban đầu
#         for (int i = 0; i < n; i++) {

#             if (i % 2 == 0) { // vị trí chẵn

#                 // pattern1 cần '0'
#                 if (s.charAt(i) == '1')
#                     cost1++;

#                 // pattern2 cần '1'
#                 else
#                     cost2++;

#             } else { // vị trí lẻ

#                 // pattern1 cần '1'
#                 if (s.charAt(i) == '0')
#                     cost1++;

#                 // pattern2 cần '0'
#                 else
#                     cost2++;
#             }
#         }

#         // kết quả ban đầu
#         int result = Math.min(cost1, cost2);

#         // nếu độ dài chuỗi là lẻ thì cần xét rotation
#         if (n % 2 == 1) {

#             // nhân đôi chuỗi
#             String doubled = s + s;

#             // sliding window
#             for (int i = 1; i < n; i++) {

#                 // ký tự rời khỏi cửa sổ
#                 char leaving = doubled.charAt(i - 1);

#                 // ký tự đi vào cửa sổ
#                 char entering = doubled.charAt(i + n - 1);

#                 // cập nhật chi phí khi ký tự rời đi
#                 if ((i - 1) % 2 == 0) {

#                     if (leaving == '1')
#                         cost1--;
#                     else
#                         cost2--;

#                 } else {

#                     if (leaving == '0')
#                         cost1--;
#                     else
#                         cost2--;
#                 }

#                 // cập nhật chi phí khi ký tự mới vào
#                 if ((i + n - 1) % 2 == 0) {

#                     if (entering == '1')
#                         cost1++;
#                     else
#                         cost2++;

#                 } else {

#                     if (entering == '0')
#                         cost1++;
#                     else
#                         cost2++;
#                 }

#                 // cập nhật kết quả nhỏ nhất
#                 result = Math.min(result, Math.min(cost1, cost2));
#             }
#         }

#         return result;
#     }
# }

# // ---

# // #8 ️⃣

# // Độ phức
# // tạp

# // Time Complexity:

# // ```

# // O(n)
# // ```

# // Space Complexity:

# // ```
# // O(n)
# // ```

# // ---

# // # 9️⃣ Ví dụ chạy chương trình

# // Input

# // ```
# // 111000
# // ```

# // Output

# // ```
# // 2
# // ```

# // ---

# // ✅ Nếu bạn muốn, mình có thể giải thích thêm:

# // * **tại sao phải dùng

# // sliding window (rất hay trong interview)**
# // * **minFlips này là bài Leetcode Hard nhưng có trick cực đẹp**
# // * **vẽ hình rotation để bạn hiểu ngay trong 1 phút**.

# // ### 1️⃣ Đề bài nói gì?

# // Bạn được cho **một chuỗi nhị phân `s`**, chỉ gồm:

# // * `'0'`
# // * `'1'`

# // Ví dụ:
# // `s = "01010"`
# // `s = "111000"`

# // Bạn có thể thực hiện thao tác:

# // 🔁 **Flip** = đổi một ký tự

# // * `0 → 1`
# // * `1 → 0`

# // Mục tiêu:
# // 👉 **Biến chuỗi thành chuỗi xen kẽ (alternating string)** với **số lần flip
# // ít nhất**.

# // ---

# // ### 2️⃣ Chuỗi xen kẽ là gì?

# // Chuỗi xen kẽ nghĩa là **hai ký tự liền nhau luôn khác nhau**.

# // Chỉ có **2 dạng hợp lệ**:

# // 1️⃣ Bắt đầu bằng **0**

# // ```
# // 0101010101...
# // ```

# // 2️⃣ Bắt đầu bằng **1**

# // ```
# // 1010101010...
# // ```

# // ---

# // ### 3️⃣ Ví dụ

# // #### Ví dụ 1

# // ```
# // s = "0100"
# // ```

# // Hai chuỗi alternating có thể là:

# // ```
# // 0101
# // 1010
# // ```

# // So sánh:

# // **với 0101**

# // ```
# // 0100
# // 0101
# // ↑
# // ```

# // → cần **1 flip**

# // **với 1010**

# // ```
# // 0100
# // 1010
# // ↑ ↑
# // ```

# // → cần **2 flips**

# // 👉 **Kết quả = 1**

# // ---

# // #### Ví dụ 2

# // ```
# // s = "1111"
# // ```

# // Alternating có thể:

# // ```
# // 1010
# // 0101
# // ```

# // So sánh:

# // ```
# // 1111
# // 1010
# // ↑ ↑
# // ```

# // → **2 flips**

# // ```
# // 1111
# // 0101
# // ↑ ↑
# // ```

# // → **2 flips**

# // 👉 **Kết quả = 2**

# // ---

# // ### 4️⃣ Bài toán yêu cầu gì?

# // 👉 Tính **số lần flip ít nhất** để biến `s` thành chuỗi alternating.

# // ---

# // ### 5️⃣ Ý tưởng giải

# // Ta thử so sánh với **2 pattern chuẩn**:

# // Pattern 1:

# // ```
# // 010101...
# // ```

# // Pattern 2:

# // ```
# // 101010...
# // ```

# // Đếm:

# // ```
# // flip1 = số vị trí khác pattern1
# // flip2 = số vị trí khác pattern2
# // ```

# // 👉 Kết quả:

# // ```
# // min(flip1, flip2)
# // ```

# // ---

# // ### 6️⃣ Ví dụ minh họa trực quan

# // ```
# // s = 1001
# // ```

# // Pattern A:

# // ```
# // 0101
# // ```

# // So sánh

# // ```
# // 1001
# // 0101
# // ↑ ↑
# // ```

# // → flip = 2

# // ---

# // Pattern B:

# // ```
# // 1010
# // ```

# // ```
# // 1001
# // 1010
# // ↑ ↑
# // ```

# // → flip = 2

# // ---

# // 👉 **Answer = 2**

# // ---

# // ### 7️⃣ Tóm lại

# // Bài này:

# // 1️⃣ Chuỗi chỉ có `0` và `1`
# // 2️⃣ Muốn biến thành chuỗi **010101...** hoặc **101010...**
# // 3️⃣ Mỗi lần flip đổi `0 ↔ 1`
# // 4️⃣ Trả về **số flip ít nhất**

# // ---

# // Nếu bạn muốn mình giải thích thêm:

# // * **cách tư duy ra solution (interview thinking)**
# // * **code Java / Python**
# // * **tại sao bài này xuất hiện trong Google / Amazon interview**

# // mình có thể giải cực kỳ dễ hiểu luôn.
