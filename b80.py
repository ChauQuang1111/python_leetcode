#  // Make Array Elements Equal to Zero(28/10/2025)
# Dưới đây là phần **giải thích chi tiết thuật toán** kèm **chú thích từng dòng code Python** cho bài LeetCode **3354. Make Array Elements Equal to Zero** 👇

class Solution(object):
    def countValidSelections(self, nums):
        # Tính tổng toàn bộ các phần tử trong mảng
        total = sum(nums)
        # Biến lưu tổng các phần tử bên trái phần tử hiện tại
        ls = 0
        # Biến đếm số trường hợp hợp lệ
        cases = 0

        # Duyệt qua từng phần tử trong mảng
        for i in range(len(nums)):
            # Tính tổng các phần tử bên phải (right sum)
            rs = total - ls - nums[i]

            # Chỉ xét nếu phần tử hiện tại là 0
            if nums[i] == 0:
                # Trường hợp 1: tổng trái = tổng phải
                # -> có thể giảm từ trái hoặc phải đều hợp lệ
                if ls == rs:
                    cases += 2
                # Trường hợp 2: tổng trái và phải chênh lệch đúng 1
                # -> chỉ có một hướng giảm hợp lệ
                elif ls == rs - 1 or ls - 1 == rs:
                    cases += 1

            # Cập nhật tổng bên trái để xét phần tử kế tiếp
            ls += nums[i]

        # Trả về tổng số trường hợp hợp lệ
        return cases

# ### 💡 **Ý tưởng bài toán:**

# Bạn được cho một mảng `nums` gồm các số nguyên (0 hoặc dương).
# Bạn có thể chọn **một vị trí chứa số 0** và bắt đầu "giảm" các phần tử **bên trái hoặc bên phải** của nó đi 1, cho đến khi **toàn bộ mảng trở thành 0**.
# Câu hỏi: Có **bao nhiêu vị trí số 0 hợp lệ** mà nếu bắt đầu từ đó, ta **có thể làm cho toàn bộ mảng về 0** theo cách hợp lệ?

# ---

### 🧩 **Giải thích thuật toán từng bước:**

# ```python
# class Solution(object):
#     def countValidSelections(self, nums):
#         total, ls, cases = sum(nums), 0, 0
# ```

# * `total`: tổng toàn bộ các phần tử trong mảng.
# * `ls`: tổng bên **trái** của phần tử hiện tại (left sum).
# * `cases`: số lượng vị trí hợp lệ mà ta có thể chọn (kết quả cuối cùng).

# ---

# ```python
#         for i in range(len(nums)):
#             rs = total - ls - nums[i]
# ```

# * Duyệt qua từng phần tử `nums[i]`.
# * `rs` (right sum) là tổng các phần tử **bên phải** phần tử hiện tại.
#   (Công thức: `rs = total - ls - nums[i]`)

# ---

# ```python
#             if nums[i] == 0:
# ```

# * Chỉ xét khi phần tử hiện tại là **0** (vì ta chỉ có thể bắt đầu từ 0).

# ---

# ```python
#                 if ls == rs:
#                     cases += 2
# ```

# * Nếu **tổng bên trái == tổng bên phải**,
#   → có thể chọn **giảm từ bên trái hoặc bên phải** đều hợp lệ
#   → cộng thêm **2 trường hợp hợp lệ**.

# ---

# ```python
#                 elif ls == rs - 1 or ls - 1 == rs:
#                     cases += 1
# ```

# * Nếu **tổng hai bên chênh lệch đúng 1**,
#   → chỉ có **1 hướng** có thể giảm để làm cân bằng
#   → cộng thêm **1 trường hợp hợp lệ**.



# ```python
#             ls += nums[i]
# ```

# * Cập nhật tổng bên trái (`ls`) sau khi duyệt qua phần tử hiện tại.

# ---

# ```python
#         return cases
# ```

# * Trả về tổng số trường hợp hợp lệ (`cases`).

# ---

### 📘 **Ví dụ minh họa:**

# Giả sử:

# ```python
# nums = [1, 0, 1]
# ```

# 👉 Tính toán từng bước:

# | i | nums[i] | ls | rs    | Điều kiện       | cases |
# | - | ------- | -- | ----- | --------------- | ----- |
# | 0 | 1       | 0  | 1+0=1 | Không phải 0    | 0     |
# | 1 | 0       | 1  | 1     | `ls == rs` → +2 | 2     |
# | 2 | 1       | 1  | 0     | Không phải 0    | 2     |

# ✅ Kết quả cuối cùng:
# `cases = 2`

# ---

# ### 🧠 **Tóm tắt ý tưởng:**

