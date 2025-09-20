# 3508. Implement Router(20/09/2025)
import bisect
from collections import deque, defaultdict
from typing import List, DefaultDict

class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit          # Giới hạn bộ nhớ (số packet tối đa)
        self.deque = deque()                    # Hàng đợi FIFO lưu packet (theo thứ tự thời gian)
        self.packet_set = set()                 # Set để tránh packet trùng lặp
        # Map: destination → danh sách timestamp đã SẮP XẾP
        self.dest_packets: DefaultDict[int, List[int]] = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)

        # Nếu packet đã tồn tại → không thêm
        if packet in self.packet_set:
            return False
        
        # Nếu bộ nhớ đầy → loại bỏ packet cũ nhất
        if len(self.deque) == self.memoryLimit:
            oldest = self.deque.popleft()       # Lấy packet đầu tiên (cũ nhất)
            self.packet_set.remove(oldest)      # Xóa khỏi set
            s_old, d_old, t_old = oldest        # Giải nén gói cũ
            arr_old = self.dest_packets[d_old]  # Lấy danh sách timestamp của destination cũ
            # Tìm vị trí timestamp trong danh sách và xóa đi
            idx_old = bisect.bisect_left(arr_old, t_old)
            del arr_old[idx_old]
        
        # Thêm packet mới
        self.deque.append(packet)                          # Đưa vào hàng đợi
        self.packet_set.add(packet)                        # Đưa vào set
        arr_new = self.dest_packets[destination]           # Lấy danh sách timestamp theo đích
        bisect.insort(arr_new, timestamp)                  # Chèn timestamp đúng vị trí (giữ sắp xếp)
        return True

    def forwardPacket(self) -> List[int]:
        # Nếu router rỗng → không có gì để forward
        if not self.deque:
            return []

        # Lấy packet cũ nhất ra
        packet = self.deque.popleft()
        self.packet_set.remove(packet)
        s, d, t = packet

        # Xóa timestamp trong danh sách dest_packets
        arr = self.dest_packets[d]
        idx = bisect.bisect_left(arr, t)
        del arr[idx]

        # Trả về packet vừa forward
        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        # Nếu chưa có packet nào cho destination này
        if destination not in self.dest_packets:
            return 0

        arr = self.dest_packets[destination]  # Lấy danh sách timestamp đã sắp xếp

        # Tìm vị trí đầu tiên >= startTime
        left_index = bisect.bisect_left(arr, startTime)
        # Tìm vị trí đầu tiên > endTime
        right_index = bisect.bisect_right(arr, endTime)

        # Số phần tử nằm trong đoạn [startTime, endTime]
        return right_index - left_index

# Dưới đây mình giải thích **đề bài LeetCode 3508 — Implement Router** (bằng tiếng Việt), tóm gọn yêu cầu, các phương thức, và ý tưởng/data-structure để cài đặt hiệu quả.
# Bạn đang viết bài **LeetCode 3508 – Implement Router**. Mình giải thích chi tiết thuật toán bạn đã code nhé 👇

# ---

# ## 1. Ý tưởng tổng quát

# * Router giống như một **hàng đợi FIFO** (First-In-First-Out) để lưu các packet (gói tin).
# * Mỗi gói tin = `(source, destination, timestamp)`.
# * Router có **giới hạn bộ nhớ** `memoryLimit`: nếu đầy thì phải loại bỏ gói tin cũ nhất (đầu hàng đợi).
# * Ba chức năng:

#   1. **addPacket**: thêm gói tin mới nếu chưa tồn tại và nếu đầy thì bỏ gói cũ nhất.
#   2. **forwardPacket**: lấy ra gói cũ nhất và xoá khỏi router.
#   3. **getCount**: đếm số packet đến cùng một `destination` trong một khoảng thời gian `[startTime, endTime]`.

# ---

# ## 2. Các cấu trúc dữ liệu bạn dùng

# * `self.deque` → lưu toàn bộ packet theo thứ tự FIFO.
# * `self.packet_set` → tập hợp để phát hiện **trùng packet** (trùng source, dest, timestamp).
# * `self.dest_packets[destination]` → danh sách **các timestamp đã sắp xếp** của những packet có cùng `destination`.

#   * Nhờ danh sách sắp xếp này, ta có thể dùng `bisect` (tìm nhị phân) để đếm nhanh số lượng packet trong khoảng thời gian.

# ---

# ## 3. Giải thích từng hàm

# ### (a) `addPacket`

# ```python
# def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
#     packet = (source, destination, timestamp)
#     if packet in self.packet_set:
#         return False
# ```

# * Nếu packet này đã có trong router → trả về `False`.

# ```python
#     if len(self.deque) == self.memoryLimit:
#         oldest = self.deque.popleft()
#         self.packet_set.remove(oldest)
#         s_old, d_old, t_old = oldest
#         arr_old = self.dest_packets[d_old]
#         idx_old = bisect.bisect_left(arr_old, t_old)
#         del arr_old[idx_old]
# ```

