# 1716. Calculate Money in Leetcode Bank(25/10/2025)
# Rất hay 👏 — đây là một bài LeetCode khá cơ bản nhưng dễ nhầm nếu không để ý đến quy luật tăng dần.
# Cùng phân tích kỹ **đề bài 1716. Calculate Money in Leetcode Bank** nhé.
class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7

        # Tổng tiền trong các tuần đầy đủ
        total = 0
        for i in range(weeks):
            total += 28 + i * 7  # 28 là tổng tuần đầu, mỗi tuần tăng thêm 7

        # Tổng tiền trong các ngày dư
        start = weeks + 1
        for i in range(days):
            total += start + i

        return total

# ---

# ## 🧩 **Đề bài**

# Bạn có một cái **ngân hàng đặc biệt** hoạt động theo quy luật sau:

# * Mỗi **tuần** có 7 ngày (thứ Hai → Chủ Nhật).
# * Vào **thứ Hai của tuần đầu tiên**, bạn gửi **1 đô la**.
# * Mỗi **ngày sau trong tuần**, bạn gửi **nhiều hơn hôm trước 1 đô**.
#   👉 Nghĩa là:

#   ```
#   Tuần 1: 1, 2, 3, 4, 5, 6, 7   → tổng 28
#   ```
# * Sang **tuần tiếp theo**, bạn lại bắt đầu từ số tiền lớn hơn **1 đô so với thứ Hai tuần trước**.

#   👉 Nghĩa là:

#   ```
#   Tuần 2: 2, 3, 4, 5, 6, 7, 8   → tổng 35
#   Tuần 3: 3, 4, 5, 6, 7, 8, 9   → tổng 42
#   ...
#   ```

# Bạn được cho một số nguyên `n` là **số ngày**.
# Hãy tính **tổng số tiền** bạn đã gửi sau `n` ngày.

# ---

# ## 💡 **Ví dụ minh họa**

# ### 🧮 Ví dụ 1:

# ```
# Input: n = 4
# ```

# Tuần đầu tiên (7 ngày):
# Ngày 1: 1
# Ngày 2: 2
# Ngày 3: 3
# Ngày 4: 4

# Tổng sau 4 ngày = `1 + 2 + 3 + 4 = 10`

# ✅ Output: `10`

# ---

# ### 🧮 Ví dụ 2:

# ```
# Input: n = 10
# ```

# * Tuần 1: `1 2 3 4 5 6 7` → tổng 28
# * Tuần 2: chỉ có 3 ngày đầu (vì tổng 10 ngày) → `2 3 4` → tổng 9

# → Tổng cộng: `28 + 9 = 37`

# ✅ Output: `37`

# ---

# ### 🧮 Ví dụ 3:

# ```
# Input: n = 20
# ```

# * Tuần 1: 1 2 3 4 5 6 7 → 28
# * Tuần 2: 2 3 4 5 6 7 8 → 35
# * Tuần 3: 3 4 5 6 7 8 9 → 42  (chỉ cần 6 ngày thôi: 3,4,5,6,7,8)

# Tổng 6 ngày tuần 3 = 3 + 4 + 5 + 6 + 7 + 8 = 33

# → Tổng cộng: `28 + 35 + 33 = 96`

# ✅ Output: `96`

# ---

# ## 🧠 **Cách tính nhanh (ý tưởng chính)**

# 1. Số tuần đầy đủ:

#    ```python
#    weeks = n // 7
#    ```

# 2. Số ngày dư (không đủ 1 tuần):

#    ```python
#    days = n % 7
#    ```

# 3. Mỗi tuần bắt đầu từ giá trị tăng dần (1, 2, 3, …).

#    Tổng 1 tuần = `7 * start + (1 + 2 + … + 6)`
#    = `7 * start + 21`

# 4. Cộng dồn các tuần + phần dư.

# ---

# ## 💻 **Code mẫu (Python)**

# ```python
# class Solution:
#     def totalMoney(self, n: int) -> int:
#         weeks = n // 7
#         days = n % 7

#         # Tổng tiền trong các tuần đầy đủ
#         total = 0
#         for i in range(weeks):
#             total += 28 + i * 7  # 28 là tổng tuần đầu, mỗi tuần tăng thêm 7

#         # Tổng tiền trong các ngày dư
#         start = weeks + 1
#         for i in range(days):
#             total += start + i

