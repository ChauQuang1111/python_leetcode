# // 3397. Maximum Number of Distinct Elements After Operations(18/10/2025)
from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        # Nếu tổng số phần tử <= (2*k + 1), ta có thể chọn sao cho tất cả đều khác nhau
        if len(nums) <= (k * 2) + 1:
            return len(nums)
        
        # Sắp xếp mảng để duyệt tuần tự từ nhỏ đến lớn
        nums.sort()

        distinct = 0      # Biến đếm số phần tử phân biệt
        last = float('-inf')  # Giá trị gần nhất đã chọn (để đảm bảo không trùng lặp)

        # Duyệt từng phần tử trong mảng
        for num in nums:
            # Ta có thể chọn một giá trị m trong đoạn [num - k, num + k]
            # Nhưng m phải > last để khác giá trị trước đó
            m = max(last + 1, num - k)

            # Nếu giá trị m vẫn nằm trong khoảng hợp lệ [num - k, num + k]
            if m <= num + k:
                distinct += 1   # Đếm thêm 1 phần tử khác biệt
                last = m        # Cập nhật giá trị vừa chọn

        return distinct  # Trả về tổng số phần tử khác nhau có thể đạt được







# import java.util.*; // import thư viện cần thiết

# public class b71 {
#   static Scanner sc = new Scanner(System.in);

#   public static void main(String[] args) {
#     int n = sc.nextInt();

#     int[] nums = new int[n];

#     for (int i = 0; i < n; i++) {
#       nums[i] = sc.nextInt();
#     }
#     int k = sc.nextInt();

#     int result = maxDistinctElements(nums, k);

#     System.out.println("Số phần tử phân biệt tối đa: " + result);

#     sc.close();
#   }

#   public static int maxDistinctElements(int[] nums, int k) {
#     // Nếu tổng độ dài mảng nhỏ hơn hoặc bằng (2*k + 1)
#     // thì có thể làm cho tất cả phần tử trở nên khác nhau
#     if (nums.length <= (k << 1) + 1)
#       return nums.length;

#     // Sắp xếp mảng tăng dần để duyệt theo thứ tự
#     Arrays.sort(nums);

#     int distinct = 0; // Biến đếm số lượng phần tử phân biệt
#     int l = Integer.MIN_VALUE; // Lưu giá trị đã chọn gần nhất (để tránh trùng)

#     // Duyệt qua từng phần tử trong mảng
#     for (int i = 0; i < nums.length; i++) {
#       // Tính giá trị nhỏ nhất có thể chọn:
#       // - nums[i] - k: giới hạn dưới
#       // - l + 1: đảm bảo lớn hơn giá trị trước đó
#       int m = Math.max(l + 1, nums[i] - k);

#       // Nếu giá trị m vẫn nằm trong khoảng hợp lệ [nums[i] - k, nums[i] + k]
#       if (m <= nums[i] + k) {
#         distinct++; // Đếm thêm 1 giá trị khác biệt
#         l = m; // Cập nhật giá trị gần nhất đã chọn
#       }
#     }

#     return distinct; // Trả về kết quả cuối cùng
#   }

# }

# // Để mình giải thích bài **** thật rõ ràng nhé — từ đề bài, ý tưởng cho tới
# // cách giải, để bạn nắm vững.

# // ---

# // ## 📝 Đề bài tóm tắt

# // Cho một mảng số nguyên `nums` và một số nguyên `k`.
# // Bạn có thể thực hiện với mỗi phần tử **tối đa một lần** phép toán:

# // > * “+” hoặc “−” một số bất kỳ từ `0` cho tới `k` (hay thức là: cộng bất kỳ
# // giá trị trong khoảng `[−k, k]`) cho phần tử đó.
# // > Ví dụ: nếu phần tử là `5` và `k = 3`, bạn có thể biến phần tử này thành
# // xuống `2` (5−3), hoặc lên `8` (5+3), hoặc bất kỳ giá trị từ `2 → 8`.

