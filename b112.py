
# // 3583. Count Special Triplets(09/12/2025)
# // Dưới đây là **giải thích đề bài LeetCode 3583 – Count Special Triplets** theo cách **dễ hiểu nhất**:
# # // Dưới đây là**giải thích thuật toán**,**code đã được thêm chú thích đầy đủ**,và**hàm main dùng Scanner**.Mình viết cực dễ hiểu,dành cho bạn học nhanh.
# Dưới đây là **giải thích thuật toán thật dễ hiểu**, kèm **code đã thêm chú thích chi tiết từng dòng** cho bạn.

# ---

# # ✅ **Ý tưởng thuật toán (Python)** — cực dễ hiểu

# Thuật toán dựa trên việc tìm các bộ ba (i, j, k) đặc biệt thỏa:

# ```
# nums[i] = 2 * nums[j]
# nums[k] = nums[j] / 2   (và nums[j] phải là số chẵn)
# # ```

# Vì trong lời giải tối ưu, bộ ba đặc biệt xảy ra khi:

# * i = số đứng trước j và bằng **2 × nums[j]**
# * k = số đứng sau j và bằng **nums[j] / 2**

# Chúng ta duyệt j từ trái sang phải và theo dõi:

# ### ✔ dic[x]:

# số lần xuất hiện của số x ở **bên trái** j (ứng với index i)

# ### ✔ dic2[x]:

# số bộ đôi hợp lệ (i, j) tạo ra giá trị x để sau này ghép với k

# ---

# # 🟦 **Giải thích từng bước khi duyệt nums[j]**

# Giả sử đang xét giá trị `num = nums[j]`:

# ---

# ## **1️⃣ Nếu num là số chẵn và num//2 đã có trong dic2 → cộng vào kết quả**

# ```python
# if num % 2 == 0 and num // 2 in dic2:
#     res += dic2[num // 2]
# ```

# Vì:

# * `dic2[num//2]` = số lượng (i, j₁) trước đó sao cho
#   `nums[i] = 2 × nums[j₁]`
#   và `nums[k] = nums[j₁]/2 = num//2 == num_k`
# * Nếu hiện tại num = nums[k], ta tạo được triplet đầy đủ (i, j₁, k)

# ## **2️⃣ Nếu tồn tại num * 2 ở bên trái → update dic2[num]**

# ```python
# if num * 2 in dic:
#     dic2[num] = dic2.get(num, 0) + dic[num * 2]
# ```

# Giải thích:

# * Nếu `num * 2` đã xuất hiện bên trái (ở i)
# * Và j hiện tại là `num`
# * Thì ta có **slot (i, j)** sẵn sàng dùng cho tương lai

# Các slot này được cộng dồn vào `dic2[num]`.

# ---

# ## **3️⃣ Đánh dấu num đã xuất hiện bên trái**

# ```python
# dic[num] = dic.get(num, 0) + 1
# ```

# ---

# ---

# # ✅ **Full code đã thêm chú thích cực chi tiết**

