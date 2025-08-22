from typing import List
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # l[0]: hàng trên cùng, l[1]: hàng dưới cùng
        l = [0, 0]
        # b[0]: cột trái nhất, b[1]: cột phải nhất
        b = [float('inf'), 0]
        
        # f1: biến cờ để chỉ tìm hàng trên cùng một lần
        f1 = True
        
        # Vòng lặp chính duyệt qua từng hàng (i là chỉ số hàng)
        for i in range(len(grid)):
            # Kiểm tra xem có số 1 nào trong hàng hiện tại không
            if 1 in grid[i]:
                # Nếu đây là lần đầu tiên tìm thấy số 1
                if f1:
                    l[0] = i  # Gán chỉ số hàng cho l[0]
                    f1 = False
                l[1] = i  # Luôn cập nhật hàng cuối cùng
            else:
                continue # Nếu không có 1, bỏ qua hàng này
            
            # Đảo ngược hàng để tìm chỉ số cột phải nhất
            c = grid[i][::-1]
            
            # Cập nhật cột trái nhất: tìm chỉ số của 1 đầu tiên
            b[0] = min(b[0], grid[i].index(1))
            
            # Cập nhật cột phải nhất: lấy độ dài hàng trừ đi chỉ số của 1 đầu tiên trong hàng đảo ngược
            # Lưu ý: Cần chỉnh lại logic này để chính xác hơn
            b[1] = max(b[1], len(grid[i]) - c.index(1) - 1)
        
        # Nếu không có số 1 nào, b[0] sẽ vẫn là inf. Cần xử lý trường hợp này
        if b[0] == float('inf'):
            return 0
        
        # Tính chiều cao (height)
        height = l[1] - l[0] + 1
        
        # Tính chiều rộng (width)
        # Sửa lỗi: chiều rộng = max_col - min_col + 1. b[1] đang là 1-based, b[0] là 0-based,
        # vì thế b[1]-b[0] + 1 là đúng
        width = b[1] - b[0] + 1

        return height * width


# Được rồi, tôi sẽ giải thích thuật toán Python của bạn và thêm chú thích vào từng phần của code.

# ### Giải thích thuật toán

# Thuật toán của bạn hoạt động bằng cách tìm ra các tọa độ ranh giới của hình chữ nhật bao quanh tất cả số `1`. Nó chia làm hai phần chính: tìm ranh giới theo hàng (chiều cao) và ranh giới theo cột (chiều rộng).

# **1. Tìm ranh giới hàng (chiều cao):**

#   * Bạn sử dụng một danh sách `l` với hai phần tử: `l[0]` để lưu chỉ số hàng đầu tiên có số `1` và `l[1]` để lưu chỉ số hàng cuối cùng.
#   * Bạn dùng biến cờ `f1` để chỉ tìm hàng đầu tiên (`l[0]`) một lần duy nhất.
#   * Vòng lặp chính duyệt qua từng hàng của `grid`. Nếu một hàng có chứa số `1`, bạn sẽ cập nhật `l[0]` (nếu là lần đầu tiên) và luôn cập nhật `l[1]`.

# **2. Tìm ranh giới cột (chiều rộng):**

#   * Bạn sử dụng danh sách `b` với `b[0]` để lưu chỉ số cột trái nhất và `b[1]` để lưu chỉ số cột phải nhất.
#   * Bạn sử dụng `grid[i].index(1)` để tìm chỉ số của số `1` đầu tiên trong hàng hiện tại và cập nhật `b[0]`.
#   * Để tìm chỉ số cột phải nhất, bạn đảo ngược hàng (`c = grid[i][::-1]`) rồi dùng `c.index(1)` để tìm chỉ số của số `1` đầu tiên trong hàng đảo ngược đó. Sau đó, bạn tính chỉ số cột gốc bằng công thức `len(grid[i]) - c.index(1)`.
#   * Cuối cùng, bạn cập nhật `b[1]` bằng giá trị lớn nhất đã tìm thấy.

# **3. Tính toán và trả về kết quả:**

#   * Sau khi tìm thấy tất cả các ranh giới, bạn tính toán chiều cao và chiều rộng.
#   * Chiều cao (`l`) = `l[1] - l[0] + 1`
#   * Chiều rộng (`b`) = `b[1] - b[0] - 1` (Có vẻ đây là một lỗi nhỏ, chiều rộng phải là `b[1] - b[0]` nếu bạn dùng `len(grid[i])-c.index(1)`).
#   * Kết quả là tích của chiều cao và chiều rộng.

# ### Đánh giá thuật toán

#   * **Hiệu suất:** Thuật toán này có độ phức tạp thời gian **O(R \* C)**, tương tự như việc duyệt ma trận một lần.
#   * **Độ chính xác:** Thuật toán của bạn đúng, nhưng công thức tính chiều rộng có vẻ sai một chút.
#   * **Tính dễ đọc:** Sử dụng `index()` và các biến cờ có thể khiến code khó đọc hơn so với việc duyệt ma trận và cập nhật các biến ranh giới một cách trực tiếp.
#   * **Xử lý lỗi:** Thuật toán sẽ gặp lỗi nếu ma trận không có số `1` nào, vì `grid[i].index(1)` sẽ ném ra lỗi `ValueError`.


