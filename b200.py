# # // // ## 🧩 Minimum Operations to Equalize Binary String (27/02/2026)

# Ok Quang 👌 mình sẽ:

# * 🧠 Giải thích **tư duy toán học đằng sau**
# * 📌 Phân tích từng khối logic
# * 💬 Viết lại code có **chú thích cực rõ từng dòng**

# ---

# # 🎯 Bản chất bài toán

# Ta có:

# * Chuỗi nhị phân `s`
# * Mỗi lần thao tác chọn đúng `k` vị trí và **đảo bit**
# * Hỏi số thao tác nhỏ nhất để chuỗi thành:

#   * toàn `'0'`
#   * hoặc toàn `'1'`

# ---

# # 🔎 Biến quan trọng

# ```python
# n = len(s)
# z = s.count('0')
# ```

# * `n` = độ dài chuỗi
# * `z` = số lượng số 0

# Nếu muốn thành toàn 1 → cần xử lý hết `z` số 0.

# ---

# # ⚠️ Trường hợp đặc biệt: k == n

# ```python
# if n == k:
# ```

# Nếu mỗi lần bắt buộc đảo **toàn bộ chuỗi**:

# * Nếu toàn 1 (`z == 0`) → không cần làm gì → 0
# * Nếu toàn 0 (`z == n`) → đảo 1 lần → 1
# * Nếu lẫn 0 và 1 → không thể cân bằng → -1

# ---

# # 📐 Hàm ceil

# ```python
# def ceil(x, y):
#     return (x + y - 1) // y
# ```

# Đây là công thức:

# [
# \lceil x/y \rceil
# ]

# Ví dụ:

# | x | y | ceil |
# | - | - | ---- |
# | 7 | 3 | 3    |
# | 6 | 3 | 2    |

# Ta dùng để tính:

# 👉 cần ít nhất bao nhiêu lần để xử lý hết `z` số 0 nếu mỗi lần xử lý tối đa `k` số.

# ---

# # 🧠 Ý tưởng chính

# Ta cần tìm số lần thao tác `m` nhỏ nhất.

# Vì mỗi lần đảo k bit → số lượng số 0 thay đổi theo parity (chẵn/lẻ).

# Do đó ta phải xét:

# 1️⃣ m chẵn
# 2️⃣ m lẻ

# ---

# # 📌 Trường hợp 1: m chẵn

# ```python
# if z % 2 == 0:
# ```

# Nếu số 0 ban đầu chẵn → ta có thể làm cho về 0 sau số lần chẵn.

# ---

# ### Tính m

# ```python
# m = max(ceil(z, k), ceil(z, n - k))
# ```

# Giải thích:

# * `ceil(z, k)`
#   → ít nhất bao nhiêu lần để xử lý hết z số 0

# * `ceil(z, n-k)`
#   → đảm bảo không tạo thêm số 0 ngoài ý muốn

# Lấy `max` vì phải thỏa cả hai điều kiện.

# ---

# ### Ép m thành chẵn

# ```python
# if m % 2 == 1:
#     m += 1
# ```

# Nếu m lẻ → tăng 1 để thành chẵn.

# ---

# # 📌 Trường hợp 2: m lẻ

# ```python
# if z % 2 == k % 2:
# ```

# Điều kiện chẵn lẻ phải tương thích.

# ---

# ### Tính m

# ```python
# m = max(ceil(z, k), ceil(n - z, n - k))
# ```

# Ở đây ta xét hướng ngược lại (biến thành toàn 0).

# ---

# ### Ép m thành lẻ

# ```python
# if m % 2 == 0:
#     m += 1
# ```

# ---

# # 📦 Nếu không có đáp án

# ```python
# return ans if ans < inf else -1
# ```

# ---

# # 💬 Code đầy đủ có chú thích chi tiết

