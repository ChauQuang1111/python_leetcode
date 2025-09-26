# #  // 611. Valid Triangle Number(26/09/2025)

from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()   # B1: Sắp xếp mảng tăng dần
        n = len(nums)
        ans = 0       # Kết quả cuối cùng: số bộ ba (a, b, c) tạo thành tam giác

        # B2: Duyệt qua từng phần tử nums[i] coi như cạnh lớn nhất (c)
        for i in range(n-1, 1, -1):   # i chạy từ n-1 -> 2
            c = nums[i]

            # Trường hợp 1: Nếu cạnh nhỏ nhất + cạnh nhỏ thứ 2 > c,
            # thì bất kỳ 3 số nào từ 0..i đều tạo thành tam giác
            if nums[0] + nums[1] > c:
                # Tính số cách chọn 3 phần tử trong (i+1) số: C(i+1, 3)
                ans += (i + 1) * i * (i - 1) // 6
                break   # Không cần xét tiếp vì i càng lớn thì điều kiện càng thỏa

            # Trường hợp 2: Nếu hai cạnh lớn nhất trong [0..i-1] cộng lại < c,
            # thì không thể tạo tam giác nào với cạnh c này
            if nums[i-2] + nums[i-1] < c:
                continue

            # Trường hợp 3: Dùng 2 con trỏ để đếm số cặp (a, b) thỏa mãn
            l, r = 0, i-1
            while l < r:
                if nums[l] + nums[r] > c:
                    # Nếu nums[l] + nums[r] > c thì tất cả cặp (nums[l..r-1], nums[r]) đều hợp lệ
                    ans += r - l
                    r -= 1   # Giảm r để kiểm tra cặp nhỏ hơn
                else:
                    # Nếu nums[l] + nums[r] <= c thì tăng l để làm tổng lớn hơn
                    l += 1

        return ans
# ```

# ### 🔑 Ý tưởng chính:

# 1. **Sắp xếp mảng** để dễ so sánh.
# 2. Chọn cạnh lớn nhất `c = nums[i]`, sau đó dùng **hai con trỏ (l, r)** tìm số cặp `(a, b)` sao cho `a + b > c`.
# 3. Nếu `nums[0] + nums[1] > c` thì tất cả đều hợp lệ → dùng công thức tổ hợp tính nhanh.
# 4. Nếu `nums[i-2] + nums[i-1] < c` thì bỏ qua vì không có cặp nào đủ lớn.

# 👉 Thuật toán tối ưu hơn `O(n^3)` vì dùng **sort + two pointers**, độ phức tạp ~ `O(n^2)`.

# ---

# Bạn có muốn mình **vẽ hình minh họa với mảng ví dụ** (VD: `nums = [2, 2, 3, 4]`) để thấy rõ cách hai con trỏ lướt không?

# Rồi 👍 mình sẽ giải thích chi tiết thuật toán bạn đưa ra (nó là một phiên bản tối ưu hơn của cách `two pointers` bình thường).

# ---

# ## 🚩 Ý tưởng chính của bài toán

# Muốn đếm số bộ ba `(a, b, c)` tạo thành tam giác hợp lệ.
# Với mảng đã **sắp xếp tăng dần** (`nums`), ta luôn có `a ≤ b ≤ c`.
# Điều kiện tam giác rút gọn thành:

# ```
# a + b > c
# ```

# ---

# ## 🚀 Thuật toán trong code

# ```python
# class Solution:
#     def triangleNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)
#         ans = 0
# ```

# * **Sắp xếp mảng** để đảm bảo `a ≤ b ≤ c`.
# * `ans` là biến đếm số tam giác.

# ---

# ### 🔹 Vòng lặp chính (chọn cạnh lớn nhất `c`)

# ```python
# for i in range(n-1, 1, -1):
#     c = nums[i]
# ```

# * `c = nums[i]` là cạnh lớn nhất.
# * Ta cần chọn 2 cạnh nhỏ hơn từ `[0..i-1]`.