# // Sau khi bạn thực hiện các phép tại nhiều phần tử tùy ý (ở mỗi phần tử chỉ làm
# // tối đa 1 lần, hoặc có thể không làm) → mảng sẽ trở thành một mảng mới.
# // Yêu cầu: **trả về số phần “phần tử riêng biệt” (distinct elements) lớn nhất**
# // bạn có thể đạt được bằng cách thực hiện các phép này.

# // Ví dụ: nếu `nums = [1,2,3]`, `k = 1` thì

# // * `1` có thể thành `[0..2]`
# // * `2` có thể thành `[1..3]`
# // * `3` có thể thành `[2..4]`
# // Bạn có thể chọn, chẳng hạn: `1 → 0`, `2 → 1`, `3 → 2` → thành `[0,1,2]` → 3
# // phần tử khác nhau.
# // Vậy kết quả = 3.

# // ---

# // ## 💡 Ý tưởng giải quyết

# // Mục tiêu là: **tạo càng nhiều phần tử khác nhau càng tốt**.
# // Ta có mỗi phần tử ban đầu `x`, nó có thể trở thành bất kỳ giá trị trong
# // khoảng `[x − k, x + k]`.
# // Vậy phần tử đó ta “giành” một giá trị trong khoảng đó mà **không trùng với
# // các giá trị đã dùng trước đó** càng tốt.

# // ### Chiến lược:

# // 1. Sắp xếp `nums` tăng dần. Vì nếu xử lý phần tử từ nhỏ tới lớn thì dễ “đặt”
# // giá trị nhỏ cho phần tử nhỏ trước, giúp phần tử lớn sau còn “không gian” để
# // chọn giá trị riêng biệt.
# // 2. Duyệt từng phần tử `x` theo thứ tự đã sắp:

# // * Khoảng khả dụng: `[x−k, x+k]`
# // * Ta đã dùng một giá trị lớn nhất trước đó gọi là `prev_assigned`
# // * Muốn tránh trùng, thì phần tử mới phải chọn một giá trị > `prev_assigned`.
# // → Giá trị tốt nhất để chọn là:

# // ```
# // cur = max(x − k, prev_assigned + 1)
# // cur = min(cur, x + k)
# // ```

# // Nếu `cur > prev_assigned` thì mình có thể “dùng” được một giá trị mới cho `x`
# // → tăng số distinct lên 1 → cập nhật `prev_assigned = cur`.

# // Nhờ vậy, ta lần lượt “đặt” mỗi phần tử vào một giá trị riêng biệt nếu có thể.
# // Nếu phần tử không thể chọn giá trị > `prev_assigned`, thì phần tử đó không
# // góp tăng số distinct.

# // ---

# // ## ⚙️ Cách chạy – ví dụ cụ thể

# // Ví dụ: `nums = [4,4,7,9]`, `k = 2`.

# // * Sắp: `[4,4,7,9]`
# // * `prev_assigned = -∞`, `ans = 0`.

# // * `x=4` → khả dụng `[2..6]`. `cur = max(2, -∞+1)=2` → ≤6 → đặt `cur=2` →
# // `ans=1`, `prev_assigned=2`.
# // * `x=4` (thứ hai) → khả dụng `[2..6]`. `cur = max(2, 2+1)=3` → ≤6 → đặt
# // `cur=3` → `ans=2`, `prev_assigned=3`.
# // * `x=7` → `[5..9]`. `cur = max(5,3+1)=5` → ≤9 → đặt `cur=5` → `ans=3`,
# // `prev_assigned=5`.
# // * `x=9` → `[7..11]`. `cur = max(7,5+1)=7` → ≤11 → đặt `cur=7` → `ans=4`,
# // `prev_assigned=7`.

# // → Kết quả = 4 distinct. Như bài viết mô tả. ([AlgoMonster][1])

