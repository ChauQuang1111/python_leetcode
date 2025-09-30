# 2221. Find Triangular Sum of an Array(30/09/2025)
from typing import List
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums) - 1   # Bậc của tam giác (vì sau n lần thì còn 1 số)
        ans, A = nums[0], 1 # ans: kết quả cuối cùng, ban đầu = nums[0]*C(n,0)
                            # A: hệ số tổ hợp C(n, k), khởi tạo C(n,0) = 1

        for k in range(1, n+1):  
            # Cập nhật hệ số tổ hợp C(n,k) từ C(n,k-1) bằng công thức:
            # C(n,k) = C(n,k-1) * (n-k+1) / k
            A = A * (n - k + 1) // k

            # Cộng thêm nums[k] * C(n,k) vào kết quả
            # Vì đề yêu cầu %10, nên lấy ans mod 10 để không bị tràn số
            ans = (ans + nums[k] * A) % 10  

        return ans

# Ok 👍 mình giải thích đề **LeetCode 2221 – Find Triangular Sum of an Array** cho bạn:

# ---

# ### 📝 Đề bài:

# Bạn được cho một mảng `nums` gồm **n số nguyên (0–9)**.
# Ta thực hiện quá trình **giảm dần mảng** cho đến khi còn **1 phần tử duy nhất**:

# 1. Ở mỗi bước, tạo ra một mảng mới ngắn hơn 1 phần tử.
# 2. Phần tử mới ở vị trí `i` được tính bằng:

# [
# new[i] = (nums[i] + nums[i+1]) \mod 10
# ]

# 3. Thay `nums` bằng mảng mới vừa tạo.
# 4. Tiếp tục cho đến khi chỉ còn 1 phần tử → đó là **triangular sum**.

# ---

# ### 🔍 Ví dụ:

# **Input:**

# ```
# nums = [1,2,3,4,5]
# ```

# 👉 Quá trình:

# * Bước 1: `[ (1+2)%10, (2+3)%10, (3+4)%10, (4+5)%10 ] = [3,5,7,9]`
# * Bước 2: `[ (3+5)%10, (5+7)%10, (7+9)%10 ] = [8,2,6]`
# * Bước 3: `[ (8+2)%10, (2+6)%10 ] = [0,8]`
# * Bước 4: `[ (0+8)%10 ] = [8]`

# ✅ Output = `8`

# ---

# ### 🎯 Yêu cầu:

# Trả về **phần tử cuối cùng** sau khi thực hiện hết quá trình.

# ---

# 👉 Đây thực chất giống như việc **xây dựng một tam giác số** từ trên xuống, giống Pascal Triangle nhưng lấy `% 10`.

# ---

# Bạn muốn mình giải thích cách **giải brute force (mô phỏng)** hay cách **tối ưu bằng tổ hợp (binomial coefficient)**?


### 📌 Đề bài (LeetCode 2221)

# * Bạn có một mảng `nums`.
# * Tạo một **tam giác số**:

#   * Ở mỗi hàng mới, phần tử thứ `i` được tính = `(nums[i] + nums[i+1]) % 10`.
#   * Làm đến khi còn đúng **1 số** → đó là đáp án.

# Ví dụ:

# ```
# nums = [1,2,3,4,5]

# [1,2,3,4,5]
#  [3,5,7,9]
#   [8,2,6]
#    [0,8]
#     [8]   ← kết quả
# ```

# ---

# ### 📌 Ý tưởng thuật toán

# Thay vì mô phỏng từng bước (O(n²)), ta có thể nhận ra:

# * Mỗi số ở dòng cuối cùng thực chất là **tổ hợp tuyến tính** của các số ban đầu `nums[k]`.
# * Cụ thể, kết quả cuối cùng chính là:
#   [
#   \text{Result} = \sum_{k=0}^{n} C(n, k) \cdot nums[k] ;;; \pmod{10}
#   ]

# Trong đó:

# * `n = len(nums) - 1` (số lần giảm mảng).
# * `C(n,k)` là hệ số **tổ hợp** (binomial coefficient).

# 👉 Đây chính là **Định lý nhị thức Newton**:
# [
# (x + y)^n = \sum_{k=0}^n C(n,k) \cdot x^{n-k} y^k
# ]
# Ở đây, ta coi việc cộng dồn các phần tử giống như đang khai triển nhị thức.

# ---

# ### 📌 Giải thích từng bước trong code

# ```python
# n = len(nums) - 1
# ```

# * Cần giảm mảng `n` lần để còn 1 số.

# ```python
# ans, A = nums[0], 1
# ```

# * `ans` = đóng góp của `nums[0] * C(n,0)` (ban đầu hệ số = 1).
# * `A` = giá trị hiện tại của `C(n,k)` (tổ hợp).

# ```python
# for k in range(1, n+1):
#     A = A * (n - k + 1) // k
# ```

# * Tính lần lượt các hệ số tổ hợp `C(n,k)` từ `C(n,k-1)`:
#   [
#   C(n,k) = C(n,k-1) \cdot \frac{n-k+1}{k}
#   ]

# ```python
#     ans = (ans + nums[k] * A) % 10
# ```

# * Cộng đóng góp của `nums[k]` với hệ số tổ hợp `C(n,k)`.
# * Lấy `% 10` vì chỉ cần chữ số cuối.

# ```python
# return ans
# ```

# * Trả về kết quả cuối cùng.

# ---

# ### 📌 Độ phức tạp

# * Thời gian: **O(n)** (chỉ duyệt 1 vòng).
# * Không gian: **O(1)** (chỉ dùng vài biến).
# * Nhanh hơn nhiều so với cách mô phỏng tam giác (**O(n²)**).

# ---

# 👉 Tóm lại:
# Thuật toán dùng **công thức tổ hợp** để tính trực tiếp kết quả cuối cùng của quá trình "tam giác hóa", tránh phải mô phỏng từng bước.

# ---

# Bạn có muốn mình vẽ thử một ví dụ nhỏ (vd: `nums = [2,5,3]`) theo cả **cách mô phỏng** và **cách tổ hợp** để thấy chúng ra kết quả giống nhau không?
