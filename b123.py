# Delete Columns to Make Sorted II(21/12/2025)
# Bài **Delete Columns to Make Sorted II** (LeetCode 955) yêu cầu hiểu hơi “xoắn” hơn bản I. Mình giải thích **ý nghĩa đề bài** trước, chưa cần code.
# Mình sẽ **giải thích thuật toán từng bước** và **thêm chú thích trực tiếp vào code** để bạn nhìn là hiểu ngay 👍
# (Bài này chính là **Delete Columns to Make Sorted II – LeetCode 955**)

# ---

# ## 🧠 Ý tưởng cốt lõi của thuật toán

# * Ta duyệt **từng cột từ trái → phải**
# * So sánh **các cặp chuỗi kề nhau** `(strs[i], strs[i+1])`
# * Với mỗi cặp:

#   * Nếu đã **phân định thứ tự** ở cột trước → không cần so nữa
#   * Nếu chưa phân định:

#     * Nếu cột hiện tại làm **sai thứ tự** → **bắt buộc xóa cột**
#     * Nếu giúp **xác định đúng thứ tự** → đánh dấu là đã “resolved”

# 👉 Chỉ khi **không gây lỗi**, ta mới giữ cột

# ---

## 🔑 Ý nghĩa các biến quan trọng

# * `resolved[i] = True`
#   → cặp `strs[i] < strs[i+1]` **đã được quyết định** ở cột trước

# * `unresolved`
#   → số cặp **chưa phân định thứ tự**

# * `bad`
#   → cột hiện tại **làm sai thứ tự**, phải xóa

# ---

## ✅ Code + chú thích chi tiết
from typing import List
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)          # số chuỗi
        m = len(strs[0])       # độ dài mỗi chuỗi (số cột)

        # resolved[i] = True nghĩa là:
        # strs[i] và strs[i+1] đã được xác định thứ tự đúng
        resolved = [False] * (n - 1)

        unresolved = n - 1     # số cặp chuỗi chưa xác định thứ tự
        deletions = 0          # số cột cần xóa

        # Duyệt từng cột từ trái sang phải
        for col in range(m):

            # Nếu tất cả cặp đã xác định thứ tự
            # thì không cần xét thêm cột nữa
            if unresolved == 0:
                break

            bad = False

            # Kiểm tra xem cột này có làm sai thứ tự không
            for i in range(n - 1):
                # Chỉ xét các cặp chưa resolved
                if not resolved[i] and strs[i][col] > strs[i + 1][col]:
                    bad = True
                    break

            # Nếu cột này gây sai thứ tự → phải xóa
            if bad:
                deletions += 1
                continue   # bỏ qua cột này, không cập nhật resolved

            # Nếu cột không gây lỗi
            # thì cập nhật các cặp được xác định thứ tự
            for i in range(n - 1):
                if not resolved[i] and strs[i][col] < strs[i + 1][col]:
                    resolved[i] = True
                    unresolved -= 1

        return deletions


# ## 📌 Ví dụ minh họa nhanh

# ```text
# strs = ["ca", "bb", "ac"]
# ```

# ### Cột 0:

# ```
# c > b ❌  → bad → xóa cột
# ```

# ### Cột 1:

# ```
# a < b < c ✅
# → các cặp được resolved
# ```

# 👉 Kết quả: `1`

# ---

# ## 🧠 Tại sao thuật toán này đúng?

# # * Ta **chỉ xóa cột khi bắt buộc**
# # * Mỗi cột giữ lại đều:

# #   * Không phá thứ tự đã có
# #   * Có thể giúp xác định thêm thứ tự mới
# # * Đây là chiến lược **greedy hợp lệ**

# # ---

# # Nếu bạn muốn:

# # * 🔍 Trace từng bước với test cụ thể
# # * ✍️ Viết lại bằng Java
# # * 🧪 Giải thích tại sao `resolved` là mấu chốt
# # * 📊 Phân tích độ phức tạp

# # 👉 cứ nói tiếp nhé 😄

# # ---

# # ## 📌 Đề bài nói gì?

# * Bạn được cho một mảng `strs` gồm **n chuỗi**,
# * **Tất cả các chuỗi có cùng độ dài** `m`.
# * Mỗi chuỗi là **một hàng**, mỗi vị trí ký tự là **một cột**.

# 👉 Bạn **được phép xóa một số cột** (xóa cùng vị trí ở tất cả các chuỗi).

# ### 🎯 Mục tiêu

# Sau khi xóa các cột đó, mảng chuỗi còn lại phải **được sắp xếp theo thứ tự từ điển (lexicographically)** **từ trên xuống dưới**.

# 👉 Hỏi: **Ít nhất phải xóa bao nhiêu cột?**

# ---

# ## 📘 Nhắc lại: Thứ tự từ điển (lexicographical)

# Giống như từ điển:

# * `"abc" < "abd"` vì `c < d`
# * So sánh **từ trái sang phải**
# * Gặp ký tự khác đầu tiên thì quyết định luôn

# ---

# ## 🔍 Ví dụ để hiểu rõ

# ### Ví dụ 1

# ```text
# strs = ["ca", "bb", "ac"]
# ```

# So sánh theo thứ tự:

# * `"ca"` > `"bb"` ❌ (sai thứ tự)
# * `"bb"` > `"ac"` ❌

# ➡️ **Chưa được sắp xếp**

# ---

# ### Thử xóa cột 0:

# ```text
# ["a", "b", "c"]
# ```

# Bây giờ:

# ```
# "a" < "b" < "c" ✅
# ```

# 👉 Chỉ cần xóa **1 cột**

# ---

# ## ❗ Điểm khác biệt quan trọng so với Delete Columns to Make Sorted I

# ### ❌ Bản I:

# * Chỉ cần **mỗi cột tự nó tăng dần từ trên xuống**
# * Các cột **độc lập**

# ### ✅ Bản II:

# * Phải đảm bảo **cả chuỗi** được sắp xếp
# * **Các cột phụ thuộc lẫn nhau**
# * Một cột có thể “cứu” hoặc “phá” thứ tự của cột trước

# 👉 Đây là lý do bài này **khó hơn nhiều**

# ---

# ## 🧠 Ý tưởng logic của đề bài (không phải code)

# * Ta **xét các cột từ trái sang phải**
# * Giữ một trạng thái:

#   * Cặp chuỗi nào **đã chắc chắn đúng thứ tự**
#   * Cặp nào **chưa quyết định** (vẫn bằng nhau ở các cột trước)
# * Nếu một cột mới:

#   * Làm **vi phạm thứ tự** cho các cặp chưa quyết định
#     👉 **bắt buộc phải xóa cột đó**
#   * Nếu không vi phạm:
#     👉 giữ lại và cập nhật trạng thái

# ---

# ## 🧩 Tóm tắt đề bài ngắn gọn

# > Cho nhiều chuỗi cùng độ dài.
# > Xóa ít nhất số cột sao cho **sau khi xóa**, các chuỗi **được sắp xếp từ điển từ trên xuống dưới**.

# ---

# Nếu bạn muốn:

# * ✅ Giải thích **bằng ví dụ từng bước**
# * ✅ So sánh **Delete Columns I vs II**
# * ✅ Giải thích **ý tưởng thuật toán bằng hình dung dễ hiểu**
# * ✅ Hoặc **code Java / Python**

# 👉 cứ nói mình nhé 👍

