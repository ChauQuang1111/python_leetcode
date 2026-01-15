# Maximize Area of Square Hole in Grid(15/01/2026)
# ## 1. Mô tả bài toán (hiểu đơn giản)
# Ok 👍 mình sẽ **giải thích thuật toán + thêm chú thích trực tiếp vào code** để bạn nhìn là hiểu ngay vì sao làm vậy.

# ---

# ## 1. Ý tưởng thuật toán (tóm tắt)

# * Khi **k thanh liên tiếp bị tháo**, ta tạo được **k + 1 ô liền nhau**
# * Vì hình cần là **hình vuông**:

#   * cạnh = `min(chiều cao lớn nhất, chiều rộng lớn nhất)`
# * Chiều cao ↔ thanh **ngang** (`hBars`)
# * Chiều rộng ↔ thanh **dọc** (`vBars`)

# ---

# ## 2. Giải thích từng phần trong code

# ### ✅ Code có chú thích chi tiết

# ```python
class Solution:
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):

        # Sắp xếp để các thanh bị tháo theo thứ tự tăng dần
        hBars.sort()
        vBars.sort()

        # Hàm tìm số thanh bị tháo LIÊN TIẾP dài nhất
        def longest(arr):
            # mx: độ dài lớn nhất tìm được
            # curr: độ dài đoạn liên tiếp hiện tại
            mx = curr = 1

            # Duyệt từ phần tử thứ 2
            for i in range(1, len(arr)):
                # Nếu hai thanh liên tiếp nhau (ví dụ 3 và 4)
                if arr[i] == arr[i - 1] + 1:
                    curr += 1          # tăng độ dài đoạn liên tiếp
                else:
                    curr = 1           # bị ngắt → reset lại

                # Cập nhật đoạn dài nhất
                mx = max(mx, curr)

            return mx

        # longest(hBars) + 1:
        # nếu tháo k thanh ngang liên tiếp → tạo k + 1 ô theo chiều cao
        # tương tự cho chiều rộng
        side = min(
            longest(hBars) + 1,   # chiều cao tối đa của hình vuông
            longest(vBars) + 1    # chiều rộng tối đa của hình vuông
        )

        # Diện tích hình vuông = cạnh × cạnh
        return side * side

# ## 3. Ví dụ chạy thuật toán

# ### Input

# ```python
# n = 5
# m = 5
# hBars = [1, 2]
# vBars = [2]
# ```

# ### Phân tích

# * `hBars = [1, 2]` → 2 thanh liên tiếp → chiều cao = `2 + 1 = 3`
# * `vBars = [2]` → 1 thanh → chiều rộng = `1 + 1 = 2`
# * cạnh hình vuông = `min(3, 2) = 2`
# * diện tích = `2² = 4`

# ---

# ## 4. Độ phức tạp

# * Sắp xếp: `O(n log n)`
# * Duyệt tìm đoạn liên tiếp: `O(n)`
# * Tổng: **O(n log n)** → rất ổn 👍



# ## 5. Ghi nhớ nhanh (đi thi / phỏng vấn)

# 📌 **Tháo k thanh liên tiếp → tạo k + 1 ô**
# 📌 **Hình vuông → lấy min(chiều cao, chiều rộng)**
# 📌 **Diện tích = cạnh²**

# ---

# Nếu bạn muốn mình:

# * ✍️ viết lại theo **phong cách LeetCode clean**
# * 🔁 đổi sang **Java**
# * 🧠 giải thích bằng **hình vẽ ASCII**

# cứ nói nhé 😄

# * Bạn có **một cái lưới hình chữ nhật** gồm:

#   * `n` **hàng** (horizontal)
#   * `m` **cột** (vertical)

# * Ban đầu, lưới được chia bởi:

#   * Các **thanh ngang** (horizontal bars)
#   * Các **thanh dọc** (vertical bars)

# * Sau đó:

#   * Một số **thanh ngang bị tháo bỏ** → được cho trong mảng `hBars`
#   * Một số **thanh dọc bị tháo bỏ** → được cho trong mảng `vBars`

# 👉 Khi các thanh bị tháo, **những ô nhỏ sẽ dính lại với nhau**, tạo thành **lỗ trống (hole)** lớn hơn.

# ---

# ## 2. Nhiệm vụ của bạn

# 👉 **Tìm diện tích lớn nhất của một lỗ hình vuông** có thể tạo ra sau khi tháo các thanh.

# * Lỗ đó **bắt buộc là hình vuông**
# * Diện tích = `cạnh × cạnh`

# ---

# ## 3. Ý nghĩa của `hBars` và `vBars`

# * `hBars[i]` = **chỉ số thanh ngang bị tháo**
# * `vBars[i]` = **chỉ số thanh dọc bị tháo**

# ⚠️ Các chỉ số này cho biết **khoảng cách giữa các đường kẻ**, không phải ô.

# ---

# ## 4. Tư duy trực quan

# ### 🔹 Thanh ngang

# * Nếu **nhiều thanh ngang liên tiếp bị tháo**
#   → chiều **cao** của lỗ tăng lên

# ### 🔹 Thanh dọc

# * Nếu **nhiều thanh dọc liên tiếp bị tháo**
#   → chiều **rộng** của lỗ tăng lên

# ---

# ## 5. Vì sao phải là hình vuông?

# * Giả sử:

#   * Chiều cao lớn nhất tạo được = `H`
#   * Chiều rộng lớn nhất tạo được = `W`

# 👉 Hình vuông lớn nhất có cạnh:

# ```
# min(H, W)
# ```

# 👉 Diện tích:

# ```
# min(H, W)²
# ```

# ---

# ## 6. Ví dụ minh họa (hiểu đề)

# Giả sử:

# ```
# n = 5, m = 5
# hBars = [1, 2]
# vBars = [2]
# ```

# * `hBars = [1,2]`
#   → tháo **2 thanh ngang liên tiếp**
#   → tạo chiều cao = **3 ô**

# * `vBars = [2]`
#   → chỉ tháo 1 thanh
#   → chiều rộng = **2 ô**

# 👉 Hình vuông lớn nhất:

# ```
# cạnh = min(3, 2) = 2
# diện tích = 2 × 2 = 4
# ```

# ---

# ## 7. Tóm tắt ngắn gọn

# 📌 Bài toán yêu cầu:

# 1. Tìm **đoạn dài nhất liên tiếp** trong `hBars` → chiều cao
# 2. Tìm **đoạn dài nhất liên tiếp** trong `vBars` → chiều rộng
# 3. Lấy **min(chiều cao, chiều rộng)**
# 4. Bình phương lên → **diện tích hình vuông lớn nhất**

# ---

# Nếu bạn muốn:

# * 👉 mình **vẽ hình minh họa**
# * 👉 hoặc **giải từng test case**
# * 👉 hoặc **viết code Java / C++ / Python**

# chỉ cần nói 👍
