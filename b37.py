# 2197. Replace Non-Coprime Numbers in Array(16/09/2025)
# Ok mình giải thích bài **LeetCode 2197. Replace Non-Coprime Numbers in Array** cho bạn nhé 👇
from typing import List
from math import gcd, lcm

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        """Thuật toán hợp nhất số không nguyên tố cùng nhau bằng LCM."""
        ans = []            # stack lưu kết quả tạm
        curr = nums[0]      # phần tử đang xử lý

        # duyệt qua các phần tử từ index 1 trở đi
        for x in nums[1:]:
            if gcd(curr, x) > 1:           # nếu curr và x không nguyên tố cùng nhau
                curr = lcm(curr, x)        # gộp thành LCM

                # sau khi gộp, kiểm tra xem curr có gộp tiếp được với phần tử cuối stack không
                while ans and gcd(curr, ans[-1]) > 1:
                    curr = lcm(curr, ans.pop())  # pop ra, gộp tiếp
            else:
                # nếu curr và x nguyên tố cùng nhau → đẩy curr vào stack
                ans.append(curr)
                curr = x   # cập nhật curr = x để xử lý tiếp

        # push phần tử cuối cùng vào stack
        ans.append(curr)

        return ans
# Ok 👍 mình giải thích chi tiết thuật toán trong đoạn code này nhé.

# ---

# ## Mục tiêu đề bài

# Bạn có một mảng số nguyên `nums`. Bạn cần **thay thế dãy các số liên tiếp không nguyên tố cùng nhau (non-coprime)** bằng **BCNN (LCM)** của chúng, lặp lại cho đến khi không còn cặp nào như vậy.

# Ví dụ:

# ```
# nums = [6, 4, 3, 2, 7, 6, 2]
# ```

# * `6` và `4` không nguyên tố cùng nhau → gộp thành `LCM(6,4)=12`
# * Sau đó `12` và `3` cũng không nguyên tố cùng nhau → gộp thành `LCM(12,3)=12`
# * Tiếp tục so với `2`, gộp tiếp → `LCM(12,2)=12`
# * … cuối cùng ra `[12,7,6,2]`

# ---

# ## Ý tưởng thuật toán

# 1. Dùng **stack (`ans`)** để lưu kết quả tạm.
# 2. Dùng biến `curr` lưu số đang xét.
# 3. Với mỗi phần tử `x` trong `nums`:

#    * Nếu `gcd(curr, x) > 1` → chúng có ước chung → gộp lại thành `lcm(curr, x)`.
#    * Sau khi gộp, có thể phải **gộp tiếp** với phần tử cuối của stack (vì nó có thể không nguyên tố cùng nhau với `curr`).
#    * Nếu `gcd(curr, x) == 1` → không gộp được, push `curr` vào stack, rồi chuyển `curr = x`.
# 4. Sau vòng lặp, push `curr` vào stack.
# 5. Trả về stack (`ans`).

# ---

# ## Minh họa với ví dụ

# ```
# nums = [6,4,3,2,7,6,2]
# ```

# * `curr = 6`, stack = \[]
# * Xét `x = 4`: gcd(6,4)=2>1 → curr=LCM(6,4)=12
#   stack = \[]
# * Xét `x = 3`: gcd(12,3)=3>1 → curr=LCM(12,3)=12
#   stack = \[]
# * Xét `x = 2`: gcd(12,2)=2>1 → curr=LCM(12,2)=12
#   stack = \[]
# * Xét `x = 7`: gcd(12,7)=1 → push curr=12 → stack=\[12], curr=7
# * Xét `x = 6`: gcd(7,6)=1 → push curr=7 → stack=\[12,7], curr=6
# * Xét `x = 2`: gcd(6,2)=2>1 → curr=LCM(6,2)=6
#   stack=\[12,7]

# Kết thúc → push curr=6 → stack=\[12,7,6]
# Trả về `[12,7,6]`. ✅

# ---

# ## Key Point

# * **LCM để gộp**, **stack để nhớ lại các số đã chắc chắn xong**, **while loop để gộp tiếp nếu cần**.

# ---

# 👉 Bạn có muốn mình vẽ **sơ đồ stack từng bước chạy** để trực quan hơn không?

# # ---

# # ## 📌 Đề bài (tóm gọn)

# # Cho một mảng số nguyên **nums**.

# # * Ta sẽ duyệt từ **trái sang phải**.
# # * Nếu bắt gặp **2 phần tử liên tiếp không nguyên tố cùng nhau (non-coprime)**, tức là `gcd(a, b) > 1`, thì ta thay chúng bằng **LCM(a, b)** (bội chung nhỏ nhất).
# # * Sau khi thay, ta tiếp tục kiểm tra lại với phần tử mới và phần tử liền trước nó (vì khi hợp nhất xong, phần tử mới có thể lại không nguyên tố cùng nhau với phần tử trước đó).
# # * Tiếp tục quá trình cho đến khi không còn cặp nào liền kề mà gcd > 1.

# # 👉 Yêu cầu: Trả về **mảng cuối cùng**.

# # ---

# # ## 📌 Ví dụ minh họa

# # ### Ví dụ 1

# # ```
# # nums = [6, 4, 3, 2, 7, 6, 2]
# # ```

# # * Bước 1: `6` và `4` → gcd(6,4)=2 > 1 → thay bằng lcm(6,4)=12
# #   Mảng: \[12, 3, 2, 7, 6, 2]

# # * Bước 2: `12` và `3` → gcd=3 > 1 → thay bằng lcm(12,3)=12
# #   Mảng: \[12, 2, 7, 6, 2]

