# 1262. Greatest Sum Divisible by Three(23/11/2025)
# Dưới đây là **giải thích đề bài LeetCode 1262 – Greatest Sum Divisible by Three** theo cách **dễ hiểu nhất**:
# Dưới đây là **giải thích thuật toán** + **code Python đã thêm chú thích rõ ràng**, giúp bạn hiểu từng dòng.

# ---

# 🧠 **Giải thích thuật toán (phiên bản Python)**

# Mục tiêu:
# Chọn ra một tập con sao cho:

# * Tổng chia hết cho 3
# * Và tổng lớn nhất có thể

# ---

# ## 🎯 Ý tưởng chính

# ### 1️⃣ Tính tổng `s = sum(nums)`

# * Nếu tổng `s % 3 == 0` → trả về luôn (tổng lớn nhất).

# ---

# ## 2️⃣ Nếu tổng không chia hết cho 3:

# Có 2 trường hợp:

# ### **Nếu s % 3 == 1**

# Để khử dư 1, ta có 2 lựa chọn:

# 1. Bỏ số nhỏ nhất có `num % 3 == 1` → `r11`
# 2. Bỏ 2 số nhỏ nhất có `num % 3 == 2` → `r21 + r22`

# 👉 Ta chọn phương án bỏ **nhỏ nhất** để tổng còn lại lớn nhất.

# ---

### **Nếu s % 3 == 2**

# Tương tự:

# 1. Bỏ số nhỏ nhất có `num % 3 == 2` → `r21`
# 2. Bỏ 2 số nhỏ nhất có `num % 3 == 1` → `r11 + r12`

# ---

# ## 3️⃣ Tại sao phải lưu 4 biến?

# * `r11`: số nhỏ nhất mod 1
# * `r12`: số nhỏ thứ 2 mod 1
# * `r21`: số nhỏ nhất mod 2
# * `r22`: số nhỏ thứ 2 mod 2

# Vì có lúc ta phải bỏ **1 số**, có lúc phải bỏ **2 số**.

# ---

# # ✅ Code Python đầy đủ + chú thích rõ ràng

# ```python
from typing import List
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        # Tổng tất cả các số
        s = sum(nums)
        
        # Nếu chia hết cho 3 thì trả kết quả luôn
        if s % 3 == 0:
            return s
        
        # 2 số nhỏ nhất có mod = 1
        r11 = 10000   # nhỏ nhất mod 1
        r12 = 10000   # nhỏ thứ 2 mod 1

        # 2 số nhỏ nhất có mod = 2
        r21 = 10000   # nhỏ nhất mod 2
        r22 = 10000   # nhỏ thứ 2 mod 2
        
        # Duyệt từng số để tìm 4 số nhỏ nhất cần thiết
        for num in nums:
            
            # Nếu num mod 1
            if num % 3 == 1 and num < r12:
                if num < r11:
                    # num nhỏ nhất → đẩy r11 sang r12
                    r12 = r11
                    r11 = num
                else:
                    # num là nhỏ thứ 2
                    r12 = num
            
            # Nếu num mod 2
            if num % 3 == 2 and num < r22:
                if num < r21:
                    # num nhỏ nhất → đẩy r21 sang r22
                    r22 = r21
                    r21 = num
                else:
                    # num là nhỏ thứ 2
                    r22 = num
        
        # Nếu tổng dư 1 → loại bỏ ít nhất 1 số mod1 hoặc 2 số mod2
        if s % 3 == 1:
            return s - min(r11, r21 + r22)
        
        # Nếu tổng dư 2 → loại bỏ 1 số mod2 hoặc 2 số mod1
        if s % 3 == 2:
            return s - min(r21, r11 + r12)


# # 📌 Tóm tắt cực ngắn

# * Tổng dư 0 → trả luôn
# * Tổng dư 1 → bỏ nhỏ nhất (mod1) **hoặc** 2 số nhỏ nhất (mod2)
# * Tổng dư 2 → bỏ nhỏ nhất (mod2) **hoặc** 2 số nhỏ nhất (mod1)
# * Lấy phương án **mất ít nhất** → tổng còn lại lớn nhất.

# ---

# Nếu bạn muốn, mình có thể viết thêm **phiên bản code rút gọn**, **so sánh với Java**, hoặc **vẽ hình minh họa**!

# ---

# # 🎯 **Yêu cầu bài toán**

# Bạn được cho một mảng số nguyên `nums`.
# Bạn cần **chọn ra một số phần tử bất kỳ** trong mảng (có thể là không chọn tất cả), sao cho:

# 1. **Tổng các phần tử được chọn chia hết cho 3**
# 2. **Tổng đó là lớn nhất có thể**

# → Đây là một bài toán **tối ưu hóa**: vừa phải chia hết cho 3, vừa phải lớn nhất.

# ---

# # 🔍 **Điều quan trọng cần hiểu**

# ### ✔ Mỗi số khi chia cho 3 sẽ có 3 loại:

# * `mod 0` → chia hết cho 3
# * `mod 1`
# * `mod 2`

# ### ✔ Tổng của bạn cũng có mod theo cách tương tự:

# * Nếu tổng cuối cùng `mod 0` → hợp lệ.

# ---

# # 🧠 **Ý tưởng của bài**

# ### B1: Tính tổng tất cả các số

# Nếu **tổng chia hết cho 3** → trả về luôn, vì lấy tất cả sẽ là lớn nhất.

# ### B2: Nếu tổng **mod = 1**

# Để làm tổng chia hết cho 3, bạn có 2 cách:

# * **Bỏ đi 1 số nhỏ nhất có mod = 1**
# * **Hoặc bỏ đi 2 số nhỏ nhất có mod = 2**

# Chọn cách nào làm **mất ít giá trị nhất** → giữ tổng lớn nhất.

# ### B3: Nếu tổng **mod = 2**

# Ngược lại:

# * **Bỏ 1 số nhỏ nhất có mod = 2**
# * Hoặc **bỏ 2 số nhỏ nhất có mod = 1**

# ---

# # 📌 Ví dụ minh họa

# ```
# nums = [3, 6, 5, 1, 8]
# ```

# Tổng = 23 → `23 % 3 = 2`

# Mod 2 → cần làm giảm tổng xuống mod 0.

# Có 2 cách:

# * Bỏ 1 số mod 2 → số nhỏ nhất mod 2 là `5` → tổng = 18
# * Bỏ 2 số mod 1 → `1 + 1 (không có số mod1 thứ 2)` → không làm được

# 👉 Kết quả: **18**

# ---

# # 🚀 **Kết luận**

# Bài này yêu cầu:

# * Tính tổng
# * Nếu không chia hết cho 3 → loại bỏ số nhỏ nhất phù hợp để biến tổng thành chia hết cho 3
# * Giữ tổng càng lớn càng tốt

# ---

# Nếu bạn muốn mình viết **code Java / C++ / Python** + giải thích từng dòng, bạn nhắn mình nhé!
