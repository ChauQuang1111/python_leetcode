# # // 3432. Count Partitions with Even Sum Difference(05/12/2025)
# # // Dưới đây là **giải thích dễ hiểu** cho đề bài **LeetCode 3432 – Count Partitions with Even Sum Difference**.
from typing import List
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        # Tính tổng tất cả phần tử trong mảng
        # Ta cần biết tổng chẵn hay lẻ để quyết định số cách chia hợp lệ
        total_sum = sum(nums)

        # Nếu tổng là số lẻ → không thể chia mảng thành 2 phần có tổng cùng parity
        # Vì chẵn + chẵn = chẵn
        #     lẻ + lẻ = chẵn
        # Không bao giờ ra lẻ → nên tổng lẻ thì không có cách chia nào hợp lệ
        if total_sum % 2 == 1:
            return 0

        # Nếu tổng là số chẵn → Tất cả vị trí chia từ 1 đến n-1 đều hợp lệ
        # Vì luôn có thể đạt được left và right cùng parity
        return len(nums) - 1

# # // #🧠**Giải thích thuật toán**

# # // Đoạn code:

# # // ```java public int countPartitions(int[]nums){int sum=0;for(int i=0;i<nums.length;i++)sum+=nums[i];if(sum%2==0)return nums.length-1;return 0;}```

# # // ###✔️ Mấu chốt để hiểu bài 3432:

# # // Ta cần tìm số vị trí chia mảng thành 2 phần:

# # // ```left=nums[0..i-1]right=nums[i..n-1]```

# # // sao cho:

# # // ```(sum(left)-sum(right))là số chẵn```

# # // ##🔍Nhận xét quan trọng:

# # // Một số là**chẵn**khi:

# # // ```(a-b)%2==0<=>a%2==b%2```

# # // Tức là**tổng bên trái và tổng bên phải phải cùng parity**(cùng chẵn hoặc cùng lẻ).

# # // ###Mà:

# # // ```sum(left)+sum(right)=sum(nums)```

# # // ⇒Nghĩa là:

# # // *Nếu**tổng toàn mảng là số lẻ**,thì bên trái+bên phải=lẻ→Không thể tách thành 2 phần cùng chẵn hoặc cùng lẻ→**Không có vị trí nào hợp lệ**

# # // *Nếu**tổng toàn mảng là số chẵn**,thì:

# # // *left và right luôn có thể cùng chẵn hoặc cùng lẻ*Mỗi vị trí chia(từ 1→n−1)đều hợp lệ→Có**(n−1)**vị trí chia

# # // Vì vậy:

# # // ###🎯Kết luận:

# # // *Nếu tổng mảng**chẵn**→kết quả=`n-1`*Nếu tổng mảng**lẻ**→kết quả=`0`

# # // Đó chính là điều code đang làm.

# # // ---

# # // #✅**Code Java đầy đủ+chú thích+Scanner**

# # // ```java

# # import java.util.*;

# # public class b109 {
# #     static Scanner sc = new Scanner(System.in);

# #     public static void main(String[] args) {
# #         int n = sc.nextInt();

# #         int[] nums = new int[n];

# #         System.out.println("Nhap mang:");
# #         for (int i = 0; i < n; i++) {
# #             nums[i] = sc.nextInt();
# #         }

# #         int result = countPartitions(nums);

# #         System.out.println("So vi tri chia hop le = " + result);

# #         sc.close();
# #     }

# #     public static int countPartitions(int[] nums) {

# #         int sum = 0;

# #         // Tính tổng toàn bộ mảng
# #         for (int i = 0; i < nums.length; i++) {
# #             sum += nums[i];
# #         }

# #         // ✔ Nếu tổng chẵn → có thể chia tại bất kỳ vị trí nào từ 1 đến n-1
# #         // Vì lúc đó left và right luôn có thể có cùng parity
# #         if (sum % 2 == 0) {
# #             return nums.length - 1;
# #         }

# #         // ✔ Nếu tổng lẻ → không có vị trí nào khiến left & right cùng parity
# #         return 0;
# #     }
# # }

# # // Input:

# # // ```n=4 nums=1 2 3 4```

# # // Tổng=1+2+3+4=10(chẵn)

# # // →
# # // Kết quả = 4 - 1=**3**

# # // ---

# # // Nếu bạn
# # // muốn mình
# # // giải thích
# # // bằng sơ
# # // đồ hoặc
# # // làm thêm
# # // ví dụ
# # // từng bước, mình
# # // làm ngay!

# # // # 🧠 **1. Đề bài nói gì?**

# # // Bạn được cho một **mảng số nguyên `nums`**.

# # // Bạn muốn chia mảng thành **hai phần liên tiếp**:

# # // * Phần 1: `nums[0 : i]` (từ đầu đến i−1)
# # // * Phần 2: `nums[i : n]` (từ i đến hết)

# # // **Điều kiện:**
# # // Bạn cần đếm **bao nhiêu vị trí `i`** sao cho hiệu giữa tổng hai phần là **số
# # // chẵn**.

# # // Tức là:

# # // ```
# # // ( sum(nums[0..i-1]) - sum(nums[i..n-1]) ) là số chẵn
# # // ```

# # // Hoặc tương đương:

# # // ```
# # // ( sum(left) - sum(right) ) % 2 == 0
# # // ```

