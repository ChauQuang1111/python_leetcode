# # // Minimum Difference Between Highest and Lowest of K Scores(25/01/2026)
# # // Ok, mình giải thích **thuật toán + từng phần code** của lời giải LeetCode **1984. Minimum Difference Between Highest and Lowest of K Scores** thật rõ ràng nhé 👌
# # // (đi theo đúng tư duy phỏng vấn + học thuật)
# # // Ok👍mình**thêm`main`dùng`Scanner`**và**chú thích trực tiếp vào code**để bạn dễ học+dễ nộp bài/thuyết trình.
# Ok 👍 đây là **lời giải Python cực ngắn (one-liner)** nhưng ý tưởng bên trong vẫn là **sắp xếp + sliding window**. Mình sẽ:

# 1️⃣ Giải thích **thuật toán bằng lời**
# 2️⃣ Tách **one-liner** ra thành các bước
# 3️⃣ Viết lại code **có chú thích rõ ràng**
from typing import List
from operator import sub

class Solution:
    def minimumDifference(self, a: List[int], k: int) -> int:

        # Nếu chỉ chọn 1 phần tử thì hiệu luôn bằng 0
        if k == 1:
            return 0

        # Sắp xếp mảng tăng dần
        b = sorted(a)

        # Tính hiệu giữa phần tử thứ (i+k-1) và i
        # tương đương hiệu max - min của mỗi nhóm k phần tử
        differences = map(
            sub,        # phép trừ
            b[k-1:],    # phần tử lớn nhất của từng nhóm
            b           # phần tử nhỏ nhất của từng nhóm
        )

        # Trả về hiệu nhỏ nhất
        return min(differences)


class Solution:
    def minimumDifference(self, a: List[int], k: int) -> int:
        return min(map(sub,(b:=sorted(a))[k-1:],b))





# ---

# ## 1️⃣ Ý tưởng thuật toán (giống Java)

# * Sắp xếp mảng tăng dần
# * Xét mọi **nhóm k phần tử liên tiếp**
# * Với mỗi nhóm:

#   ```
#   hiệu = phần tử cuối − phần tử đầu
#   ```
# * Lấy **giá trị nhỏ nhất**

# ⏱ Độ phức tạp: `O(n log n)`

# ---

# ## 2️⃣ Phân tích chi tiết one-liner

# ```python
# return min(map(sub, (b := sorted(a))[k-1:], b))
# ```

### Tách từng phần:

# ### 🔹 `b := sorted(a)`

# * Sắp xếp mảng `a`
# * Gán kết quả cho `b`

# ```python
# b = sorted(a)
# ```

# ---

# ### 🔹 `(b)[k-1:]`

# * Lấy các phần tử từ vị trí `k-1` đến hết
# * Đây là **các phần tử lớn nhất trong mỗi cửa sổ k**

# Ví dụ:

# ```python
# b = [30, 40, 80, 90, 100]
# k = 3
# → b[k-1:] = [80, 90, 100]
# ```

# ---

# ### 🔹 `map(sub, b[k-1:], b)`

# * `sub(x, y)` = `x - y`
# * Tương đương:

# ```python
# b[k-1] - b[0]
# b[k]   - b[1]
# b[k+1] - b[2]
# ```

# 👉 Chính là hiệu `max − min` của từng nhóm k phần tử

# ---

# ### 🔹 `min(...)`

# * Lấy hiệu nhỏ nhất

# ---

# ## 3️⃣ Viết lại code dễ hiểu + chú thích

# ```python
# from typing import List
# from operator import sub

# class Solution:
#     def minimumDifference(self, a: List[int], k: int) -> int:

#         # Nếu chỉ chọn 1 phần tử thì hiệu luôn bằng 0
#         if k == 1:
#             return 0

#         # Sắp xếp mảng tăng dần
#         b = sorted(a)

#         # Tính hiệu giữa phần tử thứ (i+k-1) và i
#         # tương đương hiệu max - min của mỗi nhóm k phần tử
#         differences = map(
#             sub,        # phép trừ
#             b[k-1:],    # phần tử lớn nhất của từng nhóm
#             b           # phần tử nhỏ nhất của từng nhóm
#         )

