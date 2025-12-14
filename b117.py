# 2147. Number of Ways to Divide a Long Corridor(14/12/2025)
# Mình giải thích **đề bài LeetCode 2147 – Number of Ways to Divide a Long Corridor** thật dễ hiểu nhé 👌

# ---

# ## 📌 1. Mô tả bài toán (nói đơn giản)

# Bạn có **một hành lang dài** được biểu diễn bằng **chuỗi ký tự** `corridor`, chỉ gồm:

# * `'S'` → **Seat** (ghế)
# * `'P'` → **Plant** (cây)

# 👉 Ví dụ:

# ```
# "SPSPPSSP"
# ```

# ---

# ## 📌 2. Mục tiêu của bài toán

# Bạn cần **chia hành lang thành nhiều đoạn** bằng cách đặt **vách ngăn** (divider) sao cho:

# ### ✅ Mỗi đoạn phải có **CHÍNH XÁC 2 ghế (2 'S')**

# * Không được ít hơn
# * Không được nhiều hơn

# 🌱 Cây (`'P'`) có thể có bao nhiêu cũng được

# ---

# ## 📌 3. Bạn được phép đặt vách ngăn ở đâu?

# * Chỉ được đặt **giữa 2 ký tự liên tiếp**
# * Có thể đặt **0 hoặc nhiều vách ngăn**

# 📌 Ví dụ:

# ```
# S P S | P P | S S
# ```

# ---

# ## 📌 4. Yêu cầu cần trả về

# * **Số cách khác nhau** để chia hành lang thỏa điều kiện
# * Vì số rất lớn → **lấy kết quả mod (10^9 + 7)**

# ---

# ## 📌 5. Khi nào kết quả = 0 ❌

# ### ❌ Tổng số ghế (`'S'`) **không chia hết cho 2**

# → Không thể chia

# Ví dụ:

# ```
# "SPS" → có 3 ghế → 0 cách
# ```

# ### ❌ Ít hơn 2 ghế

# ```
# "S" → 0 cách
# ```

# ---

# ## 📌 6. Ví dụ minh họa

# ### 🔹 Ví dụ 1

# ```
# corridor = "SSPPSPS"
# ```

# Ghế: `S S | S S`

# * Có thể đặt vách ngăn giữa 2 nhóm ghế
# * Kết quả: **3 cách**

# ---

# ### 🔹 Ví dụ 2

# ```
# corridor = "PPSPSP"
# ```

# Ghế = 2 → chỉ có **1 đoạn**
# → **1 cách** (không cần vách ngăn)

# ---

# ### 🔹 Ví dụ 3

# ```
# corridor = "S"
# ```

# Chỉ có 1 ghế
# → **0 cách**

# ---

# ## 📌 7. Ý tưởng cốt lõi của bài toán 🧠

# * Ta **đếm ghế (`S`)**
# * Mỗi **cặp 2 ghế liên tiếp** tạo thành 1 đoạn
# * Giữa **2 đoạn hợp lệ**, số cây (`P`) quyết định:

#   * Có bao nhiêu vị trí đặt vách ngăn
#   * → **số cách nhân lên**

# 📌 Công thức tư duy:

# ```
# kết quả = tích (số vị trí có thể đặt vách giữa các cặp ghế)
# ```

# ---

# ## 📌 8. Tóm tắt ngắn gọn 🔥

# * `'S'` = ghế, `'P'` = cây
# * Mỗi đoạn = **đúng 2 ghế**
# * Đếm số cách đặt vách
# * Nếu số ghế lẻ → **0**
# * Kết quả lấy **mod 10^9 + 7**

# ---

# Nếu bạn muốn, mình có thể:

# * ✅ giải **bằng Python / Java**
# * ✅ vẽ **minh họa từng bước**
# * ✅ giải thích **tại sao nhân số cây**

