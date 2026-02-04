# Trionic Array II(04/02/2026)
# Ok, mình sẽ **giải thích thuật toán Trionic Array II (max sum)** theo đúng logic của đoạn code bạn đưa, rồi **thêm chú thích chi tiết vào code** để bạn đọc là hiểu ngay 👌
# Ok 👍 mình **giữ nguyên thuật toán**, chỉ **thêm chú thích TIẾNG VIỆT, rõ ràng – đúng ý tưởng**, để bạn đọc code là hiểu ngay.

# ---

# ### Code đã chú thích tiếng Việt

# ```python
from typing import List
import math
from itertools import pairwise

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)

        # state biểu diễn trạng thái hiện tại của mảng con
        # 0: chưa bắt đầu
        # 1: đang tăng (tăng lần 1)
        # 2: đang giảm
        # 3: đang tăng trở lại (tăng lần 2)
        state = 0

        # sum1: tổng của đoạn tăng lần 1 + đoạn giảm
        # sum2: tổng của Trionic Array hoàn chỉnh (tăng – giảm – tăng)
        sum1, sum2 = 0, 0

        # initial_num: phần tử đầu của pha hiện tại
        # dùng để loại bỏ prefix âm nhằm tối ưu tổng
        initial_num = 0

        # lưu tổng lớn nhất tìm được
        best = -math.inf

        # duyệt từng cặp phần tử liên tiếp (nums[i], nums[i+1])
        for fst, snd in pairwise(nums):

            # ---------- TRƯỜNG HỢP ĐANG TĂNG ----------
            if snd - fst > 0:

                # bắt đầu đoạn tăng lần 1
                if state == 0:
                    state = 1
                    initial_num = fst
                    sum1 = fst + snd

                # tiếp tục tăng lần 1
                elif state == 1:
                    # nếu phần tử đầu âm thì loại bỏ
                    if initial_num < 0:
                        sum1 -= initial_num
                        initial_num = fst
                    sum1 += snd

                # chuyển từ giảm sang tăng lần 2 → hình thành Trionic
                elif state == 2:
                    state = 3
                    initial_num = fst

                    # hoàn thành tổng Trionic
                    sum2 = sum1 + snd

                    # reset sum1 để có thể bắt đầu chuỗi mới
                    sum1 = fst + snd

                    # cập nhật kết quả
                    best = max(best, sum2)

                # tiếp tục tăng lần 2
                elif state == 3:
                    # loại bỏ prefix âm
                    if initial_num < 0:
                        sum1 -= initial_num
                        initial_num = fst

                    sum1 += snd
                    sum2 += snd

                    # cập nhật kết quả
                    best = max(best, sum2)

            # ---------- TRƯỜNG HỢP ĐANG GIẢM ----------
            elif snd - fst < 0:
                # chỉ cho phép giảm khi đã bắt đầu
                if state > 0:
                    state = 2
                    sum1 += snd

            # ---------- TRƯỜNG HỢP BẰNG NHAU ----------
            else:
                # không thỏa strict → reset toàn bộ
                state = 0

        return best


### Tóm tắt ngắn gọn bằng tiếng Việt

# * Thuật toán duyệt mảng **1 lần**
# * Dùng **máy trạng thái** để theo dõi:
#   **tăng → giảm → tăng**
# * Khi hoàn thành đủ 3 pha → cập nhật tổng lớn nhất
# * Loại bỏ **prefix âm** để tối ưu tổng (ý tưởng giống Kadane)

# ---

# Nếu bạn muốn:

# * ✍️ Viết **chú thích ngắn gọn hơn cho bài thi**
# * 📘 Giải thích lại theo **tư duy từng bước cho người mới**
# * 🧪 Mô phỏng chạy code với 1 test cụ thể

# cứ nói, mình làm tiếp cho bạn nhé 💪

# ---

# ## 1. Ý tưởng tổng quát của thuật toán

