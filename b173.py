# #  Balanced Binary Tree(08/02/2026)
# Ok 👍 — mình sẽ:

# * Giải thích **thuật toán Python** của bạn
# * Thêm **chú thích chi tiết ngay trong code**
# * Giải thích luồng chạy để bạn hiểu bản chất

# ---

# # 🧠 Ý tưởng thuật toán (nhắc lại nhanh)

# Thuật toán gồm 2 bước:

# 1️⃣ **Inorder traversal**
# → Lấy node theo thứ tự tăng dần (sorted)

# 2️⃣ **Build lại BST cân bằng**
# → Luôn chọn phần tử giữa làm root

# ---

# ✅ Code đã thêm chú thích chi tiết

# ```python
# Definition for a binary tree node.
# Đây là cấu trúc node của cây nhị phân
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # Giá trị node
        self.left = left      # Con trái
        self.right = right    # Con phải


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Danh sách dùng để lưu các node theo thứ tự inorder (tăng dần)
        nodes = []

        # ===== BƯỚC 1: INORDER TRAVERSAL =====
        # Duyệt cây theo thứ tự: Left -> Root -> Right
        # Vì là BST nên kết quả sẽ sorted
        def inorder_traversal(root):

            # Nếu node rỗng thì dừng
            if not root:
                return 

            # Duyệt cây con trái
            inorder_traversal(root.left)

            # Thêm node hiện tại vào danh sách
            nodes.append(root)

            # Duyệt cây con phải
            inorder_traversal(root.right)


        # ===== BƯỚC 2: BUILD BST CÂN BẰNG =====
        # Xây lại cây từ mảng node đã sorted
        def build_balanced_bst(start, end):

            # Điều kiện dừng của đệ quy
            if start > end:
                return None
            
            # Lấy phần tử giữa làm root
            # Giúp cây cân bằng (số node trái ≈ phải)
            mid = (start + end) // 2

            # Lấy node giữa
            root = nodes[mid]

            # Xây cây con trái từ nửa bên trái
            root.left = build_balanced_bst(start, mid - 1)

            # Xây cây con phải từ nửa bên phải
            root.right = build_balanced_bst(mid + 1, end)

            return root


        # Gọi inorder để lấy danh sách node sorted
        inorder_traversal(root)

        # Build lại BST cân bằng và trả về root mới
        return build_balanced_bst(0, len(nodes) - 1)
# ```

# ---

# # 🔍 Giải thích luồng chạy

# Giả sử BST ban đầu lệch:

# ```
# 1
#  \
# #   2
#    \
#     3
#      \
#       4
# ```

# ---

# ## Bước 1 — Inorder

# Chạy:

# ```
# nodes = [1, 2, 3, 4]
# ```

# (đã sorted)

# ---

# ## Bước 2 — Build balanced

# ### Lần 1

# ```
# mid = 1 → root = 2
# # ```

# # Chia:

# # * Trái: `[1]`
# # * Phải: `[3,4]`

# # ---

# # ### Lần 2 — build phải

# # ```
# # mid = 2 → root = 3
# # ```

# # Phải của 3 → 4

# # ---

# # ## Cây kết quả

# # ```
    #   2
#      / \
#     1   3
#            \
#             4
# ```

# → Balanced hơn cây cũ.

# ---

# 📊 Độ phức tạp

### Time

# | Bước    | Complexity |
# | ------- | ---------- |
# | Inorder | O(n)       |
# | Build   | O(n)       |
# | Tổng    | **O(n)**   |

# ---

# ### Space

# | Thành phần      | Bộ nhớ   |
# | --------------- | -------- |
# | List nodes      | O(n)     |
# | Recursion stack | O(log n) |

# ---

# # ⚠️ Lưu ý quan trọng

# Bạn đang:

# ```python
# nodes.append(root)
# ```

# → Lưu **node thật** (không phải value)

# Nên khi build lại:

# * Không tạo node mới
# * Chỉ đổi con trái/phải

# Đây là cách tối ưu bộ nhớ 👍

# ---

# # 🧾 Tóm tắt thuật toán

# ```
# 1. Duyệt inorder → lấy node sorted
# 2. Chọn mid làm root
# 3. Build trái từ nửa trái
# 4. Build phải từ nửa phải
# 5. Trả về cây cân bằng
# ```

# ---

# Nếu bạn muốn, mình có thể làm thêm:

# * Viết bản **không dùng nested function**
# * Viết bản **chỉ lưu value**
# * Dry run cây lớn
# * So sánh với AVL / Red-Black
# * Viết iterative

# Bạn muốn mình mở rộng phần nào?
