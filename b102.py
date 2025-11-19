# // 2154. Keep Multiplying Found Values by Two(19/11/2025)
# Dưới đây là **giải thích thuật toán** và **code có chú thích đầy đủ**, giúp bạn hiểu rõ logic bit manipulation được dùng trong lời giải Python này.

# ---

# # ✅ **Giải thích thuật toán**

# Bài toán yêu cầu:

# * Cho mảng `nums` và số `k`
# * Tìm giá trị cuối cùng bằng cách: nếu `k` xuất hiện trong mảng thì nhân đôi k → k*2 → k*4 → k*8 → ... cho đến khi số đó **không xuất hiện trong mảng**.

# Nhưng đoạn code Python này **không làm theo cách brute-force**.
# Nó sử dụng **bitmask + toán tử bit** để tìm luôn kết quả cuối cùng trong O(n).

# ---

# # 🔥 Ý tưởng chính

# ## **1) Chỉ quan tâm đến những số trong nums chia hết cho k**

# ```python
# if num % k != 0: continue
# ```

# Vì nếu một số không phải dạng:
# 👉 `k * (2^x)`
# thì không ảnh hưởng gì tới kết quả.

# ---

# ## **2) Kiểm tra num/k có phải lũy thừa của 2?**

# ```python
# n = num // k
# if n & (n - 1) == 0:
# ```

# → Điều kiện để kiểm tra 1 số có phải power-of-two không.

# Nếu `num = k * 2^x` thì `n = 2^x`, thỏa điều kiện.

# ---

# ## **3) Ghi nhận tất cả 2^x bằng bitmask**

# ```python
# bits |= n
# ```

# Ví dụ nums chứa:
# `k, 2k, 4k`
# thì ta ghi:

# * 1  (2^0)
# * 2  (2^1)
# * 4  (2^2)

# `bits = 1 | 2 | 4 = 0b0111`

# ---

# ## **4) Tìm bit 0 đầu tiên chưa dùng**

# Sau khi gom hết bit đã có, ta làm:

# ```python
# d = bits + 1
# return k * (d & -d)
# # ```

# Đây là trick kinh điển:

# | bits   | bits+1 | d & -d | Kết quả |
# | ------ | ------ | ------ | ------- |
# | 0b0111 | 0b1000 | 0b1000 | 8       |

# → Số nhỏ nhất dạng power-of-two **chưa xuất hiện**.

# Vậy kết quả là:
# 👉 `k * (power_of_two_chưa_xuất_hiện)`

# ---

# # ⭐ code có chú thích đầy đủ

# ```python
from typing import List
class Solution:
    def findFinalValue(self, nums: list[int], k: int) -> int:
        bits = 0  # bitmask lưu các lũy thừa 2 xuất hiện: 1,2,4,8,...

        for num in nums:
            # chỉ xét num nếu chia hết cho k
            if num % k != 0:
                continue

            n = num // k  # xem num = k * (2^x) hay không

            # kiểm tra n có phải lũy thừa của 2 không (power of two)
            # trick: (x & (x-1)) == 0 <=> x là lũy thừa của 2
            if n & (n - 1) == 0:
                bits |= n     # bật bit tương ứng 2^x

        # bits chứa tất cả power-of-two đã tồn tại
        # ví dụ bits = 0b0111 nghĩa là {1,2,4} tồn tại

        d = bits + 1   # tìm bit 0 đầu tiên chưa xuất hiện
        missing_power = d & -d  # tách bit thấp nhất của d

        # kết quả = k * power-of-two chưa xuất hiện
        return k * missing_power


# 📌 Ví dụ minh họa

# Giả sử:

# ```
# nums = [4, 8, 16]
# k = 4
# ```

# → n = num/k = {1,2,4} là power-of-2
# → bits = 1 | 2 | 4 = 0b111
# → bits + 1 = 0b1000
# → d & -d = 0b1000 = 8

# ⇒ kết quả = 4 * 8 = **32**

# ---

# Nếu bạn muốn mình **vẽ biểu đồ bit minh họa từng bước**, mình có thể làm thêm!


# // Dưới đây là **giải thích đề bài LeetCode 2154 – Keep Multiplying Found Values by Two**, thật rõ ràng và dễ hiểu:
# import java.util.*;

# public class b103 {

#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int n = sc.nextInt();

#         int[] nums = new int[n];

#         for (int i = 0; i < n; i++) {
#             nums[i] = sc.nextInt();
#         }

#         int original = sc.nextInt();

#         // Gọi hàm và in kết quả
#         int result = findFinalValue(nums, original);
#         System.out.println(result);

#         sc.close();
#     }

#     public static int findFinalValue(int[] nums, int original) {

#         boolean x = true; // cờ để điều khiển while-loop

#         // Lặp cho đến khi original KHÔNG còn xuất hiện trong nums
#         while (x) {
#             x = found(nums, original); // kiểm tra original có nằm trong nums không
#             original *= 2; // nếu có thì nhân đôi
#         }

#         // Vì lần cuối while đã nhân đôi thêm 1 lần không cần thiết,
#         // nên phải chia 2 để lấy lại giá trị đúng
#         return original / 2;
#     }

#     // Hàm kiểm tra một số có xuất hiện trong mảng hay không
#     public static boolean found(int[] nums, int var) {

