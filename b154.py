# //  //  Construct the Minimum Bitwise Array II(21/01/2026)
# // // // Dưới đây là **giải thích đề bài LeetCode 3315 – Construct the Minimum Bitwise Array II** bằng **tiếng Việt**, theo cách dễ hiểu 👇
# // // Mình sẽ **giải thích thuật toán trong đoạn code này từng bước**, tập trung vào **ý tưởng bitwise** và vì sao công thức đó cho ra **kết quả nhỏ nhất**.
# //  Dưới đây là**phiên bản đầy đủ có`main`dùng`Scanner`**và**chú thích chi tiết từng dòng**đúng theo phong cách bạn hay dùng👍(Mình giữ nguyên thuật toán của bạn,chỉ bổ sung`main`và comment)
# Dưới đây là **giải thích thuật toán + phiên bản code Python có chú thích chi tiết**, bám sát đúng lời giải bạn đưa ra cho **LeetCode 3315 – Construct the Minimum Bitwise Array II**.

# ---

# ## 🧠 Ý tưởng thuật toán (giải thích ngắn gọn – đúng bản chất)

# Với mỗi số `n` trong `nums`, ta cần tìm **giá trị nhỏ nhất `x`** sao cho:

# ```
# x | (x + 1) = n
# ```

# ### 🔹 Nhận xét quan trọng

# * Khi cộng `+1`, các **bit 1 liên tiếp ở cuối** sẽ bị lật thành `0`
# * Bit `0` đầu tiên từ phải sang trái sẽ thành `1`
# * Phép OR của `x` và `x+1` sẽ **bật toàn bộ dải bit đó**

# 👉 Muốn OR ra đúng `n` và `x` **nhỏ nhất**, ta cần:

# * **Tắt đúng 1 bit 1 thấp nhất** trong chuỗi bit 1 liên tiếp bên phải của `n`

# ---

## ❌ Trường hợp đặc biệt: `n = 2`

# ```
# 2 = 10 (nhị phân)
# ```

# Không tồn tại số `x` nào sao cho:

# ```
# x | (x + 1) = 2
# ```

# ➡️ Trả về `-1`

# ---

# ## 🔑 Giải thích công thức bit

# ### Biểu thức cốt lõi

# ```python
# (n + 1) & (-n - 1)
# ```

# * `-n - 1` chính là `~n` (bit đảo của `n`)
# * `(n + 1) & (~n)`:

#   * Xác định **bit 0 thấp nhất trong `n`**
# * Chia `// 2`:

#   * Dịch bit đó sang phải 1 vị trí
#   * Chính là **bit 1 thấp nhất trong chuỗi bit 1 liên tiếp**

# ➡️ Trừ bit này khỏi `n` sẽ cho ra `x` nhỏ nhất thỏa mãn đề bài.

# ---

# ## ✅ Code Python có chú thích chi tiết

# ```python
from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        # Duyệt từng phần tử trong mảng nums
        for n in nums:

            # Trường hợp đặc biệt: n = 2 thì không tồn tại x
            # sao cho x | (x + 1) = 2
            if n == 2:
                ans.append(-1)
            else:
                """
                (n + 1) & (-n - 1)
                = (n + 1) & (~n)

                -> Tìm bit 0 thấp nhất trong n
                -> Sau đó chia cho 2 để lấy bit 1 thấp nhất
                   trong chuỗi các bit 1 liên tiếp bên phải

                Trừ bit này khỏi n để tạo ra x nhỏ nhất
                """
                lowest_bit = ((n + 1) & (-n - 1)) // 2
                ans.append(n - lowest_bit)

        return ans
# ```

# ---

# ## 🧪 Ví dụ minh họa

# ### Input

# ```python
# nums = [7, 2, 5]
# ```

# ### Output

# ```python
# [3, -1, 4]
# ```

# ### Giải thích

# * `7 → 3` vì `3 | 4 = 7`
# * `2 → -1` (không tồn tại)
# * `5 → 4` vì `4 | 5 = 5`

# ---

# ## ⏱️ Độ phức tạp

# * **Thời gian:** `O(n)`
# * **Bộ nhớ:** `O(1)` (ngoài mảng kết quả)
# * Thuật toán **bitwise + greedy**, rất tối ưu

