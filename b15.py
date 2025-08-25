# 498. Diagonal Traverse (25/08/2025)

class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            return []

        rows, cols = len(mat), len(mat[0])
        result = []
        r, c = 0, 0  # Hàng và cột hiện tại
        direction_up = True  # Hướng đi, True là lên, False là xuống

        for _ in range(rows * cols):
            result.append(mat[r][c])

            if direction_up:
                # Đi lên: r giảm, c tăng
                if r > 0 and c < cols - 1:
                    r -= 1
                    c += 1
                else:  # Đã chạm biên
                    direction_up = False
                    if c < cols - 1:
                        c += 1
                    else:
                        r += 1
            else:  # Hướng đi xuống
                # Đi xuống: r tăng, c giảm
                if r < rows - 1 and c > 0:
                    r += 1
                    c -= 1
                else:  # Đã chạm biên
                    direction_up = True
                    if r < rows - 1:
                        r += 1
                    else:
                        c += 1
        return result


# Đoạn mã này là một thuật toán hiệu quả để duyệt một ma trận theo đường chéo. Nó sử dụng một kỹ thuật mô phỏng chuyển động, di chuyển qua từng ô một và thay đổi hướng khi chạm vào biên của ma trận.

# ---

# ### Giải thích thuật toán

# Thuật toán này hoạt động bằng cách sử dụng một con trỏ (`r`, `c`) để theo dõi vị trí hiện tại trong ma trận và một biến boolean (`direction_up`) để quản lý hướng di chuyển.

# 1.  **Xử lý trường hợp đặc biệt:**
#     * `if not mat or not mat[0]: return []`
#         * Kiểm tra nếu ma trận rỗng hoặc ma trận có hàng nhưng không có cột nào. Nếu vậy, không có gì để duyệt, trả về một danh sách rỗng.

# 2.  **Khởi tạo:**
#     * `rows, cols = len(mat), len(mat[0])`: Lấy kích thước của ma trận.
#     * `result = []`: Một danh sách rỗng để lưu trữ các phần tử theo thứ tự duyệt.
#     * `r, c = 0, 0`: Khởi tạo tọa độ bắt đầu ở góc trên cùng bên trái của ma trận.
#     * `direction_up = True`: Đặt hướng di chuyển ban đầu là đi lên.

# 3.  **Vòng lặp chính:**
#     * `for _ in range(rows * cols):`
#         * Vòng lặp này chạy đúng bằng số phần tử trong ma trận (`rows * cols`). Điều này đảm bảo rằng mỗi phần tử sẽ được xử lý đúng một lần.

# 4.  **Thêm phần tử vào kết quả:**
#     * `result.append(mat[r][c])`: Trong mỗi lần lặp, thuật toán lấy phần tử tại tọa độ hiện tại `(r, c)` và thêm vào danh sách kết quả.

# 5.  **Điều khiển hướng di chuyển:**
#     * Đây là phần cốt lõi của thuật toán. Logic được chia thành hai nhánh chính: khi đi lên (`direction_up` là `True`) và khi đi xuống.

#     * **Khi đi lên (UP):**
#         * `if r > 0 and c < cols - 1:`
#             * Đây là trường hợp thông thường: Di chuyển lên trên và sang phải. Tọa độ mới sẽ là `(r-1, c+1)`.
#         * `else:`
#             * Khi chạm vào biên. Đã đến lúc phải đổi hướng (`direction_up = False`).
#             * `if c < cols - 1: c += 1`: Nếu chưa chạm biên phải, di chuyển sang phải một bước để bắt đầu đường chéo tiếp theo.
#             * `else: r += 1`: Nếu đã chạm biên phải, di chuyển xuống dưới một bước để bắt đầu đường chéo tiếp theo.

#     * **Khi đi xuống (DOWN):**
#         * `if r < rows - 1 and c > 0:`
#             * Đây là trường hợp thông thường: Di chuyển xuống dưới và sang trái. Tọa độ mới sẽ là `(r+1, c-1)`.
#         * `else:`
#             * Khi chạm vào biên. Đã đến lúc phải đổi hướng (`direction_up = True`).
#             * `if r < rows - 1: r += 1`: Nếu chưa chạm biên dưới, di chuyển xuống dưới một bước để bắt đầu đường chéo tiếp theo.
#             * `else: c += 1`: Nếu đã chạm biên dưới, di chuyển sang phải một bước để bắt đầu đường chéo tiếp theo.

# 6.  **Trả về kết quả:**
#     * `return result`: Sau khi vòng lặp hoàn thành, danh sách `result` sẽ chứa tất cả các phần tử của ma trận theo đúng thứ tự duyệt đường chéo.

# ---

# ### Tóm tắt

# Thuật toán này giải quyết bài toán bằng cách **mô phỏng quá trình duyệt ma trận**: nó bắt đầu tại `(0, 0)`, di chuyển theo một hướng (lên hoặc xuống) cho đến khi gặp một biên. Khi gặp biên, nó sẽ đổi hướng và di chuyển một bước để bắt đầu đường chéo tiếp theo. Quá trình này lặp lại cho đến khi tất cả các phần tử đã được duyệt. Cách tiếp cận này hiệu quả vì nó chỉ cần một lần duyệt duy nhất trên toàn bộ ma trận.