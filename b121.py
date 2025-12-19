# Find All People With Secret(19/12/2025)
# Dưới đây là **giải thích đề bài “Find All People With Secret” bằng tiếng Việt**, viết **dễ hiểu – đúng trọng tâm – đúng kiểu LeetCode**.

# ---

# ## 📌 Mô tả đề bài (Diễn giải)

# Có **n người**, được đánh số từ `0` đến `n - 1`.

# * **Ban đầu**:

#   * Người `0` biết một **bí mật**
#   * Người `firstPerson` cũng biết bí mật này

# * Bạn được cho một danh sách `meetings`

#   ```
#   meetings[i] = [xi, yi, timei]
#   ```

#   nghĩa là:

#   * người `xi` gặp người `yi`
#   * tại thời điểm `timei`

# ---

# ## 🔁 Quy tắc truyền bí mật

# * Nếu **một người biết bí mật** gặp **người khác**
#   → người kia sẽ biết bí mật
# * **Chỉ truyền trong cùng thời điểm**

#   * Bí mật **không được “ghi nhớ” qua các cuộc họp ở thời điểm khác**
#   * Một người **chỉ có thể truyền bí mật nếu họ đã biết bí mật trước hoặc tại thời điểm đó**

# ---

# ## 🎯 Mục tiêu

# 👉 Hãy **trả về danh sách tất cả những người biết bí mật sau khi tất cả các cuộc họp kết thúc**

# * Thứ tự trả về **không quan trọng**

# ---

# ## 🧠 Ví dụ minh họa

# ### Ví dụ 1

# ```python
# n = 6
# firstPerson = 1
# meetings = [
#     [1, 2, 5],
#     [2, 3, 8],
#     [1, 5, 10]
# ]
# ```

# ### Phân tích:

# * Ban đầu: `{0, 1}` biết bí mật
# * Thời điểm 5:

#   * 1 gặp 2 → 2 biết bí mật
# * Thời điểm 8:

#   * 2 gặp 3 → 3 biết bí mật
# * Thời điểm 10:

#   * 1 gặp 5 → 5 biết bí mật

# ### ✅ Kết quả:

# ```python
# [0, 1, 2, 3, 5]
# ```

# ---

# ## ⚠️ Điểm quan trọng dễ sai

# ### ❌ Sai lầm thường gặp

# * Cho rằng chỉ cần gặp nhau là truyền được bí mật
# * Không xét **thời gian**
# * Dùng DFS/BFS cho toàn bộ graph (sai vì mỗi thời điểm là độc lập)

# ### ✅ Điều cần nhớ

# | Điều kiện                | Giải thích                      |
# | ------------------------ | ------------------------------- |
# | Thời gian rất quan trọng | Chỉ truyền trong cùng `time`    |
# | Graph tạm                | Mỗi time block là 1 graph riêng |
# | Biết trước mới truyền    | Không “quay ngược thời gian”    |

# ---

# ## 🧩 Vì sao bài này khó?

# * Không phải graph thông thường
# * Là **graph theo thời gian**
# * Phải:

#   * sort theo time
#   * xử lý từng nhóm thời gian
#   * reset trạng thái sau mỗi time block

# ---

# ## 🧠 Cách tư duy khi gặp bài này

# > “Tại mỗi thời điểm, chỉ những người đã biết bí mật mới có quyền lan truyền nó cho những người họ gặp **cùng thời điểm**.”

# ---

# Nếu bạn muốn:

# * 🔍 Ví dụ chi tiết hơn từng bước
# * 🧠 So sánh **DFS vs Union-Find**
# * ✍️ Gợi ý cách trình bày khi phỏng vấn

# 👉 cứ nói, mình giải thích tiếp nhé 💪

# Dưới đây là **giải thích thuật toán bằng tiếng Việt** + **phiên bản code đã được thêm chú thích chi tiết từng bước** để bạn dễ học và dễ trình bày khi phỏng vấn / làm bài LeetCode.

