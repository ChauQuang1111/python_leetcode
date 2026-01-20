# 3314. Construct the Minimum Bitwise Array I(20/01/2026)
# Mình giải thích **đề bài LeetCode 3314 – Construct the Minimum Bitwise Array I** bằng **tiếng Việt, dễ hiểu từng bước** nhé.


## 1️⃣ Ý tưởng chính của thuật toán

### 🔑 Quan sát quan trọng

# * Nếu `nums[i]` **là số chẵn** → **không thể tạo** `ans[i]` hợp lệ
#   👉 vì `ans[i] | ans[i+1] = nums[i]`
#   mà OR của hai số **luôn ≥ số lớn hơn**, và để đạt **giá trị chẵn**, cả hai số phải có bit cuối = `0` → mâu thuẫn với yêu cầu tối thiểu
#   ➜ trả về `-1`

# * Nếu `nums[i]` **là số lẻ** → **luôn tồn tại** nghiệm

# ---

# ## 2️⃣ Mục tiêu khi xây `ans[i]`

# Ta cần:

# ```
# ans[i] | ans[i+1] = nums[i]
# ```

# Để mảng **nhỏ nhất (minimum)**:

# * Ta muốn `ans[i]` **nhỏ nhất có thể**
# * Nghĩa là:
#   👉 Giữ lại **bit 1 thấp nhất bắt buộc**,
#   👉 Tắt (clear) các bit 1 không cần thiết ở `nums[i]`

# ---

# ## 3️⃣ Giải thích thủ thuật bit trong code

# ### 🔍 Tìm bit 0 thấp nhất sau chuỗi bit 1

# ```python
# (n + 1) & ~n
# ```

# Ví dụ:

# ```
# n = 13 = 1101
# n+1 = 1110
# ~n  = 0010
# => (n+1) & ~n = 0010
# ```

# 👉 Kết quả là **bit 0 thấp nhất** (sau chuỗi bit 1 liên tiếp)

# ---

# ### 🔍 Dịch phải 1 bit

# ```python
# ((n + 1) & ~n) >> 1
# ```

# 👉 Xác định **bit 1 cao nhất trong chuỗi bit 1 liên tiếp ở cuối**

# ---

# ### 🔍 Tắt bit đó trong n

# ```python
# n & ~( ... )
# ```

# 👉 Tạo ra số:

# * Nhỏ hơn `n`
# * Vẫn đảm bảo:

#   ```
#   ans[i] | ans[i+1] = n
#   ```
# * Là **giá trị nhỏ nhất có thể cho ans[i]**

# ---

# ## 4️⃣ Code có chú thích chi tiết

# ```python
from typing import List
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []  # Mảng kết quả

        for n in nums:
            # Nếu n là số chẵn → không thể tạo ans hợp lệ
            if n & 1 == 0:
                res.append(-1)
                continue

            # (n + 1) & ~n:
            #  - tìm bit 0 thấp nhất trong n
            #  - ví dụ: n = 1101 → kết quả = 0010
            lowest_zero_bit = (n + 1) & ~n

            # Dịch phải 1 bit để xác định bit cần tắt
            bit_to_clear = lowest_zero_bit >> 1

            # Tắt bit đó trong n để tạo ans[i] nhỏ nhất
            ans_i = n & ~bit_to_clear

            res.append(ans_i)

        return res
# ```

# ---

# ## 5️⃣ Ví dụ minh họa

# ### Ví dụ: `nums = [7]`

# ```
# n = 7 = 111
# (n+1)&~n = 1000 & 000 = 1000
# >>1 = 0100
# ans = 111 & ~0100 = 011 = 3
# ```

# ✔ `3 | 4 = 7`
# ✔ `3` là giá trị **nhỏ nhất**

# ---

# ## 6️⃣ Độ phức tạp

# * ⏱ **Time**: `O(n)`
# * 💾 **Space**: `O(1)` (ngoài mảng kết quả)

# ---

## 7️⃣ Kết luận ngắn gọn

# ✔ Số **chẵn → -1**
# ✔ Số **lẻ → tắt bit 1 cao nhất trong chuỗi bit 1 cuối**
# ✔ Dùng trick bit:

# ```
# (n + 1) & ~n
# ```

# ---

# Nếu bạn muốn:

# * 🔹 Chứng minh vì sao **số chẵn vô nghiệm**
# * 🔹 Vẽ **bit diagram từng bước**
# * 🔹 So sánh với **Bitwise Array II**
# * 🔹 Viết lại code **Java / C++**

