# 3542. Minimum Operations to Convert All Elements to Zero(10/11/2025)
# Đề bài **3542. Minimum Operations to Convert All Elements to Zero** (LeetCode) mô tả như sau:

# > Cho một mảng `nums` gồm các số nguyên không âm.
# > Trong một **phép toán**, bạn được chọn một **đoạn con (subarray)** `[i, j]` với `0 ≤ i ≤ j < n` và **đặt tất cả các phần tử bằng giá trị nhỏ nhất không âm trong đoạn đó** về **0**. ([LeetCode][1])
# > Yêu cầu: **Trả về số phép toán tối thiểu** cần thiết để biến tất cả phần tử của mảng thành **0**.

# ---

# ### 🎯 Vắn tắt lại:

# * Bạn có mảng `nums` kiểu như `[3,1,2,1]`.
# * Mỗi lần bạn chọn một đoạn con, tìm trong đoạn đó giá trị **nhỏ nhất** (không âm), sau đó đặt **mọi phần tử có giá trị bằng giá trị nhỏ nhất đó** (có thể nhiều phần tử) trong đoạn thành 0.
# * Lặp lại cho đến khi toàn bộ mảng thành `[0,0,…,0]`.
# * Tìm số lần chọn đoạn con ít nhất có thể.

# ---

# ### 🧠 Ví dụ minh họa:

# Ví dụ: `nums = [3,1,2,1]`

# * Lần 1: chọn đoạn `[1,3]` (chỉ số từ 1 đến 3) chứa `[1,2,1]`. Giá trị nhỏ nhất là `1`. Đặt tất cả các phần tử bằng `1` trong đoạn đó thành `0` → mảng trở thành `[3,0,2,0]`.
# * Lần 2: chọn đoạn `[2,2]` chứa `[2]`. Giá trị nhỏ nhất = 2. Đặt phần tử bằng 2 thành 0 → `[3,0,0,0]`.
# * Lần 3: chọn đoạn `[0,0]` chứa `[3]`. Giá trị nhỏ nhất = 3. Đặt thành 0 → `[0,0,0,0]`.
#   Số phép toán = 3. ([Medium][2])

# ---

# ### 🔍 Nhận xét & hướng giải:

# * Nếu bạn nhìn kỹ, mỗi lần bạn “xử lý” một giá trị **v > 0**, bạn thực chất chọn các vùng mà trong đó giá trị đó là **giá trị nhỏ nhất trong vùng đó và chưa bị xử lý thành 0**.
# * Các vùng có cùng giá trị và liên tục (liên tiếp) có thể được xử lý trong cùng một phép toán nếu không bị “chặn” bởi phần tử nhỏ hơn đã bị xử lý trước đó.
# * Một hướng giải hiệu quả là sử dụng **stack đơn định (monotonic stack)**: duyệt từ trái sang phải, giữ các giá trị đang tăng lên, mỗi khi thấy giá trị giảm xuống — “thoát” khỏi stack và cần thực hiện một phép toán mới. ([WalkCCC][3])
# * Cụ thể: mỗi khi bạn gặp một giá trị `num` lớn hơn giá trị đỉnh stack, bạn cần **một phép toán mới**. Nếu giá trị nhỏ hơn hoặc bằng – pop cho tới khi stack phù hợp.

# ---

# ### ✅ Kết luận:

# Bài toán yêu cầu đếm số “khối giá trị tăng lên” (về mặt xử lý theo giá trị nhỏ nhất) mà bạn cần thực hiện để tất cả thành phần về 0.
# Chiến lược hiệu quả: dùng stack hoặc đếm nhóm liên tục cho mỗi giá trị > 0.

# Nếu bạn muốn, mình có thể **viết thuật toán chi tiết bằng Java hoặc Python**, kèm chú thích từng dòng, giúp bạn dễ hiểu và thực hành. Bạn có muốn mình làm vậy không?

# Rất hay — đây là một **thuật toán cực kỳ thông minh** và **ngắn gọn** để giải bài LeetCode **3542. Minimum Operations to Convert All Elements to Zero** 💡

