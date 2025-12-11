# # //  Count Covered Buildings(11/12/2025)
# # //  Dưới đây là **giải thích rõ ràng – dễ hiểu** cho đề bài **“Count Covered Buildings”** (LeetCode 3681).
# # //  Dưới đây là**giải thích thuật toán cực dễ hiểu**,kèm theo**code Java có thêm chú thích+hàm main dùng Scanner**đúng nhu cầu của bạn.
# Dưới đây là **giải thích thuật toán cực dễ hiểu** + **code Python đã thêm chú thích từng dòng**.

# ---

# # 🧠 **GIẢI THÍCH THUẬT TOÁN Count Covered Buildings**

# Bạn có một lưới kích thước **n × n**.
# Mỗi building có tọa độ **(row, col)**.

# Một building được gọi là **covered** nếu:

# ### 1️⃣ Trên *cùng cột col*, nó **nằm giữa** các building khác:

# * Có building phía **trên** → `minRowIndices[col] < row`
# * Có building phía **dưới** → `maxRowIndices[col] > row`

# ### 2️⃣ Trên *cùng hàng row*, nó **nằm giữa** các building khác:

# * Có building bên **trái** → `minColIndices[row] < col`
# * Có building bên **phải** → `maxColIndices[row] > col`

# ---

# ## 🧠 Ý tưởng chính

# ### Bước 1: Duyệt toàn bộ buildings để tìm:

# | Mảng                 | Ý nghĩa                    |
# | -------------------- | -------------------------- |
# | `minRowIndices[col]` | row nhỏ nhất trên cột col  |
# | `maxRowIndices[col]` | row lớn nhất trên cột col  |
# | `minColIndices[row]` | col nhỏ nhất trên hàng row |
# | `maxColIndices[row]` | col lớn nhất trên hàng row |

# ### Bước 2: Kiểm tra từng building có nằm *giữa* trên cả hàng và cột không.

# Nếu có → tính là **covered**.

# ---

# # ✅ CODE ĐÃ THÊM CHÚ THÍCH RÕ RÀNG

# ```python

from typing import List
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        
        # Khởi tạo min = n+1 và max = 0 để dễ cập nhật
        minRowIndices = [n + 1] * (n + 1)  # row nhỏ nhất trên mỗi col
        maxRowIndices = [0] * (n + 1)      # row lớn nhất trên mỗi col
        minColIndices = [n + 1] * (n + 1)  # col nhỏ nhất trên mỗi row
        maxColIndices = [0] * (n + 1)      # col lớn nhất trên mỗi row

        # Bước 1: Tìm min/max theo hàng và cột
        for building in buildings:
            row = building[0]
            col = building[1]

            # cập nhật row min/max của cột col
            if row < minRowIndices[col]:
                minRowIndices[col] = row
            if row > maxRowIndices[col]:
                maxRowIndices[col] = row

            # cập nhật col min/max của hàng row
            if col < minColIndices[row]:
                minColIndices[row] = col
            if col > maxColIndices[row]:
                maxColIndices[row] = col

        count = 0

        # Bước 2: kiểm tra từng building có nằm giữa hay không
        for building in buildings:
            row = building[0]
            col = building[1]

            # Điều kiện covered:
            # row phải nằm giữa min-max của cột col
            # col phải nằm giữa min-max của hàng row
            if (minRowIndices[col] < row and
                maxRowIndices[col] > row and
                minColIndices[row] < col and
                maxColIndices[row] > col):
                count += 1

        return count
# ```

# ---

# # 🎯 TÓM TẮT NGẮN GỌN

# Một building (row, col) được xem là **covered** nếu:

# ✔ Có building ở bên trên và bên dưới nó (cùng cột)
# ✔ Có building ở bên trái và bên phải nó (cùng hàng)

# Thế là đủ.

# ---

# Nếu bạn muốn, mình có thể vẽ hình minh họa trực quan để bạn hiểu hơn.

# //  ---

# //  #🧠**Giải thích thuật toán Count Covered Buildings**

