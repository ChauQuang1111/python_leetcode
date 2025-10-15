# 3350. Adjacent Increasing Subarrays Detection II(15/10/2025)
# Ok 👇 mình sẽ giải thích **rõ và dễ hiểu** đề **LeetCode 3350 – Adjacent Increasing Subarrays Detection II** cho bạn nhé.
from typing import List
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        # Bài toán: tìm độ dài lớn nhất k sao cho tồn tại 2 đoạn con tăng dần liền nhau
        # mỗi đoạn có độ dài >= k.

        n = len(nums)          # Độ dài mảng
        pre_cnt = 0            # Độ dài đoạn tăng trước đó
        cur_cnt = 0            # Độ dài đoạn tăng hiện tại
        i = 0                  # Con trỏ duyệt mảng
        ans = 1                # Biến lưu kết quả lớn nhất tìm được

        # Duyệt đến phần tử kế cuối (vì sẽ so sánh nums[i] và nums[i+1])
        while i < n - 1:
            
            # Nếu mảng bị ngắt (không tăng), reset lại pre_cnt và nhảy sang phần tử tiếp theo
            if nums[i] >= nums[i + 1]:
                i += 1
                pre_cnt = 1    # Đặt lại độ dài đoạn tăng trước đó = 1 (bắt đầu lại)
                continue        # Tiếp tục vòng lặp (bỏ qua phần còn lại)
            
            # Nếu nums[i] < nums[i+1], tức là bắt đầu một đoạn tăng dần mới
            start = i          # Ghi lại vị trí bắt đầu của đoạn tăng
            i += 1
            # Tiếp tục di chuyển cho đến khi đoạn tăng bị ngắt
            while i < n and nums[i] > nums[i - 1]:
                i += 1
            
            # Độ dài của đoạn tăng hiện tại = (vị trí hiện tại - vị trí bắt đầu)
            cur_cnt = i - start

            # Cập nhật kết quả:
            #  - min(pre_cnt, cur_cnt): 2 đoạn tăng liền nhau, lấy đoạn ngắn hơn làm giới hạn k
            #  - cur_cnt // 2: nếu chỉ có 1 đoạn tăng dài, có thể chia đôi nó thành 2 đoạn liền nhau
            #  - ans: giá trị k lớn nhất từng tìm được
            ans = max(ans, min(pre_cnt, cur_cnt), cur_cnt // 2)
            
            # Cập nhật pre_cnt = cur_cnt cho vòng sau (đoạn hiện tại sẽ là đoạn trước)
            pre_cnt = cur_cnt

        # Trả về kết quả cuối cùng
        return ans

# ---

# ## 🧩 Đề bài (Tóm tắt)

# Cho một **mảng số nguyên `nums`** và một số nguyên `k`.
# Ta cần **kiểm tra xem có tồn tại hai dãy con tăng dần liên tiếp, mỗi dãy có độ dài ít nhất `k` hay không.**

# Hai dãy con này phải:

# 1. Là **tăng dần nghiêm ngặt** (strictly increasing),
# 2. **Liền kề nhau** trong mảng (adjacent),
# 3. Mỗi dãy đều có **độ dài ≥ k**.

# Nếu có, trả về `true`, ngược lại `false`.

# ---

# ## 📘 Giải thích bằng ví dụ

# ### Ví dụ 1:

# ```
# Input: nums = [1,2,3,4,5,6], k = 2
# ```

# Ta chia mảng thành:

# * [1,2,3,4] là tăng dần
# * [5,6] cũng tăng dần

# Nếu chọn [1,2,3,4] là subarray 1 (dài ≥ 2)
# và [5,6] là subarray 2 (dài ≥ 2)
# → Hai dãy này liền nhau và đều tăng dần.

# ✅ Output: `true`

# ---

# ### Ví dụ 2:

# ```
# Input: nums = [1,2,1,2,3,1], k = 2
# ```

# Các đoạn tăng dần:

# * [1,2]
# * [1,2,3]
# * [1]

# Giữa [1,2] và [1,2,3], ta thấy không liền kề (vì có số 1 xen giữa).
# Không có hai đoạn tăng dài ≥ 2 nào **liền nhau**.

# ❌ Output: `false`

# ---

# ## ⚙️ Ý tưởng thuật toán

# Ta cần tìm đoạn tăng dần liên tục, sau đó kiểm tra xem có chỗ nào mà:

# * Độ dài của đoạn tăng dần **trước ≥ k**
# * Độ dài của đoạn tăng dần **sau ≥ k**
# * Và hai đoạn đó **nối liền nhau**

# ---

# ## 🔍 Cách tiếp cận

# 1. Duyệt từ trái sang phải, tìm độ dài các đoạn tăng dần liên tục.
#    Ví dụ:

#    ```
#    nums = [1,2,3,1,2,3,4]
#    => lengths = [3, 4]  // độ dài các đoạn tăng liên tục
#    ```

# 2. Khi một đoạn kết thúc, nếu:

#    * Đoạn trước có độ dài ≥ k,
#    * Đoạn hiện tại (sau) có độ dài ≥ k,
#    * Và chúng liền nhau,
#      → return `true`.

# 3. Nếu duyệt hết không thỏa, return `false`.

# ---

# ## 🧠 Tối ưu hóa (O(n))

# Ta có thể chỉ cần một biến `prev` (độ dài đoạn tăng trước đó) và `curr` (độ dài đoạn hiện tại).

# Thuật toán:

# ```java
# class Solution {
#     public boolean hasIncreasingSubarrays(List<Integer> nums, int k) {
#         int n = nums.size();
#         int prev = 1, curr = 1;

#         for (int i = 1; i < n; i++) {
#             if (nums.get(i) > nums.get(i - 1)) curr++;
#             else {
#                 if (prev >= k && curr >= k) return true;
#                 prev = curr;
#                 curr = 1;
#             }
#         }
#         // kiểm tra lần cuối vì có thể kết thúc bằng đoạn tăng
#         return prev >= k && curr >= k;
#     }
# }
# ```

# ---

# ## 💡 Tóm tắt ý chính

# | Điều kiện                | Ý nghĩa                                      |
# | ------------------------ | -------------------------------------------- |
# | `nums[i] > nums[i-1]`    | Tiếp tục tăng                                |
# | `else`                   | Đoạn tăng kết thúc                           |
# | `prev >= k && curr >= k` | Hai đoạn liền nhau đủ dài                    |
# | Duyệt hết                | Nếu không có đoạn nào đủ điều kiện → `false` |

# ---

# Bạn có muốn mình **vẽ sơ đồ minh họa bằng mảng và hai đoạn tăng liền nhau (ví dụ nums = [1,2,3,1,2,3,4], k=2)** để dễ hình dung hơn không?
# Rất hay 👏 Bạn đang xem xét một **thuật toán tối ưu O(n)** để giải bài **LeetCode 3350 – Adjacent Increasing Subarrays Detection II**, với ý tưởng rất gọn và clever.
# Mình sẽ **giải thích thuật toán + chú thích từng dòng code** để bạn hiểu rõ hoàn toàn nhé.

# ---

# ## 🎯 Mục tiêu của bài

# Tìm **độ dài lớn nhất `k`** sao cho tồn tại **hai dãy con tăng dần liền nhau**, mỗi dãy có **độ dài ≥ k**.

# ---

# ## 💡 Ý tưởng thuật toán của bạn

# Thuật toán này không cần mảng `left[]` và `right[]` như cách cơ bản, mà chỉ dùng **hai biến đếm động**:

# * `pre_cnt`: độ dài của đoạn tăng **trước đó**
# * `cur_cnt`: độ dài của đoạn tăng **hiện tại**
# * Duyệt mảng một lần duy nhất.

# Mỗi khi gặp đoạn tăng mới → tính độ dài → cập nhật đáp án.

# ---

# ## 🔍 Giải thích chi tiết từng bước

# ```python
# class Solution:
#     def maxIncreasingSubarrays(self, nums: List[int]) -> int:
#         # 1️⃣ pre_cnt: độ dài của đoạn tăng trước đó
#         # 2️⃣ cur_cnt: độ dài của đoạn tăng hiện tại
#         # 3️⃣ ans: giá trị k lớn nhất tìm được
        
#         n = len(nums)
#         pre_cnt = 0
#         cur_cnt = 0
#         i = 0
#         ans = 1
# ```

# ---

# ### 🚶‍♂️ Duyệt qua mảng

# ```python
#         while i < n - 1:
# ```

# → Dừng ở `n - 1` vì sẽ so sánh `nums[i]` và `nums[i+1]`.

# ---

# ### 🧱 Nếu mảng không tăng (bị ngắt)

# ```python
#             if nums[i] >= nums[i + 1]:
#                 i += 1
#                 pre_cnt = 1
#                 continue
# ```

# * Khi gặp `nums[i] >= nums[i+1]`, đoạn tăng bị **ngắt**.
# * Gán `pre_cnt = 1` (tức là chỉ có 1 phần tử ở sau, reset lại).
# * Tiếp tục duyệt.

# ---

# ### 📈 Khi bắt đầu một đoạn tăng mới

# ```python
#             start = i
#             i += 1
#             while i < n and nums[i] > nums[i - 1]:
#                 i += 1
# ```

# → Vòng lặp này tìm **đoạn tăng dần liên tục** bắt đầu tại `start`.

# Ví dụ:

# ```
# nums = [1,2,3,1,2,3,4]
# ```

# Khi `i=0`, vòng while này sẽ tăng `i` đến 3 (khi gặp 1 giảm).

# Khi đó:

# ```
# cur_cnt = i - start = 3 - 0 = 3
# ```

# ---

# ### 🧮 Cập nhật kết quả

# ```python
#             cur_cnt = i - start
#             ans = max(ans, min(pre_cnt, cur_cnt), cur_cnt // 2)
#             pre_cnt = cur_cnt
# ```

# **Giải thích 2 công thức:**

# 1️⃣ `min(pre_cnt, cur_cnt)`
# → đại diện cho **hai đoạn tăng liền nhau**, ví dụ:

# ```
# [1,2,3] [4,5,6,7]
# pre_cnt = 3, cur_cnt = 4  → min = 3
# ```

# → có thể tạo được `k=3`.

# 2️⃣ `cur_cnt // 2`
# → khi đoạn tăng quá dài (chưa có đoạn trước), ta có thể **tự chia đôi** thành 2 đoạn liền nhau.
# Ví dụ:

# ```
# [1,2,3,4,5,6] → cur_cnt=6 → cur_cnt//2=3
# ```

# 👉 Lấy `max` trong 3 giá trị để đảm bảo kết quả tốt nhất.

# ---

# ### 🏁 Trả về kết quả cuối cùng

# ```python
#         return ans
# ```

# ---

# ## 📘 Ví dụ minh họa chi tiết

# ```
# nums = [1,2,3,1,2,3,4]
# ```

# | i             | nums[i] | pre_cnt | cur_cnt | ans (max) | Ghi chú        |
# | ------------- | ------- | ------- | ------- | --------- | -------------- |
# | 0             | 1       | 0       | 3       | 1 → 3     | đoạn [1,2,3]   |
# | 3             | 1       | 3       | 4       | 3         | đoạn [1,2,3,4] |
# | ✅ Kết quả = 3 |         |         |         |           |                |

# ---

# ## 🧠 Độ phức tạp

# * **Thời gian:** O(n)
# * **Không gian:** O(1)

# ---

# ## ✅ Tóm tắt ý tưởng

# | Biến                    | Ý nghĩa                                    |
# | ----------------------- | ------------------------------------------ |
# | `pre_cnt`               | độ dài đoạn tăng trước đó                  |
# | `cur_cnt`               | độ dài đoạn tăng hiện tại                  |
# | `cur_cnt // 2`          | khi chỉ có một đoạn tăng rất dài, chia đôi |
# | `min(pre_cnt, cur_cnt)` | khi có hai đoạn liền nhau                  |
# | `ans = max(...)`        | cập nhật đáp án lớn nhất                   |

# ---

# 👉 Cực kỳ thông minh — vì cách này bỏ qua mảng phụ `left[]`, `right[]` và chỉ cần O(1) bộ nhớ.
# Nếu bạn muốn, mình có thể **viết lại đoạn này bằng Java** (theo style bạn hay dùng: `Scanner`, không `try-catch`, dùng `while`) để đối chiếu dễ hiểu hơn. Bạn muốn không?
