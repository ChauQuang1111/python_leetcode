#  1039. Minimum Score Triangulation of Polygon(29/09/2025)

from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        # dp[i][j] = điểm (cost) nhỏ nhất để chia đa giác con từ đỉnh i đến j (bao gồm i và j)
        dp = [[0] * n for _ in range(n)]
        
        # Xét các đoạn con (sub-polygon) có độ dài L = 3,4,...,n
        # Vì để tạo được một tam giác thì tối thiểu cần 3 đỉnh
        for L in range(3, n+1):
            for i in range(n - L + 1):   # i là điểm bắt đầu
                j = i + L - 1           # j là điểm kết thúc
                best = float('inf')
                
                # Chọn k làm đỉnh ở giữa để tạo tam giác (i, k, j)
                for k in range(i+1, j):
                    # Chi phí gồm:
                    # 1. dp[i][k] = chi phí chia đoạn (i..k)
                    # 2. dp[k][j] = chi phí chia đoạn (k..j)
                    # 3. values[i]*values[k]*values[j] = chi phí tạo tam giác (i,k,j)
                    cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
                    
                    if cost < best:
                        best = cost
                        
                dp[i][j] = best   # Lưu kết quả tối ưu vào dp[i][j]
        
        # Kết quả cuối cùng là chi phí chia toàn bộ đa giác (0..n-1)
        return dp[0][n-1]
# ```

# ---

### Giải thích thuật toán:

# * Bài toán yêu cầu: **tìm cách chia một đa giác lồi thành các tam giác sao cho tổng tích (score) nhỏ nhất**.

# * **Ý tưởng quy hoạch động (Bottom-Up)**:

#   * `dp[i][j]` = chi phí nhỏ nhất để chia đa giác con từ đỉnh `i` đến đỉnh `j`.
#   * Chỉ có ý nghĩa khi đoạn `(i..j)` có ít nhất 3 đỉnh (tức `j - i >= 2`).

# * Với mỗi đoạn `(i..j)`:

#   * Ta thử chọn một đỉnh trung gian `k` (`i < k < j`) để tạo **tam giác (i, k, j)**.
#   * Khi đó:

#     * Chi phí bên trái: `dp[i][k]`
#     * Chi phí bên phải: `dp[k][j]`
#     * Chi phí tam giác mới: `values[i] * values[k] * values[j]`.
#   * Lấy **giá trị nhỏ nhất** trong tất cả các lựa chọn `k`.

# * Cuối cùng, `dp[0][n-1]` chính là kết quả cho cả đa giác.

# ---

# # 👉 Thuật toán này có độ phức tạp **O(n³)** vì:

# # * 2 vòng lặp chọn `(i, j)`
# # * 1 vòng lặp chọn `k` trung gian.

# # ---

# # Bạn có muốn mình viết thêm **ví dụ chạy chi tiết từng bước với input nhỏ (ví dụ [1,3,1,4,1,5])** để thấy rõ `dp` được điền như thế nào không?
















# import java.util.*;

# public class b51 {
#     static Scanner sc = new Scanner(System.in);
#     static int[][] dp; // Mảng lưu kết quả trung gian (memoization)

#     public static void main(String[] args) {

#         // Nhập số đỉnh của đa giác
#         int n = sc.nextInt();

#         // Nhập giá trị gán cho mỗi đỉnh
#         int[] values = new int[n];
#         for (int i = 0; i < n; i++) {
#             values[i] = sc.nextInt();
#         }

#         // Gọi hàm tính toán
#         int result = minScoreTriangulation(values);

#         // In kết quả
#         System.out.println(result);

#         sc.close();
#     }

#     // Hàm chính tính kết quả
#     public static int minScoreTriangulation(int[] values) {
#         // Khởi tạo mảng dp
#         dp = new int[values.length][values.length];

#         // Gọi đệ quy cho toàn bộ đa giác (từ đỉnh 0 đến đỉnh n-1)
#         return helper(values, 0, values.length - 1);
#     }

#     // Hàm đệ quy tính chi phí nhỏ nhất khi chia đa giác từ đỉnh i đến j
#     public static int helper(int[] a, int i, int j) {
#         // Nếu đoạn [i..j] có ít hơn 3 đỉnh thì không tạo được tam giác
#         if (j - i < 2) {
#             return 0;
#         }

#         // Nếu đã tính trước đó thì trả về luôn
#         if (dp[i][j] != 0) {
#             return dp[i][j];
#         }

#         int min = Integer.MAX_VALUE; // Khởi tạo giá trị min rất lớn

#         // Thử tất cả các cách chọn đỉnh k ở giữa i và j để tạo tam giác (i, k, j)
#         for (int k = i + 1; k < j; k++) {
#             // Chi phí tạo tam giác (i, k, j) = tích của 3 đỉnh
#             // + chi phí chia phần bên trái (i..k)
#             // + chi phí chia phần bên phải (k..j)
#             int cost = a[i] * a[k] * a[j] + helper(a, i, k) + helper(a, k, j);

#             // Cập nhật giá trị nhỏ nhất
#             min = Math.min(min, cost);
#         }

#         // Lưu kết quả vào dp để lần sau dùng lại
#         return dp[i][j] = min;
#     }
# }

# // Ok mình
# // giải thích
# // rõ ràng bài**1039.
# // Minimum Score
# // Triangulation of Polygon**
# // cho bạn nhé👇

# // ---

# // ###

# // Đề bài (LeetCode 1039)

