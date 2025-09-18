# 3408. Design Task Manager(18/09/2025)
# Ok 👍 mình sẽ thêm chú thích trực tiếp vào code của bạn để dễ hiểu hơn.

# ```python
import heapq
from typing import List

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = []     # heap (min-heap) lưu trữ các task theo dạng (-priority, -taskId, userId)
        self.valid = {}     # dictionary: ánh xạ taskId -> phiên bản hợp lệ nhất của task

        # Khởi tạo heap và valid từ danh sách ban đầu
        for user, task, priority in tasks:
            # Lưu thành tuple: (-priority, -taskId, user)
            #   - Dùng số âm để biến min-heap thành max-heap (priority cao nhất ở đầu)
            #   - Dùng -taskId để ưu tiên taskId nhỏ hơn khi priority bằng nhau
            t = (-priority, -task, user)
            self.tasks.append(t)
            self.valid[-task] = t   # ghi nhớ phiên bản hợp lệ nhất cho taskId này
        
        heapq.heapify(self.tasks)   # biến self.tasks thành heap hợp lệ
       

    def add(self, userId: int, taskId: int, priority: int) -> None:
        # Thêm task mới vào heap và valid
        t = (-priority, -taskId, userId)
        self.valid[-taskId] = t     # ghi nhớ taskId này phiên bản hợp lệ nhất
        heapq.heappush(self.tasks, t)
        

    def edit(self, taskId: int, newPriority: int) -> None:
        # Lấy task cũ từ valid
        old_pri, old_task, old_user = self.valid[-taskId]
        # Tạo task mới với priority cập nhật
        t = (-newPriority, old_task, old_user)
        self.valid[-taskId] = t     # cập nhật phiên bản hợp lệ
        heapq.heappush(self.tasks, t)  # đẩy vào heap (bản cũ vẫn nằm trong heap nhưng sẽ bị bỏ qua sau)

    def rmv(self, taskId: int) -> None:
        # Xóa task khỏi valid (không cần xóa ngay trong heap → lazy deletion)
        del self.valid[-taskId]

    def execTop(self) -> int:
        # Trả về userId của task ưu tiên nhất, đồng thời loại bỏ task đó khỏi hệ thống
        while self.tasks:
            pri, tsk, usr = heapq.heappop(self.tasks)  # lấy task ưu tiên nhất ra

            if tsk not in self.valid:
                # Nếu taskId này không còn trong valid → đã bị remove
                continue
            
            if self.valid[tsk][0] != pri or self.valid[tsk][2] != usr:
                # Nếu priority hoặc userId không khớp với bản mới nhất trong valid → là bản cũ
                continue
            
            # Đây là bản hợp lệ nhất → xóa khỏi valid và return userId
            del self.valid[tsk]
            return usr
            
        return -1   # nếu không còn task hợp lệ nào
# ```

# ---

# ### ✅ Tóm gọn ý nghĩa từng phần

# * **Heap (`self.tasks`)**: chứa tất cả phiên bản (cả cũ và mới).
# * **Valid (`self.valid`)**: chỉ giữ phiên bản mới nhất của mỗi `taskId`.
# * **Lazy deletion**: khi `edit` hoặc `rmv`, bản cũ không xóa khỏi heap ngay mà được bỏ qua trong `execTop`.
# * **Ưu tiên trong heap**:

#   1. `priority` cao hơn → đứng trước.
#   2. Nếu bằng nhau → `taskId` nhỏ hơn → đứng trước.



# Bạn có muốn mình viết thêm **1 ví dụ chạy thử step-by-step** (từng lệnh `add`, `edit`, `execTop`) để thấy cách heap và valid thay đổi theo không?

# Rồi 👍, mình sẽ giải thích chi tiết từng bước thuật toán của đoạn code `TaskManager` bạn đưa.

# ---

# ## 📝 Ý tưởng bài toán

# Ta cần một **Task Manager** hỗ trợ 4 thao tác:

# 1. **add(userId, taskId, priority)**
#    Thêm một task mới cho user với `taskId` và `priority`.

