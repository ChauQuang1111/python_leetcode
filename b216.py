# # Bài **Fancy Sequence** (trên LeetCode 1622 Fancy Sequence) thực chất là **thiết kế một cấu trúc dữ liệu quản lý một dãy số và cho phép biến đổi toàn bộ dãy rất nhiều lần**. ([TutorialsPoint][1])

# # Mình sẽ **giải thích thuật toán trước**, sau đó **viết lại code Python có chú thích chi tiết từng dòng** để bạn dễ hiểu.

# # ---

# # # 1. Ý tưởng cốt lõi của bài

# # Bài yêu cầu thao tác trên một dãy:

# # ```
# # append(val)
# # addAll(inc)
# # multAll(m)
# # getIndex(idx)
# # ```

# # Nếu làm trực tiếp:

# # ```
# # addAll → cộng toàn bộ mảng
# # multAll → nhân toàn bộ mảng
# # ```

# # thì sẽ tốn:

# # ```
# # O(n)
# # ```

# # mỗi lần → **TLE** khi `n = 10^5`.

# # ---

# # 2. Trick quan trọng

# Thay vì cập nhật toàn bộ mảng, ta lưu **biến đổi toàn cục**.

# Giả sử mọi phần tử thực tế có dạng:

# ```
# real_value = a * x + b
# ```

# Trong đó:

# ```
# x = giá trị lưu trong list
# a = hệ số nhân toàn cục
# b = hệ số cộng toàn cục
# ```

# ---

# # 3. Khi gọi addAll

# ```
# addAll(inc)
# ```

# biến đổi:

# ```
# a*x + b + inc
# ```

# → chỉ cần:

# ```
# b = b + inc
# ```

# ---

# # 4. Khi gọi multAll

# ```
# multAll(m)
# ```

# biến đổi:

# ```
# m*(a*x + b)
# ```

# →

# ```
# a = a * m
# b = b * m
# ```

# ---

# # 5. Vấn đề khi append

# Ta muốn thêm số `val`.

# Nhưng giá trị thật là:

# ```
# a*x + b
# ```

# nên ta cần tìm `x`:

# ```
# a*x + b = val
# ```

# →

# ```
# x = (val - b) / a
# ```

# Nhưng vì có **modulo**, ta phải dùng:

# ```
# modular inverse
# ```

# tức là:

# ```
# x = (val - b) * inverse(a)
# ```

# ---

# # 6. Ý nghĩa biến trong code

# ```
# self.x    : list lưu giá trị base
# self.a    : hệ số nhân toàn cục
# self.ainv : nghịch đảo của a
# self.b    : hệ số cộng toàn cục
# ```

# ---

# # 7. Code Python có chú thích

# ```python
# modulo theo đề bài
p = 10**9 + 7

# precompute modular inverse cho số từ 1 -> 100
# inv[m] = m^(-1) mod p
inv = [None] + [pow(m, -1, p) for m in range(1, 101)]


class Fancy:

    def __init__(self):
        # list lưu giá trị base (đã reverse transform)
        self.x = []

        # hệ số nhân toàn cục
        self.a = 1

        # nghịch đảo của a
        self.ainv = 1

        # hệ số cộng toàn cục
        self.b = 0


    def append(self, val):

        # Ta cần tìm x sao cho:
        # a*x + b = val

        # => x = (val - b) / a

        # Trong modulo:
        # x = (val - b) * inverse(a)

        base = (val - self.b) * self.ainv

        # lưu giá trị base
        self.x.append(base)


    def addAll(self, inc):

        # cộng inc cho toàn bộ dãy

        # real value:
        # a*x + b + inc

        # chỉ cần cập nhật b
        self.b += inc


    def multAll(self, m):

        # nhân toàn bộ dãy với m

        # real value:
        # m*(a*x + b)

        # => hệ số mới
        self.a = self.a * m % p

        # cập nhật nghịch đảo
        self.ainv = self.ainv * inv[m] % p

        # b cũng bị nhân
        self.b = self.b * m % p


    def getIndex(self, idx):

        # nếu index vượt quá list
        if idx >= len(self.x):
            return -1

        # giá trị thật
        # real = a*x + b

        return (self.a * self.x[idx] + self.b) % p
# ```

# ---

# # 8. Ví dụ chạy

# ```
# append(2)
# addAll(3)
# append(7)
# multAll(2)
# getIndex(0)
# getIndex(1)
# ```

# Dãy thật:

# ```
# [10,14]
# ```

# ---

# # 9. Độ phức tạp

# | Operation | Time |
# | --------- | ---- |
# | append    | O(1) |
# | addAll    | O(1) |
# | multAll   | O(1) |
# | getIndex  | O(1) |

# ---

# # 10. Trực giác cực quan trọng

# Bài này là **pattern rất nổi tiếng trong competitive programming**:

