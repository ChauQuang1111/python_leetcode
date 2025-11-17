# // 1437. Check If All 1's Are at Least Length K Places Away(17/11/2025)
# Dưới đây là **giải thích thuật toán** và **phiên bản code đã thêm chú thích rõ ràng**.

# ---

# # ✅ **Giải thích thuật toán**

# Bài toán:
# Kiểm tra xem **tất cả các số 1** trong mảng **có cách nhau ít nhất k vị trí hay không**.

# Ví dụ:
# `nums = [1,0,0,0,1], k = 3` → hợp lệ
# `nums = [1,0,1], k = 2` → không hợp lệ (khoảng cách = 1 < 2)

# ---

## ⭐ Ý tưởng

# Ta chỉ cần theo dõi vị trí của **số 1 trước đó**:

# * Dùng biến `prev` để lưu vị trí số 1 gần nhất.
# * Khi gặp số 1 mới ở vị trí `i`:

#   * Nếu đã có số 1 trước đó (`prev != None`)
#   * Kiểm tra khoảng cách: `i - prev <= k`

#     * Nếu đúng → khoảng cách quá nhỏ → trả về **False**
# * Sau đó cập nhật `prev = i`

# Nếu duyệt hết mảng không vi phạm → trả về **True**

# ---

# # ✅ **Code Python có chú thích chi tiết**

# ```python
from typing import List
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # Trường hợp k = 0 → hai số 1 có thể đứng cạnh nhau
        if k == 0:
            return True

        prev = None   # lưu vị trí số 1 trước đó

        for i, num in enumerate(nums):
            if num == 1:
                # nếu đã gặp số 1 trước đó → kiểm tra khoảng cách
                if prev is not None and i - prev <= k:
                    return False  # vi phạm điều kiện cách nhau ít nhất k
                prev = i  # cập nhật vị trí số 1 gần nhất

        return True  # duyệt hết không vi phạm → hợp lệ


# ---

# # 🧠 **Minh họa nhanh**

# Ví dụ:
# `nums = [1,0,0,1], k = 2`

# * i=0: gặp 1 → prev = 0
# * i=1: 0 → bỏ qua
# * i=2: 0 → bỏ qua
# * i=3: gặp 1
#   → khoảng cách = 3 - 0 = 3 > 2 → OK

# → trả về **True**

# ---

# Nếu bạn muốn mình minh họa bằng hình hoặc viết phiên bản tối ưu hơn nữa, cứ nói mình nhé!

# import java.util.*;

# public class Main {

#     // Hàm kiểm tra các số 1 có cách nhau ít nhất k vị trí không
#     public static boolean kLengthApart(int[] nums, int k) {
#         int c = k;     // đếm số lượng số 0 sau số 1 trước đó — bắt đầu bằng k để số 1 đầu tiên luôn hợp lệ
#         int m = 0;     // m = 0: chưa gặp số 1 nào; m = 1: đã gặp số 1

#         for (int i = 0; i < nums.length; i++) {

#             if (nums[i] == 1) {            // nếu gặp số 1
#                 if (c < k) return false;   // khoảng cách c < k → không đủ → sai
#                 m = 1;                     // đánh dấu rằng đã gặp số 1
#                 c = 0;                     // reset bộ đếm số 0
#             }

#             else {                         // nếu là số 0
#                 if (m == 1) c++;           // chỉ đếm số 0 sau khi đã gặp số 1
#             }
#         }

#         return true;                       // duyệt hết không vi phạm → đúng
#     }


#     // Hàm main dùng Scanner để nhập dữ liệu
#     public static void main(String[] args) {
#         Scanner sc = new Scanner(System.in);

#         // Nhập độ dài mảng
#         int n = sc.nextInt();

#         int[] nums = new int[n];

#         // Nhập các phần tử 0 hoặc 1
#         for (int i = 0; i < n; i++) {
#             nums[i] = sc.nextInt();
#         }

#         // Nhập k
#         int k = sc.nextInt();

#         // Gọi hàm và in kết quả
#         boolean result = kLengthApart(nums, k);
#         System.out.println(result);

#         sc.close();
#     }
# }

# // Dưới đây là **giải thích chi tiết – dễ hiểu** cho thuật toán bạn dùng trong hàm:

# // ```java
# // public static boolean kLengthApart(int[] nums, int k)
# // ```

# // ---

# // # ✅ **Ý tưởng của thuật toán**

# // Thuật toán dựa vào việc **đếm khoảng cách giữa hai số 1 liên tiếp**.

# // Bạn dùng 2 biến:

# // ### 🔹 `c` – đếm khoảng cách (số lượng số 0 xuất hiện sau 1)

# // * Khi gặp `1` mới → kiểm tra xem `c` có ≥ `k` hay không
# // * Nếu không đạt → return false
# // * Sau đó reset `c = 0`

# // ### 🔹 `m` – đánh dấu xem đã từng gặp số 1 chưa

# // * `m = 0`: chưa gặp 1
# // * `m = 1`: đã gặp 1 → bắt đầu đếm khoảng cách

# // ---

# // # 🧠 **Giải thích từng dòng thuật toán**

# // ### Ban đầu:

# // ```java
# // int c = k, m = 0;
# // ```