# ```python
from math import inf

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        # O(n) time complexity
        # O(1) space complexity

        n = len(s)                 # độ dài chuỗi
        z = s.count('0')           # số lượng số 0 trong chuỗi
        
        # ===== Trường hợp đặc biệt =====
        # Nếu mỗi lần phải đảo toàn bộ chuỗi
        if n == k:
            if z == 0:
                # đã toàn 1
                return 0
            elif z == n:
                # toàn 0 → đảo 1 lần thành toàn 1
                return 1
            else:
                # lẫn 0 và 1 → không thể cân bằng
                return -1
        
        # Hàm tính ceil(x / y)
        def ceil(x, y):
            return (x + y - 1) // y
        
        ans = inf  # lưu đáp án nhỏ nhất
        
        # ===== TH1: số lần thao tác m là CHẴN =====
        # Điều kiện: số 0 ban đầu phải chẵn
        if z % 2 == 0:
            
            # số lần tối thiểu cần thiết
            m = max(
                ceil(z, k),        # đủ lần để xử lý hết số 0
                ceil(z, n - k)     # không tạo thêm 0 ngoài ý muốn
            )
            
            # ép m thành số chẵn
            if m % 2 == 1:
                m += 1
            
            ans = min(ans, m)
        
        # ===== TH2: số lần thao tác m là LẺ =====
        # Điều kiện parity phù hợp
        if z % 2 == k % 2:
            
            m = max(
                ceil(z, k),            # xử lý số 0
                ceil(n - z, n - k)     # xử lý số 1
            )
            
            # ép m thành số lẻ
            if m % 2 == 0:
                m += 1
            
            ans = min(ans, m)
        
        # Nếu không tồn tại đáp án
        return ans if ans < inf else -1
# ```

# ---

# # 🧠 Tóm tắt logic cốt lõi

# | Thành phần | Ý nghĩa                         |
# | ---------- | ------------------------------- |
# | z          | số lượng 0                      |
# | k          | số bit đảo mỗi lần              |
# | ceil(z, k) | số lần tối thiểu để xử lý hết z |
# | parity     | đảm bảo tính chẵn/lẻ đúng       |
# | max(...)   | thỏa cả hai ràng buộc           |
# | ans        | lấy số nhỏ nhất                 |

# ---

# Nếu bạn muốn mình:

# * 🔥 Chứng minh tại sao cần xét parity
# * 🔥 Giải thích vì sao có `ceil(z, n-k)`
# * 🔥 Mô phỏng từng bước với ví dụ cụ thể
# * 🔥 So sánh bản Python với bản Java

# Nói mình biết, mình đào sâu cho bạn tới gốc luôn 💪





# // Ok Quang👌mình sẽ:

# // 1.🔎Giải thích tư duy thuật toán 2.🧠Giải thích từng đoạn logic 3.💬Viết lại code có**chú thích chi tiết**4.🖥Thêm`main()`dùng`Scanner`

# // ---

# // #🧠Ý tưởng thuật toán

# // Ta có:

# // *`s`là chuỗi nhị phân độ dài`n`*`z`=số lượng ký tự`'0'`*Mỗi lần operation sẽ:

# // *Chọn**k vị trí***Và đảo bit tại các vị trí đó

# // ---

# // ##🎯Mục tiêu

# // Biến chuỗi thành:

# // *Toàn`'1'`(tức là số 0 phải trở thành 0)hoặc*Toàn`'0'`

# // ---

# // #🔎Phân tích logic chính

# // ##1 ️⃣Đếm số 0

# // ```java int z=0;for(char ch:s.toCharArray())if(ch=='0')++z;```

# // 👉Ta cần biết có bao nhiêu số 0 vì:

# // *Muốn thành toàn 1→phải xử lý hết số 0

# // ---

# // ##2 ️⃣Trường hợp đặc biệt

# // ###Nếu không có số 0

# // ```java if(z==0)return 0;```

# // Chuỗi đã toàn 1→không cần làm gì.

# // ---

# // ###Nếu k==n

# // ```java if(k==n)return z==n?1:-1;```

# // Nếu mỗi lần phải chọn toàn bộ chuỗi:

