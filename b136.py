# Number of Ways to Paint N × 3 Grid(03/01/2026)
# Mình **giải thích đề bài “Number of Ways to Paint N × 3 Grid” bằng tiếng Việt, theo kiểu dễ hiểu nhất**, không đi vào code vội nhé.
# OK 👍 Mình **giải thích thuật toán + thêm chú thích trực tiếp vào code**, từng dòng một, để bạn nhìn vào là hiểu ngay bài **LeetCode 1411**.

# ---

# ## 1️⃣ Ý nghĩa của `x` và `y`

# Trong bài này, ta **không xét từng ô**, mà xét **từng hàng (3 ô)**.

# Ta chia các cách tô **mỗi hàng** thành **2 loại**:

# ### 🔹 `x` – số cách kiểu **ABA** (2 màu)

# Ví dụ:

# ```
# Đỏ – Xanh – Đỏ
# ```

# ### 🔹 `y` – số cách kiểu **ABC** (3 màu khác nhau)

# Ví dụ:

# ```
# Đỏ – Xanh – Vàng
# ```

# ---

# ## 2️⃣ Khởi tạo ban đầu

# ```python
# x = 0   # số cách với kiểu ABA
# y = 3   # số cách với kiểu ABC
# ```

# Tại sao `y = 3`?

# ➡ Khi **chưa có hàng nào**, ta coi như có **3 cách khởi đầu** để xây dựng hàng đầu tiên
# (sau vòng lặp đầu tiên, số lượng sẽ đúng với N = 1)

# 👉 Đây là một **mẹo khởi tạo** thường dùng trong bài này.

# ---

# ## 3️⃣ Công thức chuyển trạng thái (quan trọng nhất)

# ### 🔁 Mỗi vòng lặp = thêm **1 hàng**

# ```python
# for _ in range(n):
# ```

# ---

# ### 🧠 Công thức:

# ```python
# x_new = 3*x + 2*y
# y_new = 2*x + 2*y
# ```

# ---

# ## 4️⃣ Giải thích từng công thức

# ### 🔸 `x_new = 3*x + 2*y`

# Số cách tạo **hàng mới kiểu ABA**:

# #### ✔ Từ hàng cũ cũng là ABA (`x`)

# * Có **3 cách** tô hàng dưới sao cho vẫn là ABA và không trùng màu theo cột

# 👉 đóng góp: `3 * x`

# ---

# #### ✔ Từ hàng cũ là ABC (`y`)

# * Có **2 cách** chuyển sang ABA

# 👉 đóng góp: `2 * y`

# ---

# ### 🔸 `y_new = 2*x + 2*y`

# Số cách tạo **hàng mới kiểu ABC**:

# #### ✔ Từ ABA → ABC

# * Có **2 cách hợp lệ**

# 👉 `2 * x`

# #### ✔ Từ ABC → ABC

# * Có **2 cách hợp lệ**

# 👉 `2 * y`

# ---

# ## 5️⃣ Code có chú thích đầy đủ

# ```python
class Solution:
    def numOfWays(self, n: int, x = 0, y = 3, mod = 1_000_000_007) -> int:
        # x: số cách tô hàng kiểu ABA (2 màu)
        # y: số cách tô hàng kiểu ABC (3 màu khác nhau)

        for _ in range(n):
            # Tính số cách mới cho hàng tiếp theo
            new_x = (3 * x + 2 * y) % mod  # ABA mới
            new_y = (2 * x + 2 * y) % mod  # ABC mới

            x, y = new_x, new_y  # cập nhật trạng thái

        # Tổng số cách = ABA + ABC
        return (x + y) % mod


## 6️⃣ Ví dụ nhanh để kiểm tra

### 🔹 n = 1

# Sau 1 vòng:

# * `x = 6`
# * `y = 6`

# 👉 tổng = **12** ✅

# ---

# ### 🔹 n = 2

# Kết quả = **54** ✅ (đúng đề)

# ---

# ## 7️⃣ Vì sao thuật toán này tối ưu?

# ✔ **Time**: `O(n)`
# ✔ **Space**: `O(1)`
# ✔ Không dùng mảng DP
# ✔ Chỉ giữ **2 biến**

# ---

# Nếu bạn muốn:

# * 🔥 Chứng minh chi tiết vì sao là **3,2,2,2**
# * 🔥 Vẽ bảng minh họa từng trường hợp
# * 🔥 Viết lại bằng **Java**