# //  Bạn có**n×n grid**(lưới kích thước n).Mỗi building có tọa độ**(x,y)**.

# //  Ta cần đếm số tòa nhà**bị bao phủ**—tức là nằm**không phải biên**theo**hàng và cột**,cụ thể:

# //  Một building tại**(x,y)**bị xem là*covered*nếu:

# //  *Trên**cùng hàng y**:Có building**nhỏ hơn x**(minRow[y])và building**lớn hơn x**(maxRow[y])

# //  *Trên**cùng cột x**:Có building**nhỏ hơn y**(minCol[x])và building**lớn hơn y**(maxCol[x])

# //  Nói cách khác:👉Building nằm*giữa*một cụm hàng và*giữa*một cụm cột.

# //  ---

# //  #💡**Ý tưởng thuật toán**

# //  ###1 ️⃣Giai đoạn 1:Tìm min–max của mỗi hàng và mỗi cột

# //  *`minRow[y]`:x nhỏ nhất trên hàng y*`maxRow[y]`:x lớn nhất trên hàng y*`minCol[x]`:y nhỏ nhất trên cột x*`maxCol[x]`:y lớn nhất trên cột x

# //  →Giúp biết một building có nằm**giữa**(không phải biên)hay không.

# //  ---

# //  ###2 ️⃣Giai đoạn 2:Duyệt từng building và kiểm tra

# //  Một building(x,y)được coi là covered nếu:

# //  ```minRow[y]<x<maxRow[y]minCol[x]<y<maxCol[x]```

# //  Nếu đúng→tăng kết quả.

# //  ---

# //  #✅**Java Code có chú thích+hàm main dùng Scanner**

# //  ```java

# import java.util.*;

# public class b115 {
#     static Scanner sc = new Scanner(System.in);
#     static int MAX = 1000000007;

#     public static void main(String[] args) {
#         int n = sc.nextInt();

#         // số lượng building
#         int m = sc.nextInt();

#         int[][] buildings = new int[m][2];

#         // nhập từng building (x, y)
#         for (int i = 0; i < m; i++) {
#             buildings[i][0] = sc.nextInt();
#             buildings[i][1] = sc.nextInt();
#         }

#         // Gọi hàm
#         int result = countCoveredBuildings(n, buildings);

#         // In kết quả
#         System.out.println(result);

#         sc.close();
#     }

#     public static int countCoveredBuildings(int n, int[][] buildings) {

#         // maxRow[y] = giá trị x lớn nhất trên hàng y
#         // minRow[y] = giá trị x nhỏ nhất trên hàng y
#         int[] maxRow = new int[n + 1];
#         int[] minRow = new int[n + 1];

#         // maxCol[x] = giá trị y lớn nhất trên cột x
#         // minCol[x] = giá trị y nhỏ nhất trên cột x
#         int[] maxCol = new int[n + 1];
#         int[] minCol = new int[n + 1];

#         // Khởi tạo minRow, minCol = giá trị lớn để dễ lấy min
#         Arrays.fill(minRow, n + 1);
#         Arrays.fill(minCol, n + 1);

#         // --- Bước 1: Xây bảng min/max cho từng hàng và cột ---
#         for (int[] p : buildings) {
#             int x = p[0];
#             int y = p[1];

#             // cập nhật hàng y
#             maxRow[y] = Math.max(maxRow[y], x);
#             minRow[y] = Math.min(minRow[y], x);

#             // cập nhật cột x
#             maxCol[x] = Math.max(maxCol[x], y);
#             minCol[x] = Math.min(minCol[x], y);
#         }

#         // --- Bước 2: Kiểm tra từng building có nằm giữa hay không ---
#         int res = 0;
#         for (int[] p : buildings) {
#             int x = p[0];
#             int y = p[1];

#             // kiểm tra xem (x, y) có nằm giữa trên hàng và cột hay không
#             if (x > minRow[y] && x < maxRow[y] &&
#                     y > minCol[x] && y < maxCol[x]) {
#                 res++;
#             }
#         }