# // * `c = k`: để đảm bảo rằng **số 1 đầu tiên** không gây lỗi (coi như trước đó có đủ khoảng cách)
# // * `m = 0`: chưa gặp 1 nào

# // ---

# // ### Duyệt mảng:

# // ```java
# // for (int i = 0; i < nums.length; i++)
# // ```

# // ---

# // ## Trường hợp 1️⃣: Gặp số **1**

# // ```java
# // if(nums[i] == 1)
# // {
# //     if(c < k) return false;   // khoảng cách không đủ
# //     m = 1;                    // đã bắt đầu gặp 1
# //     c = 0;                    // reset bộ đếm
# // }
# // ```

# // Giải thích:

# // * Nếu `c < k` → nghĩa là số 1 này quá gần số 1 trước → sai
# // * Set `m = 1` → để sau đó biết rằng mình sẽ bắt đầu đếm khoảng cách
# // * Reset `c = 0` để bắt đầu tính lại số 0 tiếp theo

# // ---

# // ## Trường hợp 2️⃣: Gặp số **0**

# // ```java
# // else
# // {
# //     if(m == 1) c++;
# // }
# // ```

# // * Chỉ đếm số 0 **sau khi đã gặp 1 đầu tiên**
# // * Nếu chưa gặp số 1 (`m = 0`) thì không cần đếm

# // ---

# // ### Nếu duyệt xong mà không phát hiện vi phạm:

# // ```java
# // return true;
# // ```

# // ---

# // # 📌 **Ví dụ minh họa**

# // ### Input:

# // ```
# // nums = [1,0,0,1], k = 2
# // ```

# // Duyệt:

# // | i | nums[i] | hành động              | c | m |
# // | - | ------- | ---------------------- | - | - |
# // | 0 | 1       | c (=2) ≥ k → OK, reset | 0 | 1 |
# // | 1 | 0       | m = 1 → c++            | 1 | 1 |
# // | 2 | 0       | c++                    | 2 | 1 |
# // | 3 | 1       | c (=2) ≥ 2 → OK, reset | 0 | 1 |

# // → **true**

# // ---

# // ### Input:

# // ```
# // nums = [1,0,1], k = 2
# // ```

# // Duyệt:

# // | i | nums[i] | hành động                 | c | m |
# // | - | ------- | ------------------------- | - | - |
# // | 0 | 1       | OK                        | 0 | 1 |
# // | 1 | 0       | c++                       | 1 | 1 |
# // | 2 | 1       | c (=1) < 2 → return false |   |   |

# // → **false**

# // ---

# // # ✅ **Kết luận**

# // Thuật toán:

# // * Duyệt một lần → O(n)
# // * Dùng 2 biến để theo dõi khoảng cách và trạng thái
# // * Rất tối ưu và đúng ý đề bài

# // Bạn cần mình **thêm chú thích vào code Java** không?


# // # ✅ **📘 Đề bài yêu cầu gì?**

# // Bạn được cho:

# // * Một **mảng nhị phân `nums`** chỉ gồm `0` và `1`
# // * Một số nguyên `k`

# // Bạn phải kiểm tra xem:

# // 👉 **Mọi cặp số `1` trong mảng có cách nhau ít nhất `k` vị trí hay không?**

# // Nói cách khác:

# // > Với mọi cặp chỉ số i < j sao cho nums[i] = nums[j] = 1
# // > ⇒ phải thỏa mãn: **j - i - 1 ≥ k**

# // Nếu đúng → trả về `true`
# // Nếu sai → trả về `false`

# // ---

# // # 🔍 **💡 Hiểu theo cách dễ nhất**

# // Giả sử `k = 2`. Điều kiện:

# // ```
# // 1 _ _ 1   ✔ hợp lệ (cách nhau 2 zeros)
# // 1 _ 1     ✘ không hợp lệ (chỉ có 1 zero)
# // 11        ✘ không hợp lệ (không có zero)
# // ```

# // Bạn phải kiểm tra khoảng cách giữa **tất cả các số 1 liên tiếp**.

# // ---

# // # 📌 **Ví dụ minh họa**

# // ### Ví dụ 1:

# // ```
# // nums = [1,0,0,0,1,0,0,1], k = 2
# // ```

# // Các khoảng cách:

# // * Giữa 1 ở vị trí 0 và 4 → cách 3 chữ số → ✔ ≥ 2
# // * Giữa 1 ở vị trí 4 và 7 → cách 2 chữ số → ✔ ≥ 2

# // → **Trả về true**

# // ---

# // ### Ví dụ 2:

# // ```
# // nums = [1,0,1], k = 2
# // ```

# // Khoảng cách:

# // * Giữa 1 ở vị trí 0 và 2 → cách **1** chữ số → ✘ < 2

# // → **Trả về false**

# // ---

# // # 🧠 **Tư duy lời giải**

# // Duyệt qua mảng, ghi lại vị trí của số 1 trước đó (`prev`).
# // Khi gặp 1 mới:

# // * Nếu `(current_index - prev - 1) < k` → sai → trả về `false`
# // * Cập nhật `prev = current_index`

# // Nếu duyệt xong không vi phạm gì → `true`.

# // ---

# // Nếu bạn cần **code Python/Java + chú thích** thì mình viết ngay cho bạn!
