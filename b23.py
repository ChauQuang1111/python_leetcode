# 3025. Find the Number of Ways to Place People I(02/09/2025)
# Dưới đây là giải thích chi tiết về thuật toán trong đoạn mã Python của bạn, kèm theo chú thích trong code.


# ### Phân tích Thuật toán

# Thuật toán này giải quyết bài toán "Tìm số cặp điểm thỏa mãn" bằng một cách tiếp cận hiệu quả hơn so với phương pháp vét cạn thông thường. Thay vì kiểm tra tất cả các cặp điểm và mọi điểm khác nằm giữa chúng, thuật toán này sử dụng việc **sắp xếp** để đơn giản hóa quá trình kiểm tra.

# Ý tưởng chính là:

# 1.  **Sắp xếp các điểm:** Sắp xếp tất cả các điểm theo thứ tự ưu tiên:
#       * **Tăng dần theo tọa độ x.**
#       * Nếu hai điểm có cùng tọa độ x, sắp xếp **giảm dần theo tọa độ y.**
# 2.  **Duyệt và đếm:** Lặp qua từng điểm đã được sắp xếp, coi mỗi điểm là góc trên bên trái của hình chữ nhật. Sau đó, duyệt qua các điểm còn lại để tìm các điểm có thể làm góc dưới bên phải.

# Việc sắp xếp thông minh này đảm bảo rằng khi bạn duyệt qua các điểm, điều kiện $x\_A \\le x\_B$ luôn được thỏa mãn tự động. Bạn chỉ cần tập trung vào việc kiểm tra tọa độ y và đảm bảo không có điểm nào khác nằm giữa.

# ### Chú thích trong Code

# ```python
import collections

class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        # Bước 1: Sắp xếp các điểm
        # Sắp xếp tăng dần theo tọa độ x.
        # Nếu x bằng nhau, sắp xếp giảm dần theo tọa độ y.
        # Logic này đảm bảo khi duyệt từ trái sang phải, điểm A luôn nằm bên trái B.
        # Nếu A và B có cùng x, điểm A (có y lớn hơn) sẽ đứng trước.
        points.sort(key=lambda x: (x[0], -x[1]))

        result = 0
        
        # Vòng lặp ngoài: Chọn điểm A (góc trên bên trái)
        # Bằng cách duyệt qua mọi điểm, ta cố định điểm A và tìm các điểm B hợp lệ.
        for i, (x0, y0) in enumerate(points):
            # bot: Giới hạn dưới của tọa độ y của các điểm B hợp lệ.
            # -inf: Khởi tạo với giá trị âm vô cùng để điểm B đầu tiên luôn thỏa mãn.
            # Trong quá trình duyệt, bot sẽ lưu tọa độ y của điểm B gần nhất đã tìm thấy.
            bot = float('-inf')
            
            # top: Giới hạn trên của tọa độ y của các điểm B hợp lệ.
            # top = y0, vì điểm B phải có tọa độ y <= y0 (theo định nghĩa).
            top = y0
            
            # Vòng lặp trong: Tìm điểm B (góc dưới bên phải)
            # points[i + 1:] duyệt qua tất cả các điểm đứng sau điểm A.
            # Nhờ việc sắp xếp, các điểm này luôn có x >= x0.
            for (x1, y1) in points[i + 1:]:
                # Kiểm tra điều kiện chính:
                # 1. y1 <= top (tức y1 <= y0): Đảm bảo B nằm dưới hoặc cùng mức y với A.
                # 2. y1 > bot: Đảm bảo không có điểm nào nằm giữa A và B theo trục y.
                if y1 <= top and y1 > bot:
                    # Nếu điều kiện thỏa mãn, ta tìm thấy một cặp hợp lệ (A, B).
                    result += 1
                    
                    # Cập nhật bot: Điểm B hiện tại trở thành giới hạn dưới mới.
                    # Bất kỳ điểm B tiếp theo nào phải có y1 > y_hiện_tại
                    # để không bị "dính" trong hình chữ nhật.
                    bot = y1
                    
                    # Tối ưu hóa: Nếu y1 == top, tức A và B có cùng tọa độ y.
                    # Trong trường hợp này, mọi điểm có x > x0 và y < y1
                    # sẽ nằm trong hình chữ nhật tạo bởi A và B.
                    # Do cách sắp xếp, các điểm tiếp theo chỉ có thể có x >= x1.
                    # Vì thế, bất kỳ điểm nào có y < y1 sẽ nằm trong hình chữ nhật
                    # và không hợp lệ. Ta có thể dừng vòng lặp trong.
                    if y1 == top:
                        break
        return result
















# ### Phân tích đề bài

# Bạn được cho một mảng các điểm `points`, mỗi điểm là một cặp tọa độ $(x, y)$ trên mặt phẳng 2D. Bạn cần tìm và đếm tất cả các cặp điểm $(A, B)$ sao cho:

