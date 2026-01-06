# // Bài **Maximum Level Sum of a Binary Tree** (06/01/2026)
# // //
# // Mình giải thích **thuật toán trong code của bạn** theo từng phần, đúng trọng tâm để bạn dễ nhớ khi đi thi / phỏng vấn.
# import java.util.*;

# public class b141 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         // Nhập cây theo level-order, -1 là null
#         TreeNode root = buildTree(sc);

#         // In ra level có tổng lớn nhất
#         System.out.println(maxLevelSum(root));

#         sc.close();
#     }

#     static TreeNode buildTree(Scanner sc) {
#         if (!sc.hasNextInt())
#             return null;

#         int val = sc.nextInt();
#         if (val == -1)
#             return null;

#         TreeNode root = new TreeNode(val);
#         Queue<TreeNode> queue = new LinkedList<>();
#         queue.add(root);

#         while (!queue.isEmpty() && sc.hasNextInt()) {
#             TreeNode curr = queue.poll();

#             // Node con trái
#             int leftVal = sc.nextInt();
#             if (leftVal != -1) {
#                 curr.left = new TreeNode(leftVal);
#                 queue.add(curr.left);
#             }

#             // Node con phải
#             if (!sc.hasNextInt())
#                 break;
#             int rightVal = sc.nextInt();
#             if (rightVal != -1) {
#                 curr.right = new TreeNode(rightVal);
#                 queue.add(curr.right);
#             }
#         }
#         return root;
#     }

#     // Định nghĩa TreeNode như LeetCode
#     static class TreeNode {
#         int val;
#         TreeNode left;
#         TreeNode right;

#         TreeNode(int val) {
#             this.val = val;
#         }
#     }

#     // Lưu level sâu nhất của cây (0-based)
#     static int maxLevel = 0;

#     public static int maxLevelSum(TreeNode root) {

#         // Mảng lưu tổng các node theo level
#         // sum[i] = tổng giá trị các node ở level i
#         int[] sum = new int[10000];

#         // DFS bắt đầu từ root ở level 0
#         dfs(root, 0, sum);

#         // Tìm level có tổng lớn nhất
#         int max = Integer.MIN_VALUE;
#         int level = 0;

#         for (int i = 0; i <= maxLevel; i++) {
#             if (sum[i] > max) {
#                 max = sum[i];
#                 level = i;
#             }
#         }

#         // +1 vì đề bài dùng level bắt đầu từ 1
#         return level + 1;
#     }

#     // DFS để cộng tổng theo level
#     static void dfs(TreeNode root, int currLevel, int[] sum) {
#         // Điều kiện dừng
#         if (root == null) {
#             return;
#         }

#         // Cộng giá trị node hiện tại vào level tương ứng
#         sum[currLevel] += root.val;

#         // Cập nhật level sâu nhất
#         maxLevel = Math.max(maxLevel, currLevel);

#         // DFS sang con trái và con phải
#         dfs(root.left, currLevel + 1, sum);
#         dfs(root.right, currLevel + 1, sum);
#     }
# }

# // ## 1. Ý tưởng tổng quát của thuật toán

# // 👉 Bạn đang giải bài **Maximum Level Sum of a Binary Tree (1161)** bằng:

# // > **DFS (Depth First Search) + mảng lưu tổng theo level**

# // Thay vì BFS (queue), bạn:

# // * Dùng DFS để đi khắp cây
# // * Mỗi lần đi xuống, biết mình đang ở **level nào**
# // * Cộng giá trị node vào `sum[level]`
# // * Sau khi duyệt xong → tìm level có tổng lớn nhất

# // ---

# // ## 2. Phân tích từng biến quan trọng

# // ```java
# // int maxLevel = 0;
# // ```

# // * Lưu **level sâu nhất** của cây (tính từ 0)
# // * Dùng để biết duyệt mảng `sum` đến đâu

# // ```java
# // int sum[] = new int[10000];
# // ```

