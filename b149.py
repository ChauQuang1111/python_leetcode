# // Maximum Square Area by Removing Fences From a Field(16/01/2026)
# // Dưới đây là **giải thích đề bài “Maximum Square Area by Removing Fences From a Field”** bằng **tiếng Việt**, tập trung vào **hiểu đề** (chưa đi sâu code).
# Dưới đây là **giải thích thuật toán + phiên bản code Python có chú thích chi tiết**, đúng theo bài **LeetCode 2975 – Maximum Square Area by Removing Fences From a Field**.

# ---

# ## 1. Ý tưởng thuật toán (hiểu nhanh)

# Muốn tạo **hình vuông cạnh L** thì cần:

# * Có **khoảng cách L giữa 2 hàng rào ngang**
# * Đồng thời có **khoảng cách L giữa 2 hàng rào dọc**

# 👉 Bài toán trở thành:

# > Tìm **L lớn nhất** xuất hiện **ở cả hai chiều**
# > Diện tích = `L × L`

# ---

# ## 2. Chiến lược

# 1. **Thêm biên cánh đồng** (`1` và `m / n`) vào danh sách hàng rào
# 2. **Sắp xếp** các hàng rào
# 3. Sinh **tất cả khoảng cách theo chiều cao** → lưu vào `set`
# 4. Duyệt **chiều rộng từ lớn đến nhỏ**:

#    * Nếu width ∈ possible_heights → đây là cạnh vuông lớn nhất cho vị trí đó
#    * `break` sớm để tối ưu
# 5. Trả về diện tích lớn nhất

# ---

# ## 3. Code Python (có chú thích từng dòng)

from typing import List
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:

        mod = 10**9 + 7

        # Thêm biên trên/dưới của cánh đồng vào hàng rào ngang
        hFences.extend([1, m])

        # Thêm biên trái/phải của cánh đồng vào hàng rào dọc
        vFences.extend([1, n])

        # Sắp xếp vị trí các hàng rào
        hFences.sort()
        vFences.sort()

        # Lưu tất cả các khoảng cách có thể theo chiều cao
        possible_heights = set()

        # Sinh mọi khoảng cách giữa 2 hàng rào ngang
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                possible_heights.add(hFences[j] - hFences[i])

        max_area = 0

        # Duyệt khoảng cách theo chiều rộng
        for i in range(len(vFences)):

            # Duyệt từ khoảng lớn nhất về nhỏ nhất (tối ưu)
            for j in range(len(vFences) - 1, i, -1):
                width = vFences[j] - vFences[i]

                # Nếu width cũng xuất hiện ở chiều cao → tạo được hình vuông
                if width in possible_heights:
                    max_area = max(max_area, width * width)
                    break  # break vì không thể có width lớn hơn cho i này

        # Nếu không tạo được hình vuông
        return max_area % mod if max_area > 0 else -1


## 4. Vì sao thuật toán này hiệu quả?

### 🔹 Dùng `set`

# * Kiểm tra tồn tại trong **O(1)**

# ### 🔹 Duyệt width từ lớn → nhỏ

# * Gặp được cạnh lớn nhất sớm
# * `break` giúp giảm rất nhiều phép so sánh

# ---

# ## 5. Độ phức tạp

# * Thời gian:

#   * Sinh height: `O(H²)`
#   * Duyệt width: `O(V²)` (nhưng có break sớm)
# * Bộ nhớ:

#   * `O(H²)` cho `possible_heights`

# 👉 Phù hợp với giới hạn đề bài

# ---

# ## 6. Tóm tắt 1 câu (đi thi / phỏng vấn)

# > Lưu tất cả khoảng cách giữa hàng rào ngang, sau đó duyệt các khoảng cách dọc từ lớn đến nhỏ để tìm cạnh chung lớn nhất tạo được hình vuông.

# ---

# Nếu bạn muốn:

# * 🔥 Giải thích **bằng hình minh họa**
# * ⚡ Viết lại theo **tư duy editorial**
# * 🧠 So sánh **Java vs Python**
# * ❌ Chỉ ra **lỗi thường gặp khi làm bài này**

# cứ nói tiếp nhé 👍

# import java.util.*;

# public class b150 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         // Nhập kích thước cánh đồng
#         int m = sc.nextInt(); // chiều cao
#         int n = sc.nextInt(); // chiều rộng

