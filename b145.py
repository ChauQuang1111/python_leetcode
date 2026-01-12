# # // // Minimum Time Visiting All Points(12/01/2026)
# # // // Dưới đây là **giải thích đề bài “Minimum Time Visiting All Points”** (LeetCode 1266) **một cách dễ hiểu** 👇
# # // // Mình sẽ **giải thích thuật toán của đoạn code này từng bước, đúng theo tư duy bài “Minimum Time Visiting All Points”**, và chỉ ra **ý nghĩa của từng dòng** 👇
# # // Dưới đây là**phiên bản hoàn chỉnh của chương trình Java**,có:
# Dưới đây là **giải thích thuật toán + phiên bản code Python có chú thích đầy đủ**, đúng với bài **Minimum Time Visiting All Points** 👇

# ---

# ## 1. Ý tưởng thuật toán (hiểu nhanh – đúng bản chất)

# Giữa **2 điểm liên tiếp**:

# ```
# (x1, y1) → (x2, y2)
# ```

# * Ta tính:

#   ```python
#   dx = |x2 - x1|
#   dy = |y2 - y1|
#   ```
# * Vì **được phép đi chéo**, mỗi bước chéo giảm được **cả dx và dy**
# * Thời gian ít nhất cần để đi là:

# ```
# max(dx, dy)
# ```

# 👉 Tổng thời gian = **cộng thời gian của từng đoạn**

# ---

# ## 2. Giải thích từng dòng code

# ### Code gốc

# ```python
# class Solution:
#     def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
#         ans = 0
#         for i in range(1,len(points)):
#             ans += max(abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1]))
#         return ans
# ```

# ---

# ## 3. Code có chú thích chi tiết

# ```python
from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # ans: tổng thời gian nhỏ nhất
        ans = 0

        # Duyệt các điểm từ điểm thứ 2 trở đi
        for i in range(1, len(points)):
            # Khoảng cách theo trục x giữa 2 điểm liên tiếp
            dx = abs(points[i][0] - points[i - 1][0])

            # Khoảng cách theo trục y giữa 2 điểm liên tiếp
            dy = abs(points[i][1] - points[i - 1][1])

            # Vì được đi chéo:
            # thời gian đi từ điểm i-1 đến i là max(dx, dy)
            ans += max(dx, dy)

        # Trả về tổng thời gian
        return ans
# ```

# ---

# ## 4. Ví dụ minh họa

# ### Input

# ```python
# points = [[1,1], [3,4], [-1,0]]
# ```

### Tính tay:

# * (1,1) → (3,4):

#   ```
#   dx = 2, dy = 3 → time = 3
#   ```
# * (3,4) → (-1,0):

#   ```
#   dx = 4, dy = 4 → time = 4
#   ```

# ### Output

# ```
# 3 + 4 = 7
# ```

# ---

# ## 5. Vì sao không dùng `dx + dy`?

# * `dx + dy` là **Manhattan distance** (chỉ đi ngang/dọc)
# * Bài này **cho đi chéo**
# * Đi chéo giúp tiết kiệm thời gian → dùng:

# ```
# max(dx, dy)
# ```

# ---

## 6. Độ phức tạp

# * ⏱ **Time:** `O(n)`
# * 💾 **Space:** `O(1)`

# ---

# ## 7. Ghi nhớ nhanh khi thi

# > **Bài cho đi chéo → nghĩ ngay đến `max(dx, dy)`**

# ---

# Nếu bạn muốn:

# * 🔹 So sánh với **Manhattan vs Chebyshev distance**
# * 🔹 Viết lại theo phong cách **phỏng vấn**
# * 🔹 Thêm test case + debug

# 👉 Cứ nói, mình giải tiếp cho bạn 👍

# // *✅`main`dùng**Scanner***✅**Chú thích chi tiết từng phần***✅Giữ nguyên**thuật toán đúng–tối ưu***✅Viết**dễ đọc cho học/thi**

# // ---

# // ##Code hoàn chỉnh+chú thích

# // ```java
# import java.util.*;

# public class b146 {

#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int n = sc.nextInt();
#         int[][] points = new int[n][2];

#         for (int i = 0; i < n; i++) {
#             points[i][0] = sc.nextInt();
#             points[i][1] = sc.nextInt();
#         }

#         int result = minTimeToVisitAllPoints(points);
#         System.out.println(result);

#         sc.close();
#     }

#     public static int minTimeToVisitAllPoints(int[][] points) {
#         int totalTime = 0;
#         int[] p = points[0];

#         for (int i = 1; i < points.length; i++) {
#             int[] c = points[i];
#             totalTime += min(p, c);
#             p = c;
#         }

#         return totalTime;
#     }

#     public static int min(int[] p1, int[] p2) {
#         int dx = Math.abs(p2[0] - p1[0]);
#         int dy = Math.abs(p2[1] - p1[1]);
#         return Math.max(dx, dy);
#     }
# }