# // * `sum[i]` = tổng giá trị các node ở **level i**
# // * Level tính từ **0** (root ở level 0)

# // ---

# // ## 3. Hàm `dfs()` – cốt lõi thuật toán

# // ```java
# // void dfs(TreeNode root, int currLevel, int[] sum)
# // ```

# // ### Điều kiện dừng

# // ```java
# // if (root == null) return;
# // ```

# // → Đến node rỗng thì dừng

# // ---

# // ### Cộng giá trị node vào đúng level

# // ```java
# // sum[currLevel] += root.val;
# // ```

# // Ví dụ:

# // * Node đang ở level 2
# // * `sum[2] += root.val`

# // ---

# // ### Cập nhật level sâu nhất

# // ```java
# // maxLevel = Math.max(maxLevel, currLevel);
# // ```

# // → Để sau này chỉ duyệt mảng `sum` từ `0 → maxLevel`

# // ---

# // ### DFS xuống 2 nhánh

# // ```java
# // dfs(root.left, currLevel + 1, sum);
# // dfs(root.right, currLevel + 1, sum);
# // ```

# // ➡️ Mỗi khi xuống con → level tăng 1

# // ---

# // ## 4. Hàm `maxLevelSum()` – xử lý kết quả

# // ### Bước 1: Duyệt cây

# // ```java
# // dfs(root, 0, sum);
# // ```

# // → Root bắt đầu ở level 0

# // ---

# // ### Bước 2: Tìm level có tổng lớn nhất

# // ```java
# // int max = Integer.MIN_VALUE;
# // for (int i = 0; i <= maxLevel; i++) {
# // if (sum[i] > max) {
# // max = sum[i];
# // level = i;
# // }
# // }
# // ```

# // ✔️ Duyệt từ level nhỏ → lớn
# // ✔️ Chỉ cập nhật khi `sum[i] > max`
# // ➡️ Nếu bằng nhau → giữ level nhỏ hơn (đúng yêu cầu đề)

# // ---

# // ### Bước 3: Trả kết quả

# // ```java
# // return level + 1;
# // ```

# // ⚠️ Vì:

# // * Code dùng level **0-based**
# // * Đề bài yêu cầu **1-based**

# // ---

# // ## 5. Ví dụ chạy thuật toán

# // Cây:

# // ```
# // 1
# // / \
# // 7 0
# // / \
# // 7 -8
# // ```

# // Sau DFS:

# // ```
# // sum[0] = 1
# // sum[1] = 7
# // sum[2] = -1
# // maxLevel = 2
# // ```

# // → Max = 7 ở level 1
# // → Trả `1 + 1 = 2`

# // ---

# // ## 6. Độ phức tạp

# // ### Thời gian

# // * DFS duyệt mỗi node **1 lần**

# // ```
# // O(N)
# // ```

# // ### Bộ nhớ

# // * Mảng `sum`: O(H) (H = chiều cao cây)
# // * Stack DFS: O(H)

# // ---

# // ## 7. Nhận xét & cải tiến (quan trọng)

# // ### 👍 Điểm tốt

# // * Logic đúng
# // * Không cần queue
# // * Dễ viết trong DFS

# // ### ⚠️ Có thể cải thiện

# // 1. **Không nên dùng mảng cứng `10000`**

# // * Có thể dùng `ArrayList<Integer>`

# // 2. Biến `currLevel` khai báo ngoài **không dùng**
# // → Có thể xóa

# // ---

# // ## 8. So sánh nhanh DFS vs BFS

# // | Cách | Ưu điểm | Nhược điểm |
# // | ----------- | ------------------- | ---------- |
# // | DFS + sum[] | Gọn, dễ code | Cần mảng |
# // | BFS | Tự nhiên theo level | Cần Queue |

# // ---

# // ## 9. Kết luận 1 câu (để nhớ)

