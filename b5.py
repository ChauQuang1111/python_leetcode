# 27. Remove Element (16/08/2025)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range (len(nums)):
            if(nums[i]!=val):
                nums[k]=nums[i]
                k+=1
        return k  
    




# Đoạn code này là một giải pháp hiệu quả cho bài toán **"xóa phần tử"** (remove element) khỏi một mảng. Mặc dù nó không thực sự xóa các phần tử, nó di chuyển tất cả các phần tử **không cần xóa** về phía đầu mảng.

# ### Giải thích thuật toán

# Thuật toán này sử dụng một kỹ thuật gọi là **hai con trỏ (two-pointers)**:

# * **Con trỏ đọc `i`**: Con trỏ này duyệt qua toàn bộ mảng từ đầu đến cuối. Nó có nhiệm vụ "đọc" từng phần tử.
# * **Con trỏ ghi `k`**: Con trỏ này chỉ định vị trí tiếp theo để "ghi" một phần tử hợp lệ vào. Nó chỉ tăng khi một phần tử được giữ lại.

# Thuật toán hoạt động theo các bước sau:

# 1.  **Khởi tạo**: Đặt con trỏ `k` ban đầu bằng 0.
# 2.  **Duyệt mảng**: Vòng lặp `for` sử dụng con trỏ `i` để duyệt qua từng phần tử của mảng `nums`.
# 3.  **Kiểm tra điều kiện**: Trong mỗi lần lặp, nó kiểm tra xem phần tử hiện tại `nums[i]` có khác với giá trị cần xóa `val` không.
#     * **Nếu `nums[i] != val`**: Điều này có nghĩa là chúng ta muốn giữ lại phần tử này. Thuật toán sẽ gán giá trị của `nums[i]` vào vị trí `nums[k]`, sau đó tăng `k` lên 1 để chuẩn bị cho vị trí tiếp theo.
#     * **Nếu `nums[i] == val`**: Phần tử này bị bỏ qua. Con trỏ `k` không thay đổi, vì vậy vị trí hiện tại của `k` sẽ bị ghi đè bởi phần tử hợp lệ tiếp theo.
# 4.  **Kết quả**: Sau khi vòng lặp kết thúc, `k` sẽ đại diện cho số lượng phần tử hợp lệ đã được di chuyển về phía đầu mảng. Hàm trả về `k` chính là độ dài mới của mảng.

# ### Ví dụ minh họa

# Hãy xem ví dụ với `nums = [3, 2, 2, 3]` và `val = 3`.

# * **Khởi tạo**: `k = 0`.
# * **i = 0**: `nums[0]` là 3. Vì `3 == val`, bỏ qua.
# * **i = 1**: `nums[1]` là 2. Vì `2 != val`, ta thực hiện:
#     * `nums[k] = nums[i]` (nghĩa là `nums[0] = nums[1]`). Mảng trở thành `[2, 2, 2, 3]`.
#     * `k` tăng lên 1, bây giờ `k = 1`.
# * **i = 2**: `nums[2]` là 2. Vì `2 != val`, ta thực hiện:
#     * `nums[k] = nums[i]` (nghĩa là `nums[1] = nums[2]`). Mảng vẫn là `[2, 2, 2, 3]`.
#     * `k` tăng lên 1, bây giờ `k = 2`.
# * **i = 3**: `nums[3]` là 3. Vì `3 == val`, bỏ qua.

# Vòng lặp kết thúc. Hàm trả về `k` là **2**. Mảng `nums` ban đầu được thay đổi thành `[2, 2, 2, 3]`, và độ dài mới hợp lệ là 2.    