# ---

# Nếu bạn muốn mình:

# * 🔍 Chứng minh vì sao đây là **giá trị nhỏ nhất**
# * ✍️ Viết lại cách làm **không dùng trick bit**
# * 📘 Viết lời giải theo kiểu **bài thi / editorial**

# 👉 Cứ nói tiếp nhé 👍

# //  ---

# //  ###✅Code Java hoàn chỉnh(có`main`,dùng`Scanner`,có chú thích)

# //  ```java

# import java.util.*;

# public class b155 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         // Nhập số lượng phần tử
#         int n = sc.nextInt();

#         List<Integer> nums = new ArrayList<>();

#         // Nhập các phần tử của mảng
#         int i = 0;
#         while (i < n) {
#             nums.add(sc.nextInt());
#             i++;
#         }

#         int[] result = minBitwiseArray(nums);

#         // In kết quả
#         i = 0;
#         while (i < result.length) {
#             System.out.print(result[i] + " ");
#             i++;
#         }

#         sc.close();

#     }

#     public static int[] minBitwiseArray(List<Integer> nums) {
#         int ans[] = new int[nums.size()];

#         // Duyệt từng phần tử trong nums
#         for (int i = 0; i < nums.size(); i++) {
#             int n = nums.get(i);

#             // Trường hợp đặc biệt: n = 2 thì không tồn tại x sao cho x | (x+1) = 2
#             if (n == 2) {
#                 ans[i] = -1;
#             } else {
#                 /*
#                  * (n + 1) & (-n - 1)
#                  * = (n + 1) & (~n)
#                  * -> xác định bit 0 thấp nhất trong n
#                  *
#                  * Chia cho 2 để lấy bit 1 thấp nhất trong chuỗi bit 1 liên tiếp bên phải
#                  * Trừ bit này khỏi n để tạo ra giá trị nhỏ nhất
#                  */
#                 ans[i] = n - (((n + 1) & (-n - 1)) / 2);
#             }
#         }
#         return ans;
#     }

# }

# // trong code

# // *Mỗi`nums[i]`
# // được xử lý**
# // độc lập***Nếu`nums[i]==2`→
# // không có
# // đáp án→`-1`*
# // Ngược lại:

# // *Tìm**bit 1
# // thấp nhất
# // cần tắt***
# // Trừ bit
# // đó khỏi`n`*
# // Đảm bảo:

# // ```ans[i]|(ans[i]+1)=nums[i]```*Và`ans[i]`là**
# // nhỏ nhất**

# // ---

# // ##🧪
# // Ví dụ
# // chạy thử

# // **Input**

# // ```3 7 2 5```

# // **Output**

# // ```3-1 4```

# // ---

# // Nếu bạn muốn:

# // *✨
# // Viết lại theo**while

# // hoàn toàn (không for)**
# // * ✨ Tách hàm tìm bit cho dễ hiểu hơn
# // * ✨ Viết version **giải thích cho thi / phỏng vấn**

# // 👉 Nói mình biết nhé 😄

# // ---

# // ## 📌 Bối cảnh bài toán (nhắc ngắn gọn)

# // Với mỗi phần tử `nums[i]`, ta cần tìm `ans[i]` **nhỏ nhất** sao cho:

# // ```
# // ans[i] | (ans[i] + 1) = nums[i]
# // ```

# // (Nếu không tồn tại → trả về `-1`)

# // ---

# // ## 🔍 Phân tích code tổng thể

# // ```java
# // for(int i = 0; i < nums.size(); i++) {
# // int n = nums.get(i);
# // if(n != 2)
# // ans[i] = n - ((n + 1) & (-n - 1)) / 2;
# // else
# // ans[i] = -1;
# // }
# // ```

# // Thuật toán xử lý **từng số độc lập**, không liên quan đến các phần tử khác.

# // ---

# // ## ❌ Trường hợp đặc biệt: `n == 2`

# // ### Vì sao `n = 2` không có đáp án?

# // ```
# // 2 = 10 (nhị phân)
# // ```

# // Thử mọi `x`:

# // | x | x+1 | x | (x+1) |
# // |---|----|----------|
# // | 0 | 1 | 01 |
# // | 1 | 2 | 11 |
# // | 2 | 3 | 11 |