#         // duyệt từng phần tử của mảng
#         for (int ele : nums) {

#             // nếu tìm thấy var trong nums → trả về true
#             if (ele == var) {
#                 return true;
#             }
#         }

#         // nếu duyệt hết mà không có → trả về false
#         return false;
#     }
# }

# // ---

# // # 🧩 **2154. Keep Multiplying Found Values by Two — Giải thích đề bài**

# // Bạn được cho:

# // * Một mảng số nguyên **`nums`**
# // * Một số nguyên **`original`**

# // Nhiệm vụ:

# // 👉 **Trong khi `original` còn xuất hiện trong `nums`, bạn phải nhân
# // `original` lên 2.**

# // Khi nào `original` không còn nằm trong `nums` nữa → **trả về giá trị của
# // `original`** lúc đó.

# // ---

# // # 🔍 **Ví dụ để hiểu ngay lập tức**

# // ### **Ví dụ 1**

# // ```
# // nums = [5,3,6,1,12]
# // original = 3
# // ```

# // * 3 có trong nums → nhân 2 → original = 6
# // * 6 có trong nums → nhân 2 → original = 12
# // * 12 có trong nums → nhân 2 → original = 24
# // * 24 **không có** trong nums → dừng → trả về **24**

# // ---

# // ### **Ví dụ 2**

# // ```
# // nums = [2,7,9]
# // original = 4
# // ```

# // 4 **không xuất hiện** trong mảng → trả về **4** ngay lập tức.

# // ---

# // # 🎯 **Tóm tắt yêu cầu**

# // * Lặp lại nhiều lần:

# // * Nếu `original` nằm trong `nums`, biến nó thành `original * 2`
# // * Ngược lại, dừng và trả về giá trị hiện tại của `original`

# // Đó là toàn bộ bài toán — rất đơn giản và tuyến tính.

# // ---

# // Nếu bạn muốn tiếp tục, mình có thể:

# // ✅ giải thích thuật toán
# // ✅ viết code Python/Java
# // ✅ thêm comment từng dòng
# // Chỉ cần bạn nói tiếp nhé!
# // Dưới đây là **giải thích thuật toán** rõ ràng, dễ hiểu cho đoạn code Java bạn
# // đưa:

# // ---

# // # 🔍 **Giải thích thuật toán**

# // ### **Ý tưởng chung**

# // * Kiểm tra xem giá trị `original` có trong mảng `nums` hay không.
# // * Nếu có → nhân `original` lên 2 → tiếp tục kiểm tra.
# // * Nếu không có → dừng → trả về giá trị cuối cùng.

# // ---

# // # 🧠 **Giải thích code chi tiết**

# // ## **Hàm chính**

# // ```java
# // public int findFinalValue(int[] nums, int original) {
# // boolean x = true;
# // while (x) {
# // x = found(nums, original);
# // original *= 2;
# // }
# // return original / 2;
# // }
# // ```

# // ### 🔹 **`boolean x = true;`**

# // Dùng biến cờ để điều khiển vòng lặp.

# // ### 🔹 **`while (x)`**

# // Tiếp tục lặp cho đến khi không tìm thấy `original` trong `nums`.

# // ### 🔹 **`x = found(nums, original);`**

# // Gọi hàm `found()`:

# // * Nếu `original` có trong `nums` → trả về `true`
# // * Nếu không có → trả về `false`

# // ### 🔹 **`original *= 2;`**

# // Sau mỗi lần kiểm tra, bạn nhân original lên 2.

# // 📌 **Lưu ý:** Khi `found()` trả về `false`, bạn vẫn nhân `original` lên 2
# // thêm một lần nữa → vì vậy sau vòng lặp phải **chia lại 2** để trả về đúng kết
# // quả.

# // ### 🔹 **`return original / 2;`**

# // Do lần cuối bạn nhân original lên 2 không cần thiết → trả lại giá trị trước
# // đó.

# // ---

# // ## **Hàm phụ `found()`**

# // ```java
# // public boolean found(int [] nums, int var){
# // for(int ele : nums){
# // if(ele == var){
# // return true;
# // }
# // }
# // return false;
# // }
# // ```

# // ### **Giải thích**

# // * Duyệt toàn bộ mảng `nums`
# // * Nếu có phần tử bằng `var` → trả về `true`
# // * Nếu duyệt hết mảng không tìm được → trả về `false`

# // Đây là **tìm kiếm tuyến tính** (linear search).

# // ---

# // # ✔️ **Mô phỏng chạy thử**

# // ```
# // nums = [5,3,6,1,12]
# // original = 3
# // ```

# // 1. found(3) → true → original = 6
# // 2. found(6) → true → original = 12
# // 3. found(12) → true → original = 24
# // 4. found(24) → false → original = 48
# // → return 48/2 = **24**

# // ---

# // # ⭐ **Kết luận thuật toán**

# // * Thuật toán dùng vòng lặp while để kiểm tra liên tục
# // * Mỗi lần tìm thấy giá trị thì nhân đôi
# // * Kết thúc khi không còn trong mảng
# // * Dùng tìm kiếm tuyến tính O(n)
# // * Tổng thời gian: O(n * số_lần_nhân_đôi)

# // ---

# // Nếu bạn muốn mình thêm **comment vào code**, hoặc viết lại cách tối ưu hơn,
# // mình có thể làm ngay!
