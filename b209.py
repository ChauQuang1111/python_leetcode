# Bài **Find Unique Binary String** (08/03/2026)

# Thuật toán trong code của bạn sử dụng **Cantor Diagonal Trick**. Ý tưởng là:
# Tạo một chuỗi mới sao cho **khác với mỗi chuỗi trong `nums` ít nhất 1 vị trí**.

# Cụ thể:

# * Với chuỗi thứ `i` trong `nums`
# * Lấy **ký tự thứ `i` của chính chuỗi đó**
# * **Đảo bit** (`0 → 1`, `1 → 0`)
# * Ghép lại thành chuỗi kết quả

# Như vậy:

# * Chuỗi mới **khác chuỗi `nums[0]` tại vị trí 0**
# * Khác `nums[1]` tại vị trí 1
# * Khác `nums[2]` tại vị trí 2
#   → nên **không thể trùng với bất kỳ chuỗi nào trong `nums`**.

# ---

# ## Code có chú thích

# ```python
from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Tạo list để lưu từng ký tự của chuỗi kết quả
        ans = []

        # Duyệt qua từng chỉ số i (0 -> n-1)
        for i in range(len(nums)):
            
            # Lấy ký tự ở vị trí i của chuỗi nums[i]
            # Đây là phần tử trên đường chéo của ma trận chuỗi
            curr = nums[i][i]

            # Đảo bit:
            # nếu là '0' thì đổi thành '1'
            # nếu là '1' thì đổi thành '0'
            # mục đích: đảm bảo chuỗi mới khác nums[i] tại vị trí i
            ans.append("1" if curr == "0" else "0")
        
        # Ghép các ký tự trong ans lại thành một chuỗi hoàn chỉnh
        return "".join(ans)


## Ví dụ chạy thuật toán

# ```
# nums = ["010",
#         "111",
#         "001"]
# ```

# ### Bước 1

# ```
# i = 0
# nums[0][0] = '0'
# → đảo → '1'
# ans = ['1']
# ```

# ### Bước 2

# ```
# i = 1
# nums[1][1] = '1'
# → đảo → '0'
# ans = ['1','0']
# ```

### Bước 3

# ```
# i = 2
# nums[2][2] = '1'
# → đảo → '0'
# ans = ['1','0','0']
# ```

# ### Kết quả

# ```
# "100"
# ```

# Chuỗi này chắc chắn:

# ```
# 100 ≠ 010
# 100 ≠ 111
# 100 ≠ 001


# ## Độ phức tạp

# * **Time complexity:** `O(n)`
# * **Space complexity:** `O(n)`

# Rất tối ưu vì chỉ cần **1 vòng lặp**.

# ---

# Nếu bạn muốn, mình có thể giải thích thêm **vì sao diagonal trick đảm bảo 100% không trùng (chứng minh toán học)** — cái này thường hay được hỏi khi phỏng vấn thuật toán.


# ## 1. Đề bài

# Bạn được cho một **mảng `nums` gồm `n` chuỗi nhị phân**.

# * Mỗi chuỗi có **độ dài = n**
# * Mỗi chuỗi chỉ chứa **`0` và `1`**
# * Tất cả chuỗi trong `nums` **khác nhau**

# Yêu cầu:
# **Tìm một chuỗi nhị phân độ dài `n` mà KHÔNG xuất hiện trong `nums`.**

# Bạn có thể trả về **bất kỳ chuỗi hợp lệ nào**.

# ---

# ## 2. Ví dụ

# ### Ví dụ 1

# ```
# Input: nums = ["01","10"]
# Output: "00"
# ```

# Giải thích:

# * n = 2 → chuỗi nhị phân dài 2
# * Tất cả chuỗi có thể có:

# ```
# 00
# 01
# 10
# 11
# ```

# Trong `nums` đã có:

# ```
# 01
# 10
# ```

# Chuỗi chưa xuất hiện:

# ```
# 00 hoặc 11
# ```

# → Trả về cái nào cũng đúng.

# ---

# ### Ví dụ 2

# ```
# Input: nums = ["00","01"]
# Output: "11"
# ```

# Các chuỗi có thể:

# ```
# 00
# 01
# 10
# 11
# ```

# Trong `nums` có:

# ```
# 00
# 01
# ```

# Còn lại:

# ```
# 10 hoặc 11
# ```

# ---

# ## 3. Ý chính của bài

# Nếu:

# ```
# n = 3
# ```

# Thì tổng số chuỗi nhị phân có thể tạo ra:

# ```
# 2^3 = 8
# ```

# Ví dụ:

# ```
# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111
# ```

# Nhưng đề bài chỉ cho:

# ```
# n = 3 chuỗi
# ```

# Tức là chỉ có **3 chuỗi trong 8 chuỗi có thể**.

# → **Chắc chắn luôn tồn tại ít nhất 1 chuỗi chưa xuất hiện**.

# ---

# ## 4. Tóm tắt đề bài (ngắn gọn)

# Cho:

# ```
# n chuỗi nhị phân
# mỗi chuỗi dài n
# ```

# Hãy tìm:

# ```
# 1 chuỗi nhị phân dài n
# không nằm trong nums
# ```

# ---

# ## 5. Ý tưởng nổi tiếng của bài (rất hay)

# Có một trick gọi là **Cantor Diagonal Trick**.

# Ví dụ:

# ```
# nums = ["010",
#         "111",
#         "001"]
# ```

# Ta tạo chuỗi mới bằng cách:

# * lấy **ký tự thứ i của chuỗi i**
# * **đảo bit** (0 → 1, 1 → 0)

# ```
# nums[0][0] = 0 → 1
# nums[1][1] = 1 → 0
# nums[2][2] = 1 → 0
# ```

# Chuỗi mới:

# ```
# 100
# ```

# Chuỗi này **chắc chắn khác tất cả chuỗi trong nums**.

# ---

# Nếu bạn muốn, mình có thể giải thích tiếp:

# * **Vì sao diagonal trick luôn đúng**
# * **Code Java / Python cực ngắn**
# * **Cách tư duy để gặp bài này là nghĩ ra ngay** (cái này rất quan trọng khi phỏng vấn).