# 2. **edit(taskId, newPriority)**
#    Thay đổi độ ưu tiên của task có sẵn.

# 3. **rmv(taskId)**
#    Xóa một task theo `taskId`.

# 4. **execTop()**
#    Lấy và xóa task có **priority cao nhất**, nếu bằng nhau thì `taskId` nhỏ hơn sẽ ưu tiên, trả về `userId` của task đó.

# ---

# ## ⚡ Chi tiết thuật toán trong code

# ### 1. Dữ liệu được lưu trữ

# * `self.tasks`: **heap** (ưu tiên max) để lưu tất cả task theo dạng tuple:

#   ```python
#   t = (-priority, -taskId, userId)
#   ```

#   * Dùng `-priority` để biến min-heap của Python thành max-heap (priority cao hơn sẽ đứng trước).
#   * Dùng `-taskId` vì nếu hai task có cùng priority → taskId nhỏ hơn được ưu tiên.
#   * `userId` dùng để biết ai sở hữu task.

# * `self.valid`: dictionary để giữ **task hợp lệ nhất hiện tại** theo `taskId`.

#   ```python
#   self.valid[-taskId] = t
#   ```

#   Dùng `-taskId` làm key để khớp với heap.

# 👉 Lý do: Một task có thể bị chỉnh sửa nhiều lần (`edit`) → heap sẽ chứa nhiều bản copy cũ. `valid` giúp phân biệt bản **mới nhất** và bỏ qua bản cũ.

# ---

# ### 2. `__init__`

# ```python
# for user, task, priority in tasks:
#     t = (-priority, -task, user)
#     self.tasks.append(t)
#     self.valid[-task] = t
# heapify(self.tasks)
# ```

# * Khởi tạo heap `tasks` với tất cả task.
# * Mỗi task gắn vào `valid` → chỉ giữ phiên bản mới nhất.

# ---

# ### 3. `add(userId, taskId, priority)`

# ```python
# t = (-priority, -taskId, userId)
# self.valid[-taskId] = t
# heappush(self.tasks, t)
# ```

# * Tạo tuple mới `t`.
# * Lưu vào `valid` (ghi đè nếu `taskId` đã tồn tại).
# * Đẩy vào heap.

# ---

# ### 4. `edit(taskId, newPriority)`

# ```python
# old_pri, old_task, old_user = self.valid[-taskId]
# t = (-newPriority, old_task, old_user)
# self.valid[-taskId] = t
# heappush(self.tasks, t)
# ```

# * Lấy ra task cũ từ `valid`.
# * Tạo tuple mới với priority cập nhật.
# * Ghi đè vào `valid`.
# * Đẩy thêm vào heap (bản cũ vẫn nằm trong heap nhưng sẽ bị bỏ qua khi `execTop`).

# ---

# ### 5. `rmv(taskId)`

# ```python
# del self.valid[-taskId]
# ```

# * Xóa task khỏi `valid`.
# * Bản ghi cũ trong heap vẫn còn, nhưng khi `execTop` sẽ bị bỏ qua vì không có trong `valid`.

# ---

# ### 6. `execTop`

# ```python
# while self.tasks:
#     pri, tsk, usr = heappop(self.tasks)

#     if tsk not in self.valid:
#         continue  # task đã bị remove

#     if self.valid[tsk][0] != pri or self.valid[tsk][2] != usr:
#         continue  # đây là bản cũ, bỏ qua

#     del self.valid[tsk]
#     return usr
# return -1
# ```

# * Lấy task ưu tiên nhất từ heap (`heappop`).
# * Nếu `tsk` không có trong `valid` → đã bị `rmv` → bỏ qua.
# * Nếu `pri` hoặc `usr` không khớp với bản mới nhất trong `valid` → đây là bản cũ (do `edit`) → bỏ qua.
# * Khi gặp bản **hợp lệ nhất** → xóa khỏi `valid` và return `userId`.
# * Nếu heap trống → return `-1`.

# ---

# ## ✅ Tóm tắt cơ chế

