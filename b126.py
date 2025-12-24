# # // Apple Redistribution into Boxes(24/12/2025)
# # // **Apple Redistribution into Boxes – Giải thích đề bài (tiếng Việt)**
# Dưới đây là **giải thích thuật toán + code Python có chú thích chi tiết** cho bài
# **3074. Apple Redistribution into Boxes**, đúng với đoạn code bạn đưa 👇

# ---

# ## 1. Thuật toán sử dụng

# 👉 **Greedy (Tham lam)**

# **Ý tưởng cốt lõi**:

# > Để dùng **ít hộp nhất**, luôn chọn **hộp có sức chứa lớn nhất trước**.

# Vì ta được phép **redistribute táo tự do**, nên:

# * Không quan tâm táo ban đầu ở hộp nào
# * Chỉ cần tổng số táo và sức chứa các hộp

# ---

# ## 2. Giải thích từng bước thuật toán

# 1. **Tính tổng số táo**
# 2. **Sắp xếp các hộp theo sức chứa giảm dần**
# 3. **Lấy lần lượt các hộp lớn nhất**, trừ dần số táo cần chứa
# 4. Đếm số hộp đã dùng đến khi **táo ≤ 0**

# ---

# ## 3. Code Python có chú thích chi tiết

# ```python
from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], cap: List[int]) -> int:

        # 1. Tính tổng số táo cần phân phối
        tot = sum(apple)

        # 2. Sắp xếp sức chứa hộp giảm dần
        #    để luôn chọn hộp lớn nhất trước (Greedy)
        cap.sort(reverse=True)

        # 3. res: số hộp đã sử dụng
        res = 0

        # 4. Dùng các hộp lớn nhất cho đến khi đủ chứa táo
        while tot > 0:
            tot -= cap[res]  # trừ đi sức chứa của hộp hiện tại
            res += 1         # tăng số hộp đã dùng

        # 5. Trả về số hộp ít nhất cần dùng
        return res


## 4. Ví dụ minh họa

### Input

# ```python
# apple = [1, 3, 2]
# cap = [4, 3, 1, 5]
# ```

# ### Diễn giải

# * Tổng táo = `6`
# * Sắp xếp cap → `[5, 4, 3, 1]`
# * Lấy hộp:

#   * 5 → còn 1 táo
#   * 4 → đủ

# 👉 Kết quả: `2`

# ---

# ## 5. Vì sao Greedy là đúng?

# * Nếu không chọn hộp lớn nhất
# * Mà chọn hộp nhỏ trước
#   👉 sẽ cần **nhiều hộp hơn**

# ➡️ Do đó:

# > Chọn hộp lớn nhất trước **luôn tối ưu**

# ---

# ## 6. Độ phức tạp

# | Bước          | Độ phức tạp |
# | ------------- | ----------- |
# | Tính tổng táo | O(n)        |
# | Sắp xếp cap   | O(m log m)  |
# | Vòng while    | O(m)        |

# 👉 Tổng: **O(m log m)**

# ---

# ## 7. Tóm tắt ngắn gọn (học thuộc)

# > Bài toán dùng **Greedy**:
# > sắp xếp hộp theo sức chứa giảm dần,
# > chọn lần lượt các hộp lớn nhất cho đến khi đủ chứa toàn bộ táo.

# Nếu bạn muốn, mình có thể:

# * Viết **giả mã (pseudocode)**
# * So sánh **Python vs Java**
# * Chỉ ra **lỗi thường gặp khi làm bài này**

# 👉 cứ nói nhé 👍











# import java.util.*;

# public class b127 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         // Nhập số hộp táo ban đầu
#         int n = sc.nextInt();
#         int[] apple = new int[n];

#         // Nhập số táo trong mỗi hộp
#         for (int i = 0; i < n; i++) {
#             apple[i] = sc.nextInt();
#         }

#         // Nhập số hộp chứa
#         int m = sc.nextInt();
#         int[] capacity = new int[m];

#         // Nhập sức chứa của mỗi hộp
#         for (int i = 0; i < m; i++) {
#             capacity[i] = sc.nextInt();
#         }

#         int result = minimumBoxes(apple, capacity);

#         System.out.println(result);

#         sc.close();

#     }

#     // Hàm tìm số hộp ít nhất cần dùng
#     public static int minimumBoxes(int[] apple, int[] capacity) {

#         // 1. Tính tổng số táo
#         int sum = 0;
#         for (int i = 0; i < apple.length; i++) {
#             sum += apple[i];
#         }