# ```
# Lazy affine transformation
# ```

# mọi phần tử luôn có dạng:

# ```
# f(x) = ax + b
# ```

# và ta **chỉ update a và b** thay vì update toàn mảng.

# # ---

# # Nếu bạn muốn, mình có thể giải thích thêm **3 thứ rất quan trọng để hiểu sâu bài này**:

# # 1️⃣ Vì sao cần **modular inverse**
# # 2️⃣ Vì sao phải lưu **ainv** thay vì tính mỗi lần
# # 3️⃣ Trick này còn dùng trong **Segment Tree + Lazy Propagation** rất nhiều.



# # Mình sẽ **giải thích đề bài thật đơn giản**.

# ---

# # 1. Ý tưởng của đề bài

# Bạn có một **dãy số ban đầu rỗng**.

# Bạn phải xây dựng class **Fancy** với các thao tác sau:

# ### 1️⃣ append(val)

# Thêm số `val` vào **cuối dãy**.

# Ví dụ

# ```
# append(2)
# ```

# Dãy:

# ```
# [2]
# ```

# ---

# ### 2️⃣ addAll(inc)

# Cộng `inc` cho **tất cả phần tử trong dãy**.

# Ví dụ

# ```
# [2,5,7]
# addAll(3)
# ```

# Dãy mới:

# ```
# [5,8,10]
# ```

# ---

# ### 3️⃣ multAll(m)

# Nhân **tất cả phần tử** với `m`.

# Ví dụ

# ```
# [5,8,10]
# multAll(2)
# ```

# Dãy mới:

# ```
# [10,16,20]
# ```

# ---

# ### 4️⃣ getIndex(idx)

# Lấy **giá trị tại vị trí idx** (0-based).

# Nếu `idx` vượt quá độ dài dãy → trả `-1`.

# Ví dụ

# ```
# [10,16,20]

# getIndex(1)
# ```

# Kết quả

# ```
# 16
# ```

# ---

# # 2. Ví dụ trong đề

# Chuỗi thao tác:

# ```
# Fancy()
# append(2)
# addAll(3)
# append(7)
# multAll(2)
# getIndex(0)
# getIndex(1)
# getIndex(2)
# ```

# ### Bước 1

# ```
# append(2)
# ```

# ```
# [2]
# ```

# ---

# ### Bước 2

# ```
# addAll(3)
# ```

# ```
# [5]
# ```

# ---

# ### Bước 3

# ```
# append(7)
# ```

# ```
# [5,7]
# ```

# ---

# ### Bước 4

# ```
# multAll(2)
# ```

# ```
# [10,14]
# ```

# ---

# ### Query

# ```
# getIndex(0) → 10
# getIndex(1) → 14
# getIndex(2) → -1
# ```

# ---

# # 3. Điều khó của bài

# Nếu làm **naive**:

# ```
# addAll
# multAll
# ```

# → phải cập nhật **toàn bộ mảng**

# Giả sử:

# ```
# 100000 phần tử
# 100000 operations
# ```

# Thì:

# ```
# O(n²) → TLE
# ```

# Nên bài này yêu cầu:

# ```
# append
# addAll
# multAll
# getIndex
# ```

# đều phải gần **O(1)**. ([Walkccc][2])

# ---

# # 4. Bản chất toán học của bài

# Mọi số trong dãy luôn có dạng:

# ```
# value = a * x + b
# ```

# Trong đó:

# ```
# a = hệ số nhân toàn cục
# b = hệ số cộng toàn cục
# ```

# Khi:

# ```
# addAll(inc)
# ```

# →

# ```
# b = b + inc
# ```

# Khi:

# ```
# multAll(m)
# ```

# →

# ```
# a = a * m
# b = b * m
# ```

# ---

# # 5. Tóm lại đề bài yêu cầu

# Thiết kế một cấu trúc dữ liệu hỗ trợ:

# ```
# append(val)
# addAll(inc)
# multAll(m)
# getIndex(idx)
# ```

# với:

# ```
# n ≤ 10^5
# ```

# và phải chạy **rất nhanh**.

# ---

# ✅ Nếu bạn muốn, mình có thể giải thích tiếp:

# * **Ý tưởng lời giải chuẩn (O(1))**
# * **Cách suy nghĩ để ra công thức**
# * **Code Java / C++ / Python**
# * **Trực giác để hiểu bài này trong 3 phút**

# Bài này thực ra là **một trong những bài design + math trick rất nổi tiếng**.

# [1]: https://www.tutorialspoint.com/practice/fancy-sequence.htm?utm_source=chatgpt.com "Fancy Sequence"
# [2]: https://walkccc.me/LeetCode/problems/1622/?utm_source=chatgpt.com "1622. Fancy Sequence - LeetCode Solutions"
