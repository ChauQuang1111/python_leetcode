# 1611. Minimum One Bit Operations to Make Integers Zero (08/11/2025)
# Dưới đây là **code Python hoàn chỉnh** cho bài **1611. Minimum One Bit Operations to Make Integers Zero**,
# kèm theo **giải thích chi tiết từng dòng** 👇

# ---

# ### ✅ Code hoàn chỉnh (cách đệ quy)

# ```python
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # Trường hợp cơ bản: nếu n = 0 thì không cần thao tác nào
        if n == 0:
            return 0
        
        # Tìm vị trí bit cao nhất (most significant bit)
        # Ví dụ: n = 13 (1101₂) -> bit_length = 4 -> k = 3
        k = n.bit_length() - 1
        
        # Đệ quy theo công thức:
        # f(n) = (2^(k+1) - 1) - f(n ^ (1 << k))
        # (1 << (k+1)) - 1 => tạo số có tất cả bit từ 0..k là 1
        # n ^ (1 << k) => tắt bit cao nhất của n
        return (1 << (k + 1)) - 1 - self.minimumOneBitOperations(n ^ (1 << k))
# ```

# ---

# ### 🔍 Ví dụ minh họa: `n = 6 (110₂)`

# | Bước | n                | bit cao nhất `k` | Công thức                  | Kết quả |
# | ---- | ---------------- | ---------------- | -------------------------- | ------- |
# | 1    | 6                | 2                | (2³−1) − f(6−4) = 7 − f(2) | ?       |
# | 2    | 2                | 1                | (2²−1) − f(2−2) = 3 − f(0) | 3       |
# | 3    | f(6) = 7 − 3 = 4 |                  |                            | ✅       |

# 👉 Kết quả: **4 thao tác**



# ### ⚙️ Độ phức tạp

# * **Thời gian:** O(log n) — vì mỗi lần đệ quy giảm 1 bit.
# * **Không gian:** O(log n) — do stack đệ quy.

# ---

### ⚡ Cách ngắn hơn (phi đệ quy)

# Đây là cách viết **dựa trên công thức Gray code** — nhanh hơn, không cần đệ quy:

# ```python
# class Solution:
#     def minimumOneBitOperations(self, n: int) -> int:
#         res = 0
#         while n:
#             res ^= n  # XOR dồn với n
#             n >>= 1   # Dịch phải 1 bit
#         return res


# 🧠 Ý tưởng:
# `res ^= n` mô phỏng quá trình chuyển đổi **Gray code → nhị phân**,
# và giá trị cuối cùng chính là **số thao tác cần thực hiện**.

# ---

# Bạn có muốn mình minh họa **chi tiết từng vòng while** trong cách thứ hai (phi đệ quy) không?
# Ví dụ với `n = 13 (1101₂)` để thấy rõ cách XOR hoạt động từng bước?


# Hãy cùng phân tích **từng bước** để bạn hiểu toàn bộ tư duy đằng sau nhé 👇

# ---

# ## 🎯 Đề bài

# Cho một số nguyên `n`.
# Mỗi lần thao tác, bạn có thể **đảo bit** ở vị trí `i` (0-based, tính từ phải sang trái),
# **nhưng chỉ khi** bit ở vị trí `i+1` (bên trái ngay cạnh nó) là **1**, và **tất cả các bit bên phải `i`** (nhỏ hơn i) đều **là 0**.

# Bạn cần tìm **số thao tác tối thiểu** để biến `n` thành `0`.

# ---

# ## 💡 Ví dụ

# ```
# n = 3 (binary = 011)
# ```

# Các bước:

# ```
# 011 → 001 → 000
# ```

# Kết quả: 2 bước.

# ---

# ## 🧩 Nhận xét quan trọng

# Bài này **không thể** giải bằng thao tác bit bình thường vì quy tắc bật/tắt bit khá phức tạp.
# Tuy nhiên, nếu ta quan sát kết quả cho vài số nhỏ — sẽ nhận ra **một quy luật rất giống mã Gray (Gray code)**.

