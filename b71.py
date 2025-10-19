# 1625. Lexicographically Smallest String After Applying Operations(19/10/2025)
# Rất hay — đây là một **lời giải cực tối ưu** cho bài **LeetCode 1625. Lexicographically Smallest String After Applying Operations**, được viết theo phong cách “toán học hoá” thay vì duyệt BFS như cách thông thường.
# Dưới đây là bản **giải thích chi tiết thuật toán + chú thích từng dòng code** 👇

# ---

# ## 🔍 Ý tưởng tổng quát

# Bài toán cho phép ta:

# 1. **Cộng `a` vào tất cả chữ số ở vị trí lẻ** (vị trí 1,3,5,… — tính từ 0).
# 2. **Xoay phải `b` ký tự**.

# Ta có thể áp dụng hai phép này **bao nhiêu lần cũng được** — nên thay vì thử hết (rất tốn thời gian), ta sẽ **tận dụng tính chu kỳ** của phép quay và phép cộng để chỉ xét các trường hợp *đại diện*.

# ---

# ## ✅ Phân tích từng phần

# ### 1️⃣ Ý tưởng chính

# * Nếu ta xoay `b` ký tự liên tục, sau `n / gcd(n, b)` lần, chuỗi trở về vị trí ban đầu.
#   → Chỉ cần xét các **độ xoay cách nhau `gcd(b, n)`**.

# * Việc cộng `a` vào vị trí lẻ có chu kỳ mod 10.
#   → Cộng `a` nhiều lần sẽ chỉ tạo ra **`10 / gcd(a, 10)` giá trị khác nhau** cho cùng một vị trí.

# Nhờ đó, ta **giảm số trạng thái cần xét xuống mức cực nhỏ**.

# ---

# ## 💡 Code có chú thích chi tiết

# ```python
from math import gcd

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        s = list(map(int, s))      # Chuyển chuỗi sang list số nguyên
        n = len(s)
        step = gcd(b, n)           # Mỗi lần xoay b ký tự — chỉ có n / gcd(n,b) dạng khác nhau
        g = gcd(a, 10)             # Cộng a vào 1 chữ số chỉ tạo 10 / gcd(a,10) giá trị khác nhau
        ans = [10]                 # Lưu chuỗi nhỏ nhất (khởi tạo với giá trị lớn hơn 9)

        # 🧩 Hàm phụ: điều chỉnh các vị trí chẵn/lẻ sao cho càng nhỏ càng tốt
        def modify(start: int) -> None:
            ch = t[start]  # Lấy chữ số đầu tiên ở vị trí start (0 hoặc 1)
            
            # Chữ số này có thể giảm xuống tới ch % g (chu kỳ modulo 10)
            # Ví dụ: a=2, g=2, ch=5 => có thể giảm về 1 (5→7→9→1)
            inc = ch % g - ch  # Độ thay đổi cần thêm (âm để giảm giá trị)
            
            # Nếu có thể giảm, cập nhật toàn bộ vị trí cùng loại (chẵn/lẻ)
            if inc:
                for j in range(start, n, 2):  # nhảy 2 bước (vị trí cùng parity)
                    t[j] = (t[j] + inc) % 10

        # 🌀 Xét tất cả các cách xoay khác nhau (chỉ cần duyệt step lần)
        for i in range(0, n, step):      
            t = s[i:] + s[:i]      # Tạo chuỗi sau khi xoay i ký tự sang phải

            modify(1)              # Cộng vào vị trí lẻ sao cho nhỏ nhất
            if step % 2:           # Nếu xoay khiến vị trí lẻ → chẵn được (tức n/b là lẻ)
                modify(0)          # Khi đó ta cũng có thể giảm các vị trí chẵn

            ans = min(ans, t)      # Cập nhật kết quả nhỏ nhất (so sánh từ điển)

        return ''.join(map(str, ans))

# s = "5525"
# a = 9
# b = 2
# ```

# ### Bước 1:

# `n = 4`, `step = gcd(2,4) = 2`, `g = gcd(9,10) = 1`.

# → Ta chỉ cần xét 2 kiểu xoay: xoay 0, xoay 2.

# ### Bước 2:

# * Với mỗi chuỗi xoay, thử cộng `a` để làm nhỏ nhất các vị trí lẻ.
# * Vì `g=1`, ta có thể đưa mọi chữ số lẻ về **0**.

# ### Bước 3:

# So sánh tất cả các chuỗi sau khi “giảm” — kết quả nhỏ nhất là `"2050"`.

