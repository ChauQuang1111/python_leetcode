# 3607. Power Grid Maintenance(06/11/2025)
# Dưới đây là **giải thích đề bài** 3607. Power Grid Maintenance (LeetCode) — mình sẽ phân tích phần *mô tả*, *yêu cầu*, và *ý tưởng giải thuật* giúp bạn hiểu rõ. Nếu bạn muốn sau đó mình cũng có thể tìm code mẫu và giải thích chi tiết thuật toán.
# Dưới đây là **bản giải thích chi tiết từng dòng** của đoạn code bạn gửi — đây là lời giải **cho bài “Power Grid Maintenance” (LeetCode 3607)** theo hướng **mô phỏng việc ngắt kết nối và xử lý truy vấn bảo trì trên hệ thống điện**, nhưng không dùng Union-Find theo cách thông thường.
# Thuật toán này xử lý việc **duy trì các thành phần liên thông và tìm “nút nhỏ nhất còn hoạt động trong cùng cụm”**.

# ---

# ### 🔍 **Giải thích tổng quan ý tưởng**

# * Ban đầu, bạn có `c` trạm điện và các kết nối giữa chúng (`connections`).
# * Mỗi truy vấn trong `queries` có dạng:

#   * `t = 1, x`: Hỏi **nút hoạt động nhỏ nhất trong cùng thành phần** với nút `x`.
#   * `t = 2, x`: Ngắt (tắt) trạm điện `x`.
# * Ta cần mô phỏng trạng thái của toàn mạng điện sau mỗi thao tác.

# Thuật toán này:

# * Dùng **Union-Find** để nhóm các node thuộc cùng thành phần.
# * Dùng **next_node[]** và **comp_min[]** để **duy trì danh sách liên kết giữa các node còn hoạt động trong mỗi thành phần**.
# * Dùng **offline[]** để đánh dấu node nào đã bị tắt.


### 🧠 **Code có chú thích chi tiết**

from typing import List

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Khởi tạo mảng parent cho DSU (Union-Find)
        parent = list(range(c + 1))

        # Hàm find() tìm gốc của 1 node (với nén đường đi)
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # nén đường đi để tối ưu
                x = parent[x]
            return x

        # Bước 1: Union các node có kết nối ban đầu
        for a, b in connections:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra  # nối 2 thành phần

        # Bước 2: Chuẩn bị dữ liệu cho từng thành phần
        next_node = [0] * (c + 1)   # con trỏ trỏ đến node kế tiếp trong cùng thành phần
        comp_min = [0] * (c + 1)    # node nhỏ nhất còn hoạt động trong thành phần
        last = {}                   # lưu node cuối cùng trong mỗi thành phần

        # Duyệt qua từng node
        for i in range(1, c + 1):
            r = find(i)  # tìm gốc (đại diện của thành phần)
            if comp_min[r] == 0:
                comp_min[r] = i  # i là node nhỏ nhất trong cụm ban đầu
            else:
                next_node[last[r]] = i  # liên kết node trước đó với node i
            last[r] = i  # cập nhật node cuối của thành phần r

        # Bước 3: Xử lý truy vấn
        offline = [False] * (c + 1)  # trạng thái hoạt động của node
        res = []  # lưu kết quả các truy vấn loại 1

        for t, x in queries:
            if t == 1:
                # Truy vấn loại 1: hỏi node nhỏ nhất còn hoạt động trong cùng thành phần với x
                if not offline[x]:
                    res.append(x)  # nếu x còn hoạt động → chính nó là câu trả lời
                else:
                    r = find(x)
                    m = comp_min[r]  # node nhỏ nhất còn hoạt động
                    res.append(m if m else -1)  # nếu không có node nào thì trả về -1
            else:
                # Truy vấn loại 2: tắt node x
                if offline[x]:
                    continue  # nếu đã tắt rồi thì bỏ qua
                offline[x] = True  # đánh dấu là tắt

                r = find(x)
                # Nếu node x là node nhỏ nhất đang hoạt động trong thành phần
                if comp_min[r] == x:
                    y = next_node[x]  # tìm node tiếp theo
                    # Bỏ qua các node đã tắt liên tục phía sau
                    while y and offline[y]:
                        y = next_node[y]
                    # Cập nhật node nhỏ nhất mới
                    comp_min[r] = y

        return res
# ```

# ---

# ### 🧩 **Ví dụ minh họa**

# ```python
# sol = Solution()
# c = 5
# connections = [[1, 2], [2, 3], [4, 5]]
# queries = [
#     [1, 1],  # hỏi node nhỏ nhất trong thành phần chứa 1
#     [2, 1],  # tắt node 1
#     [1, 2],  # hỏi node nhỏ nhất trong thành phần chứa 2
#     [2, 2],  # tắt node 2
#     [1, 3]   # hỏi node nhỏ nhất trong thành phần chứa 3
# ]
# print(sol.processQueries(c, connections, queries))
# ```