#         return res;
#     }
# }

# // bị bao
# // phủ không|
# // Xem nó
# // có nằm
# // giữa min–
# // max của
# // hàng và
# // cột hay không||
# // Tìm min/
# // max mỗi hàng/cột|
# // Duyệt tất
# // cả buildings||
# // Kiểm tra
# // từng building|4
# // điều kiện minRow<x<
# // maxRow AND minCol<y<maxCol|

# // ---

# // Nếu bạn muốn,
# // mình có
# // thể bỏ thêm:

# // ✅
# // Hình minh
# // họa dễ hiểu✅
# // Phân tích
# // độ phức

# // tạp O(n)
# // ✅ Đề bài gốc bằng tiếng Việt

# // Bạn muốn không?

# // ---

# // # 🏙️ **Giải thích đề bài “Count Covered Buildings”**

# // Bạn được cho:

# // * Một **mảng heights** (chiều cao của các tòa nhà)
# // * Đứng **từ vị trí đầu tiên (index 0)**, bạn nhìn sang **bên phải**
# // * Một tòa nhà được gọi là **bị che khuất (covered)** nếu:

# // > Có **một tòa nhà cao hơn hoặc bằng** nó **ở bên trái**, nằm vào đúng hướng
# // nhìn từ trái sang phải.

# // Nói cách khác:

# // 👉 Một tòa nhà **không được nhìn thấy** nếu phía trước nó (bên trái) có một
# // tòa nhà **cao hơn hoặc bằng**.

# // Nhiệm vụ:
# // **Đếm số tòa nhà bị che khuất**.

# // ---

# // # 📌 Ví dụ minh họa

# // ## **Ví dụ 1**

# // ```
# // heights = [3, 1, 5, 2, 4]
# // ```

# // Ta nhìn từ trái → phải:

# // * 3: luôn nhìn thấy → không che
# // * 1: bị che bởi 3 (3 ≥ 1)
# // * 5: cao nhất → nhìn thấy
# // * 2: bị che bởi 5 (5 ≥ 2)
# // * 4: bị che bởi 5 (5 ≥ 4)

# // → Số tòa nhà bị che = **3** (1, 2, 4)

# // ---

# // ## **Ví dụ 2**

# // ```
# // heights = [1, 2, 3, 4]
# // ```

# // * Mỗi tòa nhà đều cao hơn tòa trước → không bị che.

# // → Kết quả = **0**

# // ---

# // ## **Ví dụ 3**

# // ```
# // heights = [4, 3, 2, 1]
# // ```

# // Mọi tòa nhà sau đều thấp hơn 4:

# // → Tất cả bị che.

# // → Kết quả = **3**

# // ---

# // # 🧠 Cách giải đề bài

# // Duyệt từ trái sang phải:

# // * Theo dõi **max_height_so_far** (chiều cao lớn nhất đã thấy)
# // * Nếu `heights[i] <= max_height_so_far` → tòa nhà này bị che
# // * Ngược lại → update `max_height_so_far = heights[i]`

# // ---

# // # ✔️ Code mẫu (dễ hiểu)

# // ```python
# // def countCoveredBuildings(heights):
# // maxHeight = heights[0]
# // covered = 0

# // for h in heights[1:]:
# // if h <= maxHeight:
# // covered += 1
# // else:
# // maxHeight = h

# // return covered
# // ```

# // ---

# // # 🎯 Tóm tắt

# // Một tòa nhà **bị che** nếu có tòa nhà nào đó bên trái của nó có chiều cao
# // **lớn hơn hoặc bằng**.

# // Mục tiêu: **đếm bao nhiêu tòa bị che**.

# // ---

# // Nếu bạn muốn, mình có thể giải thích thêm:

# // ✅ Vì sao chỉ cần theo dõi max?
# // ✅ Hình vẽ minh họa giúp dễ hiểu
# // ✅ Giải bằng stack (nâng cao)

# // Bạn muốn phần nào?
