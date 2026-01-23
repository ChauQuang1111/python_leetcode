# // Minimum Pair Removal to Sort Array II(23/01/2026)
# // Ok, mình giải thích **đề bài “Minimum Pair Removal to Sort Array II”** theo kiểu **dễ hiểu – đúng bản chất**, không code nhé 👇
# // Ok, mình **giải thích thuật toán trong code này theo đúng luồng suy nghĩ**, từng khối một, để bạn **hiểu vì sao nó chạy được**, không chỉ là “đọc code” 👇
# // Ok👍mình**thêm`main`dùng`Scanner`**và**chú thích chi tiết trực tiếp trong code**để bạn**đọc là hiểu ngay thuật toán**,đúng kiểu đi học/đi phỏng vấn.

# // ---
# Ok 👍 mình **giải thích thuật toán của bài 3510 – Minimum Pair Removal to Sort Array II** theo đúng **Python code bạn đưa**, rồi **viết lại code có chú thích chi tiết từng bước** để bạn đọc là hiểu ngay.

# ---

# # 🧠 Ý tưởng cốt lõi của thuật toán

# Bài này **mô phỏng quá trình “xóa cặp” bằng cách gộp 2 phần tử kề nhau**:

# * Mỗi lần **chọn 2 phần tử kề nhau**
# * **Gộp chúng thành một phần tử mới = tổng**
# * Tương đương với **xóa 1 cặp**
# * Làm sao để **sau cùng mảng trở thành không giảm**

# 🎯 Mục tiêu:

# > Giảm số **cặp vi phạm thứ tự** (`a > b`) về 0 với **ít thao tác nhất**

# ---

# # 🔑 Các kỹ thuật được dùng

# 1. **Doubly Linked List giả** (bằng mảng `le`, `ri`)
# 2. **Min-Heap (priority queue)** → luôn gộp cặp có **tổng nhỏ nhất**
# 3. **Lazy deletion** → bỏ qua cặp lỗi thời
# 4. Biến `rest` = **số cặp chưa sorted**


# # 📌 Giải thích các biến quan trọng

# | Biến    | Ý nghĩa                                        |
# | ------- | ---------------------------------------------- |
# | `l`     | Mảng giá trị (bị thay đổi trong quá trình gộp) |
# | `le[i]` | chỉ số phần tử bên trái `i`                    |
# | `ri[i]` | chỉ số phần tử bên phải `i`                    |
# | `h`     | min-heap chứa `(tổng, vị trí trái)`            |
# | `rest`  | số cặp **vi phạm thứ tự**                      |
# | `ans`   | số lần remove pair                             |

# ---

# # 🧩 Ý nghĩa biến `rest`

# ```python
# rest = n - sum(1 for a, b in pairwise(l) if a <= b)
# ```

# * `pairwise(l)` → các cặp kề nhau
# * Đếm số cặp **đúng thứ tự** `a ≤ b`
# * Tổng số cặp là `n`
# * ⇒ `rest` = số cặp **sai thứ tự**

# 🎯 Khi `rest == 0` → mảng đã sorted

# ---

# # 🔁 Luồng hoạt động của vòng lặp

# 1. Lấy **cặp có tổng nhỏ nhất**
# 2. Kiểm tra cặp còn hợp lệ không (lazy deletion)
# 3. **Gỡ ảnh hưởng cũ** của cặp khỏi `rest`
# 4. **Gộp cặp**
# 5. **Tính lại ảnh hưởng mới**
# 6. Đưa các cặp mới vào heap
# 7. `ans += 1`

# ---

# # ✅ Code Python có chú thích chi tiết

# ```python
from heapq import heappush, heappop, heapify
from itertools import pairwise
from math import inf
from typing import List

