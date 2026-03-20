# Bài **“Minimum Absolute Difference in Sliding Submatrix”(20/03/2026)

# Mình sẽ giải thích **ý tưởng + annotate trực tiếp vào code** để bạn hiểu rõ từng dòng 👇

# ---

# ## 🧠 Ý tưởng chính của thuật toán

# * Dùng **sliding window 2D (k × k)**
# * Với mỗi cửa sổ:

#   * Lưu các phần tử trong một mảng **đã sort (`cur`)**
#   * Khi trượt sang phải:

#     * ❌ Xóa cột bên trái
#     * ➕ Thêm cột bên phải
# * Sau đó:

#   * Tính **minimum absolute difference** bằng cách:

#     * So sánh các phần tử **liền kề trong mảng đã sort**

# 👉 Trick quan trọng:

# * Dùng `bisect` (`insort`, `bisect_left`) để:

#   * Thêm/xóa mà vẫn giữ sorted order

# ---

# ## ✅ Code + chú thích chi tiết

# ```python
from bisect import bisect_left, insort
from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        # Kết quả: kích thước (rows-k+1) x (cols-k+1)
        res = [[0] * (cols - k + 1) for _ in range(rows - k + 1)]

        # Hàm tính minimum absolute difference trong 1 window (đã SORT)
        def diff(window):
            # Nếu ít hơn 2 phần tử → không có cặp
            if len(window) < 2:
                return 0

            min_diff = float('inf')

            # Vì window đã sort → chỉ cần check phần tử kề nhau
            for i in range(len(window) - 1):
                d = window[i+1] - window[i]

                # Chỉ lấy hiệu > 0 (tránh trùng số)
                if d > 0 and d < min_diff:
                    min_diff = d

            # Nếu không tìm được (tất cả giống nhau)
            return min_diff if min_diff != float('inf') else 0

        # Duyệt từng hàng bắt đầu của window
        for r in range(rows - k + 1):

            cur = []  # chứa k*k phần tử của window hiện tại (luôn SORT)

            # 🔹 Build window đầu tiên của hàng (cột 0)
            for i in range(k):
                for j in range(k):
                    insort(cur, grid[r+i][j])  # chèn giữ sorted

            # Tính kết quả cho cột đầu tiên
            res[r][0] = diff(cur)

            # 🔹 Trượt sang phải
            for c in range(1, cols - k + 1):

                # ❌ Xóa cột bên trái (cột c-1)
                for i in range(k):
                    remove = grid[r+i][c-1]

                    # tìm vị trí phần tử cần xóa
                    index = bisect_left(cur, remove)
                    cur.pop(index)

                # ➕ Thêm cột bên phải mới (c+k-1)
                for i in range(k):
                    add = grid[r+i][c+k-1]
                    insort(cur, add)

                # Tính min diff cho window hiện tại
                res[r][c] = diff(cur)

        return res


## 🔥 Điểm mấu chốt bạn cần nhớ

### 1. Vì sao phải SORT?

# 👉 Để tìm min |a - b| nhanh:

# * Chỉ cần check **phần tử liền kề**
# * Không cần O(n²)

# ---

# ### 2. Vì sao dùng `bisect`?

# 👉 Vì Python không có `multiset` như C++

# * `insort` → chèn O(n)
# * `bisect_left` → tìm vị trí O(log n)

# ---

### 3. Sliding window 2D hoạt động thế nào?

# Mỗi lần trượt ngang:

# | Hành động | Số phần tử |
# | --------- | ---------- |
# | Xóa       | k phần tử  |
# | Thêm      | k phần tử  |

# ---

## ⏱️ Độ phức tạp

# * Có ~ (m × n) window
# * Mỗi lần:

#   * Insert + remove: O(k log k) (thực tế ~ O(k²) vì list shift)
#   * diff: O(k²)

# 👉 Tổng: ~ **O(m * n * k²)**

# ---

# ## 🚀 Nếu muốn tối ưu hơn

# Có thể dùng:

# * `SortedList` (from sortedcontainers)
# * hoặc cấu trúc như **balanced BST / multiset**

# ---

# ## 🎯 Tóm lại (cực ngắn)

# 👉 Bài này làm theo flow:

# 1. Giữ window luôn **sorted**
# 2. Trượt → update bằng xóa + thêm
# 3. Tính min diff bằng **adjacent check**

# ---

# Nếu bạn muốn, mình có thể:

# * Vẽ hình sliding window (rất dễ hiểu)
# * Hoặc viết version **Java (TreeSet)** cho bạn (chuẩn interview)

# ---

# ## 🧠 1. Hiểu từng phần của tên bài

# ### 🔹 “Submatrix” (ma trận con)

# Là một phần hình chữ nhật lấy ra từ ma trận lớn.

# Ví dụ ma trận 4x4, bạn lấy một vùng 2x2 bên trong → đó là **submatrix**.

# ---

# ### 🔹 “Sliding”

# Tức là **trượt cửa sổ (sliding window)**.

# Bạn có một submatrix kích thước cố định (ví dụ k × k), rồi:

# * Đặt nó ở góc trái trên
# * Sau đó **trượt sang phải**, rồi xuống dưới
# * Duyệt qua tất cả các vị trí có thể

# ---

# ### 🔹 “Minimum Absolute Difference”

# Trong mỗi submatrix:

# * Xét tất cả các phần tử bên trong
# * Tìm **hiệu tuyệt đối nhỏ nhất giữa 2 số bất kỳ**

# Công thức:
# [
# |a - b|
# ]

# ---

# ## 📌 2. Tóm tắt đề bài

# Cho:

# * Một ma trận số nguyên kích thước m × n
# * Một số k (kích thước submatrix)

# Yêu cầu:
# 👉 Với mỗi submatrix k × k khi trượt trên ma trận:

# * Tính **minimum absolute difference** giữa mọi cặp phần tử trong submatrix đó

# 👉 Output:

# * Một ma trận kết quả (kích thước (m-k+1) × (n-k+1))
# * Mỗi ô là kết quả của submatrix tương ứng

# ---

# ## 🔍 3. Ví dụ đơn giản

# Ma trận:

# ```
# 1 5 3
# 8 2 6
# 4 7 9
# ```

# k = 2

# Các submatrix 2x2:

# ### Submatrix 1:

# ```
# 1 5
# 8 2
# ```

# Các số: [1, 5, 8, 2]
# → sort: [1, 2, 5, 8]
# → hiệu nhỏ nhất:

# * |1-2| = 1  ✅ nhỏ nhất

# ---

# ### Submatrix 2:

# ```
# 5 3
# 2 6
# ```

# → [5, 3, 2, 6] → sort → [2, 3, 5, 6]
# → min diff = 1

# ---

# 👉 Làm tương tự cho tất cả

# ---

# ## ⚠️ 4. Insight quan trọng

# 💡 Để tìm minimum absolute difference:

# * Không cần so sánh mọi cặp (O(n²))
# * 👉 Chỉ cần:

#   1. Sort các phần tử
#   2. So sánh **các phần tử kề nhau**

# ---

# ## 🚀 5. Độ khó của bài

# Khó ở chỗ:

# * Phải xử lý **sliding window 2D**
# * Mỗi lần lại phải:

#   * Lấy k×k phần tử
#   * Tính min diff nhanh

# 👉 Nếu làm brute force → dễ TLE

# ---

# ## 📌 6. Tóm lại 1 câu

# 👉 Bài này yêu cầu:

# > Trượt một cửa sổ k×k trên ma trận, và với mỗi vị trí, tìm hiệu tuyệt đối nhỏ nhất giữa hai số bất kỳ trong cửa sổ đó.

# ---

# Nếu bạn muốn, mình có thể:

# * Giải code Java tối ưu (TreeSet / multiset)
# * Hoặc breakdown cách tối ưu từ O(n⁴) → O(n² log n)

# 👉 Bạn đang làm trên LeetCode hay bài thi?
