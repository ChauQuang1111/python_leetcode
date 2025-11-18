# 717. 1-bit and 2-bit Characters(18/11/2025)
# Dưới đây là **giải thích dễ hiểu nhất** cho đề bài **LeetCode 717 – 1-bit and 2-bit Characters**.
class Solution:
    def isOneBitCharacter(self, bits):
        n = len(bits)
        currIndex = 0

        # Nếu bit cuối là 1 → chắc chắn không thể là ký tự 1-bit
        # Vì ký tự 1-bit duy nhất là "0"
        if bits[-1] == 1:
            return False

        # Duyệt từ trái sang phải
        while currIndex < n:
            if bits[currIndex] == 0:
                # Nếu bit hiện tại là 0 → đây là ký tự 1-bit
                # Nếu nó nằm đúng ở vị trí cuối cùng → ký tự cuối là 1-bit
                if currIndex == n - 1:
                    return True

                # Di chuyển 1 bước
                currIndex += 1
            else:
                # Nếu bit hiện tại là 1 → ký tự này là loại 2-bit ("10" hoặc "11")
                # Nhảy qua 2 bit
                currIndex += 2

        # Nếu thoát vòng lặp mà chưa return => ký tự cuối thuộc về 2-bit
        return False

# ---

# # 📌 **Giải thích đề bài**

# Bạn được cho một mảng `bits` gồm các số `0` và `1`.

# Các ký tự được mã hóa theo quy tắc:

# ### ✔ **Ký tự 1-bit**

# * Được biểu diễn bởi **1 số 0**
# * Ví dụ: `0`

# ### ✔ **Ký tự 2-bit**

# * Được biểu diễn bởi **2 số**
# * Có dạng:

#   * `10`
#   * `11`

# ---

# ## 🎯 **Nhiệm vụ:**

# **Bạn phải kiểm tra xem ký tự cuối cùng (bit cuối cùng) có phải là một ký tự 1-bit hay không.**

# Tức là:
# 👉 Bit cuối (phần tử cuối của mảng) có phải là **`0` độc lập** không?

# ---

# # 📌 **Một số ví dụ**

# ### **Ví dụ 1**

# ```
# Input: bits = [1,0,0]
# Giải mã: 10 | 0
# Ký tự cuối cùng = 0  → 1-bit → return True
# ```

# ### **Ví dụ 2**

# ```
# Input: bits = [1,1,1,0]
# Giải mã: 11 | 10
# Ký tự cuối cùng = 10 → 2-bit → return False
# ```

# ---

# # 📌 **Cách hiểu nhanh**

# Bạn chỉ cần mô phỏng cách đọc chuỗi:

# * Nếu gặp `1` → bỏ qua 2 bit (vì là ký tự 2-bit)
# * Nếu gặp `0` → bỏ qua 1 bit (vì là ký tự 1-bit)

# Nếu cuối cùng **điểm dừng nằm đúng vị trí phần tử cuối** → đó là ký tự 1-bit → **True**.
# Nếu điểm dừng vượt qua cuối (nhảy 2 bước) → ký tự cuối thuộc về ký tự 2-bit → **False**.

# ---

# # ✔ Kết luận

# 👉 **Mảng kết thúc bằng `0` độc lập** → return **True**
# 👉 **Mảng kết thúc là phần của ký tự 2-bit** → return **False**

# ---

# Nếu bạn muốn mình giải thích **thuật toán + code Java hoặc Python** kèm minh họa từng bước, bạn chỉ cần bảo mình nhé!
# Dưới đây là **giải thích thuật toán** và **code đã thêm chú thích chi tiết** cho bạn.

# ---

# # ✅ **Giải thích thuật toán**

# Ta duyệt từ trái → phải theo quy tắc mã hoá:

# * Nếu gặp **0** → đây là ký tự 1-bit → nhảy **1 bước**
# * Nếu gặp **1** → đây là ký tự 2-bit → nhảy **2 bước**

# Mục tiêu: **kiểm tra xem ký tự cuối cùng có phải là 1-bit ("0") hay không**.

# ---

# ## ❗ Ý tưởng chính

# * Nếu ký tự cuối cùng là `1` → chắc chắn **không phải 1-bit** → return False ngay.
# * Nếu gặp ký tự "0" đúng ở **vị trí cuối cùng** → return True.
# * Nếu không, ta tiếp tục nhảy theo quy tắc 0 → +
