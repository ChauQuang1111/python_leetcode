# Count Mentions Per User(12/12/2025)
# Dưới đây là **giải thích đề bài "Count Mentions Per User"** (LeetCode 3591).
# Dưới đây là **giải thích thuật toán** + **code đã được thêm chú thích đầy đủ, cực dễ hiểu**.

# ---

# # ✅ **Giải thích đề bài (ngắn gọn – dễ hiểu)**

# Bạn có:

# * `numberOfUsers`: số user, từ **0 → numberOfUsers - 1**
# * `events`: danh sách sự kiện, mỗi sự kiện có dạng:

# ```
# ["ENTER", timestamp, userId]
# ["MESSAGE", timestamp, "ALL"]
# ["MESSAGE", timestamp, "HERE"]
# ["MESSAGE", timestamp, "id1 id2 ..."]
# ```

# ### ✔ Nhiệm vụ:

# Đếm xem mỗi user được *mention* bao nhiêu lần.

# ---

# # 🧠 **Quy tắc mention:**

# ### ✔ `"MESSAGE" ... "ALL"`

# → Tất cả user đều được +1 mention.

# ### ✔ `"MESSAGE" ... "HERE"`

# → Chỉ những user **đang online tại timestamp đó** mới +1.
# User online nếu:

# ```
# ENTER tại t  → online từ t đến t+60
# ```

# ### ✔ `"MESSAGE" ... "id3 id7"`

# → Mention trực tiếp từng ID trong danh sách.

### ✔ `"ENTER"` event

# → Đánh dấu user online trong 60 giây.

# ---

# # 🔥 **Vì sao phải sort events trước?**

# Vì events có thể **không theo đúng thứ tự thời gian**, nên cần:

# ```
# sort theo timestamp tăng dần
# nếu cùng timestamp thì MESSAGE xử lý sau ENTER
# ```

# Mã sort:

# ```python
# events.sort(key=lambda x: (int(x[1]), x[0] == "MESSAGE"))
# ```

# ---

# # ✅ **Code Python đã thêm chú thích cực chi tiết**

# ```python
from typing import List
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        
        # mentions[i] = số lần user i được mention
        mentions = [0] * numberOfUsers
        
        # onlineUsersTime[i] = thời điểm user i hết online (t + 60)
        onlineUsersTime = [0] * numberOfUsers

        # Sắp xếp sự kiện theo:
        # 1. timestamp tăng dần
        # 2. nếu cùng timestamp thì ENTER trước MESSAGE
        events.sort(key=lambda x: (int(x[1]), x[0] == "MESSAGE"))

        # Duyệt từng event theo thời gian
        for msg, when, who in events:
            time = int(when)

            # ==========================
            #       XỬ LÝ MESSAGE
            # ==========================
            if msg == "MESSAGE":

                # Trường hợp "MESSAGE ALL"
                if who == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1

                # Trường hợp "MESSAGE HERE"
                elif who == "HERE":
                    for i in range(numberOfUsers):
                        # user đang online nếu time >= onlineUsersTime[i]
                        if time >= onlineUsersTime[i]:
                            mentions[i] += 1

                # Trường hợp direct mention: "id1 id2 ..."
                else:
                    # ví dụ: who = "id3 id7"  → replace("id","") → "3 7"
                    for u in who.replace("id", "").split():
                        mentions[int(u)] += 1

            # ==========================
            #       XỬ LÝ ENTER
            # ==========================
            else:
                # User online trong vòng 60 giây
                # ENTER lúc t → online đến t + 60
                onlineUsersTime[int(who)] = time + 60
        
        return mentions


# 📌 **Giải thích thuật toán (ý tưởng chính)**

# 1. **Sort tất cả sự kiện theo thời gian** để xử lý đúng thứ tự.
# 2. Với mỗi `"ENTER"`, đánh dấu user online đến `time + 60`.
# 3. Khi gặp `"MESSAGE"`:

#    * `"ALL"` → tất cả user +1.
#    * `"HERE"` → chỉ user đang online +1.
#    * `"idX idY"` → các user được nhắc tên trực tiếp +1.
# 4. Trả về danh sách mentions cho từng user.

# ---

# # 🎉 Nếu bạn muốn:

# * Viết lại bằng **Java**
# * Giải thích bằng hình minh họa
# * Thêm **test case** minh hoạ từng loại event

# 👉 Chỉ cần bảo mình, mình làm ngay cho bạn!

# ---

# # 📌 **📝 Đề bài yêu cầu gì?**

# Bạn được cho:

# * Một danh sách các **tin nhắn** (messages).
# * Mỗi tin nhắn là một chuỗi ký tự, có thể chứa các **mention** dạng:
#   **"@username"**

# Nhiệm vụ của bạn:

# ### 👉 **Đếm số lần mỗi user được mention**, và trả về danh sách kết quả dạng:

# ```
# [userName, count]
# ```

# theo thứ tự **tăng dần theo userName** (alphabetical order).

# ---

# # 📌 **Mentions hợp lệ theo quy tắc:**

# Một mention có dạng:

# ```
# @<username>
# ```

# Trong đó:

# ### ✔ username phải thỏa:

# 1. **Chỉ chứa chữ cái thường (a-z)**
# 2. **Độ dài 1–15**
# 3. **Ngay trước @ phải là dấu cách hoặc là ký tự đầu tiên chuỗi**
# 4. **Ngay sau username phải là khoảng trắng, dấu chấm, dấu phẩy hoặc hết chuỗi**

# Ví dụ hợp lệ:

# * `"@alice"`
# * `"hello @bob."`
# * `"@john_doe"` ❌ (không hợp lệ vì có `_`)

# Không hợp lệ:

# * `"abc@alice"` (trước @ không phải khoảng trắng)
# * `"@Alice"` (A viết hoa)
# * `"@@bob"` (username rỗng)
# * `"@bob123"` (chứa số)

# ---

# # 📌 **Kết quả mong muốn**

# Input:

# ```
# ["hi @alice and @bob", "ping @alice.", "no mention here"]
# ```

# Output:

# ```
# [
#   ["alice", 2],
#   ["bob", 1]
# ]
# ```

# ---

# # 📌 **Tóm tắt lại đề bài thật dễ hiểu**

# Bạn chỉ cần:

# ### 🔍 1. Duyệt từng message

# ### 🔧 2. Tìm tất cả các @username hợp lệ

# ### 🧮 3. Đếm số lần xuất hiện của mỗi username

# ### 🗂️ 4. Trả về danh sách `[username, count]`, sort theo tên

# ---

# # Nếu bạn cần:

# * Giải thích thuật toán mẫu
# * Thêm code Java / Python kèm chú thích
# * Minh họa từng trường hợp hợp lệ / không hợp lệ

# 👉 Chỉ cần bảo mình, mình viết cho bạn!
