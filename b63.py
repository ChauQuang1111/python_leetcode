# //  3186 — Maximum Total Damage With Spell (11/10/2025)
# Rất hay 👏 — bạn đang dùng **Dynamic Programming (DP)** theo cách khác, thông minh hơn vì tận dụng `Counter` để nhóm các phép giống nhau.
# Giờ mình sẽ **giải thích chi tiết thuật toán + chú thích từng dòng code** nhé 👇

# ---

# ```python
from typing import List
from collections import Counter

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # Đếm số lần xuất hiện của mỗi loại phép (vì có thể có nhiều phép cùng power)
        counts = Counter(power)

        # Lấy danh sách các giá trị power duy nhất, sắp xếp tăng dần,
        # và thêm 3 phần tử 0 ở đầu để tránh lỗi truy cập chỉ số âm trong DP
        keys = [0, 0, 0] + sorted(list(counts.keys()))
        n = len(keys)

        # dp[i] = tổng sát thương tối đa có thể đạt được xét đến phép có giá trị keys[i]
        dp = [0] * n

        # Duyệt từ phần tử thứ 3 trở đi (vì 3 phần tử đầu là 0)
        for i in range(3, n):
            # Tổng sát thương nếu chọn tất cả phép có giá trị keys[i]
            curr = counts[keys[i]] * keys[i]

            # Nếu cách xa hơn 2 đơn vị so với trước đó → không xung đột
            if keys[i] - keys[i-1] > 2:
                dp[i] = dp[i-1] + curr

            # Nếu cách 2 với keys[i-2] → chỉ cần so sánh dp[i-1] (không chọn) và dp[i-2] + curr (chọn)
            elif keys[i] - keys[i-2] > 2:
                dp[i] = max(dp[i-1], dp[i-2] + curr)

            # Ngược lại (các giá trị quá gần nhau, chỉ có thể lùi 3 bước)
            else:
                dp[i] = max(dp[i-1], dp[i-3] + curr)

        # Trả về kết quả lớn nhất
        return dp[-1]


## 🧠 Giải thích ý tưởng

# Bài toán:

# > Mỗi phép có giá trị `power[i]`.
# > Nếu chọn một phép có sức mạnh `x`, ta **không thể chọn** các phép có giá trị `x-2, x-1, x+1, x+2`.

# Mục tiêu:

# > Tính **tổng sát thương lớn nhất** có thể đạt được.

# ---

# ## 💡 Ý tưởng DP

# * Gọi `dp[i]` là tổng sát thương tối đa **xét đến** giá trị phép `keys[i]`.
# * Ở mỗi bước, ta có hai lựa chọn:

#   1. **Không chọn** phép `keys[i]` → `dp[i] = dp[i-1]`
#   2. **Chọn** phép `keys[i]` → cộng thêm sát thương từ `keys[i]` và bỏ qua những giá trị quá gần nó (khoảng cách ≤ 2).

# ---

# ## 🧩 Ví dụ minh họa

# Giả sử:

# ```python
# power = [1, 2, 3, 6, 6, 8]
# ```

# ### Bước 1️⃣: Đếm số lượng

# ```
# counts = {1:1, 2:1, 3:1, 6:2, 8:1}
# keys = [0, 0, 0, 1, 2, 3, 6, 8]
# ```

# ### Bước 2️⃣: Tính DP

# |  i | keys[i] |   curr |                                  Cách tính | dp[i] |
# | -: | ------: | -----: | -----------------------------------------: | ----: |
# |  3 |       1 |  1×1=1 |                                    dp[2]+1 |     1 |
# |  4 |       2 |  1×2=2 | quá gần (1–2), dp[4]=max(dp[3], dp[1]+2)=2 |     2 |
# |  5 |       3 |  1×3=3 | quá gần (2–3), dp[5]=max(dp[4], dp[2]+3)=3 |     3 |
# |  6 |       6 | 2×6=12 |                  6–3>2 → dp[6]=dp[5]+12=15 |    15 |
# |  7 |       8 |  1×8=8 |                   8–6>2 → dp[7]=dp[6]+8=23 |    23 |

