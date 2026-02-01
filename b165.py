# Divide an Array Into Subarrays With Minimum Cost I(01/02/2026)

# Bài **“Divide an Array Into Subarrays With Minimum Cost I”** (LeetCode) hiểu **ngắn gọn như sau** 👇
# Ok 👍 mình giải thích **thuật toán + chú thích chi tiết từng dòng code** cho bạn nhé.
# (Bài này là bản **Minimum Cost I**, nên logic khá gọn.)

# ---

# ## 🧠 Ý tưởng thuật toán

# ### Điều quan trọng nhất của đề:

# * Subarray đầu tiên **bắt buộc** chứa `nums[0]`
#   → **cost chắc chắn có `nums[0]`**
# * `k = 2` (vì đây là **Minimum Cost I**)
#   → Mỗi subarray phải có **ít nhất 2 phần tử**

# 👉 Điều này dẫn đến:

# * Ta cần **tạo thêm 2 subarray nữa**
# * Mỗi subarray mới cần **1 phần tử làm “đầu subarray”**
# * Để **tổng cost nhỏ nhất**, ta chọn **2 số nhỏ nhất trong các phần tử còn lại (`nums[1:]`)**

# ---

# ## 🎯 Chiến lược

# 1. Lấy luôn `nums[0]` vào tổng cost
# 2. Duyệt các phần tử từ `nums[1]` trở đi
# 3. Tìm **2 số nhỏ nhất**
# 4. Cộng chúng vào tổng

# ⏱️ Độ phức tạp: **O(n)**
# 💾 Bộ nhớ: **O(1)**

# ---

# ## 🧩 Code + chú thích chi tiết

# ```python
from typing import List
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # nums[0] bắt buộc thuộc subarray đầu tiên
        # nên cost chắc chắn bao gồm nums[0]
        sum = nums[0]

        # firstMin: số nhỏ nhất
        # secondMin: số nhỏ thứ hai
        # Khởi tạo = 51 vì đề bài cho nums[i] <= 50
        firstMin = 51
        secondMin = 51

        # Duyệt các phần tử từ vị trí 1 trở đi
        for i in range(1, len(nums)):
            # Nếu tìm được số nhỏ hơn firstMin
            if nums[i] < firstMin:
                # firstMin cũ sẽ trở thành secondMin
                secondMin = firstMin
                firstMin = nums[i]

            # Nếu nums[i] nằm giữa firstMin và secondMin
            elif nums[i] < secondMin:
                secondMin = nums[i]

        # Tổng cost = nums[0] + 2 số nhỏ nhất còn lại
        return sum + firstMin + secondMin


# ---

# ## 🔍 Ví dụ chạy tay

# ```text
# nums = [1, 3, 2, 6, 4]
# ```

# | Bước | firstMin | secondMin |
# | ---- | -------- | --------- |
# | 3    | 3        | 51        |
# | 2    | 2        | 3         |
# | 6    | 2        | 3         |
# | 4    | 2        | 3         |

# 👉 Tổng:

# ```
# 1 + 2 + 3 = 6
# ```

# ---

# ## 📝 Ghi nhớ nhanh cho đi thi / phỏng vấn

# * `nums[0]` **luôn được cộng**
# * Chỉ cần tìm **2 số nhỏ nhất trong phần còn lại**
# * Không cần chia mảng thật sự → chỉ cần **tư duy cost**

# ---

# Nếu bạn muốn:

# * 🔥 Viết lại bằng **Java**
# * 🔥 So sánh với **Minimum Cost II**
# * 🔥 Giải thích **vì sao không cần xét vị trí k**

# 👉 Cứ nói nhé, mình hỗ trợ tiếp 💪

# ---

# ## 🧩 Mô tả đề bài (giải thích dễ hiểu)

# Bạn được cho một **mảng số nguyên `nums`** và một **số nguyên `k`**.

# 👉 Nhiệm vụ của bạn là **chia mảng `nums` thành nhiều mảng con (subarrays)** sao cho:

# ### 1️⃣ Điều kiện bắt buộc

# * **Mỗi subarray phải có độ dài ≥ k**
# * **Phần tử đầu tiên của mảng gốc (`nums[0]`) phải thuộc về subarray đầu tiên**

# ### 2️⃣ Chi phí (cost)

# * **Chi phí của mỗi subarray = phần tử đầu tiên của subarray đó**
# * **Tổng chi phí = tổng phần tử đầu tiên của tất cả các subarray**

# ### 3️⃣ Mục tiêu

# ➡️ **Tìm tổng chi phí nhỏ nhất có thể**

# ---

# ## 🔍 Ví dụ minh họa

# ### Ví dụ

# ```text
# nums = [1, 3, 2, 6, 4, 2]
# k = 2
# ```

# Ta có thể chia như sau:

# ```
# [1, 3] | [2, 6] | [4, 2]
# ```

# * Subarray 1 → cost = 1
# * Subarray 2 → cost = 2
# * Subarray 3 → cost = 4

# 👉 **Tổng cost = 1 + 2 + 4 = 7**

# ---

# ## 🧠 Bản chất của bài toán

# * `nums[0]` **luôn được tính vào cost**
# * Mỗi khi bạn **bắt đầu một subarray mới**, bạn phải:

#   * Chọn **một phần tử làm phần tử đầu**
#   * Phải đảm bảo phía sau nó còn **ít nhất k − 1 phần tử**

# ➡️ **Muốn cost nhỏ → chọn các phần tử nhỏ để làm “đầu subarray”**

# ---

# ## 💡 Cách tư duy đơn giản

# * Subarray đầu tiên **bắt buộc bắt đầu từ `nums[0]`**
# * Sau đó:

#   * Mỗi subarray mới cách subarray trước **ít nhất k phần tử**
#   * Trong các vị trí hợp lệ, **chọn phần tử nhỏ nhất** để làm đầu subarray

# ---

# ## 🧠 Tóm tắt cực ngắn

# | Thành phần | Ý nghĩa                      |
# | ---------- | ---------------------------- |
# | Input      | `nums`, `k`                  |
# | Điều kiện  | Mỗi subarray ≥ `k`           |
# | Cost       | Phần tử đầu của mỗi subarray |
# | Mục tiêu   | Tổng cost **nhỏ nhất**       |

# ---

# Nếu bạn muốn, mình có thể:

# * ✅ Giải **từng bước bằng ví dụ chi tiết**
# * ✅ Giải thích **bằng hình vẽ**
# * ✅ Viết **code Java / Python**
# * ✅ So sánh với **Divide Array II**

# 👉 Chỉ cần nói bạn muốn theo hướng nào 👍
