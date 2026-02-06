# # // Minimum Removals to Balance Array(06/02/2026)
# # // ### 🧠 Giải thích đề bài: **Minimum Removals to Balance Array**
# # // Ok 👍 bài **3634. Minimum Removals to Balance Array** (theo code bạn gửi) thực chất không phải “chẵn = lẻ” nữa, mà là dạng:
# Ok 👍 mình sẽ giải thích **thuật toán trong code Python bạn gửi** — nhưng quan trọng:

# > Code này **chưa đúng hoàn toàn** với bài 3634.
# > Nó là phiên bản **rút gọn sai logic sliding window**.

# Mình sẽ:

# 1. Giải thích code đang làm gì.
# 2. Chỉ ra lỗi sai.
# 3. Sửa lại đúng + giải thích chuẩn thuật toán.

# ---

# # 1️⃣ Code bạn gửi

# ```python
# class Solution:
#     def minRemoval(self, nums: List[int], k: int) -> int:
#         nums.sort()
#         l = 0
        
#         for r in range(len(nums)):
#             if nums[r] > nums[l] * k:
#                 l += 1
#         return l
# ```

# ---

# # 2️⃣ Ý tưởng bạn đang dùng

# Bạn cũng đang làm đúng hướng:

# * Sort mảng.
# * Dùng 2 con trỏ `l` và `r`.
# * Kiểm tra điều kiện balanced:

# ```
# nums[r] ≤ nums[l] * k
# ```

# Nếu vi phạm → tăng `l`.

# 👉 Đây là sliding window.

# ---

# # 3️⃣ Diễn giải từng dòng

# ### B1 — Sort

# ```python
# nums.sort()
# ```

# Để:

# * `nums[l]` = nhỏ nhất window
# * `nums[r]` = lớn nhất window

# ---

# ### B2 — Khởi tạo

# ```python
# l = 0
# ```

# Con trỏ trái window.

# ---

# ### B3 — Duyệt con trỏ phải

# ```python
# for r in range(len(nums)):
# ```

# Mở rộng window sang phải.

# ---

# ### B4 — Kiểm tra cân bằng

# ```python
# if nums[r] > nums[l] * k:
#     l += 1
# ```

# Nếu:

# ```
# max > min*k
# ```

# → Window không hợp lệ
# → Dịch `l` sang phải.

# ---

# # 4️⃣ Code đang hiểu sai chỗ nào?

# Bạn chỉ tăng `l` **1 lần**.

# Nhưng có trường hợp phải tăng **nhiều lần**.

# ---

# ## ❌ Ví dụ phản ví dụ

# ```
# nums = [1,2,3,100]
# k = 2
# ```

# Sorted: `[1,2,3,100]`

# ---

# ### r = 3

# ```
# nums[r] = 100
# nums[l] = 1
# ```

# Check:

# ```
# 100 > 1*2 → True
# ```

# Bạn tăng:

# ```
# l = 1
# ```

# Nhưng giờ:

# ```
# 100 > 2*2 = 4 → vẫn sai
# ```

# Phải tăng tiếp:

# ```
# l = 2
# 100 > 3*2 = 6 → vẫn sai
# l = 3 → mới đúng
# ```

# 👉 Nhưng code bạn **không while**, nên sai.

# ---

# # 5️⃣ Sai logic return

# Bạn return:

# ```python
# return l
# ```

# Nhưng:

# * `l` ≠ số phần tử xóa tối thiểu.
# * `l` chỉ là vị trí con trỏ cuối.

# Ta cần:

# ```
# n - maxLen
# ```

# ---

# # 6️⃣ Thuật toán đúng phải là

# ```python
from typing import List
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        maxLen = 0
        
        for r in range(len(nums)):
            
            # Thu hẹp window đến khi hợp lệ
            while nums[r] > nums[l] * k:
                l += 1
            
            # Cập nhật dãy dài nhất giữ lại
            maxLen = max(maxLen, r - l + 1)
        
        return len(nums) - maxLen
# ```