# Bài toán:
# 👉 **Tìm tổng lớn nhất của một mảng con liên tiếp có dạng**
# **tăng → giảm → tăng** (strict)

# Thuật toán này:

# * Duyệt mảng **1 lần (O(n))**
# * Dùng **máy trạng thái (state machine)** để biết ta đang ở pha nào
# * Vừa duyệt vừa **cộng dồn tổng**
# * Khi hoàn thành đủ 3 pha → cập nhật kết quả tốt nhất

# ---

# ## 2. Ý nghĩa các biến quan trọng

# ### `state`

# | Giá trị | Ý nghĩa                    |
# | ------- | -------------------------- |
# | `0`     | Chưa bắt đầu (initial)     |
# | `1`     | Đang ở đoạn **tăng lần 1** |
# | `2`     | Đang ở đoạn **giảm**       |
# | `3`     | Đang ở đoạn **tăng lần 2** |

# ---

# ### `sum1`

# * Tổng của **đoạn tăng đầu + đoạn giảm**
# * Dùng để làm nền khi bước sang pha tăng lần 2

# ### `sum2`

# * Tổng của **trionic array hoàn chỉnh**
# * Chỉ tồn tại khi đã vào `state = 3`

# ---

# ### `initial_num`

# * Phần tử đầu của pha hiện tại
# * Nếu nó **âm**, ta loại bỏ để tăng tổng (giống Kadane)

# ---

# ### `best`

# * Kết quả lớn nhất tìm được

# ---

# ## 3. Cách thuật toán hoạt động

# Ta duyệt từng cặp `(fst, snd)`:

# ### 📈 Nếu `snd > fst` (đang tăng)

# * `state 0 → 1`: bắt đầu đoạn tăng đầu
# * `state 1`: tiếp tục tăng
# * `state 2 → 3`: bắt đầu đoạn tăng lần 2 ⇒ **đã đủ Trionic**
# * `state 3`: tiếp tục tăng lần 2 và cập nhật `best`

# ---

# ### 📉 Nếu `snd < fst` (đang giảm)

# * Nếu đã bắt đầu (`state > 0`) → chuyển sang `state = 2`
# * Tiếp tục cộng vào `sum1`

# ---

# ### ➖ Nếu `snd == fst`

# * Không thể strict → **reset toàn bộ**

# ---

# ## 4. Code đã thêm chú thích chi tiết

# ```python
# class Solution:
#     def maxSumTrionic(self, nums: List[int]) -> int:
#         n = len(nums)

#         # state machine:
#         # 0 = initial
#         # 1 = first increasing
#         # 2 = decreasing
#         # 3 = second increasing
#         state = 0

#         # sum1: sum of first increasing + decreasing
#         # sum2: sum of full trionic array
#         sum1, sum2 = 0, 0

#         # first element of current segment
#         # used to trim negative prefix
#         initial_num = 0

#         best = -math.inf

#         # iterate pairwise: (nums[i], nums[i+1])
#         for fst, snd in pairwise(nums):

#             # ---------- increasing ----------
#             if snd - fst > 0:

#                 # start first increasing
#                 if state == 0:
#                     state = 1
#                     initial_num = fst
#                     sum1 = fst + snd

#                 # continue first increasing
#                 elif state == 1:
#                     # remove negative prefix
#                     if initial_num < 0:
#                         sum1 -= initial_num
#                         initial_num = fst
#                     sum1 += snd

#                 # switch from decreasing → second increasing
#                 elif state == 2:
#                     state = 3
#                     initial_num = fst

#                     # complete trionic sum
#                     sum2 = sum1 + snd

#                     # prepare for possible new segment
#                     sum1 = fst + snd

#                     best = max(best, sum2)

#                 # continue second increasing
#                 elif state == 3:
#                     if initial_num < 0:
#                         sum1 -= initial_num
#                         initial_num = fst

#                     sum1 += snd
#                     sum2 += snd

