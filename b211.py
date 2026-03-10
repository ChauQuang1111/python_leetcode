# Bài **“Find All Possible Stable Binary Arrays II”** ( 10/03/2026)

# Mình sẽ **giải thích ý tưởng thuật toán** trước, sau đó **viết lại code của bạn với comment chi tiết** để bạn hiểu từng dòng.

# ---

# # 1. Ý tưởng thuật toán

# Ta dùng **Dynamic Programming**.

# Định nghĩa:

# ```
# dp0[i][j] = số mảng stable dùng
#             i số 0
#             j số 1
#             và kết thúc bằng 0

# dp1[i][j] = số mảng stable dùng
#             i số 0
#             j số 1
#             và kết thúc bằng 1
# ```

# ---

# ## Quy tắc chuyển trạng thái

# ### 1️⃣ Thêm số 0

# Muốn mảng kết thúc bằng **0**

# Ta có thể:

# ```
# ...1 + 0
# ...0 + 0
# ```

# Nhưng **không được có hơn limit số 0 liên tiếp**.

# Vì vậy:

# ```
# dp0[i][j] =
#     dp0[i-1][j]      (thêm 0 vào chuỗi kết thúc bằng 0)
#   + dp1[i-1][j]      (thêm 0 vào chuỗi kết thúc bằng 1)
#   - dp1[i-limit-1][j] (loại trường hợp có limit+1 số 0 liên tiếp)
# ```

# ---

# ### 2️⃣ Thêm số 1

# Tương tự:

# ```
# dp1[i][j] =
#     dp0[i][j-1]
#   + dp1[i][j-1]
#   - dp0[i][j-limit-1]
# ```

# ---

# # 2. Vì sao dùng deque ?

# Ta cần truy cập:

# ```
# dp1[i-limit-1][j]
# ```

# → phải nhớ **limit+1 dòng trước**

# Nên dùng:

# ```
# deque
# ```

# để lưu **limit+1 hàng dp1 gần nhất**

# ---

# # 3. Tối ưu bộ nhớ

# Thay vì dùng:

# ```
# dp[1000][1000]
# ```

# Ta chỉ giữ:

# ```
# dp0_prev
# dp1_prev
# ```

# vì mỗi bước chỉ cần **hàng trước đó**.

# Memory giảm từ:

# ```
# O(n*m)
# → O(m)
# ```

# ---

# # 4. Code với chú thích chi tiết

# ```python
from collections import deque

def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
    
    mod = 10**9 + 7
    
    # L = limit + 1
    # dùng để kiểm tra khi vượt quá số lượng phần tử liên tiếp cho phép
    L = limit + 1

    # Nếu số 1 nhiều hơn số 0
    # ta swap để giảm bộ nhớ sử dụng
    if one > zero:
        zero, one = one, zero

    # dp0_prev[j] = số mảng dùng i-1 số 0 và j số 1
    # và kết thúc bằng 0
    dp0_prev = [0] * (one + 1)

    # dp1_prev[j] = số mảng dùng i-1 số 0 và j số 1
    # và kết thúc bằng 1
    dp1_prev = [0] * (one + 1)

    # ====== Khởi tạo hàng đầu tiên (i = 0) ======
    # chỉ có số 1

    for j in range(1, min(one, limit) + 1):
        dp1_prev[j] = 1
        # ví dụ:
        # 1
        # 11
        # 111
        # miễn là <= limit

    # queue lưu L dòng dp1 gần nhất
    # để truy cập dp1[i-L][j]
    dp1q = deque([dp1_prev[:]])

    # ====== duyệt số lượng 0 ======
    for i in range(1, zero + 1):

        # dp của hàng hiện tại
        dp0 = [0] * (one + 1)
        dp1 = [0] * (one + 1)

        # trường hợp chỉ có 0
        if i <= limit:
            dp0[0] = 1

        # ===== duyệt số lượng 1 =====
        for j in range(1, one + 1):

            # tính dp0[i][j]

            dp0[j] = (
                dp0_prev[j]          # thêm 0 vào chuỗi kết thúc 0
                + dp1_prev[j]        # thêm 0 vào chuỗi kết thúc 1
                - (dp1q[0][j] if i >= L else 0)  # loại chuỗi có limit+1 số 0
            ) % mod


            # tính dp1[i][j]

            dp1[j] = (
                dp0[j - 1]           # thêm 1 vào chuỗi kết thúc 0
                + dp1[j - 1]         # thêm 1 vào chuỗi kết thúc 1
                - (dp0[j - L] if j >= L else 0)  # loại chuỗi có limit+1 số 1
            ) % mod

        # lưu dòng dp1 vào queue
        dp1q.append(dp1[:])

        # nếu queue dài hơn limit+1
        # bỏ dòng cũ nhất
        if len(dp1q) > L:
            dp1q.popleft()

        # cập nhật prev cho vòng sau
        dp0_prev = dp0
        dp1_prev = dp1

    # kết quả = kết thúc bằng 0 hoặc 1
    return (dp0_prev[one] + dp1_prev[one]) % mod