# ---

# # 7️⃣ Ý nghĩa thuật toán (chuẩn)

# ### Bản chất bài toán

# Không phải tìm “xóa gì” mà là:

# > Tìm dãy con dài nhất thỏa
# > `max ≤ min*k`

# ---

# ### Sliding window hoạt động

# Window `[l … r]` luôn:

# * Hợp lệ.
# * Có độ dài lớn nhất có thể tại mỗi `r`.

# ---

# ### Khi vi phạm

# ```
# nums[r] > nums[l]*k
# ```

# → Phải tăng `l` cho đến khi hợp lệ.

# ---

# 8️⃣ Minh họa nhanh

# ```
# nums = [1,2,4,8]
# k = 2
# ```

# Window dài nhất:

# * [1,2] → len 2
# * [2,4] → len 2
# * [4,8] → len 2

# → maxLen = 2
# → Xóa = 4 − 2 = 2

# ---

# # 9️⃣ So sánh code

# | Code              | Đúng? | Lý do              |
# | ----------------- | ----- | ------------------ |
# | `if`              | ❌     | Chỉ tăng l 1 lần   |
# | `while`           | ✅     | Thu hẹp đủ         |
# | return `l`        | ❌     | Không phải kết quả |
# | return `n-maxLen` | ✅     | Min removals       |

# ---

# # 🔟 Tóm tắt dễ nhớ

# * Sort mảng.
# * Dùng sliding window.
# * Giữ window thỏa:

#   ```
#   max ≤ min*k
#   ```
# * Tìm window dài nhất.
# * Xóa = phần còn lại.

# ---

# Nếu bạn muốn mình:

# * Vẽ hình chuyển động l/r.
# * So sánh với Two Sum / Longest Subarray.
# * Cho bài luyện tương tự.

# Cứ nói mình biết 👍

# import java.util.*;   

# public class b171{
#      static Scanner sc = new Scanner(System.in);
#    public static void main(String[] args) {
#      int n = sc.nextInt();
#         int[] nums = new int[n];

#         // Nhập các phần tử
#         System.out.println("Nhap cac phan tu:");
#         for (int i = 0; i < n; i++) {
#             nums[i] = sc.nextInt();
#         }

     
#         int k = sc.nextInt();

        
#         // Gọi hàm và in kết quả
#         int result = minRemoval(nums, k);

#         System.out.println( result);

#         sc.close();
#     }
#  // Hàm chính giải bài toán
#     public static  int minRemoval(int[] nums, int k) {

#         // B1: Sắp xếp mảng tăng dần
#         Arrays.sort(nums);

#         int i = 0;          // Con trỏ trái của sliding window
#         int maxLen = 0;    // Độ dài dãy con hợp lệ dài nhất

#         // j là con trỏ phải
#         for (int j = 0; j < nums.length; j++) {

#             // Nếu phần tử lớn nhất > nhỏ nhất * k → không cân bằng
#             while ((long) nums[j] > (long) nums[i] * k) {
#                 i++;   // Thu hẹp window từ bên trái
#             }

#             // Cập nhật độ dài window hợp lệ lớn nhất
#             maxLen = Math.max(maxLen, j - i + 1);
#         }

#         // Số phần tử cần xóa = tổng - giữ lại dài nhất
#         return nums.length - maxLen;
#     }


# }


# // ---

# // ## 📌 Ý nghĩa đề (theo thuật toán trong code)

# // Cho mảng `nums` và số nguyên `k`.

# // Một mảng được gọi là **balanced** nếu:

# // ```
# // max(nums_subarray) ≤ min(nums_subarray) * k
# // ```

# // Tức là:

# // > Phần tử lớn nhất không được lớn hơn k lần phần tử nhỏ nhất.

# // Bạn được phép **xóa phần tử bất kỳ**.

# // 👉 Mục tiêu:
# // Xóa ít nhất phần tử để mảng còn lại thỏa điều kiện trên.

# // ---

# // ## 🧠 Ý tưởng chính