# // ---

# // ##
# // Tóm tắt

# // tư duy (để nhớ nhanh khi thi)

# // * Giữa 2 điểm:

# // ```
# // dx = |x2 - x1|
# // dy = |y2 - y1|
# // // time = max(dx, dy)
# // // ```
# // // * Cộng tất cả các đoạn
# // // * Vì **được đi chéo**, không dùng `dx + dy`

# // // ---

# // // Nếu bạn muốn:

# // // * 🔹 Viết lại theo **OOP rõ hơn**
# // // * 🔹 Viết **theo phong cách thi HSG / ĐH**
# // // * 🔹 So sánh với **Manhattan Distance**
# // // * 🔹 Vẽ hình minh họa đường đi

# // 👉 Cứ nói, mình làm tiếp cho bạn 👍

# // ---

# // ## 1. Ý tưởng cốt lõi của thuật toán

# // Khi đi từ điểm

# // ```
# // p1(x1, y1) → p2(x2, y2)
# // ```

# // * Ta có:

# // ```
# // dx = |x2 - x1|
# // dy = |y2 - y1|
# // ```
# // * Vì **được phép đi chéo**, mỗi bước chéo giảm **cả dx và dy**
# // * Thời gian tối thiểu để đi là:

# // ```
# // max(dx, dy)
# // ```

# // 👉 Thuật toán:

# // * Duyệt các điểm **theo thứ tự**
# // * Tính thời gian tối thiểu cho **mỗi cặp điểm liên tiếp**
# // * Cộng lại

# // ---

# // ## 2. Giải thích hàm `minTimeToVisitAllPoints`

# // ```java
# // public int minTimeToVisitAllPoints(int[][] points) {
# // int min = 0;
# // int[] p = points[0];
# // ```

# // ### 🔹 Ý nghĩa:

# // * `min`: tổng thời gian nhỏ nhất
# // * `p`: điểm hiện tại (bắt đầu từ điểm đầu tiên)

# // ---

# // ```java
# // for (int i = 1; i < points.length; i++) {
# // int[] c = points[i];
# // ```

# // * Duyệt từ **điểm thứ 2 trở đi**
# // * `c`: điểm tiếp theo cần đi tới

# // ---

# // ```java
# // min = min + min(p, c);
# // p = c;
# // }
# // ```

# // * Tính **thời gian tối thiểu** để đi từ `p → c`
# // * Cộng vào tổng
# // * Cập nhật điểm hiện tại

# // ---

# // ```java
# // return min;
# // ```

# // * Trả về tổng thời gian

# // ---

# // ## 3. Giải thích hàm `min(int[] p1, int[] p2)`

# // Hàm này tính **thời gian tối thiểu đi từ p1 đến p2**

# // ---

# // ```java
# // int dx = Math.abs(p2[0] - p1[0]);
# // int dy = Math.abs(p2[1] - p1[1]);
# // ```

# // * `dx`: số bước cần đi theo trục x
# // * `dy`: số bước cần đi theo trục y

# // ---

# // ### 🔹 Trường hợp 1: `dx == dy`

# // ```java
# // if (dx == dy) {
# // min = dx;
# // }
# // ```

# // * Có thể **đi chéo hoàn toàn**
# // * Mỗi bước chéo giảm cả x và y
# // * Thời gian = `dx` (hoặc `dy`)

# // Ví dụ:

# // ```
# // (1,1) → (4,4)
# // dx = dy = 3 → 3 giây
# // ```

# // ---

# // ### 🔹 Trường hợp 2: `dx != dy`

# // ```java
# // else {
# // int d = Math.abs(dx - dy);
# // return d + Math.min(dx, dy);
# // }
# // ```

# // #### Phân tích:

# // * `Math.min(dx, dy)`:

# // * Số bước **đi chéo tối đa**
# // * `d = |dx - dy|`:

# // * Số bước **đi thẳng còn lại**

# // ➡️ Tổng thời gian:

# // ```
# // đi chéo + đi thẳng
# // = min(dx, dy) + |dx - dy|
# // = max(dx, dy)
# // ```

# // Ví dụ:

# // ```
# // dx = 5, dy = 2
# // đi chéo = 2
# // đi thẳng = 3
# // tổng = 5
# // ```

# // ---

# // ```java
# // return min;
# // ```

# // * Trả về kết quả cho trường hợp `dx == dy`

# // ---

# // ## 4. Rút gọn lại ý nghĩa thuật toán

# // Thực chất hàm `min()` đang tính:

# // ```java
# // max(dx, dy)
# // ```

# // Chỉ là viết **dài hơn để dễ hiểu logic đi chéo + đi thẳng**.

# // 👉 Có thể viết gọn thành:

# // ```java
# // public int min(int[] p1, int[] p2) {
# // int dx = Math.abs(p2[0] - p1[0]);
# // int dy = Math.abs(p2[1] - p1[1]);
# // return Math.max(dx, dy);
# // }
# // ```