# # // ---

# # // # 🎯 **2. Nhận ra điều kiện quan trọng**

# # // Một số chẵn khi:

# # // ```
# # // (sum(left) - sum(right)) % 2 == 0
# # // ```

# # // Điều này xảy ra khi:

# # // ```
# # // sum(left) % 2 == sum(right) % 2
# # // ```

# # // ✨ Nghĩa là **tổng bên trái và bên phải phải cùng parity (cùng chẵn hoặc cùng
# # // lẻ)**.

# # // ---

# # // # 🧩 **3. Tính toán đơn giản hơn**

# # // * Tính tổng toàn mảng: `total`
# # // * Khi duyệt mảng từ trái qua phải:

# # // * Cập nhật `leftSum`
# # // * `rightSum = total - leftSum`

# # // Điều kiện hợp lệ:

# # // ```
# # // leftSum % 2 == rightSum % 2
# # // ```

# # // ⚠ Lưu ý:
# # // `i` phải nằm trong `[1 … n-1]`
# # // (Vì phải chia mảng thành **2 phần không rỗng**)

# # // ---

# # // # ✨ Ví dụ minh họa

# # // Giả sử:

# # // ```
# # // nums = [2, 3, 4]
# # // ```

# # // Các vị trí chia:

# # // ### i = 1:

# # // left = [2], sum = 2 (chẵn)
# # // right = [3,4], sum = 7 (lẻ)
# # // → khác parity → ❌

# # // ### i = 2:

# # // left = [2,3], sum = 5 (lẻ)
# # // right = [4], sum = 4 (chẵn)
# # // → khác parity → ❌

# # // ➡️ Không có vị trí nào hợp lệ → kết quả = **0**

# # // ---

# # // # 📝 **Tóm tắt đề bài**

# # // Bạn cần:

# # // ✔ Chia mảng ra hai phần liên tiếp
# # // ✔ Đếm số lần hiệu của tổng hai phần là **số chẵn**
# # // ✔ Tương đương với: tổng phần trái và phải **cùng chẵn hoặc cùng lẻ**

# # // ---

# # // Nếu bạn muốn, mình có thể viết luôn lời giải **Python / Java / C++** cho bài
# # // này.
# Dưới đây là **giải thích thuật toán** + **code Python có chú thích chi tiết** cho lời giải cực ngắn của bài **3432. Count Partitions with Even Sum Difference**.

# ---

# # 🧠 **Giải thích thuật toán**

# Bài yêu cầu đếm số cách chia mảng thành hai phần liên tiếp:

# * Left = `nums[0 : i]`
# * Right = `nums[i : n]`

# Sao cho:

# ```
# (sum(left) - sum(right)) là số chẵn
# ```

# ---

# ## 🎯 Điều quan trọng nhất:

# Một số chẵn khi:

# ```
# (sum(left) - sum(right)) % 2 == 0
# ```

# Điều này tương đương:

# ```
# sum(left) % 2 == sum(right) % 2
# ```

# Tức là:

# ➡️ **Hai phần phải có tổng cùng parity (cùng chẵn hoặc cùng lẻ).**

# ---

# ## 🔍 Liên hệ với tổng toàn mảng:

# Vì:

# ```
# sum(nums) = sum(left) + sum(right)
# ```

# Ta chia thành hai trường hợp:

# ---

# ### ✔️ **1. Nếu tổng toàn mảng là số lẻ**

# * Một số lẻ **không thể** được tách thành hai phần cùng chẵn hoặc cùng lẻ.
# * Vì:

#   * chẵn + chẵn = chẵn
#   * lẻ + lẻ = chẵn
#     → Không bao giờ ra **lẻ**

# 📌 Nên không có cách chia nào hợp lệ.

# → **Trả về 0**

# ---

# ### ✔️ **2. Nếu tổng toàn mảng là số chẵn**

# * Có thể tách thành (chẵn + chẵn) hoặc (lẻ + lẻ)
# * Và khi duyệt qua từng vị trí chia `i` (từ 1 đến n−1), ta luôn có thể đạt được tổng left và right cùng parity.

# ➡️ Tất cả **n − 1** vị trí chia đều hợp lệ.
# (vị trí 0 và n không tính vì một nửa sẽ rỗng)

# → **Trả về n − 1**

# ---

# # ✔️ **Code Python có chú thích**

# ```python
# class Solution:
#     def countPartitions(self, nums: List[int]) -> int:
#         # Tính tổng toàn bộ mảng
#         total = sum(nums)
        
#         # Nếu tổng là số lẻ → không thể chia thành left & right có cùng parity
#         if total % 2 == 1:
#             return 0
        
#         # Nếu tổng chẵn → tất cả vị trí chia từ 1 tới n-1 đều hợp lệ
#         return len(nums) - 1
# ```

# ---

# # 📝 **Tóm lại**

# | Trường hợp     | Kết quả                              |
# | -------------- | ------------------------------------ |
# | Tổng mảng lẻ   | Không có cách chia → `0`             |
# | Tổng mảng chẵn | Mọi vị trí chia đều hợp lệ → `n - 1` |

# ---

# Nếu bạn muốn, mình có thể giải thích thêm bằng ví dụ cụ thể (mảng nhỏ), hoặc vẽ sơ đồ phân tích left–right cho dễ hình dung hơn.