# // 👉 **Không có cặp nào OR ra đúng `10`**

# // ➡️ **Không tồn tại `ans[i]` → trả `-1`**

# // ---

# // ## 🧠 Ý tưởng chính của thuật toán

# // Ta muốn tìm **số nhỏ nhất `x`** sao cho:

# // ```
# // x | (x + 1) = n
# // ```

# // ### Nhận xét quan trọng

# // * Khi cộng `+1`, các **bit 1 liên tiếp ở cuối** sẽ bị lật thành `0`
# // * Bit `0` đầu tiên từ phải sang trái sẽ thành `1`

# // Ví dụ:

# // ```
# // x = 01101111
# // x + 1 = 01110000
# // ```

# // 👉 OR lại sẽ **bật toàn bộ dải bit đó**

# // ---

# // ## 🔑 Mục tiêu

# // Để `x | (x+1) = n` và `x` **nhỏ nhất**:

# // * Ta cần **tắt bớt bit 1 thấp nhất có thể**
# // * Nhưng vẫn giữ OR không đổi

# // ➡️ Chính là **tắt bit 1 thấp nhất trong dãy bit 1 liên tiếp bên phải của
# // `n`**

# // ---

# // ## 🧩 Giải thích công thức bit

# // ### Dòng quan trọng nhất:

# // ```java
# // (n + 1) & (-n - 1)
# // ```

# // ### Phân tích từng phần

# // #### 1️⃣ `-n - 1` là gì?

# // ```
# // -n - 1 = ~(n)
# // ```

# // (vì `~n = -n - 1` trong hệ bù 2)

# // ➡️ Đây là **bit đảo của `n`**

# // ---

# // #### 2️⃣ `(n + 1) & (~n)`

# // 👉 Kết quả là:

# // * **bit thấp nhất mà `n` có giá trị `0`**
# // * Sau khi cộng `1`, bit đó trở thành `1`
# // * Các bit thấp hơn bị xóa

# // 📌 Đây chính là **bit 0 đầu tiên từ phải sang trái**

# // ---

# // #### 3️⃣ Chia cho 2

# // ```java
# // ((n + 1) & (~n)) / 2
# // ```

# // ➡️ Dịch bit đó sang phải 1 vị trí
# // ➡️ Tương ứng với **bit 1 thấp nhất trong chuỗi 1 liên tiếp của `n`**

# // ---

# // ## 🎯 Công thức cuối cùng

# // ```java
# // ans[i] = n - lowestSetBitInTrailingOnes
# // ```

# // ➡️ Tắt **1 bit nhỏ nhất cần thiết**
# // ➡️ Giữ cho:

# // ```
# // ans[i] | (ans[i] + 1) = n
# // ```

# // ➡️ Và `ans[i]` là **nhỏ nhất có thể**

# // ---

# // ## 🧪 Ví dụ minh họa

# // ### Ví dụ: `n = 7`

# // ```
# // n = 111
# // n+1 = 1000
# // ~n = 000
# // (n+1)&~n = 1000
# // /2 = 0100 = 4
# // ans = 7 - 4 = 3
# // ```

# // Kiểm tra:

# // ```
# // 3 | 4 = 011 | 100 = 111 = 7 ✅
# // ```

# // ---

# // ### Ví dụ: `n = 5`

# // ```
# // n = 101
# // n+1 = 110
# // ~n = 010
# // (n+1)&~n = 010
# // /2 = 001
# // ans = 5 - 1 = 4
# // ```

# // ```
# // 4 | 5 = 100 | 101 = 101 = 5 ✅
# // ```

# // ---

# // ## ✅ Tổng kết thuật toán

# // * ❌ `n == 2` → không có nghiệm
# // * ✅ Các số khác:

# // * Xác định **bit 1 thấp nhất cần tắt**
# // * Trừ nó khỏi `n`
# // * ⏱️ Thời gian: **O(n)**
# // * 🧠 Thuật toán **bitwise + greedy**, cực tối ưu

# // ---

# // Nếu bạn muốn:

# // * 🔍 Chứng minh vì sao đây là **giá trị nhỏ nhất**
# // * 🧠 Viết lại cách hiểu **không dùng công thức bit**
# // * ✍️ Code Python / C++ tương đương

