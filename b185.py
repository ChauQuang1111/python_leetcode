# # // Bài **762. Prime Number of Set Bits in Binary Representation** (21/02/2026) 
# # // ---

# Ok Quang 👌 bài này bạn đang dùng **Digit DP (Binary Digit Dynamic Programming)** – một cách nâng cao hơn hẳn cách duyệt từng số.

# Mình sẽ:

# 1. 🔎 Giải thích tư duy thuật toán
# 2. 🧠 Giải thích từng biến quan trọng
# 3. 💻 Viết lại code có chú thích chi tiết

# ---

# # 🎯 Ý tưởng tổng quát

# Thay vì:

# ```python
# for x in range(left, right+1):
# ```

# Ta làm như sau:

# 👉 Đếm trực tiếp **bao nhiêu số nhị phân nằm trong đoạn [left, right]**
# mà có số lượng bit 1 là số nguyên tố.

# Đây là dạng:

# ```text
# Digit DP trên biểu diễn nhị phân
# ```

# ---

# # 🧠 Tư duy chính

# Ta coi mỗi số như một chuỗi bit:

# Ví dụ:

# ```
# left  = 6  →  110
# right = 10 → 1010
# ```

# Ta duyệt từng vị trí bit từ trái sang phải.

# Ở mỗi vị trí ta quyết định:

# * đặt 0 hay 1
# * vẫn còn “bị ràng buộc” bởi left không?
# * vẫn còn “bị ràng buộc” bởi right không?

# ---

# # 🔥 Ý nghĩa các biến trong DFS

# ```python
# dfs(i, tight_low, tight_high, set_bits)
# ```

# | Biến       | Ý nghĩa                         |
# | ---------- | ------------------------------- |
# | i          | đang xét bit thứ i              |
# | tight_low  | còn bị giới hạn bởi left không  |
# | tight_high | còn bị giới hạn bởi right không |
# | set_bits   | đã có bao nhiêu bit 1           |

# ---

# 🧠 Giải thích cơ chế "tight"

# Nếu đang tight_low = True
# → bit hiện tại không được nhỏ hơn bit của left

# Nếu đang tight_high = True
# → bit hiện tại không được lớn hơn bit của right

# Đây chính là kỹ thuật chuẩn của Digit DP.

# ---

# # 💻 Code có chú thích chi tiết

# ```python
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        # =============================
        # Chuyển right sang dạng nhị phân (mảng bit)
        # =============================
        upper = []
        while right:
            upper.append(right & 1)  # Lấy bit cuối
            right >>= 1              # Dịch phải 1 bit
        upper = upper[::-1]          # Đảo lại để MSB -> LSB


        # =============================
        # Chuyển left sang dạng nhị phân
        # Và đảm bảo cùng độ dài với upper
        # =============================
        lower = []
        while left or len(lower) < len(upper):
            lower.append(left & 1)
            left >>= 1
        lower = lower[::-1]


        # =============================
        # Tập các số nguyên tố có thể có
        # Vì int tối đa 32 bit → tối đa 32 bit 1
        # =============================
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 31}


        # Memoization để tránh tính lại
        memo = {}


        # =============================
        # Digit DP
        # i          : đang xét vị trí bit thứ i
        # tight_low  : còn bị ràng buộc bởi left?
        # tight_high : còn bị ràng buộc bởi right?
        # set_bits   : số lượng bit 1 đã chọn
        # =============================
        def dfs(i, tight_low, tight_high, set_bits):

            # Nếu đã duyệt hết các bit
            if i == len(upper):
                # Kiểm tra số bit 1 có phải số nguyên tố không
                return 1 if set_bits in primes else 0

            # Trạng thái DP
            state = (i, tight_low, tight_high, set_bits)

            # Nếu đã tính rồi → trả lại
            if state in memo:
                return memo[state]


            # Xác định giới hạn bit có thể chọn
            start = lower[i] if tight_low else 0
            end = upper[i] if tight_high else 1

            ways = 0

            # Thử đặt bit = 0 hoặc 1
            for bit in range(start, end + 1):

                ways += dfs(
                    i + 1,
                    tight_low and bit == lower[i],
                    tight_high and bit == upper[i],
                    set_bits + (1 if bit == 1 else 0)
                )

            # Lưu kết quả vào memo
            memo[state] = ways
            return ways


        # Gọi DFS từ vị trí đầu tiên
        return dfs(0, True, True, 0)


