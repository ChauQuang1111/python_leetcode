# # Maximum Side Length of a Square with Sum Less than or Equal to Threshold* (19/01/2026) **từng bước, dễ hiểu** nhé 👇
# # Ok, mình **viết lại đầy đủ code Java**, có:
# Mình sẽ **giải thích thuật toán + thêm chú thích trực tiếp vào code Python của bạn**, đúng theo tư duy LeetCode, ngắn gọn – rõ ràng – dễ nhớ 👍

# ---

# ## 🧠 Ý tưởng thuật toán (tóm tắt trước)

# 1️⃣ Dùng **Prefix Sum 2D** để tính tổng mọi hình vuông trong **O(1)**
# 2️⃣ Với mỗi cạnh `k` (từ nhỏ → lớn), kiểm tra:

# * Có **ít nhất 1 hình vuông k×k** có tổng ≤ `threshold` không?
#   3️⃣ Nếu có → cập nhật đáp án
#   4️⃣ Nếu không → **break** (vì k lớn hơn chắc chắn cũng fail)

# ---

# ## 📌 Giải thích chi tiết + chú thích trong code

# ```python
from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        # m: số hàng, n: số cột
        m, n = len(mat), len(mat[0])

        # =========================
        # 1. BUILD PREFIX SUM 2D
        # =========================
        # pre[i][j] = tổng các phần tử trong hình chữ nhật
        # từ (0,0) đến (i-1, j-1)
        pre = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            row_sum = 0  # tổng dồn của hàng i
            for j in range(n):
                row_sum += mat[i][j]
                # Công thức prefix sum 2D
                pre[i + 1][j + 1] = pre[i][j + 1] + row_sum

        # =========================
        # 2. KIỂM TRA TỒN TẠI HÌNH VUÔNG k x k
        # =========================
        def square_exists(k: int) -> bool:
            # Duyệt mọi hình vuông k×k
            # (i, j) là góc phải dưới trong mảng prefix
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    # Tính tổng hình vuông k×k bằng prefix sum
                    s = (
                        pre[i][j]                  # bottom-right
                        - pre[i - k][j]            # top
                        - pre[i][j - k]            # left
                        + pre[i - k][j - k]        # top-left
                    )
                    # Nếu có ít nhất 1 hình vuông thỏa mãn
                    if s <= threshold:
                        return True
            return False

        # =========================
        # 3. TĂNG DẦN ĐỘ DÀI CẠNH
        # =========================
        ans = 0

        # Thử cạnh từ 1 → min(m, n)
        for k in range(1, min(m, n) + 1):
            if square_exists(k):
                ans = k  # cập nhật kết quả nếu tồn tại
            else:
                break    # k lớn hơn chắc chắn cũng không hợp lệ

        return ans
# ```

# ---

# ## 📐 Công thức quan trọng (cần thuộc)

# Tổng hình vuông k×k:

# ```
# sum =
# pre[br]
# - pre[top]
# - pre[left]
# + pre[topLeft]
# ```

# ➡️ Tính **O(1)** cho mỗi hình vuông

# ---

## ⏱️ Độ phức tạp

# | Phần           | Độ phức tạp      |
# | -------------- | ---------------- |
# | Prefix sum     | O(mn)            |
# | Kiểm tra mỗi k | O(mn)            |
# | Tổng           | O(mn × min(m,n)) |

# 👉 Đủ nhanh cho ràng buộc LeetCode

# ---

# ## ✅ Vì sao code này “đúng chuẩn”?

# * Prefix sum 2D → chuẩn bài
# * Kiểm tra **tồn tại** (early return)
# * `break` khi không còn khả năng mở rộng
# * Code **rõ ràng – dễ debug – dễ học**

# ---

# Nếu bạn muốn:

# * 🚀 Nâng cấp sang **Binary Search (nhanh hơn)**
# * 🧠 So sánh **Java vs Python version**
# * ✍️ Viết lại theo **tư duy thi ICPC**

# 👉 nói mình làm tiếp nhé 👍

# # * ✅ `main` dùng **Scanner**
# # * ✅ **Chú thích chi tiết từng bước**
# # * ✅ Giữ **đúng thuật toán bạn đã hỏi**
# # * ✅ Dễ học – dễ nhớ khi đi thi / phỏng vấn

# # ---

# # ## ✅ Code hoàn chỉnh (có `main`, Scanner, chú thích)

# # ```java
# import java.util.*;
# public class b152 {
    
# }

# class Solution {

#     // Hàm chính giải bài toán
#     public int maxSideLength(int[][] mat, int threshold) {
#         int rows = mat.length;
#         int cols = mat[0].length;