# // > **Dùng DFS để cộng tổng theo level, sau đó duyệt mảng tìm level có tổng lớn
# // nhất, trả về level nhỏ nhất nếu trùng.**

# // Nếu bạn muốn:

# // * Viết lại **phiên bản tối ưu hơn**
# // * Chuyển sang **BFS**
# // * Hoặc **giải thích kiểu trả lời phỏng vấn**

# // 👉 Nói mình biết nhé 👍

# // ## 1. Đề bài nói gì? (Diễn giải dễ hiểu)

# // Bạn được cho **một cây nhị phân**.
# // Mỗi node có một giá trị (có thể âm hoặc dương).

# // 👉 **Level (mức)** được tính như sau:

# // * Level 1: node gốc (root)
# // * Level 2: các con trực tiếp của root
# // * Level 3: các con của level 2
# // * …

# // ### Nhiệm vụ:

# // * Tính **tổng giá trị các node ở từng level**
# // * Tìm **level có tổng lớn nhất**
# // * Nếu có **nhiều level có cùng tổng lớn nhất**, **trả về level nhỏ nhất**

# // ---

# // ## 2. Ví dụ minh họa

# // ### Ví dụ 1:

# // ```
# // 1
# // / \
# // 7 0
# // / \
# // 7 -8
# // ```

# // Tính tổng từng level:

# // * Level 1: `1` → tổng = **1**
# // * Level 2: `7 + 0 = 7`
# // * Level 3: `7 + (-8) = -1`

# // 👉 Tổng lớn nhất là **7**, ở **level 2**

# // ➡️ **Kết quả: 2**

# // ---

# // ### Ví dụ 2:

# // ```
# // 989
# // \
# // 10250
# // / \
# // 98693 -89388
# // /
# // -32127
# // ```

# // * Level 1: `989`
# // * Level 2: `10250`
# // * Level 3: `98693 + (-89388) = 9305`
# // * Level 4: `-32127`

# // 👉 Tổng lớn nhất là **98693**, ở **level 3**

# // ➡️ **Kết quả: 3**

# // ---

# // ## 3. Cốt lõi của bài toán

# // Bài này thực chất kiểm tra bạn có biết:

# // * **Duyệt cây theo từng level (Level Order Traversal / BFS)**
# // * **So sánh và cập nhật tổng lớn nhất**

# // Không cần DFS phức tạp.

# // ---

# // ## 4. Ý tưởng giải (logic)

# // 1. Dùng **Queue** để duyệt cây theo BFS
# // 2. Khởi tạo:

# // * `level = 1`
# // * `maxSum = -∞`
# // * `answerLevel = 1`
# // 3. Với mỗi level:

# // * Duyệt hết các node trong level đó
# // * Tính `sumLevel`
# // 4. Nếu:

# // ```
# // sumLevel > maxSum
# // ```

# // thì:

# // * Cập nhật `maxSum`
# // * Ghi lại `answerLevel = level`
# // 5. Tăng `level` và tiếp tục

# # // ---

# # // ## 5. Những điểm dễ sai ⚠️

# # // * ❌ Quên xử lý **giá trị âm**
# # // * ❌ Nếu tổng bằng nhau mà cập nhật level mới → **sai**
# # // * ✅ Chỉ cập nhật khi `sumLevel > maxSum`
# # // * ✅ BFS là lựa chọn đúng nhất

# # // ---

# # // ## 6. Độ khó & kiến thức liên quan

# # // * **Độ khó:** Easy – Medium
# # // * **Kiến thức cần:**

# # // * Binary Tree
# # // * Queue
# # // * Breadth-First Search (BFS)

# # // ---

# # // Nếu bạn muốn:

# # // * Mình có thể **viết code Java / Python**
# # // * Hoặc **so sánh BFS vs DFS**
# # // * Hoặc **giải thích theo kiểu đi thi thuật toán**

