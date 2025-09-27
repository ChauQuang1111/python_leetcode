# // 812. Largest Triangle Area(27/09/2025)

from itertools import combinations

class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        # Duyệt qua tất cả bộ 3 điểm nằm trên convex hull
        # Tính diện tích bằng cross product (getVector) / 2
        return max(
            abs(getVector(a, b, c)) / 2
            for a, b, c in combinations(getBoundary(points), 3)
        )

def getBoundary(points):
    # Đưa các điểm vào tuple và sắp xếp theo (x, y)
    points = [(a, b) for a, b in points]
    points.sort(key=lambda x: (x[0], x[1]))

    upper = []  # hull phía trên
    lower = []  # hull phía dưới

    for point in points:
        # Xây hull dưới (lower hull)
        # Nếu 2 điểm cuối và điểm mới tạo thành góc quay phải thì loại bỏ
        while len(lower) >= 2 and getVector(lower[-2], lower[-1], point) < 0:
            lower.pop()
        lower.append(point)

        # Xây hull trên (upper hull)
        # Nếu 2 điểm cuối và điểm mới tạo thành góc quay trái thì loại bỏ
        while len(upper) >= 2 and getVector(upper[-2], upper[-1], point) > 0:
            upper.pop()
        upper.append(point)

    # Trả về tập hợp các điểm nằm trên convex hull (gộp upper và lower)
    return list(set(upper + lower))

def getVector(a, b, c):
    # Cross product để xác định hướng quay và diện tích
    # (bx - ax)(cy - ay) - (by - ay)(cx - ax)
    return (b[0] - a[0]) * (b[1] - c[1]) - (b[1] - a[1]) * (b[0] - c[0])
# ```

# ---

# 📌 Giải thích ngắn gọn:

# * `getBoundary(points)` → tìm **convex hull** bằng Monotone Chain.
# * `getVector(a, b, c)` → cross product: xác định hướng quay hoặc tính diện tích.
# * `largestTriangleArea` → duyệt qua mọi tam giác tạo bởi các điểm hull, tính diện tích, chọn lớn nhất.

# Bạn có muốn mình viết thêm một **ví dụ input/output** để thấy cách chạy thực tế không?

# Ok, đoạn code bạn đưa là một cách **tối ưu hơn** so với duyệt toàn bộ 3 điểm (O(n³)), vì nó chỉ xét các điểm nằm trên **bao lồi (convex hull)** – theo định lý hình học thì **tam giác lớn nhất** luôn được tạo thành từ các điểm thuộc convex hull.

# ---

# ### 🔎 Giải thích từng phần

# #### 1. `getBoundary(points)` → Tìm convex hull

# * Đầu vào: danh sách điểm `points`.
# * Ý tưởng: dùng thuật toán **Monotone Chain** (Andrew’s algorithm) để tìm bao lồi (convex hull).
# * Các bước:

#   1. Sắp xếp điểm theo tọa độ `(x, y)`.
#   2. Xây dựng **lower hull**: duyệt từ trái sang phải, loại bỏ những điểm làm đường gấp khúc quay **phải**.
#   3. Xây dựng **upper hull**: duyệt từ trái sang phải, loại bỏ những điểm làm đường gấp khúc quay **trái**.
#   4. Gộp cả hai để lấy tập điểm tạo thành convex hull.

# 👉 Kết quả trả về chỉ gồm các điểm nằm trên biên ngoài.

# ---

# #### 2. `getVector(a, b, c)`

# * Đây là **tích có hướng (cross product)** của vector **AB** và **AC**:

# [
# \text{cross}(AB, AC) = (b_x - a_x)(c_y - a_y) - (b_y - a_y)(c_x - a_x)
# ]

# Trong code viết lại thành dạng tương đương.

# * Nếu > 0 → quay trái.
# * Nếu < 0 → quay phải.
# * Nếu = 0 → thẳng hàng.

# 👉 Được dùng để xác định hướng khi xây hull, và cũng để tính **diện tích tam giác**.

# ---

# #### 3. Trong `largestTriangleArea`

