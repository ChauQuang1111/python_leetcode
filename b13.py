# 3197. Find the Minimum Area to Cover All Ones II(23/08/2025)
from typing import List
from math import inf

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        # Trả về min giữa 2 hướng: nguyên bản và xoay 90 độ
        return min(self.f(grid), self.f(rotate(grid)))

    def f(self, a: List[List[int]]) -> int:
        m, n = len(a), len(a[0])
        
        # Lưu cột trái - phải có số 1 ở mỗi hàng
        lr = []
        for i in range(m):
            l, r = -1, 0
            for j in range(n):
                if a[i][j] > 0:
                    if l < 0:
                        l = j
                    r = j
            lr.append((l, r))

        # ---------------------------
        # Hàm phụ: tính diện tích hình chữ nhật nhỏ nhất
        # chứa tất cả số 1 trong vùng (0,0) → (i,j)
        # ---------------------------
        def minimumArea(a: List[List[int]]) -> List[List[int]]:
            m, n = len(a), len(a[0])
            f = [[0] * (n + 1) for _ in range(m + 1)]
            border = [(-1, 0, 0)] * n  # lưu [hàng_đầu, cột_trái, cột_phải]
            for i, row in enumerate(a):
                left, right = -1, 0
                for j, x in enumerate(row):
                    if x:
                        if left < 0:
                            left = j
                        right = j
                    pre_top, pre_left, pre_right = border[j]
                    if left < 0:  
                        # Hàng này chưa có 1 → copy kết quả từ hàng trên
                        f[i + 1][j + 1] = f[i][j + 1]
                    elif pre_top < 0:  
                        # Hàng này có 1, phía trên toàn 0
                        f[i + 1][j + 1] = right - left + 1
                        border[j] = (i, left, right)
                    else:  
                        # Hàng này có 1, trên cũng có 1
                        l = min(pre_left, left)
                        r = max(pre_right, right)
                        f[i + 1][j + 1] = (r - l + 1) * (i - pre_top + 1)
                        border[j] = (pre_top, l, r)
            return f

        # Tính 4 hướng diện tích nhỏ nhất (lt, lb, rb, rt)
        lt = minimumArea(a)                           # trên trái
        a = rotate(a)
        lb = rotate(rotate(rotate(minimumArea(a))))   # dưới trái
        a = rotate(a)
        rb = rotate(rotate(minimumArea(a)))           # dưới phải
        a = rotate(a)
        rt = rotate(minimumArea(a))                   # trên phải

        ans = inf

        # -------------------------------
        # 1) Trường hợp chia thành 3 khối ngang (trên – giữa – dưới)
        # -------------------------------
        if m >= 3:
            for i in range(1, m):
                left, right, top, bottom = n, 0, m, 0
                for j in range(i + 1, m):
                    l, r = lr[j - 1]
                    if l >= 0:
                        left = min(left, l)
                        right = max(right, r)
                        top = min(top, j - 1)
                        bottom = j - 1
                    # Diện tích = khối trên + khối giữa + khối dưới
                    ans = min(ans, lt[i][n] + (right - left + 1) * (bottom - top + 1) + lb[j][n])

        # -------------------------------
        # 2) Trường hợp chia theo hình chữ L
        # -------------------------------
        if m >= 2 and n >= 2:
            for i in range(1, m):
                for j in range(1, n):
                    # chữ L kiểu trên – giữa – dưới
                    ans = min(ans, lt[i][n] + lb[i][j] + rb[i][j])
                    # chữ L kiểu trên trái – trên phải – dưới
                    ans = min(ans, lt[i][j] + rt[i][j] + lb[i][n])

        return ans


# Hàm xoay ma trận 90°
def rotate(a: List[List[int]]) -> List[List[int]]:
    # zip(*reversed(a)) = xoay 90 độ theo chiều kim đồng hồ
    return list(zip(*reversed(a)))







# Bạn có một ma trận nhị phân `grid` (gồm **0** và **1**).
# Bạn cần **chọn tối đa 3 hình chữ nhật** sao cho:

# * Mỗi hình chữ nhật bao phủ các ô liên tiếp nhau.
# * Tất cả các ô chứa **1** trong `grid` đều được bao phủ bởi ít nhất một hình chữ nhật.
# * Tổng diện tích của các hình chữ nhật là **nhỏ nhất**.

# 👉 Kết quả cần trả về chính là diện tích tối thiểu đó.

# ---

# ### 📌 2. Ý tưởng chính

# Nếu chỉ có **1 hình chữ nhật**, thì ta chỉ cần:

# * Tìm **hàng nhỏ nhất (minRow), hàng lớn nhất (maxRow)** có chứa `1`.
# * Tìm **cột nhỏ nhất (minCol), cột lớn nhất (maxCol)** có chứa `1`.
# * Diện tích = `(maxRow - minRow + 1) * (maxCol - minCol + 1)`.

# ⚡ Nhưng vì ta được phép dùng **tối đa 3 hình chữ nhật**, nên bài toán phức tạp hơn:

# * Có thể tách `grid` theo **hàng** hoặc **cột** thành 2 hoặc 3 vùng nhỏ.
# * Với mỗi vùng, ta tính hình chữ nhật nhỏ nhất bao phủ tất cả `1` trong vùng đó.
# * Tổng diện tích = tổng diện tích của các hình chữ nhật con.

# Sau đó lấy **min** trong tất cả các cách chia.

# ---

# ### 📌 3. Cách chia hình chữ nhật

# Có 2 kiểu chia:

# 1. **Theo hàng (horizontal cut)**
#    Ví dụ: chia ma trận thành 2 hoặc 3 phần theo chiều ngang.
#    Mỗi phần → tính diện tích chữ nhật bao phủ các `1` trong phần đó.

# 2. **Theo cột (vertical cut)**
#    Tương tự, chia theo chiều dọc thành 2 hoặc 3 phần.

# 👉 Với mỗi cách chia, ta tính tổng diện tích rồi chọn nhỏ nhất.

# ---

# ### 📌 4. Ví dụ minh họa

# #### Ví dụ 1:

# ```
# grid = [[1,0,1],
#         [1,1,1]]
# ```

# * Nếu chỉ dùng 1 hình chữ nhật:
#   Bao phủ từ `(0,0)` đến `(1,2)` → diện tích = `2 * 3 = 6`.

# * Nhưng ta có thể chia thành 2 phần **theo cột**:

#   * Cột trái: bao phủ `[[1],[1]]` → diện tích = `2 * 1 = 2`.
#   * Cột phải: bao phủ `[[1],[1]]` → diện tích = `2 * 1 = 2`.
#   * Giữa (cột 1): bao phủ `[[0],[1]]` → diện tích = `2 * 1 = 2`.

#   Nhưng nếu nhóm lại thông minh hơn:

#   * Lấy **cột trái (0..1)**: bao phủ từ `(0,0)` → `(1,1)` → diện tích = `2 * 2 = 4`.
#   * Lấy **cột phải (2..2)**: bao phủ từ `(0,2)` → `(1,2)` → diện tích = `2 * 1 = 2`.

#   Tổng = `4 + 1 = 5` ✅ (đáp án đúng).

# ---

# ### 📌 5. Kết luận về thuật toán

# * Thuật toán sẽ:

#   1. Thử tất cả cách chia theo hàng.
#   2. Thử tất cả cách chia theo cột.
#   3. Với mỗi vùng chia, tính hình chữ nhật nhỏ nhất bao phủ `1`.
#   4. Lấy kết quả nhỏ nhất.


# Dưới đây là giải thích chi tiết về thuật toán trong đoạn mã Python bạn đã cung cấp.

# ### Phân tích tổng quan

# Thuật toán này giải quyết bài toán "Tìm diện tích nhỏ nhất để bao phủ tất cả các số 1 bằng hai hình chữ nhật" bằng cách sử dụng **quy hoạch động (Dynamic Programming)** và kỹ thuật **xoay ma trận**.

# Ý tưởng chính là:

# 1.  **Chia bài toán lớn thành các bài toán con:** Thay vì tìm hai hình chữ nhật bao phủ tất cả các số 1 một cách trực tiếp, thuật toán tìm cách chia ma trận thành hai hoặc ba phần bằng các đường cắt ngang hoặc dọc.
# 2.  **Sử dụng quy hoạch động để tính diện tích tiền tố:** Xây dựng các ma trận con để lưu trữ diện tích bao phủ tối thiểu từ một góc của ma trận đến một điểm bất kỳ.
# 3.  **Xoay ma trận:** Bằng cách xoay ma trận 90 độ, ta có thể tái sử dụng hàm quy hoạch động để tính diện tích từ các góc khác (trên-phải, dưới-trái, dưới-phải) mà không cần viết thêm hàm mới.
# 4.  **Kết hợp các diện tích:** Cuối cùng, kết hợp các diện tích đã tính toán để tìm ra tổng diện tích nhỏ nhất cho các trường hợp chia ma trận thành 2 hoặc 3 phần.

### Giải thích chi tiết các hàm


### `minimumSum(self, grid: List[List[int]]) -> int`

# Đây là hàm chính của chương trình.

