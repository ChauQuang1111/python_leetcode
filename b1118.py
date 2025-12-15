# # //  Number of Smooth Descent Periods of a Stock
# OK, đoạn code này **rất “Pythonic” và khó hiểu** 😄
# Mình sẽ **giải thích thuật toán từ ý tưởng → rồi chú thích chi tiết từng phần của code** cho bạn nhé.

# ---

# ## 🧠 Ý tưởng bài toán (nhắc lại nhanh)

# Một **smooth descent period** là một đoạn con liên tiếp sao cho:

# ```
# a[i] = a[i-1] - 1
# ```

# Ví dụ:

# ```
# [8, 7, 6, 5]
# ```

# Các đoạn giảm liên tiếp tạo thành **1 block giảm** dài 4
# Số đoạn con giảm trong block dài `k` là:

# [
# 1 + 2 + 3 + ... + k = \frac{k(k+1)}{2}
# ]

# 👉 Tổng kết:

# * Mỗi **block giảm liên tiếp** → dùng công thức tổ hợp
# * Mỗi phần tử đơn lẻ cũng là 1 block độ dài 1

# ---

# ## 📌 Ý tưởng của code này

# 1. **Chuyển mảng giá thành mảng hiệu**:

#    ```
#    a[i] - a[i+1]
#    ```
# 2. **Tìm các đoạn liên tiếp có hiệu = 1**
# 3. Với mỗi đoạn có độ dài `k`:

#    * cộng `k*(k+1)/2`
# 4. Cuối cùng cộng thêm `len(a)` cho các phần tử đơn lẻ

# ---

# ## 🔍 Code gốc

# ```python
# class Solution:
#     def getDescentPeriods(self, a: List[int]) -> int:
#         return sum(
#             comb(sum(g) + 1, 2)
#             for d, g in groupby(map(sub, a, a[1:]))
#             if d == 1
#         ) + len(a)
# ```

# ---

# ## ✨ Giải thích từng phần (rất kỹ)

# ### 1️⃣ `map(sub, a, a[1:])`

# ```python
# map(sub, a, a[1:])
# ```

# Tương đương:

# ```python
# [a[i] - a[i+1] for i in range(len(a)-1)]
# ```

# 📌 Ví dụ:

# ```python
# a = [8, 7, 6, 5]
# ```

# Kết quả:

# ```
# [1, 1, 1]
# ```

# ---

# ### 2️⃣ `groupby(...)`

# ```python
# groupby(map(sub, a, a[1:]))
# ```

# 👉 Gom các giá trị **giống nhau liên tiếp**

# Ví dụ:

# ```
# [1, 1, 1, 0, 1, 1]
# ```

# Thành:

# ```
# (1, [1,1,1])
# (0, [0])
# (1, [1,1])
# ```

# ---

# ### 3️⃣ `for d, g in groupby(...) if d == 1`

# * `d` → giá trị (hiệu)
# * `g` → nhóm các phần tử liên tiếp

# Chỉ xử lý **những nhóm có `d == 1`**
# 👉 nghĩa là **đang giảm đều**

# ---

# ### 4️⃣ `sum(g)`

# ⚠️ Lưu ý đặc biệt:

# * `g` chứa toàn số `1`
# * `sum(g)` = số lượng phần tử trong nhóm

# Ví dụ:

# ```python
# g = [1, 1, 1]
# sum(g) = 3
# ```

# ---

# ### 5️⃣ `comb(sum(g) + 1, 2)`

# 📌 Nếu có `k` hiệu bằng 1 liên tiếp
# → số phần tử trong block = `k + 1`

# Số đoạn giảm trong block:

# ```python
# comb(k+1, 2) = (k+1)*k / 2
# ```

# Ví dụ:

# ```
# [8,7,6,5] → k = 3 → comb(4,2) = 6
# ```

# ---

# ### 6️⃣ `sum(...) + len(a)`

# ```python
# + len(a)
# ```

# 📌 Vì:

# * Mỗi phần tử riêng lẻ cũng là 1 smooth descent period

# ---

# ## 🧾 Viết lại dễ hiểu hơn (có chú thích)

from itertools import groupby
from operator import sub
from math import comb

class Solution:
    def getDescentPeriods(self, a):
        # Tính hiệu a[i] - a[i+1]
        diffs = map(sub, a, a[1:])

        total = 0

        # Gom các hiệu liên tiếp
        for d, g in groupby(diffs):
            if d == 1:  # chỉ xét đoạn giảm đều
                k = sum(g)        # số hiệu = 1 liên tiếp
                total += comb(k + 1, 2)  # số đoạn giảm trong block

        # cộng các đoạn đơn lẻ
        return total + len(a)


## 🧠 Tóm tắt cực ngắn

