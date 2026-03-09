# # // // Bài **“Find All Possible Stable Binary Arrays I (09/03/2026)

# Mình sẽ **giải thích thuật toán trước (ngắn gọn nhưng rõ)** rồi **viết lại code Python có chú thích từng dòng**.

# ---

# # 1. Ý tưởng thuật toán

# Ta cần **đếm số binary arrays** thỏa mãn:

# * có đúng `zero` số **0**
# * có đúng `one` số **1**
# * **không quá `limit` số giống nhau liên tiếp**

# ---

# ## Trạng thái DP

# Ta dùng 2 trạng thái:

# ```
# dp0[i][j]
# dp1[i][j]
# ```

# ### dp0[i][j]

# Số cách tạo mảng:

# ```
# i số 0
# j số 1
# kết thúc bằng 0
# ```

# ---

# ### dp1[i][j]

# Số cách tạo mảng:

# ```
# i số 0
# j số 1
# kết thúc bằng 1
# ```

# ---

# # 2. Công thức chuyển

# ### Khi kết thúc bằng 0

# Ta thêm `0` vào:

# ```
# dp0[i][j] =
# dp0[i-1][j] + dp1[i-1][j]
# ```

# Nhưng phải tránh **limit+1 số 0 liên tiếp**

# → nên phải **trừ trường hợp vi phạm**

# ```
# dp1[i-limit-1][j]
# ```

# ---

# ### Khi kết thúc bằng 1

# Tương tự:

# ```
# dp1[i][j] =
# dp1[i][j-1] + dp0[i][j-1]
# ```

# Trừ trường hợp:

# ```
# dp0[i][j-limit-1]
# ```

# ---

# # 3. Tối ưu bộ nhớ

# Thay vì lưu toàn bộ:

# ```
# dp0[i][j]
# dp1[i][j]
# ```

# Ta chỉ giữ:

# ```
# dp0_prev
# dp1_prev
# ```

# → hàng trước đó.

# ---

# ### Vì cần `dp1[i-L][j]`

# Ta dùng **deque** để lưu **L hàng gần nhất**.

# ```
# dp1q
# ```

# ---

# # 4. Ý nghĩa các biến

# ```
# dp0_prev
# ```

# hàng trước của dp0

# ```
# dp1_prev
# ```

# hàng trước của dp1

# ```
# dp1q
# ```

# queue chứa **L hàng dp1 gần nhất**

# ---

# # 5. Code Python có chú thích

# ```python
from collections import deque

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:

        mod = 10**9 + 7

        # L = limit + 1 dùng để kiểm tra khi vượt quá limit
        L = limit + 1

        # dp0_prev[j] = số cách với (i-1) số 0, j số 1, kết thúc bằng 0
        # dp1_prev[j] = số cách với (i-1) số 0, j số 1, kết thúc bằng 1
        dp0_prev = [0] * (one + 1)
        dp1_prev = [0] * (one + 1)

        # Base case: chỉ có số 1
        # hợp lệ nếu số lượng không vượt limit
        for j in range(1, min(one, limit) + 1):
            dp1_prev[j] = 1

        # deque để lưu L hàng dp1 gần nhất
        dp1q = deque([dp1_prev[:]])

        # duyệt số lượng 0
        for i in range(1, zero + 1):

            # dp0, dp1 là hàng hiện tại
            dp0 = [0] * (one + 1)
            dp1 = [0] * (one + 1)

            # nếu chỉ có số 0
            if i <= limit:
                dp0[0] = 1

            # lấy hàng dp1[i-L] nếu tồn tại
            old1 = dp1q[0] if i >= L else None

            # duyệt số lượng 1
            for j in range(1, one + 1):

                # tính dp0[i][j]
                # thêm số 0 vào cuối
                dp0[j] = dp0_prev[j] + dp1_prev[j]

                # trừ trường hợp vượt limit số 0 liên tiếp
                if old1 is not None:
                    dp0[j] -= old1[j]

                dp0[j] %= mod

                # tính dp1[i][j]
                # thêm số 1 vào cuối
                dp1[j] = dp0[j - 1] + dp1[j - 1]

                # trừ trường hợp vượt limit số 1 liên tiếp
                if j >= L:
                    dp1[j] -= dp0[j - L]

                dp1[j] %= mod

            # thêm hàng dp1 hiện tại vào queue
            dp1q.append(dp1[:])

            # chỉ giữ tối đa L hàng
            if len(dp1q) > L:
                dp1q.popleft()

            # cập nhật hàng trước
            dp0_prev = dp0
            dp1_prev = dp1

        # kết quả = chuỗi kết thúc bằng 0 hoặc 1
        return (dp0_prev[one] + dp1_prev[one]) % mod


# ---

# # 6. Độ phức tạp

# Time:

# ```
# O(zero × one)
# ```

# Space:

# ```
# O(one × limit)
# ```

# (nhỏ hơn nhiều so với `O(zero × one)`)

# ---

# # 7. Trực giác quan trọng nhất của bài

# Phần **khó nhất** là:

# ```
# - dp1[i-L][j]
# - dp0[i][j-L]
# ```

