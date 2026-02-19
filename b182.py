# ## 🧠 Giải thích đề bài: **Binary Number with Alternating Bits**(18/02/2026)

# ### 1️⃣ Đề bài yêu cầu gì?


# Ok 👍 mình sẽ giải thích **ý tưởng thuật toán bit manipulation** này thật dễ hiểu rồi thêm **chú thích trực tiếp vào code** cho bạn.

# ---

# # 1️⃣ Ý tưởng chính của thuật toán

# Ta cần kiểm tra:

# > Binary của `n` có dạng xen kẽ 101010… hay không?

# Ví dụ:

# * 5 = `101` → xen kẽ
# * 10 = `1010` → xen kẽ
# * 7 = `111` → không

# ---

# ## 🔑 Trick quan trọng

# Nếu một số **có bit xen kẽ**, thì khi ta làm:

# ```
# n ^ (n >> 1)
# ```

# Kết quả sẽ là **dãy toàn bit 1 liên tiếp**.

# ---

# ### Vì sao?

# Ví dụ n = 10

# ```
# n        = 1010
# n >> 1   = 0101
# XOR      = 1111
# ```

# Vì:

# * 1 ^ 0 = 1
# * 0 ^ 1 = 1

# → toàn 1

# ---

# Ví dụ n = 5

# ```
# 101
# 010
# ---
# 111
# ```

# Cũng toàn 1.

# ---

# ### Nhưng nếu KHÔNG xen kẽ?

# Ví dụ n = 7

# ```
# 111
# 011
# ---
# 100
# ```

# Không phải toàn 1 ❌

# ---

# # 2️⃣ Kiểm tra “toàn bit 1” bằng mẹo

# Một số dạng:

# ```
# 1
# 11
# 111
# 1111
# ```

# Có tính chất:

# ```
# x & (x + 1) == 0
# ```

# ---

# Ví dụ:

# ```
# x = 1111 (15)
# x+1 = 10000 (16)

# AND:
# 01111
# 10000
# ------
# 00000 → = 0
# ```

# Luôn đúng với dãy toàn 1.

# ---

# # 3️⃣ Ghép lại thành thuật toán

# Bước:

# 1. XOR với số dịch phải 1 bit
# 2. Kiểm tra kết quả có phải toàn bit 1 không

# ---

# # 4️⃣ Code có chú thích chi tiết

# ```python
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Bước 1:
        # Dịch phải n 1 bit
        # Ví dụ: 1010 >> 1 = 0101
        shifted = n >> 1
        
        # XOR n với shifted
        # Nếu n có bit xen kẽ → kết quả sẽ là toàn bit 1
        # Ví dụ:
        #   1010
        # ^ 0101
        # = 1111
        n = n ^ shifted
        
        # Bước 2:
        # Kiểm tra n có phải dạng toàn bit 1 không
        #
        # Số dạng:
        #   1, 11, 111, 1111...
        # luôn thỏa:
        #   x & (x + 1) == 0
        #
        # Ví dụ:
        #   1111 & 10000 = 0
        return (n & (n + 1)) == 0
# ```

# ---

# # 5️⃣ Minh họa chạy từng bước

# Ví dụ n = 10

# ```
# n        = 1010
# n >> 1   = 0101
# XOR      = 1111
# ```

# Kiểm tra:

# ```
# 1111
# 10000
# -----
# 0000 → True
# ```

# → Có alternating bits ✅

# ---

# Ví dụ n = 7

# ```
# 111
# 011
# ---
# 100
# ```

# Kiểm tra:

# ```
# 100
# 101
# ---
# 100 ≠ 0 → False
# ```

# ---

# # 6️⃣ Độ phức tạp

# * Time: **O(1)** (bit operation)
# * Space: **O(1)**

# Nhanh hơn cách:

# * Convert sang string binary
# * Duyệt từng bit

# ---

# # 7️⃣ Tóm tắt mẹo nhớ nhanh

# ```
# Alternating bits
# → XOR với (n >> 1)
# → Nếu ra toàn 1
# → return True
# ```

# ---

# Nếu bạn muốn mình có thể:

# * Viết lại bằng **Java / C++**
# * So sánh với cách dùng **string**
# * Hoặc vẽ bit diagram step-by-step dễ nhớ khi đi thi 🚀


# Bạn được cho **một số nguyên dương `n`**.
# Nhiệm vụ: kiểm tra xem **dạng nhị phân (binary)** của `n` có phải là **các bit xen kẽ nhau** hay không.

# 👉 “Xen kẽ” nghĩa là:

# * Bit 0 rồi đến bit 1 rồi lại 0 rồi 1…
# * Hoặc 1 → 0 → 1 → 0…

# Không được có **2 bit giống nhau đứng cạnh nhau**.

# ---

# ### 2️⃣ Ví dụ dễ hiểu

# | n (thập phân) | Binary | Kết quả | Giải thích     |
# | ------------- | ------ | ------- | -------------- |
# | 5             | 101    | ✅ True  | 1–0–1 xen kẽ   |
# | 7             | 111    | ❌ False | 1–1 trùng nhau |
# | 10            | 1010   | ✅ True  | Xen kẽ         |
# | 11            | 1011   | ❌ False | Có 11 cuối     |

# ---

# ### 3️⃣ Minh họa trực quan

# #### Ví dụ 1: n = 5

# * 5 → Binary = **101**
# * Các bit: 1 ≠ 0 ≠ 1 → Xen kẽ → **Đúng**

# ---

# #### Ví dụ 2: n = 7

# * 7 → Binary = **111**
# * Có 1 đứng cạnh 1 → **Không xen kẽ** → Sai

# ---

# ### 4️⃣ Hiểu bản chất bài toán

# Thực chất đề chỉ hỏi:

# > Khi viết `n` dưới dạng nhị phân,
# > có tồn tại 2 bit liên tiếp giống nhau không?

# * Nếu **có** → False
# * Nếu **không** → True

# ---

# ### 5️⃣ Cách nghĩ nhanh khi làm bài

# Ví dụ: n = 10

# * 10 → chia 2:

#   * 10 / 2 = 5 dư 0
#   * 5 / 2 = 2 dư 1
#   * 2 / 2 = 1 dư 0
#   * 1 / 2 = 0 dư 1
#     → Binary = **1010** → Xen kẽ → True

# ---

# ### 6️⃣ Tóm tắt ngắn gọn

# * Đổi số `n` sang **binary**
# * Kiểm tra từng bit kế nhau:

#   * Nếu giống nhau → Sai
#   * Nếu luôn khác → Đúng

# ---

# Nếu bạn muốn, mình có thể:

# * Giải bằng **bit manipulation** (XOR trick rất hay)
# * Viết code **Java / C++ / Python**
# * Hoặc vẽ flow tư duy để dễ nhớ khi đi thi 👍
