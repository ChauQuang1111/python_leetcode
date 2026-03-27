# Bài **“Matrix Similarity After Cyclic Shifts”** (27/03/2026)

# Mình sẽ giải thích **logic thuật toán** trước, rồi viết lại code của bạn với **chú thích chi tiết từng dòng** nhé.

# ---

# ## 🧠 Ý tưởng thuật toán

# 👉 Điều kiện để **sau khi cyclic shift mà ma trận vẫn giống ban đầu** là:

# * Mỗi **hàng** phải “lặp lại theo chu kỳ”
# * Tức là:
#   👉 Phần tử tại vị trí `j` phải bằng phần tử sau khi dịch `k` bước

# ---

# ### 🔑 Insight quan trọng

# Thay vì:
# ❌ Thực sự dịch trái/phải từng hàng
# ✅ Ta chỉ cần **so sánh trực tiếp bằng index**

# Cụ thể:

# [
# row[j] == row[(j + k) % n]
# ]

# 👉 Nếu đúng với **mọi j trong mọi hàng** → ma trận không đổi

# ---

# ## 💻 Code có chú thích chi tiết

# ```python
import numpy as np
from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        # m: số hàng, n: số cột
        m, n = len(mat), len(mat[0])
        
        # Vì dịch k lần giống như dịch (k % n) lần
        shift = k % n
        
        # Nếu shift = 0 → không thay đổi gì → luôn giống
        if shift == 0:
            return True
            
        # Duyệt từng hàng trong ma trận
        for row in mat:
            
            # Duyệt từng vị trí trong hàng
            for j in range(n):
                
                # So sánh:
                # - phần tử hiện tại: row[j]
                # - phần tử sau khi dịch vòng: row[(j + shift) % n]
                
                # Nếu khác nhau → sau khi shift sẽ không giống ban đầu
                if row[j] != row[(j + shift) % n]:
                    return False
        
        # Nếu tất cả đều thỏa → ma trận vẫn giống
        return True
# ```

# ---

# ## 🔍 Ví dụ để bạn hiểu sâu

# Giả sử:

# ```
# row = [1, 2, 1, 2]
# k = 2
# ```

# 👉 shift = 2

# So sánh:

# * row[0] == row[2] → 1 == 1 ✅
# * row[1] == row[3] → 2 == 2 ✅
# * row[2] == row[0] → 1 == 1 ✅
# * row[3] == row[1] → 2 == 2 ✅

# 👉 OK → hàng này **có tính chu kỳ → shift xong vẫn giống**

# ---

# ## 🚨 Điều cực quan trọng

# Code của bạn **không cần phân biệt trái/phải hay chẵn/lẻ**

# 👉 Vì bài này thực chất đang kiểm tra:

# > “Hàng có lặp lại sau k bước không?”

# ---

# ## 🧾 Tóm lại 1 câu

# 👉 Bài này = kiểm tra mỗi hàng có **chu kỳ k** hay không.

# ---

# Nếu bạn muốn, mình có thể:

# * So sánh cách này với cách **simulate dịch thật**
# * Hoặc convert sang Java (chuẩn style bạn đang dùng)


# ## 🧠 Ý tưởng chính của đề

# Bạn được cho:

# * Một ma trận ( A ) kích thước ( m \times n )
# * Một số nguyên ( k )

# Bạn cần:

# # 👉 **Xoay (shift) từng hàng hoặc từng cột theo kiểu vòng tròn (cyclic shift)**
# # 👉 Sau đó kiểm tra xem **ma trận mới có giống ma trận ban đầu hay không**

# # ---

# # ## 🔄 Cyclic Shift là gì?

# # Cyclic shift (dịch vòng) nghĩa là:

# # * Phần tử bị “đẩy ra ngoài” sẽ **quay lại đầu**

# # ### Ví dụ 1: Dịch phải 1 lần

# # Hàng:
# # `[1, 2, 3, 4]`

# # → Dịch phải 1:
# # `[4, 1, 2, 3]`

# # ---

# # ### Ví dụ 2: Dịch trái 2 lần

# `[1, 2, 3, 4]`

# → Dịch trái 2:
# `[3, 4, 1, 2]`

# ---

# ## 📌 Cụ thể bài này thường yêu cầu gì?

# ### Trường hợp phổ biến nhất:

# 👉 Với mỗi **hàng i**:

# * Nếu i là **chẵn** → dịch trái ( k ) lần
# * Nếu i là **lẻ** → dịch phải ( k ) lần

# (Sometimes đề sẽ nói rõ chiều dịch)

# ---

# ## 🎯 Nhiệm vụ của bạn

# Sau khi dịch tất cả các hàng:

# 👉 So sánh ma trận mới với ma trận ban đầu

# * Nếu **giống hệt nhau** → trả về `true`
# * Nếu **khác** → trả về `false`

# ---

# ## 🧩 Ví dụ minh họa

# ### Input:

# ```
# A = [
#  [1, 2, 3],
#  [4, 5, 6]
# ]
# k = 1
# ```

# ### Xử lý:

# * Hàng 0 (chẵn) → dịch trái 1:
#   `[1,2,3] → [2,3,1]`

# * Hàng 1 (lẻ) → dịch phải 1:
#   `[4,5,6] → [6,4,5]`

# ### Ma trận mới:

# ```
# [
#  [2, 3, 1],
#  [6, 4, 5]
# ]
# ```

# 👉 So với ban đầu → **khác** → kết quả: `false`

# ---

# ## 💡 Insight quan trọng

# Bạn **KHÔNG cần dịch thật k lần** (tốn thời gian)

# 👉 Chỉ cần:

# * Dùng công thức index:

#   * Dịch trái: `(j + k) % n`
#   * Dịch phải: `(j - k + n) % n`

# ---

# ## 🚨 Bẫy dễ sai

# * Quên `% n` (k có thể rất lớn)
# * Nhầm trái ↔ phải
# * So sánh sai index
# * Dịch xong nhưng không giữ lại ma trận gốc để so

# ---

# ## 🧾 Tóm tắt ngắn gọn

# 👉 Bài này làm 3 bước:

# 1. Với mỗi hàng → xác định hướng dịch
# 2. Tính vị trí mới bằng công thức `%`
# 3. So sánh với ma trận ban đầu

# ---

# Nếu bạn muốn, mình có thể:

# * Viết code Java (chuẩn style bạn đang dùng Scanner + while)
# * Hoặc giải từng dòng code để bạn hiểu sâu hơn 👍
