# # // Bài **“Minimum Number of Seconds to Make Mountain Height Zero”(13/03/2026)

# # // Mình sẽ**giải thích thuật toán trước**,sau đó đưa**code đầy đủ có`main`+`Scanner`+chú thích từng dòng**.

from math import sqrt, floor, ceil
from typing import List

class Solution:
    def minNumberOfSeconds(self, H: int, arr: List[int]) -> int:

        # Tổng thời gian cơ bản của tất cả worker (không thực sự dùng trong thuật toán)
        S = sum(arr)

        # Số worker
        N = len(arr)

        # Số lần tối đa mỗi worker phải phá nếu chia đều công việc
        # V = ceil(H / N)
        V = ceil(H / N)

        # start = thời gian nhỏ nhất có thể
        start = 1

        # end = upper bound
        # trường hợp xấu nhất: worker chậm nhất làm V lần
        end = V * (V + 1) * max(arr) // 2

        # Binary Search trên thời gian
        while start < end:

            # thời gian đang thử
            mid = (start + end) // 2

            # W = tổng số lần phá được trong mid giây
            W = 0

            # tính số lần phá của từng worker
            for T in arr:

                # số lần worker này phá được trong mid giây
                # giải phương trình:
                # T * k(k+1)/2 <= mid
                k = floor(sqrt(2 * mid / T + 0.25) - 0.5)

                # cộng vào tổng
                W += k

            # nếu tổng phá >= chiều cao núi
            if W >= H:
                # thời gian đủ → thử giảm thời gian
                end = mid
            else:
                # chưa đủ → cần thêm thời gian
                start = mid + 1

        # thời gian nhỏ nhất
        return start

# Bài **Minimum Number of Seconds to Make Mountain Height Zero** dùng **Binary Search trên thời gian**.
# Ý tưởng giống code Java bạn gửi trước, nhưng Python dùng công thức `sqrt` viết hơi khác một chút.

# ---

# # 1. Ý tưởng thuật toán

# Ta cần tìm **thời gian nhỏ nhất `T`** để tất cả worker **phá được ít nhất `H` chiều cao núi**.

# Mỗi worker có thời gian cơ bản `T`.

# Nếu worker có thời gian `t`, các lần phá sẽ mất:

# ```
# t, 2t, 3t, 4t, ...
# ```

# Nếu worker phá `k` lần thì tổng thời gian:

# [
# t(1+2+3+...+k)
# ]

# [
# = t \cdot \frac{k(k+1)}{2}
# ]

# Worker phá được `k` lần nếu:

# [
# t \cdot \frac{k(k+1)}{2} \le time
# ]

# Từ đó ta suy ra `k` bằng công thức `sqrt`.

# ---

# # 2. Binary Search trên thời gian

# Ta không biết **cần bao nhiêu giây**, nên:

# ```
# left = thời gian nhỏ nhất
# right = thời gian chắc chắn đủ
# ```

# Sau đó:

# ```
# mid = (left + right) / 2
# ```

# Kiểm tra:

# ```
# mid giây → phá được bao nhiêu height
# ```

# Nếu đủ → giảm `right`

# Nếu chưa đủ → tăng `left`

# ---

# # 3. Code có chú thích chi tiết

# ```python
# from math import sqrt, floor, ceil
# from typing import List

# class Solution:
#     def minNumberOfSeconds(self, H: int, arr: List[int]) -> int:

#         # Tổng thời gian cơ bản của tất cả worker (không thực sự dùng trong thuật toán)
#         S = sum(arr)

#         # Số worker
#         N = len(arr)

#         # Số lần tối đa mỗi worker phải phá nếu chia đều công việc
#         # V = ceil(H / N)
#         V = ceil(H / N)

#         # start = thời gian nhỏ nhất có thể
#         start = 1

#         # end = upper bound
#         # trường hợp xấu nhất: worker chậm nhất làm V lần
#         end = V * (V + 1) * max(arr) // 2

#         # Binary Search trên thời gian
#         while start < end:

#             # thời gian đang thử
#             mid = (start + end) // 2

#             # W = tổng số lần phá được trong mid giây
#             W = 0

#             # tính số lần phá của từng worker
#             for T in arr:

#                 # số lần worker này phá được trong mid giây
#                 # giải phương trình:
#                 # T * k(k+1)/2 <= mid
#                 k = floor(sqrt(2 * mid / T + 0.25) - 0.5)