#         // =========================
#         // A. XÂY DỰNG PREFIX SUM 2D
#         // =========================

#         // Cộng dồn theo hàng
#         // Sau bước này: mat[i][j] = tổng từ (i,0) -> (i,j)
#         for (int i = 0; i < rows; i++) {
#             for (int j = 1; j < cols; j++) {
#                 mat[i][j] += mat[i][j - 1];
#             }
#         }

#         // Cộng dồn theo cột
#         // Sau bước này: mat[i][j] = tổng từ (0,0) -> (i,j)
#         for (int i = 1; i < rows; i++) {
#             for (int j = 0; j < cols; j++) {
#                 mat[i][j] += mat[i - 1][j];
#             }
#         }

#         int maxDiagLen = 0; // cạnh lớn nhất tìm được

#         // =========================
#         // B. DUYỆT CÁC HÌNH VUÔNG
#         // =========================

#         // (i, j) là góc phải dưới của hình vuông
#         for (int i = 0; i < rows; i++) {
#             for (int j = 0; j < cols; j++) {

#                 // Chỉ thử cạnh lớn hơn kết quả hiện tại
#                 for (int diagLen = maxDiagLen + 1;
#                      i + 1 - diagLen >= 0 && j + 1 - diagLen >= 0;
#                      diagLen++) {

#                     // Tọa độ góc trên bên trái của hình vuông
#                     int iPrev = i - diagLen;
#                     int jPrev = j - diagLen;

#                     // Lấy các giá trị prefix cần thiết
#                     int topLeft = (iPrev >= 0 && jPrev >= 0) ? mat[iPrev][jPrev] : 0;
#                     int top = (iPrev >= 0) ? mat[iPrev][j] : 0;
#                     int left = (jPrev >= 0) ? mat[i][jPrev] : 0;

#                     // Công thức tính tổng hình vuông bằng prefix sum
#                     int sum = mat[i][j] + topLeft - top - left;

#                     // Kiểm tra điều kiện
#                     if (sum <= threshold) {
#                         maxDiagLen = diagLen; // cập nhật kết quả
#                     } else {
#                         // Cạnh càng lớn thì tổng càng lớn -> dừng sớm
#                         break;
#                     }
#                 }
#             }
#         }

#         return maxDiagLen;
#     }

#     // =========================
#     // HÀM MAIN - NHẬP LIỆU & CHẠY
#     // =========================
#     public static void main(String[] args) {
#         Scanner sc = new Scanner(System.in);

#         // Nhập số hàng và số cột
#         int rows = sc.nextInt();
#         int cols = sc.nextInt();

#         // Khởi tạo ma trận
#         int[][] mat = new int[rows][cols];

#         // Nhập các phần tử của ma trận
#         for (int i = 0; i < rows; i++) {
#             for (int j = 0; j < cols; j++) {
#                 mat[i][j] = sc.nextInt();
#             }
#         }

#         // Nhập threshold
#         int threshold = sc.nextInt();

#         // Gọi hàm xử lý
#         Solution solution = new Solution();
#         int result = solution.maxSideLength(mat, threshold);

#         // In kết quả
#         System.out.println(result);

#         sc.close();
#     }
# }
# # ```

# # ---

# # ## 🧠 Cách nhớ nhanh khi đi thi

# # * `mat[i][j]` sau prefix = **tổng từ (0,0) → (i,j)**
# # * `(i,j)` là **góc phải dưới**
# # * Công thức vàng:

# # ```
# # sum = br - top - left + topLeft
# # ```

# # * Duyệt cạnh từ `max + 1`
# # * Tổng > threshold → `break`

# # ---

# # Nếu bạn muốn:

# # * 🔹 Viết **phiên bản Binary Search**
# # * 🔹 So sánh **2 cách giải**
# # * 🔹 Rút gọn code cho thi ICPC / LeetCode

# # 👉 nói mình làm tiếp cho 👌

# # Mình sẽ **giải thích thuật toán đúng theo code bạn đưa**, từng khối A – B, và chỉ ra **tư duy đằng sau**, để bạn nhìn code là hiểu ngay (đúng kiểu luyện LeetCode / phỏng vấn).

# # ---

# # # 🎯 Mục tiêu của thuật toán

# # Tìm **độ dài cạnh lớn nhất `k`** của **hình vuông k×k** sao cho **tổng các phần tử ≤ threshold**.

# # ---

# # # A️⃣ Phần A – Biến `mat` thành **prefix sum 2D**

# # ```java
# # for (int i = 0 ; i < rows ; i++) {
# #     for (int j = 1 ; j < cols ; j++) {
# #         mat[i][j] += mat[i][j-1];
# #     }
# # }
# # ```