#                     best = max(best, sum2)

#             # ---------- decreasing ----------
#             elif snd - fst < 0:
#                 if state > 0:
#                     state = 2
#                     sum1 += snd

#             # ---------- equal (invalid) ----------
#             else:
#                 state = 0

#         return best
# ```

# ---

# ## 5. Độ phức tạp

# * **Time:** `O(n)`
# * **Space:** `O(1)`
# * Không dùng mảng phụ

# ---

# ## 6. Tóm tắt 1 câu cho dễ nhớ

# > Thuật toán dùng **máy trạng thái tăng–giảm–tăng**, kết hợp **cộng dồn thông minh + loại prefix âm**, để tìm **tổng lớn nhất của Trionic Array trong 1 lần duyệt**.

# Nếu bạn muốn:

# * 👉 vẽ **biểu đồ state**
# * 👉 test từng bước với 1 input cụ thể
# * 👉 rút gọn code cho dễ nhớ khi đi thi

# cứ nói, mình làm tiếp cho bạn 👍


# ## 1. Trionic Array là gì?

# Một **Trionic Array** là một mảng số **được chia thành 3 đoạn liên tiếp**:

# 1. **Đoạn 1: tăng chặt (strictly increasing)**

#    * Mỗi phần tử sau **lớn hơn** phần tử trước
#    * Ví dụ: `1 3 5 7`

# 2. **Đoạn 2: giảm chặt (strictly decreasing)**

#    * Mỗi phần tử sau **nhỏ hơn** phần tử trước
#    * Ví dụ: `7 6 4 2`

# 3. **Đoạn 3: tăng chặt (strictly increasing)**

#    * Ví dụ: `2 5 8`

# 👉 Cả 3 đoạn đều **không được rỗng** (mỗi đoạn có ít nhất 1 phần tử)

# ---

# ## 2. Trionic Array II yêu cầu gì?

# Đề bài **Trionic Array II** thường yêu cầu:

# > **Tìm độ dài lớn nhất của một mảng con liên tiếp** trong mảng ban đầu sao cho mảng con đó là **Trionic Array**

# Nói cách khác:

# * Bạn **không cần dùng toàn bộ mảng**
# * Chỉ cần chọn **một đoạn con liên tiếp**
# * Đoạn đó phải có dạng:
#   **tăng → giảm → tăng**

# ---

# ## 3. Ví dụ minh họa

# ### Ví dụ:

# ```
# A = [1, 2, 4, 6, 5, 3, 2, 4, 7]
# ```

# Một Trionic Array hợp lệ:

# ```
# [1, 2, 4, 6, 5, 3, 2, 4, 7]
#  ↑ tăng    ↓ giảm      ↑ tăng
# ```

# 👉 Độ dài = **9**

# ---

# ### Ví dụ không hợp lệ ❌

# ```
# [1, 2, 3, 4, 5]
# ```

# ❌ Chỉ tăng, **không có đoạn giảm**

# ```
# [5, 4, 3, 2, 1]
# ```

# ❌ Chỉ giảm

# ```
# [1, 3, 2, 4]
# ```

# ❌ Tăng → giảm → tăng nhưng **đoạn giảm chỉ có 1 phần tử** (không hợp lệ nếu đề yêu cầu giảm chặt với độ dài ≥ 2)

# ---

# ## 4. Điểm quan trọng cần nhớ

# ✔ Tăng và giảm đều là **strict** (>, <)
# ✔ Phải có **đủ 3 pha**: tăng – giảm – tăng
# ✔ Các phần tử **liên tiếp nhau** trong mảng
# ✔ Mục tiêu: **độ dài lớn nhất**

# ---

# Nếu bạn muốn:

# * 👉 Giải **bằng tư duy / thuật toán**
# * 👉 Viết **code Java / C++**
# * 👉 Giải theo **O(n)**

# chỉ cần nói mình nhé 😄
