#  36. Valid Sudoku(30/08/2025)
# Đây là một giải pháp rất hiệu quả cho bài toán "Valid Sudoku", sử dụng kỹ thuật **bitmask** để kiểm tra tính hợp lệ. Thuật toán này rất tối ưu, đặc biệt về mặt tốc độ và không gian, bởi nó dùng các phép toán bit thay vì các cấu trúc dữ liệu phức tạp.

# -----

# ### Phân tích Thuật toán

# Ý tưởng cốt lõi là sử dụng các số nguyên làm **mặt nạ bit** để theo dõi các số đã xuất hiện trong mỗi hàng, cột, và khối 3x3.

#   * Một số nguyên 32-bit có thể biểu diễn 32 trạng thái (bit). Chúng ta chỉ cần dùng các bit từ 1 đến 9 để biểu thị sự xuất hiện của các số từ 1 đến 9.

#       * Bit 1 (`1 << 1`) đại diện cho số 1.
#       * Bit 2 (`1 << 2`) đại diện cho số 2.
#       * ...và cứ thế.

#   * Thuật toán này sử dụng ba mảng số nguyên, mỗi mảng 9 phần tử, để lưu trữ các mặt nạ bit này:

#       * **`row_masks`**: Theo dõi các số đã xuất hiện trong 9 hàng. `row_masks[r]` lưu trạng thái cho hàng `r`.
#       * **`col_masks`**: Theo dõi các số đã xuất hiện trong 9 cột. `col_masks[c]` lưu trạng thái cho cột `c`.
#       * **`box_masks`**: Theo dõi các số đã xuất hiện trong 9 khối 3x3. `box_masks[box_idx]` lưu trạng thái cho khối `box_idx`.

# ### Chú thích chi tiết trong mã nguồn

from typing import List
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Khởi tạo ba mảng mặt nạ bit, tất cả giá trị ban đầu là 0.
        # Một giá trị 0 có nghĩa là chưa có số nào được nhìn thấy.
        row_masks = [0] * 9
        col_masks = [0] * 9
        box_masks = [0] * 9

        # Vòng lặp chính: duyệt qua từng ô (r, c) của bảng 9x9.
        for r in range(9):
            for c in range(9):
                char = board[r][c]
                
                # Bỏ qua các ô trống.
                if char == '.':
                    continue

                # Chuyển ký tự số sang số nguyên và tạo mặt nạ bit tương ứng.
                # Ví dụ: '1' trở thành 1, 1 << 1 = 2 (nhị phân 10).
                # '9' trở thành 9, 1 << 9 = 512.
                bit = 1 << int(char)

                # Tính chỉ số của khối 3x3 mà ô (r, c) thuộc về.
                # Ví dụ: (r=4, c=5) thuộc khối (4/3)*3 + (5/3) = 1*3+1 = 4.
                box_idx = (r // 3) * 3 + (c // 3)

                # --- Kiểm tra trùng lặp ---
                # Sử dụng phép toán bitwise AND (&) để kiểm tra xem bit tương ứng đã được bật chưa.
                # Nếu kết quả khác 0, nghĩa là số đó đã xuất hiện trước đó.
                if (row_masks[r] & bit) or \
                   (col_masks[c] & bit) or \
                   (box_masks[box_idx] & bit):
                    return False
                
                # --- Cập nhật mặt nạ ---
                # Nếu không có trùng lặp, dùng phép toán bitwise OR (|) để bật bit tương ứng.
                # Điều này đánh dấu rằng số đó đã được nhìn thấy trong hàng, cột và khối này.
                row_masks[r] |= bit
                col_masks[c] |= bit
                box_masks[box_idx] |= bit
        
        # Nếu duyệt xong toàn bộ bảng mà không tìm thấy lỗi nào, bảng là hợp lệ.
        return True
