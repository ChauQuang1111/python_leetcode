# //  Transformed Array(05/02/2026)
# //  ## 📘 LeetCode – **Transformed Array** (Giải thích đề bài)
# Ok 👍 đây là bài **LeetCode 3379 – Transformed Array** bạn gửi bằng **Python**.
# Mình sẽ:

# 1. Giải thích thuật toán dễ hiểu
# 2. So sánh với bản Java trước
# 3. Thêm **chú thích trực tiếp vào code**

# ---

# # 🧠 Ý tưởng thuật toán

# Với mỗi vị trí `i` trong mảng `nums`:

# * Lấy giá trị `num = nums[i]`.
# * Nếu `num = 0` → không nhảy → giữ nguyên.
# * Nếu `num ≠ 0` → nhảy `num` bước trong mảng vòng tròn.
# * Lấy giá trị ở vị trí nhảy tới → đưa vào `result`.



# 🔄 Công thức nhảy


# newIndex = (i + num) % n
# ```

# Trong Python:

# * `%` luôn ra số dương → không cần xử lý như Java.

# ---

# 📊 Ví dụ

# ```
# nums = [2, -1, 1]
# n = 3
# ```

# ### i = 0

# ```
# 0 + 2 = 2 → result[0] = nums[2] = 1
# ```

### i = 1

# ```
# 1 + (-1) = 0 → result[1] = nums[0] = 2
# ```

### i = 2

# ```
# 2 + 1 = 3 % 3 = 0 → result[2] = nums[0] = 2
# ```

# Kết quả:

# ```
# [1, 2, 2]
# ```

# ---

# # 📌 Code đã thêm chú thích

# ```python
from typing import List
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:

        result = []          # Mảng kết quả sau khi biến đổi
        n = len(nums)        # Độ dài mảng

        # enumerate(nums) trả về (index, value)
        for i, num in enumerate(nums):

            # Nếu giá trị = 0 → không nhảy
            if num == 0:
                result.append(num)   # Giữ nguyên giá trị

            else:
                """
                Tính vị trí mới sau khi nhảy:

                i + num : vị trí nhảy tới
                % n     : quay vòng mảng (circular array)

                Python % luôn dương nên không cần +n như Java
                """
                new_index = (i + num) % n

                # Lấy giá trị tại vị trí mới
                result.append(nums[new_index])

        # Trả về mảng kết quả
        return result
# ```

# ---

# # 🔍 Giải thích từng thành phần

# ---

# ## 1️⃣ enumerate(nums)

# Ví dụ:

# ```python
# nums = [5, 7, 9]

# for i, num in enumerate(nums):
#     print(i, num)
# ```

# Output:

# ```
# 0 5
# 1 7
# 2 9
# ```

# → Lấy **index + value** cùng lúc.

# ---

# ## 2️⃣ Vì sao có if num == 0 ?

# Thực ra:

# ```
# (i + 0) % n = i
# ```

# → Kết quả vẫn là chính nó.

# Nên đoạn này:

# ```python
# if num == 0:
#     result.append(num)
# ```

# Chỉ để code dễ đọc — không bắt buộc.

# Có thể viết gọn:

# ```python
# result.append(nums[(i + num) % n])
# ```

# ---

# 🆚 So với code Java

# | Python          | Java          |
# | --------------- | ------------- |
# | `%` luôn dương  | `%` có thể âm |
# | Không cần `+ n` | Phải `+ n`    |
# | List động       | Array cố định |

# ---

# # ⏱️ Độ phức tạp

# ### Time

# ```
# O(n)
# ```

# Duyệt 1 lần.

# ### Space

# ```
# O(n)
# ```

# Tạo list mới.

# ---

# 🧠 Tóm tắt 1 câu

# > Mỗi phần tử nhảy num bước trong mảng vòng tròn rồi copy giá trị ở vị trí đó.

# ---

# Nếu bạn muốn mình làm thêm:

# * Dry run bằng hình mũi tên từng bước
# * Viết lại không dùng enumerate
# * So sánh Python vs Java vs C++
# * Cho bài tương tự để luyện

# → Nói mình làm tiếp 👍

# import java.util.*;
 
# public class b170{
#    static Scanner sc = new Scanner(System.in);
#    public static void main(String[] args) {
#      int n = sc.nextInt();
#      int[] nums = new int[n];

#         // Nhập mảng
#         System.out.println("Nhap cac phan tu:");
#         for (int i = 0; i < n; i++) {
#             nums[i] = sc.nextInt();
#         }



#         // Gọi hàm biến đổi
#         int[] result = constructTransformedArray(nums);

#         // In kết quả
#         System.out.println("Mang sau khi bien doi:");

