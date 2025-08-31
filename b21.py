# 37. Sudoku Solver(31/08/2025)
from typing import List
class Solution:

    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Không cần trả về gì, chỉ cần sửa đổi bảng Sudoku tại chỗ (in-place).
        """
        # Ba mảng bitmask để theo dõi các số đã được sử dụng trong mỗi hàng, cột và ô 3x3.
        # Mỗi bit trong mask tương ứng với một chữ số (ví dụ: bit 0 cho số 1, bit 1 cho số 2, v.v.).
        self.row_mask = [0] * 9  # Các số đã dùng ở mỗi hàng.
        self.col_mask = [0] * 9  # Các số đã dùng ở mỗi cột.
        self.box_mask = [0] * 9  # Các số đã dùng ở mỗi ô 3x3.
        self.empties = []        # Danh sách lưu trữ tọa độ của các ô trống.

        # Khởi tạo các mask và thu thập các ô trống
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    # Nếu là ô trống, thêm tọa độ của nó vào danh sách.
                    # Tọa độ được mã hóa thành một số nguyên duy nhất (0-80).
                    self.empties.append(r * 9 + c)
                else:
                    # Nếu đã có số, cập nhật các mask tương ứng.
                    d = int(board[r][c]) - 1  # Chuyển số từ '1'->'9' thành chỉ số 0-8.
                    bit = 1 << d             # Tạo bitmask cho số đó (ví dụ: số 1 -> 0b1, số 2 -> 0b10).
                    box_idx = self._box_index(r, c) # Lấy chỉ số của ô 3x3.
                    self.row_mask[r] |= bit    # Đặt bit cho hàng.
                    self.col_mask[c] |= bit    # Đặt bit cho cột.
                    self.box_mask[box_idx] |= bit # Đặt bit cho ô 3x3.
        
        # Bắt đầu thuật toán tìm kiếm theo chiều sâu (DFS).
        # k là chỉ số của ô trống đang được xử lý trong danh sách `self.empties`.
        self.dfs(board, 0)

    def _box_index(self, r: int, c: int) -> int:
        # Hàm trợ giúp để tính chỉ số của ô 3x3 từ tọa độ hàng và cột.
        return (r // 3) * 3 + (c // 3)

    def _place(self, board: list[list[str]], r: int, c: int, b: int, d: int, bit: int) -> None:
        # Hàm đặt một số vào bảng và cập nhật tất cả các mask.
        board[r][c] = str(d + 1)
        self.row_mask[r] |= bit
        self.col_mask[c] |= bit
        self.box_mask[b] |= bit

    def _unplace(self, board: list[list[str]], r: int, c: int, b: int, d: int, bit: int) -> None:
        # Hàm hoàn tác việc đặt một số và khôi phục các mask.
        board[r][c] = '.'
        self.row_mask[r] ^= bit # Sử dụng XOR để xóa bit.
        self.col_mask[c] ^= bit
        self.box_mask[b] ^= bit

    def dfs(self, board: list[list[str]], k: int) -> bool:
        # Hàm tìm kiếm theo chiều sâu (DFS) đệ quy.
        
        # Điều kiện dừng: Nếu đã điền hết tất cả các ô trống, trả về True (đã giải xong).
        if k == len(self.empties):
            return True

        # Thuật toán Most Restrictive Variable (MRV)
        # Chọn ô trống có ít lựa chọn hợp lệ nhất để giải trước.
        best_idx = k
        best_choices_count = 10 # 10 là số lớn hơn 9 (số lựa chọn tối đa).
        best_choices_mask = 0

        for i in range(k, len(self.empties)):
            pos = self.empties[i]
            r, c = pos // 9, pos % 9
            b = self._box_index(r, c)
            
            # Tính các số đã được sử dụng (OR của 3 mask).
            used = self.row_mask[r] | self.col_mask[c] | self.box_mask[b]
            # Lấy các lựa chọn hợp lệ (bits = 0) và giới hạn trong 9 bit đầu.
            choices = (~used) & 0x1FF 
            # Đếm số lượng lựa chọn.
            count = bin(choices).count('1')

            # Nếu tìm thấy ô có ít lựa chọn hơn, cập nhật "ô tốt nhất".
            if count < best_choices_count:
                best_choices_count = count
                best_choices_mask = choices
                best_idx = i
                if count == 1:
                    # Nếu chỉ có 1 lựa chọn, không thể tối ưu hơn, thoát vòng lặp.
                    break
            
            # Nếu một ô có 0 lựa chọn, nhánh này không thể giải được.
            # Dừng lại và quay lui ngay lập tức.
            if count == 0:
                return False

        # Hoán đổi ô tốt nhất vào vị trí hiện tại (k).
        self.empties[k], self.empties[best_idx] = self.empties[best_idx], self.empties[k]
        
        pos = self.empties[k]
        r, c = pos // 9, pos % 9
        b = self._box_index(r, c)
        
        # Lấy mask lựa chọn đã tính ở trên.
        choices = best_choices_mask if best_choices_mask != 0 else ((~(self.row_mask[r] | self.col_mask[c] | self.box_mask[b])) & 0x1FF)
        
        # Duyệt qua từng lựa chọn hợp lệ.
        while choices:
            # Lấy bit có giá trị thấp nhất (low-bit trick).
            bit = choices & -choices
            # Chuyển bit thành chỉ số chữ số (d từ 0-8).
            d = (bit).bit_length() - 1

            # Thử đặt chữ số vào ô hiện tại.
            self._place(board, r, c, b, d, bit)
            # Gọi đệ quy để giải ô tiếp theo.
            if self.dfs(board, k + 1):
                return True
            # Nếu đệ quy không thành công, hoàn tác.
            self._unplace(board, r, c, b, d, bit)
            
            # Chuyển sang lựa chọn tiếp theo bằng cách xóa bit đã thử.
            choices &= choices - 1

        # Hoán đổi lại ô để khôi phục thứ tự ban đầu trước khi quay lui.
        self.empties[k], self.empties[best_idx] = self.empties[best_idx], self.empties[k]

        return False # Trả về False để quay lui.


#     Dưới đây là giải thích chi tiết về thuật toán giải Sudoku đã được chuyển đổi sang Python.

# ### Giới thiệu chung về thuật toán

# Thuật toán này sử dụng phương pháp **quay lui (backtracking)** kết hợp với một kỹ thuật tối ưu hóa được gọi là **Most Restrictive Variable (MRV)**, hay còn gọi là Nguyên tắc Lựa chọn Hạn chế nhất.

# Thay vì duyệt các ô trống theo một thứ tự cố định (ví dụ: từ trái sang phải, từ trên xuống dưới), thuật toán này luôn tìm và điền vào ô trống **có ít lựa chọn hợp lệ nhất**. Điều này giúp giảm đáng kể số lượng bước quay lui, vì nó sẽ nhanh chóng phát hiện ra các trường hợp không thể giải được (một ô trống không có lựa chọn nào).

# ### Cấu trúc dữ liệu chính

# Thuật toán sử dụng các cấu trúc dữ liệu sau để theo dõi trạng thái của bảng Sudoku một cách hiệu quả:

# * **`row_mask`, `col_mask`, `box_mask`**: Đây là ba mảng có kích thước 9, mỗi phần tử là một **bitmask** (mặt nạ bit).
#     * Mỗi bitmask đại diện cho các chữ số đã được sử dụng trong một hàng, cột hoặc ô 3x3.
#     * Ví dụ: nếu `row_mask[0]` có giá trị `0b100000010`, điều đó có nghĩa là các chữ số `2` và `9` đã được sử dụng trong hàng đầu tiên.
#     * Việc sử dụng bitmask cho phép kiểm tra sự hợp lệ của một chữ số trong thời gian hằng số O(1).
# * **`empties`**: Một danh sách chứa tọa độ của tất cả các ô trống trên bảng. Các tọa độ này được mã hóa thành một số nguyên duy nhất (ví dụ: `r * 9 + c`). Thuật toán sẽ sắp xếp lại danh sách này trong quá trình chạy để luôn đặt ô có ít lựa chọn nhất lên đầu.

# ### Các bước của thuật toán

# #### 1. Khởi tạo

# * Thuật toán duyệt qua toàn bộ bảng Sudoku ban đầu.
# * Với mỗi ô đã có số, nó cập nhật ba mảng bitmask (`row_mask`, `col_mask`, `box_mask`) tương ứng.
# * Với mỗi ô trống (`.`), nó lưu tọa độ vào danh sách `empties`.

#### 2. Hàm đệ quy `dfs(board, k)`

# Đây là hàm chính thực hiện quá trình quay lui.

# * **Điều kiện cơ sở:** Nếu `k` bằng với số lượng ô trống (`len(self.empties)`), điều đó có nghĩa là tất cả các ô trống đã được điền và bảng đã được giải thành công. Hàm sẽ trả về `True`.
# * **Bước MRV:**
#     * Hàm duyệt qua các ô trống từ vị trí `k` đến cuối danh sách `empties`.
#     * Với mỗi ô trống, nó tính toán số lượng lựa chọn hợp lệ bằng cách sử dụng các bitmask.
#     * Nó tìm ra ô trống có số lựa chọn ít nhất (`best_choices_count`).
#     * Nếu một ô có 0 lựa chọn, thuật toán sẽ quay lui ngay lập tức và trả về `False` vì không thể điền được.
#     * Sau khi tìm thấy ô tối ưu, nó hoán đổi ô đó với ô tại vị trí `k` trong danh sách `empties`. Điều này đảm bảo rằng ở bước tiếp theo, thuật toán sẽ bắt đầu với ô dễ nhất (khó nhất để giải).
# * **Duyệt và quay lui:**
#     * Hàm lấy ô trống mới tại vị trí `k`.
#     * Nó duyệt qua tất cả các lựa chọn hợp lệ cho ô đó (được lưu trong `best_choices_mask`).
#     * Với mỗi lựa chọn (`d`):
#         * Nó **đặt** chữ số `d+1` vào ô đó và cập nhật các bitmask.
#         * Nó gọi đệ quy `dfs(board, k + 1)` để tiếp tục giải ô tiếp theo.
#         * Nếu cuộc gọi đệ quy trả về `True`, có nghĩa là đã tìm thấy lời giải. Hàm sẽ trả về `True` ngay lập tức để thoát khỏi quá trình.
#         * Nếu không, nó **hoàn tác** (unplace) chữ số vừa đặt và khôi phục lại các bitmask.
#     * Nếu vòng lặp kết thúc mà không tìm thấy lựa chọn nào dẫn đến lời giải, hàm sẽ trả về `False`, báo hiệu cần quay lui ở bước trước đó.

# ### Ưu điểm của thuật toán

# * **Tối ưu hóa mạnh mẽ:** Kỹ thuật MRV giảm đáng kể không gian tìm kiếm. Thay vì thử các ô dễ trước, nó tập trung vào các ô khó, giúp phát hiện sớm các con đường sai và cắt nhánh tìm kiếm.
# * **Sử dụng bitmask:** Việc sử dụng các bitmask giúp kiểm tra tính hợp lệ của một chữ số trong thời gian O(1), làm cho quá trình tìm kiếm các lựa chọn trở nên cực kỳ nhanh chóng.
# * **Hiệu quả về không gian:** Thuật toán không cần tạo ra nhiều bản sao của bảng Sudoku, mà chỉ cần thay đổi tại chỗ (in-place) và sử dụng các mảng bitmask nhỏ.