# * `getBoundary(points)` lọc ra convex hull.
# * `combinations(..., 3)` chọn tất cả bộ 3 điểm trên hull.
# * `abs(getVector(a, b, c)) / 2` = diện tích tam giác (từ cross product).
# * Lấy **max** → ra diện tích lớn nhất.

# ---

# ### 📌 Thuật toán đầy đủ

# 1. Tìm **convex hull** bằng Monotone Chain.
# 2. Chỉ xét tam giác từ các điểm hull (ít hơn nhiều so với n³).
# 3. Dùng công thức diện tích từ cross product.
# 4. Trả về giá trị diện tích lớn nhất.

# ---

# ### 📊 Độ phức tạp

# * Xây convex hull: **O(n log n)** (do sắp xếp).
# * Duyệt bộ 3 điểm trên hull: **O(h³)**, với h là số điểm trên hull (thường nhỏ hơn nhiều so với n).

# # ---

# 👉 Đây là cách làm tối ưu hơn brute force.

# Bạn có muốn mình **thêm chú thích trực tiếp vào code** để dễ đọc hơn không?

# import java.util.Scanner;

# public class b49 {
#     public static void main(String[] args) {
#         Scanner sc = new Scanner(System.in);

#         // Nhập số lượng điểm
#         int n = sc.nextInt();
#         int[][] points = new int[n][2];

#         // Nhập toạ độ các điểm
#         for (int i = 0; i < n; i++) {
#             points[i][0] = sc.nextInt(); // hoành độ x
#             points[i][1] = sc.nextInt(); // tung độ y
#         }

#         // Gọi hàm tính diện tích lớn nhất

#         double res = largestTriangleArea(points);

#         // In kết quả
#         System.out.println(res);

#         sc.close();
#     }

#     public static double largestTriangleArea(int[][] points) {
#         int n = points.length;
#         double area = 0;

#         // Duyệt tất cả các bộ 3 điểm (i, j, k)
#         for (int i = 0; i < n - 2; i++) {
#             for (int j = i + 1; j < n - 1; j++) {
#                 for (int k = j + 1; k < n; k++) {
#                     // Tính diện tích tam giác tạo bởi 3 điểm
#                     double a = max(points[i], points[j], points[k]);

#                     // Cập nhật diện tích lớn nhất
#                     if (a > area) {
#                         area = a;
#                     }
#                 }
#             }
#         }
#         return area; // Trả về diện tích lớn nhất
#     }

#     // Hàm tính diện tích tam giác từ 3 điểm
#     public static double max(int p1[], int p2[], int p3[]) {
#         // Công thức diện tích tam giác từ toạ độ
#         double area = 0.5 * Math.abs(
#                 p1[0] * (p2[1] - p3[1]) +
#                         p2[0] * (p3[1] - p1[1]) +
#                         p3[0] * (p1[1] - p2[1]));
#         return area;
#     }
# }

# // Ok mình giải thích đề bài **LeetCode 812. Largest Triangle Area** nhé 👍

# // ---

# // ### 📌 Đề bài:

# // Cho một danh sách các điểm trong mặt phẳng 2D, hãy tìm **diện tích lớn nhất
# // của tam giác** có thể được tạo thành từ **3 điểm bất kỳ** trong danh sách.

# // ---

# // ### 📝 Input:

# // * `points[i] = [xi, yi]` là tọa độ của điểm thứ i.
# // * Số lượng điểm: `3 <= points.length <= 50`
# // * Tọa độ: `-50 <= xi, yi <= 50`

# // ---

# // ### 📝 Output:

# // * Trả về diện tích lớn nhất có thể của một tam giác được tạo bởi 3 điểm.
# // * Đáp án sai số cho phép trong `10^-5`.

# // ---

# // ### 🚀 Ví dụ:

# // **Input:**

# // ```
# // points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# // ```

# // **Output:**

# // ```
# // 2.0
# // ```

# // **Giải thích:**

# // * Các tam giác có thể tạo ra từ 3 điểm bất kỳ.
# // * Tam giác `(0,0), (0,2), (2,0)` có diện tích lớn nhất = `2.0`.

# // ---

# // ### 🔑 Ý tưởng giải:

# // 1. Duyệt **mọi bộ 3 điểm** trong mảng `points`.
# // (vì tối đa 50 điểm → số bộ ba là `C(50,3) = 19600` → chấp nhận được).