#         # Trả về hiệu nhỏ nhất
#         return min(differences)
# ```

# ---

# ## 4️⃣ Ví dụ chạy tay (dry run)

# ```python
# a = [90, 40, 30, 100, 80]
# k = 3

# b = [30, 40, 80, 90, 100]

# b[k-1:] = [80, 90, 100]
# b       = [30, 40, 80]

# differences:
# 80 - 30 = 50
# 90 - 40 = 50
# 100 - 80 = 20

# → min = 20
# ```

# ---

# ## 5️⃣ Kết luận 1 câu (để ghi bài)

# > Thuật toán sắp xếp mảng và tính hiệu giữa phần tử đầu và cuối của mọi nhóm k phần tử liên tiếp, sau đó lấy giá trị nhỏ nhất.

# ---

# Nếu bạn muốn mình:

# * ✍️ Viết lại **phiên bản for-loop thuần**
# * 🔍 So sánh **Python one-liner vs Java**
# * 🧠 Giải thích cú pháp `:=` (walrus operator)

# 👉 cứ nói tiếp nhé 😄

# // ---

# // ##✅Code Java hoàn chỉnh(có`main`,`Scanner`,chú thích chi tiết)
# import java.util.*;

# public class b159 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int n = sc.nextInt();

#         int[] nums = new int[n];

#         // Nhập các phần tử mảng
#         for (int i = 0; i < n; i++) {
#             nums[i] = sc.nextInt();
#         }

#         int k = sc.nextInt();

#         int result = minimumDifference(nums, k);

#         // In kết quả
#         System.out.println("Minimum difference = " + result);

#         sc.close();
#     }

#     // Hàm chính giải bài toán
#     public static int minimumDifference(int[] nums, int k) {

#         // Nếu chỉ có 1 phần tử hoặc k = 1
#         // → max = min → hiệu = 0
#         if (nums.length == 1 || k == 1)
#             return 0;

#         // Sắp xếp mảng tăng dần
#         quickSort(nums, 0, nums.length - 1);

#         int minDifference = Integer.MAX_VALUE;

#         // Duyệt các nhóm k phần tử liên tiếp
#         for (int i = k - 1; i < nums.length; i++) {
#             // nums[i] : phần tử lớn nhất trong nhóm
#             // nums[i-k+1] : phần tử nhỏ nhất trong nhóm
#             minDifference = Math.min(
#                     minDifference,
#                     nums[i] - nums[i - k + 1]);
#         }

#         return minDifference;
#     }

#     // Thuật toán QuickSort sắp xếp mảng tăng dần
#     public static void quickSort(int[] nums, int start, int end) {

#         int left = start;
#         int right = end;

#         // Chọn pivot là phần tử đầu
#         int pivot = nums[start];

#         // Phân hoạch mảng
#         while (left <= right) {

#             // Tìm phần tử >= pivot bên trái
#             while (left <= right && nums[left] < pivot) {
#                 left++;
#             }

#             // Tìm phần tử <= pivot bên phải
#             while (left <= right && nums[right] > pivot) {
#                 right--;
#             }

#             // Hoán đổi 2 phần tử sai vị trí
#             if (left <= right) {
#                 int temp = nums[left];
#                 nums[left] = nums[right];
#                 nums[right] = temp;
#                 left++;
#                 right--;
#             }
#         }

#         // Đệ quy sắp xếp nửa bên trái
#         if (right > start) {
#             quickSort(nums, start, right);
#         }

#         // Đệ quy sắp xếp nửa bên phải
#         if (left < end) {
#             quickSort(nums, left, end);
#         }
#     }

# }

# // ```java

# // ---

# // ##🧠

# // Tóm tắt
# // nhanh để
# // ghi nhớ

# // ***QuickSort**→
# // sắp xếp mảng***
# // Sliding window
# // độ dài k***
# // Mỗi window:

# // ```hiệu=
# // phần tử cuối−
# // phần tử đầu```*Lấy**min**

# // ---

# // ##🎯
# // Gợi ý
# // khi đi thi/
# // phỏng vấn

# // Nếu được
# // phép dùng
# // thư viện, bạn
# // có thể thay:

# // ```java
# // quickSort(nums, 0, nums.length - 1);

# // bằng:

# // ```java
# // Arrays.sort(nums);
# // ```

# // 👉 code **ngắn hơn, an toàn hơn**, độ phức tạp vẫn `O(n log n)`.

# // ---

# // Nếu bạn muốn:

# // * ✍️ Viết **phiên bản không dùng QuickSort**
# // * 🧪 Test case mẫu + dry run từng bước
# // * 🚨 Phân tích **lỗi tiềm ẩn của QuickSort này**

# // cứ nói, mình làm tiếp cho bạn 💪

# // ---

# // ## 1️⃣ Mục tiêu của bài toán

# // * Cho mảng `nums` (điểm số)
# // * Chọn **k phần tử**
# // * Tìm **min( max − min )** trong tất cả các nhóm k phần tử

# // ---

# // ## 2️⃣ Ý tưởng tổng quát của thuật toán

# // ### 🔑 Quan sát quan trọng

# // > Nếu mảng **đã được sắp xếp**, thì nhóm k phần tử có **độ chênh lệch nhỏ
# // nhất** sẽ nằm ở **k phần tử liên tiếp**

# // 👉 Vì các số càng gần nhau thì hiệu `max − min` càng nhỏ.

# // ---

# // ## 3️⃣ Phân tích từng bước trong `minimumDifference`

# // ```java
# // if (nums.length == 1 || k == 1) return 0;
# // ```

# // ### ✔ Trường hợp đặc biệt

# // * Chỉ có 1 số hoặc
# // * Chọn 1 số

# // 👉 max = min ⇒ hiệu = 0

# // ---

# // ```java
# // quickSort(nums, 0, nums.length - 1);
# // ```

# // ### ✔ Sắp xếp mảng tăng dần

# // Ví dụ:

# // ```
# // [90, 40, 30, 100, 80]
# // → [30, 40, 80, 90, 100]
# // ```

# // ---

# // ```java
# // int minDifference = Integer.MAX_VALUE;
# // ```

# // ### ✔ Khởi tạo kết quả nhỏ nhất

# // ---

# // ```java
# // for (int i = k - 1; i < nums.length; i++) {
# // minDifference = Math.min(
# // minDifference,
# // nums[i] - nums[i - k + 1]
# // );
# // }
# // ```

# // ### ✔ Sliding Window độ dài k

# // * Xét từng **cửa sổ k phần tử liên tiếp**
# // * Vì mảng đã sắp xếp:

# // * `nums[i]` → lớn nhất
# // * `nums[i - k + 1]` → nhỏ nhất

# // 📌 Ví dụ:

# // ```
# // nums = [30, 40, 80, 90, 100]
# // k = 3

# // i = 2 → [30,40,80] → 80 - 30 = 50
# // i = 3 → [40,80,90] → 90 - 40 = 50
# // i = 4 → [80,90,100] → 100 - 80 = 20 ✅
# // ```

# // 👉 Lấy **min** trong các hiệu này

# // ---

# // ## 4️⃣ Giải thích thuật toán QuickSort

# // ### Hàm:

# // ```java
# // public void quickSort(int[] nums, int start, int end)
# // ```

# // ### 4.1 Chọn pivot

# // ```java
# // int pivot = nums[start];
# // ```

# // * Chọn **phần tử đầu tiên** làm pivot

# // ---

# // ### 4.2 Hai con trỏ

# // ```java
# // int left = start;
# // int right = end;
# // ```

# // * `left` đi từ trái sang phải
# // * `right` đi từ phải sang trái

# // ---

# // ### 4.3 Dịch con trỏ

# // ```java
# // while (left <= right && nums[left] < pivot) left++;
# // while (left <= right && nums[right] > pivot) right--;
# // ```

# // * `left`: tìm số **≥ pivot**
# // * `right`: tìm số **≤ pivot**

# // ---

# // ### 4.4 Hoán đổi

# // ```java
# // if (left <= right) {
# // swap(nums[left], nums[right]);
# // left++;
# // right--;
# // }
# // ```

# // * Đưa số nhỏ sang trái
# // * Đưa số lớn sang phải

# // ---

