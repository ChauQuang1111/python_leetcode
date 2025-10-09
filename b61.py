# // 3494. Find the Minimum Amount of Time to Brew Potions(09/10/2025)
from numpy import array, append        # Dùng NumPy để xử lý mảng nhanh
from itertools import accumulate, pairwise  # accumulate để tính prefix sum, pairwise để duyệt cặp liên tiếp
from typing import List
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        # Bước 1: Giả định dùng toàn bộ năng lượng cuối cùng để pha tất cả potion
        ans = sum(skill) * mana[-1]  # Tổng skill * năng lượng cuối cùng

        # Bước 2: Tính prefix sum của skill — tức là tổng kỹ năng tích lũy
        acc = array(list(accumulate(skill)))  # Ví dụ: skill = [2,3,1] → acc = [2,5,6]

        # Bước 3: offset là tổng kỹ năng trước potion hiện tại
        # append(0, acc[:-1]) nghĩa là thêm 0 vào đầu và bỏ phần tử cuối của acc
        # Ví dụ: acc = [2,5,6] → offset = [0,2,5]
        offset = append(0, acc[:-1])

        # Bước 4: Duyệt qua từng cặp năng lượng liên tiếp (m1, m2)
        # Ví dụ: mana = [5, 3, 2] → duyệt (5,3) rồi (3,2)
        for m1, m2 in pairwise(mana):
            # Tính chi phí tối đa khi chuyển từ năng lượng m1 sang m2
            # acc * m1 là phần trước khi chuyển, offset * m2 là phần sau khi chuyển
            # Lấy hiệu và chọn điểm chia tối ưu (max)
            # Ví dụ: acc = [2,5], offset = [0,2], m1=5, m2=2 → [2*5 - 0*2, 5*5 - 2*2] = [10,21]
            ans += int((acc * m1 - offset * m2).max())

        # Bước 5: Trả về tổng thời gian tối thiểu
        return ans











# import java.util.*;

# class b62 {
#    static Scanner sc = new Scanner(System.in);

#    public static void main(String[] args) {

#       int n = sc.nextInt();
#       int[] skill = new int[n];
#       for (int i = 0; i < n; i++) {
#          skill[i] = sc.nextInt();
#       }

#       int m = sc.nextInt();
#       int[] mana = new int[m];
#       for (int i = 0; i < m; i++) {
#          mana[i] = sc.nextInt();
#       }

#       long result = minTime(skill, mana);

#       System.out.println(result);
#    }

#    public static long minTime(int[] skill, int[] mana) {
#       int n = skill.length; // Số lượng kỹ năng
#       int m = mana.length; // Số lượng mana

#       // Tạo mảng cộng dồn skill để tính tổng nhanh hơn
#       long[] acc = new long[n + 1];
#       for (int i = 0; i < n; i++) {
#          acc[i + 1] = acc[i] + skill[i];
#       }

#       long t = 0; // Lưu giá trị tối ưu ở bước trước
#       long t2 = 0; // Lưu giá trị tạm thời ở bước hiện tại

#       // Duyệt qua từng giai đoạn mana
#       for (int j = 1; j < m; j++) {
#          t2 = 0;
#          for (int i = 0; i < n; i++) {
#             // Cập nhật giá trị lớn nhất có thể đạt được
#             t2 = Math.max(t2, t + mana[j - 1] * acc[i + 1] - mana[j] * acc[i]);
#          }
#          t = t2; // Cập nhật lại giá trị t
#       }

#       // Kết quả cuối cùng
#       return t + mana[m - 1] * acc[n];
#    }

# }

# // Dưới đây là **giải thích đề bài** LeetCode **3494. Find the Minimum Amount of
# // Time to Brew Potions**, cùng với các điều kiện, yêu cầu và một số hướng gợi ý
# // để giải.
# // Dưới đây là phiên bản đầy đủ của chương trình Java có**hàm`main`**,sử
# // dụng**`Scanner`để nhập dữ liệu**,và có**chú thích chi tiết từng phần**giúp
# // bạn hiểu rõ:

# // ```java

# // import java.util.*;

# // public class Main {
# // public static void main(String[] args) {
# // Scanner sc = new Scanner(System.in);

# // // Nhập số phần tử của mảng skill
# // int n = sc.nextInt();
# // int[] skill = new int[n];
# // for (int i = 0; i < n; i++) {
# // skill[i] = sc.nextInt(); // Nhập từng giá trị skill
# // }