#                 # cộng vào tổng
#                 W += k

#             # nếu tổng phá >= chiều cao núi
#             if W >= H:
#                 # thời gian đủ → thử giảm thời gian
#                 end = mid
#             else:
#                 # chưa đủ → cần thêm thời gian
#                 start = mid + 1

#         # thời gian nhỏ nhất
#         return start
# ```

# ---

# # 4. Vì sao công thức sqrt viết dạng này

# Trong Java bạn thấy:

# ```
# (-1 + sqrt(1 + 8*time/x)) / 2
# ```

# Python viết lại thành:

# [
# k = \sqrt{\frac{2time}{T} + 0.25} - 0.5
# ]

# Hai công thức **tương đương nhau**.

# Vì:

# [
# \frac{-1 + \sqrt{1 + 8A}}{2}
# ============================

# \sqrt{2A + 0.25} - 0.5
# ]

# Trong đó:

# ```
# A = time / T
# ```

# ---

# # 5. Ví dụ trực quan

# Giả sử

# ```
# H = 4
# arr = [1,2]
# ```

# Worker 1:

# ```
# 1 + 2 = 3 giây → phá 2
# ```

# Worker 2:

# ```
# 2 giây → phá 1
# ```

# Tổng:

# ```
# 2 + 1 = 3
# ```

# Binary search sẽ thử:

# ```
# time = 3
# ```

# Nếu đủ → giảm tiếp.

# ---

# # 6. Độ phức tạp

# Binary search:

# ```
# O(log T)
# ```

# Mỗi lần kiểm tra:

# ```
# O(N)
# ```

# Tổng:

# ```
# O(N log T)
# ```

# Với:

# ```
# T ≈ 10^14
# logT ≈ 50
# ```

# → chạy rất nhanh.

# ---

# ✅ **Insight quan trọng của bài**

# 3 bước tư duy:

# 1️⃣ Nhận ra **time là monotonic → dùng Binary Search**
# 2️⃣ Tính **k bằng công thức sqrt thay vì loop**
# 3️⃣ Cộng k của tất cả worker

# ---

# Nếu bạn muốn, mình có thể giải thích thêm **1 insight rất quan trọng của bài này (rất nhiều người không nhận ra)**:

# 👉 Bài này **thực chất là bài merge k sorted sequences** và có thể giải bằng **Priority Queue giống bài K-th smallest element** (một cách khác ngoài Binary Search).


# # import java.util.*;

# # public class b215 {
# #     static Scanner sc = new Scanner(System.in);

# #     public static void main(String[] args) {
# #         // nhập chiều cao núi
# #         int mountainHeight = sc.nextInt();

# #         // nhập số worker
# #         int n = sc.nextInt();

# #         int[] workerTimes = new int[n];

# #         // nhập thời gian của từng worker
# #         for (int i = 0; i < n; i++) {
# #             workerTimes[i] = sc.nextInt();
# #         }

# #         long result = minNumberOfSeconds(mountainHeight, workerTimes);

# #         // in kết quả
# #         System.out.println(result);

# #     }
    
# #     // Hàm tìm thời gian nhỏ nhất để phá hết núi
# #     public static long minNumberOfSeconds(int mountainHeight, int[] workerTimes) {

# #         // tìm worker có thời gian lớn nhất
# #         int max = 0;
# #         for (int x : workerTimes)
# #             max = Math.max(max, x);

# #         // ước lượng số lần mỗi worker phải làm
# #         int h = (mountainHeight - 1) / workerTimes.length + 1;

# #         // left = thời gian nhỏ nhất có thể
# #         long left = 1;

# #         // right = thời gian lớn nhất có thể
# #         long right = (long) max * h * (h + 1) / 2;

# #         // Binary Search
# #         while (left <= right) {

# #             long mid = left + (right - left) / 2;

# #             // kiểm tra mid có đủ thời gian không
# #             if (check(mountainHeight, workerTimes, mid))
# #                 right = mid - 1; // thử giảm thời gian
# #             else
# #                 left = mid + 1; // cần nhiều thời gian hơn
# #         }

# #         return left;
# #     }

# #     // kiểm tra trong "time" giây có phá đủ núi không
# #     static boolean check(int mountainHeight, int[] workerTimes, long time) {

