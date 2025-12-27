# # Meeting Rooms III(27/12/2025)
# Rất tốt 👍
# Đây là **lời giải chuẩn contest** cho **Meeting Rooms III (LeetCode 2402)**.
# Mình sẽ làm 2 việc:

# 1️⃣ **Giải thích thuật toán (ý tưởng + tư duy greedy)**
# 2️⃣ **Viết lại code của bạn với chú thích chi tiết từng phần**

# ---

# # 1️⃣ Giải thích thuật toán (theo tư duy thi đấu)

# ## Bài toán yêu cầu gì?

# * Có `n` phòng họp (`0 → n-1`)
# * Mỗi meeting có `[start, end]`
# * Quy tắc:

#   * Nếu có phòng trống → chọn **phòng index nhỏ nhất**
#   * Nếu không có phòng trống → **chờ phòng kết thúc sớm nhất**
#   * Meeting bị dời nhưng **giữ nguyên thời lượng**
# * Cuối cùng → trả về phòng được dùng nhiều nhất

# ---

# ## Insight quan trọng

# Ta cần **luôn biết**:

# * Phòng nào **đang trống** (lấy index nhỏ nhất)
# * Phòng nào **kết thúc sớm nhất**

# 👉 Không thể dùng mảng hay vòng lặp thường
# 👉 **BẮT BUỘC dùng Priority Queue (heap)**

# ---

# ## 2 Heap cần thiết

# ### 🔹 `avail` – phòng trống

# * Min-heap theo **room index**
# * Luôn lấy phòng nhỏ nhất

# ### 🔹 `busy` – phòng đang bận

# * Min-heap theo **(endTime, room)**
# * Lấy phòng kết thúc sớm nhất

# ---

# ## Chiến lược Greedy

# Duyệt từng meeting theo **start time tăng dần**:

# ### Bước 1: Trả phòng đã xong

# ```text
# Nếu busyRoom.endTime <= start
# → phòng đó rảnh → đưa về avail
# ```

# ---

# ### Bước 2: Gán phòng

# * Nếu `avail` không rỗng:

#   * Dùng phòng nhỏ nhất
# * Nếu `avail` rỗng:

#   * Chờ phòng kết thúc sớm nhất
#   * Dời meeting sang thời điểm đó

# ---

# ### Bước 3: Cập nhật

# * Đẩy phòng vào `busy`
# * Tăng số lần dùng phòng

# ---

# # 2️⃣ Code có chú thích chi tiết

# ```python
from typing import List
from heapq import heappush, heappop, heapify

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        # Sắp xếp meetings theo thời gian bắt đầu
        meetings.sort(key=lambda x: x[0])

        # used[i]: số lần phòng i được sử dụng
        used = [0] * n

        # avail: min-heap lưu các phòng đang trống (theo index nhỏ nhất)
        avail = list(range(n))
        heapify(avail)

        # busy: min-heap lưu các phòng đang bận
        # mỗi phần tử là (endTime, room)
        busy = []
        heapify(busy)

        # Duyệt từng meeting
        for start, end in meetings:

            # Trả lại các phòng đã họp xong trước hoặc đúng start
            while busy and busy[0][0] <= start:
                _, room = heappop(busy)
                heappush(avail, room)

            # Nếu còn phòng trống
            if avail:
                room = heappop(avail)
                heappush(busy, (end, room))
                used[room] += 1

            # Nếu không còn phòng trống → phải chờ
            else:
                dur = end - start                # thời lượng meeting
                endTime, room = heappop(busy)    # phòng kết thúc sớm nhất
                heappush(busy, (endTime + dur, room))
                used[room] += 1

        # Tìm phòng được dùng nhiều nhất
        maxRoom = 0
        maxCount = 0
        for i in range(n):
            if used[i] > maxCount:
                maxCount = used[i]
                maxRoom = i

        # Trả về phòng được dùng nhiều nhất
        return maxRoom
# ```

# ---

# # 3️⃣ Ví dụ minh hoạ ngắn

# ```
# n = 2
# meetings = [[0,10],[1,5],[2,7],[3,4]]
# ```

# | Meeting | Hành động  |
# | ------- | ---------- |
# | [0,10]  | room 0     |
# | [1,5]   | room 1     |
# | [2,7]   | chờ room 1 |
# | [3,4]   | chờ room 0 |

# → room 0 dùng nhiều nhất → trả về `0`

# ---

# # 4️⃣ Độ phức tạp

# * Sort meetings: `O(m log m)`
# * Heap operations: `O(m log n)`
# * Tổng: **O(m log n)**
# * Bộ nhớ: **O(n)**

# ---

# # 5️⃣ Ghi nhớ khi đi thi 🧠

# > “Interval + phòng + sớm nhất / nhỏ nhất
# > → **2 priority queue**”

# ---

# Nếu bạn muốn:

# * Mình **giải thích từng dòng trong vòng while**
# * Viết **Java version**
# * So sánh với **Meeting Rooms I / II**
# * Vẽ **timeline mô phỏng**

# 👉 cứ nói, mình huấn luyện tiếp 💪

# OK 👍
# Mình sẽ **giải thích bài “Meeting Rooms III” (LeetCode 2402)** theo đúng phong cách **huấn luyện viên lập trình thi đấu**:
# 👉 hiểu bài → mô hình hoá → cấu trúc dữ liệu → thuật toán chuẩn contest.

