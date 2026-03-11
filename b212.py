# // **“Complement of Base 10 Integer (11/03/2026)

# Mình sẽ giải thích **thuật toán của code Python này** theo cách dễ hiểu rồi **viết lại code có chú thích chi tiết**.

# ---

# # 1. Ý tưởng của bài toán

# Bài **1009. Complement of Base 10 Integer** yêu cầu:

# > Đảo tất cả **bit của số nhị phân của n**.

# Ví dụ:

# ```
# n = 5
# ```

# Chuyển sang nhị phân:

# ```
# 5 = 101
# ```

# Đảo bit:

# ```
# 101
# ↓
# 010
# ```

# Kết quả:

# ```
# 2
# ```

# ---

# # 2. Ý tưởng thuật toán trong code

# Thuật toán làm như sau:

# ### Bước 1: xử lý trường hợp đặc biệt

# ```
# n = 0
# ```

# Binary:

# ```
# 0 → complement = 1
# ```

# ---

# ### Bước 2: duyệt từng bit của n

# Ta dùng:

# ```
# n & 1
# ```

# để lấy **bit cuối cùng** của số nhị phân.

# Nếu:

# ```
# bit = 1 → đảo thành 0
# bit = 0 → đảo thành 1
# ```

# ---

# ### Bước 3: xây dựng số kết quả

# Biến:

# ```
# cnt
# ```

# lưu **vị trí bit hiện tại**

# ```
# 2^cnt
# ```

# chính là giá trị của bit đó.

# Nếu bit đảo là **1** thì ta cộng:

# ```
# ans += 2^cnt
# ```

# ---

### Bước 4: dịch phải số n

# ```
# n = n >> 1
# ```

# Nghĩa là:

# ```
# 101 >> 1 = 10
# ```

# để xử lý bit tiếp theo.

# ---

# # 3. Code Python có chú thích chi tiết

# ```python
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        # cnt: vị trí bit hiện tại (0,1,2,...)
        cnt = 0
        
        # ans: kết quả cuối cùng
        ans = 0
        
        # Trường hợp đặc biệt
        # complement của 0 là 1
        if n == 0:
            return 1
        
        # Duyệt từng bit của số n
        while n > 0:
            
            # n & 1 lấy bit cuối cùng của n
            # ví dụ: 101 & 1 = 1
            if n & 1:
                
                # nếu bit = 1
                # complement sẽ là 0
                # nên không cộng gì vào ans
                cnt += 1
                
            else:
                
                # nếu bit = 0
                # complement sẽ là 1
                # ta cộng 2^cnt vào kết quả
                ans = ans + (2 ** cnt)
                
                # tăng vị trí bit
                cnt += 1
            
            # dịch phải để xét bit tiếp theo
            # ví dụ: 101 >> 1 = 10
            n = n >> 1
        
        # trả về kết quả
        return ans
# ```

# ---

# # 4. Ví dụ chạy từng bước

# Ví dụ:

# ```
# n = 5
# ```

# Binary:

# ```
# 101
# ```

# | vòng | n (binary) | n&1 | complement | ans |
# | ---- | ---------- | --- | ---------- | --- |
# | 1    | 101        | 1   | 0          | 0   |
# | 2    | 10         | 0   | 1          | 2   |
# | 3    | 1          | 1   | 0          | 2   |

# Kết quả:

# ```
# 2
# ```

# ---

# # 5. Độ phức tạp thuật toán

# Nếu số có **k bit**:

# ```
# Time Complexity: O(log n)
# ```

# vì số bit của n là log₂(n)

# ```
# Space Complexity: O(1)
# ```

# ---

# 💡 **Mẹo phỏng vấn / LeetCode**

# Bài này còn có **cách giải cực ngắn chỉ 3 dòng bằng XOR + mask**.

# Ví dụ:

# ```python
# mask = (1 << n.bit_length()) - 1
# return mask ^ n
# ```

# ---

# Nếu bạn muốn, mình có thể giải thích thêm **trực quan nhất về 3 cách giải của bài này (90% người mới học bit bị nhầm)**.



# // Mình sẽ**giải thích thuật toán+viết lại code đầy đủ có`main`,`Scanner`,và chú thích từng dòng**để bạn hiểu rõ.

# // ---

# // #1. Ý tưởng thuật toán(Bitwise Complement)

# // Bài toán yêu cầu:

# // >**Đảo bit của số nhị phân của n(0→1,1→0)**nhưng**chỉ trong độ dài bit của số đó**.

# // Ví dụ:

# // ```n=5```

# // Binary:

# // ```5=101```

# // Đảo bit:

# // ```101↓010```

# // Kết quả:

# // ```2```

# // ---

# // #2. Ý tưởng trong code

# // Thuật toán làm các bước:

# // ###Bước 1

# // Xử lý trường hợp đặc biệt:

# // ```n=0```

# // Binary:

# // ```0->complement=1```

# // ---

# // ###Bước 2

# // Duyệt từng**bit của n từ phải sang trái**

# // Lấy bit cuối:

# // ```n%2```

# // Nếu:

# // ```0→đổi thành 1 1→đổi thành 0```

# // ---

# // ###Bước 3

# // Xây dựng số kết quả

# // Ta dùng:

# // ```fac=1```

# // để biểu diễn:

# // ```2^0,2^1,2^2...```

# // Mỗi lần:

# // ```fac*=2```

# // ---

# // #3. Code Java đầy đủ(có main+Scanner+chú thích)

# // ```java

# import java.util.*;

# public class b213 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         // Nhập số n
#         int n = sc.nextInt();

#         // Gọi hàm
#         int result = bitwiseComplement(n);

#         // In kết quả
#         System.out.println(result);

#         sc.close();
#     }

#     // Hàm tính bitwise complement
#     public static int bitwiseComplement(int n) {

#         // Trường hợp đặc biệt
#         // complement của 0 là 1
#         if (n == 0)
#             return 1;

#         int res = 0; // kết quả cuối
#         int fac = 1; // đại diện cho 2^0, 2^1, 2^2 ...

#         // Duyệt từng bit của số n
#         while (n != 0) {

#             // Lấy bit cuối của n
#             int bit = n % 2;

#             // Nếu bit = 0 → đảo thành 1
#             // Nếu bit = 1 → đảo thành 0
#             int complementBit;

#             if (bit == 0) {
#                 complementBit = 1;
#             } else {
#                 complementBit = 0;
#             }

#             // Cộng vào kết quả
#             // fac dùng để đặt đúng vị trí bit
#             res += fac * complementBit;

#             // Tăng lên bit tiếp theo (2^k)
#             fac *= 2;

#             // Bỏ bit cuối của n
#             n /= 2;
#         }

#         return res;
#     }
# }

# // ---

# // #4.

# // Ví dụ
# // chạy chương
# // trình

# // Input

# // ```5```

# // Binary:

# // ```5=101```

# // Đảo bit:

# // ```010```

# // Output

# // ```2```

# // ---

# // #5.
# // Minh họa
# // từng vòng
# // lặp

# // Ví dụ:

# // ```n=5 binary=101```

# // |Vòng|n|n%2|complement|res|fac||----|-|---|----------|---|---||1|5|1|0|0|1||2|2|0|1|2|2||3|1|1|0|2|4|

# // Kết quả:

# // ```res=2```

# // ---

# // #6.
# // Độ phức tạp

# // ```
# // Time Complexity:

# // O(log n)
# // ```

# // vì số bit của n là `log2(n)`

# // ```
# // Space Complexity: O(1)
# // ```

# // ---

# // 💡 **Tip cho phỏng vấn / LeetCode**

# // Có cách ngắn hơn nhiều:

# // ```
# // mask = 111...111
# // result = mask ^ n
# // ```

# // Nếu bạn muốn mình giải thích **cách giải chuẩn trong

# // phỏng vấn (XOR + mask)** thì mình có thể giải thích rất dễ hiểu.

# // ---

# // ## 1. Ý nghĩa của “Complement” trong bài này

# // **Complement** nghĩa là **đảo các chữ số theo cơ số 10**.

# // Cụ thể:
# // Với mỗi chữ số **d** trong số (N), ta đổi thành:

# // [
# // 9 - d
# // ]

# // Tức là:

# // | Chữ số ban đầu | Sau khi complement |
# // | -------------- | ------------------ |
# // | 0 | 9 |
# // | 1 | 8 |
# // | 2 | 7 |
# // | 3 | 6 |
# // | 4 | 5 |
# // | 5 | 4 |
# // | 6 | 3 |
# // | 7 | 2 |
# // | 8 | 1 |
# // | 9 | 0 |

# // ---

# // ## 2. Ví dụ

# // ### Ví dụ 1

# // Input:

# // ```
# // N = 123
# // ```

# // Tính complement từng chữ số:

# // * 1 → 8 (9-1)
# // * 2 → 7 (9-2)
# // * 3 → 6 (9-3)

# // Output:

# // ```
# // 876
# // ```

# // ---

# // ### Ví dụ 2

# // Input:

# // ```
# // N = 907
# // ```

# // Từng chữ số:

# // * 9 → 0
# // * 0 → 9
# // * 7 → 2

# // Output:

# // ```
# // 092
# // ```

# // Nếu bài yêu cầu **integer**, thì kết quả sẽ là:

# // ```
# // 92
# // ```

# // ---

# // ## 3. Cách hiểu nhanh (tư duy)

# // Đề bài thực chất yêu cầu:

# // > **Đổi mỗi chữ số của số N thành (9 − chữ số đó).**

# // ---

# // ## 4. Các bước giải

# // 1. Đọc số (N)
# // 2. Duyệt từng **chữ số**
# // 3. Với mỗi chữ số (d):

# // ```
# // new_digit = 9 - d
# // ```
# // 4. Ghép các chữ số mới lại thành số kết quả.

# // ---

# // ## 5. Ví dụ lớn hơn

# // Input:

# // ```
# // N = 56019
# // ```

# // Tính:

# // | digit | 9 - digit |
# // | ----- | --------- |
# // | 5 | 4 |
# // | 6 | 3 |
# // | 0 | 9 |
# // | 1 | 8 |
# // | 9 | 0 |

# // Output:

# // ```
# // 43980
# // ```

# // ---

# // 💡 **Tóm lại:**

# // > **Complement of Base 10 Integer = thay mỗi chữ số d bằng (9 − d).**

# // ---

# // Nếu bạn muốn, mình có thể giải thích thêm:

# // * **tại sao bài này hay xuất hiện trong phỏng vấn coding**
# // * **cách code Java / Python / C++ chỉ 5 dòng**.
