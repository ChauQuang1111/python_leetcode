## 📘 Concatenation of Consecutive Binary Numbers

# Concatenation of Consecutive Binary Numbers(28/02/2026)


# ## 📘 Bài: Concatenation of Consecutive Binary Numbers

# (thuật toán tối ưu bằng **bit manipulation + tiền xử lý**)

# ---

# ## 💡 Ý tưởng chính của thuật toán

# Thay vì mỗi lần gọi hàm lại tính từ 1 → n, ta:

# * Tiền xử lý trước toàn bộ kết quả từ 1 → 10⁵
# * Lưu vào mảng `ans`
# * Khi cần chỉ việc trả về `ans[n]` (O(1))

# ---

## 🧠 Giải thích thuật toán từng phần

### 1️⃣ Hằng số MOD

# ```python
# MOD = 10**9 + 7
# ```

# Vì số sau khi nối nhị phân sẽ rất lớn nên ta luôn lấy:

# ```
# % (10^9 + 7)
# ```

# để tránh overflow.


### 2️⃣ Tạo mảng lưu kết quả

# ```python
# ans = [0]*(10**5 + 1)
# ```

# * ans[i] = kết quả sau khi nối binary từ 1 → i
# * Kích thước 100001 vì đề cho n ≤ 10^5

# ---

# ### 3️⃣ Biến lưu kết quả hiện tại

# ```python
# res = 0
# ```

# `res` sẽ chứa giá trị sau khi nối dần các số.

# ---

# ### 4️⃣ Biến length không dùng

# ```python
# length = -1
# ```

# ⚠️ Biến này thực tế **không dùng đến**. Có thể xóa.

# ---

# ## 🔥 Phần quan trọng nhất

# ```python
# for i in range(1, 18):
# ```

# ### Vì sao 18?

# * 2^17 = 131072 > 10^5
# * Nghĩa là số ≤ 10^5 chỉ cần tối đa **17 bit**
# * Nên ta duyệt số bit từ 1 → 17

# ---

# ### Vòng lặp bên trong

# ```python
# for e in range(2**(i - 1), min(2**i, len(ans))):
# ```

# Ý nghĩa:

# * Các số có **i bit** nằm trong khoảng:

# ```
# [2^(i-1), 2^i - 1]
# ```

# Ví dụ:

# | i | Khoảng số | Binary length |
# | - | --------- | ------------- |
# | 1 | 1 → 1     | 1 bit         |
# | 2 | 2 → 3     | 2 bit         |
# | 3 | 4 → 7     | 3 bit         |
# | 4 | 8 → 15    | 4 bit         |

# ---

# ## 🚀 Dòng quan trọng nhất

# # ```python
# # res = ((res << i) | e) % MOD
# # ```

# # Giải thích từng phần:

# # ### `res << i`

# # Dịch trái i bit
# # → tương đương nhân với `2^i`

# # Mục đích:
# # 👉 tạo chỗ trống i bit để nối số mới

# # ---

# ### `| e`

# Toán tử OR bit

# Vì sau khi dịch trái, phần cuối toàn là 0
# nên:

# ```
# (res << i) | e
# ```

# chính là:
# 👉 nối binary của e vào cuối



### Ví dụ minh họa

# Giả sử:

# ```
# res = 11011   (27)
# e = 100       (4)
# i = 3
# ```

# Ta làm:

# ```
# res << 3
# 11011 → 11011000

# OR 100
# 11011000
# 00000100
# ---------
# 11011100
# ```

# Kết quả:

# ```
# 11011100 = 220
# ```

# Chính là nối:

# ```
# 11011 + 100
# ```

# ---

# ### Lưu kết quả

# ```python
# ans[e] = res
# ```

# Lưu lại kết quả cho số e.

# ---

# ## 🎯 Cuối cùng

# ```python
# class Solution:
#     def concatenatedBinary(self, n: int) -> int:
#         return ans[n]
# ```

# Chỉ cần trả về giá trị đã tiền xử lý.

# ⏱ Thời gian:

# * Tiền xử lý: O(n)
# * Mỗi truy vấn: O(1)

# ---

# # 🧩 Viết lại code có chú thích rõ ràng