# ---

# ### 🔹 Trường hợp đặc biệt: tất cả đều tạo thành tam giác

# ```python
# if nums[0] + nums[1] > c:
#     ans += (i + 1) * (i) * (i-1) // 6
#     break
# ```

# * Nếu **hai cạnh nhỏ nhất** `nums[0] + nums[1] > c`,
#   → nghĩa là mọi cặp `(a, b)` trong `[0..i-1]` đều hợp lệ với `c`.
# * Khi đó, số cách chọn = **C(i+1, 3)** (chọn 3 số bất kỳ trong `[0..i]`).
# * Công thức:

#   ```
#   C(n,3) = n * (n-1) * (n-2) / 6
#   ```

#   với `n = i+1`.
# * `break` luôn vì các `c` nhỏ hơn sau này càng dễ thỏa mãn.

# ---

# ### 🔹 Trường hợp loại bỏ nhanh: không có tam giác

# ```python
# if nums[i-2] + nums[i-1] < c:
#     continue
# ```

# * Nếu **hai cạnh lớn nhất trong [0..i-1]** vẫn **nhỏ hơn hoặc bằng** `c`,
#   → thì không thể tạo tam giác với `c`.
# * Bỏ qua luôn (`continue`).

# ---

# ### 🔹 Trường hợp còn lại: dùng two pointers

# ```python
# l, r = 0, i-1
# while l < r:
#     if nums[l] + nums[r] > c:  # Nếu đủ lớn
#         ans += r - l
#         r -= 1
#     else:
#         l += 1
# ```

# * Giống như cách O(n²) chuẩn:

#   * Nếu `nums[l] + nums[r] > c`,
#     → tất cả cặp `(l..r-1, r)` đều hợp lệ.
#     → cộng `r-l`.
#     → dịch `r--` để thử cạnh nhỏ hơn.
#   * Nếu `nums[l] + nums[r] ≤ c`,
#     → cần số lớn hơn → dịch `l++`.

# ---

# ## ✅ Độ phức tạp

# * Trường hợp thường: **O(n²)** (giống two pointers).
# * Trường hợp đặc biệt (khi mọi cặp đều hợp lệ): chỉ tính toán C(n,3) 1 lần → rất nhanh.

# ---

# ## 🔎 Ví dụ minh họa

# Input:

# ```
# nums = [2, 2, 3, 4]
# ```

# * Sau sort: `[2,2,3,4]`

# 1. `i=3`, `c=4`

#    * `nums[0]+nums[1] = 2+2 = 4` **không > c** → bỏ qua trường hợp đặc biệt.
#    * `nums[1]+nums[2] = 2+3 = 5 > 4` → không bỏ qua.
#    * Two pointers:

#      * `l=0, r=2`: `2+3=5 > 4` → cộng `(2-0)=2` → ans=2 → `r=1`
#      * `l=0, r=1`: `2+2=4 ≤ 4` → `l=1` → dừng.

# 2. `i=2`, `c=3`

#    * `nums[0]+nums[1]=2+2=4 > 3` → trường hợp đặc biệt →
#      cộng C(3,3)=1 → ans=3.
#    * break luôn.

# → Kết quả: `3` (tam giác hợp lệ là `(2,2,3)`, `(2,3,4)`, `(2,3,4)`).

# ---

# 👉 Thuật toán này **thông minh hơn O(n²) thuần túy** vì có thể dùng **công thức tổ hợp** để tính nhanh trong trường hợp thuận lợi.

# ---

# Bạn có muốn mình viết lại **phiên bản Java tương ứng** với cách tối ưu này không?


# # import java.util.*;

# # public class b48 {
# #     static Scanner sc = new Scanner(System.in);

# #     public static void main(String[] args) {

# #         int n = sc.nextInt();
# #         int[] nums = new int[n];
# #         for (int i = 0; i < n; i++) {
# #             nums[i] = sc.nextInt();
# #         }