# | Thành phần           | Ý nghĩa           |
# | -------------------- | ----------------- |
# | `map(sub, a, a[1:])` | Tạo mảng hiệu     |
# | `groupby`            | Gom các đoạn giảm |
# | `d == 1`             | Đang giảm đều     |
# | `comb(k+1,2)`        | Đếm số đoạn       |
# | `+ len(a)`           | Đếm đoạn đơn      |

# ---

# Nếu bạn muốn 👉

# * Mình **viết lại bằng vòng `for` thường**
# * Hoặc **vẽ minh họa từng bước**
# * Hoặc **so sánh với Java version**

# 👉 cứ nói nhé, mình sẽ làm cho dễ hiểu nhất 👍

# //  Mình giải thích **đề bài “Number of Smooth Descent Periods of a Stock”** thật **dễ hiểu, đúng bản chất**, không dùng thuật ngữ khó nhé 👌
# import java.util.*;

# public class b119 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int n = sc.nextInt();

#         // Khai báo mảng giá
#         int[] prices = new int[n];

#         // Nhập các giá cổ phiếu
#         for (int i = 0; i < n; i++) {
#             prices[i] = sc.nextInt();
#         }

#         // Gọi hàm và in kết quả
#         long result = getDescentPeriods(prices);
#         System.out.println(result);

#         sc.close();

#     }

#     // Hàm chính giải bài toán
#     public static long getDescentPeriods(int[] prices) {
#         // ans: tổng số smooth descent periods
#         // count: độ dài đoạn giảm liên tiếp hiện tại
#         long ans = 1, count = 1;

#         // Duyệt từ phần tử đầu đến gần cuối
#         for (int i = 0; i < prices.length - 1; i++) {

#             // Nếu giá hôm nay = giá ngày mai + 1
#             // tức là đang giảm đều 1 đơn vị
#             if (prices[i] == prices[i + 1] + 1) {
#                 count++; // kéo dài đoạn giảm
#             } else {
#                 count = 1; // không giảm đều → bắt đầu lại
#             }

#             // Mỗi vị trí sẽ đóng góp thêm count dãy hợp lệ
#             ans += count;
#         }

#         return ans;
#     }

# }

# // ---

# // ## 📌 1. Đề bài nói gì?

# // Bạn được cho một mảng `prices[]`
# // → mỗi phần tử là **giá cổ phiếu theo từng ngày**.

# // ### 🎯 Nhiệm vụ:

# // 👉 **Đếm số “smooth descent period”** trong mảng này.

# // ---

# // ## 📉 2. “Smooth descent period” là gì?

# // Một **smooth descent period** là:

# // * Một **dãy con liên tiếp**
# // * Mỗi ngày **giảm đúng 1 đơn vị so với ngày trước**

# // ### Công thức:

# // ```
# // prices[i] == prices[i-1] - 1
# // ```

# // ---

# // ## ✅ 3. Những dãy nào được tính?

# // ### ✔️ Dãy **1 phần tử** → LUÔN HỢP LỆ

# // Ví dụ:

# // ```
# // [7], [6], [5]
# // ```

# // ---

# // ### ✔️ Dãy nhiều phần tử

# // Chỉ hợp lệ nếu:

# // ```
# // 7 → 6 → 5 → 4
# // ```

# // ---

# // ### ❌ Không hợp lệ

# // ```
# // 7 → 5 (giảm 2)
# // 7 → 6 → 4
# // ```

# // ---

# // ## 🧠 4. Ví dụ minh họa

# // ### Ví dụ 1:

# // ```text
# // prices = [3, 2, 1, 4]
# // ```

# // Các smooth descent periods:

# // * Đơn lẻ:

# // ```
# // [3], [2], [1], [4]
# // ```

# // → 4

# // * Dãy giảm đều:

# // ```
# // [3,2], [2,1], [3,2,1]
# // ```

# // → 3

# // ❌ `[1,4]` không hợp lệ

# // 👉 **Tổng = 7**

# // ---

# // ### Ví dụ 2:

# // ```text
# // prices = [8,7,6,5]
# // ```

# // Dãy hợp lệ:

# // * 1 phần tử: 4
# // * 2 phần tử: 3
# // * 3 phần tử: 2
# // * 4 phần tử: 1

# // 👉 Tổng:

# // ```
# // 4 + 3 + 2 + 1 = 10
# // ```

# // ---

# // ## 📐 5. Vì sao phải giảm đúng 1?

# // Đề bài yêu cầu **smooth**
# // → nghĩa là **giảm đều, không nhảy bậc**

# // ```
# // 10 → 9 → 8 ✔
# // 10 → 8 ❌
# // ```

# // ---

# // ## 🧩 6. Bài toán thực chất là gì?

# // 👉 Tìm **độ dài các đoạn liên tiếp mà:**

# // ```
# // prices[i] = prices[i-1] - 1
# // ```

# // Sau đó:

# // * Nếu đoạn có độ dài `k`
# // * Số dãy con hợp lệ là:

# // ```
# // k * (k + 1) / 2
# // ```

# // ---

# // ## 🎯 7. Tóm tắt cực ngắn