# ---

# ## 1️⃣ Tóm tắt đề bài

# Bạn có:

# * `n` phòng họp, đánh số `0 → n-1`
# * `meetings[i] = [start, end]`

# Quy tắc:

# 1. Nếu có **phòng trống tại thời điểm start**
#    → dùng phòng có **chỉ số nhỏ nhất**
# 2. Nếu **không có phòng trống**
#    → **chờ phòng kết thúc sớm nhất**, và **dời meeting** sang thời điểm đó
#    (giữ nguyên thời lượng)
# 3. Mỗi meeting được gán đúng **1 phòng**
# 4. Đếm số lần mỗi phòng được dùng

# 🎯 **Trả về phòng được dùng nhiều nhất**
# (Nếu hoà → lấy phòng có index nhỏ hơn)

# ---

# ## 2️⃣ Insight quan trọng (thi đấu)

# 👉 Ta cần **mô phỏng theo thời gian**, và luôn phải biết:

# * Phòng nào **đang trống**
# * Phòng nào **sẽ rảnh sớm nhất**

# ➡️ **Bài toán priority queue (heap)**

# ---

# ## 3️⃣ Hai heap bắt buộc phải có

# ### 🔹 Heap 1: phòng trống

# ```text
# availableRooms (min-heap)
# ```

# * Lưu **chỉ số phòng**
# * Luôn lấy phòng nhỏ nhất

# ---

# ### 🔹 Heap 2: phòng đang bận

# ```text
# busyRooms (min-heap)
# ```

# * Lưu `(endTime, roomIndex)`
# * So sánh theo:

#   1. `endTime` nhỏ nhất
#   2. nếu bằng → `roomIndex` nhỏ hơn

# ---

# ## 4️⃣ Chiến lược thuật toán

# ### Bước 1: Sort meetings

# ```text
# Sort theo start tăng dần
# ```

# ---

# ### Bước 2: Khởi tạo

# * Tất cả phòng `0 → n-1` vào `availableRooms`
# * Mảng `count[n] = 0`

# ---

# ### Bước 3: Duyệt từng meeting

# Giả sử meeting `[start, end]`, duration = `end - start`

# #### 🔹 Trả phòng đã xong

# ```text
# Trong khi busyRooms.peek().endTime <= start:
#     trả phòng đó về availableRooms
# ```

# ---

# #### 🔹 Nếu có phòng trống

# ```text
# room = availableRooms.pop()
# endTime = end
# ```

# ---

# #### 🔹 Nếu KHÔNG có phòng trống

# ```text
# (room, freeTime) = busyRooms.pop()
# endTime = freeTime + duration
# ```

# ---

# #### 🔹 Cập nhật

# ```text
# count[room]++
# push (endTime, room) vào busyRooms
# ```

# ---

# ## 5️⃣ Vì sao greedy này đúng?

# * Meeting **không được bỏ**
# * Nếu có phòng trống → dùng ngay phòng nhỏ nhất
# * Nếu không → chờ phòng xong sớm nhất để **giảm delay tổng thể**

# 👉 Đây là **mô phỏng đúng đề**, không có trick ẩn

# ---

# ## 6️⃣ Ví dụ ngắn

# ```
# n = 2
# meetings = [[0,10],[1,5],[2,7],[3,4]]
# ```

# * meeting[0]: room 0
# * meeting[1]: room 1
# * meeting[2]: room 1 (dời)
# * meeting[3]: room 0 (dời)

# 👉 room 0 dùng nhiều nhất → trả về 0

# ---

# ## 7️⃣ Code mẫu (Python – chuẩn thi đấu)

# ```python
# import heapq

# class Solution:
#     def mostBooked(self, n: int, meetings):
#         meetings.sort()

#         available = list(range(n))          # phòng trống
#         heapq.heapify(available)

#         busy = []  # (endTime, room)
#         count = [0] * n

#         for start, end in meetings:
#             duration = end - start

#             # trả phòng đã xong
#             while busy and busy[0][0] <= start:
#                 _, room = heapq.heappop(busy)
#                 heapq.heappush(available, room)

#             if available:
#                 room = heapq.heappop(available)
#                 finish = end
#             else:
#                 finish, room = heapq.heappop(busy)
#                 finish += duration

#             count[room] += 1
#             heapq.heappush(busy, (finish, room))

#         return count.index(max(count))
# ```

# ---

# ## 8️⃣ Độ phức tạp

# * Sort meetings: `O(m log m)`
# * Mỗi meeting push/pop heap: `O(log n)`

# 👉 Tổng: **O(m log n)**
# 👉 Bộ nhớ: **O(n)**

# ---

# ## 9️⃣ Dấu hiệu nhận dạng bài này trong contest

# Nếu bạn thấy:

# * meeting / task / interval
# * phòng / server / máy
# * dùng “sớm nhất” / “nhỏ nhất”

# 👉 **Priority Queue 2 heap**

# ---

# Nếu bạn muốn:

# * Giải thích **từng dòng code**
# * Viết **Java version**
# * So sánh với **Meeting Rooms I / II**
# * Vẽ **timeline mô phỏng**

# 👉 cứ nói, mình huấn luyện tiếp 💪
