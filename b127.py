# 3075. Maximize Happiness of Selected Children(25/12/2025)
# **Giải thích đề bài – LeetCode 3075: Maximize Happiness of Selected Children**
from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # Sắp xếp mức độ hạnh phúc theo thứ tự giảm dần
        # để luôn chọn những đứa trẻ hạnh phúc nhất trước
        happiness.sort(reverse=True)

        # Biến lưu tổng hạnh phúc tối đa
        res = 0

        # Chọn lần lượt k đứa trẻ
        for i in range(k):
            # Đứa trẻ thứ i sẽ bị giảm i đơn vị hạnh phúc
            # (đứa đầu tiên giảm 0, đứa thứ hai giảm 1, ...)
            gain = happiness[i] - i

            # Nếu hạnh phúc sau khi giảm <= 0
            # thì chọn tiếp sẽ không mang lại lợi ích
            # (các đứa sau chắc chắn còn nhỏ hơn)
            if gain <= 0:
                return res
            
            # Cộng hạnh phúc hợp lệ vào tổng
            res += gain
        
        # Trả về tổng hạnh phúc lớn nhất có thể đạt được
        return res

# ---

# ### Nội dung bài toán (hiểu đơn giản)

# * Bạn có một mảng số nguyên **`happiness`**
#   → mỗi phần tử biểu thị **mức độ hạnh phúc ban đầu của một đứa trẻ**.
# * Bạn được phép **chọn đúng `k` đứa trẻ** để tham gia một hoạt động.
# * Khi chọn:

#   * Đứa trẻ **đầu tiên** giữ nguyên mức hạnh phúc.
#   * Đứa trẻ **thứ hai** bị giảm **1** đơn vị hạnh phúc.
#   * Đứa trẻ **thứ ba** bị giảm **2** đơn vị hạnh phúc.
#   * ...
#   * Đứa trẻ **thứ i** bị giảm **(i − 1)** đơn vị hạnh phúc.
# * Nếu sau khi giảm mà giá trị âm → **tính là 0**.
# * Mục tiêu: **chọn k đứa trẻ sao cho tổng hạnh phúc cuối cùng là lớn nhất**.

# ---

# ### Ví dụ minh họa

# ```text
# happiness = [1, 2, 3]
# k = 2
# ```

# **Cách chọn tốt nhất**:

# * Chọn trẻ có happiness = 3 (không bị giảm) → 3
# * Chọn trẻ có happiness = 2 (bị giảm 1) → 1

# 👉 Tổng = 3 + 1 = **4**

# ---

# ### Ý nghĩa cốt lõi của bài toán

# * Mỗi lần chọn thêm một đứa trẻ, **mức phạt tăng lên**
# * Vì vậy:

#   * Ta **nên chọn những đứa có happiness lớn trước**
#   * Tránh chọn đứa có happiness nhỏ khi mức phạt đã lớn

# ---

# ### Tư duy chính (chưa cần code)

# 1. **Sắp xếp mảng `happiness` giảm dần**
# 2. Chọn lần lượt `k` phần tử lớn nhất
# 3. Với phần tử thứ `i` được chọn:

#    * Giá trị đóng góp = `max(happiness[i] − i, 0)`
# 4. Cộng tất cả lại → kết quả

# ---

# ### Tóm tắt ngắn gọn

# * Bài toán = **tham lam (greedy)**
# * Chọn trẻ **hạnh phúc nhất trước**
# * Mỗi lần chọn sau bị giảm nhiều hơn
# * Không cho giá trị âm

# ---

# Nếu bạn muốn:

# * ✅ Giải thích bằng **ví dụ lớn hơn**
# * ✅ Viết **code Java / C++ / Python**
# * ✅ Phân tích **độ phức tạp**
# * ✅ So sánh với bài greedy tương tự

# 👉 Cứ nói nhé 👍
# Mình giải thích **đúng theo đoạn code của bạn** nhé 👇
# (thuật toán **tham lam – Greedy**, rất chuẩn 👍)

# ---

# ## Ý tưởng chính của code

# 👉 **Chọn những đứa trẻ có happiness lớn nhất trước**, vì:

# * Mỗi lần chọn thêm 1 đứa thì bị trừ thêm `i`
# * Nếu chọn đứa có happiness nhỏ ở lượt sau → dễ bị về 0 hoặc âm

# ---

# ## Giải thích từng bước trong code

# ```python
# happiness.sort(reverse = True)
# ```

# * Sắp xếp mảng `happiness` **giảm dần**
# * Đứa hạnh phúc nhất sẽ được chọn đầu tiên (không bị trừ)

# ---

# ```python
# res = 0
# ```

# * `res` dùng để lưu **tổng hạnh phúc tối đa**

# ---

# ```python
# for i in range(k):
# ```

# * Chọn lần lượt **k đứa trẻ**
# * `i` chính là **số lần đã chọn trước đó**
# * Theo đề bài: đứa thứ `i` sẽ bị trừ `i`

# ---

# ```python
# gain = happiness[i] - i
# ```

# * `gain` = mức hạnh phúc thực tế của đứa trẻ thứ `i`
# * Vì:

#   * Đứa đầu tiên: trừ `0`
#   * Đứa thứ hai: trừ `1`
#   * Đứa thứ ba: trừ `2`
#   * ...

# ---

# ```python
# if gain <= 0:
#     return res
# ```

# * Nếu hạnh phúc ≤ 0:

#   * Chọn thêm **không có lợi**
#   * Vì các phần tử sau **chắc chắn còn nhỏ hơn**
# * 👉 Dừng sớm để tối ưu

# ---

# ```python
# res += gain
# ```

# * Cộng hạnh phúc hợp lệ vào tổng

# ---

# ```python
# return res
# ```

# * Trả về **tổng hạnh phúc lớn nhất**

# ---

# ## Ví dụ chạy code

# ```python
# happiness = [5, 3, 1]
# k = 3
# ```

# Sau khi sort:

# ```text
# [5, 3, 1]
# ```

# | i | gain = happiness[i] - i |
# | - | ----------------------- |
# | 0 | 5 - 0 = 5               |
# | 1 | 3 - 1 = 2               |
# | 2 | 1 - 2 = -1 ❌            |

# → Dừng tại i = 2
# → Tổng = **5 + 2 = 7**

# ---

# ## Độ phức tạp

# * **Sort**: `O(n log n)`
# * **Loop k phần tử**: `O(k)`
# * **Tổng**: `O(n log n)`
#   ✔️ Đáp ứng tốt yêu cầu LeetCode

# ---

# ## Kết luận

# * Code của bạn:

#   * ✅ Đúng
#   * ✅ Gọn
#   * ✅ Tối ưu (dừng sớm)
# * Comment `# 妙哉` là **rất chuẩn** 😄 (Greedy đẹp)

# Nếu bạn muốn mình:

# * Giải thích bằng **hình minh họa**
# * Viết lại bằng **Java / C++**
# * Chứng minh vì sao greedy luôn đúng

# 👉 Cứ nói nhé 💪
