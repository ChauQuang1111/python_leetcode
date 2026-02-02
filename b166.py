# # // Ok, mình **giải thích đề bài “Divide an Array Into Subarrays With Minimum Cost II”** một cách **dễ hiểu, đi từ ý nghĩa → yêu cầu → ví dụ** nhé 👌
# # // (Đây là bài LeetCode, bản **II** là bản nâng cao hơn bản I.)
# Ok, mình **giải thích thuật toán của đoạn code này từng bước**, đúng theo logic bài **Divide an Array Into Subarrays With Minimum Cost II**, tập trung vào **ý tưởng + vì sao làm như vậy** (không chỉ đọc code) nhé 👍
# Ok 👍 mình **thêm chú thích trực tiếp vào code**, giải thích **từng dòng / từng khối**, để bạn có thể **đọc code là hiểu thuật toán ngay**.

# ---

# ```python
from typing import List
from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        
        # Hàm chuyển phần tử LỚN NHẤT từ left_set sang right_set
        # (vì left_set chỉ nên giữ các phần tử nhỏ nhất)
        def move_from_left_to_right():
            nonlocal current_sum
            element = left_set.pop()          # pop phần tử lớn nhất
            current_sum -= element            # loại khỏi tổng
            right_set.add(element)            # đưa sang right_set

        # Hàm chuyển phần tử NHỎ NHẤT từ right_set sang left_set
        # (khi left_set chưa đủ k phần tử)
        def move_from_right_to_left():
            nonlocal current_sum
            element = right_set.pop(0)        # pop phần tử nhỏ nhất
            left_set.add(element)             # đưa vào left_set
            current_sum += element            # cộng vào tổng

        # nums[0] đã bắt buộc được chọn
        # nên chỉ cần chọn thêm k - 1 phần tử
        k -= 1

        # Tổng ban đầu của cửa sổ đầu tiên (nums[1] → nums[dist+1])
        current_sum = sum(nums[:dist + 2])

        # left_set chứa các phần tử đang được chọn (k phần tử nhỏ nhất)
        left_set = SortedList(nums[1:dist + 2])

        # right_set chứa các phần tử còn lại trong cửa sổ
        right_set = SortedList()

        # Điều chỉnh để left_set chỉ còn đúng k phần tử nhỏ nhất
        while len(left_set) > k:
            move_from_left_to_right()

        # Giá trị nhỏ nhất ban đầu
        min_cost = current_sum

        # Trượt cửa sổ từ trái sang phải
        for i in range(dist + 2, len(nums)):
            
            # Phần tử rời khỏi cửa sổ
            outgoing_element = nums[i - dist - 1]

            # Nếu phần tử bị loại nằm trong left_set
            if outgoing_element in left_set:
                left_set.remove(outgoing_element)
                current_sum -= outgoing_element
            else:
                right_set.remove(outgoing_element)

            # Phần tử mới đi vào cửa sổ
            incoming_element = nums[i]

            # Nếu phần tử mới nhỏ hơn phần tử lớn nhất đang chọn
            # thì nó nên được đưa vào left_set
            if left_set and incoming_element < left_set[-1]:
                left_set.add(incoming_element)
                current_sum += incoming_element
            else:
                right_set.add(incoming_element)

            # Cân bằng lại: đảm bảo left_set có đúng k phần tử
            while len(left_set) < k:
                move_from_right_to_left()
            while len(left_set) > k:
                move_from_left_to_right()

            # Cập nhật kết quả nhỏ nhất
            min_cost = min(min_cost, current_sum)

        # Trả về tổng nhỏ nhất tìm được
        return min_cost
# ```

# ---

# ## 🧠 Ghi nhớ nhanh (để đọc code không bị rối)

# * `left_set`
#   👉 **k phần tử nhỏ nhất đang được chọn**
# #   👉 `current_sum` = tổng của `left_set`

# * `right_set`
#   👉 phần còn lại trong cửa sổ

# * Mỗi lần trượt cửa sổ:

#   * ❌ bỏ phần tử cũ
#   * ➕ thêm phần tử mới
#   * ⚖️ cân bằng lại để giữ đúng `k` phần tử nhỏ nhất

# ---

# Nếu bạn muốn mình:

# * ✂️ **Viết lại code gọn hơn**
# * 🧪 **Chạy trace từng bước với ví dụ cụ thể**
# * 🧩 **So sánh với heap / priority queue**
# * 🗣️ **Giải thích kiểu trả lời phỏng vấn**

# 👉 cứ nói, mình làm tiếp cho bạn nhé 😄

# ---

# ## 1️⃣ Ý tưởng cốt lõi của thuật toán

# Ta nhớ lại yêu cầu bài toán:

# * **Bắt buộc chọn `nums[0]`**
# * Chọn thêm **`k - 1` phần tử** nữa
# * Các phần tử được chọn phải nằm trong **cửa sổ độ dài `dist + 1`**
# * **Tổng nhỏ nhất**

# 👉 Vấn đề thực chất là:

# > Với mỗi cửa sổ hợp lệ, hãy **chọn `k - 1` số nhỏ nhất** trong cửa sổ đó

# ---

# ## 2️⃣ Vì sao phải dùng `SortedList` + Sliding Window?

# * Cửa sổ **trượt từ trái sang phải**
# * Mỗi bước:

#   * ❌ bỏ 1 phần tử cũ
#   * ➕ thêm 1 phần tử mới
# * Luôn cần:

#   * biết **`k - 1` phần tử nhỏ nhất**
#   * cập nhật **tổng nhanh**

# 👉 Dùng **2 tập hợp có sắp xếp**:

# * `left_set`: chứa **k phần tử nhỏ nhất đang được chọn**
# * `right_set`: chứa **các phần tử còn lại trong cửa sổ**

# ---

# ## 3️⃣ Chuẩn bị ban đầu

# ```python
# k -= 1
# ```

# ✔️ Vì `nums[0]` đã được chọn sẵn
# → ta chỉ cần chọn thêm `k - 1` phần tử nữa

# ---

# ```python
# current_sum = sum(nums[:dist + 2])
# left_set = SortedList(nums[1:dist + 2])
# right_set = SortedList()
# ```

# ### Giải thích:

# * Cửa sổ đầu tiên:

# ```
# nums[1] → nums[dist+1]
# ```

# * Ban đầu:

#   * cho tất cả vào `left_set`
#   * `current_sum` là tổng của chúng

# ---

# ```python
# while len(left_set) > k:
#     move_from_left_to_right()
# ```

# 👉 Giữ đúng:

# ```
# left_set = k phần tử nhỏ nhất
# ```

# * Nếu quá nhiều → đẩy phần tử **lớn nhất** sang `right_set`

# ---

# ## 4️⃣ Hai hàm phụ (rất quan trọng)

# ### 🔁 move_from_left_to_right()

# ```python
# element = left_set.pop()
# current_sum -= element
# right_set.add(element)
# ```

# * Lấy **phần tử lớn nhất** trong `left_set`
# * Loại khỏi tổng
# * Đưa sang `right_set`

# 👉 Mục đích: giữ `left_set` toàn số nhỏ

# ---

# ### 🔁 move_from_right_to_left()

# ```python
# element = right_set.pop(0)
# left_set.add(element)
# current_sum += element
# ```

# * Lấy **phần tử nhỏ nhất** bên phải
# * Đưa vào tập đang chọn
# * Cộng vào tổng

# ---

# ## 5️⃣ Sliding Window chính

# ```python
# for i in range(dist + 2, len(nums)):
# ```

# 👉 Cửa sổ trượt từng bước

# ---

# ### ❌ Bỏ phần tử cũ

# ```python
# outgoing_element = nums[i - dist - 1]
# ```

# * Đây là phần tử **rời khỏi cửa sổ**

# Nếu nó đang ở `left_set`:

# ```python
# current_sum -= outgoing_element
# ```

# Ngược lại:

# ```python
# right_set.remove(outgoing_element)
# ```

# ---

# ### ➕ Thêm phần tử mới

# ```python
# incoming_element = nums[i]
# ```

# So sánh với phần tử lớn nhất trong `left_set`:

# * Nếu **nhỏ hơn** → đáng được chọn
# * Nếu **lớn hơn** → cho vào `right_set`

# 👉 đảm bảo:

# ```
# left_set luôn chứa các số nhỏ nhất
# ```

# ---

# ### ⚖️ Cân bằng lại 2 tập

# ```python
# while len(left_set) < k:
#     move_from_right_to_left()
# while len(left_set) > k:
#     move_from_left_to_right()
# ```

# ✔️ Sau mỗi bước:

# ```
# left_set có đúng k phần tử
# ```

# ---

# ### 📉 Cập nhật kết quả

# ```python
# min_cost = min(min_cost, current_sum)
# ```

# 👉 `current_sum` = tổng nhỏ nhất của cửa sổ hiện tại
# 👉 Lấy min toàn bộ quá trình

# ---

# ## 6️⃣ Vì sao thuật toán này đúng & nhanh?

# ### ✅ Đúng vì:

# * Luôn chọn **k phần tử nhỏ nhất hợp lệ**
# * Luôn đảm bảo **khoảng cách ≤ dist**

# ### ⚡ Nhanh vì:

# * Mỗi bước:

#   * add / remove: `O(log n)`
# * Tổng thời gian:

# ```
# O(n log n)
# ```

# 👉 phù hợp với **bản II (n rất lớn)**

# ---

