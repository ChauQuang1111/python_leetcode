# # # # 1339. Maximum Product of Splitted Binary Tree(07/01/2026)
# # # # Dưới đây là **giải thích đề bài LeetCode 1339 – Maximum Product of Splitted Binary Tree** bằng **tiếng Việt**, theo cách dễ hiểu nhất 👇
# # # # Dưới đây là **giải thích thuật toán + thêm chú thích trực tiếp vào code** của bạn cho bài
# # # # **LeetCode 1339 – Maximum Product of Splitted Binary Tree**.
# # # # Mình giữ **logic y nguyên**, chỉ giải thích rõ **tư duy + từng dòng code làm gì**.
# Dưới đây là **giải thích thuật toán + thêm chú thích chi tiết trực tiếp vào code Python** cho bài
# **1339. Maximum Product of Splitted Binary Tree**.
# Mình giữ **đúng logic bạn đang dùng**, chỉ làm rõ tư duy và ý nghĩa từng bước.

# ---

# ## 🧠 Ý tưởng thuật toán

# 1. **Duyệt DFS hậu tố (post-order)** để:

#    * Tính **tổng của mỗi cây con**
#    * Lưu các tổng này vào `subtree_sums`
# 2. Sau khi biết:

#    * `total_sum` = tổng toàn bộ cây
#    * Với mỗi `s` trong `subtree_sums`, giả sử **cắt cạnh phía trên cây con đó**
# 3. Hai phần sẽ có tổng:

#    * `s`
#    * `total_sum - s`
# 4. Tính tích:

#    ```
#    s * (total_sum - s)
#    ```
# 5. Lấy tích lớn nhất và **modulo `10^9 + 7`**

# ⏱ Time: **O(n)**
# 📦 Space: **O(n)** (do lưu danh sách subtree sums)

# ---

# ## ✅ Code đã thêm chú thích chi tiết

# ```python
# # 1339. Maximum Product of Splitted Binary Tree
# # Ý tưởng:
# # - Tính tổng của tất cả các cây con
# # - Với mỗi cây con, thử "cắt" cạnh phía trên nó
# # - Lấy tích lớn nhất giữa 2 phần của cây


from typing import Optional
# Định nghĩa TreeNode để chạy local
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        # Danh sách lưu tổng của tất cả các cây con
        subtree_sums = []

        # Hàm DFS hậu tố để tính tổng cây con
        def get_sum(node):
            # Nếu node rỗng thì tổng = 0
            if not node:
                return 0

            # Tổng cây con tại node hiện tại
            # = giá trị node + tổng cây trái + tổng cây phải
            current_sum = (
                node.val
                + get_sum(node.left)
                + get_sum(node.right)
            )

            # Lưu tổng cây con này vào danh sách
            subtree_sums.append(current_sum)

            # Trả về tổng để node cha sử dụng
            return current_sum

        # Tổng toàn bộ cây
        total_sum = get_sum(root)

        # Biến lưu tích lớn nhất
        max_prod = 0

        # Duyệt qua từng tổng cây con
        for s in subtree_sums:
            # Nếu cắt cạnh phía trên cây con có tổng = s
            # thì phần còn lại có tổng = total_sum - s
            product = s * (total_sum - s)

            # Cập nhật tích lớn nhất
            if product > max_prod:
                max_prod = product

        # Trả kết quả theo yêu cầu đề bài
        return max_prod % (10**9 + 7)
# ```

# ---

# ## 🔎 Ví dụ tư duy tại một node

# Giả sử:

# ```
# total_sum = 30
# subtree_sum = 12
# ```

# Nếu cắt cạnh phía trên cây con này:

# * Cây 1: 12
# * Cây 2: 30 − 12 = 18
# * Tích = `12 × 18 = 216`

# 👉 Ta thử với **mọi cây con** để tìm tích lớn nhất.

# ---

# ## ⚠️ Lưu ý quan trọng

# * Không cần thật sự cắt cây → chỉ **tưởng tượng**
# * DFS **post-order** là bắt buộc để có tổng cây con
# * Không modulo trong lúc so sánh
# * Python không lo overflow nhưng **Java/C++ phải dùng `long`**

# ---

# ## 📌 So sánh nhanh 2 cách

# | Cách               | Bộ nhớ | Ý tưởng    |
# | ------------------ | ------ | ---------- |
# | Lưu `subtree_sums` | O(n)   | Dễ hiểu    |
# | Không lưu (1 DFS)  | O(h)   | Tối ưu hơn |

# Nếu bạn muốn, mình có thể:

# * ✂️ Viết **phiên bản tối ưu không dùng list**
# * 🧠 Vẽ **quá trình DFS từng bước**
# * 🆚 So sánh với **code Java của bạn**
# * 🎯 Giải thích theo **phỏng vấn FAANG**

# Chỉ cần nói tiếp nhé 👍

# /**
# #  * Definition for a binary tree node.
# #  * public class TreeNode {
# #  *     int val;
# #  *     TreeNode left;
# #  *     TreeNode right;
# #  *     TreeNode() {}
# #  *     TreeNode(int val) { this.val = val; }
# #  *     TreeNode(int val, TreeNode left, TreeNode right) {
# #  *         this.val = val;
# #  *         this.left = left;
# #  *         this.right = right;
# #  *     }
# # #  * }
# #  */

# class Solution {

#     // Tổng giá trị của toàn bộ cây
#     static long sum;

#     # // Giá trị tích lớn nhất tìm được
#     static long max;

#     # // Hằng số modulo theo đề bài
#     static int MODULO = 1000000007;

#     # /**
#     #  * Hàm tính tổng tất cả node trong cây
#     #  * Duyệt DFS đơn giản
#     #  */
#     private static long getSum(TreeNode root){
#         if(root == null){
#             return 0;
#         }