# * Tính tổng hai bên cho từng phần tử là 0.
# * Nếu hai bên bằng nhau → có 2 hướng giảm hợp lệ.
# * Nếu chênh nhau đúng 1 → có 1 hướng hợp lệ.
# * Cộng dồn các trường hợp đó.

# ---

# Bạn có muốn mình minh họa **thêm một ví dụ phức tạp hơn (có nhiều số 0 và số lớn hơn 1)** để thấy rõ cách `ls` và `rs` thay đổi không?

# // Rồi 👌 mình sẽ **giải thích chi tiết từng dòng của thuật toán trong code này** (`LeetCode 3354. Count Valid Selections` — hoặc tương tự).
# import java.util.*;

# public class b81 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int n = sc.nextInt();

#         int[] nums = new int[n];
#         for (int i = 0; i < n; i++) {
#             nums[i] = sc.nextInt();
#         }

#         // Gọi hàm xử lý
#         int result = countValidSelections(nums);

#         // In kết quả ra màn hình
#         System.out.println(result);

#         sc.close();
#     }

#     // Hàm chính: đếm số vị trí "0" hợp lệ theo quy tắc đề bài
#     public static int countValidSelections(int[] nums) {
#         int total = 0, ls = 0, cases = 0;

#         // Tính tổng toàn bộ mảng
#         for (int num : nums)
#             total += num;

#         // Duyệt qua từng phần tử trong mảng
#         for (int num : nums) {
#             // Tính tổng bên phải = tổng toàn bộ - tổng bên trái - phần tử hiện tại
#             int rs = total - ls - num;

#             // Chỉ xét khi phần tử hiện tại là 0
#             if (num == 0) {
#                 // Trường hợp 1: tổng hai bên bằng nhau → có thể đặt 1 ở trái hoặc phải (2 cách)
#                 if (ls == rs) {
#                     cases += 2;
#                 }
#                 // Trường hợp 2: tổng hai bên lệch nhau đúng 1 → chỉ có 1 cách để cân bằng
#                 else if (ls == rs - 1 || ls - 1 == rs) {
#                     cases += 1;
#                 }
#             }

#             // Cập nhật tổng bên trái sau khi duyệt qua phần tử này
#             ls += num;
#         }

#         // Trả về số lượng trường hợp hợp lệ
#         return cases;
#     }

# }

# // ---

# // ## 🧩 Ý tưởng bài toán

# // Cho một mảng `nums`, ta cần **đếm số lượng vị trí có thể chọn (gọi là valid
# // selection)** sao cho:

# // * Nếu chọn một vị trí chứa **0**, ta có thể tưởng tượng “đặt 1 viên bi” vào
# // bên trái hoặc bên phải vị trí đó.
# // * Một vị trí là “hợp lệ” nếu sau khi thêm “1” về một phía, **tổng bên trái =
# // tổng bên phải** của phần tử đó.

# // Bài yêu cầu: đếm số cách hợp lệ như vậy.

# // ---

# // ## 🧮 Giải thích code

# // ```java
# // public int countValidSelections(int[] nums) {
# // int total = 0, ls = 0, cases = 0;
# // ```

# // * `total`: tổng toàn bộ mảng (sum của tất cả phần tử).
# // * `ls`: tổng bên **trái** tính đến phần tử hiện tại (Left Sum).
# // * `cases`: đếm số vị trí hợp lệ (số cách valid selection).

# // ---

# // ```java
# // for (int num : nums) total += num;
# // ```

# // 👉 Tính tổng `total` của toàn bộ mảng.

# // ---

# // ```java
# // for (int num : nums) {
# // int rs = total - ls - num;
# // ```

# // * `rs` (Right Sum) = tổng bên phải của phần tử hiện tại.
# // → vì tổng toàn bộ `total = ls + num + rs`
# // → nên `rs = total - ls - num`.

# // ---

# // ```java
# // if (num == 0) {
# // ```

# // → Ta chỉ xét các vị trí có giá trị bằng `0`, vì chỉ ở đó ta **có thể đặt thêm
# // 1 vào bên trái hoặc bên phải**.

# // ---

# // ```java
# // if (ls == rs) {
# // cases += 2;
# // }
# // ```

# // ✅ Nếu tổng hai bên bằng nhau →
# // cả **đặt bên trái** và **đặt bên phải** đều hợp lệ → `+2`.

# // ---

# // ```java
# // else if (ls == rs - 1 || ls - 1 == rs) {
# // cases += 1;
# // }
# // ```

# // ✅ Nếu tổng hai bên **chênh lệch đúng 1**,
# // thì chỉ **một bên đặt thêm 1** mới cân bằng được → `+1`.