# #         int result = triangleNumber(nums);
# #         System.out.println(result);

# #         sc.close();
# #     }

# #     // Hàm chính: đếm số tam giác hợp lệ
# #     public static int triangleNumber(int[] nums) {
# #         // Bước 1: sắp xếp mảng
# #         Arrays.sort(nums);
# #         int n = nums.length;
# #         int count = 0;

# #         // Bước 2: chọn nums[k] làm cạnh lớn nhất, duyệt từ cuối về
# #         for (int k = n - 1; k >= 2; k--) {
# #             int i = 0, j = k - 1; // i: nhỏ nhất, j: ngay trước k

# #             // Dùng 2 con trỏ để tìm cặp (i, j)
# #             while (i < j) {
# #                 // Nếu nums[i] + nums[j] > nums[k]
# #                 if (nums[i] + nums[j] > nums[k]) {
# #                     // Thì tất cả cặp (i..j-1, j) đều hợp lệ
# #                     count += (j - i);
# #                     j--; // giảm j để thử cặp nhỏ hơn
# #                 } else {
# #                     i++; // tăng i để làm tổng lớn hơn
# #                 }
# #             }
# #         }
# #         return count;
# #     }
# # }

# # // Ok mình sẽ giải thích thật chi tiết thuật toán trong code trên 👇

# # // ---

# # // ## 🚩 Bài toán nhắc lại

# # // Cho một mảng `nums`, ta cần đếm số bộ ba `(a, b, c)` sao cho chúng tạo thành
# # // **tam giác hợp lệ**.
# # // Điều kiện tam giác:

# # // ```
# # // a + b > c
# # // a + c > b
# # // b + c > a
# # // ```

# # // Nếu ta **sắp xếp mảng tăng dần**, thì với `a ≤ b ≤ c`, chỉ cần kiểm tra:

# # // ```
# # // a + b > c
# # // ```

# # // là đủ, vì 2 điều kiện còn lại chắc chắn đúng.

# # // ---

# # // ## 🚀 Thuật toán (Sort + Two Pointers)

# # // 1. **Sort mảng**

# # // * `Arrays.sort(nums);`
# # // * Giúp ta áp dụng quy tắc `a ≤ b ≤ c`.

# # // 2. **Chọn cạnh lớn nhất (c)**

# # // * Duyệt từ cuối mảng về đầu: `for (int k = n - 1; k >= 2; k--)`
# # // * `nums[k]` là cạnh lớn nhất.

# # // 3. **Dùng hai con trỏ tìm a và b**

# # // * `i = 0` (bắt đầu), `j = k - 1` (ngay trước k).
# # // * Xét `nums[i] + nums[j] > nums[k]`:

# # // * Nếu **đúng** → tất cả cặp `(i..j-1, j)` đều hợp lệ (vì mảng đã sort, nên
# # // bất kỳ `nums[i’]` với `i ≤ i’ < j` đều ≥ nums[i], do đó `nums[i’] + nums[j] >
# # // nums[k]` vẫn đúng).
# # // → cộng `(j - i)` vào kết quả.
# # // → giảm `j--` để thử cặp nhỏ hơn.
# # // * Nếu **sai** → nghĩa là `nums[i] + nums[j] ≤ nums[k]`, thì ta cần tăng `i++`
# # // để có tổng lớn hơn.

# # // 4. **Trả về tổng số bộ ba**.

# # // ---

# # // ## 🔎 Ví dụ minh họa

# # // Input:

# # // ```
# # // nums = [2, 2, 3, 4]
# # // ```

# # // * Sau sort: `[2, 2, 3, 4]`

# # // ### Vòng lặp 1: `k = 3`, `nums[k] = 4`

# # // * `i = 0, j = 2`