# ✅ **Kết quả:** `dp[-1] = 23`

# ---

# ## 🔍 Tóm tắt logic:

# * Dùng `Counter` để nhóm phép giống nhau → tiết kiệm thời gian.
# * Dùng `dp` để chọn phép sao cho **không chọn hai phép cách nhau ≤ 2 đơn vị**.
# * Dựa vào **khoảng cách giữa keys** mà lùi 1, 2, hoặc 3 bước để tính giá trị tốt nhất.

# ---

# Bạn có muốn mình thêm **phiên bản có in bảng dp từng bước (debug)** để bạn nhìn thấy rõ cách nó cập nhật không?























# import java.util.*;

# public class b64 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int n = sc.nextInt();
#         int[] power = new int[n];

#         for (int i = 0; i < n; i++) {
#             power[i] = sc.nextInt();
#         }

#         System.out.println(maximumTotalDamage(power));
#     }

#     public static long maximumTotalDamage(int[] power) {
#         // Sắp xếp mảng theo thứ tự tăng dần để xử lý dễ dàng hơn
#         Arrays.sort(power);

#         int n = power.length;
#         long[] dp = new long[n]; // dp[i] lưu tổng sát thương tối đa có thể đạt được đến vị trí i
#         long md = 0; // md (max damage) lưu giá trị dp lớn nhất mà không "va chạm" phạm vi 2 đơn vị
#         dp[0] = power[0]; // Cơ sở: chỉ có một phần tử đầu tiên thì tổng = power[0]

#         // Duyệt qua từng phần tử từ i = 1 đến n-1
#         for (int i = 1, j = 0; i < n; i++) {
#             if (power[i] == power[i - 1]) {
#                 // Nếu cùng giá trị power => có thể cộng dồn sát thương
#                 dp[i] = dp[i - 1] + power[i];
#             } else {
#                 // Dịch j sao cho power[j] + 2 < power[i]
#                 // Nghĩa là: tìm phần tử xa nhất không "gần kề" (cách nhau ít nhất 3)
#                 while (power[j] + 2 < power[i]) {
#                     md = Math.max(md, dp[j]);
#                     j++;
#                 }

#                 // Tổng sát thương tại i = giá trị lớn nhất trước đó (không trùng phạm vi) +
#                 // power[i]
#                 dp[i] = md + power[i];
#             }
#         }

#         // Trả về tổng sát thương lớn nhất có thể đạt được
#         long max = 0;
#         for (long val : dp) {
#             max = Math.max(max, val);
#         }
#         return max;
#     }
# }

# // Rất tuyệt 👏 — bạn đang xem một **phiên bản tối ưu và ngắn gọn hơn** của
# // thuật toán cho bài
# // 👉 **LeetCode 3186. Maximum Total Damage With Spell Casting**

# // Giờ mình sẽ **giải thích chi tiết từng dòng code và logic bên trong**, giúp
# // bạn hiểu **tại sao công thức này hoạt động**, không chỉ “nó chạy được” nhé 👇

# // ---

# // ## 🧠 1️⃣ Tóm tắt ý tưởng bài toán

# // Ta có mảng `power[]`, mỗi phần tử là sát thương của một phép thuật.

# // Nếu chọn phép có sát thương `x`,
# // bạn **không thể chọn** phép nào có sát thương nằm trong khoảng:

# // ```
# // [x - 2, x - 1, x + 1, x + 2]
# // ```

# // ➡️ Mục tiêu: chọn tập hợp phép sao cho **tổng sát thương lớn nhất**.

# // ---

# // ## 💡 2️⃣ Ý tưởng tổng quát của code

# // Thuật toán này thực hiện:

# // 1. **Sắp xếp mảng `power`**
# // 2. Dùng **DP (một chiều)** để ghi nhớ “tổng sát thương tốt nhất đến hiện
# // tại”.
# // 3. Biến `md` lưu **max damage** đạt được ở các phép **không xung đột** với
# // phép hiện tại.
# // 4. Duyệt `i` từ trái sang phải,