# // > **Đếm tất cả các dãy con liên tiếp mà mỗi ngày giá giảm đúng 1 so với ngày
# // trước (kể cả dãy 1 ngày).**

# // ---

# // Nếu bạn muốn:

# // * Mình giải **thuật toán O(n)** dễ nhớ
# // * Hoặc viết **code Python / Java + chú thích từng dòng**

# // 👉 nói mình biết nha 👍
# // Mình giải thích **thuật toán trong code này** theo cách **rất dễ hiểu, từng
# // bước, có ví dụ cụ thể** nhé 👍

# // ---

# // ## 📌 Mục tiêu của bài toán

# // Đếm **tổng số smooth descent periods** trong mảng `prices`.

# // 👉 **Smooth descent period** = dãy liên tiếp mà:

# // ```
# // giá hôm nay = giá hôm trước − 1
# // ```

# // (dãy 1 phần tử cũng được tính)

# // ---

# // ## 🧠 Ý tưởng cốt lõi của thuật toán

# // Thay vì xét mọi dãy con (rất chậm), ta:

# // 👉 **Duyệt từ trái sang phải**
# // 👉 Đếm độ dài của đoạn đang giảm đều
# // 👉 Mỗi khi đoạn kéo dài thêm 1 phần tử → số dãy hợp lệ tăng thêm

# // ---

# // ## 🔍 Giải thích từng biến

# // ```java
# // long ans = 1;
# // ```

# // * Kết quả cuối cùng
# // * Bắt đầu = 1 vì:

# // * Phần tử đầu tiên **luôn là một descent period**

# // ---

# // ```java
# // long count = 1;
# // ```

# // * `count` = độ dài **đoạn giảm liên tiếp hiện tại**
# // * Ban đầu = 1 (1 phần tử)

# // ---

# // ## 🔁 Vòng lặp chính

# // ```java
# // for(int i = 0; i < prices.length - 1; i++) {
# // ```

# // Duyệt từng cặp:

# // ```
# // prices[i] và prices[i + 1]
# // ```

# // ---

# // ### ✅ Trường hợp 1: tiếp tục giảm đều

# // ```java
# // if(prices[i] == prices[i + 1] + 1)
# // count++;
# // ```

# // 👉 Nghĩa là:

# // ```
# // prices[i] = prices[i+1] + 1
# // ↔ prices[i+1] = prices[i] - 1
# // ```

# // ➡️ Dãy giảm vẫn tiếp tục
# // ➡️ Độ dài đoạn tăng lên 1

# // ---

# // ### ❌ Trường hợp 2: không giảm đều

# // ```java
# // else
# // count = 1;
# // ```

# // 👉 Dãy giảm bị ngắt
# // ➡️ Bắt đầu lại từ phần tử hiện tại

# // ---

# // ### ➕ Cộng vào kết quả

# // ```java
# // ans += count;
# // ```

# // 📌 Vì sao cộng `count`?

# // Giả sử đoạn hiện tại dài `count = k`

# // → Có đúng `k` dãy con kết thúc tại vị trí này là smooth descent

# // ---

# // ## 📘 Ví dụ chạy tay

# // ### Input:

# // ```text
# // prices = [8, 7, 6, 5]
# // ```

# // | i | prices[i] | prices[i+1] | count | ans |
# // | - | --------- | ----------- | ----- | --- |
# // | - | 8 | | 1 | 1 |
# // | 0 | 8 → 7 | giảm đúng 1 | 2 | 3 |
# // | 1 | 7 → 6 | giảm đúng 1 | 3 | 6 |
# // | 2 | 6 → 5 | giảm đúng 1 | 4 | 10 |

# // ➡️ Kết quả = **10**

# // ---

# // ## 📊 Ví dụ khác

# // ```text
# // prices = [3, 2, 1, 4]
# // ```

# // | i | so sánh | count | ans |
# // | - | ------- | ----- | --- |
# // | - | | 1 | 1 |
# // | 0 | 3→2 | 2 | 3 |
# // | 1 | 2→1 | 3 | 6 |
# // | 2 | 1→4 ❌ | 1 | 7 |

# // ➡️ Kết quả = **7**

# // ---

# // ## ⚡ Độ phức tạp

# // * **Time**: `O(n)` (duyệt 1 lần)
# // * **Space**: `O(1)` (chỉ dùng biến)

# // ---

# // ## 🎯 Tóm tắt ngắn gọn

# // * `count` = độ dài đoạn giảm liên tiếp
# // * Mỗi bước:

# // * Nếu tiếp tục giảm → `count++`
# // * Ngược lại → `count = 1`
# // * Cộng `count` vào kết quả

# // ---

# // Nếu bạn muốn:

# // * Mình vẽ **sơ đồ trực quan**
# // * Hoặc giải lại bằng **ngôn ngữ cực đời thường**
# // * Hoặc viết lại code có **comment từng dòng**

# // 👉 nói mình biết nha 😄