# // 👉 Cứ hỏi tiếp nhé 👍

# // ---

# // ## 📌 Mô tả đề bài (hiểu đơn giản)

# // Bạn được cho một **mảng `nums`** gồm các số nguyên **không âm**.

# // Nhiệm vụ của bạn là **xây dựng một mảng `ans`** (cùng độ dài với `nums`) sao
# // cho:

# // ### 🔹 Điều kiện bắt buộc

# // Với mọi chỉ số `i`:

# // ```
# // (ans[i] OR ans[i+1]) = nums[i]
# // ```

# // * `OR` là phép **OR bit** (`|`)
# // * Điều kiện này áp dụng cho `i` từ `0` đến `n-2`

# // ### 🔹 Mục tiêu

# // Trong tất cả các mảng `ans` thỏa mãn điều kiện trên, hãy tìm mảng **có tổng
# // các phần tử nhỏ nhất**
# // (tức là **minimum bitwise array**).

# // ---

# // ## 🧠 Nhắc lại phép OR bit là gì?

# // * OR bit (`|`) hoạt động trên từng bit:

# // * `0 | 0 = 0`
# // * `0 | 1 = 1`
# // * `1 | 1 = 1`

# // Ví dụ:

# // ```
# // 5 | 3 = 101 | 011 = 111 = 7
# // ```

# // ---

# // ## 🔍 Ý nghĩa của điều kiện `(ans[i] | ans[i+1]) = nums[i]`

# // Điều này có nghĩa là:

# // * **Mỗi bit bằng 1 trong `nums[i]`**
# // → phải có **ít nhất một trong hai số `ans[i]` hoặc `ans[i+1]` có bit đó = 1**

# // * **Mỗi bit bằng 0 trong `nums[i]`**
# // → **cả `ans[i]` và `ans[i+1]` đều phải có bit đó = 0**

# // ---

# // ## 🎯 Mục tiêu “minimum” nghĩa là gì?

# // Bạn **không được tùy ý đặt bit 1**, vì:

# // * Bit 1 làm số lớn hơn
# // * Tổng mảng `ans` sẽ lớn hơn

# // 👉 Vì vậy:

# // * **Chỉ bật bit 1 khi bắt buộc**
# // * Nếu một bit có thể đặt ở **một trong hai vị trí**, hãy đặt sao cho **tổng
# // nhỏ nhất**

# // ---

# // ## 📖 Ví dụ minh họa

# // ### Ví dụ 1

# // ```
# // nums = [3, 1]
# // ```

# // * `3 = 11 (nhị phân)`
# // * `1 = 01`

# // Cần:

# // ```
# // ans[0] | ans[1] = 3
# // ```

# // Một cách hợp lệ và nhỏ nhất:

# // ```
# // ans = [2, 1]
# // 2 | 1 = 3
# // ```

# // Tổng = `3` (nhỏ nhất)

# // ---

# // ### Ví dụ 2

# // ```
# // nums = [1, 0]
# // ```

# // * `1 = 01`
# // * `0 = 00`

# // Cần:

# // ```
# // ans[0] | ans[1] = 1
# // ans[1] | ans[2] = 0
# // ```

# // Điều này buộc:

# // * Bit 0 phải xuất hiện ở cặp đầu
# // * Không được xuất hiện ở cặp sau

# // ---

# // ## 🔑 Tóm tắt ý chính của đề

# // * Bạn cần **xây dựng mảng `ans`**
# // * Thỏa mãn:

# // ```
# // ans[i] | ans[i+1] = nums[i]
# // ```
# // * Trong số các mảng hợp lệ, chọn mảng có **tổng nhỏ nhất**
# // * Bài này kiểm tra:

# // * Hiểu phép OR bit
# // * Cách **phân phối bit 1 tối ưu**
# // * Tư duy bitmask / greedy

# // ---

# // Nếu bạn muốn:

# // * ✅ Giải thích **ý tưởng giải (greedy / bitwise)**
# // * ✅ Viết **code Java / C++ / Python**
# // * ✅ Phân tích từng bit cụ thể

# // 👉 Cứ nói tiếp nhé 👍
