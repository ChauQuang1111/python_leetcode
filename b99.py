# 1513. Number of Substrings With Only 1s(16/11/2025)
# Dưới đây là **giải thích đề bài LeetCode 1513 — Number of Substrings With Only 1s** thật dễ hiểu và ngắn gọn.
# Dưới đây là **giải thích thuật toán + phiên bản code có chú thích đầy đủ**.

# ---

# # ✅ **Giải thích thuật toán**

# Ý tưởng:

# 1. Tách chuỗi `s` theo ký tự `'0'`
#    → Mỗi phần trong `s.split('0')` là **đoạn gồm toàn ký tự '1'**.

#    Ví dụ:
#    `"110111"` → `["11", "", "111"]`

# 2. Với mỗi đoạn `part` có độ dài `n`, số substring toàn `'1'` là:

# [
# \frac{n(n+1)}{2}
# ]

# 3. Tác giả viết:

# ```
# cnt += n*(n+1)
# ```

# sau đó cuối cùng `cnt // 2` để hoàn tất công thức.

# 4. Trả về kết quả theo modulo (10^9 + 7).

# ---

# # ✅ **Code có chú thích rõ ràng**

# ```python
class Solution:
    def numSub(self, s: str) -> int:
        cnt = 0

        # Tách chuỗi theo ký tự '0'
        # Mỗi phần thu được là một đoạn toàn '1'
        for part in s.split('0'):
            n = len(part)  # độ dài đoạn gồm toàn '1'

            # Số substring toàn '1' của một đoạn:
            # n * (n + 1) / 2
            # Ở đây tính n*(n+1) trước, chia 2 sau.
            cnt += n * (n + 1)

        # Chia 2 theo công thức và mod 1e9+7
        return (cnt // 2) % (10**9 + 7)
# ```

# ---

# # 🔍 Ví dụ minh họa

# `s = "0110111"`

# `s.split('0')` → `["", "11", "111"]`

# * `"11"` → n = 2 → 2*3/2 = 3
# * `"111"` → n = 3 → 3*4/2 = 6
#   → Tổng = **9**

# ---


# ---

# # ✅ **📌 ĐỀ BÀI: Number of Substrings With Only 1s**

# Bạn được cho một chuỗi nhị phân **s** (chỉ gồm `'0'` và `'1'`).

# **Yêu cầu:**
# 👉 Đếm số **substring** (chuỗi con liên tiếp) mà **chỉ chứa toàn ký tự '1'**, không có bất kỳ '0' nào.

# ---

# # 🔍 Ví dụ

# ### **Ví dụ 1**

# ```
# Input: s = "0110111"
# Output: 9
# ```

# Giải thích:

# Các đoạn gồm toàn `1` là:

# | Đoạn  | Số substring chỉ chứa '1'          |
# | ----- | ---------------------------------- |
# | "11"  | 3 -> ("1", "1", "11")              |
# | "111" | 6 -> ("1","1","1","11","11","111") |

# Tổng cộng: **3 + 6 = 9**

# ---

# # 🧠 Ý TƯỞNG GIẢI

# Chuỗi liên tiếp gồm `k` ký tự '1':

# ```
# "111...1" (k lần)
# ```

# sẽ tạo được:

# 👉 **k*(k+1)/2** substrings toàn '1'.

# Ví dụ "111" → 3*(3+1)/2 = 6.

# ---

# # ✨ CÁCH LÀM

# 1. Duyệt chuỗi
# 2. Mỗi khi gặp chuỗi liên tiếp gồm `k` ký tự '1', cộng vào kết quả:

#    ```
#    k*(k+1)/2
#    ```
# 3. Reset đếm nếu gặp '0'.

# ---

# # ✔️ Code mẫu Python

# ```python
# class Solution:
#     def numSub(self, s: str) -> int:
#         res = 0
#         count = 0
#         mod = 10**9 + 7
        
#         for c in s:
#             if c == '1':
#                 count += 1
#             else:
#                 res += count * (count + 1) // 2
#                 count = 0
        
#         res += count * (count + 1) // 2
#         return res % mod
# ```

# ---

# # 📌 Tổng kết

# * Tách chuỗi thành các đoạn liên tiếp `111…1`
# * Với độ dài k → có `k*(k+1)/2` substring toàn ‘1’
# * Lặp lại cho tất cả các đoạn

# ---

# Nếu bạn muốn, mình có thể:

# ✅ minh họa bằng hình
# ✅ viết code Java
# ✅ giải thích thêm về độ phức tạp

# Bạn muốn tiếp phần nào?
