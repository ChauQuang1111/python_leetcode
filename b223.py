# Bài **“Determine Whether Matrix Can Be Obtained By Rotation”*(22/03/2026)

# Mình sẽ giải thích **ý tưởng thuật toán** trước, rồi viết lại code có **chú thích chi tiết từng dòng** để bạn hiểu rõ.

# ---

# # 🧠 Ý tưởng chính

# Thay vì:

# * Xoay `mat` 4 lần rồi so sánh

# 👉 Ta làm ngược lại:

# * **Giữ nguyên `mat`**
# * Với mỗi phần tử `mat[i][j]`, kiểm tra nó có khớp với `target` ở vị trí tương ứng sau khi xoay không

# ---

# ## 🔄 4 trường hợp xoay

# Với mỗi `(i, j)` trong `mat`:

# # | Góc xoay | Vị trí tương ứng trong `target` |
# | -------- | ------------------------------- |
# | 0°       | `target[i][j]`                  |
# | 90°      | `target[j][n-1-i]`              |
# | 180°     | `target[n-1-i][n-1-j]`          |
# | 270°     | `target[n-1-j][i]`              |

# ---

# ## ⚡ Tối ưu

# * Dùng mảng `possible = [True, True, True, True]`
# * Mỗi phần tử tương ứng với 1 góc xoay
# * Nếu sai → đánh dấu `False`
# * Nếu cả 4 đều `False` → dừng sớm (early exit)

# ---

# # ✅ Code + chú thích chi tiết

# ```python
from typing import List
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        
        # possible[0] → kiểm tra xoay 0 độ
        # possible[1] → kiểm tra xoay 90 độ
        # possible[2] → kiểm tra xoay 180 độ
        # possible[3] → kiểm tra xoay 270 độ
        possible = [True, True, True, True]

        # duyệt toàn bộ phần tử của ma trận
        for i in range(n):
            for j in range(n):

                # -------------------------
                # 0 độ: giữ nguyên
                # mat[i][j] phải == target[i][j]
                # -------------------------
                if mat[i][j] != target[i][j]:
                    possible[0] = False

                # -------------------------
                # 90 độ:
                # (i, j) → (j, n-1-i)
                # -------------------------
                if mat[i][j] != target[j][n - 1 - i]:
                    possible[1] = False

                # -------------------------
                # 180 độ:
                # (i, j) → (n-1-i, n-1-j)
                # -------------------------
                if mat[i][j] != target[n - 1 - i][n - 1 - j]:
                    possible[2] = False

                # -------------------------
                # 270 độ:
                # (i, j) → (n-1-j, i)
                # -------------------------
                if mat[i][j] != target[n - 1 - j][i]:
                    possible[3] = False

                # -------------------------
                # Nếu cả 4 trường hợp đều sai
                # → không cần kiểm tra nữa
                # -------------------------
                if not any(possible):
                    return False

        # nếu còn ít nhất 1 trường hợp đúng → return True
        return any(possible)
# ```

# ---

# # 💡 Hiểu sâu hơn (rất quan trọng)

# ## ❓ Vì sao cách này nhanh?

# * Không cần tạo ma trận mới (không cần rotate thật)
# * Chỉ check index → **O(n²)**, tối ưu nhất

# ---

## 🔥 Tư duy quan trọng bạn cần nhớ

# 👉 Thay vì:

# > "Làm biến đổi dữ liệu"

# 👉 Hãy nghĩ:

# > "Mapping index sang vị trí mới"

# ---

# ## 🧠 Mẹo nhớ nhanh

# * 90°: `(i, j) → (j, n-1-i)`
# * 180°: đảo cả hàng và cột
# * 270°: ngược lại 90°

# ---

# Nếu bạn muốn, mình có thể:

# * Vẽ hình minh họa từng phép xoay (cực dễ hiểu)
# * Hoặc cho bạn bài tương tự để luyện tư duy index 💪


# ## 🧠 Ý nghĩa đề bài

# Bạn được cho:

# * Một ma trận vuông `mat` (k × k)
# * Một ma trận vuông `target` (k × k)

# 👉 Nhiệm vụ:
# Kiểm tra xem có thể **xoay ma trận `mat`** (theo góc 90°, 180°, 270° hoặc 0°) để **trở thành `target` hay không**.

# ---

# ## 🔄 Các phép xoay hợp lệ

# Bạn có thể xoay `mat` theo chiều kim đồng hồ:

# * 0° (giữ nguyên)
# * 90°
# * 180°
# * 270°

# 👉 Sau mỗi lần xoay, so sánh với `target`.

# ---

# ## 📌 Ví dụ dễ hiểu

# ### Ví dụ 1:

# ```
# mat =
# 1 2
# 3 4

# target =
# 3 1
# 4 2
# ```

# 👉 Nếu xoay `mat` 90°:

# ```
# 3 1
# 4 2
# ```

# → trùng với `target` ✅
# => Kết quả: **True**

# ---

# ### Ví dụ 2:

# ```
# mat =
# 1 2
# 3 4

# target =
# 1 3
# 2 4
# ```

# 👉 Thử xoay mọi kiểu:

# * 0° ❌
# * 90° ❌
# * 180° ❌
# * 270° ❌

# => Không trùng
# => Kết quả: **False**

# ---

# ## ⚙️ Tóm tắt cách làm

# 1. Lặp tối đa 4 lần (ứng với 4 góc xoay)
# 2. Mỗi lần:

#    * So sánh `mat` với `target`
#    * Nếu giống → return True
#    * Nếu không → xoay tiếp 90°
# 3. Nếu thử hết mà không giống → return False

# ---

# ## 🔁 Công thức xoay 90° (quan trọng)

# Khi xoay 90°:

# ```
# mat[i][j] → mat[j][n - 1 - i]
# ```

# Hoặc cách dễ code hơn:

# * Transpose (đổi hàng ↔ cột)
# * Reverse từng hàng

# ---

# ## 💡 Hiểu bản chất

# Bài này không phải toán khó, mà là:

# * Hiểu **cách xoay ma trận**
# * Biết **so sánh 2 ma trận**

# ---

# Nếu bạn muốn, mình có thể:

# * Viết code Java / Python tối ưu
# * Hoặc vẽ hình từng bước xoay để bạn hiểu cực rõ 👀