# # 📊 Độ phức tạp

# Số trạng thái tối đa:

# ```
# vị trí bit ≤ 32
# tight_low ∈ {0,1}
# tight_high ∈ {0,1}
# set_bits ≤ 32
# ```

# → Khoảng:

# ```
# 32 × 2 × 2 × 32 ≈ 4096 trạng thái
# ```

# 👉 Rất nhanh.

# ---

# 🔥 So sánh 2 cách làm

# | Cách          | Ý tưởng                | Độ khó |
# | ------------- | ---------------------- | ------ |
# | Duyệt từng số | BitCount + check prime | Dễ     |
# | Digit DP      | Đếm trực tiếp theo bit | Khó    |

# ---

# # 🎯 Kết luận

# Code của bạn là:

# ✔ Chính xác
# ✔ Tối ưu
# ✔ Thuộc dạng tư duy contest nâng cao

# ---

# Nếu bạn muốn mình vẽ sơ đồ cây DFS minh họa cách digit DP hoạt động, mình vẽ cho bạn nhìn phát hiểu luôn 😎



# // Ok Quang👌mình sẽ:

# // 1.✅Giải thích thuật toán 2.✅Thêm chú thích chi tiết vào code 3.✅Viết thêm`main()`dùng`Scanner`

# // ---

# // #🧠Giải thích thuật toán

# // Bài này làm theo 3 bước chính:

# // ###🔹Bước 1:Duyệt từ`left`→`right`

# // ```java for(int i=left;i<=right;i++)```

# // Ta xét từng số trong khoảng.

# // ---

# // ###🔹Bước 2:Đếm số bit 1 của số đó

# // ```java Integer.bitCount(i)```

# // Ví dụ:

# // *6→110→có 2 bit 1*7→111→có 3 bit 1

# // Hàm`bitCount()`là hàm có sẵn trong Java,rất tối ưu.

# // ---

# // ###🔹Bước 3:Kiểm tra số bit 1 có phải nguyên tố không

# // Ta kiểm tra:

# // *Nếu<2→không phải nguyên tố*Duyệt từ 2 đến√n*Nếu chia hết→không phải nguyên tố

# // ---

# // ###🎯Ý tưởng tổng quát

# // ```Duyệt từng số↓Đếm số bit 1↓Kiểm tra có phải số nguyên tố không↓Nếu đúng→tăng biến đếm```

# // ---

# // #💻Code đầy đủ có chú thích+main Scanner

# // ```java

# import java.util.*;

# public class b186 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         // Nhập left và right
#         int left = sc.nextInt();
#         int right = sc.nextInt();

#         // Gọi hàm xử lý
#         int result = countPrimeSetBits(left, right);

#         // In kết quả
#         System.out.println(result);
#     }

#     // Hàm chính của bài toán
#     public static int countPrimeSetBits(int left, int right) {

#         int c = 0; // Biến đếm số lượng số thỏa điều kiện

#         // Duyệt từ left đến right
#         for (int i = left; i <= right; i++) {

#             // Đếm số bit 1 trong biểu diễn nhị phân của i
#             int bits = Integer.bitCount(i);

#             // Nếu số bit 1 là số nguyên tố thì tăng biến đếm
#             if (isPrime(bits)) {
#                 c++;
#             }
#         }

#         return c; // Trả về kết quả
#     }

#     // Hàm kiểm tra một số có phải số nguyên tố không
#     public static boolean isPrime(int n) {