# * Dùng **heap** để lấy ra task ưu tiên cao nhất.
# * Dùng **valid** để loại bỏ các bản ghi cũ (lazy deletion).
# * Mỗi thao tác `add` hoặc `edit` chỉ cần thêm bản mới vào heap, không cần xoá bản cũ ngay.
# * `execTop` chịu trách nhiệm bỏ qua bản ghi lỗi thời.

# ---

# Bạn có muốn mình viết **phiên bản Java** tương tự (sử dụng `PriorityQueue` + `HashMap`) cho bài này không?

# Dưới đây là phần **giải thích rõ ràng, ngắn gọn** cho bài **LeetCode 3408 — Design Task Manager**, kèm ý tưởng dữ liệu & độ phức tạp. (Mình tham khảo mô tả bài từ LeetCode và các giải thích chuẩn). ([leetcode.com][1])

# ---

# ## 1) Mục tiêu bài toán (tóm tắt)

# Bạn phải triển khai một hệ thống quản lý task hỗ trợ khởi tạo với danh sách ban đầu và các thao tác sau:

# * **Constructor**: khởi tạo từ danh sách `tasks`, mỗi phần tử là `[userId, taskId, priority]`.
# * **add(userId, taskId, priority)**: thêm task mới (taskId là duy nhất).
# * **edit(taskId, newPriority)**: thay đổi priority của task đã tồn tại.
# * **rmv(taskId)**: xóa task.
# * **execTop()**: *thực thi* (lấy và xóa) task có **priority cao nhất**; nếu có nhiều task cùng priority thì chọn `taskId` lớn hơn (hoặc theo quy tắc đề bài — trong một số giải pháp dùng taskId lớn hơn làm tie-break). Nếu không có task trả về `-1`.

# (Chi tiết tên hàm/qui tắc tie-break hơi khác ở các nguồn/phiên bản, ý chính: hệ thống cần add/edit/remove và trả về task priority cao nhất). ([Leetcode][2])

# ---

# ## 2) Yêu cầu chức năng quan trọng

# * Truy xuất và cập nhật theo `taskId` phải nhanh (cho `edit`, `rmv`).
# * Lấy task có **priority cao nhất** phải nhanh (cho `execTop`).
# * Các thao tác chạy hiệu quả với nhiều phép update/xóa (tối ưu khoảng `O(log n)` mỗi thao tác là tiêu chuẩn).

# ---

# ## 3) Cách lưu trữ dữ liệu (ý tưởng chuẩn)

# Dùng kết hợp 2 cấu trúc:

# 1. **Map (hash)**: `taskId -> (userId, priority)` để tra cứu và cập nhật task theo `taskId` trong O(1).
# 2. **Cấu trúc sắp xếp / heap / balanced BST** để lấy nhanh task có priority cao nhất:

#    * Có thể dùng **max-heap / priority queue** lưu `(priority, taskId)`; để tie-break theo taskId dùng thứ tự phù hợp.
#    * Vì priority có thể thay đổi hoặc task bị xóa, heap sẽ chứa các bản *cũ* → cần kỹ thuật **lazy deletion**: khi pop top, kiểm tra xem priority hiện tại của `taskId` trong map có khớp không; nếu không khớp thì bỏ và pop tiếp.
#    * Hoặc dùng **ordered set / TreeSet / std::set** (C++) lưu trực tiếp các cặp `(-priority, -taskId)` (đảm bảo ordering), đồng thời giữ iterator/handle để xóa phần tử cũ khi `edit`/`rmv` (xóa O(log n)). Đây là cách “sạch” nếu ngôn ngữ hỗ trợ xóa theo iterator nhanh. ([zxi.mytechroad.com][3])

# ---

# ## 4) Các thao tác triển khai (chi tiết thuật toán)

# * **Constructor(tasks)**

#   * Duyệt list `tasks`, với mỗi `[userId, taskId, priority]`:

#     * lưu `taskMap[taskId] = (userId, priority)`.
#     * push `(priority, taskId)` vào heap (hoặc insert vào set).
#   * Tổng chi phí: O(n log n) nếu insert vào heap/set.

# * **add(userId, taskId, priority)**

