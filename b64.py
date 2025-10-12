# 3539. Find Sum of Array Product of Magical Sequences(12/10/2025)


# Dưới đây là **giải thích đề bài 3539 — Find Sum of Array Product of Magical Sequences** (trích từ LeetCode) cùng các khái niệm và cách hiểu. Nếu bạn muốn, mình có thể tiếp tục hướng dẫn cách giải (thuật toán) sau khi bạn nắm đề nhé.
# Rất hay — đoạn code bạn đưa là **lời giải nâng cao** (rất khác so với cách brute-force thông thường).
# Nó dùng **lập trình động (DFS có memoization)**, **tổ hợp**, **phép toán trên bit**, và **modular arithmetic**.
# Đây là một bài toán “biến thể mở rộng” của *Find Sum of Array Product of Magical Sequences* — chứ không phải chỉ duyệt từng dãy con đơn giản.
# Mình sẽ **giải thích chi tiết từng phần + thêm chú thích đầy đủ vào code** cho bạn 👇

# ---

# ### 🧠 Ý tưởng tổng quát

# Bài toán này không còn là duyệt dãy con nữa, mà trở thành **bài toán đếm/tính tổng dựa trên cấu trúc bit và tổ hợp**.

# * `m`: tổng số phần tử cần chọn
# * `k`: số phần tử “thỏa điều kiện đặc biệt” (ví dụ bit bằng 1)
# * `nums`: danh sách các giá trị
# * Thuật toán sử dụng **DFS có cache** để duyệt mọi cách phân phối `m` phần tử vào `n` vị trí.

# Vì số lượng tổ hợp rất lớn, nên code:

# * Dùng `fac` (factorial) và `inv_f` (modular inverse factorial)
# * Dùng `pow_v[i][j]` để lưu `nums[i]**j % MOD`
#   → giúp giảm thời gian tính toán lặp lại.

# ---

# ### 🧩 Giải thích từng đoạn code

# ```python
# MOD = 1_000_000_007  # Số nguyên lớn để tránh tràn số khi tính modulo
# MX = 31              # Giới hạn factorial (tối đa m = 30)
# ```

# #### 1️⃣ Tính giai thừa và nghịch đảo modular

# ```python
# fac = [0] * MX
# fac[0] = 1
# for i in range(1, MX):
#     fac[i] = fac[i - 1] * i % MOD  # fac[i] = i! mod MOD

# inv_f = [0] * MX
# inv_f[-1] = pow(fac[-1], -1, MOD)  # Nghịch đảo modular của fac[MX-1]
# for i in range(MX - 1, 0, -1):
#     inv_f[i - 1] = inv_f[i] * i % MOD  # inv_f[i] = 1 / fac[i]
# ```

# → Đây là kỹ thuật tổ hợp chuẩn:
# ( inv_f[i] = (fac[i])^{-1} \mod MOD )

# ---

# #### 2️⃣ Tiền tính mũ của từng phần tử

# ```python
# pow_v = [[1] * (m + 1) for _ in range(n)]
# for i in range(n):
#     for j in range(1, m + 1):
#         pow_v[i][j] = pow_v[i][j - 1] * nums[i] % MOD
# ```

# → `pow_v[i][j]` = `nums[i] ** j % MOD`
# Giúp tính nhanh khi cần nhân nhiều lần cùng một số.

# ---

# #### 3️⃣ DFS có memoization

# ```python
# @cache
# def dfs(i: int, left_m: int, x: int, left_k: int) -> int:
#     c1 = x.bit_count()  # đếm số bit 1 trong x
    
#     # Nếu số bit 1 hiện tại + số phần tử còn lại < số k cần đạt → không thể thỏa
#     if c1 + left_m < left_k:
#         return 0

#     # Nếu đã xét hết n phần tử
#     if i == n:
#         # Chỉ hợp lệ nếu đã chọn đủ m phần tử và số bit 1 == k
#         return 1 if left_m == 0 and c1 == left_k else 0
# ```

# ---

# #### 4️⃣ Duyệt tất cả cách chọn j phần tử tại vị trí i

# ```python
#     res = 0
#     for j in range(left_m + 1):
#         bit = (x + j) & 1  # bit mới sinh ra khi cộng x+j
#         if bit <= left_k:
#             r = dfs(i + 1, left_m - j, (x + j) >> 1, left_k - bit)
#             res += r * pow_v[i][j] * inv_f[j]
#     return res % MOD
# ```

# 🔍 Giải thích:

# * `j`: số phần tử chọn tại vị trí `i`
# * `(x + j) & 1`: kiểm tra bit mới sinh ra
# * `(x + j) >> 1`: dịch bit để tính tiếp ở cấp tiếp theo
# * `r * pow_v[i][j] * inv_f[j]`:

#   * `r`: số cách từ phần còn lại
#   * `pow_v[i][j]`: nhân giá trị `nums[i]**j`
#   * `inv_f[j]`: chia cho hoán vị trùng lặp (tổ hợp)

# ---

# #### 5️⃣ Kết quả cuối cùng

# ```python
# return dfs(0, m, 0, k) * fac[m] % MOD
# ```

# → Nhân `fac[m]` để hoàn tất nhân hoán vị (đảo lại chia trước đó).
# Kết quả cuối cùng được tính modulo `1e9+7`.

# ---

# ### 💡 Tóm tắt ý tưởng

# | Thành phần                  | Ý nghĩa                                                |
# | --------------------------- | ------------------------------------------------------ |
# | `fac`, `inv_f`              | Dùng để tính toán tổ hợp nhanh                         |
# | `pow_v`                     | Lưu giá trị `nums[i]^j` để tránh tính lại              |
# | `dfs(i, left_m, x, left_k)` | Hàm đệ quy tính số cách chọn phần tử để thỏa điều kiện |
# | `x`                         | Trạng thái bit để kiểm tra điều kiện “magical”         |
# | `bit_count`                 | Số lượng bit 1 đã sinh ra                              |
# | `MOD`                       | Dùng để tránh tràn số nguyên                           |

