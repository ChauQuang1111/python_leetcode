# //  Delete Nodes From Linked List Present (01/11/2025)

# // ```python
# // # Định nghĩa lớp ListNode cho danh sách liên kết đơn
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # Giá trị của node hiện tại
        self.next = next    # Con trỏ tới node kế tiếp


class Solution:
    def modifiedList(self, nums: list[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None  # Nếu danh sách liên kết rỗng thì trả về None

        sety = set(nums)  # Chuyển mảng nums thành tập hợp để tìm kiếm nhanh hơn O(1)

        # --- Bước 1: Loại bỏ các node đầu có giá trị thuộc sety ---
        while head and head.val in sety:
            head = head.next  # Di chuyển head tới node tiếp theo

        # Nếu tất cả các node bị loại bỏ thì danh sách rỗng
        if not head:
            return None

        # --- Bước 2: Duyệt qua phần còn lại của danh sách ---
        prev = head          # prev là node trước node đang xét
        curr = head.next     # curr là node hiện tại

        while curr:  # Duyệt đến khi hết danh sách
            if curr.val in sety:
                # Nếu node hiện tại có giá trị nằm trong sety → bỏ qua node này
                prev.next = curr.next
            else:
                # Nếu node hợp lệ → giữ lại node này
                prev = curr
            curr = curr.next  # Di chuyển sang node kế tiếp

        # --- Bước 3: Trả về danh sách đã được chỉnh sửa ---
        return head




# // **Giải thích thuật toán:**

# // 1. **Tạo tập hợp (`sety`)** từ `nums` để có thể kiểm tra nhanh xem một giá trị có cần bị xóa không (`O(1)` thời gian truy cập).
# // 2. **Bỏ qua các node đầu tiên** nếu giá trị của chúng nằm trong `nums`.
# // 3. Sau khi đã đến được node đầu tiên không bị xóa, ta bắt đầu **duyệt danh sách**:

# //    * Nếu `head.val` **không** nằm trong `sety`, giữ lại node đó.
# //    * Nếu `head.val` **nằm trong** `sety`, bỏ qua node đó.
# // 4. **Xử lý node cuối cùng**, đảm bảo rằng nếu nó cần bị xóa thì ngắt liên kết.
# // 5. **Trả về node đầu tiên hợp lệ (`temp`)**, là đầu của danh sách mới.

# // ⏱ **Độ phức tạp thời gian:** O(n)
# // 💾 **Độ phức tạp bộ nhớ:** O(k), với k là số phần tử trong `nums` (do dùng `set`).

# // ---

# // ## 🧩 **Đề bài gốc (LeetCode 3217: Delete Nodes From Linked List Present in Array)**

# // Bạn được cho:

# // 1. Một **mảng số nguyên `nums`**.
# // 2. Một **danh sách liên kết đơn `head`** (linked list) — mỗi node trong danh sách chứa một giá trị nguyên.

# // ---

# // ### 🎯 **Yêu cầu**

# // Hãy **xóa tất cả các node** trong linked list **có giá trị xuất hiện trong mảng `nums`**.

# // Sau khi xóa xong, **trả về con trỏ đến đầu danh sách mới (head mới)**.

# // ---

# // ### 🧠 **Ví dụ minh họa**

# // #### 📥 Input:

# // ```
# // nums = [1, 2, 3]
# // linked list: 1 -> 2 -> 3 -> 4 -> 5
# // ```

# // #### ⚙️ Quá trình xử lý:

# // * Các số cần xóa là: `1, 2, 3`
# // * Duyệt qua danh sách:

# //   * Node 1 (giá trị 1) → bị xóa (vì có trong nums)
# //   * Node 2 → bị xóa
# //   * Node 3 → bị xóa
# //   * Node 4 → giữ lại
# //   * Node 5 → giữ lại

# // #### 📤 Output:

# // ```
# // 4 -> 5
# // ```

# // ---

# // ### 💡 **Ý tưởng thuật toán**

# // 1. Dùng một **HashSet** (tập hợp) để lưu tất cả các giá trị trong `nums` → giúp kiểm tra nhanh xem một giá trị có nằm trong `nums` không (O(1)).
# // 2. Duyệt qua danh sách liên kết:

# //    * Nếu giá trị của node hiện tại **có trong HashSet** → bỏ qua node đó (xóa).
# //    * Nếu không → giữ lại node.
# // 3. Trả về con trỏ `head` mới của danh sách sau khi đã xóa.

# // ---

# // ### ⚙️ **Ví dụ 2**

# // #### Input:

# // ```
# // nums = [2, 5, 8]
# // head = 2 -> 8 -> 3 -> 5 -> 10 -> 2
# // ```

# // #### Quá trình:

# // * 2: xóa (vì có trong nums)
# // * 8: xóa
# // * 3: giữ lại
# // * 5: xóa
# // * 10: giữ lại
# // * 2: xóa

# // #### Output:

# # // ```
# # // 3 -> 10
# # // ```

# # // ---

# # // ### 🧮 **Độ phức tạp**

# # // * **Thời gian:** O(n + m)
# # //   (với n = số phần tử trong linked list, m = độ dài nums)
# # // * **Không gian:** O(m) cho HashSet.

# # // ---

# # // 👉 **Tóm lại:**

# # // > Bài này yêu cầu xóa các node trong danh sách liên kết nếu giá trị của chúng nằm trong mảng `nums`.
# # // > Cách nhanh nhất là dùng `HashSet` để lưu `nums`, rồi duyệt qua danh sách và bỏ qua những node có giá trị trùng.

# # // ---

# # // Bạn có muốn mình viết **code Java** (hoặc Python) có chú thích rõ từng bước cho bài này không?