# // * Bạn có một **đa giác lồi** với `n` đỉnh.
# // * Mỗi đỉnh i có gán một số `values[i]`.
# // * Ta cần **chia đa giác thành nhiều tam giác** bằng cách kẻ các

# // đường chéo (không cắt nhau).

# // 👉 **Điểm số của một tam giác** = tích 3 số ở 3 đỉnh tam giác đó.
# // 👉 **Điểm số của một phép phân chia đa giác** = tổng điểm số của tất cả tam
# // giác tạo ra.

# // Nhiệm vụ: tìm **điểm số nhỏ nhất có thể** khi phân chia đa giác.

# // ---

# // ### Ví dụ 1

# // ```
# // Input: values = [1,2,3]
# // ```

# // * Đây là 1 tam giác rồi, không thể chia nhỏ hơn.
# // * Điểm số = 1×2×3 = 6.
# // ✅ Output: 6

# // ---

# // ### Ví dụ 2

# // ```
# // Input: values = [3,7,4,5]
# // ```

# // * Đây là

# // tứ giác (4 cạnh). Có 2 cách chia thành tam giác:

# // 1. Cắt từ đỉnh 0 → 2: tạo (3,7,4) và (3,4,5)

# // * Điểm = 3×7×4 + 3×4×5 = 84 + 60 = 144

# // 2. Cắt từ đỉnh 1 → 3: tạo (7,4,5) và (7,5,3)

# // * Điểm = 7×4×5 + 7×5×3 = 140 + 105 = 245

# // 👉 Chọn cách 1 → kết quả = 144

# // ✅ Output: 144

# // ---

# // ### Nhận xét

# // * Bài toán yêu cầu **tìm cách chia đa giác tối ưu** để tổng điểm nhỏ nhất.
# // * Đây là bài toán **quy hoạch

# // động (Dynamic Programming)** cổ điển, tương tự như "Matrix Chain
# // Multiplication".

# // ---

# // Bạn có muốn mình giải thích luôn **thuật toán DP và cách triển

# // khai code (Java hoặc Python)** không?
# // Rồi 👍 mình giải thích **thuật toán trực tiếp từ code Java của bạn**:

# // ---

# // ### Ý tưởng trong code

# // * Dùng **quy hoạch động (DP + đệ quy có nhớ - memoization)** để tính chi phí
# // nhỏ nhất khi chia một đa giác thành các tam giác.

# // ---

# // ### Phân tích từng phần

# // 1. **Khai báo mảng nhớ:**

# // ```java
# // int [][]dp;
# // ```

# // * `dp[i][j]` lưu **chi phí nhỏ nhất** để chia đoạn đa giác từ đỉnh `i` đến
# // đỉnh `j`.
# // * Tránh tính lại nhiều lần.

# // ---

# // 2. **Hàm chính:**

# // ```java

# // public int minScoreTriangulation(int[] values) {
# // dp = new int[values.length][values.length];
# // return helper(values, 0, values.length-1);
# // }```

# // *

# // Bắt đầu
# // từ toàn
# // bộ đa giác:
# // đỉnh đầu`0`→
# // đỉnh cuối`n-1`.*
# // Gọi hàm
# // đệ quy`helper`.

# // ---

# // 3.**Điều kiện dừng:**

# // ```java if(j-i<2)
# // {
# // return 0;
# // }```

# // *
# // Nếu đoạn`(i..j)`
# // có ít hơn 3 đỉnh→
# // không tạo
# // được tam giác→
# // chi phí = `0`.

# // ---

# // 4. **Tránh tính lại:**

# // ```java if(dp[i][j]!=0)return dp[i][j];```

# // *
# // Nếu đã tính`dp[i][j]`
# // rồi thì
# // trả về

# // ngay (memoization).

# // ---

# // 5. **Tính toán bằng cách chia nhỏ:**

# // ```java
# // int min = Integer.MAX_VALUE;
# // for(int k = i+1 ; k < j ; k++){
# // int cost = a[i]*a[k]*a[j] + helper(a,i,k)+helper(a,k,j);
# // min = Math.min(min, cost);
# // }
# // ```

# // * Chọn một đỉnh trung gian `k` giữa `i` và `j`.

# // * Tam giác tạo ra: `(i, k, j)`.

# // * Chi phí:

# // * `a[i] * a[k] * a[j]`: chi phí tam giác hiện tại.
# // * `helper(a, i, k)`: chi phí chia đa giác bên trái `(i..k)`.
# // * `helper(a, k, j)`: chi phí chia đa giác bên phải `(k..j)`.

# // * Lấy **chi phí nhỏ nhất** trong tất cả lựa chọn `k`.

# // ---

# // 6. **Lưu kết quả và trả về:**

# // ```java
# // return dp[i][j] = min;
# // ```

# // * Lưu vào `dp[i][j]` để lần sau dùng lại.
# // * Trả về kết quả.

# // ---

# // ### Kết quả

# // * `helper(values, 0, n-1)` chính là chi phí nhỏ nhất để chia toàn bộ đa giác.

# // ---

# // 👉 Tóm gọn:
# // Thuật toán thử tất cả cách chọn tam giác `(i, k, j)` để chia đa giác thành
# // hai phần nhỏ hơn, tính chi phí, rồi chọn cách **rẻ nhất**. Nhờ có `dp`, mỗi
# // đoạn `(i, j)` chỉ tính một lần.

# // ---

# // Bạn có muốn mình viết lại thuật toán này dưới dạng **bottom-up (vòng lặp)**
# // thay vì **đệ quy + memoization** để dễ thấy quy hoạch động hơn không?