# Đây là kỹ thuật:

# > **Prefix DP để tránh L+1 phần tử giống nhau liên tiếp**

# Nếu bạn muốn, mình có thể giải thích **trực quan bằng ví dụ nhỏ (limit = 2)** để bạn **hiểu ngay vì sao phải trừ `i-L`** — đây là phần giúp hiểu **DP nâng cao rất nhanh.**




# // Mình sẽ**giải thích thuật toán trước**,sau đó đưa**code hoàn chỉnh có`main`,`Scanner`và chú thích chi tiết**.

# // ---

# // #1. Ý tưởng thuật toán(Dynamic Programming)

# // Ta cần**đếm số binary arrays**thỏa mãn:

# // *có`zero`số**0***có`one`số**1*****không quá`limit`số giống nhau liên tiếp**

# // ---

# // ##Trạng thái DP

# // Ta dùng**2 bảng DP**:

# // ```dp0[i][j]dp1[i][j]```

# // ###dp0[i][j]

# // Số cách tạo mảng:

# // ```i số 0 j số 1 và phần tử cuối là 0```

# // ---

# // ###dp1[i][j]

# // Số cách tạo mảng:

# // ```i số 0 j số 1 và phần tử cuối là 1```

# // ---

# // #2. Khởi tạo base case

# // Nếu chỉ có**0**

# // ```0 00 000```

# // Nhưng**không được vượt limit**

# // ```for(i<=limit)dp0[i][0]=1```

# // ---

# // Tương tự nếu chỉ có**1**

# // ```1 11 111```

# // ```for(j<=limit)dp1[0][j]=1```

# // ---

# // #3. Công thức chuyển trạng thái

# // ##Tính dp0[i][j]

# // Nếu chuỗi**kết thúc bằng 0**

# // Ta có thể thêm`0`vào:

# // ```dp0[i-1][j]dp1[i-1][j]```

# // nhưng phải**tránh>limit số 0 liên tiếp**

# // →nên phải**trừ trường hợp vi phạm**

# // ```dp1[i-L][j]```

# // với

# // ```L=limit+1```

# // Công thức:

# // ```dp0[i][j]=dp0[i-1][j]+dp1[i-1][j]-dp1[i-L][j]```

# // ---

# // ##Tính dp1[i][j]

# // Tương tự:

# // ```dp1[i][j]=dp1[i][j-1]+dp0[i][j-1]-dp0[i][j-L]```

# // ---

# // #4. Kết quả cuối

# // Chuỗi có thể kết thúc bằng:

# // ```0 hoặc 1```

# // nên:

# // ```answer=dp0[zero][one]+dp1[zero][one]```

# // ---

# // #5. Độ phức tạp

# // Time:

# // ```O(zero×one)```

# // Space:

# // ```O(zero×one)```

# // ---

# // #6. Code hoàn chỉnh(có`main`,`Scanner`,chú thích)

# // ```java

# import java.util.*;

# public class b211 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         // nhập số lượng 0
#         int zero = sc.nextInt();

#         // nhập số lượng 1
#         int one = sc.nextInt();

#         // nhập giới hạn số phần tử giống nhau liên tiếp
#         int limit = sc.nextInt();

#         int result = numberOfStableArrays(zero, one, limit);

#         System.out.println(result);

#         sc.close();
#     }

#     public static int numberOfStableArrays(int zero, int one, int limit) {

#         final int mod = 1_000_000_007;

#         // L = limit + 1 để kiểm tra trường hợp vượt quá limit
#         int L = limit + 1;

#         // dp0[i][j] = số cách tạo mảng có i số 0, j số 1 và kết thúc bằng 0
#         int[][] dp0 = new int[zero + 1][one + 1];

#         // dp1[i][j] = số cách tạo mảng có i số 0, j số 1 và kết thúc bằng 1
#         int[][] dp1 = new int[zero + 1][one + 1];

#         // Base case: chỉ có số 0
#         // Chỉ hợp lệ nếu số lượng không vượt limit
#         for (int i = 1; i <= Math.min(zero, limit); i++) {
#             dp0[i][0] = 1;
#         }

#         // Base case: chỉ có số 1
#         for (int j = 1; j <= Math.min(one, limit); j++) {
#             dp1[0][j] = 1;
#         }

#         // Duyệt qua tất cả trạng thái
#         for (int i = 1; i <= zero; i++) {
#             for (int j = 1; j <= one; j++) {

#                 // Tính dp0[i][j]
#                 // thêm số 0 vào cuối
#                 dp0[i][j] = dp0[i - 1][j] + dp1[i - 1][j];

#                 // trừ trường hợp vượt limit số 0 liên tiếp
#                 if (i >= L) {
#                     dp0[i][j] -= dp1[i - L][j];
#                 }

#                 dp0[i][j] %= mod;

#                 // Tính dp1[i][j]
#                 // thêm số 1 vào cuối
#                 dp1[i][j] = dp1[i][j - 1] + dp0[i][j - 1];

#                 // trừ trường hợp vượt limit số 1 liên tiếp
#                 if (j >= L) {
#                     dp1[i][j] -= dp0[i][j - L];
#                 }