#         for (int i = 0; i < n; i++) {
#             System.out.print(result[i] + " ");
#         }

#         sc.close();
    

#     }
# // Hàm biến đổi mảng theo đề bài LeetCode
#     public  static int[] constructTransformedArray(int[] nums) {

#         int n = nums.length;          // Lấy độ dài mảng
#         int[] ans = new int[n];      // Tạo mảng kết quả

#         // Duyệt từng phần tử
#         for (int i = 0; i < n; i++) {

#             /*
#              * Tính vị trí mới sau khi "nhảy"
#              * i + nums[i]  : vị trí nhảy tới
#              * % n          : quay vòng mảng
#              * + n rồi % n : xử lý trường hợp số âm
#              */
#             int newIndex = ((i + nums[i]) % n + n) % n;

#             // Lấy giá trị tại vị trí mới gán vào kết quả
#             ans[i] = nums[newIndex];
#         }

#         return ans;   // Trả về mảng đã biến đổi
    

# }}

   

# // Bài **“Transformed Array”** trên LeetCode là bài **mảng + mô phỏng dịch chuyển phần tử theo giá trị của chính nó**.
# // Ok mình sẽ **giải thích thuật toán trong code của bạn từng dòng — cực dễ hiểu** 👇
# // (đây chính là lời giải chuẩn của bài **LeetCode – Transformed Array**)

# // ---

# // # 📌 Code gốc

# // ```java
# // class Solution {
# //     public int[] constructTransformedArray(int[] nums) {
# //         int n = nums.length;
# //         int[] ans = new int[n];

# //         for (int i = 0; i < n; i++) {
# //             ans[i] = nums[((i + nums[i]) % n + n) % n];
# //         }

# //         return ans;
# //     }
# // }
# // ```

# // ---

# // # 🧠 Ý tưởng thuật toán

# // Thuật toán này làm đúng theo đề:

# // > Với mỗi vị trí i → nhảy nums[i] bước → lấy giá trị ở vị trí mới.

# // Không đổi mảng gốc — chỉ tạo mảng mới.

# // ---

# // # 🔍 Giải thích từng dòng

# // ---

# // ## 1️⃣ Lấy độ dài mảng

# // ```java
# // int n = nums.length;
# // ```

# // * `n` = số phần tử.
# // * Dùng để:

# //   * Chia `% n` (quay vòng mảng).
# //   * Tạo mảng kết quả.

# // ---

# // ## 2️⃣ Tạo mảng kết quả

# // ```java
# // int[] ans = new int[n];
# // ```

# // * `ans[i]` = giá trị sau khi biến đổi tại vị trí i.

# // ---

# // ## 3️⃣ Duyệt từng phần tử

# // ```java
# // for (int i = 0; i < n; i++)
# // ```

# // * Xử lý từng vị trí `i`.

# // ---

# // # 🔥 Dòng quan trọng nhất

# // ```java
# // ans[i] = nums[((i + nums[i]) % n + n) % n];
# // ```

# // Tách ra cho dễ hiểu 👇

# // ---

# // ## Bước 1 — Tính vị trí nhảy tới

# // ```java
# // i + nums[i]
# // ```

# // * Nếu `nums[i]` dương → nhảy phải.
# // * Nếu âm → nhảy trái.

# // ---

# // ## Bước 2 — Quay vòng mảng

# // ```java
# // (i + nums[i]) % n
# // ```

# // Để không vượt quá mảng.

# // Ví dụ:

# // ```
# // n = 5
# // i = 4
# // nums[i] = 2

# // 4 + 2 = 6
# // 6 % 5 = 1
# // ```

# // → Quay về index 1.

# // ---

# // ## ⚠️ Vấn đề: số âm

# // Java `%` có thể ra âm.

# // Ví dụ:

# // ```
# // i = 1
# // nums[i] = -3
# // n = 5

# // 1 + (-3) = -2
# // -2 % 5 = -2   ❌
# // ```

# // Index âm → lỗi.

# // ---

# // ## Bước 3 — Chuẩn hóa về dương

# // ```java
# // ((i + nums[i]) % n + n) % n
# // ```

# // Ý nghĩa:

# // 1. `% n` lần 1 → đưa về khoảng (-n → n)
# // 2. `+ n` → đẩy lên dương
# // 3. `% n` lần 2 → đưa về [0 → n-1]

# // ---

# // ## 📊 Ví dụ minh họa

# // ```
# // nums = [2, -1, 1]
# // n = 3
# // ```

# // ---

# // ### i = 0

# // ```
# // i + nums[i] = 0 + 2 = 2
# // 2 % 3 = 2
# // ans[0] = nums[2] = 1
# // ```

# // ---

# // ### i = 1