#   * `return min(self.f(grid), self.f(rotate(grid)))`:
#       * Hàm này gọi `f(grid)` để tính toán các trường hợp chia ngang và dọc trên ma trận ban đầu.
#       * Sau đó, nó gọi `f(rotate(grid))` để xử lý các trường hợp tương tự nhưng trên ma trận đã xoay 90 độ.
#       * Việc xoay ma trận cho phép bao phủ các trường hợp mà hai hình chữ nhật được tạo thành bởi các đường cắt chéo, vì một đường cắt chéo trên ma trận gốc sẽ trở thành một đường cắt ngang hoặc dọc trên ma trận đã xoay.



### `f(self, a: List[List[int]]) -> int`

# Hàm này là trung tâm của thuật toán, nơi tất cả các phép tính được thực hiện.

#   * `lr`: Mảng này lưu trữ tọa độ cột của số 1 ở **cực trái** và **cực phải** cho **mỗi hàng**.

#       * `l, r = lr[j-1]` trong vòng lặp có vẻ như là một lỗi chính tả, có thể ý đồ là `lr[j - 1]`.

#   * **Các ma trận DP:**

    #   * `lt`: `lt[i+1][j+1]` lưu trữ diện tích nhỏ nhất để bao phủ tất cả các số 1 trong vùng **trên-trái** (từ `(0,0)` đến `(i,j)`).
    #   * `lb`: Tương tự, bao phủ vùng **dưới-trái**.
    #   * `rb`: Bao phủ vùng **dưới-phải**.
    #   * `rt`: Bao phủ vùng **trên-phải**.
    #   * Các ma trận này được tạo ra bằng cách gọi hàm `minimumArea` và xoay ma trận ban đầu.

#   * **Các trường hợp chia:** Thuật toán này dựa trên một quan sát quan trọng: một cách chia 2 hình chữ nhật bất kỳ có thể được biểu diễn bằng cách chia ma trận thành 3 phần. Các trường hợp được xét là:

#       * **Chia thành 3 phần ngang (`m >= 3`)**: Một hình chữ nhật ở trên, một ở giữa, và một ở dưới.
#         ```python
#         ans = min(ans, lt[i][n] + (right - left + 1) * (bottom - top + 1) + lb[j][n])
#         ```
#           * `lt[i][n]` là diện tích bao phủ phần trên cùng.
#           * `(right - left + 1) * (bottom - top + 1)` là diện tích hình chữ nhật ở giữa (được tính từ mảng `lr`).
#           * `lb[j][n]` là diện tích bao phủ phần dưới cùng.
#       * **Chia thành 3 phần kết hợp (`m >= 2, n >= 2`)**:
#           * **Trường hợp 1**: Một hình chữ nhật ở trên, và hai hình chữ nhật ở dưới (dưới-trái và dưới-phải).
#             ```python
#             ans = min(ans, lt[i][n] + lb[i][j] + rb[i][j])
#             ```
#           * **Trường hợp 2**: Hai hình chữ nhật ở trên (trên-trái và trên-phải), và một hình chữ nhật ở dưới.
#             ```python
#             ans = min(ans, lt[i][j] + rt[i][j] + lb[i][n])
#             ```

# -----

# ### `minimumArea(a: List[List[int]]) -> List[List[int]]`

# Đây là hàm quy hoạch động chính để tính **diện tích bao phủ tiền tố**.

#   * `f[i+1][j+1]` biểu thị diện tích nhỏ nhất bao phủ tất cả các số 1 trong vùng từ `(0,0)` đến `(i,j)`.
#   * Nó duyệt qua từng ô của ma trận và cập nhật giá trị của `f`.
#   * `border`: Một mảng để lưu trữ thông tin về đường bao hiện tại (hàng trên cùng, cột trái nhất, cột phải nhất).
#       * Nếu hàng hiện tại không có số 1, diện tích vẫn bằng diện tích của hàng trên.
#       * Nếu hàng hiện tại có số 1, nhưng các hàng trên chưa có, diện tích là hình chữ nhật nhỏ nhất bao phủ các số 1 trên hàng hiện tại.
#       * Nếu cả hàng hiện tại và các hàng trên đều có số 1, diện tích mới được tính bằng cách mở rộng hình chữ nhật hiện có để bao gồm cả các số 1 trên hàng hiện tại.

# -----

# ### `rotate(a: List[List[int]]) -> List[List[int]]`

# Hàm này xoay ma trận đầu vào 90 độ theo chiều kim đồng hồ. Cụ thể, nó thực hiện các bước sau:

# 1.  `reversed(a)`: Đảo ngược thứ tự các hàng.
# 2.  `zip(...)`: Chuyển đổi hàng thành cột.
# 3.  `list(...)`: Chuyển đổi kết quả thành một danh sách (list) để tạo ma trận đã xoay.




