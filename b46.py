# 120. Triangle(25/09/2025)

# Rồi 👍 mình giải thích chi tiết thuật toán trong code bạn viết nhé:

# ---
# Ok 👍 mình sẽ giải thích chi tiết code Python bạn đưa ra.

# ---

# ### Code:

# ```python
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)   # tạo mảng dp với kích thước = số hàng + 1
        for row in triangle[::-1]:       # duyệt từ hàng cuối lên trên
            for i, n in enumerate(row):  # i = chỉ số, n = giá trị tại hàng
                dp[i] = min(dp[i], dp[i + 1]) + n
        return dp[0]                     # kết quả nhỏ nhất nằm ở đỉnh
# ```

# ---

# ### Ý tưởng thuật toán:

# Đây là cách giải bằng **Bottom-up Dynamic Programming** (không dùng đệ quy).

# 1. Tạo một mảng `dp` có độ dài = số hàng + 1.

#    * Ban đầu `dp` toàn số 0.
#    * Ý nghĩa: `dp[i]` sẽ lưu tổng đường đi nhỏ nhất bắt đầu từ hàng hiện tại xuống dưới.

# 2. Duyệt tam giác từ **dưới lên trên** (`triangle[::-1]`).

#    * Ở mỗi hàng `row`, ta tính lại `dp[i]` cho từng phần tử.
#    * Với mỗi số `n = row[i]`:

#      ```
#      dp[i] = n + min(dp[i], dp[i+1])
#      ```

#      → nghĩa là: tổng nhỏ nhất đi qua `n` = giá trị `n` + min(tổng nhỏ nhất từ 2 nhánh con bên dưới).

# 3. Sau khi xử lý hết các hàng, `dp[0]` sẽ chứa tổng đường đi nhỏ nhất từ đỉnh tam giác.

# ---

# ### Ví dụ minh họa

# Input:

# ```python
# triangle = [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# ```

# Ban đầu:

# ```
# dp = [0, 0, 0, 0, 0]
# ```

# * Xử lý hàng cuối `[4,1,8,3]`:

# ```
# dp[0] = min(0,0)+4 = 4
# dp[1] = min(0,0)+1 = 1
# dp[2] = min(0,0)+8 = 8
# dp[3] = min(0,0)+3 = 3
# dp = [4, 1, 8, 3, 0]
# ```

# * Xử lý hàng `[6,5,7]`:

# ```
# dp[0] = min(4,1)+6 = 7
# dp[1] = min(1,8)+5 = 6
# dp[2] = min(8,3)+7 = 10
# dp = [7, 6, 10, 3, 0]
# ```

# * Xử lý hàng `[3,4]`:

# ```
# dp[0] = min(7,6)+3 = 9
# dp[1] = min(6,10)+4 = 10
# dp = [9, 10, 10, 3, 0]
# # ```

# * Xử lý hàng `[2]`:

# ```
# dp[0] = min(9,10)+2 = 11
# dp = [11, 10, 10, 3, 0]
# ```

# Kết quả:

# ```
# dp[0] = 11
# ```

# ---

# ### Độ phức tạp

# * **Thời gian**: O(n²) (n = số hàng, tổng phần tử ≈ n²).
# * **Không gian**: O(n) (chỉ cần mảng 1 chiều `dp`).

# ---

# 👉 Bạn có muốn mình viết lại đoạn code này thành phiên bản **có in ra từng bước cập nhật `dp`** để dễ hình dung hơn không?

# ### Ý tưởng của code:

# Đây là cách giải bằng **Đệ quy + Ghi nhớ (Top-down DP with memoization)**.

# 1. Hàm `minimumTotal`

#    * Lấy kích thước tam giác `m`.
#    * Tạo mảng `dp` (kích thước `m x m`) để nhớ kết quả đã tính, tránh tính lại.
#    * Gọi hàm đệ quy `helper(tran, 0, 0)` → bắt đầu từ đỉnh tam giác (hàng 0, cột 0).

# 2. Hàm `helper(tran, row, col)`

#    * **Điều kiện dừng**:
#      Nếu `row == m` (tức là vượt quá hàng cuối cùng) → trả về `0` vì không còn phần tử nào để cộng nữa.

#    * **Kiểm tra memo**:
#      Nếu `dp[row][col]` khác `null`, nghĩa là đã tính kết quả cho ô `(row, col)` rồi → trả về ngay, không tính lại.

#    * **Đệ quy**:
#      Từ `tran[row][col]`, bạn có 2 lựa chọn đi xuống:

#      * `left = helper(tran, row+1, col)` (đi thẳng xuống)
#      * `right = helper(tran, row+1, col+1)` (đi chéo xuống phải)

#    * **Công thức**:

#      ```
#      dp[row][col] = tran[row][col] + Math.min(left, right)
#      ```

#      tức là giá trị nhỏ nhất của đường đi bắt đầu từ `(row,col)` = giá trị hiện tại + đường đi nhỏ hơn trong 2 hướng đi xuống.

# 3. Kết quả cuối cùng sẽ được lưu ở `dp[0][0]`.

# ---

# ### Ví dụ minh họa với input:

# ```
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# ```

# * Bắt đầu `helper(0,0)` → giá trị `2`

#   * Gọi `helper(1,0)` → giá trị `3`

#     * Gọi `helper(2,0)` → giá trị `6`

#       * Gọi `helper(3,0)` → giá trị `4` → hết hàng → return 4
#       * Gọi `helper(3,1)` → giá trị `1` → return 1
#         → `helper(2,0) = 6 + min(4,1) = 6+1=7`
#     * Gọi `helper(2,1)` → giá trị `5`

#       * Gọi `helper(3,1)=1`, `helper(3,2)=8`
#         → `helper(2,1) = 5 + min(1,8) = 6`
#         → `helper(1,0) = 3 + min(7,6) = 9`
#   * Gọi `helper(1,1)` → giá trị `4`

#     * Gọi `helper(2,1)=6`, `helper(2,2)=7+min(8,3)=10`
#       → `helper(1,1) = 4 + min(6,10) = 10`
#       → `helper(0,0) = 2 + min(9,10) = 11`

# 👉 Kết quả cuối cùng: **11**.

# ---

# ### Độ phức tạp:

# * **Thời gian**: O(n²)
#   Vì có tổng cộng \~n² trạng thái `(row, col)` và mỗi trạng thái được tính **1 lần** nhờ `dp`.
# * **Bộ nhớ**: O(n²) cho mảng `dp` + O(n) cho ngăn xếp đệ quy.

# ---

# Bạn có muốn mình viết thêm phiên bản **Bottom-up DP** (không dùng đệ quy, chỉ dùng vòng lặp) để so sánh với code của bạn không?