# // ---

# // ## ✅ Nhận xét về độ phức tạp

# // * Sắp xếp: `O(n log n)`
# // * Duyệt một lần: `O(n)`
# // * Tổng: `O(n log n)`
# // * Bộ nhớ thêm chủ yếu cho sort và biến tạm → `O(n)` hoặc `O(1)` ngoài đầu
# // vào.

# // ---

# // Nếu bạn muốn, mình có thể **viết lại phiên bản Java có chú thích** cho bài
# // này – hoặc nếu bạn đã có code và cần tôi **giải thích chi tiết code**, mình
# // cũng có nhé. Bạn muốn dạng nào?

# // [1]: https://algo.monster/liteproblems/3397?utm_source=chatgpt.com "3397.
# // Maximum Number of Distinct Elements After Operations"
# // Rất hay 👏 — bạn đã viết đúng **thuật toán tối ưu O(n log n)** cho bài
# // **LeetCode 3397 – Maximum Number of Distinct Elements After Operations**.
# // Giờ mình sẽ **giải thích từng dòng và toàn bộ tư duy thuật toán** để bạn hiểu
# // sâu 👇

# // ---

# // ## 🧩 Đề bài tóm tắt

# // Bạn có mảng `nums` và số `k`.
# // Với mỗi phần tử `nums[i]`, bạn **được phép cộng hoặc trừ bất kỳ giá trị nào
# // trong khoảng [-k, k]**
# // → tức là `nums[i]` có thể biến thành **bất kỳ số nào trong đoạn [nums[i] - k,
# // nums[i] + k]**.

# // 👉 Mục tiêu: **Chọn giá trị cho từng phần tử sao cho số lượng giá trị phân
# // biệt (distinct) là lớn nhất.**

# // ---

# // ## 🧠 Ý tưởng chính

# // Ta cần **chọn 1 giá trị cụ thể** cho từng `nums[i]` trong khoảng `[nums[i]-k,
# // nums[i]+k]`

# // * sao cho **không trùng với các giá trị trước đó**,
# // * và **có thể chọn được nhiều giá trị riêng biệt nhất**.

# // Cách làm hiệu quả:

# // 1. **Sắp xếp mảng** để xử lý từ nhỏ đến lớn.
# // 2. Giữ biến `l` = giá trị đã chọn gần nhất.
# // 3. Với mỗi phần tử `x`, ta chọn **giá trị nhỏ nhất có thể** sao cho:

# // * lớn hơn `l` (để khác với phần tử trước),
# // * và vẫn nằm trong khoảng hợp lệ `[x - k, x + k]`.

# // ---

# // ## 🔍 Giải thích từng dòng code

# // ```java
# // if (nums.length <= (k << 1) + 1) return nums.length;
# // ```

# // * `(k << 1)` = `2 * k`.
# // * Nếu toàn bộ mảng nhỏ hơn hoặc bằng `(2*k + 1)` phần tử,
# // thì ta **có thể chọn tất cả đều khác nhau**,
# // vì chỉ cần dịch mỗi phần tử đi 1 chút là được.

# // → **Trả luôn `nums.length`** vì tất cả đều có thể distinct.

# // ---

# // ```java
# // Arrays.sort(nums);
# // ```

# // * Sắp xếp tăng dần để duyệt các phần tử theo thứ tự, giúp đảm bảo chọn được
# // giá trị nhỏ nhất có thể mà không bị trùng.

# // ---

# // ```java
# // int distinct = 0;
# // int l = Integer.MIN_VALUE;
# // ```

# // * `distinct`: đếm số lượng giá trị riêng biệt đã chọn.
# // * `l`: lưu **giá trị đã chọn gần nhất**, để đảm bảo phần tử hiện tại chọn giá
# // trị **lớn hơn l**.

# // ---

# // ```java
# // for (int i = 0; i < nums.length; i++) {
# // int m = Math.max(l + 1, nums[i] - k);
# // ```

