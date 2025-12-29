# # Pyramid Transition Matrix(29/12/2025)
# Mình sẽ **giải thích thuật toán + chú thích chi tiết từng phần code** để bạn hiểu rõ cách lời giải này hoạt động (và cả điểm chưa tối ưu của nó).
from typing import List
from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        # mp: map từ 2 ký tự phía dưới -> danh sách ký tự có thể đặt lên trên
        # Ví dụ: "BCG" -> mp["BC"] = ["G"]
        mp = defaultdict(list)
        for temp in allowed:
            lr = temp[:2]     # lấy 2 ký tự phía dưới
            t = temp[2:]      # ký tự phía trên
            mp[lr].append(t)

        # Hàm DFS: kiểm tra xem từ hàng 'line' có thể xây tiếp lên đỉnh hay không
        def dfs(line):
            lth = len(line)

            # Nếu chỉ còn 1 ký tự -> đã xây xong kim tự tháp
            if lth == 1:
                return True

            # cand[i] = danh sách ký tự có thể đặt lên cặp (line[i], line[i+1])
            cand = []

            # số lượng lựa chọn lớn nhất trong các cand
            maxcand = 0

            # Duyệt tất cả các cặp ký tự kề nhau ở hàng hiện tại
            for i in range(lth - 1):
                lr = line[i:i+2]   # cặp ký tự dưới

                # Nếu không có luật chuyển cho cặp này thì bỏ qua
                if lr not in mp:
                    continue

                toplist = mp[lr]   # danh sách ký tự có thể đặt lên trên
                cand.append(toplist)
                maxcand = max(maxcand, len(toplist))

            # Nếu số cặp hợp lệ < lth - 1
            # => có ít nhất một cặp không xây được hàng trên
            if len(cand) != lth - 1:
                return False

            # Thử sinh các hàng phía trên (chưa sinh đủ mọi tổ hợp)
            for i in range(maxcand):
                temp = ""   # hàng phía trên đang được tạo

                for j in range(lth - 1):
                    # Chọn ký tự thứ i trong cand[j]
                    # Nếu cand[j] ngắn hơn thì lấy phần tử cuối
                    idx = min(len(cand[j]) - 1, i)
                    u = cand[j][idx]
                    temp += u

                # Nếu tạo được hàng hợp lệ
                if len(temp) == lth - 1:
                    # Gọi đệ quy để xây tiếp
                    if dfs(temp):
                        return True

            # Thử hết mọi khả năng mà không xây được
            return False

        # Bắt đầu DFS từ hàng đáy
        return dfs(bottom)

# ---

# ## 1. Ý tưởng tổng quát

# Bài **Pyramid Transition Matrix** dùng **DFS / Backtracking**:

# * Mỗi lần ta có một hàng `line`
# * Ta sinh ra **tất cả các hàng phía trên có thể**
# * Gọi đệ quy `dfs(hàng_mới)`
# * Nếu lên được hàng dài 1 → `True`

# ---

# ## 2. Phân tích từng phần code

# ### 2.1. Tiền xử lý `allowed`

# ```python
# mp = defaultdict(list)
# for temp in allowed:
#     lr = temp[:2]   # 2 ký tự dưới
#     t = temp[2:]    # ký tự phía trên
#     mp[lr].append(t)
# ```

# 👉 Chuyển `allowed` thành **bảng tra cứu**:

# Ví dụ:

# ```python
# "BCG" → mp["BC"] = ["G"]
# "CDE" → mp["CD"] = ["E"]
# ```

# ➡️ Giúp tra cứu nhanh:
# **(A, B) → danh sách các ký tự có thể đặt lên trên**

# ---

# ## 3. Hàm DFS chính

# ```python
# def dfs(line):
# ```

# `line` = một hàng hiện tại của kim tự tháp

# ---

# ### 3.1. Điều kiện dừng

# ```python
# lth = len(line)
# if lth == 1:
#     return True
# ```

# ✔️ Nếu chỉ còn 1 ký tự → xây xong kim tự tháp

# ---

# ### 3.2. Sinh các khả năng cho hàng trên

# ```python
# cand = []
# maxcand = 0
# ```

# * `cand[i]` = danh sách ký tự có thể đặt lên cặp `(line[i], line[i+1])`
# * `maxcand` = số lượng lớn nhất trong các danh sách đó

# ---

# ```python
# for i in range(lth-1):
#     lr = line[i:i+2]
#     if lr not in mp:
#         continue
#     toplist = mp[lr]
#     cand.append(toplist)
#     maxcand = max(maxcand, len(toplist))
# ```

# 📌 Ví dụ:

# ```
# line = "BCD"
# cand = [
#     ["G"],   # từ "BC"
#     ["E"]    # từ "CD"
# ]
# ```

# ---

# ### 3.3. Nếu thiếu luật → không xây được

# ```python
# if len(cand) != lth-1:
#     return False
# ```

# ❌ Nếu có **ít nhất một cặp** không có luật chuyển
# → không thể tạo hàng phía trên

# ---

# ## 4. Sinh các hàng phía trên (chưa tối ưu)

# ```python
# up = [None] * (lth-1)
# ```

# (Không dùng đến, có thể bỏ)

# ---

# ### 4.1. Sinh hàng mới bằng cách "ghép chỉ số"

# ```python
# for i in range(maxcand):
#     temp = ""
#     for j in range(lth-1):
#         idx = min(len(cand[j])-1, i)
#         u = cand[j][idx]
#         temp += u
# ```

# 📌 Cách hoạt động:

# * Lấy **ký tự thứ i** trong mỗi `cand[j]`
# * Nếu danh sách ngắn hơn → dùng phần tử cuối

# ⚠️ **Điểm yếu**:

# * Không sinh **tất cả tổ hợp**
# * Bỏ sót nhiều khả năng
# * Không phải cách backtracking chuẩn

# Ví dụ:

# ```
# cand = [["A","B"], ["C","D"]]
# → chỉ sinh:
# AC, BD
# ❌ thiếu: AD, BC
# ```

# ---

# ### 4.2. Gọi DFS tiếp

# ```python
# if len(temp) == lth-1:
#     if dfs(temp):
#         return True
# ```

# ✔️ Nếu **có một cách** xây được đến đỉnh
# → trả về `True`

# ---

# ### 4.3. Nếu thử hết mà không được

# ```python
# return False
# ```

# ---

# ## 5. Tổng kết thuật toán

# ### ✔️ Đúng ở:

# * Ý tưởng DFS
# * Dùng map để tra luật
# * Dừng khi còn 1 ký tự

# ### ❌ Chưa chuẩn ở:

# * Sinh hàng trên **không phải tất cả tổ hợp**
# * Có thể **miss case đúng**

# ---

# ## 6. Phiên bản DFS chuẩn (để bạn so sánh)

# ```python
# def dfs(line):
#     if len(line) == 1:
#         return True

#     def backtrack(pos, cur):
#         if pos == len(line) - 1:
#             return dfs(cur)

#         pair = line[pos:pos+2]
#         if pair not in mp:
#             return False

#         for ch in mp[pair]:
#             if backtrack(pos + 1, cur + ch):
#                 return True
#         return False

#     return backtrack(0, "")
# ```

# 📌 Phiên bản này:

# * Sinh **đầy đủ tổ hợp**
# * Không bỏ sót
# * Chuẩn LeetCode

# ---

# ## 7. Nếu bạn muốn

# * 🔹 Mình **chú thích lại code của bạn ngay trong từng dòng**
# * 🔹 So sánh **DFS vs DP**
# * 🔹 Tối ưu bằng **memoization**
# * 🔹 Viết lại bằng **Java**

# 👉 Nói mình biết hướng bạn muốn học tiếp nhé 👌

# Đây là một bài toán thường gặp trên LeetCode, nói về việc **xây một kim tự tháp chữ** dựa trên các quy tắc cho trước.

# ---

# ## 1. Mô tả bài toán

# Bạn được cho:

# ### 🔹 `bottom`

# * Một **chuỗi ký tự** (thường là chữ in hoa A–G).
# * Đây là **hàng đáy** của kim tự tháp.

# Ví dụ:

# ```
# bottom = "BCD"
# ```

# ### 🔹 `allowed`

# * Một **danh sách các chuỗi dài 3 ký tự**.
# * Mỗi chuỗi có dạng `"ABC"` nghĩa là:

#   > Nếu **A** và **B** đứng cạnh nhau ở hàng dưới
#   > thì **C** có thể đứng lên trên chúng ở hàng trên.

# Ví dụ:

# ```
# allowed = ["BCG", "CDE", "GEA", "FFF"]
# ```

# ---

# ## 2. Luật xây kim tự tháp

# * Kim tự tháp được xây **từ dưới lên trên**.
# * Mỗi khối ở **hàng trên** được tạo từ **2 khối kề nhau ở hàng dưới**.
# * Với mỗi cặp `(x, y)` ở hàng dưới, ta tìm xem có luật nào `xy -> z` trong `allowed` hay không.
# * Nếu có nhiều `z` thì **được chọn bất kỳ**.

# 📌 Mục tiêu:
# 👉 **Kiểm tra xem có thể xây lên đến đỉnh (còn 1 ký tự) hay không**

# ---

# ## 3. Ví dụ minh họa

# ### Ví dụ 1

# ```
# bottom = "BCD"
# allowed = ["BCG", "CDE", "GEA", "FFF"]
# ```

# **Bước 1:**
# Hàng đáy:

# ```
# B   C   D
# ```

# * (B, C) → G (vì có "BCG")
# * (C, D) → E (vì có "CDE")

# Hàng trên:

# ```
# G   E
# ```

# **Bước 2:**

# * (G, E) → A (vì có "GEA")

# Đỉnh:

# ```
# A
# ```

# ✅ Xây được kim tự tháp → **true**

# ---

# ### Ví dụ 2

# ```
# bottom = "AABA"
# allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
# ```

# * Có thể xây lên một vài tầng
# * Nhưng đến một tầng nào đó **không có luật phù hợp**
#   ❌ Không xây tiếp được → **false**

# ---

# ## 4. Bài toán thực chất là gì?

# 👉 Đây là bài **Backtracking / DFS**

# * Mỗi tầng có thể có **nhiều cách tạo**
# * Ta thử **tất cả khả năng**
# * Chỉ cần **1 cách thành công** là trả về `true`

# ---

# ## 5. Tóm tắt ngắn gọn

# * `bottom`: hàng đáy
# * `allowed`: luật chuyển từ 2 ký tự → 1 ký tự
# * Xây từ dưới lên
# * Nếu lên được đến **1 ký tự** → `true`
# * Nếu bị kẹt ở giữa → `false`

# ---

# Nếu bạn muốn:

# * 🔹 Giải thích bằng **cây DFS**
# * 🔹 Ví dụ chi tiết hơn từng bước
# * 🔹 Code Java / Python kèm giải thích

# 👉 Cứ nói, mình sẽ giải tiếp theo cách bạn dễ hiểu nhất 👍
