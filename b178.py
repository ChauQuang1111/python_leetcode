# Champagne Tower(14/02/2026)
# ## 🥂 Champagne Tower – Giải thích đề bài (LeetCode)

# Ok 👍 — mình sẽ **giải thích thuật toán + thêm chú thích trực tiếp vào code** để bạn đọc là hiểu ngay.

# ---

# # 🧠 Ý tưởng thuật toán (trước khi xem code)

# Bài này mô phỏng champagne chảy xuống tháp.

# Cách thường gặp:

# * Dùng mảng 2D `dp[row][col]`

# Nhưng code bạn gửi **tối ưu bộ nhớ → dùng 1D array**:

# * `glass[j]` = lượng champagne ở cột `j` của hàng hiện tại.
# * Cập nhật **từ phải → trái** để tránh ghi đè.

# Ngoài ra còn tối ưu:

# * Chỉ tính đến ly cần hỏi (`query_glass`)
# * Dùng đối xứng tam giác:
#   `query_glass = min(query_glass, query_row - query_glass)`

# ---

# # 🧾 Code đã thêm chú thích chi tiết

# ```python
class Solution:
    def champagneTower(self, poured, query_row, query_glass):

        # Dùng tính đối xứng của tháp
        # Ví dụ hàng 4: ly 0 và ly 4 giống nhau
        # → chỉ cần tính nửa bên trái
        query_glass = min(query_glass, query_row - query_glass)

        # Mảng 1D lưu lượng champagne của hàng hiện tại
        glass = [0.] * (query_glass + 1)

        # Đổ toàn bộ champagne vào ly trên cùng
        glass[0] = float(poured)

        # c = số ly tối đa cần xét (giới hạn trái)
        c = query_row - query_glass + 1

        # z = mốc dừng sớm khi bên trái đã hết tràn
        z = -1

        # Duyệt từng hàng
        for i in range(query_row):

            # mid = vị trí giữa của hàng i
            mid = i >> 1   # i // 2

            # Nếu giữa vượt quá ly cần tính → giới hạn lại
            if mid >= query_glass:
                mid, i1 = query_glass, 0
            else:
                i1 = i & 1   # kiểm tra i chẵn/lẻ

            # Tính phần tràn ở ly giữa
            excess = max(glass[mid] - 1., 0.)

            if excess:
                # Nếu hàng lẻ → có ly bên phải
                if i1 != 0:
                    glass[mid + 1] += excess

                # Ly giữa giữ lại phần tràn chia đôi
                glass[mid] = excess * .5
            else:
                # Nếu giữa không tràn → các ly ngoài cũng không tràn
                return 0.

            # Lan tràn từ giữa → trái
            for j in range(mid - 1, max(i - c, z), -1):

                # Tính phần tràn
                excess = max(glass[j] - 1., 0.) * .5

                if excess:
                    # Chia sang phải
                    glass[j + 1] += excess

                    # Giữ lại nửa
                    glass[j] = excess
                else:
                    # Nếu không tràn → dừng sớm
                    z = j
                    break

        # Kết quả tối đa là 1 (ly đầy)
        return min(1., glass[query_glass])
# ```

# ---

# # 🔍 Giải thích từng kỹ thuật tối ưu

# ## 1️⃣ Đối xứng tháp

# ```
#     0
#    0 1
#   0 1 2
# ```

# Ly trái = ly phải đối xứng.

# → Chỉ cần tính đến giữa → giảm bộ nhớ + thời gian.

# ---

# ## 2️⃣ 1D Dynamic Programming

# Thay vì:

# ```
# dp[row][col]
# ```

# Chỉ cần:

# ```
# glass[col]
# ```

# Vì mỗi hàng chỉ phụ thuộc hàng trước.

# ---

# ## 3️⃣ Cập nhật từ giữa → trái

# Tránh ghi đè dữ liệu chưa dùng.

# ---

# ## 4️⃣ Early stop (dừng sớm)

# Nếu 1 ly không tràn:

# → Các ly xa hơn cũng không tràn
# → Không cần tính tiếp.

# Biến dùng:

# ```
# z = mốc dừng
# ```

# ---

# # 📊 Độ phức tạp

# * Time: ~ O(query_row × query_glass)
#   (nhưng thực tế nhanh hơn nhờ dừng sớm)

