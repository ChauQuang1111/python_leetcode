# Minimum Absolute Difference(26/01/2026)
# **Minimum Absolute Difference – Giải thích đề bài (dễ hiểu)**
# Ok 👍 mình **giải thích thuật toán từng bước** và **thêm chú thích trực tiếp vào code** cho bạn, đúng theo cách tư duy khi học / đi thi.

# ---

# ## 🔹 Ý tưởng thuật toán (nhắc lại ngắn gọn)

# 1. **Sắp xếp mảng**
# 2. Tính hiệu tuyệt đối giữa **các phần tử kề nhau**
# 3. Tìm **hiệu nhỏ nhất**
# 4. Lấy ra **các cặp phần tử có hiệu = min**

# 👉 Vì sau khi sắp xếp, cặp có hiệu nhỏ nhất **chỉ có thể nằm cạnh nhau**

# ---

# ## 🔹 Code có chú thích chi tiết

# ```python
import numpy as np
from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        # 1. Chuyển list arr sang numpy array và sắp xếp tăng dần
        # Ví dụ: arr = [3, 1, 4] -> a = [1, 3, 4]
        a = np.sort(np.array(arr))
        
        # 2. Tính hiệu giữa các phần tử kề nhau
        # diff_a[i] = a[i+1] - a[i]
        # Ví dụ: a = [1, 3, 4] -> diff_a = [2, 1]
        diff_a = np.diff(a)
        
        # 3. Tìm hiệu nhỏ nhất trong mảng diff_a
        min_abs = np.min(diff_a)

        # 4. Tìm tất cả chỉ số i sao cho diff_a[i] == min_abs
        # inds là mảng các chỉ số thỏa mãn điều kiện
        inds, = np.where(diff_a == min_abs)
        
        # 5. Với mỗi chỉ số i, cặp số tương ứng là [a[i], a[i+1]]
        res = []
        for i in inds:
            res.append([int(a[i]), int(a[i + 1])])

        # 6. Trả về danh sách các cặp có hiệu tuyệt đối nhỏ nhất
        return res
# ```

# ---

# ## 🔹 Minh họa nhanh bằng ví dụ

# ```text
# arr = [4, 2, 1, 3]

# Sau khi sort:
# a = [1, 2, 3, 4]

# diff_a = [1, 1, 1]
# min_abs = 1

# Các cặp thỏa mãn:
# [1, 2], [2, 3], [3, 4]
# ```

# ---

## 🔹 Độ phức tạp

# * Sắp xếp: `O(n log n)`
# * diff, min, where: `O(n)`
# * Tổng: **O(n log n)** ✅

# # ---

# ## 🔹 Lưu ý khi đi thi / phỏng vấn

# * Ý tưởng **sort + so sánh phần tử kề nhau** là điểm mấu chốt
# * Có thể **không dùng numpy** nếu bị giới hạn thư viện (LeetCode khuyến khích Python thuần)

# Nếu bạn muốn, mình có thể:

# * Viết lại **bản Python không dùng numpy**
# * So sánh **2 cách làm (numpy vs thường)**
# * Giải thích tại sao **không cần dùng abs()** sau khi sort

# Cứ nói nhé 👌

# Đề bài thường gặp trên LeetCode với nội dung như sau 👇

# ---

# ### 📌 Đề bài (tóm tắt)

# Bạn được cho **một mảng số nguyên `nums`**.
# Nhiệm vụ của bạn là:

# 👉 **Tìm giá trị nhỏ nhất của hiệu tuyệt đối giữa hai phần tử bất kỳ trong mảng**.

# ---

# ### 📌 Hiệu tuyệt đối là gì?

# Hiệu tuyệt đối giữa hai số `a` và `b` là:

# [
# |a - b|
# ]

# Ví dụ:

# * (|3 - 5| = 2)
# * (|7 - 2| = 5)

# ---

# ### 📌 Ví dụ minh họa

# **Ví dụ 1:**

# ```text
# nums = [3, 1, 4]
# ```

# Xét mọi cặp:

# * |3 − 1| = 2
# * |3 − 4| = 1
# * |1 − 4| = 3

# 👉 **Kết quả = 1**

# ---

# **Ví dụ 2:**

# ```text
# nums = [1, 5, 3, 19, 18, 25]
# ```

# Sắp xếp mảng:

# ```text
# [1, 3, 5, 18, 19, 25]
# ```

# Hiệu các cặp liền kề:

# * |1 − 3| = 2
# * |3 − 5| = 2
# * |5 − 18| = 13
# * |18 − 19| = 1 ✅
# * |19 − 25| = 6

# 👉 **Kết quả = 1**

# ---

# ### 📌 Ý tưởng quan trọng của đề

# ❗ Không cần so sánh **mọi cặp** (O(n²) – quá chậm)

# 👉 **Cách đúng**:

# 1. **Sắp xếp mảng**
# 2. Chỉ cần so sánh **các phần tử đứng cạnh nhau**
# 3. Lấy hiệu nhỏ nhất

# 📌 Lý do:

# * Sau khi sắp xếp, hai số **gần nhau nhất về giá trị** chắc chắn nằm **cạnh nhau**

# ---

# ### 📌 Độ phức tạp

# * Sắp xếp: `O(n log n)`
# * Duyệt mảng: `O(n)`
# * Tổng: **O(n log n)** ✅

# ---

# ### 📌 Tóm gọn 1 câu

# > **Minimum Absolute Difference** yêu cầu tìm khoảng cách nhỏ nhất giữa hai số bất kỳ trong mảng, và cách làm tối ưu là **sắp xếp mảng rồi so sánh các phần tử kề nhau**.

# ---

# Nếu bạn muốn, mình có thể:

# * Giải thích **code Java / C++ / Python**
# * So sánh với bài **Minimum Difference with k elements**
# * Hoặc hướng dẫn cách **tự suy luận khi đi thi** 💡