#                 dp1[i][j] %= mod;

#                 // tránh số âm
#                 dp0[i][j] = (dp0[i][j] + mod) % mod;
#                 dp1[i][j] = (dp1[i][j] + mod) % mod;
#             }
#         }

#         // kết quả = chuỗi kết thúc bằng 0 hoặc 1
#         return (dp0[zero][one] + dp1[zero][one]) % mod;
#     }
# }

# // ---

# // #7.

# // Ví dụ
# // chạy chương
# // trình

# // Input

# // ```2 1 2```

# // Output

# // ```3```

# // Các mảng:

# // ```001 010 100```

# // ---

# // Nếu bạn
# // muốn mình
# // giải thích thêm**vì sao
# // phải trừ`dp1[i-L][j]`(đây là
# // phần khó
# // nhất của bài)**
# // mình có
# // thể minh họa**
# // bằng hình+
# // ví dụ nhỏ**,
# // hiểu xong
# // sẽ thấy
# // DP này
# // rất đẹp.

# // ---

# // ## 1. Binary Array là gì?

# // **Binary array** là mảng chỉ chứa **0 và 1**.

# // Ví dụ:

# // ```
# // [0,1,0,1]
# // [1,1,0]
# // [0,0,0,1]
# // ```

# // ---

# // ## 2. Input của bài

# // Bài cho 3 số:

# // ```
# // zero = số lượng số 0
# // one = số lượng số 1
# // limit = số phần tử giống nhau tối đa được đứng liên tiếp
# // ```

# // ---

# // ## 3. Stable nghĩa là gì?

# // Một **binary array được gọi là stable nếu:**

# // > Không có **hơn `limit` số giống nhau đứng liên tiếp**.

# // Ví dụ:

# // ### limit = 2

# // Hợp lệ:

# // ```
# // 0 0 1 1 0
# // 1 0 1 1
# // 0 1 0 1
# // ```

# // Không hợp lệ:

# // ```
# // 0 0 0 1 (3 số 0 liên tiếp > limit)
# // 1 1 1 0 (3 số 1 liên tiếp > limit)
# // ```

# // ---

# // ## 4. Yêu cầu bài toán

# // Bạn phải:

# // > **Đếm số lượng binary arrays khác nhau** thỏa mãn:

# // 1️⃣ Có đúng `zero` số **0**
# // 2️⃣ Có đúng `one` số **1**
# // 3️⃣ Không có quá `limit` số giống nhau đứng liên tiếp

# // ---

# // ## 5. Ví dụ

# // ### Ví dụ 1

# // ```
# // zero = 1
# // one = 1
# // limit = 2
# // ```

# // Các mảng có thể tạo:

# // ```
# // [0,1]
# // [1,0]
# // ```

# // Kết quả:

# // ```
# // 2
# // ```

# // ---

# // ### Ví dụ 2

# // ```
# // zero = 2
# // one = 1
# // limit = 2
# // ```

# // Các mảng:

# // ```
# // 0 0 1
# // 0 1 0
# // 1 0 0
# // ```

# // Kiểm tra:

# // ```
# // 0 0 1 ✔
# // 0 1 0 ✔
# // 1 0 0 ✔
# // ```

# // Tất cả hợp lệ

# // Kết quả:

# // ```
# // 3
# // ```

# // ---

# // ### Ví dụ 3

# // ```
# // zero = 3
# // one = 1
# // limit = 2
# // ```

# // Possible arrays:

# // ```
# // 0 0 1 0 ✔
# // 0 1 0 0 ✔
# // 1 0 0 0 ❌ (3 số 0 liên tiếp > limit)
# // ```

# // Kết quả:

# // ```
# // 2
# // ```

# // ---

# // ## 6. Ý tưởng bài toán

# // Bài này thực chất là:

# // > **Đếm số cách sắp xếp 0 và 1 với ràng buộc số lượng liên tiếp**

# // Ta cần theo dõi:

# // * còn bao nhiêu **0**
# // * còn bao nhiêu **1**
# // * trước đó là **0 hay 1**
# // * đã dùng **bao nhiêu số giống nhau liên tiếp**

# // → nên thường giải bằng **Dynamic Programming (DP)**.

# // ---

# // ## 7. Tóm tắt đề bài (rất quan trọng)

# // Cho:

# // ```
# // zero = số 0
# // one = số 1
# // limit = tối đa số giống nhau liên tiếp
# // ```

# // Hỏi:

# // > Có **bao nhiêu binary arrays** có **zero số 0** và **one số 1** mà **không
# // có quá limit phần tử giống nhau đứng liên tiếp**.

# // ---

# // Nếu bạn muốn, mình có thể giải tiếp:

# // * **Cách nghĩ để giải bài này (intuition)**
# // * **DP state là gì**
# // * **Code Java / Python**
# // * **Cách tối ưu từ O(n⁴) → O(n²)**

# // Chỉ cần nói **“giải thích cách nghĩ bài này”** là mình sẽ phân tích từng bước
# // rất dễ hiểu.