#         // Nhập số hàng rào ngang
#         int h = sc.nextInt();
#         int[] hFences = new int[h];
#         for (int i = 0; i < h; i++) {
#             hFences[i] = sc.nextInt();
#         }

#         // Nhập số hàng rào dọc
#         int v = sc.nextInt();
#         int[] vFences = new int[v];
#         for (int i = 0; i < v; i++) {
#             vFences[i] = sc.nextInt();
#         }

#         int result = maximizeSquareArea(m, n, hFences, vFences);

#         // In kết quả
#         System.out.println(result);

#         sc.close();

#     }

#     // Hàm giải bài toán
#     public static int maximizeSquareArea(int m, int n, int[] hFences, int[] vFences) {

#         long mod = 1_000_000_007L;
#         long maxArea = 0;

#         // Số lượng hàng rào theo chiều dọc và ngang (thêm 2 biên)
#         int numY = hFences.length + 2;
#         int numX = vFences.length + 2;

#         // Mảng lưu tọa độ hàng rào + biên
#         int[] coordY = new int[numY];
#         int[] coordX = new int[numX];

#         // Biên của cánh đồng
#         coordY[0] = 1;
#         coordY[numY - 1] = m;
#         coordX[0] = 1;
#         coordX[numX - 1] = n;

#         // Gán các hàng rào vào mảng
#         for (int i = 0; i < hFences.length; i++) {
#             coordY[i + 1] = hFences[i];
#         }
#         for (int i = 0; i < vFences.length; i++) {
#             coordX[i + 1] = vFences[i];
#         }

#         // Sắp xếp tọa độ
#         Arrays.sort(coordY);
#         Arrays.sort(coordX);

#         // Lưu tất cả khoảng cách có thể theo chiều ngang
#         Set<Long> horizontalDiffs = new HashSet<>();

#         for (int i = 0; i < coordX.length; i++) {
#             for (int j = i + 1; j < coordX.length; j++) {
#                 long diff = coordX[j] - coordX[i];
#                 horizontalDiffs.add(diff);
#             }
#         }

#         // Duyệt tất cả khoảng cách theo chiều dọc
#         for (int i = 0; i < coordY.length; i++) {
#             for (int j = i + 1; j < coordY.length; j++) {
#                 long diff = coordY[j] - coordY[i];

#                 // Nếu diện tích nhỏ hơn kết quả hiện tại thì bỏ
#                 if (diff * diff <= maxArea)
#                     continue;

#                 // Nếu cùng độ dài tồn tại ở chiều ngang => tạo được hình vuông
#                 if (horizontalDiffs.contains(diff)) {
#                     maxArea = diff * diff;
#                 }
#             }
#         }

#         // Không tạo được hình vuông
#         if (maxArea == 0)
#             return -1;

#         return (int) (maxArea % mod);
#     }
    
# }


   

# // ---

# // ## 1. Bối cảnh đề bài

# // Bạn có **một cánh đồng hình chữ nhật**:

# // * Chiều **cao = h**
# // * Chiều **rộng = w**

# // Trong cánh đồng có:

# // * Các **hàng rào ngang** (song song cạnh đáy)
# // * Các **hàng rào dọc** (song song cạnh bên)

# // Những hàng rào này **chia cánh đồng thành nhiều ô nhỏ**.

# // Bạn **được phép tháo bỏ một số hàng rào** (không giới hạn số lượng) để **tạo ra một hình vuông lớn nhất có thể**.

# // ---

# // ## 2. Input (dữ liệu cho trước)

# // * `h`: chiều cao cánh đồng
# // * `w`: chiều rộng cánh đồng
# // * `horizontalFences`: mảng vị trí các hàng rào **ngang**
# // * `verticalFences`: mảng vị trí các hàng rào **dọc**

# // ⚠️ Lưu ý:

# // * Mép trên, dưới, trái, phải của cánh đồng **cũng được coi là hàng rào** (ở vị trí 0 và h / w).

# // ---

# // ## 3. Bạn cần làm gì?

# // 👉 **Tìm diện tích lớn nhất của một hình vuông** có thể tạo ra sau khi tháo hàng rào.

# // * Hình vuông phải **nằm hoàn toàn trong cánh đồng**
# // * Các cạnh song song với trục (không xoay)

# // Nếu không tạo được hình vuông → trả về `-1`.

# // ---

# // ## 4. Ý tưởng hiểu đề (rất quan trọng)