# // * Nếu phép hiện tại giống phép trước (`power[i] == power[i-1]`), cộng dồn
# // lại.
# // * Nếu khác, kiểm tra những phép **quá xa hơn 2 đơn vị** (`power[j] + 2 <
# // power[i]`),
# // nghĩa là phép tại `j` **không còn xung đột** với phép `i`, ta cập nhật `md =
# // max(md, dp[j])`.
# // * Sau đó `dp[i] = md + power[i]` (cộng phép hiện tại vào tổng sát thương tốt
# // nhất trước đó).

# // ---

# // ## 🧩 3️⃣ Giải thích từng phần chi tiết

# // ```java
# // Arrays.sort(power);
# // ```

# // 👉 Sắp xếp các phép theo sát thương tăng dần để dễ so sánh “khoảng cách ≤ 2”.

# // ---

# // ```java
# // long[] dp = new long[power.length];
# // long md = 0;
# // dp[0] = power[0];
# // ```

# // 👉

# // * `dp[i]`: tổng sát thương tối đa nếu bạn chọn phép tại vị trí `i`.
# // * `md`: "max damage" của các phép **đã xử lý mà không xung đột** với phép
# // hiện tại.
# // * `dp[0] = power[0]`: phép đầu tiên, chỉ có thể lấy chính nó.

# // ---

# // ### 🔁 Vòng lặp chính:

# // ```java
# // for (int i = 1, j = 0; i < power.length; i++) {
# // ```

# // `i`: phép hiện tại
# // `j`: phép cũ nhất chưa loại khỏi phạm vi cấm (điều kiện cách > 2)

# // ---

# // #### 📍 Trường hợp 1 — phép trùng nhau

# // ```java
# // if (power[i] == power[i-1]) {
# // dp[i] = dp[i-1] + power[i];
# // }
# // ```

# // 👉 Nếu hai phép có **sát thương bằng nhau**, bạn có thể cộng dồn sát thương
# // vì chúng không “xung đột” (giống nhau không bị cấm).

# // **Ví dụ:**
# // `[6, 6, 6]` → có thể cộng tất cả:
# // `dp = [6, 12, 18]`

# // ---

# // #### 📍 Trường hợp 2 — phép mới khác

# // ```java
# // else {
# // while (power[j] + 2 < power[i]) {
# // md = Math.max(md, dp[j]);
# // j++;
# // }
# // dp[i] = md + power[i];
# // }
# // ```

# // Giải thích chi tiết 👇

# // * `while (power[j] + 2 < power[i])`:
# // Khi phép `j` **cách xa hơn 2 đơn vị** so với phép hiện tại,
# // thì phép `j` **an toàn** (không bị xung đột).
# // → Cập nhật `md = max(md, dp[j])`.

# // * Sau khi cập nhật xong,
# // `dp[i] = md + power[i]`
# // Nghĩa là tổng sát thương tối đa khi chọn phép hiện tại =
# // “tổng sát thương tốt nhất không xung đột trước đó” + “sát thương phép này”.

# // ---

# // ### ✅ Sau vòng lặp

# // ```java
# // long max = 0;
# // for (long n : dp) {
# // max = Math.max(max, n);
# // }
# // return max;
# // ```

# // 👉 Tìm tổng sát thương lớn nhất trong `dp` — đây là kết quả cuối cùng.

# // ---

# // ## 📘 4️⃣ Ví dụ minh họa cụ thể

# // ```
# // Input: power = [1, 1, 3, 4]
# // ```

# // Sau khi sắp xếp:

# // ```
# // power = [1, 1, 3, 4]
# // ```