# ```python
MOD = 10**9 + 7

# ans[i] = kết quả nối binary từ 1 đến i
ans = [0]*(10**5 + 1)

res = 0  # lưu kết quả hiện tại

# duyệt theo số bit từ 1 đến 17
for i in range(1, 18):
    
    # các số có đúng i bit nằm trong khoảng này
    for e in range(2**(i - 1), min(2**i, len(ans))):
        
        # dịch trái i bit để tạo chỗ
        # OR với e để nối binary của e vào cuối
        res = ((res << i) | e) % MOD
        
        # lưu kết quả
        ans[e] = res


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return ans[n]
# ```

# ---

# ## 🏆 Bản chất thuật toán

# Thay vì:

# ```
# chuyển sang string → nối → convert lại
# ```

# Ta dùng:

# ```
# bit shift + OR
# ```

# Nhanh hơn rất nhiều.

# ---

# Nếu bạn muốn, mình có thể:

# * 🔥 Giải thích vì sao dùng `|` mà không dùng `+`
# * 🔥 So sánh cách này với cách tính bit-length bằng `log2`
# * 🔥 Viết lại phiên bản Java cho bạn

# Bạn muốn đào sâu phần nào?


# ---

# ## 🧠 Yêu cầu đề bài (giải thích đơn giản)

# Cho một số nguyên dương **n**.

# Bạn cần:

# 1. Chuyển từng số từ **1 đến n** sang **hệ nhị phân (binary)**.
# 2. Nối (concatenate) tất cả các số nhị phân đó lại thành **một chuỗi duy nhất**.
# 3. Chuyển chuỗi nhị phân đó thành **một số thập phân**.
# 4. Trả về kết quả **mod (10⁹ + 7)**.

# ---

# ## 🔎 Ví dụ minh hoạ

# ### Ví dụ 1:

# ```
# Input: n = 1
# ```

# * 1 → binary: `1`
# * Nối lại: `1`
# * Decimal: 1

# 👉 Output: `1`

# ---

# ### Ví dụ 2:

# ```
# Input: n = 3
# ```

# Ta làm từng bước:

# | Số | Binary |
# | -- | ------ |
# | 1  | 1      |
# | 2  | 10     |
# | 3  | 11     |

# Nối lại:

# ```
# 1 + 10 + 11 = 11011
# ```

# Chuyển sang thập phân:

# ```
# 11011₂ = 27₁₀
# ```

# 👉 Output: `27`

# ---

# ### Ví dụ 3:

# ```
# Input: n = 4
# ```

# | Số | Binary |
# | -- | ------ |
# | 1  | 1      |
# | 2  | 10     |
# | 3  | 11     |
# | 4  | 100    |

# Nối lại:

# ```
# 11011100
# ```

# Chuyển sang thập phân:

# ```
# 11011100₂ = 220₁₀
# ```

# 👉 Output: `220`

# ---

# ## 🎯 Tóm lại bản chất bài toán

# Thay vì:

# ```
# res = "1"
# res += "10"
# res += "11"
# res += "100"
# ```

# Ta thực hiện nối số nhị phân liên tục từ 1 → n.

# ---

# ## ❗ Tại sao phải mod (10⁹ + 7)?

# Vì:

# * Khi n lớn (ví dụ 10^5)
# * Chuỗi nhị phân cực kỳ dài
# * Số thập phân sẽ rất lớn (overflow)

# Nên đề bài yêu cầu:

# ```
# answer % (10^9 + 7)
# ```

# ---

# ## 💡 Insight quan trọng (để sau này code)

# Thay vì tạo chuỗi (rất chậm), ta có thể:

# Mỗi lần thêm số mới `i`, ta:

# ```
# res = (res << số_bit_của_i) + i
# ```

# Ví dụ khi thêm số 4 (100 có 3 bit):

# ```
# res = res << 3
# res = res + 4
# ```

# ---

# Nếu bạn muốn, mình có thể:

# * Giải thích tư duy bit chi tiết từng bước
# * Hoặc phân tích code Java dòng từng dòng
# * Hoặc chỉ ra vì sao phải dùng bit shift

# Bạn muốn mình đào sâu phần nào?
