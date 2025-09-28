# 976. Largest Perimeter Triangle(28/09/2025)
import heapq
from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # Đổi dấu toàn bộ phần tử để dùng heapq như max-heap (heapq mặc định là min-heap)
        nums = [-num for num in nums]
        heapq.heapify(nums)  # biến nums thành một heap hợp lệ O(n)

        # Lặp cho đến khi còn ít nhất 3 cạnh
        while len(nums) >= 3:
            # Lấy cạnh lớn nhất a
            a = -heapq.heappop(nums)
            # Lấy cạnh lớn thứ 2 b
            b = -heapq.heappop(nums)
            # Lấy cạnh lớn thứ 3 c (không pop ra ngay, chỉ nhìn giá trị)
            c = -nums[0]

            # Kiểm tra điều kiện tam giác: b + c > a
            if b + c > a:
                return a + b + c  # tìm được tam giác có chu vi lớn nhất

            # Nếu không tạo được tam giác, trả lại b vào heap
            # (vì a quá lớn → bỏ a, nhưng b vẫn có thể tạo tam giác với cạnh khác)
            heapq.heappush(nums, -b)

        # Nếu không tìm được tam giác hợp lệ
        return 0
# Ok, mình giải thích thuật toán trong code bạn đưa ra cho **bài 976. Largest Perimeter Triangle** nhé:

# ---

# ### 🔹 Ý tưởng của bài toán:

# * Muốn tìm **chu vi lớn nhất** của một tam giác từ mảng `nums`.
# * Điều kiện để 3 cạnh tạo thành tam giác:

#   ```
#   a + b > c
#   ```

#   với `a ≤ b ≤ c` (sắp xếp từ nhỏ đến lớn).
# * Để có chu vi lớn nhất, ta nên ưu tiên thử các cạnh lớn nhất trước.

# ---

# ### 🔹 Thuật toán trong code (dùng `heapq`):

# ```python
# class Solution:
#     def largestPerimeter(self, nums: List[int]) -> int:
#         # 1. Đảo dấu tất cả các phần tử để tạo heap max
#         nums = [-num for num in nums]
#         heapq.heapify(nums)

#         # 2. Lặp khi trong heap còn ít nhất 3 phần tử
#         while len(nums) >= 3:
#             # Lấy cạnh lớn nhất
#             a = -heapq.heappop(nums)
#             # Lấy cạnh lớn thứ 2
#             b = -heapq.heappop(nums)
#             # Xem cạnh lớn thứ 3 nhưng chưa pop
#             c = -nums[0]

#             # 3. Kiểm tra điều kiện tam giác
#             if b + c > a:
#                 return a + b + c  # Nếu thỏa, trả về chu vi

#             # 4. Nếu không thỏa, push lại b vì b có thể ghép với cạnh khác
#             heapq.heappush(nums, -b)
        
#         return 0
# ```

# ---

# ### 🔹 Giải thích chi tiết từng bước:

# 1. **Đảo dấu tạo max-heap**

#    * Python `heapq` mặc định là **min-heap**.
#    * Muốn dùng **max-heap** (lấy số lớn nhất trước), ta đảo dấu: `nums = [-num for num in nums]`.

# 2. **Pop 2 cạnh lớn nhất**

#    * `a = -heapq.heappop(nums)` → lấy cạnh lớn nhất.
#    * `b = -heapq.heappop(nums)` → lấy cạnh lớn nhì.

# 3. **Xem xét cạnh thứ 3 (c lớn)**

#    * `c = -nums[0]` → lấy phần tử lớn thứ 3 trong heap (chưa pop để giữ lại).

# 4. **Kiểm tra điều kiện tam giác**

#    * Nếu `b + c > a` → 3 cạnh này tạo thành tam giác.
#    * Chu vi chính là `a + b + c`. Vì đây là những cạnh lớn nhất trước tiên, nên đó chắc chắn là **chu vi lớn nhất**.

# 5. **Nếu không tạo thành tam giác**

#    * Đẩy lại `b` vào heap (`heapq.heappush(nums, -b)`), vì `b` vẫn có thể kết hợp với cạnh khác nhỏ hơn `a`.
#    * Còn `a` thì bỏ hẳn, vì nếu `b + c <= a` thì với bất kỳ cạnh nhỏ hơn nữa cũng **không thể tạo tam giác**.

# 6. **Nếu hết vòng lặp mà không tìm được tam giác** → trả về `0`.

# ---

# 👉 Thuật toán này đảm bảo luôn tìm **chu vi tam giác lớn nhất** vì:

# * Luôn ưu tiên thử 3 cạnh dài nhất.
# * Nếu không hợp lệ, loại bỏ cạnh dài nhất và thử tiếp với cạnh nhỏ hơn.

# ---

# Bạn có muốn mình viết lại một **version đơn giản hơn (chỉ dùng sort, không cần heap)** để dễ hiểu không?

# Ok, mình giải thích đề **LeetCode 976 – Largest Perimeter Triangle** cho bạn nhé 👇

# ---

# ### 📌 Đề bài:

# * Bạn được cho một mảng số nguyên `nums`, trong đó mỗi phần tử là **độ dài cạnh**.
# * Nhiệm vụ: **tìm chu vi lớn nhất của một tam giác có thể tạo thành từ 3 cạnh trong mảng**.
# * Nếu không thể tạo được tam giác hợp lệ, trả về `0`.

# ---

# ### 📌 Điều kiện tạo tam giác hợp lệ:

# Với ba cạnh `a, b, c` (sắp xếp theo `a ≤ b ≤ c`), cần thỏa:

# ```
# a + b > c
# ```

# Nếu điều kiện này không đúng thì **không tạo thành tam giác**.

# ---

# ### 📌 Ví dụ minh họa:

# #### Ví dụ 1:

# ```
# Input: nums = [2,1,2]
# ```

# * Sắp xếp: [1,2,2]
# * Kiểm tra 3 cạnh: `1 + 2 > 2` ✅ đúng → tạo được tam giác.
# * Chu vi = 1 + 2 + 2 = **5**.

# 👉 Output: `5`

# ---

# #### Ví dụ 2:

# ```
# Input: nums = [1,2,1]
# ```

# * Sắp xếp: [1,1,2]
# * Kiểm tra: `1 + 1 > 2` ❌ sai.
# * Không thể tạo tam giác.

# 👉 Output: `0`

# ---

# #### Ví dụ 3:

# ```
# Input: nums = [3,6,2,3]
# ```

# * Sắp xếp: [2,3,3,6]
# * Lấy 3 cạnh lớn nhất [3,3,6]: `3 + 3 > 6` ❌ sai.
# * Lấy [2,3,3]: `2 + 3 > 3` ✅ đúng.
# * Chu vi = 2 + 3 + 3 = **8**.

# 👉 Output: `8`

# ---

# ### 📌 Ý tưởng giải:

# 1. Sắp xếp mảng tăng dần.
# 2. Duyệt ngược từ cuối (các cạnh lớn nhất) → kiểm tra 3 cạnh liên tiếp `nums[i-2], nums[i-1], nums[i]`.

#    * Nếu tạo thành tam giác, trả về chu vi luôn (vì đó là chu vi lớn nhất).
# 3. Nếu không tìm được, trả về `0`.

# ---

# Bạn có muốn mình viết code Java/Python kèm chú thích để minh họa luôn không?