# 👉 cứ nói tiếp nhé 😄

# ---

# ## 1️⃣ Mô tả đề bài (hiểu bằng ngôn ngữ đời thường)

# * Bạn có **một cái bảng gồm N hàng và 3 cột** (N × 3).
# * Mỗi ô được sơn **1 trong 3 màu khác nhau** (thường là: đỏ – vàng – xanh).
# * **Luật sơn quan trọng**:

#   * ❌ Hai ô **kề nhau theo chiều ngang hoặc chiều dọc** **không được cùng màu**.
# * Nhiệm vụ của bạn là:

# > 👉 **Đếm số cách sơn hợp lệ** cho cả bảng.

# Kết quả thường yêu cầu **lấy modulo 1e9 + 7** (vì số rất lớn).

# ---

# ## 2️⃣ Ví dụ để dễ hình dung

# ### 🔹 Khi N = 1 (1 hàng, 3 cột)

# Chỉ có **1 hàng** như thế này:

# ```
# [ ] [ ] [ ]
# ```

# Điều kiện:

# * Ô 1 ≠ ô 2
# * Ô 2 ≠ ô 3

# 👉 Ta chỉ cần chọn 3 màu sao cho **3 ô liên tiếp không trùng màu**.

# ---

# ## 3️⃣ Ý tưởng cốt lõi của bài này

# Thay vì xét từng ô (rất phức tạp), người ta **xét theo từng hàng**.

# ### Với 1 hàng (3 ô), chỉ có **2 kiểu hợp lệ**:

# #### 🔸 Kiểu 1: **ABA** (2 màu)

# Ví dụ:

# ```
# Đỏ – Xanh – Đỏ
# ```

# * Ô 1 = ô 3
# * Ô 2 khác ô 1

# 👉 Gọi là **type A**

# ---

# #### 🔸 Kiểu 2: **ABC** (3 màu khác nhau)

# Ví dụ:

# ```
# Đỏ – Xanh – Vàng
# ```

# 👉 Gọi là **type B**

# ---

# ## 4️⃣ Đếm số cách cho 1 hàng

# ### 🧮 Type A (ABA):

# * Chọn màu cho A: **3 cách**
# * Chọn màu cho B (khác A): **2 cách**

# 👉 **3 × 2 = 6 cách**

# ---

# ### 🧮 Type B (ABC):

# * Chọn A: **3**
# * Chọn B (≠ A): **2**
# * Chọn C (≠ A, ≠ B): **1**

# 👉 **3 × 2 × 1 = 6 cách**

# ---

# ➡️ **Tổng cho N = 1 là: 12 cách**

# ---

# ## 5️⃣ Khi N ≥ 2 thì sao?

# Lúc này phải để ý thêm:

# * Ô **trên – dưới** cũng **không được cùng màu**.

# 👉 Vì vậy:

# * Một hàng **type A** ở trên sẽ **chuyển sang** type A hoặc B ở hàng dưới theo **quy luật nhất định**
# * Tương tự với **type B**

# 👉 Đây là lý do bài này dùng **Dynamic Programming (Quy hoạch động)**.

# ---

# ## 6️⃣ Trạng thái DP (chỉ cần hiểu, chưa cần code)

# Ta chỉ cần theo dõi:

# * `a[i]` = số cách sơn **i hàng**, hàng cuối là **type A**
# * `b[i]` = số cách sơn **i hàng**, hàng cuối là **type B**

# Sau đó:

# * Dựa vào hàng trước → tính hàng sau
# * Lặp từ 1 → N

# ---

# ## 7️⃣ Tóm tắt ngắn gọn (để nhớ nhanh)

# ✔ Bảng N × 3
# ✔ 3 màu
# ✔ Ô kề nhau không trùng màu
# ✔ Mỗi hàng chỉ có **2 kiểu hợp lệ**:

# * **ABA (2 màu)**
# * **ABC (3 màu)**
#   ✔ Dùng **DP theo từng hàng**

# ---

# Nếu bạn muốn:

# * 👉 mình **giải tiếp phần công thức chuyển DP**
# * 👉 hoặc **viết code Java / Python**
# * 👉 hoặc **giải thích bằng ví dụ N = 2, 3**

# chỉ cần nói 👍