# // *Nếu chuỗi toàn 0→lật 1 lần thành toàn 1→trả về 1*Nếu không→không thể cân bằng→-1

# // ---

# // #⚖️ Logic chính:Tính số lần thao tác m

# // Mỗi lần ta đảo k bit→số lượng 0 sẽ thay đổi.

# // Ta cần tìm số m nhỏ nhất sao cho sau m lần:

# // *Hoặc số 0=0*Hoặc số 0=n

# // ---

# // #📌Trường hợp 1:m chẵn

# // ```java if(z%2==0)```

# // Nếu số 0 ban đầu chẵn→sau số lần chẵn thì có thể về 0.

# // Công thức:

# // ```java int m=Math.max((z+k-1)/k,(z+n-k-1)/(n-k));```

# // ###Ý nghĩa:

# // *`(z+k-1)/k`→số lần tối thiểu để loại bỏ hết số 0*`(z+n-k-1)/(n-k)`→đảm bảo không tạo dư số 0

# // 👉Lấy max vì phải thỏa cả hai điều kiện.

# // Sau đó:

# // ```java ans=m%2==0?m:m+1;```

# // Nếu m lẻ→tăng lên 1 để thành chẵn.

# // ---

# // #📌Trường hợp 2:m lẻ

# // ```java if(z%2==k%2)```

# // Điều kiện parity(chẵn lẻ)phải phù hợp.

# // Tính m:

# // ```java int m=Math.max((z+k-1)/k,(n-z+n-k-1)/(n-k));```

# // Sau đó ép m phải lẻ:

# // ```java m=(m%2)!=0?m:m+1;```

# // ---

# // #🧩Nếu không có đáp án

# // ```java if(ans==Integer.MAX_VALUE)return-1;```

# // ---

# // #🖥Code đầy đủ có chú thích+main dùng Scanner

# // ```java

# import java.util.*;

# public class b201 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         String s = sc.next();

#         int k = sc.nextInt();

#         int result = minOperations(s, k);

#         System.out.println(result);
#     }

#     public static int minOperations(String s, int k) {

#         int n = s.length(); // độ dài chuỗi

#         int z = 0; // số lượng ký tự '0'

#         // Đếm số lượng số 0
#         for (char ch : s.toCharArray()) {
#             if (ch == '0')
#                 z++;
#         }

#         // Nếu không có số 0 → đã toàn 1
#         if (z == 0)
#             return 0;

#         // Nếu mỗi lần phải đảo toàn bộ chuỗi
#         if (k == n) {
#             // Nếu toàn 0 → đảo 1 lần
#             if (z == n)
#                 return 1;
#             else
#                 return -1;
#         }

#         int ans = Integer.MAX_VALUE;

#         // ===== Trường hợp số lần thao tác m là chẵn =====
#         if (z % 2 == 0) {

#             // số lần tối thiểu cần thiết
#             int m = Math.max(
#                     (z + k - 1) / k,
#                     (z + n - k - 1) / (n - k));

#             // đảm bảo m là số chẵn
#             if (m % 2 == 0)
#                 ans = m;
#             else
#                 ans = m + 1;
#         }

#         // ===== Trường hợp m là lẻ =====
#         if (z % 2 == k % 2) {

#             int m = Math.max(
#                     (z + k - 1) / k,
#                     (n - z + n - k - 1) / (n - k));

#             // ép m thành số lẻ
#             if (m % 2 != 0)
#                 ans = Math.min(ans, m);
#             else
#                 ans = Math.min(ans, m + 1);
#         }

#         // Nếu không tìm được đáp án
#         if (ans == Integer.MAX_VALUE)
#             return -1;

#         return ans;
#     }
# }

# // ---

# // #🎯

# // Tóm tắt
# // tư duy
# // ngắn gọn

# // |Ý|
# // Giải thích||-------------|-----------------------||z|
# // số lượng số 0||k|
# // số bit
# // được đảo
# // mỗi lần||
# // Mỗi lần|
# // thay đổi
# // k bit||
# // Điều kiện|
# // xét chẵn