# // // Nhập số phần tử của mảng mana
# // int m = sc.nextInt();
# // int[] mana = new int[m];
# // for (int i = 0; i < m; i++) {
# // mana[i] = sc.nextInt(); // Nhập từng giá trị mana
# // }

# // // Tạo đối tượng Solution và gọi hàm minTime
# // Solution sol = new Solution();
# // long result = sol.minTime(skill, mana);

# // // In ra kết quả
# // System.out.println(result);
# // }
# // }

# // class Solution {
# // public long minTime(int[] skill, int[] mana) {
# // int n = skill.length; // Số lượng kỹ năng
# // int m = mana.length; // Số lượng mana

# // // Tạo mảng cộng dồn skill để tính tổng nhanh hơn
# // long[] acc = new long[n + 1];
# // for (int i = 0; i < n; i++) {
# // acc[i + 1] = acc[i] + skill[i];
# // }

# // long t = 0; // Lưu giá trị tối ưu ở bước trước
# // long t2 = 0; // Lưu giá trị tạm thời ở bước hiện tại

# // // Duyệt qua từng giai đoạn mana
# // for (int j = 1; j < m; j++) {
# // t2 = 0;
# // for (int i = 0; i < n; i++) {
# // // Cập nhật giá trị lớn nhất có thể đạt được
# // t2 = Math.max(t2, t + mana[j - 1] * acc[i + 1] - mana[j] * acc[i]);
# // }
# // t = t2; // Cập nhật lại giá trị t
# // }

# // // Kết quả cuối cùng
# // return t + mana[m - 1] * acc[n];
# // }}```

# // ---

# // ###🧩

# // Giải thích
# // ngắn gọn:

# // *`acc[i]`là**tổng kỹ năng**
# // của các
# // phần tử`skill[0..i-1]`.*
# // Vòng lặp`for(
# // int j = 1;j<m;j++)`
# // mô phỏng**
# // từng giai
# // đoạn sử
# // dụng mana
# // khác nhau**.*
# // Biểu thức`t+mana[j-1]*acc[i+1]-mana[j]*acc[i]`tìm**
# // giá trị
# // tối ưu**
# // khi chuyển
# // giữa hai
# // mức mana
# // liên tiếp.*
# // Cuối cùng, trả
# // về tổng
# // thời gian
# // tối thiểu
# // có thể
# // đạt được
# // sau khi
# // xử lý
# // toàn bộ.

# // ---

# // Bạn có
# // muốn tôi thêm**
# // ví dụ input/output mẫu**và**
# // giải thích
# // cách chương
# // trình chạy
# // cụ thể**không?

# // ---

# // ## 🧩 Đề bài (tóm tắt)

# // Bạn có:

# // * `n` **wizard** (phù thủy), gọi là `wizard[0]`, `wizard[1]`, …,
# // `wizard[n−1]`.
# // * `m` **potion** cần được “pha chế” theo thứ tự (cần pha potion 0 trước rồi
# // potion 1, v.v.).
# // * Mỗi potion `j` có **mana capacity** là `mana[j]`.
# // * Mỗi wizard `i` có một **kỹ năng (skill) hoặc tốc độ** (giả sử là `skill[i]`
# // hoặc giá trị tương ứng) — tùy theo cách đặt tên trong đề bài.
# // * Yêu cầu: mỗi potion khi được pha chế sẽ đi qua **từng wizard theo thứ tự**
# // (wizard 0 → wizard 1 → … → wizard n−1).

# // Cụ thể: để hoàn thành potion `j`, wizard 0 bắt đầu, rồi wizard 1 tiếp tục,
# // v.v.
# // Mỗi wizard `i` cần thời gian **`skill[i] * mana[j]`** để xử lý potion đó (ví
# // dụ nhân kỹ năng và mana).

# // Tuy nhiên, có một ràng buộc quan trọng:

# // > Khi một wizard hoàn thành việc xử lý potion `j`, wizard tiếp theo bắt đầu
# // **không sớm hơn** thời điểm mà wizard trước đó hoàn thành các potion trước
# // đó, để đảm bảo **tuần tự công việc** không bị lật ngược.