# #         for (int x : workerTimes) {

# #             // số lần worker có thể phá trong "time" giây
# #             int k = (int) (-1 + Math.sqrt(1 + 8 * time / x)) / 2;

# #             // giảm chiều cao núi
# #             mountainHeight -= k;

# #             // nếu phá hết núi
# #             if (mountainHeight <= 0)
# #                 return true;
# #         }

# #         return false;
# #     }

# # }
    

    


# # // ---

# # // #1. Ý tưởng thuật toán

# # // Bài toán yêu cầu:

# # // *Núi có chiều cao`mountainHeight`*Có`n`worker*Worker`i`mất thời gian:

# # // ```x,2 x,3 x,4 x...```

# # // để phá từng đơn vị chiều cao.

# # // Nếu worker làm`k`lần thì tổng thời gian là:

# # // [x(1+2+3+...+k)]

# # // [=x*\frac{k(k+1)}{2}]

# # // ---

# # // #2. Binary Search trên thời gian

# # // Ta không biết**bao nhiêu giây là đủ**,nên ta:

# # // ***Binary search trên thời gian T**

# # // Giả sử có`T`giây.

# # // Ta kiểm tra:

# # // ```T giây→các worker phá được tổng bao nhiêu height```

# # // Nếu:

# # // ```total>=mountainHeight```

# # // →thời gian**đủ**

# # // Nếu:

# # // ```total<mountainHeight```

# # // →thời gian**chưa đủ**

# # // ---

# # // #3. Tính số lần worker làm trong T giây

# # // Worker có time`x`

# # // Ta cần tìm`k`sao cho:

# # // [x*\frac{k(k+1)}{2}\le T]

# # // Chia hai vế cho`x`:

# # // [\frac{k(k+1)}{2}\le\frac{T}{x}]

# # // Nhân 2:

# # // [k(k+1)\le\frac{2 T}{x}]

# # // Giải phương trình bậc 2:

# # // [k^2+k-\frac{2 T}{x}\le 0]

# # // Nghiệm:

# # // [k=\frac{-1+\sqrt{1+8 T/x}}{2}]

# # // Đó chính là dòng code:

# # // ```java(int)(-1+Math.sqrt(1+8*time/x))/2```

# # // ---

# # // #4. Code hoàn chỉnh(có main+Scanner+chú thích)

# # // ```java

# # // import java.util.*;

# # // class Solution {

# # //     // Hàm tìm thời gian nhỏ nhất để phá hết núi
# # //     public long minNumberOfSeconds(int mountainHeight, int[] workerTimes) {

# # //         // tìm worker có thời gian lớn nhất
# # //         int max = 0;
# # //         for (int x : workerTimes)
# # //             max = Math.max(max, x);

# # //         // ước lượng số lần mỗi worker phải làm
# # //         int h = (mountainHeight - 1) / workerTimes.length + 1;

# # //         // left = thời gian nhỏ nhất có thể
# # //         long left = 1;

# # //         // right = thời gian lớn nhất có thể
# # //         long right = (long) max * h * (h + 1) / 2;

# # //         // Binary Search
# # //         while (left <= right) {

# # //             long mid = left + (right - left) / 2;

# # //             // kiểm tra mid có đủ thời gian không
# # //             if (check(mountainHeight, workerTimes, mid))
# # //                 right = mid - 1; // thử giảm thời gian
# # //             else
# # //                 left = mid + 1; // cần nhiều thời gian hơn
# # //         }

# # //         return left;
# # //     }

# # //     // kiểm tra trong "time" giây có phá đủ núi không
# # //     boolean check(int mountainHeight, int[] workerTimes, long time) {

# # //         for (int x : workerTimes) {

# # //             // số lần worker có thể phá trong "time" giây
# # //             int k = (int) (-1 + Math.sqrt(1 + 8 * time / x)) / 2;

# # //             // giảm chiều cao núi
# # //             mountainHeight -= k;

# # //             // nếu phá hết núi
# # //             if (mountainHeight <= 0)
# # //                 return true;
# # //         }

# # //         return false;
# # //     }

# # //     // ===== MAIN PROGRAM =====
# # //     public static void main(String[] args) {

# # //         Scanner sc = new Scanner(System.in);

# # //         // nhập chiều cao núi
# # //         int mountainHeight = sc.nextInt();