# // * Tính giá trị nhỏ nhất có thể chọn cho `nums[i]`:

# // * `nums[i] - k`: giới hạn dưới.
# // * `l + 1`: để lớn hơn giá trị trước đó (tránh trùng).
# // → Lấy **max** giữa 2 cái để đảm bảo hợp lệ và không trùng.

# // ---

# // ```java
# // if (m <= nums[i] + k) {
# // distinct++;
# // l = m;
# // }
# // ```

# // * Nếu giá trị `m` vẫn nằm trong khoảng hợp lệ `[nums[i] - k, nums[i] + k]`,
# // thì ta **chọn nó làm giá trị đại diện cho phần tử này**.
# // * Cập nhật `l = m` để làm mốc cho phần tử tiếp theo.
# // * Tăng `distinct` vì ta đã chọn được thêm 1 giá trị khác biệt.

# // ---

# // ```java
# // return distinct;
# // ```

# // * Sau khi duyệt hết mảng, ta trả về số lượng phần tử phân biệt tối đa.

# // ---

# // ## 🧮 Ví dụ minh họa

# // **Input:**

# // ```
# // nums = [4, 4, 7, 9], k = 2
# // ```

# // **Quá trình:**

# // | i | nums[i] | [x−k, x+k] | l (trước) | m = max(l+1, x−k) | có hợp lệ? | l
# // (mới) | distinct |
# // | - | ------- | ---------- | --------- | ----------------- | ---------- |
# // ------- | -------- |
# // | 0 | 4 | [2,6] | -∞ | 2 | ✅ | 2 | 1 |
# // | 1 | 4 | [2,6] | 2 | 3 | ✅ | 3 | 2 |
# // | 2 | 7 | [5,9] | 3 | 5 | ✅ | 5 | 3 |
# // | 3 | 9 | [7,11] | 5 | 7 | ✅ | 7 | 4 |

# // **Output:** `4`

# // ---

# // ## ⚙️ Độ phức tạp

# // * `sort`: O(n log n)
# // * `loop`: O(n)
# // → **Tổng:** O(n log n)
# // * **Không dùng thêm bộ nhớ phụ đáng kể (O(1)).**

# // ---

# // ## ✅ Tóm tắt tư duy:

# // * **Sắp xếp** → **chọn nhỏ nhất hợp lệ** → **tránh trùng**
# // * Greedy chọn giá trị càng nhỏ càng tốt để giữ chỗ cho phần tử sau.
# // * Đảm bảo tối đa số lượng distinct.

# // ---

# // Bạn có muốn mình minh họa thuật toán này bằng **đồ họa ASCII (một dòng
# // timeline các đoạn [x−k, x+k])** để dễ hình dung cách greedy chọn giá trị
# // không?

## 🧩 Đề bài tóm tắt

# Bạn có một mảng `nums`, và mỗi phần tử `nums[i]` có thể **tăng hoặc giảm** trong phạm vi `k`.
# Nói cách khác, ta có thể biến `nums[i]` thành **bất kỳ giá trị nào trong đoạn `[nums[i] - k, nums[i] + k]`**.

# 👉 Mục tiêu:
# Sau khi thực hiện những thay đổi này, bạn muốn **có càng nhiều phần tử phân biệt (distinct)** càng tốt.

# ---

## 🚀 Ý tưởng chính — *Greedy (tham lam)*

# Ta muốn **chọn các giá trị khác nhau nhiều nhất có thể**, nhưng mỗi giá trị phải nằm trong giới hạn thay đổi cho phép của từng phần tử.

# Cách đơn giản nhất là:

# 1. **Sắp xếp mảng `nums` tăng dần**
#    → Như vậy ta duyệt các giá trị từ nhỏ đến lớn, dễ chọn các giá trị khác nhau mà không bỏ lỡ cơ hội.