# // ### Bước 1: Xem các khoảng trống giữa các hàng rào

# // Ví dụ (chiều cao):

# // ```text
# // 0 ---- fence ---- fence ---- fence ---- h
# // ```

# // Khoảng cách giữa các fence tạo thành **các đoạn chiều cao có thể dùng**.

# // Tương tự cho chiều rộng.

# // ---

# // ### Bước 2: Vì là HÌNH VUÔNG

# // → **Cạnh hình vuông = min(chiều cao đoạn, chiều rộng đoạn)**

# // Nhưng để **lớn nhất**, ta cần:

# // > 🔥 **Tìm độ dài L lớn nhất sao cho:**
# // >
# // > * Có **một đoạn cao = L**
# // > * Có **một đoạn rộng = L**

# // ---

# // ## 5. Ví dụ minh họa

# // ### Ví dụ:

# // ```text
# // h = 5, w = 8
# // horizontalFences = [1, 2, 4]
# // verticalFences = [2, 4]
# // ```

# // #### Chiều cao:

# // Thêm 0 và 5 → `[0, 1, 2, 4, 5]`
# // Các khoảng:

# // * 1, 1, 2, 1 → **max = 2**

# // #### Chiều rộng:

# // Thêm 0 và 8 → `[0, 2, 4, 8]`
# // Các khoảng:

# // * 2, 2, 4 → **max = 4**

# // 👉 Cạnh hình vuông lớn nhất:

# // ```
# // L = min(2, 4) = 2
# // ```

# // 👉 Diện tích:

# // ```
# // 2 × 2 = 4
# // ```

# // ---

# // ## 6. Kết luận hiểu đề

# // ✔ Đề **KHÔNG yêu cầu** bạn chọn ô cụ thể
# // ✔ Chỉ cần quan tâm:

# // * **Khoảng trống lớn nhất theo chiều cao**
# // * **Khoảng trống lớn nhất theo chiều rộng**
# //   ✔ Lấy **min của hai giá trị đó**, rồi **bình phương lên**

# // ---

# // Nếu bạn muốn:

# // * 👉 Giải thích **bằng hình vẽ**
# // * 👉 Phân tích **tư duy thuật toán**
# // * 👉 Viết **code Java / Python / C++**
# // * 👉 So sánh **cách làm sai thường gặp**

# // nói mình biết nhé 👍
# // Mình sẽ **giải thích thuật toán trong đoạn code của bạn**, đi **từng bước đúng theo code**, đồng thời chỉ ra **ý tưởng cốt lõi + những điểm cần chú ý**.

# // ---

# // ## 1. Mục tiêu thuật toán

# // Bài toán yêu cầu:

# // > Tìm **diện tích hình vuông lớn nhất** có thể tạo ra bằng cách **bỏ hàng rào**, sao cho:

# // * Cạnh hình vuông song song trục
# // * Cạnh hình vuông xuất hiện **đồng thời ở chiều ngang và chiều dọc**

# // ➡️ Tức là cần tìm **một độ dài L**:

# // * L xuất hiện như **khoảng cách giữa 2 hàng rào dọc**
# // * L cũng xuất hiện như **khoảng cách giữa 2 hàng rào ngang**

# // Diện tích = `L × L`

# // ---

# // ## 2. Chuẩn bị dữ liệu (ý tưởng hình học)

# // ### 2.1. Thêm biên của cánh đồng

# // ```java
# // coordy[0] = 1;
# // coordy[numY-1] = m;

# // coordx[0] = 1;
# // coordx[numX-1] = n;
# // ```

# // Ý nghĩa:

# // * Coi **biên trên/dưới/trái/phải** cũng là hàng rào
# // * Vì hình vuông có thể dùng toàn bộ cánh đồng

# // 📌 Ví dụ:

# // * Chiều cao từ `1 → m`
# // * Chiều rộng từ `1 → n`

# // ---

# // ### 2.2. Gộp hàng rào + biên vào chung một mảng

# // ```java
# // coordy = [1, hFences..., m]
# // coordx = [1, vFences..., n]
# // ```

# // Sau đó:

# // ```java
# // Arrays.sort(coordy);
# // Arrays.sort(coordx);
# // ```

# // ➡️ Ta có **tọa độ các hàng rào đã sắp xếp**

# // ---

# // ## 3. Ý tưởng chính của thuật toán

# // ### 🔑 Ý tưởng cốt lõi:

# // > Nếu một hình vuông cạnh L tồn tại
# // > 👉 thì **L phải xuất hiện đồng thời**:

# // * Là khoảng cách giữa **2 hàng rào dọc**
# // * Là khoảng cách giữa **2 hàng rào ngang**

# // ---

# // ## 4. Bước 1 – Tính tất cả khoảng cách theo chiều ngang

# // ```java
# // Set<Long> diffs = new HashSet<>();
# // ```

# // ### Mục đích:

# // * Lưu **mọi khoảng cách có thể** giữa 2 hàng rào dọc
# // * Để sau này kiểm tra nhanh O(1)

# // ```java
# // for(int i = 0; i < coordx.length; i++){
# //     for(int j = i; j < coordx.length; j++){
# //         long temp1 = (long) coordx[i] - coordx[j];
# //         diffs.add(temp1);
# //     }
# // }
# // ```

# // 📌 Ý nghĩa:

# // * Duyệt **mọi cặp (i, j)**
# // * Lấy hiệu tọa độ → chính là **độ dài cạnh có thể có theo chiều ngang**

# // 👉 `diffs` chứa **tất cả độ dài L có thể tạo được theo chiều ngang**

# // ---

# // ## 5. Bước 2 – Duyệt chiều dọc & tìm hình vuông lớn nhất

# // ```java
# // for(int a = 0; a < coordy.length; a++){
# //     for(int b = a; b < coordy.length; b++){
# //         long temp2 = (long) coordy[a] - coordy[b];
# // ```

# // ### Với mỗi khoảng cách dọc `temp2`:

# // #### 5.1. Cắt nhánh (tối ưu)

# // ```java
# // if(temp2 * temp2 <= maxLen)
# //     continue;
# // ```

# // ➡️ Nếu **diện tích hiện tại nhỏ hơn kết quả đã có**
# // → Không cần xét tiếp (tối ưu thời gian)

# // ---

# // #### 5.2. Kiểm tra có tạo được hình vuông không

# // ```java
# // boolean same = diffs.contains(temp2);
# // ```

# // Ý nghĩa:

# // * Nếu `temp2` cũng xuất hiện trong `diffs`
# //   → tồn tại khoảng ngang = khoảng dọc
# //   → **tạo được hình vuông**

# // ---

# // #### 5.3. Cập nhật kết quả

# // ```java
# // temp = temp2 * temp2;
# // if(same){
# //     maxLen = Math.max(maxLen, temp);
# // }
# // ```

# // ➡️ Lưu **diện tích lớn nhất**

# // ---

# // ## 6. Kết thúc

# // ```java
# // if(maxLen == 0){
# //     return -1;
# // }
# // return (int)(maxLen % mod);
# // ```

# // * Không tìm được hình vuông → `-1`
# // * Có → trả về diện tích (mod 1e9+7)

# // ---

# // ## 7. Tóm tắt thuật toán (dạng phỏng vấn)

# // > 🔹 Thêm biên cánh đồng vào danh sách hàng rào
# // > 🔹 Sắp xếp các hàng rào
# // > 🔹 Sinh **mọi khoảng cách ngang** và lưu vào `HashSet`
# // > 🔹 Duyệt **mọi khoảng cách dọc**, nếu:
# // >
# // > * Khoảng đó cũng xuất hiện ở chiều ngang
# // > * Diện tích lớn hơn kết quả hiện tại
# // >   👉 thì cập nhật đáp án

# // ---

# // ## 8. Độ phức tạp

# // * Thời gian:
# //   **O(X² + Y²)**
# //   (X = số hàng rào dọc, Y = số hàng rào ngang)

# // * Không gian:
# //   **O(X²)** cho `HashSet`

# // ---

# // ## 9. Nhận xét nhanh (rất quan trọng)

# // * ✅ Ý tưởng **đúng và phổ biến**
# // * ⚠️ Có thể tối ưu hơn bằng:

# //   * Chỉ xét **hiệu dương**
# //   * Sinh khoảng cách theo thứ tự giảm dần để break sớm

# // Nếu bạn muốn:

# // * 👉 Mình giải thích **bằng hình vẽ**
# // * 👉 Chỉ ra **điểm dễ sai trong code**
# // * 👉 Viết lại **phiên bản tối ưu hơn**
# // * 👉 So sánh với **solution chuẩn LeetCode**

# // cứ nói nhé 👍
