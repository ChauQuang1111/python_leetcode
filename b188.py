# ## 🧩 1022. Sum of Root To Leaf Binary Numbers (24/02/2026)

# Ok mình sẽ:

# 1. ✅ Giải thích thuật toán từng bước
# 2. ✅ Thêm chú thích chi tiết trực tiếp vào code
# 3. ✅ Giải thích tại sao dùng `<< 1` và `|`

# ---

# # 🔎 Ý tưởng thuật toán

# Ta dùng **DFS (Depth-First Search)** để duyệt tất cả đường đi từ root → leaf.

# Mỗi khi đi xuống 1 node:

# ```
# current_val = current_val * 2 + node.val
# ```

# Trong code bạn viết:

# ```
# (current_val << 1) | node.val
# ```

# Giải thích:

# * `<< 1` = dịch trái 1 bit = nhân 2
# * `| node.val` = thêm bit 0 hoặc 1 vào cuối

# Ví dụ:

# ```
# current_val = 5 (101)
# node.val = 1

# 5 << 1 = 1010 (10)
# 1010 | 1 = 1011 (11)
# ```

# ---

# # 🧠 Tại sao khi gặp leaf thì return?

# Vì lúc đó ta đã tạo xong **1 số nhị phân hoàn chỉnh**, nên trả về giá trị đó để cộng vào tổng.

# ---

# ✍ Code có chú thích đầy đủ

# ```python
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        # Hàm DFS để duyệt cây
        # node: node hiện tại
        # current_val: giá trị nhị phân tính đến node hiện tại
        def dfs(node, current_val):
            
            # Nếu node rỗng → không có gì để cộng
            if not node:
                return 0
            
            # Dịch trái 1 bit (nhân 2)
            # Sau đó thêm giá trị node.val (0 hoặc 1)
            # Ví dụ:
            # current_val = 5 (101)
            # node.val = 1
            # -> 5 << 1 = 10 (1010)
            # -> 1010 | 1 = 1011 (11)
            current_val = (current_val << 1) | node.val
            
            # Nếu node hiện tại là node lá
            # (không có con trái và con phải)
            # → ta đã có 1 số nhị phân hoàn chỉnh
            if not node.left and not node.right:
                return current_val
            
            # Nếu chưa phải lá
            # Tiếp tục DFS xuống trái và phải
            # Cộng kết quả của hai nhánh lại
            left_sum = dfs(node.left, current_val)
            right_sum = dfs(node.right, current_val)
            
            return left_sum + right_sum
        
        # Bắt đầu DFS từ root
        return dfs(root, 0)
# ```

# ---

# # 🔥 Độ phức tạp

# * Thời gian: **O(N)**
#   → Mỗi node duyệt đúng 1 lần

# * Bộ nhớ: **O(H)**
#   → H là chiều cao cây (do đệ quy)


# 🎯 Tóm tắt bản chất bài

# Thực chất bài này là:

# > Duyệt mọi đường root → leaf
# > Dùng bit manipulation để xây dựng số nhị phân
# > Cộng tất cả lại

# ---

# Nếu bạn muốn mình giải thích thêm:

# * Tại sao không cần backtracking?
# * Hoặc trace từng bước trên một cây cụ thể?

# Mình sẽ vẽ từng bước cho bạn hiểu sâu luôn.


# Bài này nói về **cây nhị phân (binary tree)** mà:

# * Mỗi node chỉ có giá trị **0 hoặc 1**.
# * Mỗi đường đi từ **root → leaf** tạo thành **một số nhị phân (binary number)**.
# * Yêu cầu: **Tính tổng tất cả các số nhị phân đó (sau khi đổi sang hệ thập phân).**

# ---

# ### 📌 1. Root và Leaf là gì?

# * **Root**: node gốc (node đầu tiên của cây).
# * **Leaf**: node không có con (không có left và right).

# ---

# ### 📌 2. Ý nghĩa đề bài

# Mỗi đường đi từ root đến leaf giống như bạn ghép các số 0/1 lại thành một số nhị phân.

# Ví dụ cây:

# ```
#         1
#        / \
#       0   1
#      / \   \
#     0   1   1
# ```

# Các đường đi:

# 1. 1 → 0 → 0  → "100"
# 2. 1 → 0 → 1  → "101"
# 3. 1 → 1 → 1  → "111"

# ---

# ### 📌 3. Đổi sang hệ thập phân

# | Binary | Decimal |
# | ------ | ------- |
# | 100    | 4       |
# | 101    | 5       |
# | 111    | 7       |

# 👉 Tổng = 4 + 5 + 7 = **16**

# ---

# ### 📌 4. Bản chất thuật toán

# Mỗi lần đi xuống 1 node:

# ```
# current = current * 2 + node.val
# ```

# Vì:

# * Nhân 2 = dịch trái trong nhị phân
# * Cộng node.val (0 hoặc 1)

# Ví dụ:

# ```
# path: 1 → 0 → 1
# ```

# Tính dần:

# ```
# start = 0
# 1  -> 0*2 + 1 = 1
# 0  -> 1*2 + 0 = 2
# 1  -> 2*2 + 1 = 5
# ```

# Khi gặp leaf → cộng vào tổng.

# ---

# ### 📌 5. Tóm lại đề yêu cầu gì?

# ✔ Duyệt toàn bộ các đường từ root đến leaf
# ✔ Mỗi đường tạo thành một số nhị phân
# ✔ Chuyển sang số thập phân
# ✔ Cộng tất cả lại

# ---

# Nếu bạn muốn, mình có thể:

# * Giải bằng **DFS đệ quy**
# * Hoặc viết code Java theo style bạn đang dùng (Scanner, while, tối ưu).
