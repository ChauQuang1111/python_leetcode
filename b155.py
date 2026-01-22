# **Minimum Pair Removal to Sort Array I (22/01/2026)
# Dưới đây là **giải thích thuật toán + chú thích chi tiết từng dòng code**, đúng theo đoạn bạn đưa.
# (Bài này là **Minimum Pair Removal to Sort Array I – bản greedy + mô phỏng**)
# OK 👍 dưới đây là **code đã được chú thích trực tiếp từng phần**, đúng theo yêu cầu *“chú thích vào code”* để bạn đọc là hiểu ngay thuật toán làm gì.

# ```python
from typing import List
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        
        # Hàm kiểm tra mảng có không giảm hay không
        # Trả về True nếu nums[i] >= nums[i-1] với mọi i
        def nondecreasing(a):
            for i in range(1, len(a)):
                if a[i] < a[i - 1]:     # phát hiện vi phạm thứ tự không giảm
                    return False
            return True

        ops = 0   # đếm số lần xóa cặp (gộp cặp)

        # Lặp cho đến khi mảng trở thành không giảm
        while not nondecreasing(nums):

            min_sum = float("inf")  # lưu tổng nhỏ nhất của cặp liền kề
            idx = 0                 # vị trí bắt đầu của cặp có tổng nhỏ nhất

            # Duyệt tất cả các cặp liền kề
            for i in range(len(nums) - 1):
                s = nums[i] + nums[i + 1]  # tổng của cặp (i, i+1)

                # Nếu tìm được cặp có tổng nhỏ hơn
                # Nếu bằng nhau thì tự động giữ cặp bên trái (greedy)
                if s < min_sum:
                    min_sum = s
                    idx = i

            # Gộp cặp được chọn:
            # thay nums[idx] bằng tổng của hai phần tử
            nums[idx] = nums[idx] + nums[idx + 1]

            # Xóa phần tử idx+1 (đã bị gộp)
            nums.pop(idx + 1)

            # Tăng số lần thao tác
            ops += 1

        # Khi mảng đã không giảm, trả về số thao tác tối thiểu
        return ops
# ```

# ---

# ### Ghi nhớ nhanh 🧠

# * **while**: mảng chưa không giảm → tiếp tục xử lý
# * **greedy**: luôn gộp cặp có **tổng nhỏ nhất**
# * **gộp = 1 lần xóa cặp**
# * Kết thúc khi mảng **đã được sắp không giảm**

# Nếu bạn muốn mình:

# * ✍️ viết chú thích **ngắn hơn kiểu thi**
# * 🔁 chuyển sang **Java**
# * 📊 minh họa bằng **1 test cụ thể chạy từng dòng**

# 👉 nói mình biết nhé.

# ---

# ## 1. Ý tưởng tổng quát của thuật toán

# 👉 Thay vì **xóa hẳn 2 phần tử**, bài này cho phép:

# * **Gộp (merge)** 2 phần tử liền kề `nums[i] + nums[i+1]`
# * Thao tác này **tương đương 1 lần xóa cặp**
# * Lặp lại cho đến khi mảng **không giảm**

# ### Chiến lược (Greedy)

# * Khi mảng **chưa không giảm**:

#   * Chọn **cặp liền kề có tổng nhỏ nhất**
#   * Gộp chúng lại
# * Vì:

#   * Tổng nhỏ → ít phá vỡ thứ tự phía sau
#   * Gộp bên trái trước giúp mảng ổn định sớm hơn

# ---

# ## 2. Phân tích code chi tiết (có chú thích)

# ```python
# class Solution:
#     def minimumPairRemoval(self, nums: List[int]) -> int:
# ```

# 👉 Hàm trả về **số lần gộp (xóa cặp)** tối thiểu để mảng trở thành **không giảm**

# ---

# ### Hàm kiểm tra mảng không giảm

# ```python
#         def nondecreasing(a):
#             for i in range(1, len(a)):
#                 if a[i] < a[i - 1]:
#                     return False
#             return True
# ```

# 🔍 Ý nghĩa:

# * Duyệt từ trái sang phải
# * Nếu tồn tại `a[i] < a[i-1]` → mảng **không hợp lệ**
# * Ngược lại → **không giảm**

# ---

# ### Biến đếm số thao tác

# ```python
#         ops = 0
# ```

# 👉 `ops` = số lần **xóa cặp / gộp cặp**

# ---

# ### Vòng lặp chính

# ```python
#         while not nondecreasing(nums):
# ```

# 👉 Chừng nào mảng **chưa không giảm** → tiếp tục xử lý

# ---

# ### Tìm cặp liền kề có tổng nhỏ nhất

# ```python
#             min_sum = float("inf")
#             idx = 0
# ```

# * `min_sum`: lưu tổng nhỏ nhất
# * `idx`: vị trí bắt đầu của cặp cần gộp

# ---

# ```python
#             for i in range(len(nums) - 1):
#                 s = nums[i] + nums[i + 1]
#                 if s < min_sum:   # leftmost tie kept automatically
#                     min_sum = s
#                     idx = i
# ```

# 🔎 Duyệt tất cả các cặp `(i, i+1)`:

# * Tính tổng `s`
# * Nếu nhỏ hơn `min_sum` → cập nhật
# * Nếu bằng nhau → **giữ cặp bên trái** (greedy ổn định)

# ---

# ### Gộp cặp đã chọn

# ```python
#             nums[idx] = nums[idx] + nums[idx + 1]
#             nums.pop(idx + 1)
# ```

# 👉 Thao tác này tương đương:

# * Gộp 2 phần tử liền kề
# * Giảm độ dài mảng đi 1
# * Tương ứng **xóa 1 cặp**

# Ví dụ:

# ```
# [3, 1, 4] → gộp (3,1) → [4, 4]
# ```

# ---

# ### Tăng số thao tác

# ```python
#             ops += 1
# ```

# ---

# ### Trả kết quả

# ```python
#         return ops
# ```

# 👉 Khi mảng đã **không giảm**, trả về số thao tác tối thiểu

# ---

# ## 3. Ví dụ chạy tay

# ```
# nums = [1, 3, 2, 4]
# ```

# * Chưa không giảm (3 > 2)
# * Các cặp:

#   * (1,3) → 4
#   * (3,2) → 5
#   * (2,4) → 6
# * Chọn (1,3)
# * Gộp → [4,2,4]
# * Chưa không giảm
# * Gộp (4,2) → [6,4]
# * Chưa không giảm
# * Gộp (6,4) → [10]
# * Hoàn tất

# 👉 `ops = 3`

# ---

# ## 4. Bản chất thuật toán

# * **Greedy + Simulation**
# * Không tối ưu cho input lớn
# * Phù hợp với **Minimum Pair Removal I (constraints nhỏ)**

# ⏱️ Độ phức tạp:

# * Worst case: **O(n³)** (vì mỗi lần check + duyệt)

# ---

# Nếu bạn muốn:

# * ✅ So sánh với **bài II**
# * ✅ Viết lại theo **Java**
# * ✅ Giải thích vì sao chọn **min sum**
# * ✅ Phân tích test edge-case

# 👉 cứ nói, mình giải tiếp ngay.


# ---

# ### 1. Tóm tắt đề bài

# Bạn được cho **một mảng số nguyên** `nums`.

# * Trong **mỗi bước**, bạn **được phép chọn một cặp 2 phần tử liền kề** `(nums[i], nums[i+1])` và **xóa cả hai phần tử đó khỏi mảng**.
# * Mục tiêu: **xóa ít cặp nhất** sao cho **mảng còn lại trở thành mảng không giảm** (non-decreasing), tức là:

#   ```
#   nums[0] ≤ nums[1] ≤ nums[2] ≤ ...
#   ```

# 👉 Bạn cần **tính số cặp tối thiểu phải xóa**.

# ---

# ### 2. Giải thích “mảng không giảm”

# Mảng **không giảm** nghĩa là:

# * Các phần tử **đứng sau không nhỏ hơn phần tử đứng trước**
# * Ví dụ:

#   * ✅ `[1, 2, 2, 3]` → hợp lệ
#   * ❌ `[1, 3, 2]` → không hợp lệ vì `3 > 2`

# ---

# ### 3. Quy tắc quan trọng cần nhớ

# * **Chỉ được xóa theo cặp**
# * **Hai phần tử phải liền kề**
# * Không được xóa 1 phần tử đơn lẻ
# * Sau khi xóa, các phần tử còn lại **tự động dồn lại**

# ---

# ### 4. Ví dụ minh họa

# #### Ví dụ 1

# ```
# nums = [1, 3, 2, 4]
# ```

# * Mảng **chưa không giảm** vì `3 > 2`
# * Ta có thể xóa cặp `(3, 2)`
# * Mảng còn lại: `[1, 4]` → không giảm

# ✅ Số cặp xóa tối thiểu: **1**

# ---

# #### Ví dụ 2

# ```
# nums = [1, 2, 3]
# ```

# * Mảng đã không giảm
# * Không cần xóa gì

# ✅ Kết quả: **0**

# ---

# #### Ví dụ 3

# ```
# nums = [5, 4, 3, 2]
# ```

# * Mảng giảm dần hoàn toàn
# * Có thể xóa:

#   * `(5, 4)` → còn `[3, 2]`
#   * `(3, 2)` → còn `[]`

# ✅ Kết quả: **2**

# ---

# ### 5. Bản chất của bài toán

# 👉 Ta cần **loại bỏ các phần tử “phá vỡ thứ tự tăng”**,
# nhưng **chỉ được loại theo cặp liền kề**, nên không thể xử lý từng phần tử riêng lẻ.

# Nói cách khác:

# * Ta muốn **giữ lại một dãy con không giảm**
# * Các phần tử còn lại **bị xóa theo từng cặp**
# * Số phần tử bị xóa **phải là số chẵn**

# ---

# ### 6. Điều bài toán muốn kiểm tra

# * Tư duy **greedy / dynamic programming**
# * Hiểu rõ **thao tác xóa theo cặp**
# * Khả năng xử lý **thứ tự mảng**

# ---

# Nếu bạn muốn:

# * 👉 **ví dụ chạy từng bước**
# * 👉 **ý tưởng giải + code Java/Python**
# * 👉 **so sánh với bài II (nếu có)**

# cứ nói mình sẽ giải tiếp 👍