# 1.  **A ở phía trên bên trái của B:** Điều này có nghĩa là tọa độ $x$ của điểm A phải nhỏ hơn hoặc bằng tọa độ $x$ của điểm B ($x_A \le x_B$), và tọa độ $y$ của điểm A phải lớn hơn hoặc bằng tọa độ $y$ của điểm B ($y_A \ge y_B$).
#     * Nếu $x_A = x_B$, thì A và B nằm trên cùng một đường thẳng đứng.
#     * Nếu $y_A = y_B$, thì A và B nằm trên cùng một đường thẳng ngang.
#     * Nếu $x_A = x_B$ và $y_A = y_B$, điều này không xảy ra vì tất cả các điểm đều khác nhau.
#     * Nếu $x_A < x_B$ và $y_A > y_B$, thì A nằm ở phía trên bên trái của B theo đúng nghĩa đen.

# 2.  **Không có điểm nào khác nằm trong hình chữ nhật (hoặc đường thẳng) tạo bởi A và B:** Hình chữ nhật này được xác định bởi hai điểm A và B là các góc đối diện.
#     * Các điểm nằm trong hình chữ nhật này là các điểm có tọa độ $(x, y)$ thỏa mãn $x_A \le x \le x_B$ và $y_B \le y \le y_A$.
#     * Điều kiện này bao gồm cả các điểm nằm trên biên của hình chữ nhật.
#     * Ví dụ: Nếu A là $(1, 3)$ và B là $(5, 1)$, thì hình chữ nhật tạo bởi chúng là vùng có $1 \le x \le 5$ và $1 \le y \le 3$. Bất kỳ điểm nào khác trong `points` mà có tọa độ thỏa mãn điều kiện này đều làm cho cặp $(A, B)$ không hợp lệ.

# ### Ví dụ minh họa

# * **Ví dụ 1:** `points = [[1,1],[2,2],[3,3]]`
#     * Không có cặp $(A, B)$ nào thỏa mãn điều kiện 1 ($x_A \le x_B$ và $y_A \ge y_B$) ngoài trường hợp $A=B$ (không được tính). Ví dụ: với A=(1,1) và B=(2,2), $x_A < x_B$ nhưng $y_A < y_B$, nên không thỏa mãn.
#     * Kết quả: 0

# * **Ví dụ 2:** `points = [[6,2],[4,4],[2,6]]`
#     * Xét cặp $(A, B)$ với A=(4,4) và B=(6,2). Điều kiện 1: $x_A=4 \le x_B=6$ và $y_A=4 \ge y_B=2$. Thỏa mãn.
#     * Kiểm tra điểm còn lại (2,6). Tọa độ của nó là $(2,6)$, không nằm trong hình chữ nhật tạo bởi A và B (vì $x=2$ không nằm trong khoảng $[4,6]$).
#     * Vậy, cặp (4,4) và (6,2) là một cặp hợp lệ.
#     * Tương tự, cặp A=(2,6) và B=(4,4) cũng là một cặp hợp lệ.
#     * Xét cặp A=(2,6) và B=(6,2). Hình chữ nhật tạo bởi chúng là vùng $2 \le x \le 6$ và $2 \le y \le 6$. Điểm (4,4) nằm bên trong hình chữ nhật này.
#     * Vì vậy, cặp (2,6) và (6,2) không hợp lệ.
#     * Kết quả: 2

# ### Hướng giải quyết

# Một cách tiếp cận đơn giản và hiệu quả cho bài toán này (với giới hạn `n` nhỏ, $2 \le n \le 50$) là sử dụng phương pháp duyệt vét cạn (brute-force).

# 1.  Duyệt qua tất cả các cặp điểm $(i, j)$ có thể có trong mảng `points`.
# 2.  Đối với mỗi cặp $(points[i], points[j])$, giả sử `A = points[i]` và `B = points[j]`.
# 3.  Kiểm tra xem cặp này có thỏa mãn điều kiện 1 không:
#     * $x_A \le x_B$ và $y_A \ge y_B$.
# 4.  Nếu thỏa mãn, tiếp tục kiểm tra điều kiện 2:
#     * Duyệt qua tất cả các điểm `k` khác trong mảng (`k` khác `i` và `k` khác `j`).
#     * Với mỗi điểm `k`, kiểm tra xem nó có nằm trong hình chữ nhật tạo bởi `A` và `B` không. Điều kiện là:
#         * $x_A \le x_k \le x_B$
#         * $y_B \le y_k \le y_A$
#     * Nếu tìm thấy một điểm `k` thỏa mãn cả hai điều kiện trên, thì cặp $(A, B)$ không hợp lệ. Thoát khỏi vòng lặp kiểm tra điểm `k` và chuyển sang cặp $(i, j)$ tiếp theo.
# 5.  Nếu sau khi duyệt hết tất cả các điểm `k` mà không tìm thấy điểm nào nằm bên trong hình chữ nhật, thì cặp $(A, B)$ là một cặp hợp lệ. Tăng biến đếm kết quả lên 1.
# 6.  Sau khi duyệt hết tất cả các cặp $(i, j)$, giá trị của biến đếm chính là kết quả cuối cùng.

# Với $n \le 50$, một thuật toán có độ phức tạp $O(n^3)$ như trên là hoàn toàn khả thi.

