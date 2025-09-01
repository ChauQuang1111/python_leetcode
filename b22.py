# 1792. Maximum Average Pass Ratio(01/09/2025)

from typing import List
from heapq import *

class Solution:
    def maxAverageRatio(self, cls: List[List[int]], extra: int) -> float:
        cls = [(p/t - (p+1)/(t+1), p, t) for p, t in cls]
        heapify(cls)

        if cls[0][0] == 0:
            return 1

        for _ in range(extra):
            _, p, t = heappop(cls)
            heappush(cls, ((p+1)/(t+1) - (p+2)/(t+2), p+1, t+1))

        return sum(p/t for _, p, t in cls) / len(cls)









# Đoạn mã Python bạn cung cấp là một giải pháp rất ngắn gọn và thông minh cho bài toán "Maximum Average Pass Ratio". Về mặt thuật toán, nó sử dụng cách tiếp cận tham lam (greedy) kết hợp với cấu trúc dữ liệu heap (hàng đợi ưu tiên).

# ### Giải thích thuật toán

# Ý tưởng cốt lõi của thuật toán này là **tối đa hóa tổng của các tỷ lệ đỗ** bằng cách phân bổ mỗi học sinh phụ vào lớp học mang lại **sự gia tăng tỷ lệ lớn nhất** tại mỗi bước.

# Để thực hiện chiến lược này, thuật toán của bạn thực hiện ba bước chính:

# 1.  **Tính toán và khởi tạo lợi ích**:
#     * Bạn tạo một danh sách các tuple, mỗi tuple đại diện cho một lớp học. Mỗi tuple chứa ba giá trị: `(lợi ích, passes, total)`.
#     * **Lưu ý quan trọng**: Lợi ích được tính là `(p/t - (p+1)/(t+1))`. Đây là một cách tính lợi ích ngược so với thông thường (`(p+1)/(t+1) - p/t`). Bằng cách này, lợi ích lớn nhất sẽ là giá trị âm nhỏ nhất. Điều này cho phép bạn sử dụng một **min-heap** (mặc định của Python) để lấy ra phần tử có lợi ích cao nhất một cách hiệu quả.
#     * Sử dụng `heapify(cls)` để biến danh sách này thành một min-heap, đảm bảo rằng phần tử có lợi ích cao nhất (giá trị âm nhỏ nhất) luôn nằm ở đầu.

# 2.  **Phân bổ học sinh tham lam**:
#     * Bạn lặp lại `extra` lần, tương ứng với số học sinh phụ cần phân bổ.
#     * Trong mỗi vòng lặp, `heappop(cls)` lấy ra tuple đầu tiên từ heap. Tuple này chính là lớp học có lợi ích lớn nhất (vì giá trị lợi ích của nó là số âm nhỏ nhất).
#     * Bạn tăng `passes` và `total` của lớp đó lên 1.
#     * Bạn tính toán lợi ích mới cho lớp đã cập nhật và đẩy nó trở lại heap bằng `heappush`.

# 3.  **Tính toán kết quả cuối cùng**:
#     * Sau khi phân bổ hết học sinh, bạn duyệt qua tất cả các lớp còn lại trong heap (đã được cập nhật).
#     * Bạn tính tổng tỷ lệ đỗ của tất cả các lớp và chia cho tổng số lớp ban đầu để có được tỷ lệ đỗ trung bình tối đa.

# ---

# ### Phân tích chi tiết từng dòng mã

# * `cls = [(p/t - (p+1)/(t+1), p, t) for p, t in cls]`: Dòng này sử dụng list comprehension để tạo một danh sách mới. Mỗi phần tử trong danh sách là một tuple, chứa lợi ích âm, số học sinh đỗ, và tổng số học sinh ban đầu.
# * `heapify(cls)`: Biến danh sách `cls` thành một min-heap. Thao tác này có độ phức tạp là $O(N)$, với $N$ là số lượng lớp học.
# * `if cls[0][0] == 0: return 1`: Đây là một trường hợp đặc biệt. Nếu lợi ích của lớp tốt nhất bằng 0 (chỉ xảy ra khi `passes` và `total` ban đầu bằng nhau, ví dụ `[1, 1]` hoặc `[2, 2]`), tỷ lệ đỗ đã là 100%. Thêm học sinh sẽ không làm tăng tỷ lệ, nên bạn có thể trả về 1 ngay.
# * `for _ in range(extra)`: Vòng lặp này chạy `extra` lần, mỗi lần phân bổ một học sinh.
# * `_, p, t = heappop(cls)`: Lấy ra phần tử đầu tiên của heap (lợi ích cao nhất) và gán các giá trị `passes` và `total` cho biến. Dấu gạch dưới `_` được sử dụng cho biến lợi ích vì chúng ta không cần dùng nó nữa.
# * `heappush(cls, ((p+1)/(t+1) - (p+2)/(t+2), p+1, t+1))`: Đẩy lớp đã cập nhật trở lại heap với lợi ích mới. Lợi ích mới này được tính cho lớp `[p+1, t+1]` và sẽ xác định vị trí mới của nó trong heap.
# * `return sum(p/t for _, p, t in cls) / len(cls)`: Sau khi vòng lặp kết thúc, bạn tính tổng tỷ lệ đỗ của tất cả các lớp còn lại trong heap và chia cho tổng số lớp ban đầu.