# 2. **Duyệt từng phần tử**
#    → Với mỗi phần tử `num`, ta có thể chọn giá trị `m` sao cho:

#    * `m` nằm trong `[num - k, num + k]` (giới hạn thay đổi được)
#    * `m > last` (phải lớn hơn giá trị đã chọn trước để không bị trùng)

#    → Khi đó, `m = max(last + 1, num - k)`

#    * `num - k` là giá trị nhỏ nhất có thể chọn
#    * `last + 1` là giá trị nhỏ nhất để khác phần tử trước
#      → Lấy giá trị lớn hơn trong hai cái này để vừa hợp lệ, vừa không trùng.

# 3. **Nếu `m` nằm trong khoảng cho phép `[num - k, num + k]`**
#    → Ta có thể chọn nó, tăng `distinct++`, và cập nhật `last = m`.

# ---

## 🔍 Ví dụ minh họa

# Giả sử:

# ```
# nums = [4, 4, 7, 9], k = 2
# ```

# ### Bước 1: Sắp xếp

# ```
# [4, 4, 7, 9]
# ```

# ### Bước 2: Duyệt từng phần tử

# | i | nums[i] | Khoảng [nums[i]-k, nums[i]+k] | last | m = max(last+1, nums[i]-k) | Có hợp lệ không? | Chọn m | distinct |
# | - | ------- | ----------------------------- | ---- | -------------------------- | ---------------- | ------ | -------- |
# | 0 | 4       | [2..6]                        | -∞   | 2                          | ✅                | 2      | 1        |
# | 1 | 4       | [2..6]                        | 2    | 3                          | ✅                | 3      | 2        |
# | 2 | 7       | [5..9]                        | 3    | 5                          | ✅                | 5      | 3        |
# | 3 | 9       | [7..11]                       | 5    | 6                          | ✅                | 6      | 4        |

# ✅ Tất cả chọn được → `distinct = 4`

# ---

# ## 🧠 Độ phức tạp

# * **Thời gian:** `O(n log n)` do cần sắp xếp.
# * **Bộ nhớ:** `O(1)` chỉ dùng vài biến phụ.

# ---

# ## 🏁 Kết luận

# Thuật toán này **tham lam (greedy)** vì:

# * Mỗi bước đều chọn **giá trị nhỏ nhất có thể** mà vẫn hợp lệ.
# * Điều đó giúp **tối đa hóa không gian** cho các phần tử phía sau → tạo được **nhiều giá trị khác nhau nhất**.

# ---

# Bạn có muốn mình vẽ **minh họa bằng hình (timeline)** cho ví dụ `[4, 4, 7, 9], k=2` để trực quan hơn không?
# Rất hay — bạn đã viết lại đúng thuật toán chuẩn cho bài **3397. Maximum Number of Distinct Elements After Operations** 🎯
# Dưới đây là **phần giải thích chi tiết từng bước** để bạn hiểu rõ toàn bộ logic:

# ---

# ## 🧩 Mục tiêu đề bài

# Bạn có một mảng số nguyên `nums` và một số `k`.

# 👉 Mỗi phần tử `nums[i]` **có thể được thay đổi** (tăng hoặc giảm) **trong phạm vi ±k**, tức là:
# [
# nums[i] \rightarrow bất\ kỳ\ giá\ trị\ nào\ trong\ [nums[i] - k, , nums[i] + k]
# ]

# Mục tiêu:

# > Làm sao để sau khi thay đổi, ta có **nhiều phần tử phân biệt nhất có thể** (distinct values).

# ---

## 💡 Ý tưởng cốt lõi (Greedy – tham lam)

# Ta cần sắp xếp sao cho:

# * Mỗi phần tử chọn được **một giá trị hợp lệ** (trong khoảng cho phép)
# * Mà **không trùng** với giá trị đã chọn của phần tử trước đó.

# => Ta duyệt từ nhỏ đến lớn, và **chọn giá trị nhỏ nhất có thể** mà vẫn lớn hơn phần tử trước.

