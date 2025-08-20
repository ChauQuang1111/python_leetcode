# 1277. Count Square Submatrices with All Ones (20/08/2023)
from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        m, n = len(matrix), len(matrix[0])

        dp = [[0] * (n+1) for _ in range(m+1)] # new int[m+1][n+1];

        ans = 0

        for i in range(m):

            for j in range(n):

             if matrix[i][j]:

                dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j], dp[i][j]) + 1

        ans += dp[i+1][j+1]

        return ans

# Đoạn mã Python bạn cung cấp là một giải pháp rất hiệu quả và ngắn gọn cho bài toán "Count Square Submatrices with All Ones" (LeetCode 1277). Đây là một biến thể của phương pháp lập trình động (Dynamic Programming), sử dụng một ma trận `dp` phụ để lưu trữ kết quả trung gian.

# ### Phân tích thuật toán

# 1.  **Ý tưởng cốt lõi**:
#     * Thuật toán này sử dụng một ma trận **`dp`** có kích thước `(m+1) x (n+1)`, lớn hơn ma trận đầu vào một hàng và một cột. Các hàng và cột "extra" này được khởi tạo với giá trị `0` giúp đơn giản hóa việc xử lý các trường hợp biên (hàng và cột đầu tiên).
#     * Giá trị tại `dp[i+1][j+1]` sẽ lưu trữ **độ dài cạnh của hình vuông lớn nhất** có góc dưới cùng bên phải tại vị trí `matrix[i][j]`.

# 2.  **Duyệt ma trận**:
#     * Thuật toán duyệt qua ma trận đầu vào `matrix` từ trái sang phải, từ trên xuống dưới.
#     * Tại mỗi ô `matrix[i][j]`, nó kiểm tra xem giá trị có phải là `1` hay không.

# 3.  **Công thức lập trình động**:
#     * **Nếu `matrix[i][j]` là `1`**:
#         * Một hình vuông có góc tại `(i, j)` chỉ có thể tồn tại nếu các ô lân cận của nó (phía trên, bên trái và chéo trên-trái) cũng là một phần của hình vuông.
#         * Độ dài cạnh của hình vuông lớn nhất tại `(i, j)` sẽ bằng `1` cộng với giá trị **nhỏ nhất** trong ba ô lân cận đã được tính toán trong ma trận `dp`.
#         * Công thức: `dp[i+1][j+1] = 1 + min(dp[i][j+1], dp[i+1][j], dp[i][j])`.
#         * Tại sao lại sử dụng `i+1, j+1`? Vì ma trận `dp` của chúng ta có kích thước lớn hơn 1, nên `dp[i+1][j+1]` tương ứng với `matrix[i][j]`, `dp[i][j+1]` tương ứng với ô phía trên `matrix[i-1][j]`, `dp[i+1][j]` tương ứng với ô bên trái `matrix[i][j-1]`, và `dp[i][j]` tương ứng với ô chéo trên-trái `matrix[i-1][j-1]`.
#     * **Nếu `matrix[i][j]` là `0`**:
#         * Không thể tạo hình vuông nào có góc tại đây.
#         * Vì ma trận `dp` đã được khởi tạo với `0`, nên `dp[i+1][j+1]` sẽ vẫn giữ giá trị `0`.

# 4.  **Tính tổng kết quả**:
#     * Mỗi khi tính toán được một giá trị `dp[i+1][j+1]` khác `0`, giá trị này cũng chính là số hình vuông mới có thể được tạo ra và kết thúc tại vị trí `matrix[i][j]`.
#     * Ví dụ, nếu `dp[i+1][j+1]` là `3`, có nghĩa là có một hình vuông cạnh `3`, một cạnh `2` và một cạnh `1` đều kết thúc tại `(i, j)`.
#     * Do đó, ta chỉ cần cộng `dp[i+1][j+1]` vào biến `ans` sau mỗi lần tính toán.

# ### Tóm tắt

# Thuật toán này cực kỳ hiệu quả vì nó tránh việc phải kiểm tra từng hình vuông tiềm năng. Bằng cách sử dụng lập trình động, mỗi ô chỉ được xử lý một lần, và kết quả được xây dựng dựa trên các kết quả đã tính toán trước đó. Độ phức tạp thời gian của giải pháp này là `O(m * n)` và độ phức tạp không gian là `O(m * n)`.
 