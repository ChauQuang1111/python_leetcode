# 3005. Count Elements With Maximum Frequency(22/09/2025)
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        # B1: Đếm tần suất của từng phần tử trong nums
        freq = Counter(nums)   # vd: [1,2,2,3,1,4] -> {1:2, 2:2, 3:1, 4:1}
        
        # B2: Tìm tần suất lớn nhất
        max_freq = max(freq.values())   # vd: max_freq = 2
        
        # B3: Cộng tổng số lần xuất hiện của tất cả phần tử có tần suất = max_freq
        result = sum(count for count in freq.values() if count == max_freq)
        # vd: freq = {1:2, 2:2, 3:1, 4:1} -> result = 2+2 = 4
        
        return result

# Ok 👍 mình sẽ giải thích đề **LeetCode 3005 - Count Elements With Maximum Frequency**.

# ---

# ## 📌 Đề bài

# Cho một mảng số nguyên `nums`, bạn cần:

# 1. Tìm **tần suất xuất hiện lớn nhất** trong mảng (một số xuất hiện nhiều nhất).
# 2. Trả về **tổng số lần xuất hiện của tất cả các số có tần suất bằng tần suất lớn nhất**.

# ---

# ## 🚀 Ví dụ

# ### Ví dụ 1

# ```
# Input: nums = [1,2,2,3,1,4]
# ```

# * Tần suất:

#   * 1 → xuất hiện 2 lần
#   * 2 → xuất hiện 2 lần
#   * 3 → xuất hiện 1 lần
#   * 4 → xuất hiện 1 lần
# * Tần suất lớn nhất = **2**
# * Có 2 số đạt tần suất này: `1` và `2`.
# * Tổng số lần xuất hiện = 2 (cho 1) + 2 (cho 2) = **4**.

# 👉 Output:

# ```
# 4
# ```

# ---

# ### Ví dụ 2

# ```
# Input: nums = [1,2,3,4,5]
# ```

# * Tần suất:

#   * 1,2,3,4,5 → mỗi số chỉ xuất hiện 1 lần.
# * Tần suất lớn nhất = 1
# * Có 5 số đạt tần suất này
# * Tổng số lần xuất hiện = 5 × 1 = **5**

# 👉 Output:

# ```
# 5
# ```

# ---

# ## 📊 Ý tưởng thuật toán

# 1. Dùng **hashmap (map hoặc dictionary)** để đếm tần suất xuất hiện của từng số.
# 2. Tìm giá trị tần suất lớn nhất `max_freq`.
# 3. Duyệt lại hashmap, cộng tất cả các số lần xuất hiện của những phần tử có `freq == max_freq`.

# ---

# ## ⏱️ Độ phức tạp

# * Thời gian: **O(n)** (duyệt mảng và map).
# * Bộ nhớ: **O(n)** (lưu tần suất).

# ---

# 👉 Bạn có muốn mình viết luôn **code Java + Python có chú thích** cho bài này không?