#         // 2. Sắp xếp mảng capacity tăng dần (Bubble Sort)
#         int c;
#         for (int i = 0; i < capacity.length; i++) {
#             for (int j = 0; j < capacity.length - i - 1; j++) {
#                 if (capacity[j] > capacity[j + 1]) {
#                     c = capacity[j];
#                     capacity[j] = capacity[j + 1];
#                     capacity[j + 1] = c;
#                 }
#             }
#         }

#         // 3. Chọn các hộp có sức chứa lớn nhất trước (Greedy)
#         int temp = 0; // tổng sức chứa hiện tại
#         int count = 0; // số hộp đã dùng

#         for (int i = capacity.length - 1; i >= 0; i--) {
#             if (temp < sum) {
#                 temp += capacity[i];
#                 count++;
#             }
#         }

#         // 4. Trả về số hộp ít nhất
#         return count;
#     }

# }

# // Đề bài này thường xuất hiện trong các bài toán **chia táo vào hộp**
# // (redistribution), trọng tâm là **phân phối lại** sao cho thỏa mãn một điều
# // kiện nào đó (công bằng, đủ chỗ, đúng số lượng,…).

# // ---

# // ## Nội dung đề bài (ý nghĩa chung)

# // * Bạn có **n hộp**.
# // * Mỗi hộp ban đầu chứa **một số quả táo** (có thể khác nhau).
# // * Bạn được phép **chuyển táo giữa các hộp**.
# // * Mục tiêu là **phân phối lại táo** sao cho:

# // * Mỗi hộp có **đủ táo theo yêu cầu** (thường là ≥ một số nào đó, hoặc bằng
# // nhau).
# // * Hoặc kiểm tra **có thể hay không thể** phân phối lại theo điều kiện đề bài.

# // 👉 Thông thường đề sẽ hỏi:

# // * Có thể phân phối không? (`YES / NO`)
# // * Hoặc số hộp thỏa mãn điều kiện
# // * Hoặc số táo tối đa/tối thiểu mỗi hộp sau khi phân phối

# // ---

# // ## Ví dụ dạng đề phổ biến

# // ### Dạng 1: Chia đều táo

# // * Có `n` hộp, tổng `S` quả táo
# // * Hỏi: có thể chia sao cho **mỗi hộp có số táo bằng nhau** không?

# // 👉 Điều kiện:

# // ```
# // S % n == 0
# // ```

# // ---

# // ### Dạng 2: Đảm bảo mỗi hộp có ít nhất k quả

# // * Mỗi hộp i cần **ít nhất `k[i]` quả táo**
# // * Tổng số táo là `S`

# // 👉 Điều kiện:

# // ```
# // S ≥ k[0] + k[1] + ... + k[n-1]
# // ```

# // ---

# // ### Dạng 3: Hộp có sức chứa giới hạn

# // * Mỗi hộp có **capacity[i]**
# // * Táo có thể chuyển tự do giữa các hộp

# // 👉 Điều kiện:

# // ```
# // Tổng táo ≤ tổng sức chứa
# // ```

# // ---

# // ## Ý tưởng giải chung

# // 1. **Tính tổng số táo**
# // 2. **So sánh với yêu cầu đề bài**
# // 3. Vì được phép **redistribute (phân phối lại)** →
# // 👉 không quan tâm táo đang ở hộp nào ban đầu
# // 👉 chỉ quan tâm **tổng táo**

# // ---

# // ## Ví dụ minh họa

# // **Input**

# // ```
# // boxes = [1, 2, 3]
# // ```

# // **Giải thích**

# // * Tổng táo = 6
# // * Có 3 hộp
# // * Mỗi hộp có thể có 2 táo → hợp lệ

# // **Output**

# // ```
# // YES
# // ```

# // ---

# // ## Tóm tắt ngắn gọn

# // 👉 *Apple Redistribution into Boxes* =
# // **Kiểm tra xem tổng số táo có đủ để phân phối lại vào các hộp theo điều kiện
# // hay không.**

# // Không cần quan tâm táo ở hộp nào ban đầu, chỉ cần:

# // * **Tổng táo**
# // * **Điều kiện mỗi hộp**

# // ---

# // Nếu bạn có **đề bài gốc (Codeforces / LeetCode / HackerRank)** hoặc
# // **input–output cụ thể**, gửi mình nhé 👉 mình sẽ **giải chi tiết từng dòng
# // code** cho bạn 💡
# // Mình sẽ **giải thích thuật toán (algorithm)** của đoạn code này **từng bước,
# // đúng trọng tâm**, để bạn có thể trình bày lại trong bài thi / vấn đáp 👇