# ## 7️⃣ Tóm tắt một câu (rất quan trọng)

# > Thuật toán dùng **sliding window + two sorted sets** để luôn duy trì **k−1 phần tử nhỏ nhất trong phạm vi dist**, từ đó tìm **tổng nhỏ nhất** một cách hiệu quả.

# ---

# Nếu bạn muốn, mình có thể:

# * 🔍 Vẽ **minh họa từng bước bằng ví dụ**
# * 🧠 So sánh với **Priority Queue**
# * 🧾 Viết lại **phiên bản dễ hiểu hơn**
# * 💬 Giải thích kiểu **đi phỏng vấn LeetCode**

# 👉 nói mình chọn hướng nào nhé 😄

# // ---

# // ## 1️⃣ Ý nghĩa chung của đề bài

# // Bạn được cho:

# // * Một mảng số nguyên `nums`
# // * Hai số nguyên `k` và `dist`

# // 👉 Nhiệm vụ của bạn là **chia mảng thành các subarray (nhóm con)** sao cho **tổng chi phí (cost) là nhỏ nhất**, theo một **quy tắc chọn phần tử** cụ thể.

# // ---

# // ## 2️⃣ Luật chia mảng (rất quan trọng)

# // * **Phần tử đầu tiên của mảng (`nums[0]`) BẮT BUỘC phải được chọn**
# // * Ngoài `nums[0]`, bạn phải chọn thêm **`k - 1` phần tử nữa**
# // * Các phần tử được chọn phải thỏa mãn điều kiện **khoảng cách**

# // ### 📏 Điều kiện khoảng cách `dist`

# // Nếu bạn chọn một phần tử ở vị trí `i`
# // → thì **phần tử tiếp theo được chọn** phải nằm trong đoạn:

# // ```
# // i < j ≤ i + dist
# // ```

# // 👉 Nói đơn giản:
# // Bạn **không được chọn các phần tử cách nhau quá xa**.

# // ---

# // ## 3️⃣ Cost (chi phí) được tính như thế nào?

# // 👉 **Cost = tổng giá trị của `k` phần tử được chọn**

# // Mục tiêu cuối cùng:

# // > **Chọn đúng `k` phần tử (bao gồm `nums[0]`) sao cho tổng của chúng là NHỎ NHẤT**

# // ---

# // ## 4️⃣ Ví dụ minh họa

# // ```text
# // nums = [1, 3, 2, 6, 4]
# // k = 3
# // dist = 2
# // ```

# // ### Bước 1: Bắt buộc chọn

# // ```
# // 1 (nums[0])
# // ```

# // ### Bước 2: Chọn thêm 2 phần tử nữa

# // * Từ vị trí `0`, bạn chỉ được chọn trong `[1, 2]`
# //   → các giá trị là `3` và `2`

# // * Giả sử chọn `2` (nhỏ hơn)

# // * Từ vị trí của `2`, tiếp tục chọn trong phạm vi `dist`

# // 👉 Một cách chọn hợp lệ:

# // ```
# // 1 + 2 + 4 = 7
# // ```

# // 👉 Các cách khác có thể lớn hơn

# // ➡️ **Kết quả nhỏ nhất = 7**

# // ---

# // ## 5️⃣ Điểm KHÓ của bản II

# // So với bản I:

# // | Điểm            | Version I                 | Version II                       |
# // | --------------- | ------------------------- | -------------------------------- |
# // | Kích thước mảng | Nhỏ                       | Rất lớn                          |
# // | Cách làm        | Brute force / DP đơn giản | Sliding window + Heap / Multiset |
# // | Độ khó          | Trung bình                | Khó                              |

# // 👉 **Không thể thử tất cả cách chọn**, vì sẽ **TLE**
# // 👉 Phải dùng **cấu trúc dữ liệu** để:

# // * Luôn giữ `k-1` số **nhỏ nhất**
# // * Trong phạm vi `dist`

# // ---

# // ## 6️⃣ Tóm tắt ngắn gọn (để nhớ nhanh)

# // 📌 Bài toán yêu cầu:

# // * Chọn **k phần tử**
# // * **Bắt buộc có `nums[0]`**
# // * Khoảng cách giữa các phần tử ≤ `dist`
# // * **Tổng nhỏ nhất có thể**

# // 📌 Bản II:

# // * Không hỏi cách chia
# // * **Chỉ hỏi giá trị cost nhỏ nhất**

# // ---

# // Nếu bạn muốn:

# // * ✅ Giải thích **ý tưởng thuật toán**
# // * ✅ So sánh **bản I và bản II**
# // * ✅ Giải thích **theo code Java / C++ / Python**
# // * ✅ Giải thích kiểu **phỏng vấn – dễ nhớ**

# // 👉 cứ nói mình biết nhé 😄
