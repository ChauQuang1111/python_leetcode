# 2125. Number of Laser Beams in a Bank(27/10/2025)
from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0       # Biến lưu tổng số tia laser trong ngân hàng
        prev = 0      # Lưu số lượng thiết bị ('1') ở hàng trước có thiết bị
        
        # Duyệt qua từng hàng trong ngân hàng
        for row in bank:
            cnt = row.count('1')   # Đếm số thiết bị ('1') trong hàng hiện tại
            
            if cnt > 0:  # Nếu hàng này có thiết bị
                # Tính số tia laser giữa hàng trước (prev) và hàng hiện tại (cnt)
                ans += prev * cnt
                
                # Cập nhật prev cho lần lặp tiếp theo (vì chỉ hàng có thiết bị mới tính)
                prev = cnt
                
        # Trả về tổng số tia laser
        return ans

### 🧩 **Đề bài**

# Một **ngân hàng** có hệ thống **bảo mật bằng laser** được biểu diễn dưới dạng **mảng chuỗi nhị phân (binary strings)**.

# * Mỗi phần tử trong mảng `bank[i]` là **một hàng (row)** trong tòa nhà.
# * Mỗi ký tự `'1'` trong chuỗi đại diện cho **một thiết bị bảo mật (security device)**.
# * Mỗi `'0'` là **khoảng trống** (không có thiết bị).

# ---

# ### 💡 **Quy tắc tạo tia laser**

# * **Tia laser chỉ xuất hiện giữa hai hàng có thiết bị** (tức là 2 hàng đều có ít nhất một `'1'`).
# * **Tia chỉ đi giữa các hàng không liền kề cũng được**, **miễn là hàng ở giữa không có thiết bị** (toàn là `'0'`).
# * **Số tia giữa hai hàng** =
#   `(số thiết bị ở hàng thứ nhất) × (số thiết bị ở hàng thứ hai)`

# ---

# ### 🎯 **Nhiệm vụ**

# Tính **tổng số tia laser** trong ngân hàng.

# ---

# ### 🧮 **Ví dụ minh họa**

# #### Ví dụ 1:

# ```python
# bank = ["011001", "000000", "010100", "001000"]
# ```

# Biểu diễn:

# ```
# Row 0: 0 1 1 0 0 1  → có 3 thiết bị
# Row 1: 0 0 0 0 0 0  → 0 thiết bị (bỏ qua)
# Row 2: 0 1 0 1 0 0  → có 2 thiết bị
# Row 3: 0 0 1 0 0 0  → có 1 thiết bị
# ```

# → Chỉ tính **tia giữa các hàng có thiết bị**:

# * Giữa hàng 0 (3 thiết bị) và hàng 2 (2 thiết bị):
#   `3 × 2 = 6 tia`
# * Giữa hàng 2 (2 thiết bị) và hàng 3 (1 thiết bị):
# #   `2 × 1 = 2 tia`

# # ✅ Tổng: `6 + 2 = 8`

# **Output:** `8`

# ---

# ### 🔢 **Tư duy thuật toán**

# 1. Đếm số thiết bị (`count_1s`) ở mỗi hàng.
# 2. Bỏ qua các hàng có 0 thiết bị.
# 3. Với mỗi cặp **liền kề (có thiết bị)**, tính số tia:
#    `ans += prev_count * curr_count`
# 4. Cập nhật `prev_count = curr_count`.

# ---

# ### 💻 **Code mẫu (Python)**

# ```python
# class Solution:
#     def numberOfBeams(self, bank: List[str]) -> int:
#         prev = 0
#         ans = 0

#         for row in bank:
#             curr = row.count('1')
#             if curr > 0:
#                 ans += prev * curr
#                 prev = curr

#         return ans
# ```

# ---

# ### ⚙️ **Phân tích ví dụ**

# | Hàng   | Thiết bị ('1') | Tia sinh ra | Tổng |
# | ------ | -------------- | ----------- | ---- |
# | 011001 | 3              | -           | -    |
# | 000000 | 0              | -           | -    |
# | 010100 | 2              | 3×2 = 6     | 6    |
# | 001000 | 1              | 2×1 = 2     | 8    |

# ✅ Kết quả cuối: **8**

# ---




### 🔍 Giải thích thuật toán:

# 1. **Khởi tạo:**

#    * `ans = 0`: tổng số tia laser.
#    * `prev = 0`: số thiết bị ở hàng trước (nếu hàng trước không có thiết bị, bỏ qua).

# 2. **Duyệt từng hàng:**

#    * Dùng `row.count('1')` để đếm số lượng thiết bị (`cnt`) trong hàng đó.
#    * Nếu hàng không có thiết bị (`cnt == 0`), bỏ qua hàng đó.

# 3. **Khi gặp hàng có thiết bị:**

#    * Nếu `prev > 0`, nghĩa là có một hàng trước đó có thiết bị.
#    * Khi đó, **tia laser giữa hai hàng** được tính bằng:
#      [
#      prev \times cnt
#      ]
#      vì **mỗi thiết bị ở hàng trên** sẽ tạo tia laser với **mỗi thiết bị ở hàng dưới**.

# 4. **Cập nhật `prev`:**

#    * Đặt `prev = cnt` để chuẩn bị tính cho hàng có thiết bị kế tiếp.

# 5. **Trả kết quả cuối cùng:** `ans`.

# ---

# ### 🧮 Ví dụ minh họa

# ```python
# bank = ["011001", "000000", "010100", "001000"]
# ```

# | Hàng     | Số thiết bị (`cnt`) | Tính toán                    | `ans` | `prev` |
# | -------- | ------------------- | ---------------------------- | ----- | ------ |
# | "011001" | 3                   | Không có hàng trước ⇒ bỏ qua | 0     | 3      |
# | "000000" | 0                   | Bỏ qua vì không có thiết bị  | 0     | 3      |
# | "010100" | 2                   | +3×2 = 6                     | 6     | 2      |
# | "001000" | 1                   | +2×1 = 2                     | 8     | 1      |

# ✅ **Kết quả cuối cùng:** `ans = 8`

# ---

# 👉 Tóm lại:
# Thuật toán chỉ cần duyệt **một lần qua mảng** → **O(n)**,
# rất hiệu quả cho bài này.