#         return total
# ```

# ---

# ## ⚙️ **Độ phức tạp**

# * ⏱️ `O(1)` (vì có thể tính công thức trực tiếp hoặc `O(n)` nếu dùng vòng lặp ngắn)
# * 💾 `O(1)` bộ nhớ

# ---

# Bạn có muốn mình viết luôn **phiên bản Java** của lời giải này + chú thích từng dòng không?
# Tuyệt vời 👍 — cùng mình **giải thích chi tiết thuật toán** của bài
# **LeetCode 1716. Calculate Money in Leetcode Bank** nhé.

# ---

# ## 🎯 **Mục tiêu của bài**

# Bạn phải tính tổng tiền sau `n` ngày gửi tiết kiệm,
# theo quy luật tăng dần từng ngày và từng tuần như sau:

# | Tuần | Thứ Hai bắt đầu | Số tiền mỗi ngày | Tổng tuần |
# | ---- | --------------- | ---------------- | --------- |
# | 1    | 1               | 1,2,3,4,5,6,7    | 28        |
# | 2    | 2               | 2,3,4,5,6,7,8    | 35        |
# | 3    | 3               | 3,4,5,6,7,8,9    | 42        |
# | …    | …               | …                | …         |

# Mỗi tuần tăng thêm **1 đô la ở ngày đầu tiên** so với tuần trước.

# ---

# ## 🧠 **Ý tưởng thuật toán**

# ### Bước 1️⃣: Chia tổng số ngày `n` thành **tuần đầy đủ** và **ngày dư**

# Ví dụ:

# ```
# n = 20
# ```

# → Mỗi tuần có 7 ngày
# → Ta chia ra:

# ```python
# weeks = n // 7 = 2
# days = n % 7 = 6
# ```

# Tức là có **2 tuần đầy đủ**, và **6 ngày tuần thứ 3**.

# ---

# ### Bước 2️⃣: Tính tổng tiền của các **tuần đầy đủ**

# * Tuần 1 bắt đầu từ 1 đô
#   → tổng = 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28

# * Tuần 2 bắt đầu từ 2 đô
#   → tổng = 2 + 3 + 4 + 5 + 6 + 7 + 8 = 35

# * Tuần 3 bắt đầu từ 3 đô
#   → tổng = 3 + 4 + 5 + 6 + 7 + 8 + 9 = 42

# Nhận thấy:

# > Mỗi tuần tăng thêm **7 đô** so với tuần trước
# > (vì mỗi ngày tăng thêm 1, có 7 ngày → 7 đô).

# → Công thức tổng 1 tuần thứ `i` (tính từ 0):

# ```
# sum_week_i = 28 + 7 * i
# ```

# Tổng tất cả các tuần đầy đủ:

# ```
# total = 28 + (28 + 7) + (28 + 14) + ... + (28 + 7*(weeks-1))
# ```

# ---

# ### Bước 3️⃣: Tính tổng tiền của **các ngày dư**

# Tuần sau cùng bắt đầu từ `(weeks + 1)` đô.

# Ví dụ `weeks = 2`
# → Tuần 3 bắt đầu từ 3 đô.
# Nếu còn `days = 6`, thì ta cộng:

# ```
# 3 + 4 + 5 + 6 + 7 + 8 = 33
# ```

# Công thức:

# ```python
# start = weeks + 1
# for i in range(days):
#     total += start + i
# ```

# ---

# ### Bước 4️⃣: Trả về tổng

# ```python
# return total
# ```

# ---

# ## 💡 **Ví dụ chạy chi tiết**

# ### Input:

# ```
# n = 20
# ```

# 1️⃣ weeks = 2
# 2️⃣ days = 6

# * Tuần 1: 28
# * Tuần 2: 35
# * Tuần 3 (6 ngày): 3 + 4 + 5 + 6 + 7 + 8 = 33

# 👉 Tổng = 28 + 35 + 33 = **96**

# ✅ Output: `96`

# ---

# ## 📊 **Độ phức tạp**

# * ⏱️ Thời gian: `O(weeks + days)` (rất nhỏ, ≤ n)
# * 💾 Bộ nhớ: `O(1)`

# ---

# Nếu bạn muốn, mình có thể viết lại **phiên bản Java** của thuật toán này,
# và **minh họa từng vòng lặp chạy ra giá trị cụ thể** nhé — bạn muốn mình làm không?