class Solution:
    def minimumPairRemoval(self, l: List[int]) -> int:
        n = len(l)

        # Thêm sentinel (∞) để tránh check biên phải
        l.append(inf)

        # Mô phỏng doubly linked list
        # le[i]: chỉ số bên trái của i
        # ri[i]: chỉ số bên phải của i
        le = list(range(-1, n))
        ri = list(range(1, n + 1))

        # Min-heap lưu (tổng của cặp kề nhau, vị trí bên trái)
        h = [(a + b, i) for i, (a, b) in enumerate(pairwise(l))]
        heapify(h)

        ans = 0  # số lần remove pair

        # rest = số cặp vi phạm thứ tự (a > b)
        rest = n - sum(1 for a, b in pairwise(l) if a <= b)

        # Lặp cho đến khi mảng không giảm
        while rest > 0:
            v, i = heappop(h)
            r = ri[i]

            # ===== Lazy deletion =====
            # Bỏ qua nếu:
            # - i và r không còn kề nhau
            # - Tổng không còn đúng
            if le[r] != i or l[i] + l[r] != v:
                continue

            rr = ri[r]

            # ===== Tạm thời hoàn lại các quan hệ cũ =====
            # Vì ta sắp xóa cặp (i, r)
            rest += (l[le[i]] <= l[i])    # (le[i], i)
            rest += (l[i] <= l[r])        # (i, r)
            rest += (l[r] <= l[rr])       # (r, rr)

            # ===== Gộp i và r =====
            # i giữ lại, r bị loại bỏ
            le[rr] = i
            ri[i] = rr
            l[i] = v  # giá trị mới = tổng

            # ===== Trừ các quan hệ mới sau khi gộp =====
            rest -= 1                        # cặp (i, r) chắc chắn biến mất
            rest -= (l[le[i]] <= l[i])       # (le[i], i)
            rest -= (l[i] <= l[rr])          # (i, rr)

            # ===== Đưa các cặp mới vào heap =====
            if i:  # có phần tử bên trái
                heappush(h, (l[le[i]] + l[i], le[i]))
            if rr < n:  # có phần tử bên phải (không phải sentinel)
                heappush(h, (l[i] + l[rr], i))

            ans += 1  # một lần gộp = một lần remove pair

        return ans


# # 🧠 Tóm tắt để nhớ nhanh

# * `heap` → chọn cặp **tổng nhỏ nhất**
# * `le / ri` → linked list giả
# * `rest` → số cặp sai thứ tự
# * Mỗi vòng:

#   * gỡ ảnh hưởng cũ
#   * gộp
#   * tính ảnh hưởng mới

# 👉 Khi `rest = 0` → mảng đã sorted → dừng

# ---

# Nếu bạn muốn:

# * 🔹 So sánh **Python vs Java version**
# * 🔹 Chạy **1 test cụ thể từng bước**
# * 🔹 Giải thích **vì sao greedy này đúng**

# 👉 nói mình biết, mình làm tiếp cho bạn 👌

# // ```java

# import java.util.*;

# public class b157 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         // Nhập số phần tử
#         int n = sc.nextInt();

#         int[] nums = new int[n];
#         for (int i = 0; i < n; i++) {
#             nums[i] = sc.nextInt();
#         }

#         int result = minimumPairRemoval(nums);

#         System.out.println(result);

#         sc.close();

#     }

#     public static int minimumPairRemoval(int[] nums) {
#         int n = nums.length;
#         if (n <= 1)
#             return 0; // mảng <= 1 phần tử luôn sorted

#         // Lưu giá trị hiện tại của mỗi node (dùng long để tránh overflow)
#         long[] vals = new long[n];

#         // Mô phỏng linked list
#         int[] nexts = new int[n];
#         int[] prevs = new int[n];

#         // Đánh dấu node đã bị xóa
#         boolean[] removed = new boolean[n];

#         // Khởi tạo linked list
#         for (int i = 0; i < n; i++) {
#             vals[i] = nums[i];
#             prevs[i] = i - 1;
#             nexts[i] = i + 1;
#         }
#         nexts[n - 1] = -1; // phần tử cuối không có next

#         /*
#          * PriorityQueue lưu:
#          * [tổng của cặp kề nhau, vị trí bên trái]
#          * Ưu tiên tổng nhỏ hơn (greedy)
#          */
#         PriorityQueue<long[]> pq = new PriorityQueue<>(
#                 3 * n,
#                 (a, b) -> {
#                     if (a[0] != b[0])
#                         return Long.compare(a[0], b[0]);
#                     return Long.compare(a[1], b[1]);
#                 });

#         // Đếm số nghịch thế kề nhau
#         int unsortedCnt = 0;

#         for (int i = 0; i < n - 1; i++) {
#             if (vals[i] > vals[i + 1])
#                 unsortedCnt++;
#             pq.offer(new long[] { vals[i] + vals[i + 1], i });
#         }

#         // Nếu đã sorted ngay từ đầu
#         if (unsortedCnt == 0)
#             return 0;

#         int moves = 0; // số lần remove pair

#         // Lặp cho đến khi mảng sorted
#         while (unsortedCnt > 0 && !pq.isEmpty()) {

