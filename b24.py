# 3027. Find the Number of Ways to Place People II(03/09/2025)
from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Bước 1: Sắp xếp các điểm
        # Sắp xếp các điểm theo tọa độ x tăng dần.
        # Nếu x bằng nhau, sắp xếp theo tọa độ y giảm dần.
        # Ví dụ: [[1, 5], [1, 2], [3, 4]] sẽ thành [[1, 5], [1, 2], [3, 4]]
        # Việc này giúp đảm bảo điểm sau luôn có x >= điểm trước.
        points.sort(key=lambda p: (p[0], -p[1]))

        # Khởi tạo biến đếm
        res = 0
        
        # Bước 2: Duyệt qua các điểm để tìm cặp
        # Vòng lặp ngoài: Chọn điểm đầu tiên (người A)
        for i, (x1, y1) in enumerate(points):
            
            # Khởi tạo biến y_max để theo dõi tọa độ y của điểm hợp lệ gần nhất.
            # -inf đại diện cho giá trị y rất nhỏ, đảm bảo điểm đầu tiên sẽ được chọn.
            y_max = float('-inf')
            
            # Vòng lặp trong: Chọn điểm thứ hai (người B) từ các điểm sau người A
            for (x2, y2) in points[i + 1:]:
                
                # Kiểm tra điều kiện "Đông-Nam" và "không có điểm ở giữa"
                # y1 >= y2: Đảm bảo B có tọa độ y nhỏ hơn hoặc bằng A. (Đếm các cặp Đông-Nam)
                # y2 > y_max: Đảm bảo không có điểm nào khác nằm giữa B và đường thẳng y=y_max.
                #             Đây là cách kiểm tra hiệu quả điều kiện "không có điểm nào ở giữa".
                if y1 >= y2 > y_max:
                    
                    # Nếu thỏa mãn, đây là một cặp hợp lệ
                    res += 1
                    
                    # Cập nhật y_max để loại trừ các điểm có y nhỏ hơn y2 trong các lần lặp tiếp theo
                    y_max = y2
        
        # Trả về tổng số cặp hợp lệ đã tìm được
        return res
























# // Bạn được
# // cho một
# // mảng các
# // tọa độ, gọi là`points`,
# // trong đó
# // mỗi phần
# // tử là
# // một cặp`[x,y]`
# // biểu thị
# // tọa độ
# // của một
# // người.

# // Mục tiêu
# // của bạn
# // là tìm
# // số cách
# // để chọn**
# // hai người**(
# // gọi là
# // người A
# // và người B)
# // thỏa mãn
# // các điều
# // kiện sau:

# // 1.**
# // Người B
# // nằm ở
# // phía Đông
# // Bắc của
# // người A:**
# // Điều này
# // có nghĩa
# // là tọa độ`x`
# // của người
# // B phải
# // lớn hơn
# // hoặc bằng`x`
# // của người

# // A (`xB >= xA`), và tọa độ `y` của người B phải lớn hơn hoặc bằng `y` của
# // người A (`yB >= yA`).
# // 2. **Không có người nào khác ở trong "hộp" của họ:** Giả sử bạn vẽ một hình
# // chữ nhật với hai đỉnh đối diện là người A và người B. Hình chữ nhật này được
# // định nghĩa bởi các cạnh có tọa độ `x` từ `xA` đến `xB` và `y` từ `yA` đến
# // `yB`. Điều kiện thứ hai yêu cầu không có bất kỳ người nào khác trong danh
# // sách `points` nằm bên trong hình chữ nhật

# // này (tức là không có người C nào có tọa độ `xC` và `yC` thỏa mãn `xA <= xC <=
# // xB` và `yA <= yC <= yB`, ngoại trừ người A và người B).

# // ---


# Đoạn mã Python bạn cung cấp là một giải pháp tối ưu hơn cho bài toán **3027. Find the Number of Ways to Place People II**. Dưới đây là giải thích chi tiết về thuật toán này.



# ### Giải thích thuật toán

# Thuật toán này dựa trên một cách tiếp cận thông minh để giảm độ phức tạp từ $O(N^3)$ xuống $O(N^2)$. Thay vì duyệt qua tất cả các bộ ba điểm, nó sử dụng sắp xếp và một vòng lặp lồng nhau để tìm các cặp hợp lệ.