# // ---

# // ```java
# // }
# // ls += num;
# // }
# // ```

# // Sau khi xét xong phần tử này,
# // → cộng phần tử hiện tại vào `ls` (vì bước qua bên phải rồi).

# // ---

# // ```java
# // return cases;
# // ```

# // Trả về tổng số cách hợp lệ.

# // ---

# // ## 🔢 Ví dụ minh họa

# // ```
# // nums = [1, 0, 1]
# // ```

# // ### Bước 1:

# // * total = 2
# // * i=0 → num=1 → không phải 0 → bỏ qua
# // * ls=1

# // ### Bước 2:

# // * i=1 → num=0
# // * rs = total - ls - num = 2 - 1 - 0 = 1
# // * ls = 1, rs = 1 → ls == rs → +2
# // → cases = 2
# // * ls += 0 → ls = 1

# // ### Bước 3:

# // * i=2 → num=1 → không phải 0 → bỏ qua

# // ✅ Kết quả: `cases = 2`.

# // ---

# // ## 🧠 Tóm tắt ý tưởng:

# // Thuật toán duyệt từng phần tử:

# // * Duy trì tổng trái (`ls`) và tính tổng phải (`rs`).
# // * Khi gặp `0`:

# // * Nếu `ls == rs` → có **2 cách hợp lệ**.
# // * Nếu `|ls - rs| == 1` → có **1 cách hợp lệ**.
# // * Cộng dồn kết quả.

# // ---

# // Bạn có muốn mình thêm **phiên bản Java có `main()` và chú thích từng dòng
# // code** cho dễ hiểu hơn không?

# // ---

# // ## 🧩 Đề bài:

# // Bạn được cho một mảng số nguyên `nums`.

# // Trong **một thao tác**, bạn có thể:

# // * **Chọn một phần tử nhỏ nhất khác 0 trong mảng**, và
# // * **Trừ giá trị đó** khỏi **tất cả các phần tử khác 0** trong mảng.

# // 👉 Mục tiêu: Tính **số thao tác tối thiểu** để **tất cả các phần tử trở thành
# // 0**.

# // ---

# // ## 🔢 Ví dụ minh họa:

# // ### Ví dụ 1:

# // ```python
# // nums = [1, 5, 0, 3, 5]
# // ```

# // **Bước 1:**
# // Phần tử nhỏ nhất khác 0 là `1`.
# // → Trừ `1` khỏi tất cả phần tử khác 0 → `[0, 4, 0, 2, 4]`

# // **Bước 2:**
# // Phần tử nhỏ nhất khác 0 bây giờ là `2`.
# // → Trừ `2` khỏi tất cả phần tử khác 0 → `[0, 2, 0, 0, 2]`

# // **Bước 3:**
# // Phần tử nhỏ nhất khác 0 bây giờ là `2`.
# // → Trừ `2` khỏi tất cả phần tử khác 0 → `[0, 0, 0, 0, 0]`

# // ✅ Tất cả phần tử đều bằng 0 sau **3 thao tác**.

# // → Kết quả: **3**

# // ---

# // ### Ví dụ 2:

# // ```python
# // nums = [0, 0, 0]
# // ```

# // Tất cả đều bằng 0 rồi → không cần làm gì.
# // ✅ Kết quả: **0**

# // ---

# // ## 💡 Nhận xét quan trọng:

# // Mỗi thao tác chỉ “loại bỏ” **một giá trị khác nhau khác 0** trong mảng.

# // 👉 Nghĩa là:

# // * Nếu mảng có `k` **giá trị khác 0 và khác nhau**,
# // thì số bước chính là `k`.

# // ---

# // ## ⚙️ Công thức:

# // ```python
# // Số thao tác = số lượng giá trị khác nhau trong nums mà != 0
# // ```

# // ---

# // ## 🧠 Ví dụ tổng quát:

# // ```python
# // nums = [4, 4, 2, 0, 3, 3]
# // Các giá trị khác 0: {2, 3, 4}
# // → 3 giá trị khác nhau
# // → Kết quả = 3
# // ```

# // ---

# // ## ✅ Kết luận:

# // **Ý tưởng giải:**
# // Chỉ cần đếm **số lượng phần tử khác nhau khác 0** trong mảng.

# // ---

# // ## 🧮 Mã giả:

# // ```python
# // def minimumOperations(nums):
# // return len(set(nums) - {0})
# // ```

# // ---

# // Bạn có muốn mình viết lại **phiên bản Java** (có `main` và chú thích từng
# // dòng) cho bài này không?