# # * Bước 3: `12` và `2` → gcd=2 > 1 → thay bằng lcm(12,2)=12
# #   Mảng: \[12, 7, 6, 2]

# # * Bước 4: `12` và `7` → gcd=1 (ok, giữ nguyên).

# # * `7` và `6` → gcd=1 (ok).

# # * `6` và `2` → gcd=2 > 1 → thay bằng lcm(6,2)=6
# #   Mảng: \[12, 7, 6]

# # ✅ Kết quả cuối: `[12, 7, 6]`.

# # ---

# # ### Ví dụ 2

# # ```
# # nums = [2,2,1,1,3,3,3]
# # ```

# # * `2` và `2` → gcd=2 → thay bằng lcm=2 → \[2,1,1,3,3,3]
# # * `2` và `1` → gcd=1 → giữ nguyên.
# # * `1` và `1` → gcd=1 → giữ nguyên.
# # * `1` và `3` → gcd=1 → giữ nguyên.
# # * `3` và `3` → gcd=3 → thay bằng 3 → \[2,1,1,3,3]
# # * `3` và `3` → lại hợp → \[2,1,1,3]

# # ✅ Kết quả cuối: `[2, 1, 1, 3]`.

# # ---

# # ## 📌 Ý tưởng thuật toán

# # * Dùng **stack** để lưu kết quả tạm thời.
# # * Với mỗi số trong `nums`:

# #   1. Push vào stack.
# #   2. Trong khi **stack có ≥ 2 phần tử** và gcd(top2) > 1 → pop 2 số, thay bằng lcm, rồi push lại.
# # * Kết quả cuối cùng chính là stack.

# # ⏱️ Độ phức tạp:

# # * Mỗi phần tử chỉ push + pop vài lần → O(n log A), với A là giá trị tối đa trong nums (do gcd/lcm).

# # ---

# # 👉 Bạn có muốn mình viết code **Java** kèm comment chi tiết cho bài này không?
# # Ok 👍 mình giải thích kỹ hơn vì sao lại ra **kết quả cuối** như vậy nhé.
# # Lấy lại **ví dụ đầu tiên**:

# # ```
# # nums = [6, 4, 3, 2, 7, 6, 2]
# # ```

# # ---

# # ### 🔎 Bắt đầu duyệt:

# # **Bước 1:**

# # * Cặp đầu: `(6, 4)`
# # * gcd(6,4)=2 > 1 → thay = lcm(6,4)=12
# # * Mảng mới: `[12, 3, 2, 7, 6, 2]`

# # ---

# # **Bước 2:**

# # * Xem `(12, 3)`
# # * gcd(12,3)=3 > 1 → thay = lcm(12,3)=12
# # * Mảng mới: `[12, 2, 7, 6, 2]`

# # ---

# # **Bước 3:**

# # * Xem `(12, 2)`
# # * gcd(12,2)=2 > 1 → thay = lcm(12,2)=12
# # * Mảng mới: `[12, 7, 6, 2]`

# # ---

# # **Bước 4:**

# # * Xem `(12, 7)`
# # * gcd(12,7)=1 → **không gộp**.

# # ---

# # **Bước 5:**

# # * Xem `(7, 6)`
# # * gcd(7,6)=1 → **không gộp**.

# # ---

# # **Bước 6:**

# # * Xem `(6, 2)`
# # * gcd(6,2)=2 > 1 → thay = lcm(6,2)=6
# # * Mảng mới: `[12, 7, 6]`

# # ---

# # ✅ Không còn cặp nào `gcd > 1` nữa → **kết quả cuối cùng** là:

# # ```
# # [12, 7, 6]
# # ```

# # ---

# # 👉 Điểm quan trọng:

# # * Sau khi gộp một cặp thành **LCM**, phần tử mới đó **có thể lại gộp tiếp với phần tử trước đó**.
# # * Ta phải kiểm tra liên tục cho đến khi không còn gộp được.

# # ---

# # Bạn có muốn mình minh họa lại toàn bộ quá trình này bằng **stack (ngăn xếp)** thay vì thay trực tiếp trong mảng (sẽ dễ hình dung hơn) không?
# # À 👍 mình giải thích đơn giản nhé:

# # ### 📌 LCM là gì?

# # * **LCM (Least Common Multiple)** = **Bội chung nhỏ nhất** của hai số.
# # * Nghĩa là số **nhỏ nhất > 0** mà **cả hai số đều chia hết**.

# # ---

# # ### 📌 Ví dụ:

# # * LCM(4, 6) = 12
# #   (vì bội của 4 = 4, 8, 12, 16, ...;
# #   bội của 6 = 6, 12, 18, ...;
# #   → bội chung nhỏ nhất là 12).

# # * LCM(3, 5) = 15

# # * LCM(2, 8) = 8

# # ---

# # ### 📌 Công thức tính nhanh:

# # $$
# # \text{LCM}(a, b) = \frac{a \times b}{\text{GCD}(a, b)}
# # $$

# # Trong đó:

# # * **GCD** = Ước số chung lớn nhất (Greatest Common Divisor).
# # * Ví dụ:

# #   * gcd(6, 4) = 2
# #   * lcm(6, 4) = (6×4)/2 = 12

# # ---

# # 👉 Trong bài **2197. Replace Non-Coprime Numbers in Array**, ta dùng **LCM** để thay thế 2 số liên tiếp không nguyên tố cùng nhau.

# # Bạn có muốn mình viết 1 đoạn **Java code tính GCD và LCM** đơn giản để bạn test thử không?