# // ```
# // 1 + (-1) = 0
# // 0 % 3 = 0
# // ans[1] = nums[0] = 2
# // ```

# // ---

# // ### i = 2

# // ```
# // 2 + 1 = 3
# // 3 % 3 = 0
# // ans[2] = nums[0] = 2
# // ```

# // ---

# // ✅ Kết quả:

# // ```
# // [1, 2, 2]
# // ```

# // ---

# // # 🖼️ Minh họa “nhảy vòng tròn”

# // Hình dung:

# // * Mảng là vòng tròn.
# // * Nhảy quá phải → quay đầu.
# // * Nhảy quá trái → vòng về cuối.

# // ---

# // # ⏱️ Độ phức tạp

# // ### Time Complexity

# // ```
# // O(n)
# // ```

# // * Duyệt mảng 1 lần.

# // ### Space Complexity

# // ```
# // O(n)
# // ```

# // * Tạo mảng `ans`.

# // ---

# // # 🧾 Tóm tắt thuật toán

# // 1️⃣ Duyệt từng index `i`
# // 2️⃣ Tính vị trí mới:

# // ```
# // i + nums[i]
# // ```

# // 3️⃣ Dùng `% n` để quay vòng
# // 4️⃣ Chuẩn hóa số âm
# // 5️⃣ Lấy giá trị gán vào `ans[i]`

# // ---

# // # 🧠 Hiểu bản chất 1 câu

# // > Mỗi phần tử đứng yên, nhưng copy giá trị từ vị trí nó nhảy tới trong mảng vòng tròn.

# // ---

# // Nếu bạn muốn mình:

# // * Dry run từng dòng với test case bạn tự cho
# // * Viết lại không dùng `%` 2 lần
# // * Làm bản Python / C++

# // → Gửi mình nhé 👍

# // ---

# // ## 🧩 Đề bài (diễn giải dễ hiểu)

# // Bạn được cho:

# // * Một mảng số nguyên `nums` có độ dài `n`.

# // Nhiệm vụ:

# // * Tạo mảng mới `result` cũng độ dài `n`.
# // * Với mỗi vị trí `i`, bạn **di chuyển từ i** sang vị trí khác dựa trên giá trị `nums[i]`.

# // ---

# // ## 🔄 Quy tắc biến đổi

# // Với mỗi `i`:

# // ```
# // newIndex = (i + nums[i]) % n
# // ```

# // Sau đó:

# // ```
# // result[i] = nums[newIndex]
# // ```

# // ---

# // ## ⚠️ Lưu ý quan trọng

# // ### 1️⃣ Có số âm

# // Nếu `nums[i]` âm → di chuyển sang trái.

# // Nhưng `%` trong nhiều ngôn ngữ có thể ra số âm → cần chuẩn hóa:

# // ```
# // newIndex = ((i + nums[i]) % n + n) % n
# // ```

# // Để đảm bảo luôn nằm trong `[0, n-1]`.

# // ---

# // ## 🧠 Hiểu bản chất bài

# // * Mỗi phần tử **không đổi vị trí**.
# // * Nhưng nó **nhìn sang vị trí khác** rồi lấy giá trị về.

# // Giống kiểu:

# // > “Đứng tại chỗ, nhưng copy giá trị từ chỗ khác.”

# // ---

# // ## 📊 Ví dụ minh họa

# // ### Ví dụ 1

# // ```
# // nums = [2, -1, 1]
# // n = 3
# // ```

# // ---

# // ### i = 0

# // ```
# // newIndex = (0 + 2) % 3 = 2
# // result[0] = nums[2] = 1
# // ```

# // ---

# // ### i = 1

# // ```
# // newIndex = (1 + (-1)) % 3 = 0
# // result[1] = nums[0] = 2
# // ```

# // ---

# // ### i = 2

# // ```
# // newIndex = (2 + 1) % 3 = 0
# // result[2] = nums[0] = 2
# // ```

# // ---

# // ✅ Kết quả:

# // ```
# // result = [1, 2, 2]
# // ```

# // ---

# // ## 🖼️ Minh họa dịch chuyển

# // Hình dung mảng là **vòng tròn**:

# // * Đi quá phải → quay lại đầu.
# // * Đi quá trái → vòng về cuối.

# // ---

# // ## 💻 Code mẫu (Java)

# // ```java
# // public int[] transformedArray(int[] nums) {
# //     int n = nums.length;
# //     int[] result = new int[n];

# //     for (int i = 0; i < n; i++) {
# //         int newIndex = (i + nums[i]) % n;

# //         // xử lý số âm
# //         if (newIndex < 0) {
# //             newIndex += n;
# //         }

# //         result[i] = nums[newIndex];
# //     }

# //     return result;
# // }
# // ```

# // ---

