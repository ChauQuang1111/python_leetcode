# **Maximal Rectangle (11/01/2026)
# Dưới đây là **giải thích thuật toán + chú thích chi tiết trực tiếp vào code** cho bài
# **85. Maximal Rectangle** (đúng theo code bạn đưa).

# ---

# ## 1. Ý tưởng tổng quát (rất quan trọng)

# Bài **Maximal Rectangle** được giải bằng cách **chuyển về bài con**:

# > 👉 **Largest Rectangle in Histogram**

# ### Cách làm:

# * Duyệt **từng hàng** của ma trận
# * Với mỗi cột `j`, ta xây dựng mảng `hist[j]`:

#   * `hist[j]` = số lượng `'1'` **liên tiếp theo chiều dọc** tính tới hàng hiện tại
# * Mỗi hàng → coi `hist` như **một histogram**
# * Tính **diện tích hình chữ nhật lớn nhất trong histogram**
# * Lấy max qua tất cả các hàng

# ---

# ## 2. Minh họa nhanh

# Matrix:

# ```
# 1 0 1
# 1 1 1
# ```

# Duyệt từng hàng:

# * Hàng 0 → hist = `[1,0,1]`
# * Hàng 1 → hist = `[2,1,2]`

# 👉 Với mỗi `hist`, ta giải bài **Largest Rectangle in Histogram**

# ---

# ## 3. Giải thích hàm `area()` (Histogram)

# ```python
from typing import List
def area(self, heights: List[int]) -> int:
    stack = []          # stack lưu chỉ số cột, đảm bảo heights tăng dần
    maxArea = 0
    n = len(heights)

    # duyệt thêm 1 bước (i == n) để "xả stack"
    for i in range(n + 1):
        # khi i == n, ta coi chiều cao = 0 để ép tính hết diện tích
        h = 0 if i == n else heights[i]

        # nếu chiều cao hiện tại nhỏ hơn đỉnh stack
        while stack and h < heights[stack[-1]]:
            height = heights[stack.pop()]  # chiều cao cột bị pop

            # nếu stack rỗng => hình chữ nhật kéo từ 0 → i-1
            if not stack:
                width = i
            else:
                # chiều rộng = khoảng cách giữa 2 cột nhỏ hơn gần nhất
                width = i - stack[-1] - 1

            maxArea = max(maxArea, height * width)

        stack.append(i)

    return maxArea
# ```

# ### Nguyên lý stack:

# * Stack **luôn tăng dần theo chiều cao**
# * Khi gặp cột thấp hơn → ta tính diện tích với:

#   * `height` = cột vừa bị pop
#   * `width` = khoảng mà cột đó có thể mở rộng

# ---

# ## 4. Giải thích hàm `maximalRectangle()`

# ```python
# def maximalRectangle(self, matrix: List[List[str]]) -> int:
#     if not matrix:
#         return 0

#     m, n = len(matrix), len(matrix[0])
#     hist = [0] * n   # histogram chiều cao cho mỗi cột
#     ans = 0

#     # duyệt từng hàng
#     for i in range(m):
#         for j in range(n):
#             if matrix[i][j] == '1':
#                 hist[j] += 1   # tăng chiều cao nếu là '1'
#             else:
#                 hist[j] = 0    # reset nếu gặp '0'

#         # với mỗi hàng, tính histogram lớn nhất
#         ans = max(ans, self.area(hist))

#     return ans
# ```

# ### Ý nghĩa `hist`:

# * `hist[j]` = số `'1'` liên tiếp **từ trên xuống** tại cột `j`
# * Mỗi hàng → một histogram mới

# ---

# ## 5. Độ phức tạp

# * **Time:** `O(m × n)`

#   * Mỗi phần tử vào stack đúng **1 lần**
# * **Space:** `O(n)` cho histogram + stack

# ---

# ## 6. Tóm tắt 1 câu để nhớ bài

# > **Mỗi hàng → histogram → Largest Rectangle in Histogram → lấy max**

# ---

# Nếu bạn muốn:

# * Mô phỏng stack **từng bước bằng hình**
# * Giải thích riêng **vì sao width = i - stack[-1] - 1**
# * Viết lại code theo style **dễ học cho phỏng vấn**

# 👉 nói mình biết nhé 👍


# ---

# ### 1. Mô tả bài toán

# Bạn được cho một **ma trận nhị phân** (chỉ gồm ký tự `'0'` và `'1'`), kích thước `m x n`.

# **Nhiệm vụ:**
# 👉 Tìm **diện tích hình chữ nhật lớn nhất** chỉ gồm toàn `'1'` trong ma trận.

# * Hình chữ nhật phải **liền kề**, các ô nằm cạnh nhau theo hàng – cột
# * Không được xoay (chỉ song song với trục)

# ---

# ### 2. Ví dụ minh họa

# Ví dụ ma trận:

# ```
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# ```

# Một hình chữ nhật lớn nhất toàn `'1'` có dạng:

# ```
# 1 1 1
# 1 1 1
# ```

# * Rộng = 3
# * Cao = 2
#   ➡️ **Diện tích = 3 × 2 = 6**

# **Kết quả trả về: `6`**

# ---

# ### 3. Input – Output

# * **Input:**

#   * `matrix`: mảng 2 chiều các ký tự `'0'` và `'1'`
# * **Output:**

#   * Một số nguyên: **diện tích lớn nhất** của hình chữ nhật toàn `'1'`

# ---

# ### 4. Những hiểu nhầm thường gặp

# ❌ Không phải tìm hình vuông
# ❌ Không phải đếm số lượng `'1'`
# ❌ Không được lấy các ô `'1'` rời rạc

# ✔️ Phải là **hình chữ nhật liên tục**

# ---

# ### 5. Ý tưởng cốt lõi (chưa đi vào code)

# Cách nghĩ phổ biến khi giải bài này:

# * Duyệt từng **hàng**
# * Coi mỗi hàng như **đáy của một histogram**
# * Với mỗi cột, đếm xem từ hàng hiện tại **liên tiếp bao nhiêu số 1 ở trên**
# * Sau đó áp dụng bài toán con:
#   👉 **Largest Rectangle in Histogram**

# (Đây là lý do bài này được xếp mức **Hard**)

# ---

# Nếu bạn muốn:

# * Giải thích **ý tưởng chi tiết từng bước**
# * So sánh với bài **Largest Rectangle in Histogram**
# * Hoặc **code Java / C++ / Python** kèm chú thích

# 👉 cứ nói mình biết nhé 👍
