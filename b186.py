# ## 📌 Binary Gap (22/02/2026)


# Bài **868. Binary Gap** yêu cầu:

# > Tìm khoảng cách lớn nhất giữa **hai bit 1 liên tiếp** trong biểu diễn nhị phân của số `n`.

# ⚠️ Lưu ý:
# Binary Gap trong bài 868 = **khoảng cách giữa hai bit 1 liên tiếp** (tính cả vị trí),
# khác với bài Codility (đếm số 0 ở giữa).

# ---

# ## 🔎 Ý tưởng thuật toán

# Ta duyệt từng bit từ phải sang trái:

# * Nếu gặp `1`:

#   * Cập nhật khoảng cách lớn nhất
#   * Reset biến đếm
# * Nếu gặp `0`:

#   * Tăng biến đếm khoảng cách

# ---

# ## 🧠 Giải thích từng dòng code

# Dưới đây là code của bạn, mình thêm chú thích chi tiết:

# ```python
class Solution:
    def binaryGap(self, n: int) -> int:
        # Nếu n là lũy thừa của 2 (chỉ có 1 bit 1 duy nhất)
        # Ví dụ: 8 = 1000, 16 = 10000
        # Thì không có hai bit 1 nào → return 0
        if (n & (n - 1)) == 0:
            return 0

        # n & -n lấy bit 1 phải nhất (lowest set bit)
        # Ví dụ: n = 20 (10100)
        # n & -n = 4 (00100)
        # n //= 4 → bỏ hết số 0 phía sau
        # Giúp bắt đầu từ bit 1 đầu tiên bên phải
        n //= n & -n

        max_gap = 0  # khoảng cách lớn nhất
        gap = 0      # khoảng cách hiện tại giữa 2 bit 1

        while n:
            if n & 1:  # nếu bit cuối là 1
                # cập nhật khoảng cách lớn nhất
                max_gap = max(max_gap, gap)
                gap = 0  # reset đếm
            else:
                # nếu là bit 0 thì tăng khoảng cách
                gap += 1

            # dịch phải 1 bit (bỏ bit vừa xét)
            n >>= 1

        # +1 vì gap chỉ đếm số bit giữa 2 bit 1
        # còn bài yêu cầu tính khoảng cách vị trí
        return max_gap + 1


## 📌 Ví dụ minh họa

# Ví dụ: `n = 22`

# 22 = `10110`

# Các vị trí bit 1:

# * vị trí 1
# * vị trí 2
# * vị trí 4

# Khoảng cách:

# * giữa vị trí 1 và 2 = 1
# * giữa vị trí 2 và 4 = 2

# ➡ Kết quả = **2**

# ---

# ## 🎯 Phân tích kỹ thuật

# ### 1️⃣ `(n & (n - 1)) == 0`

# Kiểm tra n có phải lũy thừa của 2 không.

# Vì:

# ```
# 1000
# 0111
# ----
# 0000
# ```

# Nếu chỉ có 1 bit 1 → không có cặp nào → return 0.

# ---

# ### 2️⃣ `n & -n`

# Lấy **bit 1 phải nhất**.

# Ví dụ:

# ```
# n = 1011000
# -n = 0101000 (two's complement)
# n & -n = 0001000
# ```

# Giúp loại bỏ số 0 phía sau để bắt đầu tính từ bit 1 đầu tiên.

# ---

# ### 3️⃣ `n >>= 1`

# Dịch phải để duyệt từng bit.
# Giống như chia 2 liên tục.

# ---

# ## ⏱ Độ phức tạp

# * Time Complexity: **O(log n)**
# * Space Complexity: **O(1)**

# ---

# Nếu bạn muốn mình:

# * So sánh với cách làm không dùng bitwise
# * Hoặc viết lại phiên bản dễ hiểu hơn
# * Hoặc phân tích sâu phần `n & -n`

# thì nói mình biết nhé 🚀


# **Binary Gap** (khoảng cách nhị phân) là:

# > **Số lượng số 0 liên tiếp dài nhất nằm giữa hai số 1 trong biểu diễn nhị phân của một số nguyên dương.**

# ---

# ## 🧠 Hiểu đơn giản

# 1. Đổi số từ hệ thập phân sang **hệ nhị phân (binary)**.
# 2. Tìm các đoạn **0 liên tiếp**.
# 3. Chỉ tính các đoạn **0 nằm giữa hai số 1**.
# 4. Lấy độ dài lớn nhất trong các đoạn đó.

# ---

# ## 🔎 Ví dụ minh họa

# ### Ví dụ 1: N = 9

# * 9 trong nhị phân = **1001**
# * Có 2 số 0 nằm giữa hai số 1
#   ➡ Binary Gap = **2**

# ---

# ### Ví dụ 2: N = 529

# * 529 trong nhị phân = **1000010001**
# * Các khoảng 0:

#   * 4 số 0
#   * 3 số 0
# * Lớn nhất là 4
#   ➡ Binary Gap = **4**

# ---

# ### Ví dụ 3: N = 20

# * 20 trong nhị phân = **10100**
# * Có 1 số 0 giữa hai số 1
# * Hai số 0 cuối KHÔNG tính (vì không có số 1 phía sau)

# ➡ Binary Gap = **1**

# ---

# ### Ví dụ 4: N = 15

# * 15 trong nhị phân = **1111**
# * Không có số 0 nào giữa hai số 1

# ➡ Binary Gap = **0**

# ---

# ## ❗ Lưu ý quan trọng

# ✅ Chỉ tính số 0 **nằm giữa hai số 1**
# ❌ Không tính số 0 ở cuối dãy
# ❌ Không tính số 0 ở đầu dãy

# ---

# ## 🎯 Tóm lại đề bài yêu cầu gì?

# Cho một số nguyên dương N:

# 1. Đổi N sang nhị phân.
# 2. Tìm đoạn 0 liên tiếp dài nhất nằm giữa hai số 1.
# 3. Trả về độ dài đoạn đó.

# ---

# Nếu bạn muốn mình giải thích luôn cách code (Java / Python) hoặc phân tích độ phức tạp thì nói mình biết nhé 🚀