# * Nếu bộ nhớ đầy → lấy gói tin cũ nhất (`popleft` từ deque).
# * Xoá gói đó khỏi `packet_set`.
# * Đồng thời xoá timestamp của nó khỏi `dest_packets[d_old]`.

#   * Dùng `bisect_left` để tìm vị trí timestamp và `del` để xoá.

# ```python
#     self.deque.append(packet)
#     self.packet_set.add(packet)
#     arr_new = self.dest_packets[destination]
#     bisect.insort(arr_new, timestamp)
#     return True
# ```

# * Thêm packet mới vào `deque` và `packet_set`.
# * Với `destination`, chèn timestamp mới vào danh sách đã sắp xếp bằng `bisect.insort` (giữ thứ tự).
# * Trả về `True` (thêm thành công).

# ---

# ### (b) `forwardPacket`

# ```python
# def forwardPacket(self) -> List[int]:
#     if not self.deque:
#         return []
#     packet = self.deque.popleft()
#     self.packet_set.remove(packet)
#     s, d, t = packet
#     arr = self.dest_packets[d]
#     idx = bisect.bisect_left(arr, t)
#     del arr[idx]
#     return [s, d, t]
# ```

# * Nếu router rỗng → trả về `[]`.
# * Ngược lại: lấy gói cũ nhất trong `deque`, xoá khỏi `packet_set`.
# * Tìm vị trí timestamp trong danh sách `dest_packets[d]` và xoá đi.
# * Trả về `[source, destination, timestamp]`.

# ---

# ### (c) `getCount`

# ```python
# def getCount(self, destination: int, startTime: int, endTime: int) -> int:
#     if destination not in self.dest_packets:
#         return 0
#     arr = self.dest_packets[destination]
#     left_index = bisect.bisect_left(arr, startTime)
#     right_index = bisect.bisect_right(arr, endTime)
#     return right_index - left_index
# ```

# * Lấy danh sách timestamp của `destination`.
# * Dùng **binary search** để tìm vị trí đầu tiên ≥ `startTime` (`left_index`) và vị trí đầu tiên > `endTime` (`right_index`).
# * Số phần tử trong khoảng `[startTime, endTime]` = `right_index - left_index`.
# * Đây là kỹ thuật **range counting trên mảng đã sắp xếp**.

# ---

# ## 4. Độ phức tạp

# * `addPacket`:

#   * O(log n) để chèn/xoá timestamp bằng `bisect`.
# * `forwardPacket`:

#   * O(log n) để xoá timestamp.
# * `getCount`:

#   * O(log n) cho hai lần binary search.
# * Nhờ `bisect`, tất cả đều khá nhanh.

# ---

# 👉 Thuật toán của bạn đã **đúng ý tưởng** và chạy ổn.
# Điểm cần lưu ý: việc xoá trong list (`del arr[idx]`) có độ phức tạp O(n), nhưng vì memoryLimit không quá lớn (giới hạn trong đề), cách này vẫn chấp nhận được.

# ---

# Bạn có muốn mình viết thử một **ví dụ chạy tay** với input cụ thể (addPacket, forwardPacket, getCount) để thấy rõ mấy thao tác `bisect` này hoạt động thế nào không?

# ---

# ## 1) Yêu cầu (tóm tắt)

# Thiết kế một lớp `Router` quản lý các *packet* (gói dữ liệu). Mỗi packet có 3 thuộc tính: `source`, `destination`, `timestamp`.
# Phải hỗ trợ các thao tác:

# * `Router(int memoryLimit)`
#   Khởi tạo router với **giới hạn bộ nhớ** `memoryLimit` — tức tối đa có thể chứa `memoryLimit` packet cùng lúc. Nếu thêm packet mới vượt giới hạn thì phải **loại bỏ packet cũ nhất** (FIFO) để nhường chỗ.

# * `bool addPacket(int source, int destination, int timestamp)`
#   Thêm 1 packet. Nếu packet *trùng lặp* (tồn tại packet có cùng `source`, `destination`, `timestamp`) → không thêm và trả về `false`. Nếu thêm thành công → trả `true`. Nếu bộ nhớ đã đầy thì trước khi thêm phải remove packet cũ nhất. (Lưu ý: các cuộc gọi `addPacket` có `timestamp` theo thứ tự không giảm — non-decreasing). ([WalkCCC][1])

# * `List<Integer> forwardPacket()`  (hoặc tương đương `int[]`)
#   Lấy và **loại bỏ** packet tiếp theo theo thứ tự FIFO (packet vào trước được forward trước). Trả về `[source, destination, timestamp]` cho packet đó. Nếu không còn packet thì trả mảng rỗng. ([WalkCCC][1])

# * `int getCount(int destination, int startTime, int endTime)`
#   Trả về **số packet đã được thêm vào router (vẫn tồn tại trong bộ nhớ)** có `destination` bằng giá trị cho trước và có `timestamp` nằm trong khoảng `[startTime, endTime]` (khoảng bao gồm cả `startTime` và `endTime`). (Yêu cầu là trả nhanh cho nhiều truy vấn). ([Tech Road][2])

# ---

# ## 2) Những điểm cần lưu ý (edge / behavior)

