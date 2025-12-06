#  Count Partitions With Max-Min Difference at Most K(06/12/2025)
#  Dưới đây là **giải thích đề bài "Count Partitions With Max–Min Difference at Most K"** theo cách dễ hiểu nhất cho bạn.
# Dưới đây là **giải thích thuật toán của lời giải**, kèm **code đã được chú thích chi tiết từng dòng** để bạn hiểu rõ toàn bộ cách hoạt động.

# ---

# # 🧠 **Ý tưởng chính của thuật toán**

# Chúng ta cần đếm **số cách chia mảng thành các nhóm liên tiếp**, sao cho mỗi nhóm thỏa:

# ```
# max(group) − min(group) ≤ k
# ```

# Đây là dạng bài:

# * cần đếm số partition → dùng DP
# * cần kiểm tra max–min trong đoạn [left…right] → dùng **deque** để giữ min và max dạng sliding window

# Cách này giúp ta xử lý mọi đoạn **O(n)** thay vì O(n²).

# ---

# # 🎯 Giải thích từng thành phần

# ## 1️⃣ **Dùng sliding window để đảm bảo max–min ≤ k**

# * `mxQueue`: deque lưu các phần tử theo thứ tự giảm dần → phần tử đầu là **max**.
# * `mnQueue`: deque lưu theo thứ tự tăng dần → phần tử đầu là **min**.

# Mỗi lần thêm phần tử mới:

# * Loại bỏ các phần tử không còn phù hợp ở cuối deque.
# * Thêm phần tử vào cuối.

# → Từ đó ta lấy được `max = mxQueue[0]`, `min = mnQueue[0]`.

# Nếu:

# ```
# max - min > k
# ```

# → Ta phải dịch `left++`, đồng thời loại phần tử đó khỏi deque nếu cần.

# ---

# ## 2️⃣ **DP để đếm số cách**

# * `dp[i]` = số cách chia **nums[0..i]**

# Ý tưởng:

# Tại mỗi vị trí `r`, nếu ta có `left` là biên trái **nhỏ nhất** sao cho đoạn [left…r] hợp lệ, thì:

# → Ta có thể chọn chia hoặc không chia trước r
# → Khi thêm 1 phần tử → số cách tăng gấp đôi
# Nhưng phải đảm bảo không tính các đoạn invalid → dùng biến `cnt`.

# `cnt` = tổng số cách chia của tất cả dp thuộc vùng cửa sổ hợp lệ.

# ---

# ## 3️⃣ **Pourquoi gấp đôi?**

# Khi thêm nums[r]:

# * Mỗi cách chia cũ → vẫn tồn tại
# * Và ta có thể chọn thêm một partition mới kết thúc ở r → tạo thêm số cách bằng chính dp[r]

# Nhưng để đúng, ta chỉ được phép nhân đôi khi **window hợp lệ**.
# Khi window bị nới vì max-min > k → ta phải loại bỏ số cách bắt đầu từ `left`, vì chúng không còn hợp lệ.

# ---

# # 🟢 **Code đã chú thích đầy đủ**

# ```python
from typing import List
from collections import deque
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:

        left = 0                     # biên trái của sliding window
        cnt = 1                      # số cách hợp lệ hiện tại cho cửa sổ
        mod_ = 1_000_000_007         # modulo
        mnQueue, mxQueue = deque(), deque()
        dp = [cnt]                   # dp[0] = 1 (mặc định có 1 cách: 1 partition đầu tiên)

        for rght, num in enumerate(nums):

            # ---- cập nhật max deque ----
            # loại bỏ phần tử nhỏ hơn num ở cuối vì chúng không thể là max
            while mxQueue and num > mxQueue[-1]:
                mxQueue.pop()
            mxQueue.append(num)

            # ---- cập nhật min deque ----
            # loại bỏ phần tử lớn hơn num ở cuối vì chúng không thể là min
            while mnQueue and num < mnQueue[-1]:
                mnQueue.pop()
            mnQueue.append(num)

            # ---- kiểm tra điều kiện max - min > k ----
            # nếu vượt quá k, ta phải dịch cửa sổ sang phải
            while mxQueue[0] - mnQueue[0] > k:
                # loại dp[left] khỏi cnt vì left không còn nằm trong cửa sổ hợp lệ
                cnt -= dp[left]

                # nếu phần tử rời đi là max hoặc min thì pop khỏi deque
                if nums[left] == mxQueue[0]:
                    mxQueue.popleft()
                if nums[left] == mnQueue[0]:
                    mnQueue.popleft()

                left += 1  # dịch cửa sổ sang phải

            # ---- thêm số cách mới ----
            dp.append(cnt)   # dp[r] = số cách hợp lệ trước khi nhân đôi
            cnt *= 2         # gấp đôi số cách vì thêm nums[r] → có thể chia hoặc không chia tại đây
            cnt %= mod_      # mod để tránh tràn số

        # dp[-1] = tổng số cách chia toàn mảng
        return dp[-1] % mod_