# // ---

# // ## 5. Độ phức tạp

# // * **Thời gian:** `O(n)` (duyệt 1 lần qua các điểm)
# // * **Bộ nhớ:** `O(1)`

# // ---

# // ## 6. Tóm tắt dễ nhớ

# // * Mỗi đoạn giữa 2 điểm:

# // ```
# // time = max(|dx|, |dy|)
# // ```
# // * Cộng thời gian của tất cả đoạn
# // * Code của bạn **đúng và tối ưu**

# // ---

# // Nếu bạn muốn:

# // * Mình giải thích **bằng hình vẽ từng bước đi**
# // * Hoặc **chuyển tư duy này sang bài khác (Chebyshev distance)**
# // * Hoặc **giải thích kiểu “vì sao không phải dx + dy”**

# // 👉 Cứ nói nhé 👌

# // ---

# // ## 1. Nội dung đề bài (hiểu đơn giản)

# // * Bạn được cho một danh sách các **điểm trên mặt phẳng 2D**:
# // `points[i] = [xi, yi]`
# // * Bạn **bắt đầu từ điểm đầu tiên** `points[0]`
# // * Bạn phải **đi qua tất cả các điểm theo đúng thứ tự đã cho**
# // * Mỗi giây, bạn có thể:

# // * Đi **lên / xuống / trái / phải** (di chuyển 1 đơn vị)
# // * Hoặc đi **chéo** (vừa thay đổi x và y cùng lúc)

# // 👉 **Yêu cầu:**
# // Tính **thời gian ít nhất (số giây)** để đi qua tất cả các điểm.

# // ---

# // ## 2. Quy tắc di chuyển (rất quan trọng)

# // Trong **1 giây**, bạn có thể:

# // * `(x+1, y)`
# // * `(x-1, y)`
# // * `(x, y+1)`
# // * `(x, y-1)`
# // * `(x+1, y+1)`
# // * `(x+1, y-1)`
# // * `(x-1, y+1)`
# // * `(x-1, y-1)`

# // 👉 Nghĩa là: **được phép đi chéo**

# // ---

# // ## 3. Bài toán thực chất hỏi gì?

# // Với **2 điểm liên tiếp**:

# // ```
# // A(x1, y1) → B(x2, y2)
# // ```

# // Cần bao nhiêu giây để đi từ A đến B **nhanh nhất**?

# // ---

# // ## 4. Phân tích cách đi nhanh nhất

# // * Gọi:

# // ```
# // dx = |x2 - x1|
# // dy = |y2 - y1|
# // ```

# // ### ✨ Ý tưởng then chốt:

# // * Mỗi bước đi **chéo** giúp giảm **cả dx và dy**
# // * Bạn có thể đi chéo cho đến khi:

# // * Một trong hai tọa độ đã bằng nhau

# // 👉 Thời gian tối thiểu để đi từ A đến B là:

# // ```
# // max(dx, dy)
# // ```

# // ### Vì sao?

# // * Nếu dx > dy:

# // * Đi chéo dy lần → hết chênh lệch y
# // * Đi thẳng dx - dy lần → hết chênh lệch x
# // * Tổng = dx
# // * Tương tự nếu dy > dx

# // ---

# // ## 5. Cách tính cho toàn bộ đường đi

# // * Đi từng cặp điểm liên tiếp
# // * Cộng thời gian tối thiểu của từng đoạn

# // 📌 Công thức tổng:

# // ```
# // answer = Σ max(|xi - xi-1|, |yi - yi-1|)
# // ```

# // ---

# // ## 6. Ví dụ minh họa

# // ### Ví dụ:

# // ```
# // points = [[1,1],[3,4],[-1,0]]
# // ```

# // ### Đoạn 1: (1,1) → (3,4)

# // ```
# // dx = |3 - 1| = 2
# // dy = |4 - 1| = 3
# // time = max(2,3) = 3
# // ```

# // ### Đoạn 2: (3,4) → (-1,0)

# // ```
# // dx = |−1 − 3| = 4
# // dy = |0 − 4| = 4
# // time = max(4,4) = 4
# // ```

# // ### Tổng thời gian:

# // ```
# // 3 + 4 = 7
# // ```

# // ---

# // ## 7. Tóm tắt cực ngắn (để nhớ khi đi thi)

# // * Được đi **chéo**
# // * Mỗi đoạn giữa 2 điểm:

# // ```
# // time = max(|dx|, |dy|)
# // ```

# // * Cộng tất cả lại

# // ---

# // Nếu bạn muốn:

# // * Mình có thể **giải thích bằng hình minh họa**
# // * Hoặc **viết code Python / Java và giải thích từng dòng**
# // * Hoặc **so sánh với Manhattan distance**

# // 👉 Cứ nói nhé 👍