# // lẻ (parity) |
# // | Tìm m | nhỏ nhất thỏa điều kiện |
# // | Không tồn tại | trả -1 |

# // ---

# // Nếu bạn muốn mình:

# // * 🔥 Giải thích sâu phần công thức ceil `(a+b-1)/b`
# // * 🔥 Hoặc chứng minh vì sao phải xét chẵn lẻ
# // * 🔥 Hoặc mô phỏng 1 ví dụ cụ thể từng bước

# // Nói mình biết, mình phân tích kỹ hơn cho bạn 💪

# // Bài này cho bạn:

# // * Một **chuỗi nhị phân** `s` (chỉ gồm `'0'` và `'1'`)
# // * Bạn được phép thực hiện một số **thao tác (operations)**

# // 🎯 **Mục tiêu:**
# // Tìm **số thao tác ít nhất** để biến chuỗi thành trạng thái mà tất cả ký tự
# // **giống nhau**
# // → hoặc toàn `'0'`
# // → hoặc toàn `'1'`

# // ---

# // ## 🔄 Thao tác là gì?

# // Mỗi lần thao tác, bạn được phép:

# // * Chọn **một đoạn con liên tiếp**
# // * Và **lật toàn bộ bit trong đoạn đó**

# // * `'0'` → `'1'`
# // * `'1'` → `'0'`

# // ---

# // ## 📌 Ví dụ minh họa

# // ### Ví dụ 1

# // ```
# // Input: s = "0011"
# // ```

# // Chuỗi có:

# // * 2 số 0 đầu
# // * 2 số 1 sau

# // 👉 Nếu muốn toàn 0:

# // * Lật đoạn `"11"` → thành `"00"`

# // Kết quả: `"0000"`
# // ✔ Chỉ cần **1 thao tác**

# // ---

# // ### Ví dụ 2

# // ```
# // Input: s = "0101"
# // ```

# // Chuỗi: xen kẽ 0 và 1

# // Nếu muốn toàn 0:

# // * Lật vị trí 2 (1 → 0)
# // * Lật vị trí 4 (1 → 0)

# // → Cần 2 thao tác

# // Nếu lật từng đoạn thông minh hơn vẫn không ít hơn 2.

# // ---

# // ## 🧠 Bản chất bài toán

# // Điều quan trọng không phải là số lượng 0 hay 1,
# // mà là **số lần chuỗi chuyển từ 0 sang 1 hoặc 1 sang 0**

# // Ví dụ:

# // ```
# // 001100
# // ```

# // Các đoạn giống nhau:

# // * 00
# // * 11
# // * 00

# // Có 3 "block"

# // ---

# // ## 🔑 Insight quan trọng

# // Số thao tác tối thiểu =
# // 👉 **Số block của 0** hoặc **Số block của 1**
# // → lấy **giá trị nhỏ hơn**

# // Vì mỗi lần lật một block sẽ biến block đó thành block kia.

# // ---

# // ## 🎯 Ví dụ phân tích kỹ

# // ### Chuỗi: `"000111000"`

# // Block:

# // * 000
# // * 111
# // * 000

# // → Block 0 = 2
# // → Block 1 = 1

# // Nếu muốn toàn 0:

# // * Lật block 111 → 1 thao tác

# // Nếu muốn toàn 1:

# // * Lật 2 block 000 → 2 thao tác

# // 👉 Chọn nhỏ hơn → **1**

# // ---

# // ## 📎 Tóm tắt dễ hiểu

# // | Ý | Giải thích |
# // | ---------- | ---------------------------- |
# // | Mục tiêu | Làm chuỗi toàn 0 hoặc toàn 1 |
# // | Thao tác | Lật một đoạn liên tiếp |
# // | Chiến lược | Đếm số block 0 và block 1 |
# // | Đáp án | min(block0, block1) |

# // ---

# // Nếu bạn muốn mình giải thích thêm theo hướng tư duy để code (O(n), một vòng
# // for), mình sẽ phân tích từng dòng cho bạn dễ hiểu 👌
