# # // // //  Count Negative Numbers in a Sorted Matrix(28/12/2025)
# # // // //  **Giải thích đề bài: “Count Negative Numbers in a Sorted Matrix”**
# # // // Mình giải thích **thuật toán trong đoạn code Java của bạn** từng bước, đúng tư duy LeetCode 👇
# # // Dưới đây là**phiên bản đầy đủ có`main`dùng`Scanner`**và**chú thích chi tiết từng dòng**đúng theo yêu cầu của bạn👇(Mình giữ nguyên thuật toán Binary Search của bạn)
# Mình sẽ **giải thích thuật toán trước**, sau đó **chú thích trực tiếp vào code Python** của bạn để bạn dễ nhớ khi đi thi / phỏng vấn 👇

# ---

# ## 🧠 Giải thích thuật toán (O(n + m))

# ### 📌 Bài toán nhắc lại

# * Ma trận `grid` đã được **sắp xếp giảm dần theo hàng và cột**
# * Cần đếm **số phần tử âm**

# ---

# ## 🎯 Ý tưởng chính

# Ta **không duyệt toàn bộ ma trận**.

# 👉 Bắt đầu từ **góc trên bên phải** của ma trận:

# * Vị trí `(0, m-1)`

# ### Vì sao chọn góc này?

# * Sang **trái** → giá trị **tăng**
# * Đi **xuống** → giá trị **giảm**

# Điều này giúp ta **loại bỏ cả một hàng hoặc một cột** mỗi bước.

# ---

# ## 🔄 Chi tiết từng bước

# Giả sử đang đứng tại `grid[i][j]`

# ### 🔹 Trường hợp 1: `grid[i][j] < 0`

# * Vì **cột đã giảm dần**, nên:

#   ```
#   grid[i][j], grid[i+1][j], ..., grid[n-1][j]
#   ```

#   👉 **Tất cả đều là số âm**

# ➡️ Ta đếm luôn:

# ```
# n - i
# ```

# ➡️ Sau đó **dịch sang trái** (`j -= 1`) để xét cột tiếp theo

# ---

# ### 🔹 Trường hợp 2: `grid[i][j] >= 0`

# * Vì **hàng đã giảm dần**, nên:

#   * Bên trái sẽ còn lớn hơn
#   * Số âm **chỉ có thể nằm bên dưới**

# ➡️ Ta **đi xuống** (`i += 1`)

# ---

# ## ⏱️ Độ phức tạp

# * Mỗi bước **giảm một cột hoặc tăng một hàng**
# * Tổng số bước tối đa:

# ```
# n + m
# ```

# 👉 **O(n + m)** (tối ưu nhất)

# ---

# ## ✅ Code Python + chú thích chi tiết

# ```python
from typing import List
def countNegatives(self, grid: List[List[int]]) -> int:
    
    n = len(grid)        # số hàng
    m = len(grid[0])     # số cột

    i = 0               # con trỏ hàng (bắt đầu từ hàng đầu tiên)
    j = m - 1           # con trỏ cột (bắt đầu từ cột cuối cùng)

    count = 0           # biến đếm số phần tử âm

    # Duyệt khi còn nằm trong ma trận
    while i < n and j >= 0:

        # Nếu phần tử hiện tại là số âm
        if grid[i][j] < 0:
            # Tất cả phần tử từ hàng i đến hàng n-1
            # trong cùng cột j đều là số âm
            count += n - i

            # Dịch sang trái để xét cột tiếp theo
            j -= 1

        else:
            # Nếu không âm, số âm chỉ có thể nằm phía dưới
            i += 1


## 📌 Ví dụ minh họa nhanh


# 4  3  2 -1  ← bắt đầu tại đây
# 3  2  1 -1
# 1  1 -1 -2
# -1 -1 -2 -3
# ```

# * Gặp `-1` → đếm luôn cả cột
# * Gặp số dương → đi xuống
# * Không duyệt lại phần đã xét

# ---

# ## 🏁 Tóm tắt để nhớ nhanh

# * Bắt đầu **góc phải trên**
# * Số âm → đếm cả cột
# * Không âm → đi xuống
# * Độ phức tạp: **O(n + m)** ⭐⭐⭐

# ---

# Nếu bạn muốn, mình có thể:

# * So sánh **Binary Search vs O(n+m)**
# * Vẽ **sơ đồ di chuyển i, j**
# * Chuyển sang **Java theo đúng logic này**

# 👉 Bạn muốn tiếp theo phần nào?

# // ---

# // ##✅Code Java hoàn chỉnh+chú thích

# // ```java

# import java.util.*;

# public class b131 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int rows = sc.nextInt();
#         int cols = sc.nextInt();

#         // Khai báo ma trận
#         int[][] grid = new int[rows][cols];

