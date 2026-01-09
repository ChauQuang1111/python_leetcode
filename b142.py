# Smallest Subtree with all the Deepest Nodes(09/01/2026)
# Dưới đây là **giải thích dễ hiểu đề bài “Smallest Subtree with all the Deepest Nodes”** (LeetCode 865), bằng tiếng Việt 👇
# Mình sẽ **giải thích thuật toán từng bước** và **thêm chú thích trực tiếp vào code** cho bạn, theo đúng đoạn code bạn đưa 👍
# (giải thích theo tư duy DFS – đúng kiểu hay gặp khi phỏng vấn)

# ---

# ## 1. Ý tưởng chính của thuật toán

# Thuật toán dùng **DFS (Depth-First Search)** để làm **2 việc cùng lúc**:

# ### (1) Tìm độ sâu lớn nhất của cây (`maxDepth`)

# * Khi DFS chạm tới `None` → tức là **đi hết 1 nhánh**
# * Cập nhật `maxDepth` = độ sâu lớn nhất từng đạt được

# ### (2) Tìm node thấp nhất bao trùm toàn bộ các node sâu nhất

# * Nếu:

#   * `leftDepth == rightDepth`
#   * **và** độ sâu đó chính là `maxDepth`
# * ⇒ node hiện tại chính là **root của subtree nhỏ nhất chứa tất cả node sâu nhất**

# ---

# ## 2. Vì sao điều kiện `left == right == maxDepth` đúng?

# * `left == right`
#   👉 Các node sâu nhất **xuất hiện ở cả 2 nhánh trái và phải**

# * `== maxDepth`
#   👉 Các node đó **thực sự là sâu nhất trong toàn cây**

# ➡️ Node hiện tại là **Lowest Common Ancestor (LCA)** của tất cả node sâu nhất
# ➡️ Đây chính là **smallest subtree**

# ---

# ## 3. Giải thích chi tiết từng bước DFS

# Giả sử gọi:

# ```python
# dfs(root, 0)
# ```

# ### DFS trả về cái gì?

# 👉 **Độ sâu lớn nhất của subtree hiện tại**

# ---

# ### Trường hợp 1: `root == None`

# ```python
# if not root:
#     self.maxDepth = max(self.maxDepth, depth)
#     return depth
# ```

# * Ta đã đi tới cuối một nhánh
# * Cập nhật `maxDepth`
# * Trả về độ sâu hiện tại

# ---

# ### Trường hợp 2: node bình thường

# ```python
# left = self.dfs(root.left, depth + 1)
# right = self.dfs(root.right, depth + 1)
# ```

# * DFS trái → lấy độ sâu sâu nhất bên trái
# * DFS phải → lấy độ sâu sâu nhất bên phải

# ---

# ### Kiểm tra điều kiện cập nhật kết quả

# ```python
# if left == right and left == self.maxDepth:
#     self.res = root
# ```

# * Hai bên sâu bằng nhau
# * Đúng bằng độ sâu lớn nhất toàn cây
#   ➡️ `root` là câu trả lời (hoặc ghi đè kết quả cũ vì node này thấp hơn)

# ---

# ### Trả về độ sâu lớn nhất của subtree

# ```python
# return max(left, right)
# ```

# ---

# ## 4. Code có chú thích chi tiết

# ```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = None          # Lưu root của subtree nhỏ nhất cần tìm
        self.maxDepth = -1       # Độ sâu lớn nhất của toàn bộ cây

    def dfs(self, root, depth):
        # Nếu gặp node None → đã đi đến cuối một nhánh
        if not root:
            # Cập nhật độ sâu lớn nhất
            self.maxDepth = max(self.maxDepth, depth)
            return depth

        # DFS sang trái và phải
        left = self.dfs(root.left, depth + 1)
        right = self.dfs(root.right, depth + 1)

        # Nếu hai bên có cùng độ sâu
        # và độ sâu đó là lớn nhất toàn cây
        # => root là subtree nhỏ nhất chứa tất cả node sâu nhất
        if left == right and left == self.maxDepth:
            self.res = root

        # Trả về độ sâu lớn nhất của subtree hiện tại
        return max(left, right)

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # Bắt đầu DFS từ root với depth = 0
        self.dfs(root, 0)
        return self.res
