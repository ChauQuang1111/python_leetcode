# # Reverse Bits (16/02/2026)

# Ok, mình sẽ **chú thích trực tiếp vào code** + giải thích thuật toán theo kiểu dễ hiểu nhất 👇

# ---

# ## 🧾 Code đã chú thích

# ```python
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0          # Biến lưu kết quả sau khi đảo bit

        for i in range(32):   # Vì đề bài cho số 32-bit → lặp đúng 32 lần

            # B1: Dịch trái result 1 bit
            # -> Tạo chỗ trống ở cuối để gắn bit mới vào
            result = (result << 1)

            # B2: Lấy bit cuối của n (0 hoặc 1)
            # n & 1 sẽ trả về bit phải nhất của n
            last_bit = n & 1

            # B3: Gắn bit vừa lấy vào result
            # Dùng OR để thêm bit vào cuối
            result = result | last_bit

            # B4: Dịch phải n để xử lý bit tiếp theo
            n = n >> 1

        return result
# ```

# ---

# ## 🔍 Giải thích từng phép toán bit

# ### 1️⃣ `n & 1` — Lấy bit cuối

# Ví dụ:

# ```
# n = 10110
#         &
#         00001
#       = 00000  → bit cuối = 0
# ```

# Nếu:

# ```
# n = 10111
        # &
#         00001
#       = 00001  → bit cuối = 1
# ```

# 👉 Dùng để “bóc” từng bit từ phải sang trái.

# ---

# ### 2️⃣ `result << 1` — Dịch trái

# Ví dụ:

# ```
# result = 101
# result << 1 → 1010
# ```

# Ý nghĩa:

# * Nhân đôi số
# * Tạo chỗ trống ở cuối để nhét bit mới vào

# ---

# ### 3️⃣ `result | last_bit` — Gắn bit vào

# Ví dụ:

# ```
# result = 1010
# last_bit = 1

# 1010
# OR 0001
# = 1011
# ```

# ---

# ## 🔄 Thuật toán hoạt động thế nào?

# Ta đang làm đúng kiểu:

# > Lấy bit cuối của n → gắn vào đầu result

# Nhưng vì không thể “gắn đầu”, nên ta:

# 1. Dịch trái result
# 2. Nhét bit vào cuối

# Lặp lại → sẽ thành đảo ngược.

# ---

## 🧠 Trace ví dụ nhỏ (8 bit cho dễ nhìn)

# Giả sử:

# ```
# n = 00010110
# ```

# | Lần | result (sau khi gắn) | n (sau shift) |
# | --- | -------------------- | ------------- |
# | 1   | 0                    | 00001011      |
# | 2   | 1                    | 00000101      |
# | 3   | 10                   | 00000010      |
# | 4   | 101                  | 00000001      |
# | 5   | 1011                 | 00000000      |
# | ... | ...                  | ...           |

# Cuối cùng:

# ```
# 01101000
# ```

# → Đã đảo bit.

# ---

# ## 📌 Tóm tắt thuật toán

# **Input:** số 32 bit
# **Process:**

# Lặp 32 lần:

# 1. Lấy bit cuối `n & 1`
# 2. Dịch trái result
# 3. Gắn bit vào result
# 4. Dịch phải n

# **Output:** result = số đã đảo bit

# ---

# ## 💡 Độ phức tạp

# * Time: `O(32)` → coi như `O(1)`
# * Space: `O(1)`

# Vì số bit cố định.

# ---

# Nếu bạn muốn mình:

# * Vẽ sơ đồ từng bước 32 bit
# * So sánh với cách dùng string
# * Giải thích vì sao phải lặp 32 thay vì đến khi n = 0

# Cứ nói mình biết 👍


# ---

# ## 🧠 Ý nghĩa đề bài Reverse Bits

# **Yêu cầu:**
# Cho một số nguyên không dấu 32-bit `n`, hãy **đảo ngược thứ tự các bit** của nó và trả về số mới.

# Nói đơn giản:

# > Bit ở đầu → xuống cuối
# > Bit ở cuối → lên đầu

# ---

# ## 📌 Ví dụ minh họa

# ### Ví dụ 1

# Input:

# ```
# n = 00000010100101000001111010011100
# ```

# Đây là biểu diễn **32 bit** của số nguyên.

# Sau khi đảo bit:

# ```
# 00111001011110000010100101000000
# ```

# Output (dạng thập phân):

# ```
# 964176192
# ```

# ---

# ## 👀 Hình dung trực quan

# ---

# ## 🔄 Nguyên lý đảo bit

# Giả sử có chuỗi bit:

# ```
# abcde
# ```

# Đảo lại thành:

# ```
# edcba
# ```

# Với 32 bit cũng vậy — chỉ là dài hơn thôi.

# ---

# ## 🧮 Ví dụ nhỏ cho dễ hiểu (8 bit)

# Giả sử:

# ```
# n = 00010110   (22)
# ```

# Đảo lại:

# ```
# 01101000   (104)
# ```

# ---

# ## ⚙️ Cách máy tính làm

# Thường làm theo quy trình:

# 1. Lấy bit cuối của `n` (`n & 1`)
# 2. Dịch trái kết quả (`res << 1`)
# 3. Gắn bit vừa lấy vào
# 4. Dịch phải `n` (`n >> 1`)
# 5. Lặp 32 lần

# ---

# ## 📌 Tóm tắt đề bài

# * Input: số nguyên **không dấu 32 bit**
# * Task: đảo ngược thứ tự **từng bit**
# * Output: số mới sau khi đảo

# ---

# Nếu bạn muốn, mình có thể:

# * Giải thích code Java / C++ / Python
# * Trace từng bước bằng ví dụ của bạn
# * Giải thích vì sao phải dùng `<<` và `>>`

# Cứ gửi code hoặc phần bạn chưa hiểu 👍