# // Bạn cần tìm **thời gian tối thiểu T** sao cho **tất cả m potion đều được pha
# // chế xong** (qua tất cả wizard) trong thời gian ≤ T.

# // ---

# // ## ⚙️ Những điều cần lưu ý / ràng buộc

# // * Potion phải được pha theo thứ tự: potion 0 trước, rồi 1, rồi 2...
# // * Wizard phải xử lý potion `j` chỉ sau khi đã xử lý potion `j-1`.
# // * Wizard i không thể bắt đầu potion j trước thời điểm wizard i−1 hoàn thành
# // potion j (vì potion j phải đi qua tất cả wizard theo thứ tự).
# // * Giá trị `skill[i]`, `mana[j]`, và số lượng wizard/potion đều có thể lớn —
# // cần tìm cách tối ưu, không brute force một cách thô.

# // ---

# // ## 🧠 Hướng giải ý tưởng

# // Một cách tiếp cận khả thi là:

# // 1. **Binary Search** thời gian `T`.
# // Giả sử bạn đặt thời gian tối đa là `T`, kiểm tra xem có thể hoàn thành tất cả
# // potion trong ≤ `T` không.

# // 2. Cách kiểm tra (simulate / greedy):

# // * Duyệt từng potion `j` theo thứ tự
# // * Duyệt wizard theo thứ tự và tính thời gian mỗi wizard xử lý
# // * Theo ràng buộc “không bắt đầu trước”, giữ cho thời gian bắt đầu của wizard
# // i cho potion j ≥ thời gian hoàn thành wizard (i−1) cho cùng potion j
# // * Nếu tổng thời gian vượt `T` → không thể
# // * Nếu tất cả potion thực hiện xong ≤ `T`, thì `T` khả thi

# // 3. Tìm giá trị thấp nhất `T` bằng binary search.

# // ---

# // Nếu bạn muốn, mình có thể gửi **phiên bản code Python hoặc Java hoàn chỉnh**
# // cho bài này, kèm **chú thích chi tiết từng bước**, để bạn hiểu cách thực thi.
# // Bạn muốn mình gửi code kèm giải thích không?
# // Rồi, ta cùng **phân tích chi tiết** thuật toán trong đoạn code này 👇

# // ---

# // ### 🧩 **Đề bài tóm tắt (theo cách hiểu của code)**

# // Có hai mảng:

# // * `skill[i]`: kỹ năng hoặc độ khó của loại thuốc thứ `i`.
# // * `mana[j]`: lượng năng lượng cần để pha thuốc ở giai đoạn thứ `j`.

# // Ta cần tìm **thời gian nhỏ nhất (hoặc năng lượng nhỏ nhất)** để hoàn thành
# // toàn bộ quá trình pha chế thuốc — qua nhiều giai đoạn — sao cho tổng thời
# // gian là **nhỏ nhất có thể**.

# // ---

# // ### 📘 **Giải thích từng phần trong code**

# // #### 1️⃣ Tính prefix sum (`acc`)

# // ```java
# // long[] acc = new long[n + 1];
# // for (int i = 0; i < n; i++) {
# // acc[i + 1] = acc[i] + skill[i];
# // }
# // ```

# // ➡️ `acc[i]` là tổng kỹ năng của các potion **từ 0 đến i-1**
# // Ví dụ:

# // ```
# // skill = [2, 3, 5]
# // acc = [0, 2, 5, 10]
# // ```

# // Tức là:

# // * Tổng skill đến potion 1 = 2
# // * Tổng skill đến potion 2 = 5
# // * Tổng skill đến potion 3 = 10

# // Prefix sum giúp ta nhanh chóng tính được tổng `skill` trong bất kỳ đoạn nào.

# // ---

# // #### 2️⃣ Khởi tạo biến

# // ```java
# // long t = 0, t2 = 0;
# // ```

# // * `t`: thời gian (hoặc chi phí) ít nhất đến giai đoạn `j-1`.
# // * `t2`: thời gian tạm tính cho giai đoạn hiện tại `j`.

# // ---

# // #### 3️⃣ Vòng lặp qua các giai đoạn pha chế (`mana[j]`)

# // ```java
# // for (int j = 1; j < m; j++) {
# // t2 = 0;
# // for (int i = 0; i < n; i++) {
# // t2 = Math.max(t2, t + mana[j - 1] * acc[i + 1] - mana[j] * acc[i]);
# // }
# // t = t2;
# // }
# // ```