# // | i | power[i] | dp[i] | j | md | Giải thích |
# // | - | -------- | ----- | --- | -- |
# // -------------------------------------------------------- |
# // | 0 | 1 | 1 | 0 | 0 | Bắt đầu |
# // | 1 | 1 | 2 | 0 | 0 | Cộng dồn vì trùng |
# // | 2 | 3 | 3 | 0→1 | 2 | 1 và 3 cách 2, nên md=dp[1]=2 |
# // | 3 | 4 | 6 | 0→2 | 3 | 4 cách 1 với 3, nhưng 1 cách 3 hơn 2 → md=3,
# // dp[3]=3+3=6 |

# // → **Kết quả = 6**

# // ---

# // ## ⏱️ Độ phức tạp

# // | Loại | Mức độ |
# // | --------- | --------------------------------------- |
# // | Thời gian | O(n) (vì `i` và `j` chỉ tăng một chiều) |
# // | Bộ nhớ | O(n) |

# // ---

# // ## 🔍 Tóm tắt logic cốt lõi

# // | Thành phần | Ý nghĩa |
# // | ------------------------------- |
# // ---------------------------------------------------- |
# // | `dp[i]` | Tổng sát thương tối đa khi chọn phép tại i |
# // | `md` | Max damage của phép không xung đột |
# // | `while (power[j]+2 < power[i])` | Loại bỏ phép không ảnh hưởng nữa |
# // | `dp[i] = md + power[i]` | Chọn phép hiện tại + kết quả tối ưu an toàn trước
# // đó |
# // | `dp[i] = dp[i-1] + power[i]` | Nếu phép trùng nhau, cộng dồn luôn |

# // ---

# // Nếu bạn muốn, mình có thể **vẽ sơ đồ dòng thời gian `i, j` di chuyển** cho ví
# // dụ `[1, 1, 3, 4, 6, 6]`, giúp bạn thấy rõ cách `md` cập nhật — nhìn hình là
# // hiểu 100%.
# // Bạn có muốn mình vẽ minh họa đó không?

# // ---

# // ## 📝 Đề bài (phiên bản tiếng Việt)

# // * Cho mảng `power`, trong đó mỗi phần tử là sát thương (damage) của một phép
# // thuật mà bạn có thể thi triển (có thể có phép trùng sát thương).
# // * Khi bạn thi triển một phép có sát thương `x = power[i]`, bạn **không thể**
# // thi triển bất kỳ phép thuật có sát thương trong khoảng:

# // ```
# // x - 2, x - 1, x + 1, x + 2
# // ```

# // tức là 2 giá trị sát thương bên cạnh đều bị “khóa”.
# // * Mỗi phép chỉ thi triển được **một lần**.
# // * Yêu cầu: **lấy tổng sát thương tối đa** mà bạn có thể đạt được bằng cách
# // chọn một tập các phép thỏa mãn ràng buộc trên.

# // Ví dụ:

# // * `power = [1, 1, 3, 4]` → output = 6
# // Giải thích: bạn có thể chọn hai phép có sát thương 1 (tổng = 2) và phép có
# // sát thương 4 (tổng = 4), cộng lại = 6.
# // * `power = [7, 1, 6, 6]` → output = 13
# // Giải: chọn phép 1 + hai phép 6 = 1 + 6 + 6 = 13.

# // Đề bài gốc: nếu chọn phép sát thương `x`, bạn **không được chọn** phép có sát
# // thương `x ± 1` hoặc `x ± 2`. ([Leetcode][1])

# // ---

# // ## 💡 Ý tưởng & phân tích

# // Đây là bài toán kiểu **quy hoạch động + chọn/không chọn** với ràng buộc “cách
# // nhau ±1 hoặc ±2 không được chọn”.

# // Một cách để hiểu là:

# // * Ta có nhiều giá trị `x` có thể xuất hiện nhiều lần (có phép thuật trùng sát
# // thương).
# // * Nếu bạn quyết định “lấy” các phép có sát thương `x`, thì bạn không thể lấy
# // các phép có sát thương `x-2, x-1, x+1, x+2`.