# ---

# ## 🔍 Giải thích từng dòng code

# ### 🧱 Khởi tạo

# ```python
# if len(nums) <= (k * 2) + 1:
#     return len(nums)
# ```

# * Nếu tổng số phần tử nhỏ hơn hoặc bằng `(2k + 1)` → mỗi phần tử có thể chọn một giá trị khác nhau, vì khoảng thay đổi đủ rộng để tạo `len(nums)` giá trị khác nhau.

# → Trả về `len(nums)` luôn là tối đa.

# ---

# ### 🪄 Bước sắp xếp

# ```python
# nums.sort()
# ```

# * Giúp ta duyệt từ **giá trị nhỏ đến lớn**
# * Đảm bảo khi chọn giá trị cho phần tử sau, ta **không quay lại thay đổi phần tử trước**.

# ---

### 🔢 Vòng lặp chính

# ```python
# distinct = 0
# last = float('-inf')
# ```

# * `distinct`: Đếm số phần tử phân biệt đã chọn.
# * `last`: Lưu giá trị cuối cùng đã chọn → giúp đảm bảo phần tử tiếp theo không trùng.

# ---

### ⚙️ Chọn giá trị cho từng phần tử

# ```python
# for num in nums:
#     m = max(last + 1, num - k)
# ```

# 👉 `num - k`: Giá trị nhỏ nhất ta có thể chọn cho phần tử này.
# 👉 `last + 1`: Giá trị nhỏ nhất để **khác phần tử trước**.

# ⇒ Lấy `max(...)` để đảm bảo **cả hai điều kiện đều thỏa mãn**:

# * Nằm trong khoảng hợp lệ.
# * Không trùng với phần tử trước.

# ---

# ### ✅ Kiểm tra hợp lệ

# ```python
# if m <= num + k:
#     distinct += 1
#     last = m
# # ```

# * Nếu giá trị `m` vẫn còn nằm trong khoảng `[num - k, num + k]`, nghĩa là ta **có thể chọn được m**.
# * Tăng `distinct` vì vừa chọn thêm được một giá trị khác biệt.
# * Cập nhật `last = m` để so sánh cho phần tử sau.

# ---

# ## 📈 Ví dụ minh họa

# ### Input:

# ```python
# nums = [4, 4, 7, 9]
# k = 2
# ```

# ### Bước 1: Sắp xếp

# `[4, 4, 7, 9]`

# ### Bước 2: Duyệt từng phần tử

# | num | last | num-k | num+k | m = max(last+1, num-k) | m ≤ num+k ? | distinct | last |
# | --- | ---- | ----- | ----- | ---------------------- | ----------- | -------- | ---- |
# | 4   | -∞   | 2     | 6     | 2                      | ✅           | 1        | 2    |
# | 4   | 2    | 2     | 6     | 3                      | ✅           | 2        | 3    |
# | 7   | 3    | 5     | 9     | 5                      | ✅           | 3        | 5    |
# | 9   | 5    | 7     | 11    | 6                      | ✅           | 4        | 6    |

# ✅ Kết quả: `distinct = 4`

# ---

# ## 🧮 Độ phức tạp

# * **Thời gian:** `O(n log n)` — do sắp xếp mảng.
# * **Bộ nhớ:** `O(1)` — chỉ dùng vài biến phụ.

# ---

# ## ✅ Kết luận

# Thuật toán hoạt động theo chiến lược:

# > “Chọn giá trị nhỏ nhất có thể mà không trùng với giá trị trước.”

# Cách này **đảm bảo tối đa số phần tử khác nhau**, vì mỗi phần tử sau có **nhiều không gian hơn** để chọn giá trị hợp lệ.

# ---

# Bạn có muốn mình minh họa **bằng biểu đồ khoảng [num−k, num+k] trên trục số** để dễ hình dung hơn không?