#         // Nhập các phần tử của ma trận
#         for (int i = 0; i < rows; i++) {
#             for (int j = 0; j < cols; j++) {
#                 grid[i][j] = sc.nextInt();
#             }
#         }

#         // Gọi hàm đếm số âm
#         int result = countNegatives(grid);

#         // In kết quả
#         System.out.println(result);

#         sc.close();
#     }

#     public static int countNegatives(int[][] grid) {
#         int rows = grid.length; // số hàng
#         int cols = grid[0].length; // số cột
#         int count = 0; // biến đếm số âm

#         // Duyệt từng hàng của ma trận
#         for (int i = 0; i < rows; i++) {

#             int left = 0;
#             int right = cols - 1;

#             // firstNeg lưu vị trí số âm đầu tiên trong hàng
#             // mặc định = cols nghĩa là "không có số âm"
#             int firstNeg = cols;

#             // Binary Search trong hàng i
#             while (left <= right) {
#                 int mid = left + (right - left) / 2;

#                 // Nếu phần tử tại mid là số âm
#                 if (grid[i][mid] < 0) {
#                     firstNeg = mid; // cập nhật vị trí số âm đầu tiên
#                     right = mid - 1; // tiếp tục tìm bên trái
#                 }
#                 // Nếu phần tử không âm
#                 else {
#                     left = mid + 1; // tìm bên phải
#                 }
#             }

#             // Số phần tử âm trong hàng i
#             count += cols - firstNeg;
#         }

#         return count;
#     }

# }

# // input để test

# // ```4 4 4 3 2-1 3 2 1-1 1 1-1-2-1-1-2-3```

# // ###Output

# // ```8```

# // ---

# // ##🧠
# // Tóm tắt

# // thuật toán (để nhớ khi thi/phỏng vấn)

# // * Mỗi hàng **đã sắp xếp giảm dần**
# // * Dùng **Binary Search** tìm **số âm đầu tiên**
# // * Số âm trong hàng = `cols - firstNeg`
# // * Tổng thời gian: **O(m log n)**

# // ---

# // Nếu bạn muốn:

# // * Viết lại **chỉ dùng while (không for)**
# // * Tối ưu xuống **O(m + n)**
# // * Hoặc mình giải thích lại **theo kiểu dễ nhớ để đi thi**

# // 👉 Cứ nói, mình làm tiếp cho bạn 👍

# // ---

# // ## 🎯 Mục tiêu của thuật toán

# // Đếm **tổng số phần tử âm** trong ma trận `grid` đã được:

# // * Sắp xếp **giảm dần theo hàng**
# // * Sắp xếp **giảm dần theo cột**

# // ---

# // ## 🧠 Ý tưởng chính

# // 👉 **Mỗi hàng đã được sắp xếp giảm dần**, nên:

# // * Các số **không âm (≥ 0)** nằm bên trái
# // * Các số **âm (< 0)** nằm liên tiếp bên phải

# // ➡️ Với **mỗi hàng**, ta chỉ cần:

# // > Tìm **vị trí đầu tiên xuất hiện số âm**
# // > Sau đó:
# // > `số âm = tổng số cột - vị trí đó`

# // Để tìm nhanh vị trí này → dùng **Binary Search**

# // ---

# // ## 📌 Phân tích từng phần code

# // ### 1️⃣ Lấy số hàng và số cột

# // ```java
# // int rows = grid.length;
# // int cols = grid[0].length;
# // int count = 0;
# // ```

# // * `rows`: số hàng của ma trận
# // * `cols`: số cột
# // * `count`: biến đếm tổng số phần tử âm

# // ---

# // ### 2️⃣ Duyệt từng hàng

# // ```java
# // for (int i = 0; i < rows; i++) {
# // ```

# // 👉 Xử lý **từng hàng độc lập**, vì mỗi hàng đã được sắp xếp.

# // ---

# // ### 3️⃣ Khởi tạo Binary Search

# // ```java
# // int left = 0, right = cols - 1;
# // int firstNeg = cols; // mặc định: không có số âm
# // ```

# // * `left`, `right`: biên tìm kiếm
# // * `firstNeg = cols`:

# // * Nếu **không tìm thấy số âm**, thì:

# // ```
# // cols - firstNeg = 0
# // ```

# // ---

# // ### 4️⃣ Binary Search tìm số âm đầu tiên

# // ```java
# // while (left <= right) {
# // int mid = left + (right - left) / 2;
# // ```

# // ➡️ Tính `mid` an toàn (tránh overflow)

# // ---

# // #### 🔹 Trường hợp 1: gặp số âm

# // ```java
# // if (grid[i][mid] < 0) {
# // firstNeg = mid;
# // right = mid - 1;
# // }
# // ```

# // * `mid` là số âm → **có thể là số âm đầu tiên**
# // * Lưu lại vị trí `firstNeg = mid`
# // * Tiếp tục tìm **bên trái** để xem còn số âm nào sớm hơn không