# * Space: O(query_glass)
#   (tối ưu hơn 2D rất nhiều)

# ---

# # 🆚 So sánh với cách thường

# | Cách                 | Bộ nhớ    | Dễ hiểu  | Tốc độ     |
# | -------------------- | --------- | -------- | ---------- |
# | 2D DP                | Cao       | Dễ       | Trung bình |
# | 1D DP (code bạn)     | Thấp      | Khó      | Nhanh      |
# | 1D + tối ưu đối xứng | Thấp nhất | Khó nhất | Nhanh nhất |

# ---

# # Nếu bạn muốn mình làm tiếp, mình có thể:

# # * Viết lại code **phiên bản dễ hiểu hơn**
# # * Vẽ flow champagne từng bước
# # * So sánh với Pascal Triangle
# # * Chuyển sang Java / C++

# # Bạn muốn mình giải thích sâu đoạn nào nhất?


# # ### 1️⃣ Mô tả bài toán (hiểu đơn giản)

# # Bạn có một **tháp ly champagne xếp hình tam giác**:

# # * Hàng 0: 1 ly
# # * Hàng 1: 2 ly
# # * Hàng 2: 3 ly
# # * …

# Mỗi ly **chứa tối đa 1 cốc champagne**.

# Bạn rót vào ly trên cùng một lượng champagne là `poured` (số thực hoặc số nguyên).

# ---

# ### 2️⃣ Quy tắc tràn (overflow rule)

# * Nếu một ly **≤ 1** → giữ nguyên, không tràn.
# * Nếu **> 1** → phần dư sẽ tràn xuống **2 ly bên dưới**:

#   * Trái nhận: `(dư / 2)`
#   * Phải nhận: `(dư / 2)`

# Ví dụ:

# * Ly có 1.8 → giữ 1
# * Dư 0.8 → mỗi ly dưới nhận 0.4

# ---

# ### 3️⃣ Yêu cầu đề bài

# Cho 3 tham số:

# * `poured` → lượng champagne rót vào ly trên cùng
# * `query_row` → hàng cần hỏi
# * `query_glass` → vị trí ly trong hàng đó

# 👉 Hỏi: **Ly đó đang có bao nhiêu champagne?**
# (Kết quả tối đa là 1 vì ly đầy là dừng.)

# ---

# ### 4️⃣ Ví dụ minh họa

# #### Ví dụ 1

# ```
# poured = 1
# query_row = 1
# query_glass = 1
# ```

# * Rót 1 vào ly trên → vừa đầy, không tràn
# * Hàng dưới không nhận gì

# ➡️ Kết quả: `0`

# ---

# #### Ví dụ 2

# ```
# poured = 2
# query_row = 1
# query_glass = 1
# ```

# * Ly trên giữ 1
# * Dư 1 → chia đôi
# * Mỗi ly dưới nhận 0.5

# ➡️ Ly (1,1) có `0.5`

# ---

# #### Ví dụ 3 (hiểu bản chất lan truyền)

# ```
# poured = 4
# ```

# Luồng chảy:

# * Hàng 0: nhận 4 → giữ 1, dư 3
# * Hàng 1: mỗi ly nhận 1.5 → giữ 1, dư 0.5
# * Hàng 2: mỗi nhánh lại chia tiếp…

# ➡️ Champagne lan dần xuống dưới theo hình tam giác.

# ---

# ### 5️⃣ Bản chất thuật toán

# Đây là bài **mô phỏng + quy hoạch động (DP)**:

# * Mỗi ly phụ thuộc 2 ly phía trên.
# * Chỉ quan tâm **phần dư**.
# * Kết quả cuối cùng lấy `min(1, lượng trong ly)`.

# ---

# ### 6️⃣ Công thức tràn

# Nếu ly `(r, c)` có lượng `x`:

# ```
# overflow = max(0, x - 1)

# Ly (r+1, c)     += overflow / 2
# Ly (r+1, c+1)   += overflow / 2
# ```

# ---

# Nếu bạn muốn, mình có thể:

# * Viết code Java / Python giải bài này
# * Giải từng bước với ví dụ lớn
# * Giải thích cách tối ưu bộ nhớ (1D DP)

# Bạn muốn mình làm phần nào tiếp theo?