# Thuật toán của bạn rất hiệu quả, với độ phức tạp thời gian là $O(N + extra \cdot \log N)$, trong đó $N$ là số lớp. Đây là cách giải quyết tối ưu cho bài toán này.

# Chào bạn,

# Dưới đây là giải thích chi tiết về đề bài "1792. Maximum Average Pass Ratio" trên LeetCode.

### Giải thích đề bài

# **1. Yêu cầu chính:**

# Bạn được cho một danh sách các lớp học, mỗi lớp được biểu diễn bằng một cặp số: `[passes_i, total_i]`.
# * `passes_i`: Số học sinh đỗ trong lớp đó.
# * `total_i`: Tổng số học sinh trong lớp đó.

# Tỷ lệ đỗ của một lớp là `passes_i / total_i`.

# Bạn được cấp thêm `extraStudents` (số học sinh dư). Bạn có thể phân bổ những học sinh này vào bất kỳ lớp học nào. Khi một học sinh được phân bổ vào một lớp, cả số học sinh đỗ (`passes`) và tổng số học sinh (`total`) của lớp đó đều tăng lên 1.

# Mục tiêu của bạn là phân bổ tất cả `extraStudents` sao cho **tỷ lệ đỗ trung bình** của tất cả các lớp là **lớn nhất có thể**. Cuối cùng, bạn cần trả về giá trị tỷ lệ đỗ trung bình này.

# **2. Khái niệm "Tỷ lệ đỗ trung bình":**

# Đây là trung bình cộng của tỷ lệ đỗ của tất cả các lớp.
# Công thức: `(tỷ lệ đỗ lớp 1 + tỷ lệ đỗ lớp 2 + ... + tỷ lệ đỗ lớp n) / n`
# Trong đó `n` là tổng số lớp học.

# **3. Phân tích bài toán:**

# Bài toán này không yêu cầu bạn tìm ra cách phân bổ cụ thể, mà chỉ yêu cầu tìm **giá trị trung bình lớn nhất** có thể đạt được.

# Để tối đa hóa tổng của các tỷ lệ đỗ, bạn cần phân bổ mỗi học sinh thêm vào lớp học mà việc đó mang lại **lợi ích lớn nhất**.

# # * **Lợi ích:** Lợi ích của việc thêm một học sinh vào một lớp `[p, t]` là sự gia tăng của tỷ lệ đỗ.
#     * Tỷ lệ đỗ ban đầu: `p / t`
#     * Tỷ lệ đỗ sau khi thêm 1 học sinh: `(p + 1) / (t + 1)`
#     * Lợi ích: `(p + 1) / (t + 1) - p / t`

# * **Chiến lược tham lam (Greedy Strategy):**
#     * Mỗi lần bạn có một học sinh thêm, bạn cần tìm lớp học nào mà việc thêm học sinh đó vào sẽ mang lại lợi ích lớn nhất (tức là tăng tỷ lệ đỗ nhiều nhất).
#     * Bạn sẽ lặp lại quá trình này `extraStudents` lần, mỗi lần phân bổ một học sinh vào lớp có lợi ích cao nhất tại thời điểm đó.

# **4. Dữ liệu đầu vào và đầu ra:**

# * **Input:**
#     * `classes`: Một mảng/danh sách các mảng con, mỗi mảng con là `[passes_i, total_i]`.
#     * `extraStudents`: Một số nguyên, số học sinh có thể phân bổ.
# * **Output:**
#     * Một số thực, là tỷ lệ đỗ trung bình lớn nhất có thể.

# ### Ví dụ minh họa

# Giả sử bạn có `classes = [[1,2], [3,5]]` và `extraStudents = 1`.

# * **Lớp 1:** `[1,2]`, tỷ lệ đỗ: `1/2 = 0.5`
# * **Lớp 2:** `[3,5]`, tỷ lệ đỗ: `3/5 = 0.6`

# Bây giờ bạn có 1 học sinh thêm, bạn nên cho vào lớp nào để có lợi nhất?
# * **Thêm vào Lớp 1:** Tỷ lệ mới là `(1+1)/(2+1) = 2/3 ≈ 0.667`. Lợi ích: `0.667 - 0.5 = 0.167`.
# * **Thêm vào Lớp 2:** Tỷ lệ mới là `(3+1)/(5+1) = 4/6 ≈ 0.667`. Lợi ích: `0.667 - 0.6 = 0.067`.

# Lợi ích của việc thêm vào Lớp 1 lớn hơn. Do đó, bạn nên phân bổ học sinh vào Lớp 1.

# * Tỷ lệ đỗ mới của Lớp 1: `0.667`
# * Tỷ lệ đỗ của Lớp 2: `0.6`
# * Tỷ lệ đỗ trung bình: `(0.667 + 0.6) / 2 = 0.6335`.

# Để giải quyết bài toán này một cách hiệu quả, bạn có thể sử dụng một cấu trúc dữ liệu ưu tiên (priority queue) để luôn tìm được lớp có lợi ích cao nhất một cách nhanh chóng.