#   * `taskMap[taskId] = (userId, priority)`; push `(priority, taskId)` vào heap.
#   * O(log n) cho push.

# * **edit(taskId, newPriority)**

#   * Cập nhật map: `taskMap[taskId].priority = newPriority`.
#   * Push `(newPriority, taskId)` vào heap (không xóa bản cũ ngay).
#   * (Nếu dùng ordered set với handle → erase old pair rồi insert new pair, vẫn O(log n)).
#   * O(log n).

# * **rmv(taskId)**

#   * Xoá entry khỏi `taskMap`.
#   * Nếu dùng set với handle: erase pair trong set O(log n).
#   * Nếu dùng heap + lazy deletion: chỉ xóa khỏi `taskMap` (bản cũ trong heap sẽ bị bỏ khi gặp ở top).
#   * O(log n) nếu xóa trực tiếp, amortized O(1) (map removal) + lazy cost later if heap used.

# * **execTop()**

#   * Nếu heap rỗng → trả `-1`.
#   * Lặp: lấy top `(p, id)` từ heap. Kiểm tra `taskMap`:

#     * Nếu `id` không còn trong `taskMap` (đã rmv) hoặc `taskMap[id].priority != p` (phiên bản cũ), thì `pop` và tiếp tục.
#     * Nếu khớp → lấy `userId = taskMap[id].userId`, xóa `taskMap[id]` (task đã thực thi), `pop` khỏi heap, trả `userId`.
#   * Mỗi phần tử bị bỏ khỏi heap chỉ một lần → tổng amortized O(log n) per pop.

# ---

# ## 5) Ví dụ ngắn

# Giả sử tasks ban đầu: `[[1, 101, 5], [2, 102, 7], [3,103,7]]`

# * execTop() → trả user có task priority 7; nếu có 2 task priority 7 thì theo tie-break (ví dụ chọn taskId lớn hơn) chọn một trong hai theo quy tắc.
# * edit(101, 8) → cập nhật priority, push phiên bản mới vào heap; execTop() tiếp theo sẽ trả userId của task 101.

# ---

# ## 6) Lựa chọn dữ liệu & ưu/nhược

# * **Heap + HashMap (lazy deletion)**

#   * Ưu: triển khai đơn giản, mỗi add/edit là O(log n).
#   * Nhược: heap chứa nhiều bản stale, nhưng mỗi bản stale bị pop tối đa 1 lần → amortized tốt.
# * **Ordered set / Tree (map) + HashMap + iterator handle**

#   * Ưu: có thể xóa trực tiếp bản cũ O(log n) → heap sạch hơn.
#   * Nhược: cần cấu trúc hỗ trợ erase bằng iterator (C++ `set` hoặc Java `TreeSet` + custom objects + maintain references).

# ---

# ## 7) Độ phức tạp (tóm tắt)

# * Constructor: O(n log n).
# * `add`, `edit`, `rmv`, `execTop`: **amortized O(log n)**.
# * Không gian: O(n) (heap + map). ([walkccc.me][4])

# ---

# Nếu bạn muốn mình:

# * Viết **mã mẫu** (Java / Python / C++) theo kiểu **heap + map (lazy deletion)**, hoặc
# * Viết **mã dùng TreeSet** (xóa trực tiếp) trong Java/C++,

# hãy nói rõ bạn muốn ngôn ngữ nào — mình sẽ viết code hoàn chỉnh kèm giải thích.

# [1]: https://leetcode.com/problems/design-task-manager/?utm_source=chatgpt.com "Design Task Manager - LeetCode"
# [2]: https://leetcode.ca/2025-01-21-3408-Design-Task-Manager/?utm_source=chatgpt.com "3408 - Design Task Manager - leetcode.ca"
# [3]: https://zxi.mytechroad.com/blog/priority-queue/leetcode-3408-design-task-manager/?utm_source=chatgpt.com "花花酱LeetCode 3408. Design Task Manager - Huahua's Tech Road"
# [4]: https://walkccc.me/LeetCode/problems/3408/?utm_source=chatgpt.com "3408. Design Task Manager - LeetCode Solutions - walkccc.me"