# # ### 👉 Việc này làm gì?

# # * Cộng **theo hàng**
# # * Sau vòng này:

# #   ```
# #   mat[i][j] = tổng từ (i,0) → (i,j)
# #   ```

# # ---

# # ```java
# # for (int i = 1 ; i < rows ; i++) {
# #     for (int j = 0 ; j < cols ; j++) {
# #         mat[i][j] += mat[i-1][j];
# #     }
# # }
# # ```

# # ### 👉 Việc này làm gì?

# # * Cộng tiếp **theo cột**
# # * Sau vòng này:

# #   ```
# #   mat[i][j] = tổng từ (0,0) → (i,j)
# #   ```

# # 📌 **Kết luận phần A**
# # `mat[i][j]` bây giờ chính là **prefix sum 2D**

# # ---

# # # B️⃣ Phần B – Duyệt hình vuông & tính tổng O(1)

# # ## 🔹 Ý tưởng duyệt

# # ```java
# # for (int i = 0 ; i < rows ; i++) {
# #     for (int j = 0 ; j < cols ; j++) {
# # ```

# # 👉 `(i, j)` được xem là **góc dưới bên phải** của hình vuông.

# # ---

# # ## 🔹 Duyệt độ dài cạnh hình vuông

# # ```java
# # for (int diagLen = maxDiagLen + 1 ;
# #      i + 1 - diagLen >= 0 && j + 1 - diagLen >= 0 ;
# #      diagLen++)
# # ```

# # ### Vì sao bắt đầu từ `maxDiagLen + 1`?

# # 👉 Vì:

# # * Các cạnh **≤ maxDiagLen** đã được kiểm tra rồi
# # * Chỉ cần thử **lớn hơn**

# # ➡️ Đây là **tối ưu quan trọng**

# # ---

# # ## 🔹 Xác định góc trên trái

# # ```java
# # int iPrev = i - diagLen;
# # int jPrev = j - diagLen;
# # ```

# # Hình vuông:

# # ```
# # (iPrev+1, jPrev+1) --------
# # |                           |
# # |                           |
# # |                           |
# # ---------------------- (i, j)
# # ```

# # ---

# # ## 🔹 Lấy các giá trị prefix cần thiết

# # ```java
# # int topLeft = iPrev >= 0 && jPrev >= 0 ? mat[iPrev][jPrev] : 0;
# # int left = jPrev >= 0 ? mat[i][jPrev] : 0;
# # int top = iPrev >= 0 ? mat[iPrev][j] : 0;
# # ```

# # 👉 Đây chính là 4 điểm để áp dụng công thức prefix sum.

# # ---

# # ## 🔹 Công thức tính tổng hình vuông

# # ```java
# # int sum = mat[i][j] + topLeft - top - left;
# # ```

# # 📐 Công thức chuẩn:

# # ```
# # sum =
# # prefix(bottomRight)
# # - prefix(top)
# # - prefix(left)
# # + prefix(topLeft)
# # ```

# # ⏱️ **O(1)** cho mỗi hình vuông

# # ---

# # ## 🔹 Kiểm tra điều kiện

# # ```java
# # if (sum <= threshold) {
# #     maxDiagLen = diagLen;
# # } else {
# #     break;
# # }
# # ```

# # ### Vì sao `break`?

# # * `diagLen` càng lớn → tổng càng lớn
# # * Đã vượt threshold thì **không cần thử tiếp**

# # ➡️ Đây là **tối ưu thứ 2**

# # ---

# # # 🧠 Tổng hợp tư duy thuật toán

# # 1️⃣ Dùng **prefix sum 2D** để tính tổng nhanh
# # 2️⃣ Mỗi ô `(i, j)` làm **góc phải dưới**
# # 3️⃣ Chỉ thử cạnh **lớn hơn kết quả hiện tại**
# # 4️⃣ Khi tổng vượt threshold → **dừng sớm**

# # ---

# # # ⏱️ Độ phức tạp

# # | Thành phần       | Độ phức tạp                         |
# # | ---------------- | ----------------------------------- |
# # | Prefix sum       | `O(mn)`                             |
# # | Duyệt hình vuông | ~ `O(mn * k)`                       |
# # | Thực tế          | **Nhanh hơn brute force rất nhiều** |

# # ---

# # # ✅ Vì sao code này “hay”?

# # * Không dùng extra array → tiết kiệm bộ nhớ
# # * Break sớm → chạy nhanh
# # * Duyệt từ cạnh lớn → ít kiểm tra thừa

# # ---