# ```python
from typing import List
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        dic = {}     # dic[x] = số lần xuất hiện x bên trái j (ứng với i)
        dic2 = {}    # dic2[x] = số bộ đôi (i, j) đã tạo ra để k sau này bằng x
        res = 0
        MOD = 10**9 + 7

        for num in nums:

            # 1) num đang là ứng viên cho vị trí k
            #    => nếu k = num và j trước đó là num/2 (phải chẵn)
            #    => và đã có (i, j) lưu trong dic2[num//2]
            if num % 2 == 0 and num // 2 in dic2:
                res += dic2[num // 2]
                res %= MOD

            # 2) num đang làm j
            #    => check xem có ai bên trái làm i = 2 * num
            #    => nếu có thì tạo cặp (i, j) để tương lai kết hợp với k
            if num * 2 in dic:
                if num in dic2:
                    dic2[num] += dic[num * 2]
                else:
                    dic2[num] = dic[num * 2]

            # 3) Đánh dấu num đã xuất hiện bên trái (cho những j sau này)
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        return res
# ```

# ---

# # 🎯 **Tóm tắt thuật toán siêu ngắn**

# | Giai đoạn | Ý nghĩa                                     |
# | --------- | ------------------------------------------- |
# | dic       | Đếm số i có thể đóng góp vào j              |
# | dic2      | Đếm số (i, j) có thể ghép thành bộ ba với k |
# | res       | Kết quả bộ ba đặc biệt                      |

# # Mỗi lần gặp num:

# * Nó thử đóng vai k → check dic2
# * Nó thử đóng vai j → update dic2 từ dic
# * Nó trở thành phần tử bên trái cho tương lai → update dic

# ---

# # Nếu bạn muốn

# Mình có thể làm thêm:

# ✔ minh họa từng bước với ví dụ
# ✔ so sánh code Java – Python
# ✔ vẽ hình mô phỏng thuật toán

# Bạn cần phần nào?

# import java.util.*;

# public class b113 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int n = sc.nextInt();
#         int[] nums = new int[n];

#         for (int i = 0; i < n; i++) {
#             nums[i] = sc.nextInt();
#         }

#         System.out.println(specialTriplets(nums));
#     }

#     // f[x] = số lượng xuất hiện của x ở bên trái j (i < j)
#     // r[x] = số lượng xuất hiện của x ở bên phải j (k > j)
#     static int[] f = new int[100001];
#     static int[] r = new int[100001];

#     static int MOD = 1_000_000_007;

#     public static int specialTriplets(int[] nums) {

#         // Bước 1: Ban đầu, tất cả phần tử đều nằm bên phải j → đưa hết vào r[]
#         for (int n : nums) {
#             r[n]++;
#         }

#         int count = 0;
#         int t;

#         // Bước 2: Duyệt từng nums[j]
#         for (int n : nums) {

#             // nums[j] không còn bên phải nữa → giảm r[n]
#             r[n]--;

#             // t = 2 * n (quy luật toán học của bài)
#             t = n << 1; // dịch trái 1 bit = nhân 2

#             // Nếu t trong phạm vi
#             if (t < f.length) {

#                 // Số triplets thêm = f[t] * r[t]
#                 // f[t] = số lượng t nằm bên trái (chọn làm i)
#                 // r[t] = số lượng t nằm bên phải (chọn làm k)
#                 count = (count + (int) ((1L * f[t] * r[t]) % MOD)) % MOD;
#             }

#             // Chuyển nums[j] sang bên trái
#             f[n]++;
#         }

#         // Reset f[] để tránh lỗi test nhiều lần
#         for (int n : nums) {
#             f[n] = 0;
#         }

#         return count;
#     }
# }

# // ---

# // #✅**Ý tưởng thuật toán(giải thích đơn giản nhất)**

# // Ta muốn đếm số bộ ba chỉ số**(i,j,k)**sao cho:

# // ```i<j<k(nums[i]%nums[j]==nums[k])(nums[j]%nums[k]==nums[i])```

# // Nhưng nếu duyệt 3 vòng for→O(n³)→TLE ngay.

# // ###🔥Cách làm trong lời giải tối ưu:

# // Họ dùng 2 mảng tần suất:

# // |Mảng|Ý
# // nghĩa||------|---------------------------------------------------||`r[x]`|số
# // lượng phần tử**chưa duyệt**bằng x(bên phải j)||`f[x]`|số lượng phần tử**đã
# // duyệt**bằng x(bên trái j)|

# // Khi đứng tại`nums[j]=n`:

# // ###✔1)Giảm r[n]

# // Vì nums[j]**không**còn nằm bên phải nữa.

# // ###✔2)Tính giá trị cần tìm:

# // Họ cần:

# // ```nums[i]=t và nums[k]=t với t=n*2```

# // Đây là rút gọn điều kiện toán học của bài→không cần bạn hiểu sâu.

# // ###✔3)Kết quả cộng thêm:

# // ```f[t]*r[t]```

# // (vì f[t]=số phần tử bên trái=nums[i]r[t]=số phần tử bên phải=nums[k])

# // ###✔4)Sau cùng tăng f[n]

# // Vì nums[j]trở thành phần tử bên trái.

# // ---

# // #✅**Code Java có chú thích đầy đủ**

# // ```java

# // import java.util.Scanner;

# // class Solution {

# // // f[x]: số lượng phần tử đã đi qua (bên trái j)
# // // r[x]: số lượng phần tử chưa đi qua (bên phải j)
# // static int[] f = new int[100001];
# // static int[] r = new int[100001];
# // final int MOD = 1_000_000_007;

# // public int specialTriplets(int[] nums) {

# // // Bước 1: đếm tần suất ban đầu cho r[]
# // for (int n : nums) {
# // r[n]++;
# // }

# // int count = 0;
# // int t;

# // // Duyệt từng nums[j]
# // for (int n : nums) {

# // // Bước 2: nums[j] không còn nằm bên phải nữa
# // r[n]--;

# // // t = 2 * n (giá trị cần xét)
# // t = n << 1; // dịch trái = n * 2

# // // Nếu t nằm trong phạm vi
# // if (t < f.length) {

# // // Bước 3: cộng số bộ ba có nums[i] = t và nums[k] = t
# // // f[t] = số t nằm bên trái
# // // r[t] = số t nằm bên phải
# // count = (count + (int) ((1L * f[t] * r[t]) % MOD)) % MOD;
# // }

# // // Bước 4: chuyển nums[j] sang phía bên trái
# // f[n]++;
# // }

# // // Reset f[] cho lần chạy sau (LeetCode gọi nhiều test)
# // for (int n : nums) {
# // f[n] = 0;
# // }

# // return count;
# // }}```

# // ---

# // #✅**Hàm main
# // dùng Scanner**

# // ```java

# // public class Main {
# // public static void main(String[] args) {
# // Scanner sc = new Scanner(System.in);

# // // Nhập số lượng phần tử
# // int n = sc.nextInt();
# // int[] nums = new int[n];

# // // Nhập mảng
# // for (int i = 0; i < n; i++) {
# // nums[i] = sc.nextInt();
# // }

# // Solution sol = new Solution();
# // System.out.println(sol.specialTriplets(nums));
# // }
# // }```

# // ---

# // #✅

# // Muốn giải
# // thích sâu
# // hơn đoạn toán"t = n*2"?

# // Chỉ cần
# // bảo mình:**“
# // giải thích
# // vì sao t=2*n”**nhé!

# // ---

# // # ✅ **3583. Count Special Triplets — Giải thích đề bài**

# // Bạn được cho một mảng số nguyên **nums**.

# // Bạn cần đếm số bộ ba **(i, j, k)** sao cho:

# // 1. **0 ≤ i < j < k < n**
# // 2. **nums[i] % nums[j] == nums[k]**
# // 3. **nums[j] % nums[k] == nums[i]**

# // Tức là **tam giác điều kiện chia lấy dư** xảy ra theo hai chiều.

# // ---

# // # 🔍 **Hiểu bằng ví dụ**

# // Giả sử:

# // ```
# // nums = [5, 2, 1]
# // ```

# // Ta thử tất cả bộ ba (i, j, k):

# // ### Bộ ba duy nhất: (0,1,2) → (5, 2, 1)

# // Kiểm tra 2 điều kiện:

# // 1️⃣ nums[i] % nums[j] == nums[k]
# // → 5 % 2 = 1
# // → đúng, vì nums[k] = 1

# // 2️⃣ nums[j] % nums[k] == nums[i]
# // → 2 % 1 = 0
# // → nhưng nums[i] = 5
# // → sai

# // → ❌ Không phải bộ ba đặc biệt → count = 0.

# // ---

# // # 📌 **Diễn giải điều kiện trực quan**

# // ## Điều kiện 1:

# // ### ✔ nums[i] % nums[j] = nums[k]

# // → nums[k] phải là **phần dư khi i chia j**
# // → nghĩa là **nums[k] < nums[j]**
# // → và nums[j] không được bằng 0.

# // ## Điều kiện 2:

# // ### ✔ nums[j] % nums[k] = nums[i]

# // → nums[i] phải là **phần dư khi j chia k**
# // → nghĩa là nums[i] < nums[k].

# // So sánh 3 số:

# // ```
# // nums[i] < nums[k] < nums[j]
# // ```

# // Đây là một cách hiểu trực quan — sức mạnh nằm ở **điều kiện chia lấy dư hai
# // chiều**, cực kỳ hiếm khi xảy ra.

# // ---

# // # 🎯 **Kết luận đề bài**

# // Bạn phải:

# // ✔ duyệt tất cả bộ ba chỉ số (i < j < k)
# // ✔ kiểm tra 2 điều kiện modulo
# // ✔ đếm xem có bao nhiêu bộ ba thỏa mãn

# // ---

# // Nếu bạn muốn mình giải thích **thuật toán tối ưu**, hoặc **thêm code
# // Python/Java có chú thích**, chỉ cần nói mình biết nhé!
# // Ok, mình giải thích lại thật **ngắn – dễ – rõ**, đúng trọng tâm cho bạn nhé.

# // ---

# // # 🟩 **3583. Count Special Triplets – Giải thích đơn giản nhất**

# // Đề bài:
# // Đếm số bộ ba chỉ số **(i, j, k)** thỏa:

# // ### 1️⃣ Thứ tự:

# // ```
# // i < j < k
# // ```

# // ### 2️⃣ Thỏa 2 điều kiện chia dư:

# // #### Điều kiện A:

# // ```
# // nums[i] % nums[j] == nums[k]
# // ```

# // #### Điều kiện B:

# // ```
# // nums[j] % nums[k] == nums[i]
# // ```

# // ---

# // # 🔥 **Giải thích bằng ví dụ SIÊU DỄ**

# // Giả sử:

# // ```
# // nums = [6, 4, 2]
# // ```

# // Ta thử bộ ba (0, 1, 2):

# // ### ✔ nums[i] = 6

# // ### ✔ nums[j] = 4

# // ### ✔ nums[k] = 2

# // ---

# // ## ♦ Kiểm tra điều kiện A:

# // ```
# // 6 % 4 = 2
# // ```

# // → đúng bằng nums[k] = 2 → **đúng**

# // ## ♦ Kiểm tra điều kiện B:

# // ```
# // 4 % 2 = 0
# // ```

# // → phải bằng nums[i] = 6, nhưng 0 ≠ 6 → **sai**

# // → ❌ Không phải bộ ba đặc biệt.

# // ---

# // # 🟦 Vậy bản chất bài này là gì?

# // Bạn thử TẤT CẢ bộ ba (i, j, k) rồi kiểm tra 2 điều kiện:

# // ### ✔ Điều kiện A:

# // “Dư của nums[i] chia nums[j] phải bằng chính nums[k]”

# // ### ✔ Điều kiện B:

# // “Dư của nums[j] chia nums[k] phải bằng chính nums[i]”

# // Hai điều kiện này **rất khó xảy ra**, nên số bộ ba thỏa mãn thường rất ít.

# // ---

# // # 🟥 Tóm tắt lại cho dễ nhớ:

# // Muốn (i, j, k) hợp lệ thì:

# // ```
# // (nums[i] % nums[j]) phải bằng nums[k]
# // và
# // (nums[j] % nums[k]) phải bằng nums[i]
# // ```

# // Chỉ thế thôi.

# // ---

# // # 🟩 Nếu bạn muốn, mình sẽ:

# // ✅ giải thích bằng hình minh họa
# // ✅ viết code Python/Java siêu dễ hiểu
# // ✅ đưa ví dụ nhiều hơn

# // Chỉ cần bạn nói: *"giải thích lại bằng hình"* hoặc *"viết code Java dễ
# // hiểu"*.
