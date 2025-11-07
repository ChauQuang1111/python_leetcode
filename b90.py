
# // 2528. Maximize the Minimum Powered City(07/11/2025)
# Rất hay — đây là **phiên bản Python rút gọn và tối ưu** của bài **2528. Maximize the Minimum Powered City**, sử dụng **difference array (mảng sai khác)** để xử lý hiệu quả việc cộng trừ trong vùng ảnh hưởng.
# Dưới đây là phần **giải thích chi tiết thuật toán + code có chú thích từng dòng** 👇

# ---

# ## 🔍 Ý tưởng bài toán

# Bạn có `n` thành phố nằm dọc theo một đường thẳng, trong đó:

# * `stations[i]` là **số trạm điện tại thành phố i**.
# * Mỗi trạm điện có thể **phát điện đến các thành phố trong phạm vi r** (khoảng cách ≤ r).
# * Bạn được phép **xây thêm tối đa k trạm điện** (ở bất kỳ đâu).
# * Mục tiêu: **tăng sao cho công suất tối thiểu của mọi thành phố là lớn nhất có thể**.

# ---

# ## ⚙️ Tư duy thuật toán

# 1. **Dùng Binary Search** để tìm giá trị `mid = công suất tối thiểu` có thể đạt.

#    * Nếu có thể phân bổ ≤ `k` trạm để mọi thành phố có công suất ≥ `mid` → tăng `mid`.
#    * Ngược lại → giảm `mid`.

# 2. **Dùng Difference Array (mảng sai khác)** để cập nhật hiệu ứng "bán kính r" nhanh chóng:

#    * Khi thêm trạm vào vị trí `i`, nó ảnh hưởng đến đoạn `[i - r, i + r]`.
#    * Với `diff[l] += x` và `diff[r+1] -= x`, ta cộng nhanh `x` cho cả đoạn `[l, r]`.

# ---

# ## 🧠 Giải thích chi tiết code

