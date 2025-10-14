# 3349. Adjacent Increasing Subarrays Detection I(14/10/2025)
from typing import List
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        knew = k - 1     # Biến đếm số lần liên tiếp tìm thấy 2 vị trí tăng song song
        if knew == 0:    # Nếu k == 1, thì mặc định đúng luôn (vì chỉ cần 1 phần tử)
            return True

        # Duyệt từ vị trí k+1 trở đi (vì ta cần so sánh cả nums[j] và nums[j-k])
        for j in range(k + 1, len(nums)):
            # Kiểm tra điều kiện:
            # 1️⃣ nums[j] > nums[j-1] → phần tử hiện tại nằm trong chuỗi tăng
            # 2️⃣ nums[j-k] > nums[j-k-1] → phần tử cách k vị trí cũng đang tăng
            # Nếu cả hai đều tăng, tức là 2 chuỗi tăng (cách nhau k phần tử) đang song song
            if nums[j] > nums[j - 1] and nums[j - k] > nums[j - k - 1]:
                knew -= 1    # Giảm biến đếm (vì thêm được một “bước tăng song song”)
            else:
                knew = k - 1 # Nếu bị ngắt chuỗi tăng, reset lại đếm

            # Khi knew == 0 → ta đã tìm đủ k-1 bước tăng song song giữa 2 dãy liền nhau
            if knew == 0:
                return True

        return False


### 🧠 Giải thích thuật toán bằng lời:

# 1. **Ý tưởng chính:**

#    * Xem hai chuỗi tăng song song (cách nhau `k` phần tử) như hai “đường chạy”.
#    * Nếu tại từng vị trí `j`, cả `nums[j] > nums[j-1]` **và** `nums[j-k] > nums[j-k-1]` cùng đúng, thì hai đường này đang cùng **tăng liền nhau**.
#    * Nếu ta tìm được **k−1 lần liên tiếp** như vậy, thì tức là tồn tại hai đoạn tăng độ dài `k` liền nhau.

# 2. **Biến `knew`** dùng để đếm bao nhiêu bước tăng song song còn lại cần tìm.

#    * Ban đầu là `k-1`.
#    * Mỗi khi thấy một cặp tăng song song → `knew -= 1`.
#    * Nếu bị ngắt → reset về `k-1`.
#    * Khi `knew == 0` → nghĩa là ta đã có 2 dãy tăng độ dài `k` liên tiếp → trả về `True`.

# 3. Nếu duyệt hết mảng mà chưa đạt điều kiện, trả về `False`.

# ---

# ### 🧪 Ví dụ minh họa

# ```
# nums = [2,5,7,8,9,2,3,4,3,1]
# k = 3
# ```

# | j | nums[j-k-1:j+1] | nums[j]>nums[j-1]? | nums[j-k]>nums[j-k-1]? | knew | Ghi chú                       |
# | - | --------------- | ------------------ | ---------------------- | ---- | ----------------------------- |
# | 4 | [2,5,7,8,9]     | ✅                  | ✅                      | 1→0  | đủ k-1 cặp song song → ✅ True |

# Khi `j=4`, hai chuỗi tăng `[2,5,7,8,9]` và `[2,3,4]` (bắt đầu ở `j-k+1=2` và `j+1=5`) được tìm thấy.

# ---

# ### ✅ Kết quả:

# ```python
# nums = [2,5,7,8,9,2,3,4,3,1]
# k = 3
# print(Solution().hasIncreasingSubarrays(nums, k))
# # ✅ Output: True
# ```

# ---

### ⚠️ Lưu ý:

# * `knew = k - 1` vì cần `k-1` “bước tăng song song” để tạo hai dãy độ dài `k`.
# * Nếu `k == 1`, thì luôn đúng (`return True`) vì 1 phần tử bất kỳ cũng là một dãy tăng.



# Bạn có muốn mình viết **phiên bản Java tương đương có chú thích dòng từng dòng** không?

# ---

# ### 🧩 **Đề bài:**

# Cho một mảng số nguyên `nums` và một số nguyên `k`.

# Một **subarray tăng dần độ dài k** là một dãy con liên tiếp gồm `k` phần tử, trong đó mỗi phần tử sau **lớn hơn phần tử trước**.

# Bạn cần **kiểm tra xem có tồn tại hai subarray tăng dần độ dài `k` nằm liền kề nhau** hay không.
# Nếu có → trả về `true`, ngược lại → `false`.

# ---

### 📘 **Ví dụ:**

#### Ví dụ 1:

# ```
# Input: nums = [1, 2, 3, 4, 5, 6], k = 2
# ```

# Các subarray độ dài 2 là:

# * [1, 2] ✅ tăng
# * [2, 3] ✅ tăng
# * [3, 4] ✅ tăng
# * [4, 5] ✅ tăng
# * [5, 6] ✅ tăng

# → Có thể ghép [1, 2] và [3, 4] (chúng liền nhau trong mảng và đều tăng).
# => **Output: true**

# ---

# #### Ví dụ 2:

# ```
# Input: nums = [1, 2, 3, 2, 3, 4], k = 2
# ```

# Các subarray độ dài 2:

# * [1, 2] ✅ tăng
# * [2, 3] ✅ tăng
# * [3, 2] ❌ không tăng
# * [2, 3] ✅ tăng
# * [3, 4] ✅ tăng

# Ta thấy [1, 2] và [2, 3] là hai subarray tăng liên tiếp → ✅
# => **Output: true**

# ---

# #### Ví dụ 3:

# ```
# Input: nums = [1, 2, 3, 4], k = 3
# ```

# Các subarray độ dài 3:

# * [1, 2, 3] ✅ tăng
# * [2, 3, 4] ✅ tăng

# Hai subarray này kề nhau và đều tăng
# => **Output: true**

# ---

# #### Ví dụ 4:

# ```
# Input: nums = [1, 3, 5, 4, 6, 8], k = 2
# ```

# Các subarray độ dài 2:

# * [1, 3] ✅ tăng
# * [3, 5] ✅ tăng
# * [5, 4] ❌
# * [4, 6] ✅
# * [6, 8] ✅

# Ở đây [1,3] và [3,5] là hai dãy tăng liên tiếp → ✅
# => **Output: true**

# ---

# ### 🧠 **Tóm tắt logic cần làm:**

# 1. Duyệt qua mảng, đếm số phần tử liên tiếp thỏa `nums[i] < nums[i+1]`.
# 2. Nếu đếm được **2*k - 1** phần tử tăng liên tục → tức là có **hai subarray tăng độ dài k** kề nhau.
#    → Trả về `true`.
# 3. Nếu duyệt hết mà không tìm thấy → trả về `false`.

# ---

# Nếu bạn muốn, mình có thể viết code Java hoặc Python minh họa cho thuật toán này, kèm chú thích từng dòng.
# 👉 Bạn muốn xem bằng ngôn ngữ nào?