# # // * `nums[i] + nums[j] = 2 + 3 = 5 > 4` → hợp lệ
# # // → thêm `j - i = 2` (cặp `(2,3,4)` và `(2,3,4)` với 2 ở vị trí khác).
# # // → `count = 2`
# # // → `j-- = 1`
# # // * `i = 0, j = 1`

# # // * `2 + 2 = 4` **không > 4** → tăng `i = 1`
# # // * Kết thúc vòng này.

# # // ### Vòng lặp 2: `k = 2`, `nums[k] = 3`

# # // * `i = 0, j = 1`

# # // * `2 + 2 = 4 > 3` → hợp lệ
# # // → thêm `1`
# # // → `count = 3`
# # // → `j-- = 0` → dừng.

# # // ---

# # // ## ✅ Kết quả

# # // Có **3 tam giác hợp lệ**:

# # // * `(2, 3, 4)` (từ 2 đầu tiên)
# # // * `(2, 3, 4)` (từ 2 thứ hai)
# # // * `(2, 2, 3)`

# # // ---

# # // 👉 Thuật toán này chạy trong **O(n²)** thay vì **O(n³)** (duyệt 3 vòng lồng
# # // nhau).

# # // ---

# # // Bạn có muốn mình **vẽ sơ đồ hai con trỏ i, j di chuyển** trên mảng đã sắp xếp
# # // để dễ hình dung hơn không?

# # // Ok, mình giải thích chi tiết bài **LeetCode 611. Valid Triangle Number** nhé
# # // 🚀

# # // ---

# # // ### 📌 Đề bài

# # // Cho một mảng số nguyên dương `nums`.
# # // Hãy **đếm số bộ ba (i, j, k)** (với `i < j < k`) sao cho `nums[i], nums[j],
# # // nums[k]` có thể tạo thành **một tam giác hợp lệ**.

# # // ---

# # // ### 📐 Điều kiện tam giác hợp lệ

# # // Với 3 cạnh `a, b, c`, điều kiện là:

# # // ```
# # // a + b > c
# # // a + c > b
# # // b + c > a
# # // ```

# # // 👉 Nếu ta **sắp xếp mảng tăng dần** (`a ≤ b ≤ c`) thì chỉ cần kiểm tra:

# # // ```
# # // a + b > c
# # // ```

# # // vì điều này tự động đảm bảo 2 bất đẳng thức còn lại.

# # // ---

# # // ### 🔎 Ví dụ

# # // #### Input:

# # // ```
# # // nums = [2, 2, 3, 4]
# # // ```

# # // #### Các bộ ba:

# # // * (2, 2, 3) → 2 + 2 > 3 ✅
# # // * (2, 3, 4) → 2 + 3 > 4 ✅
# # // * (2, 2, 4) → 2 + 2 > 4 ❌
# # // * (2, 3, 4) → đã tính
# # // * (2, 2, 3) → đã tính

# # // 👉 Kết quả = **3** bộ tam giác hợp lệ.

# # // ---

# # // ### 🧠 Ý tưởng giải

# # // 1. **Sort mảng** trước.
# # // 2. Dùng **2-pointer** để đếm số cặp `(i, j)` thỏa điều kiện với mỗi `k` (là
# # // cạnh lớn nhất).

# # // Cụ thể:

# # // * Fix `k` (cạnh lớn nhất).
# # // * Dùng `i = 0`, `j = k - 1`.
# # // * Nếu `nums[i] + nums[j] > nums[k]` → tất cả các cặp `(i ... j-1, j)` đều hợp
# # // lệ (vì mảng sort rồi).
# # // * Ngược lại → tăng `i` để tìm cặp lớn hơn.

# # // ---

# # // ### ⏱️ Độ phức tạp

# # // * Sắp xếp: `O(n log n)`
# # // * Duyệt + 2-pointer: `O(n^2)`
# # // 👉 Tổng: `O(n^2)` (tốt hơn brute force `O(n^3)`).

# # // ---

# # // 👉 Bạn có muốn mình viết luôn code Python tối ưu cho bài này không?