# Hãy cùng giải thích chi tiết **từng dòng code** và **ý tưởng đằng sau thuật toán** nhé 👇

# ---

# ## 🧩 Mục tiêu

# Ta cần **đếm số phép toán tối thiểu** để biến toàn bộ mảng `nums` thành `0`.

# ---

# ## 🧠 Ý tưởng chính của thuật toán (tư duy “stack tăng dần”)

# * Mỗi phần tử `nums[i]` biểu diễn **độ cao hiện tại** (ví dụ như cột cao bao nhiêu).
# * Mỗi khi chiều cao **giảm xuống**, nghĩa là ta đã hoàn thành việc “xoá” một đoạn con — cần **1 phép toán**.
# * Stack lưu **các mức độ cao đang mở (chưa hoàn tất)**, theo **thứ tự tăng dần**.
# * Khi gặp số nhỏ hơn đỉnh stack, ta phải “đóng” các đoạn cao hơn → mỗi lần giảm `top` là **thêm một phép toán**.

# ---

# ## 🔍 Code chi tiết có chú thích

# ```python
class Solution:
    def minOperations(self, nums):
        # Stack dùng để lưu "các mức độ cao hiện tại"
        # thêm 1 phần tử 0 ở đầu để tránh stack trống
        stack = [0] * (len(nums) + 1)
        top = 0   # con trỏ đỉnh stack
        ans = 0   # kết quả - tổng số phép toán

        # Duyệt qua từng phần tử trong mảng
        for num in nums:
            # Khi chiều cao hiện tại nhỏ hơn chiều cao ở đỉnh stack,
            # nghĩa là vùng này đã kết thúc (chúng ta "xoá" được một đoạn)
            while stack[top] > num:
                top -= 1  # bỏ bớt mức cao nhất đi
                ans += 1  # mỗi lần bỏ là 1 phép toán

            # Nếu giá trị hiện tại khác giá trị đỉnh stack,
            # nghĩa là bắt đầu một vùng mới với độ cao khác
            if stack[top] != num:
                top += 1
                stack[top] = num  # đẩy độ cao mới vào stack

        # Sau khi duyệt xong, còn 'top' mức chưa đóng → cộng thêm vào kết quả
        return ans + top
# ```

# ---

# ## 📊 Ví dụ minh hoạ

# ### Input:

# ```python
# nums = [1, 2, 2, 3, 2]
# ```

# ### Quá trình:

# | i | num | Stack (trên cùng bên phải) | Hành động  | ans | top |
# | - | --- | -------------------------- | ---------- | --- | --- |
# | 0 | 1   | [0] → [0,1]                | push 1     | 0   | 1   |
# | 1 | 2   | [0,1] → [0,1,2]            | push 2     | 0   | 2   |
# | 2 | 2   | [0,1,2]                    | không đổi  | 0   | 2   |
# | 3 | 3   | [0,1,2] → [0,1,2,3]        | push 3     | 0   | 3   |
# | 4 | 2   | 3 > 2 → pop 3              | xoá 1 vùng | 1   | 2   |

# Kết thúc mảng:
# → Còn 2 mức chưa đóng (`[0,1,2]`)
# ✅ `ans + top = 1 + 2 = 3`

# **Output = 3**

# ---

# ## 💬 Tóm tắt logic

# * Mỗi lần **stack giảm độ cao** ⇒ hoàn thành 1 phép xoá.
# * Mỗi lần **xuất hiện độ cao mới (khác với đỉnh)** ⇒ mở 1 vùng mới.
# * Sau cùng cộng `top` để đếm các vùng chưa khép lại.

# ---

# ## 🧮 Độ phức tạp

# * ⏱ **Thời gian:** O(n) — mỗi phần tử chỉ push/pop 1 lần.
# * 💾 **Không gian:** O(n) — dùng stack.

# ---

# Bạn có muốn mình minh hoạ bằng **hình trực quan (dạng cột, stack)** để dễ hình dung các “vùng cao thấp” trong quá trình chạy không?
