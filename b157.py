# “Minimize Maximum Pair Sum in Array(24/01/2026)
# Ok 👍 mình sẽ **giải thích thuật toán + thêm chú thích trực tiếp vào code** để bạn nhìn là hiểu liền (chuẩn kiểu học LeetCode).

# ---

# ## 🧠 Ý tưởng thuật toán (Greedy + Two Pointers)

# **Mục tiêu:**
# Ghép các số thành cặp sao cho **tổng lớn nhất trong các cặp là nhỏ nhất**.

# ### Tư duy:

# * Sau khi **sắp xếp**, số **nhỏ nhất** và **lớn nhất** là hai cực trị
# * Nếu không ghép chúng lại với nhau, số lớn sẽ phải ghép với số khác → tổng còn lớn hơn
# * Vì vậy, chiến lược tối ưu là:

# 👉 **Luôn ghép số nhỏ nhất còn lại với số lớn nhất còn lại**

# ---

# ## ⏱️ Độ phức tạp

# * **Sort:** `O(n log n)`
# * **Two pointers:** `O(n)`
# * **Tổng:** `O(n log n)`
# * **Bộ nhớ:** `O(1)` (không tính sort)

# ---

# ## ✅ Code có chú thích chi tiết

# ```python
from  typing import List
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # Biến lưu kết quả: tổng lớn nhất nhỏ nhất có thể
        res = 0
        
        # Con trỏ trái (phần tử nhỏ nhất)
        l = 0
        
        # Con trỏ phải (phần tử lớn nhất)
        r = len(nums) - 1
        
        # Sắp xếp mảng để dễ ghép cặp
        nums.sort()
        
        # Ghép cặp khi còn ít nhất 2 phần tử
        while l < r:
            # Tính tổng của cặp nhỏ nhất + lớn nhất
            pair_sum = nums[l] + nums[r]
            
            # Cập nhật tổng lớn nhất trong các cặp đã ghép
            res = max(res, pair_sum)
            
            # Di chuyển con trỏ vào trong
            l += 1
            r -= 1
        
        # Trả về tổng lớn nhất nhỏ nhất có thể
        return res
# ```

# ---

# ## 📌 Ví dụ chạy tay nhanh

# ```
# nums = [3, 5, 2, 3]
# sort → [2, 3, 3, 5]

# (2,5) → 7 → res = 7
# (3,3) → 6 → res = 7

# return 7
# ```

# ---

## 🧩 Ghi nhớ nhanh khi gặp bài này

# * **Sort**
# * **Two pointers**
# * **Minimize max → pair small + large**
# * Thuộc nhóm bài: `Greedy + Two Pointers`

# ---

# Nếu bạn muốn mình:

# * ✍️ Viết **comment ngắn gọn kiểu đi thi**
# * 🔄 So sánh với cách ghép sai để hiểu sâu hơn
# * 🧠 Viết lại bằng **Java / C++**

# 👉 nói mình nhé 😄

# ---

# ## 1️⃣ Đề bài nói gì?

# Bạn được cho **một mảng số nguyên** `nums` có **số phần tử chẵn**.

# 👉 Nhiệm vụ của bạn là:

# * **Ghép các phần tử thành từng cặp** (mỗi phần tử chỉ dùng **1 lần**)
# * Với mỗi cặp, tính **tổng của cặp đó**
# * Trong tất cả các cặp, lấy **tổng lớn nhất**
# * Cuối cùng, hãy **làm sao để tổng lớn nhất này là nhỏ nhất có thể**

# 📌 Tức là:

# > *Tối ưu cách ghép cặp sao cho cặp “tệ nhất” cũng không quá lớn.*

# ---

# ## 2️⃣ Ví dụ minh hoạ

# ### Ví dụ:

# ```
# nums = [3, 5, 2, 3]
# ```

# ### Bước 1: Sắp xếp mảng

# ```
# [2, 3, 3, 5]
# ```

# ### Bước 2: Ghép cặp sao cho hợp lý

# * Ghép **nhỏ nhất + lớn nhất**

# ```
# (2, 5) → tổng = 7
# (3, 3) → tổng = 6
# ```

# ### Bước 3: Lấy tổng lớn nhất

# ```
# max = 7
# ```

# 👉 **Kết quả = 7**

# ---

# ## 3️⃣ Vì sao phải ghép nhỏ nhất với lớn nhất?

# Nếu bạn ghép:

# ```
# (5, 3) và (3, 2)
# → tổng = 8 và 5 → max = 8 ❌
# ```

# So với:

# ```
# (5, 2) và (3, 3)
# → tổng = 7 và 6 → max = 7 ✅
# ```

# ➡️ Ghép **số lớn với số nhỏ** giúp **giảm sự chênh lệch**, từ đó **giảm tổng lớn nhất**.

# 📌 Đây là một dạng **greedy strategy** (tham lam nhưng đúng).

# ---

# ## 4️⃣ Tóm tắt ý chính (rất hay dùng khi đi phỏng vấn / LeetCode)

# * Mảng có số phần tử **chẵn**
# * Sắp xếp mảng
# * Dùng **2 con trỏ**:

#   * `left` (nhỏ nhất)
#   * `right` (lớn nhất)
# * Mỗi lần:

#   * Tính `nums[left] + nums[right]`
#   * Cập nhật `maxSum`
#   * `left++`, `right--`

# ---

# ## 5️⃣ Ý tưởng ngắn gọn để nhớ

# > **Muốn cặp lớn nhất nhỏ đi → ghép số lớn với số nhỏ**

# ---

# Nếu bạn muốn:

# * ❓ Giải bằng **Java / C++ / Python**
# * ❓ Giải thích theo **tư duy thuật toán cho người mới**
# * ❓ So sánh với bài **Two Pointers / Greedy**

# 👉 cứ nói mình làm tiếp nha 😄
