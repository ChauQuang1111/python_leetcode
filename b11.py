# 1504. Count Submatrices With All Ones (21/08/2025)
from typing import List
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        heights = [0] * n
        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            res += self.countRow(heights)
        
        return res
    
    def countRow(self, heights: List[int]) -> int:
        stack = []
        subs = [0] * len(heights)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                stack.pop()
                
            if stack:
                left = stack[-1]
                subs[i] = subs[left] + h * (i-left)
            else:
                subs[i] = h * (i+1)

            stack.append(i)

        return sum(subs)
    



# Tóm tắt bài toán:Mục tiêu của bài toán là đếm tổng số ma trận con (submatrices) trong một ma trận nhị phân (chỉ chứa số 0 và 1) mà tất cả các phần tử của ma trận con đó đều là số 1.

# Tuyệt vời! Bạn đã tìm thấy một giải pháp cực kỳ hiệu quả và tối ưu để giải quyết bài toán "Count Submatrices With All Ones". Thuật toán này sử dụng một kỹ thuật mạnh mẽ: **biến đổi bài toán 2D thành một loạt các bài toán 1D** và sử dụng **monotonic stack** (ngăn xếp đơn điệu) để tối ưu hóa việc tính toán.

# ### Giải thích thuật toán

# Thuật toán này chia bài toán thành hai phần chính:

# 1.  **Chuyển đổi ma trận thành các biểu đồ hình cột (histograms).**
# 2.  **Đếm các hình chữ nhật cho mỗi biểu đồ hình cột một cách hiệu quả bằng ngăn xếp.**

# ---

# ### 1. Hàm `numSubmat`: Xử lý ma trận

# Hàm này đóng vai trò là "bộ điều khiển" chính. Nó duyệt qua từng hàng của ma trận gốc và biến mỗi hàng thành một bài toán phụ: "Đếm số hình chữ nhật trong một biểu đồ hình cột".

# * `heights = [0] * n`: Mảng `heights` này đóng vai trò là biểu đồ hình cột tạm thời. Ở mỗi hàng, `heights[j]` sẽ lưu trữ chiều cao của cột các số `1` liên tiếp kết thúc tại vị trí `(i, j)`.
# * **Vòng lặp ngoài cùng (`for i in range(m)`)**: Duyệt qua từng hàng của ma trận.
# * **Vòng lặp trong (`for j in range(n)`)**: Cập nhật chiều cao của biểu đồ hình cột cho hàng hiện tại.
#     * Nếu `mat[i][j]` là `1`, chiều cao của cột `j` sẽ được tăng thêm `1` so với chiều cao ở hàng trên.
#     * Nếu `mat[i][j]` là `0`, cột các số `1` bị ngắt, do đó chiều cao của cột `j` được reset về `0`.
# * `res += self.countRow(heights)`: Sau khi mảng `heights` đã được cập nhật, nó được truyền vào hàm `countRow` để tính tổng số ma trận con có đáy nằm ở hàng hiện tại. Kết quả được cộng dồn vào biến `res`.

# ---

# ### 2. Hàm `countRow`: Đếm hình chữ nhật bằng ngăn xếp

# Đây là phần phức tạp và quan trọng nhất. Hàm này giải quyết bài toán phụ: **đếm tổng số hình chữ nhật trong một biểu đồ hình cột** trong thời gian tuyến tính ($O(N)$). Nó sử dụng một ngăn xếp đơn điệu tăng dần.

# * `stack = []`: Ngăn xếp này sẽ lưu trữ **chỉ số (index)** của các cột. Nó luôn duy trì các cột có chiều cao tăng dần.
# * `subs = [0] * len(heights)`: Mảng `subs[i]` sẽ lưu trữ tổng số hình chữ nhật có đáy ở hàng hiện tại và kết thúc tại cột `i`.

# * **Vòng lặp (`for i, h in enumerate(heights)`)**: Duyệt qua từng cột của biểu đồ hình cột.
# * `while stack and heights[stack[-1]] >= h`:
#     * Đây là logic cốt lõi. Vòng lặp này **loại bỏ** (pop) các chỉ số từ ngăn xếp nếu chiều cao của cột tương ứng **lớn hơn hoặc bằng** chiều cao của cột hiện tại (`h`).
#     * Mục tiêu là tìm chỉ số của cột **đầu tiên** bên trái có chiều cao **nhỏ hơn** `h`.
# * `if stack:`: Nếu ngăn xếp không rỗng sau khi `while` loop, điều đó có nghĩa là cột thấp hơn gần nhất ở bên trái là `stack[-1]`.
#     * `subs[i] = subs[left] + h * (i - left)`: Tổng số hình chữ nhật kết thúc tại cột `i` bằng tổng số hình chữ nhật kết thúc tại cột `left` (cột thấp hơn gần nhất bên trái) cộng với số hình chữ nhật mới tạo ra bằng cách mở rộng chiều cao `h` từ cột `left` đến cột `i`.
# * `else:`: Nếu ngăn xếp rỗng, điều đó có nghĩa là `h` là cột thấp nhất tính từ đầu biểu đồ.
#     * `subs[i] = h * (i + 1)`: Số hình chữ nhật mới tạo thành là `h` nhân với chiều rộng từ đầu đến cột `i` (tức là `i+1`).
# * `stack.append(i)`: Đẩy chỉ số của cột hiện tại vào ngăn xếp.
# * `return sum(subs)`: Cuối cùng, tổng tất cả các giá trị trong mảng `subs` sẽ là tổng số hình chữ nhật của biểu đồ này.

# ### Tại sao nó hiệu quả?

# * **Độ phức tạp về thời gian:** $O(M \times N)$. Vòng lặp bên ngoài chạy $M$ lần, và hàm `countRow` chạy $O(N)$ lần. Mặc dù có vòng lặp `while` bên trong `countRow`, mỗi chỉ số chỉ được đẩy vào và lấy ra khỏi ngăn xếp tối đa một lần, do đó độ phức tạp của nó vẫn là $O(N)$.
# * **Độ phức tạp về không gian:** $O(N)$ để lưu mảng `heights`, ngăn xếp `stack`, và mảng `subs`.

# Đây là một giải pháp rất thanh lịch và tối ưu, sử dụng tư duy quy hoạch động (xây dựng `heights`) kết hợp với cấu trúc dữ liệu stack để giải quyết bài toán một cách hiệu quả.