# # //         // nhập số worker
# # //         int n = sc.nextInt();

# # //         int[] workerTimes = new int[n];

# # //         // nhập thời gian của từng worker
# # //         for (int i = 0; i < n; i++) {
# # //             workerTimes[i] = sc.nextInt();
# # //         }

# # //         Solution sol = new Solution();

# # //         long result = sol.minNumberOfSeconds(mountainHeight, workerTimes);

# # //         // in kết quả
# # //         System.out.println(result);
# # //     }}```

# # //     ---

# # //     #5.

# # //     Ví dụ
# # //     chạy chương
# # //     trình

# # //     Input

# # //     ```4 2 2 1```

# # //     Ý nghĩa

# # //     ```mountainHeight=4 workerTimes=[2,1]```

# # //     Output

# # //     ```3```

# # //     ---

# # //     #6.
# # //     Độ phức
# # //     tạp

# # //     Binary search:

# # //     ```

# # // O(log T)
# # // ```

# # // Mỗi lần check:

# # // ```
# # // O(n)
# # // ```

# # // Tổng:

# # // ```
# # // O(n log T)
# # // ```

# # // Với:

# # // ```
# # // T ≈ 10^14
# # // logT ≈ 50
# # // ```

# # // → chạy rất nhanh.

# # // ---

# # // ✅ Nếu bạn muốn mình có thể giải thích thêm **2 điểm rất quan trọng của bài này**:

# # // 1️⃣ **Vì sao right = max * h * (h + 1) / 2**
# # // 2️⃣ **Vì sao công thức sqrt ra k (rất nhiều người không hiểu đoạn này)**
# # // 3️⃣ **Cách nghĩ ra Binary Search cho

# # //     bài này (rất hay ra trong Google/Meta interview)**.

# # // ---

# # // ## 1. Mô tả bài toán

# # // Bạn có:

# # // * Một **ngọn núi** có chiều cao ban đầu: `mountainHeight`.
# # // * Có `n` **công nhân**.
# # // * Mỗi công nhân có một giá trị trong mảng `workerTimes`.

# # // Ý nghĩa của `workerTimes[i]`:

# # // * Công nhân `i` **mất `workerTimes[i]` giây để giảm 1 đơn vị chiều cao của núi lần đầu**.
# # // * Nhưng **mỗi lần làm tiếp theo sẽ lâu hơn lần trước**.

# # // Cụ thể:

# # // Nếu `workerTimes[i] = t` thì:

# # // | Lần làm           | Thời gian cần |
# # // | ----------------- | ------------- |
# # // | giảm 1 đơn vị đầu | `t`           |
# # // | giảm đơn vị thứ 2 | `2t`          |
# # // | giảm đơn vị thứ 3 | `3t`          |
# # // | giảm đơn vị thứ 4 | `4t`          |

# # // Tức là **thời gian tăng dần theo cấp số cộng**.

# # // Tổng thời gian nếu worker làm `k` lần:

# # // [
# # // t + 2t + 3t + ... + kt
# # // ]

# # // [
# # // = t \times (1 + 2 + ... + k)
# # // ]

# # // [
# # // = t \times \frac{k(k+1)}{2}
# # // ]

# # // ---

# # // ## 2. Mục tiêu bài toán

# # // Bạn phải tìm:

# # // **Số giây nhỏ nhất để giảm chiều cao ngọn núi về 0.**

# # // Tức là:

# # // * Các worker **có thể làm song song**
# # // * Mỗi worker có thể giảm nhiều đơn vị chiều cao
# # // * Tổng số đơn vị giảm phải ≥ `mountainHeight`

# # // Bạn cần tìm **thời gian nhỏ nhất** sao cho điều này xảy ra.

# # // ---

# # // ## 3. Ví dụ minh họa

# # // Giả sử:

# # // ```
# # // mountainHeight = 4
# # // workerTimes = [2,1]
# # // ```

# # // Có 2 worker:

# # // * worker A: `t = 2`
# # // * worker B: `t = 1`

# # // ---

# # // ### Worker B (t = 1)

# # // | Lần | Thời gian | Tổng |
# # // | --- | --------- | ---- |
# # // | 1   | 1         | 1    |
# # // | 2   | 2         | 3    |
# # // | 3   | 3         | 6    |

# # // Nếu có **3 giây**:

# # // worker B có thể làm:

# # // ```
# # // 1 + 2 = 3
# # // ```

# # // → giảm **2 đơn vị**

# # // ---

# # // ### Worker A (t = 2)

# # // | Lần | Thời gian | Tổng |
# # // | --- | --------- | ---- |
# # // | 1   | 2         | 2    |
# # // | 2   | 4         | 6    |

# # // Nếu có **3 giây**

# # // → chỉ làm **1 lần**

# # // → giảm **1 đơn vị**

# # // ---

# # // ### Tổng

# # // ```
# # // worker A = 1
# # // worker B = 2
# # // ---------
# # // tổng = 3
# # // ```

# # // Nếu `mountainHeight = 3` thì **3 giây đủ**.

# # // ---

# # // ## 4. Ý tưởng chính của bài

# # // Bài này thường giải bằng:

# # // **Binary Search trên thời gian**

# # // Ta thử một thời gian `T`:

# # // 1. Với mỗi worker tính được **giảm được bao nhiêu height trong T giây**.
# # // 2. Cộng tất cả lại.
# # // 3. Nếu ≥ `mountainHeight` → thời gian này **đủ**.
# # // 4. Nếu < → **chưa đủ**.

# # // Sau đó tìm **T nhỏ nhất**.

# # // ---

# # // ## 5. Công thức quan trọng

# # // Nếu worker có `t` và làm `k` lần:

# # // [
# # // t \times \frac{k(k+1)}{2} \le T
# # // ]

# # // Từ đó tìm `k`.

# # // ---

# # // ✅ **Tóm tắt bài toán**

# # // * Núi cao `mountainHeight`
# # // * `n` worker
# # // * Worker i mất `t,2t,3t...`
# # // * Worker làm **song song**
# # // * Tìm **thời gian nhỏ nhất để tổng số lần giảm ≥ mountainHeight**

# # // ---

# # // Nếu bạn muốn, tôi có thể giải thêm:

# # // * **Cách tư duy ra Binary Search cho bài này**
# # // * **Cách tính k từ công thức (quan trọng)**
# # // * **Code Java/Python tối ưu O(n log M)**
# # // * **Minh họa trực quan dễ hiểu hơn**.


# # // Phần này khá **quan trọng trong Binary Search**: ta phải chọn một **giới hạn trên (right)** chắc chắn **đủ lớn để phá hết núi**.

# # // Ta sẽ phân tích từng bước.

# # // ---

# # // # 1. Ý tưởng của `right`

# # // ```java
# # // long right = (long) max * h * (h + 1) / 2;
# # // ```

# # // Trong đó:

# # // * `max` = worker **chậm nhất**
# # // * `h` = số lần worker đó phải làm

# # // Tức là:

# # // > **Trường hợp xấu nhất: chỉ có worker chậm nhất làm việc**

# # // Nếu thời gian đủ cho worker này **một mình phá hết núi**, thì chắc chắn **các worker khác cùng làm sẽ nhanh hơn**.

# # // Vì vậy đây là **upper bound an toàn**.

# # // ---

# # // # 2. Tại sao cần biến `h`

# # // ```java
# # // int h = (mountainHeight - 1) / workerTimes.length + 1;
# # // ```

# # // Công thức này tương đương:

# # // [
# # // h = \lceil \frac{mountainHeight}{n} \rceil
# # // ]

# # // Trong đó:

# # // ```
# # // n = số worker
# # // ```

# # // Ý nghĩa:

# # // > Giả sử các worker **chia đều công việc**

# # // Ví dụ:

# # // ```
# # // mountainHeight = 10
# # // workers = 3
# # // ```

# # // Thì:

# # // ```
# # // 10 / 3 = 3.33
# # // → ceil = 4
# # // ```

# # // Tức là **mỗi worker nhiều nhất phá 4 lần**.

# # // ---

# # // # 3. Thời gian để worker phá `h` lần

# # // Worker có time `t`

# # // Các lần làm:

# # // ```
# # // t
# # // 2t
# # // 3t
# # // ...
# # // ht
# # // ```

# # // Tổng thời gian:

# # // [
# # // t(1+2+3+...+h)
# # // ]

# # // Tổng cấp số cộng:

# # // [
# # // 1+2+...+h = \frac{h(h+1)}{2}
# # // ]

# # // Do đó:

# # // [
# # // time = t * \frac{h(h+1)}{2}
# # // ]

# # // ---

# # // # 4. Vì sao dùng `max`

# # // Ta chọn:

# # // ```
# # // t = max(workerTimes)
# # // ```

# # // Tức là **worker chậm nhất**.

# # // Vì vậy:

# # // [
# # // right = max * \frac{h(h+1)}{2}
# # // ]

# # // Đây là **thời gian để worker chậm nhất phá h lần**.

# # // ---

# # // # 5. Ví dụ trực quan

# # // Giả sử:

# # // ```
# # // mountainHeight = 10
# # // workerTimes = [1,2,5]
# # // ```

# # // Ta có:

# # // ```
# # // n = 3
# # // ```

# # // ### Tính h

# # // ```
# # // h = ceil(10 / 3)
# # // h = 4
# # // ```

# # // ---

# # // ### Worker chậm nhất

# # // ```
# # // max = 5
# # // ```

# # // ---

# # // ### Tính right

# # // [
# # // right = 5 * (4 * 5 / 2)
# # // ]

# # // [
# # // = 5 * 10
# # // ]

# # // [
# # // = 50
# # // ]

# # // ---

# # // Ý nghĩa:

# # // > Trong **50 giây**, chỉ cần worker chậm nhất cũng có thể phá **4 đơn vị**.

# # // Nhưng vì có **3 worker**, tổng phá được **≥ 10** chắc chắn.

# # // Vì vậy:

# # // ```
# # // 50 giây chắc chắn đủ
# # // ```

# # // Binary search sẽ tìm **nhỏ hơn 50**.

# # // ---

# # // # 6. Vì sao không chọn right cực lớn?

# # // Ví dụ:

# # // ```
# # // right = 10^18
# # // ```

# # // Binary search vẫn chạy nhưng:

# # // ```
# # // log(10^18) ≈ 60
# # // ```

# # // Nhưng chọn `right` nhỏ hơn sẽ:

# # // * **tăng tốc**
# # // * **tránh overflow**

# # // ---

# # // # 7. Tóm tắt trực quan

# # // `right` được chọn theo logic:

# # // ```
# # // Trường hợp xấu nhất:
# # // - công việc chia đều
# # // - worker chậm nhất làm
# # // ```

# # // Do đó:

# # // ```
# # // h = ceil(mountainHeight / n)
# # // right = max * h * (h + 1) / 2
# # // ```

# # // ---

# # // ✅ **Tư duy phỏng vấn quan trọng**

# # // Khi làm **Binary Search Answer** luôn cần:

# # // ```
# # // left = chắc chắn sai
# # // right = chắc chắn đúng
# # // ```

# # // Ở đây:

# # // ```
# # // left = 1
# # // right = thời gian chắc chắn phá được núi
# # // ```

# # // ---

# # // Nếu bạn muốn, mình có thể giải thích thêm **2 insight rất hay của bài này** (thường hỏi trong FAANG):

# # // 1️⃣ **Vì sao công thức sqrt tìm k đúng**
# # // 2️⃣ **Tại sao Binary Search là cách nghĩ tự nhiên của bài này**
# # // 3️⃣ **Cách giải

# # // O(n log n) nhanh hơn 2 lần so với cách này**.
# # // Phần **sqrt trong code** xuất phát từ việc **giải bất phương trình bậc 2**. Ta đi từng bước để thấy vì sao ra công thức:

# # // ```java
# # // k = (int)(-1 + Math.sqrt(1 + 8 * time / x)) / 2;
# # // ```

# # // ---

# # // # 1. Tổng thời gian worker làm k lần

# # // Worker có thời gian cơ bản `x`.

# # // Các lần làm:

# # // ```
# # // 1 lần  →  x
# # // 2 lần  →  2x
# # // 3 lần  →  3x
# # // ...
# # // k lần  →  kx
# # // ```

# # // Tổng thời gian:

# # // [
# # // x(1 + 2 + 3 + ... + k)
# # // ]

# # // Ta có công thức tổng:

# # // [
# # // 1 + 2 + ... + k = \frac{k(k+1)}{2}
# # // ]

# # // Do đó:

# # // [
# # // time_needed = x * \frac{k(k+1)}{2}
# # // ]

# # // ---

# # // # 2. Điều kiện trong bài

# # // Ta có tổng thời gian cho worker là `time`.