# | n (decimal) | binary | min steps to 0 |
# | ----------- | ------ | -------------- |
# | 0           | 000    | 0              |
# | 1           | 001    | 1              |
# | 2           | 010    | 3              |
# | 3           | 011    | 2              |
# | 4           | 100    | 7              |
# | 5           | 101    | 6              |
# | 6           | 110    | 4              |
# | 7           | 111    | 5              |

# 🔎 Dễ thấy:
# `f(n)` **chính là** giá trị nhị phân của **Gray code đảo ngược**.

# Cụ thể:
# 👉 `f(n) = n ^ (n >> 1) ^ (n >> 2) ^ ...` cho tới khi `n = 0`.
# Hay viết gọn hơn:

# > **Gray code → integer conversion**
# > `grayToBinary(n) = n ^ (n >> 1) ^ (n >> 2) ^ ...`

# ---

# ## ✅ Thuật toán (Recursive)

# ### Ý tưởng

# Giả sử:

# * `f(n)` là số bước tối thiểu để biến `n` → `0`.
# * Nếu `n` = `0`, rõ ràng `f(0) = 0`.
# * Nếu `n` có bit cao nhất ở vị trí `k`, nghĩa là `n` nằm trong khoảng `[2^k, 2^{k+1})`.

# Công thức:

# ```
# f(n) = 2^{k+1} - 1 - f(n - 2^k)
# ```

# ### Giải thích:

# * `2^k` là số có duy nhất bit cao nhất bật lên.
# * `2^{k+1} - 1` là tất cả các bit từ 0..k đều bằng 1.
# * Quy luật: để tắt bit cao nhất, bạn cần phải "đảo" toàn bộ dãy bit nhỏ hơn nó —
#   nên phải đi qua tất cả trạng thái trong Gray code theo thứ tự đảo ngược.

# ---

# ## 🧮 Ví dụ minh họa

# Giả sử `n = 6 (110₂)`

# * bit cao nhất ở vị trí `k = 2` (`2^2 = 4`)
# * `n - 2^k = 6 - 4 = 2`

# Khi đó:

# ```
# f(6) = (2^{3} - 1) - f(2)
#      = 7 - f(2)
#      = 7 - 3
#      = 4
# ```

# ✅ Kết quả đúng như bảng trên.

# ---

# ## 🧠 Code Python

# ```python
# class Solution:
#     def minimumOneBitOperations(self, n: int) -> int:
#         if n == 0:
#             return 0
#         k = n.bit_length() - 1  # vị trí bit cao nhất
#         return (1 << (k + 1)) - 1 - self.minimumOneBitOperations(n ^ (1 << k))
# ```

# ---

# ## 💡 Giải thích code

# 1️⃣ `n.bit_length() - 1` → tìm vị trí bit cao nhất (MSB).
# 2️⃣ `(1 << (k + 1)) - 1` → tạo số có tất cả các bit từ 0..k bằng 1.
# 3️⃣ `n ^ (1 << k)` → tắt bit cao nhất của `n`.
# 4️⃣ Đệ quy để xử lý phần còn lại.

# ---

# ## ⏱️ Độ phức tạp

# * **Thời gian:** O(log n)
#   (mỗi lần giảm một bit)
# * **Không gian:** O(log n) (do đệ quy)

# ---

# ## 🧩 Cách khác (Bitwise trick)

# Nếu bạn muốn công thức *phi đệ quy*, có thể dùng Gray-code trick:

# ```python
# def minimumOneBitOperations(n: int) -> int:
#     res = 0
#     while n:
#         res ^= n
#         n >>= 1
#     return res
# ```

# 📘 Đây là cách nhanh nhất — chỉ cần duyệt qua các bit một lần.

# ---

# Bạn có muốn mình minh họa từng bước chạy **với ví dụ `n = 13 (1101₂)`** để thấy cách đệ quy hoạt động không?