# 📌 **Tóm tắt logic**

# 1. Dùng hai deque để giữ max và min trong cửa sổ.
# 2. Nếu max−min > k → đẩy left lên.
# 3. `dp[r] = cnt` là số cách hợp lệ hiện tại.
# 4. `cnt *= 2` vì mỗi cách cũ có thêm lựa chọn:

#    * tiếp tục không chia
#    * chia tại r
# 5. Khi left tăng → bỏ đi dp[left] khỏi cnt để tránh tính cách chia invalid.

# ---

# Nếu bạn muốn, mình có thể:

# ✔️ làm ví dụ minh họa từng bước
# ✔️ vẽ bảng dp
# ✔️ giải thích bằng hình sliding window

# Bạn muốn phần nào?

# ---

# # 🧠 **Đề bài nói gì?**

# Bạn được cho:

# * Một mảng số nguyên `nums`
# * Một số `k`

# Bạn phải **chia mảng thành nhiều nhóm (partitions)** sao cho:

# 👉 **Trong mỗi nhóm, hiệu giữa phần tử lớn nhất và nhỏ nhất của nhóm ≤ k**

# Và câu hỏi là:

# 👉 **Có bao nhiêu cách chia mảng thỏa mãn điều kiện đó?**

# ---

# # 📌 Quan trọng: Các nhóm phải theo thứ tự ban đầu

# Tức là bạn không được đảo vị trí phần tử.

# Ví dụ:

# ```
# nums = [1, 3, 6]
# ```

# # Chỉ được chia như:

# * `[1] | [3] | [6]`
# * `[1, 3] | [6]`
# * `[1] | [3, 6]`
# # * `[1, 3, 6]`

# Không được chia kiểu:

# ```
# [1, 6] | [3]   ❌ không đúng
# ```

# vì không giữ thứ tự ban đầu.

# ---

# # 🎯 Điều kiện của mỗi nhóm:

# Giả sử nhóm đó là:

# ```
# [ a, b, c, d ]
# ```

# thì nhóm hợp lệ nếu:

# ```
# max(group) - min(group) ≤ k
# ```

# ---

# # 📘 Ví dụ đơn giản

# ### Ví dụ 1

# ```
# nums = [1, 2, 3]
# k = 2
# ```

# Tất cả nhóm đều có max-min ≤ 2 nên mọi cách chia đều hợp lệ:

# Các cách chia:

# 1. `[1] [2] [3]`
# 2. `[1, 2] [3]`
# 3. `[1] [2, 3]`
# 4. `[1, 2, 3]`

# → **4 cách**

# ---

# ### Ví dụ 2

# ```
# nums = [1, 5, 6]
# k = 3
# ```

# Kiểm tra từng nhóm:

# * `[1]` → ok
# * `[1,5]` → max-min = 5−1 = 4 > 3 ❌
# * `[1,5,6]` → 6−1 = 5 > 3 ❌
# * `[5,6]` → 6−5 = 1 ≤ 3 ✔

# Các cách chia hợp lệ:

# 1. `[1] [5] [6]`
# 2. `[1] [5, 6]`

# → **2 cách**

# ---

# # 🧠 Cần kỹ thuật gì để giải?

# Để giải bài này thường dùng:

# ### ✔️ DP (Dynamic Programming)

# Ở mỗi vị trí i, ta xét xem có thể ghép bao nhiêu phần tử về bên trái để tạo 1 nhóm hợp lệ.

# ### ✔️ Hai con trỏ / Sliding window

# Để tìm đoạn [l…r] sao cho max-min ≤ k.

# ---

# # 📝 Tóm tắt đề bài (ngắn gọn)

# > Đếm số cách chia mảng thành các nhóm liên tiếp sao cho:
# > Trong mỗi nhóm, hiệu giữa phần tử lớn nhất và nhỏ nhất không vượt quá `k`.

# ---

# Nếu bạn muốn, mình có thể:

# ✅ Viết lời giải DP (Python / Java)
# ✅ Giải thích từng bước bằng ví dụ
# ✅ Thêm code có chú thích đầy đủ

# Bạn muốn loại nào?