# 👉 Cứ nói nhé!
# Mình giải thích **thuật toán + chú thích từng dòng code** cho bài **2147. Number of Ways to Divide a Long Corridor** theo cách **dễ hiểu nhất** nhé 👍
# (đoạn code này dùng **DP 3 trạng thái**, hơi “ảo” nên mình sẽ nói chậm và có ví dụ)

# ---

# ## 🔑 Ý tưởng cốt lõi (trước khi vào code)

# Ta duyệt hành lang **từ trái sang phải** và đếm số cách chia hợp lệ.

# Mỗi đoạn hợp lệ phải có **đúng 2 ghế (`S`)**.

# Thay vì cắt thật sự, ta dùng **DP với 3 trạng thái**:

### 🎯 Ý nghĩa 3 biến

# | Biến   | Ý nghĩa                                                                              |
# | ------ | ------------------------------------------------------------------------------------ |
# | `zero` | số cách chia khi **đã hoàn thành 1 đoạn (2 ghế)** và **sẵn sàng bắt đầu đoạn mới**   |
# | `one`  | số cách chia khi **đã gặp 1 ghế trong đoạn hiện tại**                                |
# | `two`  | số cách chia khi **chưa bắt đầu đoạn nào** hoặc **đang ở trạng thái hợp lệ ban đầu** |

# 👉 Ban đầu:

# * Chưa có ghế nào
# * Có **1 cách duy nhất** (chưa làm gì cả)

# ```python
# zero = 0
# one = 0
# two = 1

class Solution:
    def numberOfWays(self, corridor):
        MOD = 10**9 + 7
        
        # zero: số cách khi vừa kết thúc 1 đoạn (đã có đủ 2 ghế)
        # one : số cách khi đoạn hiện tại đã có 1 ghế
        # two : số cách ban đầu / chưa bắt đầu đoạn
        zero = 0
        one = 0
        two = 1

        # Duyệt từng ký tự trong hành lang
        for thing in corridor:
            
            # Nếu gặp GHẾ
            if thing == 'S':
                # Khi gặp ghế:
                # - các cách có 1 ghế (one) -> hoàn thành 1 đoạn => zero
                # - các cách hợp lệ (two) -> bắt đầu đoạn mới => one
                zero = one
                one, two = two, one

            # Nếu gặp CÂY
            else:
                # Cây không ảnh hưởng đến số ghế
                # Nhưng nếu đã hoàn thành đoạn (zero),
                # ta có thể đặt vách ngăn tại đây
                two = (two + zero) % MOD

        # Kết quả là số cách kết thúc đúng tại trạng thái hoàn thành đoạn
        return zero


## 🧠 Giải thích trực giác bằng ví dụ

# Ví dụ:

# ```
# corridor = "SPSPS"
# ```

# | Ký tự | zero | one | two | Giải thích                 |
# | ----- | ---- | --- | --- | -------------------------- |
# | start | 0    | 0   | 1   | ban đầu                    |
# | S     | 0    | 1   | 0   | bắt đầu đoạn               |
# | P     | 0    | 1   | 0   | cây không đổi              |
# | S     | 1    | 0   | 1   | đủ 2 ghế → hoàn thành đoạn |
# | P     | 1    | 0   | 2   | có thêm vị trí đặt vách    |
# | S     | 0    | 2   | 0   | bắt đầu đoạn mới           |

# 👉 **kết quả = zero**

# ---

# ## 📌 Vì sao `return zero`?

# * `zero` đại diện cho **những cách kết thúc với đủ 2 ghế**
# * Các trạng thái khác (`one`, `two`) là **chưa hợp lệ**



# ## 🧾 Tóm tắt ngắn gọn

# * Đây là **DP một lần duyệt**
# * Không cần đếm ghế trước
# * Tự động loại trường hợp sai (ghế lẻ)
# * Time: **O(n)**
# * Space: **O(1)**

# ---

# Nếu bạn muốn:

# * 🔍 mình **vẽ bảng chạy từng bước**
# * 🔁 viết lại bằng **Java**
# * 🤔 giải thích lại theo kiểu “đếm khoảng P giữa các cặp S”

# 👉 cứ nói nhé!