# 5. Độ phức tạp

### Time

# ```
# O(zero × one)
# ```

# max:

# ```
# 1000 × 1000 = 10^6
# ```

# → chạy nhanh

# ---

# ### Space

# ```
# O(one)
# ```

# vì chỉ lưu **1 hàng**

# ---

# 💡 Nếu bạn muốn, mình có thể giải thích thêm:

# * **intuition cực dễ hiểu (tại sao phải trừ dp[i-limit-1])**
# * **dry run từng bước với ví dụ nhỏ**
# * **so sánh bài I vs II**
# * **cách nghĩ ra thuật toán này khi đi phỏng vấn** (rất hay hỏi).


# ---

# ## 1. Input của bài

# Bạn được cho **3 số nguyên**:

# * `zero` : số lượng **số 0** phải dùng trong mảng
# * `one` : số lượng **số 1** phải dùng trong mảng
# * `limit` : **không được có quá `limit` số giống nhau liên tiếp**

# ---

# ## 2. Stable Binary Array là gì?

# Một **binary array** là mảng chỉ gồm:

# ```
# 0 và 1
# ```

# Một **stable binary array** trong bài này là mảng thỏa:

# 1. Có đúng `zero` số **0**
# 2. Có đúng `one` số **1**
# 3. Không có **hơn `limit` số giống nhau liên tiếp**

# ---

# ## 3. Ví dụ dễ hiểu

# ### Ví dụ 1

# ```
# zero = 1
# one = 1
# limit = 2
# ```

# Ta cần mảng dài:

# ```
# 1 + 1 = 2
# ```

# Các mảng có thể tạo:

# ```
# [0,1]
# [1,0]
# ```

# Không có mảng nào vi phạm limit.

# → **Kết quả = 2**

# ---

# ### Ví dụ 2

# ```
# zero = 3
# one = 1
# limit = 2
# ```

# Tổng độ dài:

# ```
# 4
# ```

# Ta phải dùng:

# ```
# 0,0,0,1
# ```

# Nhưng **không được có hơn 2 số giống nhau liên tiếp**

# Xét các cách:

# ```
# 0001 ❌ (3 số 0 liên tiếp > limit)
# 0010 ❌
# 0100 ❌
# 1000 ❌
# ```

# Không có cách hợp lệ.

# → **Kết quả = 0**

# ---

# ### Ví dụ 3

# ```
# zero = 2
# one = 1
# limit = 2
# ```

# Các mảng có thể:

# ```
# 001  (2 số 0 liên tiếp OK)
# 010
# 100
# ```

# → **3 mảng hợp lệ**

# ---

# ## 4. Tóm tắt đề bài

# Bạn phải:

# 1️⃣ Tạo tất cả mảng gồm `zero` số 0 và `one` số 1
# 2️⃣ Không được có quá `limit` số giống nhau liên tiếp
# 3️⃣ **Đếm số lượng mảng hợp lệ**
# 4️⃣ Vì số có thể rất lớn → trả về **mod 1e9 + 7**

# ---

# ## 5. Vì sao bài này khó (II)?

# Phiên bản **II** khó vì:

# * `zero` và `one` có thể **rất lớn (~1000)**
# * Không thể **brute force sinh tất cả mảng**

# → phải dùng:

# * **Dynamic Programming**
# * hoặc **DP + prefix sum optimization**

# ---

# ✅ **Ý tưởng chính của bài:**

# DP theo:

# ```
# dp[i][j][last]
# ```

# * `i` = số 0 đã dùng
# * `j` = số 1 đã dùng
# * `last` = số cuối là 0 hay 1

# ---

# 💡 Nếu bạn muốn mình giải tiếp:

# * **intuition của DP**
# * **cách nghĩ để ra công thức**
# * **code Java / Python**
# * **tối ưu từ bài I → II**

# Mình có thể giải **từng bước rất dễ hiểu (giống cách phỏng vấn FAANG)**.