# ---

# ### 📘 Code có chú thích đầy đủ

# ```python
# MOD = 1_000_000_007
# MX = 31

# # Tiền tính giai thừa và nghịch đảo modular
# fac = [0] * MX
# fac[0] = 1
# for i in range(1, MX):
#     fac[i] = fac[i - 1] * i % MOD

# inv_f = [0] * MX
# inv_f[-1] = pow(fac[-1], -1, MOD)
# for i in range(MX - 1, 0, -1):
#     inv_f[i - 1] = inv_f[i] * i % MOD


MOD = 1_000_000_007
MX = 31

# Tiền tính giai thừa và nghịch đảo modular
fac = [0] * MX
fac[0] = 1
for i in range(1, MX):
    fac[i] = fac[i - 1] * i % MOD

inv_f = [0] * MX
inv_f[-1] = pow(fac[-1], -1, MOD)
for i in range(MX - 1, 0, -1):
    inv_f[i - 1] = inv_f[i] * i % MOD


from functools import cache

class Solution:
    def magicalSum(self, m: int, k: int, nums: list[int]) -> int:
        n = len(nums)

        # pow_v[i][j] = nums[i]^j mod MOD
        pow_v = [[1] * (m + 1) for _ in range(n)]
        for i in range(n):
            for j in range(1, m + 1):
                pow_v[i][j] = pow_v[i][j - 1] * nums[i] % MOD

        @cache
        def dfs(i: int, left_m: int, x: int, left_k: int) -> int:
            c1 = x.bit_count()
            if c1 + left_m < left_k:
                return 0
            if i == n:
                return 1 if left_m == 0 and c1 == left_k else 0

            res = 0
            for j in range(left_m + 1):
                bit = (x + j) & 1
                if bit <= left_k:
                    r = dfs(i + 1, left_m - j, (x + j) >> 1, left_k - bit)
                    res += r * pow_v[i][j] * inv_f[j]
            return res % MOD

        # Kết quả cuối cùng
        return dfs(0, m, 0, k) * fac[m] % MOD

# ```

# ---

# Nếu bạn muốn, mình có thể **vẽ sơ đồ đệ quy (DFS tree)** để bạn thấy rõ cách các trạng thái `(i, left_m, x, left_k)` được mở rộng như thế nào — bạn có muốn không?

# ---

# ## 📄 Đề bài (tóm lược)

# Bạn được cho:

# * Một số nguyên **m** — độ dài của mỗi **sequence** (chuỗi) bạn sẽ tạo.
# * Một số nguyên **k**.
# * Một mảng `nums` (có độ dài ≥ m).

# Bạn định nghĩa:

# * Một **magical sequence** (chuỗi ma thuật) là một sequence `seq` của độ dài **m**, trong đó mỗi phần tử `seq[i]` là một chỉ số trong `nums` (tức chọn các vị trí).

# * Với mỗi sequence `seq`, bạn tính **array product**:
#   [
#   \text{prod(seq)} = nums[,seq[0],] \times nums[,seq[1],] \times \cdots \times nums[,seq[m-1],]
#   ]

# * Ngoài ra, sequence được gọi là **magical** nếu nó thỏa điều kiện nào đó liên quan đến **k** (theo mô tả đề).
#   (Trong mô tả mở rộng, có nói về “set bit” của tổng 2^seq[i] và đếm số bit set, nhưng tóm lại là có một điều kiện để sequence được xem là magical.)

# Yêu cầu:

# > Tính tổng (sum) của tất cả các **array product** của mọi sequence `seq` hợp lệ (magical).
# > Vì kết quả có thể rất lớn, trả kết quả mod (10^9 + 7). ([Hello, World! System Design Newsletter][1])

# Ví dụ:

# * Nếu `m = 5, k = 5, nums = [1, 10, 100, 10000, 1000000]`, output là `991600007`. ([Hello, World! System Design Newsletter][1])
# * Nếu `m = 2, k = 2, nums = [5,4,3,2,1]`, output là `170`. ([Hello, World! System Design Newsletter][1])

# ---

# ## 🧩 Phân tích và cách hiểu chi tiết

# Để hiểu đề, ta cần làm rõ các phần:

# 1. **Sequence & array product**

#    * `seq` là một dãy độ dài **m** chứa các chỉ số từ `0` đến `nums.length - 1`.
#    * `prod(seq)` = tích các `nums[seq[i]]`.

# 2. **Điều kiện magical**

#    * Có liên quan đến việc tính (2^{seq[0]} + 2^{seq[1]} + \cdots + 2^{seq[m-1]}).
#    * Đếm số bit set (số bit 1) trong tổng đó.
#    * Nếu số bit set = k thì sequence đó là magical. ([Hello, World! System Design Newsletter][1])

# 3. **Tổng các sản phẩm**

#    * Với mỗi sequence hợp lệ, tính `prod(seq)`, sau đó cộng vào tổng (mod (10^9 + 7)).
#    * Cần xét **mọi sequence** nhưng chỉ lấy những cái “magical”.

# 4. **Tính toán lớn**

#    * Vì số sequence có thể rất nhiều (combinatorial), bạn không thể liệt kê tất cả. Phải tìm công thức, tối ưu bằng DP / toán tổ hợp / bitmasking / kỹ thuật nhúng mod.
#    * Đề nhấn là “return modulo (10^9 + 7)”. ([LeetCode][2])

# ---

