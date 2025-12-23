# Two Best Non-Overlapping Events(23/12/2025)
# OK, mình sẽ **giải thích thuật toán** và **thêm chú thích chi tiết vào code** để bạn nhìn là hiểu ngay 👍
# (Thuật toán này là **sweep line + two pointers**, chạy **O(n log n)**)

# ---

# ## 🧠 Ý tưởng thuật toán (giải thích trước)

# ### Mục tiêu

# Chọn **2 event không overlap** sao cho tổng `value` lớn nhất.

# ---

# ### Cách làm

# 1. **Sắp xếp events theo start time** → duyệt từng event làm **event thứ 2**
# 2. **Sắp xếp events theo end time** → tìm **event tốt nhất đã kết thúc trước start**
# 3. Dùng biến `end_max` để lưu:

#    > Giá trị lớn nhất của các event đã kết thúc **trước thời điểm hiện tại**

# ---

# ### Vì sao đúng?

# * Khi đang xét event `(s, e, val)`
# * Tất cả event có `end < s` **không overlap** với nó
# * Chỉ cần **event có value lớn nhất trong số đó**
# * Tổng tốt nhất lúc này là:

#   ```
#   val + end_max
#   ```

# ---

# ## ✨ Code đã thêm chú thích chi tiết

# ```python
from typing import List
from collections import deque
from operator import itemgetter
from math import inf

class Solution:
    def maxTwoEvents(self, a: List[List[int]]) -> int:
        n = len(a)

        # Mỗi event có dạng: [start, end, value]
        # start, end đều INCLUSIVE → end < start mới là không overlap

        # Sắp xếp theo end time (để pop dần các event đã kết thúc)
        end_sorted = deque(sorted(a, key=itemgetter(1)))

        # Sắp xếp theo start time (duyệt event hiện tại)
        start_sorted = sorted(a, key=itemgetter(0))

        # Trường hợp chỉ chọn 1 event
        ret = max(map(itemgetter(2), a))

        # end_max = giá trị lớn nhất của event
        # đã kết thúc trước start hiện tại
        end_max = -inf

        # Duyệt từng event theo start time
        for s, e, val in start_sorted:

            # Cập nhật end_max:
            # Lấy tất cả event có end < s
            # → không overlap với event hiện tại
            while end_sorted and end_sorted[0][1] < s:
                S, E, VAL = end_sorted.popleft()
                end_max = max(end_max, VAL)

            # Tổng giá trị khi chọn:
            # 1 event đã kết thúc + event hiện tại
            chal = val + end_max

            # Cập nhật kết quả
            ret = max(ret, chal)

        return ret


# ## 📊 Ví dụ chạy tay

# ```text
# events = [[1,3,2],[4,5,2],[2,4,3]]
# ```

# ### Sau khi sort:

# * start_sorted:
#   `[1,3,2] → [2,4,3] → [4,5,2]`
# * end_sorted:
#   `[1,3,2] → [2,4,3] → [4,5,2]`

# ### Duyệt:

# * s=1 → chưa có end < 1 → end_max = -inf
# * s=2 → chưa có end < 2
# * s=4 → pop `[1,3,2]` → end_max = 2
#   → 2 + 2 = 4 ✅

# ---

# ## ⏱️ Độ phức tạp

# * Sort: `O(n log n)`
# * Sweep: `O(n)`
# * **Tổng: `O(n log n)`**
# * Bộ nhớ: `O(n)`

# ---

## 🧩 Vì sao dùng `< s` chứ không phải `<= s`?

# 👉 Vì đề bài yêu cầu **KHÔNG overlap**

# ```
# end == start → vẫn overlap ❌
# ```

# ---

# Nếu bạn muốn:

# * 🔥 Viết lại bằng **Binary Search**
# * 🔥 Giải thích bằng **hình timeline**
# * 🔥 Chuyển sang **Java / C++**
# * 🔥 Phân tích kiểu **phỏng vấn FAANG**

# 👉 Cứ nói, mình làm tiếp cho bạn 👌

# ---

# ## 📘 Mô tả bài toán (giải thích dễ hiểu)

# Bạn được cho một mảng `events`, trong đó mỗi phần tử là:

# ```
# [startTime, endTime, value]
# ```

# * `startTime`: thời điểm bắt đầu sự kiện
# * `endTime`: thời điểm kết thúc sự kiện
# * `value`: giá trị (lợi ích) bạn nhận được nếu tham gia sự kiện đó

# ---

# ## 🎯 Mục tiêu

# 👉 **Chọn tối đa 2 sự kiện KHÔNG chồng thời gian**
# 👉 Sao cho **tổng value là lớn nhất**

# ---

# ## ❗ Điều kiện “không chồng thời gian” là gì?

# Hai sự kiện **không chồng nhau** nếu:

# ```
# endTime của sự kiện 1 < startTime của sự kiện 2
# HOẶC
# endTime của sự kiện 2 < startTime của sự kiện 1
# ```

# ⚠️ Lưu ý:

# * Nếu `endTime == startTime` → **vẫn bị coi là chồng nhau**
# * Phải **nhỏ hơn**, không phải ≤

# ---

# ## 🔍 Ví dụ 1

# ```text
# events = [[1,3,2], [4,5,2], [2,4,3]]
# ```

# ### Phân tích:

# * Event A: từ 1 → 3, value = 2
# * Event B: từ 4 → 5, value = 2
# * Event C: từ 2 → 4, value = 3

# ### Các cách chọn:

# * A + B → không chồng nhau → tổng = 4
# * C + B → **chồng nhau** (C kết thúc lúc 4, B bắt đầu lúc 4) ❌
# * Chỉ chọn C → value = 3

# ✅ **Kết quả lớn nhất: 4**

# ---

# ## 🔍 Ví dụ 2

# ```text
# events = [[1,5,3], [1,5,1], [6,6,5]]
# ```

# * Event 1: 1–5 (3)
# * Event 2: 1–5 (1)
# * Event 3: 6–6 (5)

# 👉 Chọn Event 1 + Event 3
# 👉 Tổng = 3 + 5 = **8**

# ---

# ## 🧠 Tóm tắt đề bài

# * Bạn có **n sự kiện**
# * Mỗi sự kiện có **thời gian + giá trị**
# * Chọn **tối đa 2 sự kiện**
# * Hai sự kiện **không được trùng hoặc chạm thời gian**
# * Tìm **tổng value lớn nhất**

# ---

# Nếu bạn muốn, mình có thể:

# * ✅ Giải bằng **ý tưởng (intuition)**
# * ✅ Giải bằng **Binary Search + DP**
# * ✅ Giải bằng **Java / C++ / Python**
# * ✅ Giải theo kiểu **phù hợp phỏng vấn**

# 👉 Bạn muốn mình đi tiếp theo hướng nào?