#             long[] top = pq.poll();
#             long sum = top[0];
#             int u = (int) top[1];

#             // ===== Loại bỏ dữ liệu lỗi thời (lazy deletion) =====
#             if (removed[u])
#                 continue;

#             int v = nexts[u];
#             if (v == -1 || removed[v])
#                 continue;

#             if (vals[u] + vals[v] != sum)
#                 continue;

#             int p = prevs[u]; // node bên trái u
#             int nextV = nexts[v]; // node bên phải v

#             moves++; // 1 lần gộp = 1 lần remove pair

#             // ===== Gỡ các nghịch thế cũ =====
#             if (p != -1 && vals[p] > vals[u])
#                 unsortedCnt--;
#             if (vals[u] > vals[v])
#                 unsortedCnt--;
#             if (nextV != -1 && vals[v] > vals[nextV])
#                 unsortedCnt--;

#             // ===== Gộp u và v =====
#             vals[u] = sum;
#             nexts[u] = nextV;
#             if (nextV != -1)
#                 prevs[nextV] = u;
#             removed[v] = true;

#             // ===== Thêm các nghịch thế mới (nếu có) =====
#             if (p != -1 && vals[p] > vals[u])
#                 unsortedCnt++;
#             if (nextV != -1 && vals[u] > vals[nextV])
#                 unsortedCnt++;

#             // Nếu đã sorted thì dừng
#             if (unsortedCnt == 0)
#                 break;

#             // ===== Đưa các cặp mới vào PQ =====
#             if (p != -1)
#                 pq.offer(new long[] { vals[p] + vals[u], p });
#             if (nextV != -1)
#                 pq.offer(new long[] { vals[u] + vals[nextV], u });
#         }

#         return moves;
#     }

# }
# /*
#  * Ý tưởng:
#  * - Mô phỏng mảng như một doubly linked list
#  * - Dùng PriorityQueue để luôn gộp (remove pair) cặp kề nhau có tổng nhỏ nhất
#  * - Theo dõi số nghịch thế kề nhau (unsortedCnt)
#  * - Khi unsortedCnt = 0 => mảng đã không giảm
#  */

# // code cho

# // nhanh (mẹo thi / phỏng vấn)

# // * `unsortedCnt` = **chìa khóa dừng**
# // * `PriorityQueue` = **chọn cặp gộp tốt nhất**
# // * `vals + nexts + prevs` = **linked list giả**
# // * `removed[]` + check stale = **lazy deletion**

# // ---

# // Nếu bạn muốn:

# // * 🔹 Viết lại **ngắn hơn cho contest**
# // * 🔹 Chạy **1 test cụ thể từng bước**
# // * 🔹 So sánh với **LNDS solution**

# // 👉 nói mình biết, mình làm tiếp 👌

# // ---

# // # 🎯 Ý tưởng lớn của thuật toán

# // Bài này **KHÔNG** giải bằng LNDS như cách chuẩn lý thuyết, mà dùng **chiến
# // lược tham lam + mô phỏng**:

# // 👉 **Mỗi lần chọn một cặp kề nhau có tổng nhỏ nhất để “gộp” lại**
# // 👉 Việc gộp tương đương với **xóa 1 cặp**, đúng 1 lần removal
# // 👉 Làm sao để **giảm dần số nghịch thế (unsorted pairs)** về 0

# // ---

# // ## 1️⃣ Mô hình hóa mảng thành “linked list”

# // ```java
# // long[] vals
# // int[] nexts, prevs
# // boolean[] removed
# // ```

# // 👉 Mảng được xem như **danh sách liên kết đôi**:

# // * `vals[i]` : giá trị hiện tại của node i
# // * `nexts[i]` : phần tử bên phải
# // * `prevs[i]` : phần tử bên trái
# // * `removed[i]` : node đã bị xóa chưa

# // 📌 Lý do:

# // * Khi gộp `(u, v)` → xóa `v`, cập nhật liên kết rất nhanh **O(1)**

# // ---

# // ## 2️⃣ Khái niệm cực kỳ quan trọng: `unsortedCnt`

# // ```java
# // if (vals[i] > vals[i + 1]) unsortedCnt++;
# // ```

# // 👉 `unsortedCnt` = **số nghịch thế kề nhau**

# // Ví dụ:

# // ```
# // [1, 5, 3, 4]
# // ↑
# // 5 > 3 → unsortedCnt = 1
# // ```

# // 🎯 **Mục tiêu**: đưa `unsortedCnt = 0`
# // → mảng trở thành **không giảm**