# ---

# ## 🧠 Ý tưởng & Thuật toán

# **Bài toán:**
# Có `n` người, ban đầu **người 0** và `firstPerson` biết bí mật.
# Các cuộc họp diễn ra tại những **thời điểm khác nhau**.
# → Nếu một người biết bí mật và **gặp người khác tại cùng thời điểm**, họ sẽ truyền bí mật.

# ---

### 🔑 Chiến lược chính

# 1. **Sắp xếp meetings theo thời gian**

#    * Để xử lý các cuộc họp theo đúng thứ tự xảy ra.

# 2. **Xử lý theo từng “khối thời gian”**

#    * Tại mỗi thời điểm `t`, tạo **graph tạm thời** gồm các cuộc họp diễn ra đúng thời điểm đó.
#    * Chỉ những người đã biết bí mật **trước hoặc tại thời điểm t** mới có thể truyền bí mật.

# 3. **DFS trong từng khối thời gian**

#    * Nếu một người biết bí mật xuất hiện trong graph tại thời điểm đó
#      → lan truyền bí mật cho tất cả người kết nối với họ trong graph này.

# 4. **Sau khi sang thời điểm mới**

#    * Xóa graph cũ
#    * Reset visited (vì mỗi time block là độc lập)

# ---

# ### ⏱ Độ phức tạp

# * **Time:** `O(m log m)` (do sort meetings)
# * **Space:** `O(n + m)`

# ---

# ## ✅ Code đã được chú thích đầy đủ

# ```python
from typing import List
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        """
        Ý tưởng:
        - Sắp xếp các cuộc họp theo thời gian
        - Với mỗi thời điểm, xây dựng graph tạm
        - Dùng DFS để lan truyền bí mật trong cùng thời điểm
        """

        # 1. Sắp xếp meetings theo thời gian tăng dần
        meetings.sort(key=lambda x: x[2])

        # 2. Những người hiện đang biết bí mật
        secretPeople = set([0, firstPerson])

        # Graph tạm cho mỗi khối thời gian
        person2people = {}

        # Đánh dấu các node đã DFS trong cùng time block
        visit = set()

        # DFS để lan truyền bí mật
        def dfs(person):
            if person in visit:
                return
            visit.add(person)
            secretPeople.add(person)

            for nei in person2people.get(person, []):
                dfs(nei)

        prev_time = -1

        # 3. Duyệt từng cuộc họp
        for p1, p2, t in meetings:

            # Nếu sang thời điểm mới → xử lý xong time block cũ
            if t != prev_time:
                # Lan truyền bí mật trong graph của time block trước
                for person in person2people:
                    if person in secretPeople and person not in visit:
                        dfs(person)

                # Reset graph & visited cho time block mới
                person2people = {}
                visit = set()
                prev_time = t

            # 4. Xây graph cho time block hiện tại
            person2people.setdefault(p1, []).append(p2)
            person2people.setdefault(p2, []).append(p1)

        # 5. Xử lý time block cuối cùng
        for person in person2people:
            if person in secretPeople and person not in visit:
                dfs(person)

        return list(secretPeople)
# ```

# ---

# ## 📌 Tóm tắt ngắn gọn (rất hay dùng khi giải thích miệng)

# > “Ta xử lý các cuộc họp theo thứ tự thời gian.
# > Với mỗi thời điểm, ta tạo một graph tạm thời.
# > Nếu trong graph đó có người đã biết bí mật, ta dùng DFS để lan truyền bí mật cho tất cả người kết nối với họ trong cùng thời điểm.”

# ---

# Nếu bạn muốn:

# * 🔄 Viết lại bằng **Union-Find**
# * 🧪 Giải thích bằng **ví dụ minh họa từng bước**
# * 🎯 Tối ưu hoặc rút gọn code cho phỏng vấn

# 👉 cứ nói, mình hỗ trợ tiếp nhé 👍