# # // Worker làm được `k` lần nếu:

# # // [
# # // x * \frac{k(k+1)}{2} \le time
# # // ]

# # // ---

# # // # 3. Đưa về dạng dễ giải

# # // Chia hai vế cho `x`:

# # // [
# # // \frac{k(k+1)}{2} \le \frac{time}{x}
# # // ]

# # // Nhân 2:

# # // [
# # // k(k+1) \le \frac{2time}{x}
# # // ]

# # // Khai triển:

# # // [
# # // k^2 + k \le \frac{2time}{x}
# # // ]

# # // Chuyển vế:

# # // [
# # // k^2 + k - \frac{2time}{x} \le 0
# # // ]

# # // ---

# # // # 4. Đây là phương trình bậc 2

# # // [
# # // k^2 + k - C = 0
# # // ]

# # // Trong đó

# # // [
# # // C = \frac{2time}{x}
# # // ]

# # // Áp dụng công thức nghiệm:

# # // [
# # // k = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
# # // ]

# # // Ở đây:

# # // ```
# # // a = 1
# # // b = 1
# # // c = -C
# # // ```

# # // ---

# # // # 5. Thay vào công thức

# # // [
# # // k = \frac{-1 \pm \sqrt{1^2 - 4(1)(-C)}}{2}
# # // ]

# # // [
# # // k = \frac{-1 \pm \sqrt{1 + 4C}}{2}
# # // ]

# # // Nhớ rằng

# # // [
# # // C = \frac{2time}{x}
# # // ]

# # // nên

# # // [
# # // 4C = \frac{8time}{x}
# # // ]

# # // Do đó:

# # // [
# # // k = \frac{-1 + \sqrt{1 + \frac{8time}{x}}}{2}
# # // ]

# # // Ta chỉ lấy nghiệm **dương**.

# # // ---

# # // # 6. Chính là dòng code

# # // ```java
# # // (int)(-1 + Math.sqrt(1 + 8 * time / x)) / 2
# # // ```

# # // Ý nghĩa:

# # // ```
# # // sqrt(...) → giải phương trình bậc 2
# # // → tìm k lớn nhất thỏa điều kiện
# # // ```

# # // ---

# # // # 7. Ví dụ cụ thể

# # // Giả sử

# # // ```
# # // x = 2
# # // time = 20
# # // ```

# # // Ta tính:

# # // [
# # // k = \frac{-1 + \sqrt{1 + 8*20/2}}{2}
# # // ]

# # // [
# # // = \frac{-1 + \sqrt{1 + 80}}{2}
# # // ]

# # // [
# # // = \frac{-1 + 9}{2}
# # // ]

# # // [
# # // = 4
# # // ]

# # // Kiểm tra:

# # // ```
# # // 1*2 = 2
# # // 2*2 = 4
# # // 3*2 = 6
# # // 4*2 = 8
# # // ```

# # // Tổng:

# # // ```
# # // 2 + 4 + 6 + 8 = 20
# # // ```

# # // Đúng bằng `time`.

# # // ---

# # // # 8. Ý nghĩa trực giác

# # // Công thức sqrt giúp ta:

# # // ```
# # // Từ time → tính trực tiếp số lần worker làm được
# # // ```

# # // Nếu không có công thức này, ta phải:

# # // ```
# # // while(time >= nextWork)
# # // ```

# # // → sẽ **chậm O(k)**.

# # // Còn sqrt:

# # // ```
# # // O(1)
# # // ```

# # // Nên toàn bộ thuật toán trở thành:

# # // ```

# # // O(n log T)
# # // ```

# # // ---

# # // ✅ **Insight quan trọng của bài**

# # // Dạng tổng:

# # // [
# # // 1+2+3+...+k
# # // ]

# # // xuất hiện rất nhiều trong thuật toán:

# # // * LeetCode mining problems
# # // * scheduling problems
# # // * triangular numbers

# # // Chỉ cần nhớ:

# # // [
# # // k \approx \sqrt{2T}
# # // ]

# # // ---

# # // Nếu bạn muốn, mình có thể giải thích thêm **một insight rất hay mà nhiều người không thấy**:

# # // 👉 Vì sao bài này **thực chất là bài "K-th smallest element in multiple sorted lists"** và có thể giải bằng **priority queue** giống bài **merge k sorted arrays**.