# * Duplicate = cùng `source, destination, timestamp`. Phải phát hiện nhanh để trả `false`. ([WalkCCC][1])
# * Khi bộ nhớ đầy, kiểu eviction là **xóa packet cũ nhất** (không theo destination). Thao tác này có thể xảy ra tự động trong `addPacket` (trước khi push packet mới) hoặc khi gọi `forwardPacket`. ([WalkCCC][1])
# * Timestamps của `addPacket` được gọi theo thứ tự không giảm (non-decreasing) — giúp ta append timestamps cho mỗi destination theo thứ tự tăng, thuận tiện cho binary search khi đếm. ([Tech Road][2])

# ---

# ## 3) Ý tưởng cài đặt (high-level)

# Để mỗi thao tác chạy nhanh ta dùng các cấu trúc sau:

# 1. **Queue / Deque** `packetQueue` để lưu các packet theo thứ tự đến (FIFO). Dùng `deque`/`LinkedList`/`Queue` để pop front O(1) và push back O(1).

# 2. **Hash set** `uniquePackets` để kiểm tra trùng lặp nhanh (key = tuple `(source,destination,timestamp)` hoặc string `"s_d_t"`). `addPacket` kiểm tra set trước khi thêm.

# 3. **Map từ destination -> list/deque timestamps** (`Map<int, List<int>> destToTimestamps`) để hỗ trợ `getCount(destination, start, end)`.

#    * Vì `addPacket` được gọi theo timestamp không giảm, khi thêm timestamp vào `destToTimestamps[destination]` ta luôn *append* ở cuối — danh sách cho mỗi destination được giữ **sắp tăng dần**.
#    * Khi cần `getCount`, ta dùng binary search (`lower_bound`/`upper_bound`) trên mảng timestamps để đếm số phần tử trong khoảng `[start,end]` — chạy O(log m) với m = số packet cho destination đó.

# 4. Khi xóa 1 packet (do `forwardPacket()` hoặc do eviction trước khi `addPacket` nếu đầy):

#    * Pop packet từ `packetQueue`.
#    * Xóa từ `uniquePackets`.
#    * Cần **loại timestamp tương ứng khỏi `destToTimestamps[destination]`**. Vì ta chỉ xóa những packet cũ nhất (theo thứ tự global FIFO), timestamp để xóa sẽ nằm ở **đầu** danh sách timestamps của destination (nếu ta lưu timestamps dạng deque). Do đó, ta có thể `pop_front` từ deque của destination O(1). Một cách khác là dùng mảng + một con trỏ đếm đã processed (processedIndex) cho từng destination để tránh xóa giữa mảng. ([WalkCCC][1])

# ---

# ## 4) Phức tạp thuật toán (kỳ vọng)

# * `addPacket`: amortized O(1) (kiểm tra set O(1), nếu đầy gọi `forwardPacket()` O(1), append queue & append timestamp O(1)).
# * `forwardPacket`: O(1) (pop queue, xóa set, cập nhật deque/destination counter O(1)).
# * `getCount(destination, start, end)`: O(log m) với m = số packet hiện có cho destination (binary search trên danh sách timestamp).
# * Space: O(M) với M = số packet hiện lưu (≤ memoryLimit). ([Tech Road][2])

# ---

# ## 5) Lưu ý khi triển khai

# * Dùng kiểu key trong `uniquePackets` là tuple hoặc chuỗi ghép tránh collision.
# * Khi dùng `ArrayList` cho `destToTimestamps[d]`, vì ta luôn append và cũng luôn xóa ở đầu theo FIFO, xóa đầu `ArrayList` là O(n) — **không tốt**. Thay vì ấy:

#   * Dùng `Deque` (pop\_front O(1)), hoặc
#   * Dùng `List` + một con trỏ `processedIndex` (số đã bị xóa ở đầu) để không thực sự remove phần tử, chỉ tăng con trỏ — phù hợp nếu bạn vẫn cần binary search (nhưng binary search phải tính offset).
# * Chú ý các test case: có issue trên LeetCode về “increasing vs non-decreasing” timestamp (một số test dùng non-decreasing), nên thiết kế theo non-decreasing để an toàn. ([Thư Viện Trực Tuyến Wiley][3])

# ---

# ## 6) Muốn mình viết code mẫu không?

# Mình có thể gửi **mã mẫu** (Python / Java / C++) theo kiến trúc trên — kèm giải thích từng đoạn. Bạn muốn ngôn ngữ nào? (Python/Java/C++)

# [1]: https://walkccc.me/LeetCode/problems/3508/?utm_source=chatgpt.com "3508. Implement Router - LeetCode Solutions"
# [2]: https://zxi.mytechroad.com/blog/uncategorized/leetcode-3508-implement-router/?utm_source=chatgpt.com "花花酱LeetCode 3508. Implement Router - Huahua's Tech Road"
# [3]: https://onlinelibrary.wiley.com/doi/10.1155/2022/1401683?utm_source=chatgpt.com "[Retracted] Detection of DDoS Attack within Industrial IoT ..."