# // ---

# // #### 🔹 Trường hợp 2: số không âm

# // ```java
# // else {
# // left = mid + 1;
# // }
# // ```

# // * `grid[i][mid] >= 0`
# // * Vì hàng giảm dần → **số âm chỉ có thể nằm bên phải**
# // * Dịch `left` sang phải

# // ---

# // ### 5️⃣ Sau khi kết thúc Binary Search

# // ```java
# // count += cols - firstNeg;
# // ```

# // * `firstNeg`: vị trí số âm đầu tiên
# // * Số phần tử âm trong hàng:

# // ```
# // cols - firstNeg
# // ```

# // 📌 Ví dụ:

# // ```
# // [4, 3, 1, -1, -2]
# // ↑
# // firstNeg = 3
# // → số âm = 5 - 3 = 2
# // ```

# // ---

# // ### 6️⃣ Trả về kết quả

# // ```java
# // return count;
# // ```

# // ---

# // ## ⏱️ Độ phức tạp

# // * Binary Search mỗi hàng: `O(log n)`
# // * Tổng:

# // ```
# // O(m log n)
# // ```

# // (với `m` hàng, `n` cột)

# // 👉 Tối ưu hơn so với `O(m × n)`

# // ---

# // ## ✅ Tóm tắt ngắn gọn

# // * Duyệt từng hàng
# // * Dùng **Binary Search** tìm số âm đầu tiên
# // * Cộng `cols - firstNeg` vào kết quả
# // * Thuật toán **đúng – tối ưu – chuẩn phỏng vấn**

# // ---

# // Nếu bạn muốn, mình có thể:

# // * Giải thích lại **bằng hình minh họa**
# // * So sánh với cách **O(m + n)** (đi từ góc phải trên)
# // * Viết lại theo phong cách bạn hay dùng (while loop, tối ưu hơn)

# // 👉 Bạn muốn đi tiếp theo hướng nào?

# // // ---

# // // ### 📌 Nội dung đề bài

# // // Bạn được cho **một ma trận 2D** (m x n) gồm các số nguyên.

# // // Ma trận này có **tính chất đã được sắp xếp**:

# // // * **Mỗi hàng** được sắp xếp **giảm dần từ trái sang phải**
# // // * **Mỗi cột** được sắp xếp **giảm dần từ trên xuống dưới**

# // // 👉 **Yêu cầu:**
# // // Đếm **tổng số phần tử âm** (số < 0) trong ma trận.

# // // ---

# // // ### 🔍 Ví dụ

# // // ```
# // // Input:
# // // grid = [
# // // [ 4, 3, 2, -1],
# // // [ 3, 2, 1, -1],
# // // [ 1, 1, -1, -2],
# // // [-1, -1, -2, -3]
# // // ]

# // // Output: 8
# // // ```

# // // **Giải thích:**
# // // Các số âm là:

# // // ```
# // // -1, -1,
# // // -1, -2,
# // // -1, -1, -2, -3
# // // ```

# // // 👉 Tổng cộng **8 số âm**

# // // ---

# // // ### 🧠 Ý nghĩa của việc “ma trận đã sắp xếp”

# // // Do mỗi hàng và mỗi cột đều **giảm dần**, nên:

# // // * Khi bạn gặp **một số âm**, thì **tất cả các số bên phải nó trong cùng
# // hàng cũng là số âm**
# // // * Bạn **không cần duyệt từng phần tử**

# // // 👉 Đây là điểm quan trọng để **tối ưu thuật toán**

# // // ---

# // // ### 💡 Cách hiểu đơn giản

# // // 1. Duyệt từng **hàng**
# // // 2. Trong mỗi hàng:

# // // * Tìm **vị trí đầu tiên xuất hiện số âm**
# // // * Số phần tử âm = `số cột - vị trí đó`
# // // 3. Cộng dồn lại cho tất cả các hàng

# // // ---

# // // ### ⏱️ Độ phức tạp

# // // * Cách ngây thơ: `O(m × n)` (duyệt hết)
# // // * Cách tối ưu (nhờ sắp xếp):
# // // 👉 `O(m + n)` hoặc `O(m log n)` tùy cách làm

# // // ---

# // // ### 🎯 Tóm tắt ngắn gọn

# // // * Đề bài yêu cầu **đếm số âm**
# // // * Ma trận đã được **sắp xếp giảm dần**
# // // * Có thể tận dụng tính chất này để **không duyệt toàn bộ ma trận**

# // // Nếu bạn muốn, mình có thể:

# // // * Giải bằng **Java / C++ / Python**
# // // * Giải theo **tư duy phỏng vấn LeetCode**
# // // * Vẽ sơ đồ minh họa từng bước 👌
