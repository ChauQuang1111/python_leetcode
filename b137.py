# # //  Four Divisors(04/01/2026)
# # //  **Four Divisors – Giải thích đề bài (bằng tiếng Việt)**
# Dưới đây là **giải thích thuật toán + code Python có chú thích chi tiết** cho đoạn bạn đưa. Thuật toán này dùng **tiền xử lý (precompute)** rất hay và ngắn gọn 👍

# ---

# ## 🎯 Ý tưởng chính của thuật toán

# Thay vì:

# * Với **mỗi số trong `nums`** lại đi tìm ước số (chậm),

# ta sẽ:
# 👉 **Tiền xử lý trước** cho **tất cả các số từ 1 → 10⁵**:

# * `s[x]` = **tổng các ước của x**
# * `c[x]` = **số lượng ước của x**

# Sau đó:

# * Chỉ cần duyệt `nums`
# * Nếu `c[i] == 4` → cộng `s[i]`

# ---

# ## 🧠 Tư duy giống “Sàng Eratosthenes”

# * Với mỗi `i`, ta coi `i` là **một ước**
# * Cộng `i` vào **tất cả bội số của i**

# ---

# ## ✅ Code có chú thích chi tiết

# ```python
from typing import List
MAX = 10**5 + 1

# s[x]: tổng các ước số của x
# c[x]: số lượng ước số của x
s = [1] * MAX
c = [1] * MAX

# Duyệt tất cả các ước i từ 2 đến MAX - 1
for i in range(2, MAX):
    x = i
    # Duyệt tất cả bội số của i
    while x < MAX:
        s[x] += i   # i là 1 ước của x → cộng vào tổng ước
        c[x] += 1   # tăng số lượng ước của x
        x += i

# Lúc này:
# s[x] = tổng các ước của x
# c[x] = số lượng ước của x

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # Duyệt từng số trong nums
        # Nếu số đó có đúng 4 ước → cộng tổng ước của nó
        return sum(s[i] for i in nums if c[i] == 4)


# ## 📌 Ví dụ minh họa

# Giả sử `nums = [21, 4, 7]`

# Sau tiền xử lý:

# * `c[21] = 4`, `s[21] = 32`
# * `c[4] = 3`
# * `c[7] = 2`

# 👉 Chỉ lấy `21`
# 👉 Kết quả = `32`

# ---

# ## ⚡ Độ phức tạp

# ### ⏱️ Tiền xử lý:

# ```
# O(n log n)
# ```

# (vì giống sàng nguyên tố)

# ### ⏱️ Truy vấn:

# ```
# O(len(nums))
# ```

# 👉 **Rất nhanh** nếu `nums` lớn

# ---

## 👍 Ưu & nhược điểm

# ### ✅ Ưu điểm

# * Code **rất ngắn**
# * Không cần kiểm tra nguyên tố
# * Chạy nhanh với nhiều test

# ### ❌ Nhược điểm

# * Tốn bộ nhớ `O(MAX)`
# * Chỉ phù hợp khi `nums[i] ≤ 10⁵`

# ---

# ## 🧠 So sánh nhanh

# | Cách                      | Ý tưởng  | Khi nên dùng         |
# | ------------------------- | -------- | -------------------- |
# | Duyệt √n                  | Toán học | MAX nhỏ              |
# | **Tiền xử lý (code này)** | Sàng     | Nhiều test, nums lớn |

# ---

# Nếu bạn muốn:

# * 🔹 viết lại **theo kiểu dễ hiểu cho người mới**
# * 🔹 chuyển sang **Java**
# * 🔹 tối ưu bộ nhớ hơn

# cứ nói tiếp nhé 👌

# import java.util.*;

# public class b138 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int n = sc.nextInt();
#         int[] nums = new int[n];

#         // Nhập mảng
#         for (int i = 0; i < n; i++) {
#             nums[i] = sc.nextInt();
#         }

#         int result = 0;

#         // Duyệt từng số trong mảng
#         for (int x : nums) {
#             result += sumFourDivisors(x);
#         }

#         // In kết quả
#         System.out.println(result);

#         sc.close();
#     }

#     static boolean isPrime(int n) {
#         if (n < 2)
#             return false;
#         for (int i = 2; i * i <= n; i++) {
#             if (n % i == 0)
#                 return false;
#         }
#         return true;
#     }

#     // Hàm tính tổng ước nếu n có đúng 4 ước, ngược lại trả 0
#     static int sumFourDivisors(int n) {
#         // Duyệt từ 2 đến căn bậc hai của n
#         for (int i = 2; i * i <= n; i++) {
#             if (n % i == 0) {
#                 int j = n / i;

#                 // Trường hợp 1: n = i^3
#                 if (i == j && i * i * i == n && isPrime(i)) {
#                     return 1 + i + i * i + n;
#                 }

#                 // Trường hợp 2: n = i * j (i != j)
#                 if (i != j && isPrime(i) && isPrime(j)) {
#                     return 1 + i + j + n;
#                 }

#                 // Nếu đã có ước nhưng không thỏa → loại luôn
#                 return 0;
#             }
#         }
#         return 0; // Không có đủ điều kiện
#     }
# }

# // Bài **Four Divisors** thường có nội dung như sau:

# // ---

# // ### 📌 **Đề bài (ý nghĩa)**

# // Bạn được cho **một mảng số nguyên dương** `nums`.

# // Với **mỗi số** trong mảng:

# // * Nếu số đó **có đúng 4 ước số dương khác nhau**, thì **cộng tổng 4 ước số
# // đó** vào kết quả.
# // * Nếu **không có đúng 4 ước**, thì **bỏ qua số đó**.

# // 👉 **Kết quả cuối cùng** là **tổng các tổng ước** của những số thỏa mãn điều
# // kiện.