# // ## 🧮 Độ phức tạp

# // * Time: `O(n)` → duyệt 1 lần
# // * Space: `O(n)` → tạo mảng mới

# // ---

# // ## 📝 Tóm tắt nhớ nhanh

# // | Bước | Làm gì                       |
# // | ---- | ---------------------------- |
# // | 1    | Duyệt từng i                 |
# // | 2    | Tính `i + nums[i]`           |
# // | 3    | Lấy `% n` để không vượt mảng |
# // | 4    | Chuẩn hóa số âm              |
# // | 5    | Gán vào result               |

# // ---

# // Nếu bạn muốn mình:

# // * Trace từng bước với test case của bạn
# // * Viết code Python / C++ / JS
# // * Tối ưu hoặc làm in-place

# // → Cứ gửi mình nhé 👍

# // Ok mình giải thích lại **siêu dễ hiểu** nha — kiểu đọc xong là hiểu liền 👇

# // ---

# // # 🧩 Transformed Array – Hiểu đề bài theo cách đơn giản nhất

# // Bạn có 1 mảng:

# // ```
# // nums = [ ... ]
# // ```

# // Bạn phải tạo mảng mới `result`.

# // Nhưng **không phải biến đổi giá trị**…
# // mà là:

# // > Mỗi phần tử sẽ “nhảy” sang vị trí khác rồi lấy số ở đó.

# // ---

# // # 🧠 Hình dung như trò chơi nhảy ô

# // * Bạn đứng ở ô `i`.
# // * Số trong ô đó = số bước bạn phải nhảy.
# // * Nhảy xong → nhìn xuống ô đang đứng → lấy số đó bỏ vào result[i].

# // ---

# // # 📌 Công thức đề bài

# // ```
# // newIndex = i + nums[i]
# // ```

# // Nhưng vì mảng là vòng tròn nên phải:

# // ```
# // newIndex = (i + nums[i]) % n
# // ```

# // ---

# // # 🔄 Mảng là vòng tròn

# // Ví dụ mảng 5 phần tử:

# // ```
# // 0   1   2   3   4
# // ```

# // Đi tiếp nữa sẽ quay vòng:

# // ```
# // … → 0 → 1 → 2 …
# // ```

# // Đi ngược cũng vậy.

# // ---

# // # 📊 Ví dụ cực dễ

# // ```
# // nums = [1, 2, -1, 1]
# // n = 4
# // ```

# // ---

# // ## 👉 i = 0

# // * Đứng ô 0
# // * nums[0] = 1 → nhảy 1 bước sang phải

# // ```
# // newIndex = 0 + 1 = 1
# // ```

# // Lấy:

# // ```
# // result[0] = nums[1] = 2
# // ```

# // ---

# // ## 👉 i = 1

# // * nums[1] = 2 → nhảy 2 bước

# // ```
# // 1 → 2 → 3
# // ```

# // ```
# // result[1] = nums[3] = 1
# // ```

# // ---

# // ## 👉 i = 2

# // * nums[2] = -1 → nhảy trái 1 bước

# // ```
# // 2 → 1
# // ```

# // ```
# // result[2] = nums[1] = 2
# // ```

# // ---

# // ## 👉 i = 3

# // * nums[3] = 1 → nhảy phải 1

# // ```
# // 3 → quay vòng → 0
# // ```

# // ```
# // result[3] = nums[0] = 1
# // ```

# // ---

# // ✅ Kết quả:

# // ```
# // result = [2, 1, 2, 1]
# // ```

# // ---

# // # 🖼️ Minh họa dễ hiểu

# // Nhìn như vòng tròn:

# // * Nhảy phải → quay lại đầu.
# // * Nhảy trái → vòng về cuối.

# // ---

# // # ❗ 2 ý quan trọng nhất đề bài

# // ### 1️⃣ Không đổi chỗ phần tử

# // Bạn **không di chuyển mảng**.

# // Chỉ là:

# // ```
# // Đứng ở i → nhìn sang ô khác → copy số về.
# // ```

# // ---

# // ### 2️⃣ Có số âm

# // Âm = nhảy trái.

# // Phải dùng:

# // ```
# // ((i + nums[i]) % n + n) % n
# // ```

# // để không bị index âm.

# // ---

# // # 📝 Tóm tắt 1 dòng

# // > Mỗi vị trí i sẽ lấy giá trị ở vị trí (i + nums[i]) theo vòng tròn.

# // ---

# // Nếu bạn muốn mình:

# // * Vẽ mũi tên từng bước cho test case của bạn
# // * Giải thích bằng code Java bạn đang học
# // * Cho bài tương tự để luyện

# // → Gửi mình mảng ví dụ, mình làm cùng bạn 👍
