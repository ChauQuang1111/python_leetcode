# # Find the Largest Area of Square Inside Two Rectangles(17/01/2026)
# # Mình **giải thích đề bài** theo cách dễ hiểu nhé (chưa đi vào code).
# Ok, mình **giải thích thuật toán + thêm chú thích trực tiếp vào code** theo đúng tư duy bài *Largest Square Area Inside Two Rectangles*.
# Mình sẽ giữ nguyên logic của bạn, chỉ **chú thích rõ từng bước** để bạn nhìn là hiểu ngay.

# ---

# ## Ý tưởng tổng quát của thuật toán

# * Ta có **n hình chữ nhật**
# * Duyệt **mọi cặp (i, j)** để:

#   1. Kiểm tra chúng **có giao nhau không**
#   2. Nếu có → tính **hình chữ nhật giao**
#   3. Từ đó suy ra **cạnh hình vuông lớn nhất**
# * Luôn cập nhật `maximal_size`
# * Cuối cùng trả về **diện tích = cạnh²**

# ⏱️ Độ phức tạp: **O(n²)**

# ---

# ## Code đã thêm chú thích chi tiết

# ```python
from typing import List
class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        # maximal_size: cạnh lớn nhất của hình vuông tìm được đến hiện tại
        maximal_size = 0 

        # Duyệt hình chữ nhật thứ i
        for i in range(len(bottomLeft)): 
            # Tọa độ hình chữ nhật i
            x10, y10 = bottomLeft[i]
            x11, y11 = topRight[i]

            # Nếu chính hình chữ nhật i
            # không thể chứa hình vuông lớn hơn maximal_size hiện tại
            # thì bỏ qua (pruning)
            if y11 - y10 <= maximal_size or x11 - x10 <= maximal_size: 
                continue

            # Duyệt hình chữ nhật thứ j (j > i)
            for j in range(i + 1, len(bottomLeft)): 
                # Tọa độ hình chữ nhật j
                x20, y20 = bottomLeft[j]
                x21, y21 = topRight[j]

                # Tương tự: nếu hình chữ nhật j
                # không thể chứa hình vuông lớn hơn maximal_size
                if y21 - y20 <= maximal_size or x21 - x20 <= maximal_size: 
                    continue

                # Kiểm tra 2 hình chữ nhật có giao nhau không
                # Nếu một hình nằm hoàn toàn bên trái / phải / trên / dưới hình kia
                # → không giao
                if x21 <= x10 or y21 <= y10 or x20 >= x11 or y20 >= y11: 
                    continue 

                # Chiều rộng vùng giao nhau theo trục X
                size_x_intersect = min(x11, x21) - max(x10, x20)

                # Nếu chiều rộng này <= maximal_size
                # thì không thể tạo hình vuông lớn hơn
                if size_x_intersect < maximal_size: 
                    continue 

                # Chiều cao vùng giao nhau theo trục Y
                size_y_intersect = min(y11, y21) - max(y10, y20)

                # Nếu chiều cao này <= maximal_size
                if size_y_intersect < maximal_size:
                    continue 

                # Cạnh hình vuông lớn nhất có thể đặt
                # chính là min(chiều rộng, chiều cao)
                maximal_size = min(size_x_intersect, size_y_intersect)

        # Trả về diện tích hình vuông
        return maximal_size ** 2
# ```

# ---

# ## Vì sao dùng `min(width, height)`?

# Vì:

# * Hình vuông cần **2 cạnh bằng nhau**
# * Bị giới hạn bởi cạnh **ngắn hơn** của hình chữ nhật giao

# ---

# ## Điểm hay trong code của bạn 👍

# ✔️ **Pruning rất tốt** (skip sớm khi không thể lớn hơn `maximal_size`)
# ✔️ Không tính thừa cặp (j bắt đầu từ i+1)
# ✔️ Logic giao hình chữ nhật **chuẩn xác**
# ✔️ Đúng tư duy thi LeetCode / CF

# ---

# Nếu bạn muốn, mình có thể:

# * 🔍 Minh họa hình vẽ để dễ nhớ
# * 🚀 Viết version **ngắn gọn hơn**
# * 🧠 Giải thích theo kiểu **tư duy hình học thi ICPC**
# * 🧪 Test từng case đặc biệt (không giao, giao mỏng, trùng nhau…)

# 👉 Bạn đang học bài này để **thi**, **phỏng vấn**, hay **luyện LeetCode**?

# ---

# ## Ý nghĩa đề: *Find the Largest Area of Square Inside Two Rectangles*

# 👉 **Tìm diện tích lớn nhất của một hình vuông** sao cho hình vuông đó **nằm hoàn toàn bên trong cả hai hình chữ nhật**.

# Nói cách khác:

# * Có **2 hình chữ nhật**
# * Ta muốn đặt **1 hình vuông**
# * Hình vuông này phải **thuộc phần chung (giao nhau)** của **cả 2 hình chữ nhật**
# * Hỏi: **diện tích lớn nhất** của hình vuông đó là bao nhiêu?

# ---

# ## Cách hiểu từng bước

# ### 1️⃣ Hai hình chữ nhật

# Mỗi hình chữ nhật thường được cho bởi:

# * Tọa độ 2 góc đối diện
#   Ví dụ:

#   * Rectangle 1: `(x1, y1)` và `(x2, y2)`
#   * Rectangle 2: `(x3, y3)` và `(x4, y4)`

# 👉 Các cạnh **song song trục tọa độ** (thường là giả định ngầm trong bài).

# ---

# ### 2️⃣ Phần giao nhau của 2 hình chữ nhật

# * Nếu **không giao nhau** → ❌ **không đặt được hình vuông** → kết quả = `0`
# * Nếu **có giao nhau** → ta chỉ xét **vùng chồng lên nhau**

# Vùng giao nhau cũng là **một hình chữ nhật nhỏ hơn**.

# ---

# ### 3️⃣ Hình vuông lớn nhất nằm trong vùng giao

# * Một hình vuông bị giới hạn bởi:

#   * **Chiều rộng** của vùng giao
#   * **Chiều cao** của vùng giao

# 👉 Cạnh hình vuông lớn nhất =

# ```
# min(chiều rộng vùng giao, chiều cao vùng giao)
# ```

# ---

# ### 4️⃣ Diện tích hình vuông

# Nếu:

# ```
# cạnh = s
# ```

# 👉 Diện tích:

# ```
# s²
# ```

# ---

# ## Tóm tắt tư duy bài toán

# 1. Tìm **vùng giao nhau** của 2 hình chữ nhật
# 2. Nếu **không có giao** → đáp án = `0`
# 3. Nếu có:

#    * Lấy **min(width, height)** của vùng giao
#    * Bình phương lên → **diện tích hình vuông lớn nhất**

# ---

# ## Ví dụ trực quan

# * Vùng giao có:

#   * Rộng = 5
#   * Cao = 3

# 👉 Hình vuông lớn nhất chỉ có cạnh = `3`
# 👉 Diện tích = `3 × 3 = 9`

# ---

# 📌 **Lưu ý quan trọng**
# Đề hỏi **diện tích hình vuông**, **không phải cạnh**.

# ---

# Nếu bạn muốn, mình có thể:

# * ✔️ Vẽ hình minh họa
# * ✔️ Viết công thức tổng quát
# * ✔️ Giải bằng C++ / Java / Python
# * ✔️ Giải theo kiểu tư duy thi ICPC / Codeforces

# 👉 Bạn đang gặp bài này ở đâu (LeetCode, Codeforces, hay đề tiếng Việt)?