# # Nếu bạn muốn:

# # * 🔍 Mình **vẽ hình minh họa prefix sum**
# # * 🔁 So sánh với **Binary Search version**
# # * ✍️ Viết lại code cho **dễ nhớ khi thi**

# # 👉 cứ nói, mình làm tiếp cho đúng gu học của bạn 👌


# # ## 1️⃣ Đề bài nói gì?

# # Bạn được cho:

# # * Một **ma trận số nguyên** `mat` kích thước `m x n`
# # * Một số nguyên `threshold`

# # 👉 Nhiệm vụ:
# # **Tìm cạnh lớn nhất `k` của một hình vuông (k × k)** sao cho **tổng các phần tử trong hình vuông đó ≤ threshold**.

# # 📌 Lưu ý:

# # * Hình vuông có thể nằm **ở bất kỳ vị trí nào** trong ma trận
# # * Nếu không có hình vuông nào thỏa mãn → trả về `0`

# # ---

# # ## 2️⃣ Hiểu bằng ví dụ đơn giản

# # Ví dụ:

# # ```
# # mat = [
# #   [1, 1, 3, 2],
# #   [1, 1, 3, 2],
# #   [1, 1, 3, 2]
# # ]
# # threshold = 4
# # ```

# # ### Xét các hình vuông:

# # #### 🔹 Hình vuông 1×1

# # * Mỗi ô ≤ 4 → OK

# # #### 🔹 Hình vuông 2×2

# # Ví dụ:

# # ```
# # 1 1
# # 1 1
# # ```

# # 👉 Tổng = 4 ≤ threshold → OK

# # #### 🔹 Hình vuông 3×3

# # ```
# # 1 1 3
# # 1 1 3
# # 1 1 3
# # ```

# # 👉 Tổng = 15 > threshold → ❌

# # ✅ **Kết luận:** cạnh lớn nhất là **2**

# # ---

# # ## 3️⃣ Bản chất bài toán

# # 👉 Ta cần:

# # * Thử **mọi hình vuông**
# # * So sánh **tổng các phần tử**
# # * Lấy **cạnh lớn nhất hợp lệ**

# # ❌ Cách ngây thơ (brute force):

# # * Duyệt từng hình vuông
# # * Tính tổng từng cái
# #   → **Quá chậm** (`O(n^4)`)

# # ✅ Cách thông minh:

# # * Dùng **Prefix Sum (ma trận cộng dồn)**
# # * * **Binary Search** hoặc duyệt cạnh

# # ---

# # ## 4️⃣ Ý tưởng cốt lõi (rất quan trọng)

# # ### 🔹 Prefix Sum 2D là gì?

# # Tạo mảng `sum[i][j]`:

# # > Tổng các phần tử từ `(0,0)` đến `(i-1,j-1)`

# # Công thức:

# # ```
# # sum[i][j] =
# # sum[i-1][j] + sum[i][j-1]
# # - sum[i-1][j-1] + mat[i-1][j-1]
# # ```

# # ### 🔹 Tính tổng hình vuông nhanh O(1)

# # Tổng hình vuông cạnh `k`, góc trái trên `(r, c)`:

# # ```
# # total =
# # sum[r+k][c+k]
# # - sum[r][c+k]
# # - sum[r+k][c]
# # + sum[r][c]
# # ```

# # 🚀 Không cần cộng từng ô nữa!

# # ---

# # ## 5️⃣ Chiến lược giải bài

# # ### Cách thường dùng nhất:

# # 1️⃣ Tạo prefix sum
# # 2️⃣ Duyệt độ dài cạnh `k` từ **1 → min(m, n)**
# # 3️⃣ Với mỗi `k`, duyệt mọi vị trí đặt hình vuông
# # 4️⃣ Nếu **có ít nhất 1 hình vuông tổng ≤ threshold**
# # → cập nhật kết quả

# # ⏱️ Độ phức tạp: `O(n^3)` → **đủ nhanh**

# # ---

# # ## 6️⃣ Tóm tắt cực ngắn (để nhớ)

# # * Bài toán: **tìm hình vuông lớn nhất có tổng ≤ threshold**
# # * Công cụ chính: **Prefix Sum 2D**
# # * Mấu chốt:
# #   👉 Tính tổng hình vuông **O(1)**
# #   👉 Tránh cộng lại từ đầu

# # ---

# # Nếu bạn muốn:

# # * ✅ Mình **giải bằng Java / Python**
# # * ✅ Giải theo **tư duy thi LeetCode**
# # * ✅ So sánh **Binary Search vs brute force**

# # 👉 cứ nói nhé, mình làm tiếp cho bạn 💪