#         // Nếu nhỏ hơn 2 thì không phải nguyên tố
#         if (n < 2)
#             return false;

#         // Duyệt từ 2 đến căn bậc hai của n
#         for (int i = 2; i * i <= n; i++) {

#             // Nếu chia hết thì không phải nguyên tố
#             if (n % i == 0)
#                 return false;
#         }

#         return true; // Nếu không chia hết cho số nào → là số nguyên tố
#     }
# }

# // Giả sử:

# // *N=right-
# // left

# // Ta có:

# // *
# // Duyệt N lần*bitCount=

# // O(1)
# // * isPrime kiểm tra tối đa √32 ≈ 6

# // lần (vì số bit tối đa của int là 32)

# // 👉 Thực tế gần như O(N)
# // 👉 Rất nhanh

# // ---

# // Nếu bạn muốn mình giải thích:

# // * Vì sao chỉ cần kiểm tra đến √n?
# // * Cách tối ưu hơn nữa (hardcode prime nhỏ)
# // * Hoặc cách làm dùng bit manipulation thuần

# // Nói mình biết 😎

# // ## 📌 Yêu cầu đề bài

# // Cho hai số nguyên `left` và `right`.

# // Với **mỗi số nguyên x trong đoạn [left, right]**, ta:

# // 1. Chuyển x sang dạng **nhị phân**.
# // 2. Đếm số lượng bit `1` trong biểu diễn nhị phân đó
# // → gọi là **set bits**.
# // 3. Kiểm tra xem số lượng bit `1` đó có phải là **số nguyên tố** hay không.

# // 👉 Kết quả: **Trả về số lượng các số thỏa điều kiện trên.**

# // ---

# // ## 🧠 Giải thích khái niệm

# // ### 1️⃣ Set bits là gì?

# // Là **số lượng bit 1** trong biểu diễn nhị phân của một số.

# // Ví dụ:

# // | Số | Nhị phân | Số bit 1 |
# // | -- | -------- | -------- |
# // | 6 | 110 | 2 |
# // | 7 | 111 | 3 |
# // | 8 | 1000 | 1 |

# // ---

# // ### 2️⃣ Số nguyên tố là gì?

# // Số nguyên tố là số:

# // * Lớn hơn 1
# // * Chỉ chia hết cho 1 và chính nó

# // Ví dụ:
# // 2, 3, 5, 7, 11, ...

# // Không phải nguyên tố:
# // 1, 4, 6, 8, 9, ...

# // ---

# // ## 📘 Ví dụ cụ thể

# // ### Input:

# // ```
# // left = 6
# // right = 10
# // ```

# // Ta xét từng số:

# // | Số | Nhị phân | Số bit 1 | Có phải số nguyên tố? |
# // | -- | -------- | -------- | -------------------------- |
# // | 6 | 110 | 2 | ✅ (2 là nguyên tố) |
# // | 7 | 111 | 3 | ✅ (3 là nguyên tố) |
# // | 8 | 1000 | 1 | ❌ (1 không phải nguyên tố) |
# // | 9 | 1001 | 2 | ✅ |
# // | 10 | 1010 | 2 | ✅ |

# // 👉 Có 4 số thỏa điều kiện
# // → Output: `4`

# // ---

# // ## 🎯 Tóm lại đề bài yêu cầu

# // Đếm bao nhiêu số trong đoạn `[left, right]` mà:

# // ```
# // số lượng bit 1 trong nhị phân của nó là số nguyên tố
# // ```

# // ---

# // Nếu bạn muốn, mình có thể:

# // * Giải thích cách làm tối ưu
# // * Phân tích độ phức tạp
# // * Viết code Java (theo style bạn thích: Scanner, while loop, tối ưu)
# // * Hoặc hướng dẫn tư duy từng bước để bạn tự code

# // Bạn muốn theo hướng nào? 🚀