# // ---

# // ## 3️⃣ PriorityQueue dùng để làm gì?

# // ```java
# // pq.offer(new long[]{vals[i] + vals[i + 1], i});
# // ```

# // PQ lưu:

# // ```
# // (sum = vals[i] + vals[i+1], vị trí i)
# // ```

# // và sắp xếp theo:

# // 1. Tổng nhỏ nhất
# // 2. Index nhỏ hơn (tie-break)

# // 👉 **Luôn ưu tiên gộp cặp có tổng nhỏ nhất**
# // → giúp giá trị mới **ít phá thứ tự xung quanh**

# // 📌 Đây chính là **greedy strategy** của bài.

# // ---

# // ## 4️⃣ Vòng lặp chính

# // ```java
# // while (unsortedCnt > 0 && !pq.isEmpty())
# // ```

# // Chừng nào:

# // * Mảng chưa sorted
# // * Còn cặp để xử lý

# // ---

# // ## 5️⃣ Kiểm tra “stale” (rất quan trọng)

# // ```java
# // if (removed[u]) continue;
# // int v = nexts[u];
# // if (v == -1 || removed[v]) continue;
# // if (vals[u] + vals[v] != sum) continue;
# // ```

# // 👉 Vì PQ chứa **dữ liệu cũ**, nên phải loại bỏ:

# // * Node đã bị xóa
# // * Cặp không còn kề nhau
# // * Tổng không còn đúng

# // 📌 Đây là kỹ thuật **lazy deletion** cực kỳ phổ biến.

# // ---

# // ## 6️⃣ Một lần gộp = một lần xóa cặp

# // ```java
# // moves++;
# // ```

# // Gộp `(u, v)` thành:

# // ```
# // vals[u] = vals[u] + vals[v]
# // v bị xóa
# // ```

# // 👉 **Đúng 1 pair removal**

# // ---

# // ## 7️⃣ Cập nhật số nghịch thế (linh hồn thuật toán)

# // ### ❌ Xóa nghịch thế cũ

# // ```java
# // if (p != -1 && vals[p] > vals[u]) unsortedCnt--;
# // if (vals[u] > vals[v]) unsortedCnt--;
# // if (nextV != -1 && vals[v] > vals[nextV]) unsortedCnt--;
# // ```

# // Các cặp bị mất:

# // * `(p, u)`
# // * `(u, v)`
# // * `(v, nextV)`

# // ---

# // ### 🔁 Gộp node

# // ```java
# // vals[u] = sum;
# // nexts[u] = nextV;
# // removed[v] = true;
# // ```

# // ---

# // ### ➕ Thêm nghịch thế mới (nếu có)

# // ```java
# // if (p != -1 && vals[p] > vals[u]) unsortedCnt++;
# // if (nextV != -1 && vals[u] > vals[nextV]) unsortedCnt++;
# // ```

# // 👉 Sau khi gộp, giá trị mới có thể **tạo nghịch thế mới**

# // ---

# // ## 8️⃣ Đưa các cặp mới vào PriorityQueue

# // ```java
# // if (p != -1) pq.offer(new long[]{vals[p] + vals[u], p});
# // if (nextV != -1) pq.offer(new long[]{vals[u] + vals[nextV], u});
# // ```

# // 📌 Vì cấu trúc đã đổi, các cặp mới cần được xem xét.

# // ---

# // ## 9️⃣ Điều kiện dừng

# // ```java
# // if (unsortedCnt == 0) break;
# // ```

# // 👉 Khi **không còn nghịch thế**
# // → mảng đã **sorted**
# // → dừng ngay, không làm dư thao tác

# // ---

# // ## 🔚 Kết luận thuật toán

# // ### 🧠 Bản chất

# // * Mô phỏng quá trình **xóa cặp**
# // * Mỗi lần **tham lam gộp cặp kề nhau có tổng nhỏ nhất**
# // * Giảm dần số nghịch thế đến 0

# // ### ⏱ Độ phức tạp

# // * `O(n log n)`
# // * Phù hợp với mảng lớn

# // ---

# // ## 🧩 Tóm tắt 1 dòng để nhớ khi phỏng vấn

# // > “Dùng priority queue để luôn gộp cặp kề nhau có tổng nhỏ nhất, mô phỏng
# // linked list, và theo dõi số nghịch thế để biết khi nào mảng đã được sắp xếp.”

# // ---

# // Nếu bạn muốn:

# // * 🔹 Chạy **ví dụ cụ thể từng bước**
# // * 🔹 So sánh với lời giải **LNDS**
# // * 🔹 Chứng minh vì sao greedy này đúng

# // 👉 cứ nói, mình làm tiếp cho bạn 👍

# // ---

# // ## 1️⃣ Bài toán nói chung là gì?

# // Bạn được cho **một mảng số nguyên** `nums`.

# // 👉 **Mục tiêu**:
# // Làm sao để **biến mảng thành không giảm** (`nums[i] ≤ nums[i+1]`)
# // bằng cách **loại bỏ ít nhất số cặp phần tử**.

# // ---

# // ## 2️⃣ “Pair Removal” nghĩa là gì?

# // * Mỗi lần thao tác, bạn được **chọn 2 phần tử bất kỳ** trong mảng (không cần
# // liền kề).
# // * **Xóa cả hai phần tử đó** khỏi mảng.
# // * Một lần xóa = **1 pair removal**.

# // ⚠️ Không được xóa 1 phần tử đơn lẻ, **phải xóa theo cặp**.

# // ---

# // ## 3️⃣ Khi nào thì mảng được coi là “đã sắp xếp”?

# // Mảng được coi là **sorted (không giảm)** nếu:

# // ```
# // nums[0] ≤ nums[1] ≤ nums[2] ≤ ... ≤ nums[n-1]
# // ```

# // 📌 Mảng rỗng hoặc mảng chỉ có 1 phần tử → **luôn được coi là sorted**.

# // ---

# // ## 4️⃣ Bạn cần tìm gì?

# // 👉 **Số lần xóa cặp ít nhất** để mảng còn lại là **non-decreasing**.

# // ---

# // ## 5️⃣ Ví dụ minh họa

# // ### Ví dụ 1

# // ```
# // nums = [1, 3, 2, 4]
# // ```

# // * Mảng **chưa sorted** vì `3 > 2`
# // * Ta có thể xóa cặp `(3, 2)`

# // ➡️ Mảng còn lại:

# // ```
# // [1, 4] → sorted
# // ```

# // ✅ Số lần xóa = **1**

# // ---

# // ### Ví dụ 2

# // ```
# // nums = [5, 4, 3, 2]
# // ```

# // * Mảng giảm hoàn toàn
# // * Có thể xóa:

# // * `(5,4)`
# // * `(3,2)`

# // ➡️ Mảng rỗng → sorted

# // ✅ Số lần xóa = **2**

# // ---

# // ### Ví dụ 3

# // ```
# // nums = [1, 2, 3, 4]
# // ```

# // * Đã sorted sẵn
# // * Không cần xóa gì

# // ✅ Kết quả = **0**

# // ---

# // ## 6️⃣ Bản chất tư duy của bài này 🧠

# // 👉 Thay vì nghĩ **xóa cái gì**, hãy nghĩ ngược lại:

# // ### ❓ Giữ lại được **dãy con không giảm dài nhất** là bao nhiêu?

# // * Các phần tử **giữ lại** phải:

# // * Giữ **thứ tự ban đầu**
# // * Không giảm

# // 👉 Đây chính là:

# // > **Longest Non-Decreasing Subsequence (LNDS)**

# // ---

# // ## 7️⃣ Vì sao liên quan đến LNDS?

# // * Giả sử:

# // * Mảng có `n` phần tử
# // * LNDS dài `k`
# // * Ta cần xóa `n - k` phần tử

# // ⚠️ Nhưng:

# // * Mỗi lần xóa **2 phần tử**
# // * Nên:

# // ```
# // số lần xóa = (n - k) / 2
# // ```

# // 📌 Đề đảm bảo kết quả luôn là số nguyên (luôn xóa được theo cặp).

# // ---

# // ## 8️⃣ Tóm tắt nhanh (để nhớ khi đi thi)

# // ✔ Được xóa **2 phần tử bất kỳ** mỗi lần
# // ✔ Mục tiêu: mảng **không giảm**
# // ✔ Giữ lại **LNDS dài nhất**
# // ✔ Công thức:

# // ```
# // answer = (n - LNDS_length) / 2
# // ```

# // ---

# // Nếu bạn muốn:

# // * 🔹 Giải bằng **DP**
# // * 🔹 Giải bằng **binary search (O(n log n))**
# // * 🔹 Có **ví dụ chạy tay từng bước**
# // * 🔹 So sánh với bản **Minimum Pair Removal I**

# // 👉 chỉ cần nói mình muốn hướng nào 👍