# // Thay vì nghĩ “xóa gì”, ta nghĩ ngược lại:

# // > Tìm **dãy con dài nhất** thỏa điều kiện balanced.

# // Vì:

# // ```
# // Min removals = n - độ dài dãy giữ lại dài nhất
# // ```

# // ---

# // ## 🔧 Bước 1 — Sort mảng

# // ```java
# // Arrays.sort(nums);
# // ```

# // Tại sao cần sort?

# // Vì khi sort:

# // * `nums[i]` = nhỏ nhất trong window
# // * `nums[j]` = lớn nhất trong window

# // Ta chỉ cần check:

# // ```
# // nums[j] ≤ nums[i] * k
# // ```

# // ---

# // ## 🔁 Bước 2 — Sliding Window (2 con trỏ)

# // ```java
# // int i = 0;
# // for (int j = 0; j < nums.length; j++)
# // ```

# // * `i` = đầu window
# // * `j` = cuối window

# // Window = đoạn `[i … j]` đang xét.

# // ---

# // ## ⚠️ Điều kiện phá vỡ cân bằng

# // ```java
# // while (nums[j] > nums[i] * k) {
# //     i++;
# // }
# // ```

# // Nếu:

# // ```
# // max > min * k
# // ```

# // → Window không hợp lệ
# // → Phải **dịch i sang phải** để tăng min.

# // ---

# // ## 📊 Minh họa ví dụ

# // ```
# // nums = [1, 2, 4, 8]
# // k = 2
# // ```

# // Sau sort vẫn vậy.

# // ---

# // ### j = 0

# // Window: [1]

# // ```
# // 1 ≤ 1*2 → OK
# // len = 1
# // ```

# // ---

# // ### j = 1

# // Window: [1,2]

# // ```
# // 2 ≤ 1*2 → OK
# // len = 2
# // ```

# // ---

# // ### j = 2

# // Window: [1,2,4]

# // ```
# // 4 ≤ 1*2 = 2 ❌
# // ```

# // Phải tăng i:

# // * i = 1 → min = 2

# // Check lại:

# // ```
# // 4 ≤ 2*2 = 4 → OK
# // ```

# // Window mới: [2,4]
# // len = 2

# // ---

# // ### j = 3

# // Window: [2,4,8]

# // ```
# // 8 ≤ 2*2 = 4 ❌
# // ```

# // Tăng i:

# // * i = 2 → min = 4

# // ```
# // 8 ≤ 4*2 = 8 → OK
# // ```

# // Window: [4,8]
# // len = 2

# // ---

# // ## 🧮 Cập nhật độ dài lớn nhất

# // ```java
# // maxLen = Math.max(maxLen, j - i + 1);
# // ```

# // Giữ window dài nhất hợp lệ.

# // ---

# // ## 📤 Kết quả cuối

# // ```java
# // return nums.length - maxLen;
# // ```

# // Vì:

# // * `maxLen` = số phần tử giữ lại nhiều nhất
# // * Xóa ít nhất = tổng − giữ lại

# // ---

# // ## 🔍 Phân tích độ phức tạp

# // * Sort: `O(n log n)`
# // * Sliding window: `O(n)`
# // * Tổng: `O(n log n)`

# // Không có vòng lặp lồng nhau thực sự vì `i` chỉ tăng.

# // ---

# // ## 🧠 Insight quan trọng

# // 1. Balanced phụ thuộc **min và max**.
# // 2. Sort → window tự đảm bảo min ở trái, max ở phải.
# // 3. Khi vi phạm → chỉ cần tăng `i`.
# // 4. Bản chất: **Longest Valid Subarray**.

# // ---

# // ## 🧩 Tóm tắt thuật toán

# // 1. Sort mảng.
# // 2. Dùng 2 con trỏ tạo window.
# // 3. Nếu `max > min*k` → tăng `i`.
# // 4. Lưu độ dài lớn nhất.
# // 5. Kết quả = `n - maxLen`.

# // ---

# // Nếu bạn muốn mình:

# // * Vẽ timeline con trỏ i/j.
# // * Dry run chi tiết từng dòng code.
# // * Viết lại bằng Python / giải thích dễ hơn.

# // Cứ nói mình biết 👍

# // Bài này thường được hiểu như sau (theo LeetCode / DSA chuẩn):

# // ---

# // ## 📌 Đề bài (dịch nghĩa)

# // Cho một mảng số nguyên `nums`.

# // Một mảng được gọi là **balanced (cân bằng)** nếu:

# // > **Tổng các phần tử ở vị trí chẵn = Tổng các phần tử ở vị trí lẻ**
# // > (đếm theo index 0-based).

# // Nhiệm vụ của bạn:

# // 👉 **Xóa ít phần tử nhất** (có thể xóa ở bất kỳ vị trí nào) để mảng sau khi xóa trở thành **balanced**.

# // Trả về **số phần tử tối thiểu cần xóa**.

# // ---

# // ## 📊 Ví dụ minh họa

# // ### Ví dụ 1

# // ```
# // nums = [2, 1, 6, 4]
# // ```

# // Index:   0  1  2  3
# // Value:   2  1  6  4

# // * Tổng chẵn = 2 + 6 = 8
# // * Tổng lẻ   = 1 + 4 = 5
# //   → Không cân bằng

# // Thử xóa từng phần tử:

# // * Xóa 2 → [1,6,4]

# //   * chẵn = 1 + 4 = 5
# //   * lẻ = 6 = 6 ❌

# // * Xóa 1 → [2,6,4]

# //   * chẵn = 2 + 4 = 6
# //   * lẻ = 6 = 6 ✅ Balanced

# // Chỉ cần xóa **1 phần tử** → Kết quả = **1**

# // ---

# // ### Ví dụ 2

# // ```
# // nums = [1,1,1]
# // ```

# // * chẵn = 1 + 1 = 2
# // * lẻ = 1 = 1 ❌

# // Thử xóa:

# // * Xóa index 0 → [1,1] → chẵn = 1, lẻ = 1 ✅

# // → Kết quả = **1**

# // ---

# // ## ⚠️ Điểm quan trọng dễ nhầm

# // Khi bạn **xóa 1 phần tử**:

# // ➡️ Các phần tử phía sau **dịch trái**
# // ➡️ Index chẵn/lẻ **đổi lại**

# // Ví dụ:

# // ```
# // nums = [2, 1, 6, 4]

# // Xóa index 1 (giá trị 1)

# // Mảng mới: [2, 6, 4]
# // Index mới: 0  1  2
# // ```

# // Nên:

# // * 6 từ index 2 → thành index 1
# // * 4 từ index 3 → thành index 2

# // 👉 Vì vậy khi tính tổng phải tính theo **index mới**, không phải index cũ.

# // ---

# // ## 🎯 Tóm tắt yêu cầu

# // Bạn cần:

# // 1. Thử xóa từng vị trí (hoặc tính toán thông minh).
# // 2. Sau khi xóa:

# //    * Tính tổng vị trí chẵn.
# //    * Tính tổng vị trí lẻ.
# // 3. Nếu bằng nhau → hợp lệ.
# // 4. Tìm số lần xóa **ít nhất**.

# // ---

# // ## 🧩 Bản chất thuật toán

# // Để tối ưu (O(n)):

# // * Dùng **prefix sum**:

# //   * Tổng chẵn bên trái.
# //   * Tổng lẻ bên trái.
# //   * Tổng chẵn bên phải.
# //   * Tổng lẻ bên phải.
# // * Khi xóa 1 phần tử:

# //   * Phần bên phải bị **đảo chẵn ↔ lẻ**.

# // Đây là key insight của bài.

# // ---

# // Nếu bạn muốn, mình có thể:

# // * Giải từng bước bằng hình minh họa.
# // * Viết code Python/Java.
# // * Giải thích prefix sum đoạn này chi tiết.

# // Bạn muốn mình giải theo hướng nào tiếp? 🚀