# // ---

# // ## 1. Tên & bản chất thuật toán

# // 👉 Thuật toán sử dụng: **Greedy (Tham lam)**

# // **Ý tưởng chính**:

# // > Muốn dùng **ít hộp nhất** để chứa **toàn bộ táo**, thì **luôn chọn hộp có
# // sức chứa lớn nhất trước**.

# // ---

# // ## 2. Mục tiêu bài toán

# // * Có nhiều quả táo → **tổng số táo cố định**
# // * Có nhiều hộp với sức chứa khác nhau
# // * Được phép **redistribute** (đổ táo tự do)

# // 🎯 **Tìm số hộp ít nhất** sao cho **tổng sức chứa ≥ tổng táo**

# // ---

# // ## 3. Các bước của thuật toán

# // ---

# // ### 🔹 Bước 1: Tính tổng số táo

# // ```java
# // int sum = 0;
# // for (int i = 0; i < apple.length; i++) {
# // sum += apple[i];
# // }
# // ```

# // 📌 Kết quả:

# // * `sum` = **tổng số táo cần chứa**

# // ---

# // ### 🔹 Bước 2: Sắp xếp mảng capacity (tăng dần)

# // ```java
# // for (int i = 0; i < capacity.length; i++) {
# // for (int j = 0; j < capacity.length - i - 1; j++) {
# // if (capacity[j] > capacity[j + 1]) {
# // c = capacity[j];
# // capacity[j] = capacity[j + 1];
# // capacity[j + 1] = c;
# // }
# // }
# // }
# // ```

# // 📌 Thuật toán sắp xếp:

# // * **Bubble Sort**
# // * Đưa các hộp **lớn nhất về cuối mảng**

# // 📌 Mục đích:

# // * Dễ dàng chọn hộp có **sức chứa lớn nhất trước**

# // ---

# // ### 🔹 Bước 3: Chọn hộp lớn nhất cho đến khi đủ táo (Greedy)

# // ```java
# // int temp = 0;
# // int count = 0;

# // for (int i = capacity.length - 1; i >= 0; i--) {
# // if (temp < sum) {
# // temp += capacity[i];
# // count++;
# // }
# // }
# // ```

# // 📌 Giải thích:

# // * `temp`: tổng sức chứa đã dùng
# // * Duyệt từ **hộp lớn nhất → nhỏ nhất**
# // * Mỗi lần:

# // * cộng sức chứa vào `temp`
# // * tăng số hộp `count`
# // * Dừng khi `temp ≥ sum`

# // 📌 Đây chính là **bước Greedy**:

# // > Luôn chọn phương án “tốt nhất ngay lúc này” → hộp lớn nhất

# // ---

# // ### 🔹 Bước 4: Trả kết quả

# // ```java
# // return count;
# // ```

# // 👉 `count` = **số hộp ít nhất cần dùng**

# // ---

# // ## 4. Vì sao Greedy là đúng?

# // Giả sử:

# // * Nếu không chọn hộp lớn nhất
# // * Mà chọn nhiều hộp nhỏ hơn

# // 👉 Sẽ cần **nhiều hộp hơn** để đạt cùng tổng sức chứa

# // ➡️ Do đó:

# // > Chọn hộp lớn nhất trước **luôn tối ưu**

# // ---

# // ## 5. Độ phức tạp thuật toán

# // | Phần | Độ phức tạp |
# // | -------------------- | ----------- |
# // | Tính tổng táo | O(n) |
# // | Bubble Sort capacity | O(m²) |
# // | Chọn hộp | O(m) |

# // 👉 Tổng: **O(m²)**
# // (*m = số hộp*)

# // 📌 Nếu dùng `Arrays.sort()` → **O(m log m)** (tối ưu hơn)

# // ---

# // ## 6. Tóm tắt ngắn gọn để nhớ

# // 📌 **Thuật toán Apple Redistribution**

# // 1. Tính tổng táo
# // 2. Sắp xếp sức chứa hộp
# // 3. Lấy hộp lớn nhất trước (Greedy)
# // 4. Đếm số hộp đủ chứa táo

# // ---

# // Nếu bạn muốn, mình có thể:

# // * Viết **phiên bản tối ưu**
# // * Viết **giả mã (pseudocode)**
# // * Hướng dẫn **cách trình bày khi thi vấn đáp**

# // 👉 chỉ cần nói 👍