# 1.  **Sắp xếp các điểm:**
#     * Bước đầu tiên và quan trọng nhất là sắp xếp mảng `points`.
#     * Chúng ta sắp xếp các điểm theo tọa độ `x` tăng dần.
#     * Nếu hai điểm có cùng tọa độ `x`, ta sắp xếp chúng theo tọa độ `y` giảm dần.
#     * Việc sắp xếp này đảm bảo rằng khi chúng ta duyệt qua các điểm theo thứ tự, mọi điểm ở phía sau đều có tọa độ `x` lớn hơn hoặc bằng điểm hiện tại. Điều này tự động thỏa mãn một phần của điều kiện "Đông Bắc" ($B.x \ge A.x$).

# 2.  **Duyệt và tìm kiếm cặp:**
#     * Ta sử dụng một vòng lặp ngoài để chọn điểm **A** (điểm "trái" hoặc "dưới"). Gọi điểm này là `points[i]`.
#     * Sau đó, ta dùng một vòng lặp trong để duyệt qua tất cả các điểm sau `points[i]` trong mảng đã sắp xếp. Gọi điểm này là **B** (điểm "phải" hoặc "trên").
#     * Nhờ việc sắp xếp, chúng ta chỉ cần kiểm tra điều kiện `B.y >= A.y` để xác định xem B có ở phía Đông Bắc của A không.

# 3.  **Làm thế nào để kiểm tra điều kiện "không có điểm nào ở giữa"?**
#     * Đây là phần tinh tế của thuật toán. Khi ta duyệt từ điểm `i` sang phải, ta cần đảm bảo không có điểm nào khác nằm trong "hộp" tạo bởi A và B.
#     * Khi xét một điểm `points[j]` (là điểm B), chúng ta biết rằng `x` của nó đã lớn hơn hoặc bằng `x` của `points[i]`.
#     * Chúng ta cần tìm một điểm `points[j]` có `y` nằm trong khoảng từ `A.y` đến `B.y` và không có điểm nào khác chen giữa.
#     * Để làm điều này, chúng ta sử dụng một biến `y` để theo dõi tọa độ `y` của điểm "hợp lệ" gần nhất đã tìm thấy. Ban đầu, `y` được gán một giá trị rất nhỏ (vô cực âm).
#     * Khi duyệt qua các điểm `points[j]` từ `i + 1` trở đi:
#         * Ta kiểm tra xem `y2` (`points[j].y`) có nằm trong dải `y` hợp lệ hay không. Dải `y` hợp lệ là `y1 >= y2 > y`.
#         * **`y1 >= y2`**: Đảm bảo rằng điểm `B` không nằm quá cao so với điểm `A`.
#         * **`y2 > y`**: Đây là chìa khóa. Điều kiện này đảm bảo rằng điểm `B` có `y` lớn hơn tất cả các điểm "hợp lệ" đã tìm thấy trước đó trong dải từ `i+1` đến `j-1`. Điều này có nghĩa là không có điểm nào khác nằm trên đường thẳng đứng từ `B` xuống, nằm trong hình chữ nhật của `A` và `B`.
#     * Nếu một điểm `points[j]` thỏa mãn cả hai điều kiện trên, ta coi nó là một cặp hợp lệ với `points[i]`, tăng `res` lên 1, và cập nhật biến `y = y2`. Việc cập nhật `y` này sẽ loại trừ các điểm có `y` nhỏ hơn hoặc bằng `y2` khỏi các lần kiểm tra sau, đảm bảo rằng chúng ta chỉ chọn các điểm hợp lệ nhất và không có điểm nào ở giữa.

# ### Tóm tắt

# Thuật toán này hoạt động hiệu quả vì nó tận dụng lợi thế của việc sắp xếp để loại bỏ việc kiểm tra `x` và giảm việc kiểm tra `y` thành một bước đơn giản hơn. Thay vì duyệt qua tất cả các điểm để tìm vật cản (độ phức tạp $O(N)$), nó chỉ cần duyệt qua các điểm sau điểm hiện tại và sử dụng biến `y` để kiểm soát, dẫn đến độ phức tạp tổng thể là $O(N^2)$.