# // 2. Dùng **công thức tọa độ để tính diện tích tam giác**:
# // Nếu tam giác có 3 đỉnh `(x1,y1), (x2,y2), (x3,y3)` thì diện tích là:

# // [
# // S = \frac{1}{2} \times |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)|
# // ]

# // 3. Tính tất cả diện tích, lấy **max**.

# // ---

# // 👉 Nói gọn:

# // * Thử tất cả bộ ba điểm.
# // * Dùng công thức diện tích tam giác từ tọa độ.
# // * Trả về giá trị lớn nhất.

# // ---

# // Bạn có muốn mình viết luôn code **Java** và **Python** cho bài này kèm chú
# // thích không?
# // Ok, mình giải thích chi tiết thuật toán trong code của bạn:

# // ---

# // ### 📌 Ý tưởng của bài toán

# // * Bạn có một tập hợp các điểm 2D.
# // * Nhiệm vụ: **Tìm diện tích lớn nhất của một tam giác** có thể tạo từ 3 điểm
# // bất kỳ.
# // * Công thức tính diện tích tam giác từ 3 điểm ((x1,y1), (x2,y2), (x3,y3)):

# // [
# // S = \frac{1}{2} \times |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)|
# // ]

# // ---

# // ### 📌 Giải thích code

# // ```java
# // class Solution {
# // // Khối static: chạy trước khi chương trình bắt đầu
# // // Ở đây chỉ test thử hàm largestTriangleArea với 500 lần gọi
# // static {
# // Solution s = new Solution();
# // for (int i = 0; i < 500; i++)
# // s.largestTriangleArea(new int[][]{{0,0},{0,0},{0,0}});
# // }

# // public double largestTriangleArea(int[][] points) {
# // int n = points.length;
# // double area = 0;

# // // Duyệt qua tất cả các bộ 3 điểm (i, j, k)
# // for (int i = 0; i < n - 2; i++) {
# // for (int j = i + 1; j < n - 1; j++) {
# // for (int k = j + 1; k < n; k++) {
# // // Tính diện tích tam giác tạo bởi points[i], points[j], points[k]
# // double a = max(points[i], points[j], points[k]);

# // // Nếu diện tích lớn hơn max hiện tại thì cập nhật
# // if (a > area) {
# // area = a;
# // }
# // }
# // }
# // }
# // return area; // trả về diện tích lớn nhất
# // }

# // // Hàm tính diện tích tam giác từ 3 điểm
# // public double max(int p1[], int p2[], int p3[]) {
# // double area = 0.5 * Math.abs(
# // p1[0] * (p2[1] - p3[1]) +
# // p2[0] * (p3[1] - p1[1]) +
# // p3[0] * (p1[1] - p2[1])
# // );
# // return area;
# // }
# // }
# // ```

# // ---

# // ### 📌 Các bước thuật toán

# // 1. **Khởi tạo `area = 0`** (diện tích lớn nhất ban đầu).
# // 2. **Duyệt 3 vòng lồng nhau** để chọn mọi bộ ba điểm `(i, j, k)`.

# // * Số bộ ba = (C(n,3) = \frac{n(n-1)(n-2)}{6}).
# // 3. **Tính diện tích tam giác** bằng công thức toạ độ trong hàm `max()`.
# // 4. **So sánh và cập nhật diện tích lớn nhất** vào biến `area`.
# // 5. Trả về `area`.

# // ---

# // ### 📌 Độ phức tạp

# // * **Thời gian**: (O(n^3)) vì duyệt hết các bộ ba điểm. Với `n ≤ 50` (theo đề
# // LeetCode 812) thì chấp nhận được.
# // * **Không gian**: (O(1)), chỉ dùng biến lưu diện tích.

# // ---

# // 👉 Tóm lại: Code của bạn đang **brute force duyệt tất cả các tam giác có thể
# // tạo ra từ tập điểm, tính diện tích và chọn lớn nhất**.

# // ---

# // Bạn có muốn mình viết **phiên bản tối ưu hơn** dùng **cross product vector**
# // (để gọn code và tính toán nhanh hơn) không?