# // ---

# // ### 📌 **Ước số là gì?**

# // Ước số của một số `n` là các số **chia hết n**.

# // Ví dụ:

# // * Ước của `10` là: `1, 2, 5, 10`
# // * Ước của `6` là: `1, 2, 3, 6`

# // ---

# // ### 📌 **Thế nào là “có đúng 4 ước”?**

# // Một số **chỉ hợp lệ** nếu nó có **chính xác 4 ước khác nhau**.

# // Ví dụ:

# // | Số | Các ước | Số lượng | Hợp lệ? |
# // | -- | ----------- | -------- | ------- |
# // | 6 | 1, 2, 3, 6 | 4 | ✅ |
# // | 10 | 1, 2, 5, 10 | 4 | ✅ |
# // | 8 | 1, 2, 4, 8 | 4 | ✅ |
# // | 9 | 1, 3, 9 | 3 | ❌ |
# // | 7 | 1, 7 | 2 | ❌ |

# // ---

# // ### 📌 **Ví dụ minh họa**

# // **Input:**

# // ```
# // nums = [21, 4, 7]
# // ```

# // Phân tích:

# // * `21` có các ước: `1, 3, 7, 21` → đúng 4 ước → tổng = **32**
# // * `4` có các ước: `1, 2, 4` → 3 ước → bỏ
# // * `7` có các ước: `1, 7` → 2 ước → bỏ

# // 👉 **Output:** `32`

# // ---

# // ### 📌 **Gợi ý quan trọng**

# // Một số có **đúng 4 ước** khi:

# // * Nó có dạng **`p³`** (p là số nguyên tố)
# // Ví dụ: `8 = 2³` → ước: `1, 2, 4, 8`
# // * Hoặc có dạng **`p × q`** (p và q là **hai số nguyên tố khác nhau**)
# // Ví dụ: `10 = 2 × 5`

# // ---

# // Nếu bạn muốn:

# // * 👉 giải bằng **Java**
# // * 👉 giải bằng **Python**
# // * 👉 hoặc phân tích **cách tối ưu thuật toán**

# // cứ nói mình biết nhé 👍
# // Dưới đây là **giải thích thuật toán bài Four Divisors** một cách **ngắn gọn –
# // đúng bản chất – dễ nhớ**.

# // ---

# // ## 🎯 Mục tiêu

# // Với mỗi số `n` trong mảng:

# // * Nếu `n` có **đúng 4 ước số dương khác nhau**
# // * 👉 Cộng **tổng 4 ước đó** vào kết quả

# // ---

# // ## 🔍 Nhận xét then chốt (quan trọng nhất)

# // Một số **chỉ có đúng 4 ước** khi và chỉ khi nó thuộc **1 trong 2 dạng**:

# // ### ✅ **Dạng 1: `n = p³`**

# // * `p` là **số nguyên tố**
# // * Các ước: `1, p, p², p³`

# // 📌 Ví dụ:

# // * `8 = 2³` → ước: `1, 2, 4, 8`
# // * `27 = 3³` → ước: `1, 3, 9, 27`

# // ---

# // ### ✅ **Dạng 2: `n = p × q`**

# // * `p`, `q` là **hai số nguyên tố khác nhau**
# // * Các ước: `1, p, q, p×q`

# // 📌 Ví dụ:

# // * `6 = 2 × 3`
# // * `10 = 2 × 5`
# // * `21 = 3 × 7`

# // ---

# // ## 🧠 Ý tưởng thuật toán

# // ### Với mỗi số `n` trong mảng:

# // ### **Bước 1: Duyệt ước nhỏ nhất**

# // * Duyệt `i` từ `2` đến `√n`
# // * Nếu `i` chia hết `n`:

# // * Ta có cặp ước: `i` và `n / i`

# // ---

# // ### **Bước 2: Phân loại**

# // #### 🔹 Trường hợp A: `i × i × i == n`

# // → `n = i³`
# // → kiểm tra `i` có phải số nguyên tố không
# // → nếu đúng → cộng `1 + i + i² + i³`

# // ---

# // #### 🔹 Trường hợp B: `i != n / i`

# // → kiểm tra:

# // * `i` là số nguyên tố
# // * `n / i` là số nguyên tố

# // → nếu đúng → cộng `1 + i + (n/i) + n`

# // ---

# // ### **Bước 3: Dừng sớm**

# // * Nếu tìm được **hơn 2 ước khác 1 và n** → loại luôn (không thể có đúng 4
# // ước)

# // ---

# // ## ⚡ Vì sao thuật toán nhanh?

# // * Chỉ duyệt đến `√n`
# // * Mỗi số chỉ cần **tìm tối đa 1 cặp ước**
# // * Không liệt kê toàn bộ ước số

# // ⏱️ **Độ phức tạp:**

# // ```
# // O(n × √m)
# // ```

# // với `m` là số lớn nhất trong mảng

# // ---

# // ## 📌 Ví dụ minh họa

# // **n = 21**

# // * `i = 3` → 21 % 3 = 0
# // * `21 = 3 × 7`
# // * 3 và 7 đều là số nguyên tố
# // → hợp lệ
# // → tổng = `1 + 3 + 7 + 21 = 32`

# // ---

# // ## 🧩 Tóm tắt cực ngắn (để nhớ)

# // > Một số có đúng 4 ước **⇔**
# // > 👉 `p³` **hoặc** `p × q` (p, q nguyên tố khác nhau)

# // ---

# // Nếu bạn muốn:

# // * 🔹 giả mã (pseudo-code)
# // * 🔹 code Java theo đúng thuật toán
# // * 🔹 tối ưu hơn bằng sàng nguyên tố

# // chỉ cần nói nhé 👌
