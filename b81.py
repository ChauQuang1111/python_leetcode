# 3370. Smallest Number With All Set Bits(29/10/2025)
# Bài **3370. Smallest Number With All Set Bits** (LeetCode) là một bài **toán bit manipulation** — thao tác trên bit.
# Mình sẽ giải thích **đề bài, ví dụ, và tư duy thuật toán** thật dễ hiểu nhé 👇
class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1  # Bắt đầu với số nhỏ nhất có tất cả bit bằng 1 (1)
        
        # Lặp cho đến khi x >= n
        while x < n:
            # (x << 1): dịch trái 1 bit => nhân đôi số x
            # | 1: bật bit cuối cùng thành 1 => tạo thêm 1 bit '1' ở cuối
            x = (x << 1) | 1
        
        return x  # Kết quả nhỏ nhất >= n mà có tất cả bit bằng 1

# ---

# ### 🧩 **Đề bài**

# Bạn được cho một số nguyên **n**.
# Hãy **tìm số nguyên nhỏ nhất m ≥ n**, sao cho **m có tất cả các bit trong biểu diễn nhị phân đều là 1**.

# Nói cách khác:

# * Hãy tìm **số lớn nhất dạng 1, 3, 7, 15, 31, 63, 127, ...** (tức là dạng `2^k - 1`)
# * mà **≥ n**.

# ---

# ### 🧠 **Giải thích chi tiết**

# Số có **tất cả bit bằng 1** trong nhị phân có dạng:

# ```
# 1  -> 1 (2^1 - 1)
# 3  -> 11 (2^2 - 1)
# 7  -> 111 (2^3 - 1)
# 15 -> 1111 (2^4 - 1)
# 31 -> 11111 (2^5 - 1)
# ...
# ```

# 👉 Mỗi số dạng đó là `2^k - 1`.

# ---

# ### 🧮 **Mục tiêu**

# Tìm **nhỏ nhất k** sao cho `2^k - 1 >= n`.

# ---

# ### 🔍 **Ví dụ**

# #### Ví dụ 1:

# ```
# Input: n = 6
# ```

# * Các số dạng `2^k - 1` là:
#   1, 3, 7, 15, 31, ...
# * Ta thấy:
#   7 ≥ 6 → ✅
#   Nhưng 3 < 6 → ❌
#   ⇒ **Kết quả = 7**

# #### Ví dụ 2:

# ```
# Input: n = 19
# ```

# * Các số dạng `2^k - 1` là:
#   1, 3, 7, 15, 31, 63...
# * 15 < 19 → ❌
# * 31 ≥ 19 → ✅
#   ⇒ **Kết quả = 31**

# ---

# ### ⚙️ **Thuật toán**

# ```java
# public int smallestNumberWithAllBitsSet(int n) {
#     int x = 1;
#     while (x < n) {
#         x = (x << 1) | 1; // nhân 2 rồi cộng 1 -> tạo bit 1 mới
#     }
#     return x;
# }
# ```

# #### 🔍 Giải thích dòng `x = (x << 1) | 1`

# * Dịch trái (<< 1): nhân đôi số hiện tại, thêm một bit 0 bên phải.
# * `| 1`: bật bit đó thành 1.
# * Kết quả: thêm một bit 1 vào cuối dãy bit 1 có sẵn.

# Ví dụ từng bước với `n = 6`:

# ```
# x = 1  (1)
# x = 3  (11)
# x = 7  (111) -> dừng lại vì 7 >= 6
# ```

# ---

# 👉 **Tóm tắt:**

# * Dạng số cần tìm: `2^k - 1`
# * Duyệt tăng dần k đến khi `2^k - 1 ≥ n`
# * Trả về kết quả đó.

# ---

# Bạn có muốn mình viết lại lời giải này bằng **Python hoặc C++** (kèm chú thích từng dòng) để dễ hiểu hơn không?
