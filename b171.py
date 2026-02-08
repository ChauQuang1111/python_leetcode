# Minimum Deletions to Make String Balanced(07/02/2026)

# Ok 👍 mình sẽ **giải thích thuật toán + thêm chú thích trực tiếp vào code** để bạn hiểu từng dòng.

# ---

# # 🧠 Ý tưởng thuật toán

# Ta duyệt chuỗi từ trái → phải.

# Giữ 2 biến:

# * `count` = số lượng `'b'` đã gặp ở bên trái
# * `res` = số lần xóa tối thiểu

# ---

# ## ⚖️ Nguyên tắc xử lý

# Khi gặp:

# ### 1️⃣ Ký tự `'b'`

# → Không sai thứ tự (vì b đứng trước b/a sau này chưa biết)

# 👉 Tăng `count`

# ---

# ### 2️⃣ Ký tự `'a'`

# Nếu bên trái **đã có `'b'`** (`count > 0`)
# → Sai thứ tự vì:

# ```
# ... b ... a
# ```

# Ta có 2 lựa chọn:

# | Cách | Xóa gì               |
# | ---- | -------------------- |
# | 1    | Xóa `'a'` hiện tại   |
# | 2    | Xóa 1 `'b'` trước đó |

# Thuật toán greedy chọn:

# 👉 Xóa `'b'` trước đó (giảm `count`)
# Và tăng số lần xóa `res`

# Vì làm vậy giữ được nhiều `'a'` phía sau hơn.

# ---

# # 📜 Code có chú thích

# ```python
class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = 0      # số lần xóa tối thiểu
        count = 0    # số lượng 'b' đã gặp bên trái

        # duyệt từng ký tự trong chuỗi
        for ch in s:

            # nếu là 'b'
            if ch == 'b':
                # tăng số lượng 'b' bên trái
                count += 1

            # nếu là 'a'
            # và trước đó đã có 'b'
            elif count:
                # cần xử lý vi phạm "b đứng trước a"

                # tăng số lần xóa
                res += 1

                # giả sử ta xóa 1 'b' trước đó
                # nên giảm count
                count -= 1
        
        # trả về kết quả
        return res


# # 🔍 Chạy thử từng bước

# Ví dụ:

# ```
# s = "aababbab"
# ```

# Ta lập bảng:

# | Ký tự | count(b bên trái) | res | Giải thích    |
# | ----- | ----------------- | --- | ------------- |
# | a     | 0                 | 0   | OK            |
# | a     | 0                 | 0   | OK            |
# | b     | 1                 | 0   | gặp b         |
# | a     | 0                 | 1   | xóa 1 b trước |
# | b     | 1                 | 1   | gặp b         |
# | b     | 2                 | 1   | gặp b         |
# | a     | 1                 | 2   | xóa 1 b trước |
# | b     | 2                 | 2   | gặp b         |

# 👉 Kết quả = **2**

# ---

# # 💡 Vì sao giảm `count`?

# Đoạn này quan trọng nhất:

# ```python
# res += 1
# count -= 1
# ```

# Ý nghĩa:

# * Ta quyết định xóa 1 `'b'` trước đó
# * Nên số `'b'` còn lại giảm

# Nếu không giảm → sẽ đếm sai.

# ---

# # 🧭 Trực giác dễ hiểu

# Hãy tưởng tượng:

# * `'b'` = người đứng sai hàng
# * `'a'` = người đúng hàng

# Khi thấy `'a'` đứng sau `'b'`:

# * Hoặc đuổi `'a'`
# * Hoặc đuổi 1 `'b'` trước

# Thuật toán chọn cách tối ưu hơn.

# ---

# ⏱️ Độ phức tạp

# * Time: **O(n)** (duyệt 1 lần)
# * Space: **O(1)** (chỉ 2 biến)

# → Rất tối ưu.

# ---

# Nếu bạn muốn mình giải thích thêm:

# * So sánh với DP solution
# * Vẽ hình minh họa trực quan
# * Viết bản Java
# * Giải thích vì sao greedy đúng

# Cứ nói mình nhé 👍





## 📖 Đề bài yêu cầu gì?

# Bạn được cho một chuỗi `s` chỉ gồm **2 ký tự**:

# * `'a'`
# * `'b'`

# Bạn được phép **xóa (delete)** bất kỳ ký tự nào trong chuỗi.

# 👉 Mục tiêu:
# Làm sao để sau khi xóa ít ký tự nhất, chuỗi trở thành **balanced**.

# ---

# ## 🔎 Balanced là gì?

# Chuỗi được gọi là **balanced** nếu:

# > Không có ký tự `'b'` nào đứng **trước** ký tự `'a'`.

# Nói cách khác:

# * Tất cả `'a'` phải đứng **bên trái**
# * Tất cả `'b'` phải đứng **bên phải**

# Dạng chuẩn của chuỗi balanced:

# ```
# aaaa....bbbb
# ```

# Cho phép:

# * Chỉ có `a` → OK
# * Chỉ có `b` → OK
# * Rỗng → OK

# ---

# ## 🧠 Ví dụ minh họa

# ### Ví dụ 1

# ```
# Input:  s = "aababbab"
# ```

# Chuỗi này chưa balanced vì có `'b'` đứng trước `'a'`.

# Ta có thể xóa:

# * Xóa 1 số `'a'` phía sau
# * Hoặc xóa 1 số `'b'` phía trước

# Kết quả tối ưu:

# ```
# "aabbbb"   (xóa 2 ký tự)
# ```

# 👉 Output: `2`

# ---

# ### Ví dụ 2

# ```
# Input: "bbaaaaabb"
# ```

# Có nhiều `'b'` ở đầu → vi phạm.

# Cách tốt nhất:

# * Xóa 2 ký tự `'b'` đầu

# Chuỗi thành:

# ```
# "aaaaabb"
# ```

# 👉 Output: `2`

# ---

# ## 💡 Hiểu bản chất bài toán

# Ta cần chọn **1 điểm chia** chuỗi thành 2 phần:

# ```
# [ bên trái ] | [ bên phải ]
# ```

# Điều kiện balanced:

# * Bên trái: chỉ nên có `'a'`
# * Bên phải: chỉ nên có `'b'`

# Những ký tự sai vị trí phải xóa:

# * `'b'` ở bên trái → xóa
# * `'a'` ở bên phải → xóa

# ---

# ## 🧮 Minh họa cách tính

# Ví dụ:

# ```
# s = "aababbab"
#         ^
#       điểm chia
# ```

# Ta đếm:

# * Số `'b'` bên trái
# * Số `'a'` bên phải

# Tổng = số ký tự cần xóa nếu chia tại đó.

# Làm với mọi điểm chia → lấy nhỏ nhất.

# ---

# ## 📌 Tóm tắt đề bài

# * Input: Chuỗi chỉ gồm `'a'` và `'b'`
# * Được phép xóa ký tự
# * Mục tiêu: Chuỗi không có `'b'` đứng trước `'a'`
# * Output: Số lần xóa ít nhất

# ---

# ## 🧭 Nhận diện nhanh khi làm bài

# Dấu hiệu nhận ra dạng này:

# * Chuỗi chỉ có 2 loại ký tự
# * Có thứ tự đúng/sai
# * Cho phép **delete**
# * Tối thiểu hóa số lần xóa

# → Thường dùng:

# * Prefix count
# * Dynamic Programming
# * Greedy

# ---

# Nếu bạn muốn, mình có thể:

# * Giải thích thuật toán O(n) dễ hiểu
# * Viết code Java / Python
# * Vẽ bảng chạy tay từng bước

# Bạn muốn mình giải thích theo cách nào tiếp theo?