# # // 👉 Cứ nói nhé 👍
# Mình sẽ **giải thích thuật toán BFS (Level Order)** của đoạn code Python bạn đưa và **thêm chú thích trực tiếp vào code**, đúng kiểu dễ nhớ khi học thuật toán / đi thi.

# ---

# ## 1. Ý tưởng thuật toán (tóm gọn)

# 👉 Dùng **BFS (Breadth-First Search)** để duyệt **từng level của cây nhị phân**.

# Với mỗi level:

# 1. Tính tổng giá trị các node trong level đó
# 2. So sánh với tổng lớn nhất đã gặp
# 3. Nếu lớn hơn → cập nhật level hiện tại là kết quả

# ➡️ Vì duyệt từ level 1 → n, nên **nếu có nhiều level cùng tổng**, level nhỏ nhất sẽ được giữ lại (đúng yêu cầu đề).

# ---

# ## 2. Giải thích từng biến quan trọng

# | Biến            | Ý nghĩa                            |
# | --------------- | ---------------------------------- |
# | `queue`         | Lưu các node cần duyệt theo BFS    |
# | `level_size`    | Số node ở level hiện tại           |
# | `level_sum`     | Tổng giá trị node ở level hiện tại |
# | `current_level` | Level đang xét (1-based)           |
# | `max_sum`       | Tổng lớn nhất từng gặp             |
# | `max_level`     | Level có tổng lớn nhất             |

# ---

# ## 3. Code **có chú thích chi tiết**

# ```python
from collections import deque

class Solution:
    def maxLevelSum(self, root):
        # Nếu cây rỗng thì không có level nào
        if not root:
            return 0

        # Queue dùng cho BFS, bắt đầu với node gốc
        queue = deque([root])

        # Lưu tổng lớn nhất từng gặp
        max_sum = float('-inf')

        # Level có tổng lớn nhất (đề bài tính level từ 1)
        max_level = 1

        # Level hiện tại đang xét
        current_level = 1

        # BFS: duyệt từng level
        while queue:

            # Số node ở level hiện tại
            level_size = len(queue)

            # Tổng giá trị các node ở level hiện tại
            level_sum = 0

            # Duyệt hết các node trong level
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                # Thêm con trái vào queue (nếu có)
                if node.left:
                    queue.append(node.left)

                # Thêm con phải vào queue (nếu có)
                if node.right:
                    queue.append(node.right)

            # Nếu tổng level hiện tại lớn hơn tổng lớn nhất
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level

            # Sang level tiếp theo
            current_level += 1

        # Trả về level có tổng lớn nhất
        return max_level


## 4. Ví dụ chạy thuật toán

# Cây:

# ```
#         1
#        / \
#       7   0
#      / \
#     7  -8
# ```

# | Level | Node  | Tổng |
# | ----- | ----- | ---- |
# | 1     | 1     | 1    |
# | 2     | 7, 0  | 7    |
# | 3     | 7, -8 | -1   |

# ➡️ Tổng lớn nhất = **7** → level **2**

# ---

# ## 5. Độ phức tạp

# * **Thời gian:** `O(N)` (mỗi node duyệt đúng 1 lần)
# * **Bộ nhớ:** `O(W)` (W là số node lớn nhất ở 1 level)

# ---

# ## 6. So sánh nhanh BFS vs DFS (như bạn đã học)

# | BFS                       | DFS                    |
# | ------------------------- | ---------------------- |
# | Duyệt theo level tự nhiên | Cần lưu level thủ công |
# | Dễ hiểu cho bài này       | Code gọn               |
# | Dùng Queue                | Dùng đệ quy            |

# ---

# ## 7. 1 câu kết luận để nhớ

# > **Dùng BFS, mỗi vòng while xử lý đúng 1 level, tính tổng và cập nhật level có tổng lớn nhất.**

# Nếu bạn muốn:

# * Viết lại **bằng DFS**
# * Chuyển sang **Java**
# * Hoặc **tối ưu cho phỏng vấn**

# 👉 Cứ nói nhé 👍