# // ### 4.5 Đệ quy chia mảng

# // ```java
# // if (right > start)
# // quickSort(nums, start, right);

# // if (left < end)
# // quickSort(nums, left, end);
# // ```

# // * Sau khi chia:

# // * Bên trái pivot
# // * Bên phải pivot
# // * Tiếp tục sắp xếp từng phần

# // ---

# // ## 5️⃣ Độ phức tạp

# // ### ⏱ Thời gian

# // * **QuickSort trung bình**: `O(n log n)`
# // * Duyệt sliding window: `O(n)`

# // 👉 Tổng: **O(n log n)**

# // ---

# // ### 💾 Bộ nhớ

# // * QuickSort đệ quy: `O(log n)` (trung bình)

# // ---

# // ## 6️⃣ Tóm tắt tư duy thuật toán

# // > 1️⃣ Sắp xếp mảng
# // > 2️⃣ Duyệt mọi nhóm k phần tử liên tiếp
# // > 3️⃣ Tính `max − min`
# // > 4️⃣ Lấy giá trị nhỏ nhất

# // ---

# // Nếu bạn muốn:

# // * 🔥 So sánh QuickSort này với `Arrays.sort`
# // * 🔥 Viết lại bằng **2 con trỏ + không QuickSort**
# // * 🔥 Phân tích lỗi tiềm ẩn trong QuickSort (worst-case)

# // 👉 nói mình biết, mình đào sâu tiếp cho bạn 💪

# // ---

# // ## 1️⃣ Nội dung đề bài (hiểu đơn giản)

# // * Bạn có **một mảng điểm số** `scores`
# // * Bạn được chọn **K học sinh bất kỳ**
# // * Với mỗi cách chọn K học sinh:

# // * Lấy **điểm cao nhất** trong nhóm đó
# // * Lấy **điểm thấp nhất** trong nhóm đó
# // * Tính **hiệu = điểm cao nhất − điểm thấp nhất**
# // * **Mục tiêu**: tìm **hiệu nhỏ nhất có thể**

# // 👉 Nói gọn:
# // **Chọn K điểm sao cho khoảng cách giữa điểm lớn nhất và nhỏ nhất là nhỏ
# // nhất.**

# // ---

# // ## 2️⃣ Ví dụ minh họa

# // ### Ví dụ:

# // ```
# // scores = [90, 40, 30, 100, 80]
# // K = 3
# // ```

# // ### Các cách chọn 3 điểm:

# // * `[30, 40, 80]` → max = 80, min = 30 → hiệu = 50
# // * `[40, 80, 90]` → hiệu = 50
# // * `[80, 90, 100]` → hiệu = 20 ✅
# // * `[30, 40, 90]` → hiệu = 60

# // 👉 **Kết quả nhỏ nhất là 20**

# // ---

# // ## 3️⃣ Ý tưởng cốt lõi của đề

# // 🔑 Muốn **hiệu nhỏ**, các điểm phải **gần nhau**

# // ➡️ Vì vậy:

# // 1. **Sắp xếp mảng tăng dần**
# // 2. Xét **mọi nhóm K phần tử liên tiếp**
# // 3. Với mỗi nhóm:

# // ```
# // hiệu = phần tử cuối − phần tử đầu
# // ```
# // 4. Lấy **hiệu nhỏ nhất**

# // ---

# // ## 4️⃣ Tại sao chỉ xét K phần tử liên tiếp?

# // * Sau khi sắp xếp,
# // các phần tử **liền nhau là những giá trị gần nhau nhất**
# // * Chọn rời rạc (nhảy cóc) chỉ làm hiệu **lớn hơn**

# // ---

# // ## 5️⃣ Tóm tắt đề bài trong 1 câu

# // > Cho mảng điểm và số K, hãy chọn K điểm sao cho **chênh lệch giữa điểm cao
# // nhất và thấp nhất là nhỏ nhất có thể**.

# // ---

# // Nếu bạn muốn:

# // * ✔️ Giải bằng **Java / Python**
# // * ✔️ Phân tích **độ phức tạp**
# // * ✔️ So sánh với bài tương tự trong **sliding window**

# // 👉 cứ nói tiếp, mình giải ngay 👍