# ```python
from typing import List
from itertools import accumulate

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)

        # ✅ df là mảng sai khác lưu ảnh hưởng điện năng
        df = [0] * (n + 5)
        for i, j in enumerate(stations):
            # Trạm j tại vị trí i ảnh hưởng đến đoạn [i - r, i + r]
            df[max(0, i - r)] += j
            df[min(n - 1, i + r) + 1] -= j

        # ✅ Tính công suất hiện tại từng thành phố (tổng cộng dồn của df)
        lo = min(accumulate(df[:n]))  # công suất nhỏ nhất hiện tại
        hi = 2 * 10 ** 10            # giới hạn trên cho binary search

        # 🔹 Hàm kiểm tra xem có thể đạt mức công suất tối thiểu "mid" hay không
        def check(mid):
            diff = df[:]   # copy lại mảng sai khác ban đầu
            cur, cnt = 0, 0  # cur: công suất hiện tại; cnt: số trạm đã thêm

            for i in range(n):
                cur += diff[i]  # cập nhật công suất tại thành phố i
                if cur < mid:   # nếu chưa đủ điện → cần thêm trạm
                    need = mid - cur
                    cnt += need
                    if cnt > k:  # vượt quá số trạm cho phép → thất bại
                        return False
                    # thêm trạm vào để tăng điện cho vùng ảnh hưởng [i, i + 2r]
                    diff[min(n - 1, i + 2 * r) + 1] -= need
                    cur = mid  # cập nhật lại công suất tại vị trí i
            return True  # đạt được yêu cầu với ≤ k trạm

        # ✅ Binary search tìm giá trị lớn nhất có thể đạt
        while lo < hi:
            mid = (lo + hi + 1) >> 1  # dịch phải chia 2 (nhanh hơn //2)
            if check(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo  # ✅ kết quả cuối cùng


# ## 🧮 Ví dụ minh họa

# ### Input:

# ```
# stations = [1, 2, 4, 5, 0]
# r = 1
# k = 2
# ```

# ### Diễn giải:

# * Ban đầu, công suất của 5 thành phố:

#   ```
#   Thành phố 0: 1+2 = 3
#   Thành phố 1: 1+2+4 = 7
#   Thành phố 2: 2+4+5 = 11
#   Thành phố 3: 4+5+0 = 9
#   Thành phố 4: 5+0 = 5
#   ```

#   → min = 3

# * Sau khi thêm 2 trạm (`k=2`) ở các vị trí hợp lý nhất,
#   công suất tối thiểu có thể nâng lên tới **7**.

### Output:

# ```
# 7
# ```

# ---

# ## 💡 Tóm tắt ưu điểm của thuật toán

# | Bước           | Kỹ thuật sử dụng                           | Mục đích                          |
# | -------------- | ------------------------------------------ | --------------------------------- |
# | 1              | Prefix Sum / Difference Array              | Cập nhật vùng ảnh hưởng nhanh     |
# | 2              | Binary Search                              | Tìm giá trị lớn nhất có thể đạt   |
# | 3              | Kiểm tra khả năng đạt (check)              | Duyệt O(n), mỗi lần thêm ≤ k trạm |
# | ⚙️ Độ phức tạp | O(n log M) — M là khoảng giá trị công suất |                                   |

# ---

# Bạn có muốn mình **thêm phần in log minh họa từng vòng lặp trong hàm `check(mid)`** để thấy rõ cách `cur` và `diff[]` thay đổi không?

# // Dưới đây là phần **giải thích đề bài** 2528. Maximize the Minimum Powered City (LeetCode) — gồm: mô tả, yêu cầu, và ý tưởng giải bài. Nếu bạn muốn, mình có thể tiếp tục với **bản tổng quan thuật toán** và **ví dụ bước-thực thi**.
# import java.util.*;

# public class b91 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int n = sc.nextInt();

#         // Nhập mảng stations
#         int[] stations = new int[n];
#         for (int i = 0; i < n; i++) {
#             stations[i] = sc.nextInt();
#         }

#         // Nhập bán kính ảnh hưởng r và số trạm có thể thêm k

#         int r = sc.nextInt();

#         int k = sc.nextInt();

#         long result = maxPower(stations, r, k);

#         // Xuất kết quả
#         System.out.println(result);
#     }

#     public static int len, r;

#     // 👉 Hàm chính giải bài toán
#     public static long maxPower(int[] stations, int r, int k) {
#         b91.len = stations.length;
#         b91.r = r;

#         // prefixSum[i] = tổng trạm điện từ 0 → i-1
#         long[] prefixSum = new long[len + 1];
#         long[] powers = new long[len];

#         // ✅ B1: Tính prefix sum
#         for (int i = 0; i < len; ++i) {
#             prefixSum[i + 1] = prefixSum[i] + stations[i];
#         }

#         // ✅ B2: Tính công suất (power) ban đầu của mỗi thành phố
#         for (int i = 0; i < len; ++i) {
#             int left = Math.max(0, i - r); // biên trái vùng ảnh hưởng
#             int right = Math.min(len - 1, i + r); // biên phải vùng ảnh hưởng
#             powers[i] = prefixSum[right + 1] - prefixSum[left];
#         }

#         // ✅ B3: Binary Search để tìm giá trị nhỏ nhất lớn nhất (maximize minimum)
#         long start = 0L, end = prefixSum[len] + k; // end = tổng trạm hiện có + trạm có thể thêm
#         while (start < end - 1) {
#             long mid = start + (end - start) / 2;
#             if (isReachable(mid, k, powers))
#                 start = mid; // có thể đạt được → thử cao hơn
#             else
#                 end = mid - 1; // không thể → giảm xuống
#         }

#         // ✅ Trả về kết quả cuối cùng
#         return isReachable(end, k, powers) ? end : start;
#     }

#     // 👉 Hàm kiểm tra có thể đạt mức điện tối thiểu "required" không
#     public static boolean isReachable(long required, int extra, long[] powers) {
#         long[] diff = new long[len + 1]; // mảng hiệu ứng (difference array)
#         long powerDiff = 0L; // ảnh hưởng tích lũy tại mỗi vị trí

#         for (int i = 0; i < len; ++i) {
#             powerDiff += diff[i]; // cập nhật ảnh hưởng từ các trạm trước đó
#             long needed = required - (powers[i] + powerDiff);

#             // Nếu thành phố này chưa đủ điện, cần thêm trạm
#             if (needed > 0) {
#                 extra -= needed; // trừ số trạm được phép thêm
#                 if (extra < 0)
#                     return false; // hết trạm → thất bại

#                 powerDiff += needed; // thêm trạm mới tại vùng này

#                 // ảnh hưởng kết thúc tại vị trí i + 2r + 1
#                 if (i + 2 * r + 1 < len)
#                     diff[i + 2 * r + 1] -= needed;
#             }
#         }
#         return true;
#     }

# }

# // ---

# // ## 📄 Mô tả đề bài

# // * Cho mảng `stations` độ dài `n`, trong đó `stations[i]` là số lượng trạm
# // phát điện (power stations) tại thành phố `i`. ([Leetcode][1])
# // * Một trạm phát điện đặt ở thành phố `i` có thể cung cấp điện cho mọi thành
# // phố `j` thỏa mãn `|i-j| ≤ r` (với `r` là bán kính vùng phủ). ([Leetcode][1])
# // * Độ “power” của một thành phố `j` được định nghĩa là **tổng số trạm phát
# // điện** đang cung cấp điện cho `j`.
# // * Chính phủ có quyền **xây thêm `k` trạm phát điện** (có thể đặt ở bất kỳ
# // thành phố nào, có cùng bán kính `r`) để **tối ưu** sao cho **giá trị tối
# // thiểu** của “power” trên tất cả các thành phố được **lớn nhất có thể**.
# // ([Leetcode][1])
# // * Trả về giá trị lớn nhất khả thi mà tất cả các thành phố đều có power **ít
# // nhất** bằng giá trị đó.

# // ---

# // ## ✅ Yêu cầu

# // * Tìm giá trị `X` sao cho sau khi tối ưu đặt thêm `k` trạm, mỗi thành phố có
# // power ≥ `X`, và `X` là lớn nhất có thể.
# // * Kích thước: `n ≤ 10^5`, `stations[i] ≤ 10^5`, `k ≤ 10^9`… ([Leetcode][1])
# // * Vì `k` và `n` lớn nên cần tìm giải thuật tối ưu hơn O(n × k) hay
# // brute-force.

# // ---

# // ## 🧠 Ý tưởng lớn

# // ### ○ Tính power ban đầu

# // * Trước tiên, ta tính **power ban đầu** của mỗi thành phố: mỗi trạm ở vị trí
# // `i` góp cho các thành phố từ `[i-r, i+r]`.
# // * Có thể sử dụng **difference array** hoặc prefix sum + sliding window để
# // tính nhanh O(n). ([AlgoMonster][2])

# // ### ○ Tìm giá trị tối thiểu khả thi bằng **binary search**

# // * Vì nếu ta có thể đạt được “tất cả thành phố có power ≥ X” thì **bất kỳ Y <
# // X** cũng khả thi — tính chất đơn điệu giúp dùng binary search.
# // ([AlgoMonster][2])
# // * Thiết lập `low = 0`, `high = (một số lớn)`, và tìm `mid`. Với mỗi `mid`,
# // kiểm tra xem có thể đảm bảo tất cả power ≥ `mid` với ≤ k trạm thêm hay không.

# // ### ○ Hàm kiểm tra (check/feasible) bằng cách **đặt thêm trạm một cách
# // greedy**

# // * Duyệt các thành phố từ trái sang phải.
# // * Dùng difference array để theo dõi việc đặt bổ sung trạm ảnh hưởng đến một
# // khoảng.
# // * Nếu tại thành phố `i`, tổng power hiện tại (ban đầu + bổ sung) < `mid`, thì
# // cần đặt thêm một số trạm để nâng tới `mid`.
# // * Đặt các trạm ở vị trí càng “điều trị” được phần bên phải càng tốt — tức vị
# // trí `min(i+r, n-1)` để tối đa hóa ảnh hưởng cho các thành phố sau đó.
# // ([AlgoMonster][2])
# // * Nếu tổng số trạm cần dùng > k → `mid` không khả thi. Ngược lại thì khả thi.

# // ### ○ Kết quả

# // * Sau khi binary search hoàn tất, ta tìm được giá trị lớn nhất `X` khả thi.

# // ---

# // Nếu bạn muốn, mình có thể gửi **ý tưởng code Python và Java** cùng **chú
# // thích từng bước** cho đề bài này để bạn tham khảo — bạn có muốn không?

# // Rất hay — bạn đang xem lời giải **chuẩn tối ưu của bài 2528. Maximize the
# // Minimum Powered City** bằng **Java**, viết cực gọn và hiệu quả.
# // Mình sẽ giúp bạn **giải thích chi tiết thuật toán từng bước + từng đoạn
# // code** 👇

# // ---

# // ## 🎯 Mục tiêu của bài toán

# // Bạn có:

# // * `stations[i]`: số lượng trạm điện ở thành phố `i`
# // * `r`: phạm vi phủ sóng của mỗi trạm điện
# // (một trạm ở vị trí `j` cung cấp điện cho các thành phố trong `[j - r, j +
# // r]`)
# // * `k`: số **trạm mới tối đa** bạn được phép thêm (có thể thêm vào bất kỳ
# // thành phố nào)

# // ➡️ Mục tiêu: **Tối đa hóa giá trị nhỏ nhất của “công suất điện” (total power)
# // trên toàn bộ các thành phố**
# // tức là làm cho *min(power[i])* lớn nhất có thể.

# // ---

# // ## 🧩 Ý tưởng thuật toán

# // Bài này giải bằng **Binary Search + Prefix Sum + Difference Array**.

# // ---

# // ### ⚙️ 1. Tính power ban đầu của mỗi thành phố

# // ```java
# // long[] prefixSum = new long[len + 1];
# // for (int i = 0; i < len; ++i) {
# // prefixSum[i + 1] = prefixSum[i] + stations[i];
# // }
# // for (int i = 0; i < len; ++i) {
# // int left = Math.max(0, i - r);
# // int right = Math.min(len - 1, i + r);
# // powers[i] = prefixSum[right + 1] - prefixSum[left];
# // }
# // ```

# // 🔹 Ở đây:

# // * `prefixSum[i]` = tổng trạm từ 0 → i-1
# // → giúp ta tính nhanh tổng số trạm trong đoạn `[left, right]`
# // * `powers[i]` = tổng số trạm ảnh hưởng đến thành phố `i`

# // 🧠 Ví dụ:

# // ```
# // stations = [1,2,4,5,0], r = 1
# // => powers = [3,7,11,9,5]
# // ```

# // (vì mỗi power[i] = tổng stations trong [i-1, i+1]).

# // ---

# // ### ⚙️ 2. Binary Search trên đáp án

# // ```java
# // long start = 0L, end = prefixSum[len] + k;
# // while (start < end - 1) {
# // long mid = start + (end - start) / 2;
# // if (isReachable(mid, k, powers)) start = mid;
# // else end = mid - 1;
# // }
# // return isReachable(end, k, powers) ? end : start;
# // ```

# // * Ta **giả sử** có thể làm cho mọi `power[i] >= mid`.
# // * Nếu có thể → ta thử giá trị cao hơn.
# // * Nếu không thể → giảm giá trị xuống.

# // 🧩 Phạm vi tìm kiếm `end = prefixSum[len] + k`
# // → tức là tổng tất cả trạm hiện có cộng với số trạm có thể thêm — mức tối đa
# // lý thuyết.

# // ---

# // ### ⚙️ 3. Hàm kiểm tra `isReachable(required, extra, powers)`

# // Đây là phần cốt lõi — kiểm tra liệu có thể đạt mức điện tối thiểu `required`
# // với tối đa `extra` trạm được thêm hay không.

# // ```java
# // long[] diff = new long[len + 1]; // mảng hiệu ứng trạm
# // long powerDiff = 0L; // ảnh hưởng tích lũy
# // ```

# // Ta dùng **difference array** để mô phỏng việc thêm trạm mới —
# // thêm 1 trạm ở vị trí `i` ảnh hưởng đến các thành phố từ `i - r` đến `i + r`.

# // ---

# // #### Vòng lặp chính:

# // ```java
# // for (int i = 0; i < len; ++i) {
# // powerDiff += diff[i]; // áp dụng hiệu ứng tích lũy
# // long needed = required - (powers[i] + powerDiff);
# // if (needed > 0) {
# // extra -= needed; // cần thêm 'needed' trạm để đạt mức yêu cầu
# // if (extra < 0) return false; // không đủ trạm -> thất bại
# // powerDiff += needed; // thêm trạm vào vùng hiện tại
# // if (i + 2 * r + 1 < len) diff[i + 2 * r + 1] -= needed; // hiệu ứng hết sau
# // 2r+1
# // }
# // }
# // return true;
# // ```

# // 📘 Giải thích:

# // * `powerDiff` = tổng ảnh hưởng từ các trạm mới đã thêm trước đó.
# // * Nếu `powers[i] + powerDiff < required`
# // → cần thêm `(required - currentPower)` trạm mới để nâng mức lên.

# // 🧮 Khi thêm trạm ở `i + r` (điểm xa nhất để tối đa hiệu quả):

# // * Ảnh hưởng kéo dài đến `i + 2r`.
# // * Vì vậy khi ra khỏi vùng `i + 2r + 1`, ta trừ lại bằng `diff`.

# // ---

# // ### 🔁 Quá trình hoạt động mẫu

# // Giả sử:

# // ```
# // stations = [1,2,4,5,0], r = 1, k = 2
# // ```

# // * powers ban đầu = [3,7,11,9,5]
# // * binary search thử mid = 7
# // → thành phố cuối chỉ có 5, cần thêm 2 trạm → đủ k → hợp lệ
# // → tăng mid lên.
# // * thử mid = 8
# // → cần thêm 3 trạm → quá k → không hợp lệ.
# // => kết quả: 7.

# // ---

# // ### 🧮 Độ phức tạp

# // | Phần | Thời gian |
# // | -------------------------------- | ------------------------------- |
# // | Tính prefix & powers | `O(n)` |
# // | Mỗi lần kiểm tra | `O(n)` |
# // | Binary search log(1e18) ≈ 60 lần | `O(60n)` ≈ `O(n)` trong thực tế |
# // | Bộ nhớ | `O(n)` |

# // ---

# // ### ✅ Tổng kết

# // Thuật toán:

# // 1. Dùng prefix sum để tính power nhanh.
# // 2. Binary search trên giá trị min power.
# // 3. Mỗi lần check dùng difference array để mô phỏng việc thêm trạm hiệu quả
# // nhất.

# // 💡 Cực kỳ tối ưu và là cách giải chính thức được đánh giá cao nhất (Runtime ~
# // O(n log M)).

# // ---

# // Nếu bạn muốn, mình có thể giúp bạn thêm **hàm `main()` dùng Scanner để nhập
# // input và chạy code này** (giống LeetCode nhưng chạy trên console) — bạn muốn
# // mình viết luôn không?
# # 