# // Giải thích chi tiết:

# // * Giai đoạn `j` phụ thuộc vào giai đoạn trước (`j-1`).
# // * Ở mỗi bước, ta **chọn vị trí chia i** (vì có thể chuyển từ potion `i` này
# // sang potion `i+1` kia).
# // Tức là, ta xét xem nên dừng giai đoạn trước ở đâu để tổng chi phí là nhỏ
# // nhất.

# // Công thức:

# // ```
# // t2 = max( t + mana[j-1]*acc[i+1] - mana[j]*acc[i] )
# // ```

# // Ý nghĩa:

# // * `t`: thời gian tích lũy đến giai đoạn `j-1`
# // * `mana[j-1] * acc[i+1]`: chi phí hoàn thành potion đến `i` trong giai đoạn
# // trước
# // * `mana[j] * acc[i]`: chi phí bắt đầu pha potion `i` trong giai đoạn hiện tại

# // → Lấy **hiệu giữa hai phần đó** để biết nếu ta chia ranh giới tại potion `i`,
# // thì tổng thời gian sẽ thay đổi thế nào.
# // → Dùng `Math.max` vì ta cần chọn điểm dừng (chia) tối ưu nhất.

# // ---

# // #### 4️⃣ Sau khi qua hết các giai đoạn

# // ```java
# // return t + mana[m - 1] * acc[n];
# // ```

# // * `t`: thời gian tối ưu đã tính đến giai đoạn `m-1`
# // * `mana[m - 1] * acc[n]`: chi phí để pha toàn bộ potion ở giai đoạn cuối.

# // ---

# // ### 🧮 **Ví dụ minh họa**

# // Giả sử:

# // ```
# // skill = [2, 3]
# // mana = [5, 2]
# // ```

# // → `acc = [0, 2, 5]`

# // * Ban đầu `t = 0`
# // * Ở j = 1:

# // * i = 0 → `t2 = max(0, 0 + 5*2 - 2*0) = 10`
# // * i = 1 → `t2 = max(10, 0 + 5*5 - 2*2) = max(10, 21) = 21`
# // → `t = 21`

# // Cuối cùng:

# // ```
# // t + mana[m-1] * acc[n] = 21 + 2 * 5 = 31
# // ```

# // → Kết quả: **31**

# // ---

# // ### ⚙️ **Tóm tắt ý tưởng**

# // * Tính prefix sum `acc` để dễ tính tổng skill.
# // * Duyệt từng giai đoạn (mỗi `mana[j]`) và tìm điểm chia tối ưu để **giảm tổng
# // thời gian**.
# // * Công thức `t + mana[j-1]*acc[i+1] - mana[j]*acc[i]` đảm bảo cân bằng giữa
# // chi phí trước và sau.
# // * Cuối cùng cộng phần chi phí còn lại ở giai đoạn cuối.

# // ---

# // Nếu bạn muốn, tôi có thể **vẽ sơ đồ trực quan (diagram)** minh họa cách các
# // giai đoạn và công thức hoạt động — bạn muốn chứ?
# Rất hay! 🧠
# Đoạn code Python này là **phiên bản ngắn gọn, tối ưu hơn** của thuật toán trong Java mà bạn hỏi trước đó — nhưng dùng thư viện **NumPy** để xử lý vector (mảng) hiệu quả.
# Giờ mình sẽ **giải thích từng dòng code và toàn bộ ý tưởng thuật toán** 👇

# ---

# ## ✅ **Mục tiêu bài toán**

# Bài toán **“Find the Minimum Amount of Time to Brew Potions”** yêu cầu tính tổng thời gian nhỏ nhất cần thiết để pha chế tất cả các potion, trong đó:

# * `skill[i]`: độ khó của potion thứ `i`.
# * `mana[j]`: lượng năng lượng sử dụng ở giai đoạn `j`.

# Thuật toán dựa vào việc tìm cách “chia điểm dừng” giữa các potion sao cho **tổng chi phí (mana * skill)** là nhỏ nhất.

# ---

# ## ✅ **Giải thích chi tiết code**

# ```python
# from numpy import array, append
# from itertools import accumulate, pairwise
# ```

# 👉 Import thư viện:

# * `numpy.array` để xử lý mảng nhanh hơn.
# * `accumulate` để tính prefix sum (tổng dồn).
# * `pairwise` (Python 3.10+) để lặp qua cặp `(m1, m2)` liên tiếp trong `mana`.

# ---

# ```python
# class Solution:
#     def minTime(self, skill: List[int], mana: List[int]) -> int:
# ```

# Định nghĩa lớp `Solution` với hàm chính `minTime`.

# ---

# ```python
# ans = sum(skill) * mana[-1]
# ```

# 👉 Đây là **thời gian cơ bản** nếu bạn dùng **chỉ năng lượng cuối cùng `mana[-1]`** để pha toàn bộ potion.
# Giống như giả định ban đầu: chưa tối ưu gì cả, cứ dùng giai đoạn cuối cho tất cả.

# Ví dụ:
# Nếu `skill = [2, 3]` và `mana[-1] = 2`,
# thì `ans = (2 + 3) * 2 = 10`.

# ---

# ```python
# acc = array(list(accumulate(skill)))
# ```

# 👉 Tính **prefix sum** (tổng dồn) của mảng `skill`:

# | i | skill[i] | acc[i] |
# | - | -------- | ------ |
# | 0 | 2        | 2      |
# | 1 | 3        | 5      |

# → `acc = [2, 5]`

# Biểu diễn: `acc[i] = tổng skill từ 0 → i`.

# ---

# ```python
# offset = append(0, acc[:-1])
# ```

# 👉 Tạo mảng **offset** để biểu diễn tổng trước potion hiện tại.

# | acc    | offset |
# | ------ | ------ |
# | [2, 5] | [0, 2] |

# → `offset[i] = tổng skill từ 0 → i-1`

# (giúp tính toán phần “trước khi chuyển sang giai đoạn tiếp theo”).

# ---

# ```python
# for m1, m2 in pairwise(mana):
#     ans += int((acc * m1 - offset * m2).max())
# ```

# 🧠 Đây là **trái tim của thuật toán**.

# Giải thích từng phần:

# * `pairwise(mana)` duyệt qua từng cặp năng lượng liên tiếp `(m1, m2)`.
#   Ví dụ: nếu `mana = [5, 2]` → duyệt `(5, 2)`.

# * Với mỗi cặp `(m1, m2)`, ta xét công thức:

#   ```
#   acc * m1 - offset * m2
#   ```

#   → Biểu diễn chi phí **nếu ta chuyển từ pha chế bằng m1 sang dùng m2**
#   (tức là chọn điểm dừng giữa các potion sao cho tối ưu nhất).

# * `.max()` chọn giá trị lớn nhất trong biểu thức đó (tức là vị trí chia tốt nhất).

# * `int(...)` chuyển về số nguyên.

# * `ans += ...` cộng vào tổng thời gian.

# ---

# ```python
# return ans
# ```

# 👉 Sau khi xét hết các giai đoạn năng lượng, trả về tổng thời gian tối thiểu.

# ---

## 🔍 Ví dụ minh họa:

# Giả sử:

# ```python
# skill = [2, 3]
# mana = [5, 2]
# ```

# ### Bước 1:

# ```
# sum(skill) * mana[-1] = (2 + 3) * 2 = 10
# ```

# ### Bước 2:

# ```
# acc = [2, 5]
# offset = [0, 2]
# ```

# ### Bước 3:

# Chỉ có 1 cặp (m1=5, m2=2)

# Tính:

# ```
# acc * m1 - offset * m2 = [2*5 - 0*2, 5*5 - 2*2] = [10, 21]
# max = 21
# ```

# → `ans += 21`

# ### Bước 4:

# ```
# ans = 10 + 21 = 31
# ```

# ✅ Kết quả cuối cùng = **31**

# ---

# ## 🧩 Tóm tắt ý tưởng:

# * `acc` và `offset` giúp xác định tổng kỹ năng đến từng điểm chia.
# * `m1` và `m2` mô tả “năng lượng trước” và “năng lượng sau”.
# * Với mỗi cặp `(m1, m2)`, tìm điểm chia tối ưu sao cho tổng thời gian nhỏ nhất.
# * Kết quả cuối cùng là tổng của tất cả giai đoạn.

# ---

# Bạn có muốn mình **vẽ sơ đồ minh họa dòng chảy thuật toán (flow chart)** cho code này để dễ hình dung hơn không?