# ```

# ---

# ## 5. Độ phức tạp

# * **Time Complexity:** `O(n)`
#   → Mỗi node duyệt đúng 1 lần

# * **Space Complexity:** `O(h)`
#   → Stack đệ quy, `h` là chiều cao cây

# ---

## 6. Một câu tóm tắt để nhớ lâu (đi thi/phỏng vấn)

# > **DFS trả về độ sâu sâu nhất của mỗi subtree;
# > khi trái và phải chạm maxDepth cùng lúc, node hiện tại chính là smallest subtree chứa tất cả deepest nodes.**

# ---

# Nếu bạn muốn mình:

# * 🔹 Vẽ **flow DFS từng bước**
# * 🔹 Viết lại theo **kiểu bottom-up dễ hiểu hơn**
# * 🔹 So sánh với cách dùng **LCA**

# 👉 cứ nói, mình làm tiếp cho bạn 👌

# ---

# ## 1. Đề bài nói gì?

# Bạn được cho **một cây nhị phân (binary tree)**.

# 👉 Nhiệm vụ:
# Tìm **cây con nhỏ nhất** (smallest subtree) sao cho **cây con đó chứa TẤT CẢ các node sâu nhất** trong cây.

# 👉 Trả về **node gốc (root)** của cây con đó.

# ---

# ## 2. Giải thích các khái niệm quan trọng

# ### 🔹 Node sâu nhất là gì?

# * **Độ sâu (depth)** của một node = số cạnh từ **root** đến node đó.
# * **Node sâu nhất** là node có **độ sâu lớn nhất** trong cây.

# Ví dụ:

# ```
#         3
#        / \
#       5   1
#      / \
#     6   2
#          \
#           7
# ```

# * Node `7` có độ sâu lớn nhất → là node sâu nhất.

# ---

# ### 🔹 Cây con (subtree) là gì?

# * Một cây con gồm **một node bất kỳ** và **toàn bộ các node con của nó**.

# Ví dụ:
# Nếu chọn node `5` làm root thì cây con là:

# ```
#     5
#    / \
#   6   2
#        \
#         7
# ```

# ---

# ### 🔹 “Smallest subtree” nghĩa là gì?

# * Trong tất cả các cây con **chứa đủ các node sâu nhất**,
#   → chọn **cây con có ít node nhất**
#   → tương đương với **node thấp nhất (deepest) nhưng vẫn bao trùm hết các node sâu nhất**.

# ---

# ## 3. Ví dụ minh họa

# ### Ví dụ 1:

# ```
#         3
#        / \
#       5   1
#      / \
#     6   2
# ```

# * Node sâu nhất: `6` và `2` (cùng độ sâu)
# * Cây con nhỏ nhất chứa **cả 6 và 2** là cây có root = `5`

# 👉 **Kết quả: node 5**

# ---

# ### Ví dụ 2:

# ```
#         1
#        / \
#       2   3
# ```

# * Node sâu nhất: `2` và `3`
# * Cây con nhỏ nhất chứa cả hai là toàn bộ cây

# 👉 **Kết quả: node 1**

# ---

# ### Ví dụ 3:

# ```
#     1
#      \
#       2
#        \
#         3
# ```

# * Node sâu nhất: `3`
# * Cây con nhỏ nhất chứa node đó chính là node `3`

# 👉 **Kết quả: node 3**

# ---

# ## 4. Tóm tắt đề bài bằng 1 câu

# > **Hãy tìm node thấp nhất trong cây sao cho toàn bộ các node sâu nhất đều nằm trong cây con của node đó.**

# ---

# ## 5. Gợi ý tư duy (chưa phải lời giải code)

# * Nếu **các node sâu nhất nằm ở cả trái và phải** → kết quả là **node hiện tại**
# * Nếu **chỉ nằm một phía** → đi xuống phía đó
# * Thường giải bằng **DFS + tính chiều cao cây**

# ---

# Nếu bạn muốn:

# * ✅ Giải thích **bằng hình vẽ từng bước**
# * ✅ Viết **code Java / Python**
# * ✅ Giải theo **tư duy phỏng vấn**

# 👉 cứ nói mình sẽ làm tiếp nhé 👍