# 👉 cứ nói, mình giải tiếp nhé 🚀

# ---

# ## 1️⃣ Mô tả bài toán (hiểu đề)

# Bạn được cho một **mảng số nguyên không âm** `nums` có độ dài `n`.

# Nhiệm vụ của bạn là **xây dựng một mảng mới** `ans` cũng có độ dài `n` sao cho:

# ### Điều kiện bắt buộc

# Với **mọi chỉ số i**:

# ```
# (ans[i] OR ans[i+1]) == nums[i]
# ```

# * `OR` là **phép toán OR bit (|)**
# * Áp dụng cho các cặp **liền kề**
# * Riêng `ans[n-1]` (phần tử cuối) **không cần xét với ai**

# ### Mục tiêu

# * Trong tất cả các mảng `ans` thỏa điều kiện trên
#   ➡️ **chọn mảng có giá trị nhỏ nhất theo thứ tự từ trái sang phải (lexicographically smallest)**

# Nếu **không tồn tại** mảng nào thỏa mãn → trả về **mảng rỗng**.

# ---

# ## 2️⃣ Nhắc lại: OR bit là gì?

# Phép OR bit hoạt động như sau:

# | Bit A | Bit B | A OR B |
# | ----- | ----- | ------ |
# | 0     | 0     | 0      |
# | 0     | 1     | 1      |
# | 1     | 0     | 1      |
# | 1     | 1     | 1      |

# 👉 Chỉ cần **một trong hai bit là 1 → kết quả là 1**

# ---

# ## 3️⃣ Hiểu điều kiện `(ans[i] | ans[i+1]) == nums[i]`

# Điều này có nghĩa:

# * Mọi bit **bằng 1** trong `nums[i]`
#   → **ít nhất một** trong hai số `ans[i]` hoặc `ans[i+1]` phải có bit đó = 1
# * Mọi bit **bằng 0** trong `nums[i]`
#   → **cả hai** `ans[i]` và `ans[i+1]` **đều phải là 0** ở bit đó

# ---

# ## 4️⃣ Mục tiêu “minimum” nghĩa là gì?

# **Minimum bitwise array** ở đây hiểu là:

# * Ưu tiên `ans[0]` **nhỏ nhất có thể**
# * Nếu nhiều cách cho `ans[0]`, chọn cách làm `ans[1]` nhỏ nhất
# * Tiếp tục như vậy cho đến hết

# 📌 Tức là **lexicographically smallest array**.

# ---

# ## 5️⃣ Ví dụ minh họa

# ### Ví dụ 1

# ```
# nums = [3, 1]
# ```

# * 3 = `11` (nhị phân)
# * 1 = `01`

# Ta cần:

# ```
# ans[0] | ans[1] = 3
# ans[1] | ans[2] = 1   (không tồn tại vì n = 2 → bỏ)
# ```

# Một cách hợp lệ:

# ```
# ans = [2, 1]
# 2 | 1 = 3 ✅
# ```

# Nhưng cách nhỏ hơn:

# ```
# ans = [1, 2]
# 1 | 2 = 3 ✅  → nhỏ hơn lexicographically
# ```

# ➡️ Kết quả: `[1, 2]`

# ---

# ## 6️⃣ Khi nào không có lời giải?

# Nếu có bit nào trong `nums[i]` **bắt buộc là 0**, nhưng:

# * `ans[i]` đã có bit đó = 1 từ bước trước
#   → **mâu thuẫn**, không thể tạo mảng hợp lệ

# ➡️ Trả về `[]`

# ---

# ## 7️⃣ Tóm tắt ngắn gọn

# ✔ Bạn cần tìm mảng `ans` sao cho:

# * `ans[i] | ans[i+1] = nums[i]`
# * Mảng `ans` **nhỏ nhất có thể**

# ✔ OR bit:

# * Bit 0 → cả hai phải 0
# * Bit 1 → ít nhất một số phải 1

# ✔ Nếu không thể thỏa điều kiện → trả mảng rỗng

# ---

# Nếu bạn muốn, mình có thể:

# * ✅ Giải **tư duy thuật toán**
# * ✅ Giải **theo từng bit**
# * ✅ Viết **code Java / C++ / Python**
# * ✅ So sánh với **Bitwise Array II**

# Chỉ cần nói tiếp nhé 👍