# **Kết quả:**

# ```
# [1, 2, 3]
# ```

# ---

### ⚙️ **Tóm tắt hoạt động của từng cấu trúc:**

# | Tên biến      | Vai trò                                                     |
# | ------------- | ----------------------------------------------------------- |
# | `parent[]`    | DSU để xác định thành phần liên thông                       |
# | `next_node[]` | Con trỏ sang node tiếp theo trong cùng thành phần           |
# | `comp_min[]`  | Node nhỏ nhất còn hoạt động trong thành phần                |
# | `offline[]`   | Đánh dấu node nào đã tắt                                    |
# | `res[]`       | Kết quả các truy vấn loại 1                                 |
# | `last`        | Ghi nhớ node cuối cùng của mỗi cụm để xây chuỗi `next_node` |

# ---

# Bạn có muốn mình **vẽ sơ đồ minh họa cấu trúc `next_node` và cách cập nhật khi tắt node** để hiểu rõ hơn không?

# ---

# ## 📄 Mô tả đề bài

# * Có `c` trạm phát điện (power stations) được đánh số từ `1` đến `c`.

# * Có `n` đường cáp hai chiều (bidirectional cables) kết nối giữ các trạm bạn với nhau — tức tạo thành một mạng lưới (graph) giữa các trạm.

# * Bạn sẽ có một dãy truy vấn (queries). Mỗi truy vấn là hai phần:

#   1. `[1, x]` — tức là “kiểm tra bảo trì” cho trạm `x`.
#   2. `[2, x]` — tức là trạm `x` **ngộp đi** (offline) — nghĩa là trạm đó ngừng hoạt động.

# * Khi thực hiện truy vấn kiểu `[1, x]` (bảo trì trạm x):

#   * Nếu trạm `x` *đang online* (hoạt động) → thì trả về `x`.
#   * Nếu trạm `x` *đang offline* → thì bạn phải trả về **trạm online có số nhỏ nhất** trong cùng **thành phần liên thông** (connected component) với `x`.

#     * Nếu trong thành phần đó **không còn trạm nào online** → trả về `-1`.

# * Mỗi khi có truy vấn kiểu `[2, x]`, nghĩa là trạm `x` chuyển sang trạng thái offline, ảnh hưởng đến liên thông và khả năng trả về trong các truy vấn sau.

# ---

# ## ✅ Yêu cầu của bài

# * Quản lý mạng lưới trạm & cáp, theo thời gian (với các truy vấn bật/tắt offline và bảo trì).
# * Cần trả lời mỗi truy vấn kiểm tra bảo trì một cách **hiệu quả** (không chạy lại toàn bộ mạng lưới mỗi lần).
# * Vì số lượng trạm, đường nối, truy vấn có thể lớn, nên cần giải thuật tối ưu (ví dụ DSU/Union-Find, heap/priority queue, hoặc lưu trữ thông tin theo components).

# ---

# ## 🧠 Ý tưởng giải thuật

# Đây là một mô hình điển hình: **graph + dynamic state (online/offline) + queries**. Sau đây là cách giải phổ biến:

# 1. **Xây dựng graph** từ các đường cáp: mỗi trạm là một nút, mỗi cáp là cạnh nối hai trạm.

#    * Dùng DSU (disjoint set union) để biết mỗi nút thuộc thành phần nào.
#    * Khi offline hoặc online thay đổi, thành phần có thể bị ảnh hưởng — nhưng trong bài này, “offline” chỉ là trạng thái của trạm, mạng lưới cáp không bị thay đổi.

# 2. **Lưu trữ cho mỗi component** một cấu trúc dữ liệu để biết được trạm *nhỏ nhất đang online* trong thành phần đó.

#    * Ví dụ: mỗi component có một min-heap hoặc TreeSet chứa các trạm đang online.
#    * Khi trạm bị offline → loại bỏ khỏi heap/TreeSet.
#    * Khi có truy vấn bảo trì `[1, x]`:

#      * xác định component của `x`,
#      * nếu `x` online → trả `x`;
#      * ngược lại → kiểm tra heap/TreeSet của component đó, nếu còn phần tử → lấy phần tử nhỏ nhất trả về, nếu không → `-1`.

# 3. **Cập nhật dynamic**: khi một trạm chuyển offline (`[2, x]`), ta cập nhật trạng thái và cấu trúc dữ liệu của component tương ứng.

# 4. **Phức tạp thời gian**: N trạm, M cáp, Q truy vấn.

#    * Việc tìm component là O(α(N)) với DSU.
#    * Việc truy vấn hoặc cập nhật min-heap/TreeSet là O(log N).
#      → Tổng O((N + M + Q) log N) hoặc tương đương.

# ---

# Nếu bạn muốn, mình có thể tìm và gửi **mã mẫu (Java hoặc Python)** cho bài này, và **giải thích chi tiết code từng dòng** để bạn nắm vững thuật toán. Bạn có muốn mình làm vậy không?