# // Điều này gợi nhớ bài toán House Robber (với khoảng cách 1) hoặc “delete and
# // earn” (LeetCode) — nhưng ở đây ràng buộc “cách 2 bước” (±2) thay vì ±1.

# // **Cách tiếp cận phổ biến**:

# // 1. **Đếm tần suất** từng giá trị sát thương `x` — gọi `cnt[x] = số lần xuất
# // hiện` của `x`.

# // 2. **Sắp xếp** các giá trị sát thương **độc nhất** (unique) theo thứ tự tăng
# // dần. Gọi mảng `vals` là danh sách các giá trị sát thương duy nhất, đã sắp
# // xếp.

# // 3. **Xây dựng mảng tiếp theo (next index)**:
# // Với mỗi giá trị `vals[i]`, nếu bạn “lấy” nó, bạn phải nhảy đến chỉ số `j` sao
# // cho `vals[j] > vals[i] + 2`.
# // Dùng binary search để tìm `j = first index trong vals có giá trị > vals[i] +
# // 2`.

# // 4. **DP / memoization** hoặc **DP dưới dạng bảng**:

# // Định nghĩa `dp[i]` là “tổng sát thương tối đa nếu bạn xem xét từ vị trí `i`
# // (giá trị `vals[i]`) trở đi”.

# // Khi ở `i`, bạn có hai lựa chọn:

# // * **Bỏ (skip)** giá trị `vals[i]` → sang `i + 1`, tức `dp[i+1]`
# // * **Lấy (take)** tất cả các phép có sát thương `vals[i]` → thêm `vals[i] *
# // cnt[vals[i]]` + `dp[j]`, với `j = nextIndex[i]`

# // => `dp[i] = max( skip, take )`

# // 5. Kết quả là `dp[0]`.

# // Độ phức tạp: sắp xếp `O(n log n)`, xây `nextIndex` với binary search mỗi phần
# // tử, và DP là `O(n)`. ([Leetcode][1])

# // ---

# // ## 📂 Sơ đồ & ví dụ cụ thể

# // Giả sử:

# // ```
# // power = [1, 1, 3, 4]
# // ```

# // * Đếm: `cnt[1] = 2`, `cnt[3] = 1`, `cnt[4] = 1`
# // * Giá trị duy nhất đã sắp xếp: `vals = [1, 3, 4]`
# // * Tính nextIndex:

# // * Với `vals[0] = 1`, tìm giá trị > 3 → `vals[1] = 3`, `vals[2] = 4` → first >
# // 3 là `vals[2]` (index = 2)
# // * Với `vals[1] = 3`, tìm > 5 → không có → nextIndex = len
# // * Với `vals[2] = 4`, tìm > 6 → không có → nextIndex = len

# // Vậy next = `[2, 3, 3]` (nếu len = 3).

# // DP từ phải sang trái:

# // * `i = 2` (value 4):
# // take = `4 * cnt[4] + dp[next[2]] = 4 * 1 + dp[3] = 4 + 0 = 4`
# // skip = `dp[3] = 0`
# // → `dp[2] = 4`

# // * `i = 1` (value 3):
# // take = `3 * cnt[3] + dp[next[1]] = 3 * 1 + 0 = 3`
# // skip = `dp[2] = 4`
# // → `dp[1] = max(3, 4) = 4`

# // * `i = 0` (value 1):
# // take = `1 * cnt[1] + dp[next[0]] = 1 * 2 + dp[2] = 2 + 4 = 6`
# // skip = `dp[1] = 4`
# // → `dp[0] = max(6, 4) = 6`

# // Kết quả = `6`.

# // ---

# // Nếu bạn muốn, mình có thể viết **code Python + Java** với chú thích cho đề
# // này và giải thích từng dòng. Bạn muốn mình gửi code đó không?

# // [1]:
# // https://leetcode.ca/2024-06-25-3186-Maximum-Total-Damage-With-Spell-Casting/?utm_source=chatgpt.com
# // "3186 - Maximum Total Damage With Spell Casting - leetcode.ca"
