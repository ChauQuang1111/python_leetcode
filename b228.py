# Bài **“Check if Strings Can Be Made Equal With Operations I” (29/03/2026)

# Ok mình sẽ **giải thích thuật toán + thêm chú thích trực tiếp vào code** cho bạn để dễ hiểu 👇

# ---

# ## 🧠 Ý tưởng nhanh

# * Chia chuỗi thành 2 nhóm:

#   * **Chẵn**: index `0, 2`
#   * **Lẻ**: index `1, 3`
# * Mỗi nhóm chỉ cần kiểm tra xem có thể hoán đổi để giống nhau không

# ---

# ## 💻 Code có chú thích

# ```python
# class Solution:
#     def canBeEqual(self, s1: str, s2: str) -> bool:
#         # --- Kiểm tra nhóm CHẴN (index 0 và 2) ---
#         # Có 2 trường hợp:
#         # 1. Giữ nguyên: s1[0] == s2[0] và s1[2] == s2[2]
#         # 2. Swap: s1[0] == s2[2] và s1[2] == s2[0]
#         even_ok = (
#             (s1[0] == s2[0] and s1[2] == s2[2]) or
#             (s1[0] == s2[2] and s1[2] == s2[0])
#         )

#         # --- Kiểm tra nhóm LẺ (index 1 và 3) ---
#         # Tương tự như trên:
#         # 1. Giữ nguyên
#         # 2. Swap
#         odd_ok = (
#             (s1[1] == s2[1] and s1[3] == s2[3]) or
#             (s1[1] == s2[3] and s1[3] == s2[1])
#         )

#         # Chỉ khi CẢ 2 nhóm đều hợp lệ thì trả về True
#         return even_ok and odd_ok
# ```

# ---

# ## 🔍 Diễn giải logic

# ### ✳️ Nhóm chẵn

# Ví dụ:

# ```
# s1 = a b c d
#        0   2
# ```

# 👉 Có 2 khả năng:

# * Không swap → giữ nguyên thứ tự
# * Swap 0 ↔ 2

# ---

# ### ✳️ Nhóm lẻ

# ```
# s1 = a b c d
#          1   3
# ```

# 👉 Cũng giống:

# * Không swap
# * Swap 1 ↔ 3

# ---

# ## 🔥 Tối ưu hơn (pro hơn chút 😎)

# Bạn có thể viết gọn bằng cách **sort từng nhóm**:

# ```python
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # So sánh nhóm chẵn
        if sorted([s1[0], s1[2]]) != sorted([s2[0], s2[2]]):
            return False
        
        # So sánh nhóm lẻ
        if sorted([s1[1], s1[3]]) != sorted([s2[1], s2[3]]):
            return False
        
        return True
# ```

# 👉 Cách này dễ hiểu hơn:

# * Chỉ cần cùng “tập ký tự” là được

# ---

# ## 🎯 Kết luận

# * Không cần thử swap thật
# * Chỉ cần kiểm tra:

#   * Nhóm chẵn match
#   * Nhóm lẻ match

# ---

# Nếu bạn muốn mình có thể:

# * Viết lại bằng Java (theo style bạn hay dùng Scanner + while)
# * Hoặc cho bạn bài nâng cấp (length > 4) để luyện tư duy 💪

# ---

# ## 🧠 Ý tưởng đề bài

# Bạn có 2 chuỗi:

# * `s1`
# * `s2`

# Cả hai đều có **độ dài bằng nhau = 4** (rất quan trọng).

# ---

# ## 🔁 Phép toán được phép

# Bạn có thể thực hiện thao tác sau trên **một chuỗi**:

# 👉 Chọn **2 vị trí bất kỳ có cùng parity (cùng chẵn hoặc cùng lẻ)** và hoán đổi (swap)

# Cụ thể:

# * Vị trí **chẵn**: index 0 và 2
# * Vị trí **lẻ**: index 1 và 3

# 👉 Nghĩa là bạn chỉ được swap:

# * `s[0] ↔ s[2]`
# * `s[1] ↔ s[3]`

# KHÔNG được swap chéo kiểu:

# * ❌ `s[0] ↔ s[1]`
# * ❌ `s[2] ↔ s[3]` (khác parity)

# ---

# ## ❓ Mục tiêu

# Kiểm tra xem:
# 👉 Có thể biến `s1` thành `s2` bằng các phép swap trên không?

# ---

# ## 🔍 Hiểu bản chất

# Vì bạn chỉ swap được trong 2 nhóm:

# * Nhóm chẵn: `{0, 2}`
# * Nhóm lẻ: `{1, 3}`

# 👉 Nên:

# * Các ký tự ở vị trí **chẵn của s1** chỉ có thể đổi chỗ với nhau
# * Các ký tự ở vị trí **lẻ của s1** cũng chỉ đổi với nhau

# ⛔ Không thể di chuyển ký tự từ chẵn → lẻ hoặc ngược lại

# ---

# ## ✅ Điều kiện để làm được

# 👉 Bạn chỉ cần kiểm tra:

# * Tập ký tự ở vị trí **chẵn của s1** == tập ký tự ở vị trí **chẵn của s2**
# * Tập ký tự ở vị trí **lẻ của s1** == tập ký tự ở vị trí **lẻ của s2**

# ---

# ## 📌 Ví dụ

# ### Ví dụ 1:

# ```
# s1 = "abcd"
# s2 = "cdab"
# ```

# * s1 chẵn: a, c

# * s2 chẵn: c, a ✅ giống nhau

# * s1 lẻ: b, d

# * s2 lẻ: d, b ✅ giống nhau

# 👉 ✔️ Kết quả: TRUE

# ---

# ### Ví dụ 2:

# ```
# s1 = "abcd"
# s2 = "dacb"
# ```

# * s1 chẵn: a, c
# * s2 chẵn: d, c ❌ khác

# 👉 ❌ Kết quả: FALSE

# ---

# ## 🔥 Tóm lại (rất quan trọng)

# 👉 Bạn KHÔNG cần thử swap thật
# 👉 Chỉ cần:

# * So sánh ký tự ở index chẵn
# * So sánh ký tự ở index lẻ

# ---

# ## 💡 Insight quan trọng

# Đây là dạng:

# > “Grouping by parity” (chia nhóm theo chẵn/lẻ)

# → Hay gặp trong LeetCode

# ---

# Nếu bạn muốn, mình có thể:

# * Viết code Java (chuẩn theo style bạn thích)
# * Hoặc cho bạn bài tương tự để luyện thêm 💪