#         // Tổng = node hiện tại + tổng cây con trái + tổng cây con phải
#         return root.val + getSum(root.left) + getSum(root.right);
#     }

#     /**
#      * Hàm duyệt cây để tìm tích lớn nhất
#      * Trả về: tổng của cây con tại node hiện tại
#      */
#     private static long getMaxProduct(TreeNode root){
#         if(root == null){
#             return 0;
#         }

#         // Tính tổng cây con bên trái
#         long left = getMaxProduct(root.left);

#         // Tính tổng cây con bên phải
#         long right = getMaxProduct(root.right);

#         // Tổng cây con tại node hiện tại
#         long t1 = left + right + root.val;

#         // Nếu cắt cạnh phía trên node này:
#         // - Một phần có tổng = t1
#         // - Phần còn lại có tổng = sum - t1
#         long temp = (sum - t1) * t1;

#         // Cập nhật tích lớn nhất
#         if(temp > max){
#             max = temp;
#         }

#         // Trả tổng cây con để node cha sử dụng
#         return t1;
#     }

#     /**
#      * Hàm chính theo yêu cầu đề bài
#      */
#     public static int maxProduct(TreeNode root) {

#         // Reset giá trị max
#         max = 0;

#         // Bước 1: Tính tổng toàn bộ cây
#         sum = getSum(root);

#         // Bước 2: Duyệt DFS để tìm tích lớn nhất
#         getMaxProduct(root);

#         // Bước 3: Trả kết quả theo modulo
#         return (int)(max % MODULO);
#     }
# }

# # # ---

# # # ## 🧠 Ý tưởng thuật toán (tóm tắt)

# # # 1. **Tính tổng toàn bộ cây** → `sum`
# # # 2. **Duyệt DFS hậu tố (post-order)**:

# # #    * Với mỗi node, tính **tổng cây con** tại node đó (`t1`)
# # #    * Giả sử **cắt cạnh phía trên node**
# # #    * Hai phần có tổng:

# # #      * `t1`
# # #      * `sum - t1`
# # #    * Tích: `(sum - t1) * t1`
# # #    * Cập nhật tích lớn nhất → `max`
# # # 3. Trả về `max % (10^9 + 7)`

# # # ⏱ Thời gian: **O(n)**
# # # 📦 Bộ nhớ: **O(h)** (độ cao cây – recursion stack)

# # # ---

# # # ## ✅ Code đã thêm chú thích chi tiết

# # # ```java
# # # /**
# # #  * Definition for a binary tree node.
# # #  * public class TreeNode {
# # #  *     int val;
# # #  *     TreeNode left;
# # #  *     TreeNode right;
# # #  *     TreeNode() {}
# # #  *     TreeNode(int val) { this.val = val; }
# # #  *     TreeNode(int val, TreeNode left, TreeNode right) {
# # #  *         this.val = val;
# # #  *         this.left = left;
# # #  *         this.right = right;
# # #  *     }
# # #  * }
# # #  */

# # class Solution {

# #     # // Tổng giá trị của toàn bộ cây
# #     # static long sum;

# #     # // Giá trị tích lớn nhất tìm được
# #     # static long max;

# #     # // Hằng số modulo theo đề bài
# #     # static int MODULO = 1000000007;

# #     # /**
# #     #  * Hàm tính tổng tất cả node trong cây
# #     #  * Duyệt DFS đơn giản
# #     #  */
# #     private static long getSum(TreeNode root){
# #         if(root == null){
# #             return 0;
# #         }

# #         // Tổng = node hiện tại + tổng cây con trái + tổng cây con phải
# #         return root.val + getSum(root.left) + getSum(root.right);
# #     }

# #     # /**
# #     #  * Hàm duyệt cây để tìm tích lớn nhất
# #     #  * Trả về: tổng của cây con tại node hiện tại
# #     #  */
# #     private static long getMaxProduct(TreeNode root){
# #         if(root == null){
# #             return 0;
# #         }

# #         // Tính tổng cây con bên trái
# #         long left = getMaxProduct(root.left);

# #         // Tính tổng cây con bên phải
# #         long right = getMaxProduct(root.right);

# #         // Tổng cây con tại node hiện tại
# #         long t1 = left + right + root.val;

# #         // Nếu cắt cạnh phía trên node này:
# #         // - Một phần có tổng = t1
# #         // - Phần còn lại có tổng = sum - t1
# #         long temp = (sum - t1) * t1;

# #         // Cập nhật tích lớn nhất
# #         if(temp > max){
# #             max = temp;
# #         }

# #         // Trả tổng cây con để node cha sử dụng
# #         return t1;
# #     }

# #     /**
# #      * Hàm chính theo yêu cầu đề bài
# #      */
# #     public static int maxProduct(TreeNode root) {

# #         // Reset giá trị max
# #         max = 0;

# #         // Bước 1: Tính tổng toàn bộ cây
# #         sum = getSum(root);

# #         // Bước 2: Duyệt DFS để tìm tích lớn nhất
# #         getMaxProduct(root);

# #         // Bước 3: Trả kết quả theo modulo
# #         return (int)(max % MODULO);
# #     }
# # }
# # # ```

# # # ---

# # # ## 🔎 Minh họa logic tại 1 node

# # # Giả sử tại node X:

# # # ```
# # # subtreeSum = t1
# # # remainingSum = sum - t1
# # # product = t1 * (sum - t1)
# # # ```

# # # ➡️ Việc **“cắt cạnh phía trên X”** tương đương với việc chia cây thành:

# # # * Cây con gốc X
# # # * Phần còn lại của cây

# # # ---

# # # ## ⚠️ Lưu ý quan trọng

# # # */