# ---

# ## 🧠 Tóm tắt ý tưởng

# | Bước | Mục tiêu                          | Cách làm                                   |
# | ---- | --------------------------------- | ------------------------------------------ |
# | 1    | Giảm số lần xoay cần xét          | Dựa trên `gcd(b, n)`                       |
# | 2    | Giảm số lần cộng cần xét          | Dựa trên `gcd(a, 10)`                      |
# | 3    | Giảm từng vị trí sao cho nhỏ nhất | Dựa theo parity (chẵn/lẻ)                  |
# | 4    | So sánh tất cả chuỗi              | Giữ lại chuỗi nhỏ nhất theo thứ tự từ điển |

# ---

# Bạn có muốn mình **viết lại lời giải này sang Java** (có chú thích chi tiết tương đương) không?


# ---

## 🧩 **Đề bài tóm tắt**

# Cho một **chuỗi số** `s` (chỉ gồm các ký tự `'0'–'9'`) và hai **số nguyên** `a`, `b`.
# Ta có thể thực hiện **hai loại thao tác tùy ý số lần** như sau:

### 🔹 Operation 1 — Add `a` to odd indices:

# Cộng `a` vào **các ký tự ở vị trí lẻ (1, 3, 5, …)**.

# * Nếu vượt quá `9`, thì tính theo modulo `10`.
#   (Ví dụ: `'8' + 5 → '3'` vì `(8 + 5) % 10 = 3`)

# 👉 Ví dụ:
# `s = "3456"`, `a = 7`
# → cộng `a` vào vị trí 1 và 3
# → `"3456"` → `"3153"`

# ---

### 🔹 Operation 2 — Rotate right by `b` positions:

# Dịch vòng chuỗi sang phải **`b` ký tự**.
# (Ví dụ `b = 2`: `"123456"` → `"561234"`)

# ---

## 🎯 **Mục tiêu:**

# Sau khi thực hiện **bất kỳ số lần các phép trên (theo thứ tự tự do)**,
# hãy tìm **chuỗi nhỏ nhất theo thứ tự từ điển (lexicographically smallest)** có thể đạt được.



## 📘 Ví dụ:

# **Input:**

# ```
# s = "5525"
# a = 9
# b = 2
# ```

# **Các bước có thể xảy ra:**

# ```
# "5525"  (ban đầu)
# rotate(2) → "2555"
# add(odd) → "2454"
# rotate(2) → "5424"
# add(odd) → "5313"
# ...
# ```

# Sau nhiều bước, chuỗi nhỏ nhất có thể đạt được là `"2050"`.

# **Output:** `"2050"`



# ## 💡 **Trực giác thuật toán:**

# * Vì mỗi phép có thể được lặp lại **vô hạn lần**,
#   ta nên nghĩ đến **duyệt toàn bộ các trạng thái có thể đạt được**.
# * Mỗi trạng thái là một chuỗi khác nhau.
# * Do đó, ta dùng **BFS hoặc DFS + visited set** để:

#   * Tránh lặp vô hạn.
#   * Khám phá tất cả các chuỗi có thể đạt được từ `s`.
#   * Cập nhật chuỗi nhỏ nhất gặp được.


## 🧠 **Tóm tắt ý tưởng giải:**

# 1. Sử dụng `queue` để BFS từ chuỗi ban đầu `s`.
# 2. Tại mỗi bước:

#    * Sinh chuỗi mới sau khi **thêm `a` vào các vị trí lẻ**.
#    * Sinh chuỗi mới sau khi **xoay phải `b` ký tự**.
# 3. Nếu chuỗi mới **chưa xuất hiện trước đó**, thêm vào `queue`.
# 4. Cập nhật **chuỗi nhỏ nhất theo thứ tự từ điển** khi gặp chuỗi mới nhỏ hơn.
# 5. Khi BFS xong, kết quả là chuỗi nhỏ nhất.

# ---

# ## ✅ **Tóm lại:**

# | Thành phần   | Mô tả                                  |
# | ------------ | -------------------------------------- |
# | **Input**    | `s` (string gồm chữ số), `a`, `b`      |
# | **Phép 1**   | Cộng `a` (mod 10) vào các vị trí lẻ    |
# | **Phép 2**   | Xoay phải `b` ký tự                    |
# | **Mục tiêu** | Tìm chuỗi nhỏ nhất theo thứ tự từ điển |
# | **Kỹ thuật** | BFS (hoặc DFS) + Set tránh lặp         |

