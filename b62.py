# Taking Maximum Energy From the Mystic Dungeon(10/10/2025)
# Rất hay 👍
# Dưới đây là **bản code đầy đủ** của bài **LeetCode 3147 - Taking Maximum Energy From the Mystic Dungeon**, kèm theo **chú thích chi tiết từng dòng** và **giải thích thuật toán** nhé 👇

# ---

# ### 🧠 **Ý tưởng thuật toán:**

# Bài toán yêu cầu ta tìm tổng năng lượng lớn nhất khi:

# * Bắt đầu ở một vị trí bất kỳ `i`.
# * Cứ mỗi lần chỉ được nhảy **cách k vị trí** (tức `i → i + k → i + 2k → ...`).
# * Cộng tất cả giá trị `energy[i]` trên đường đi.

# Ta có thể coi đây là một dạng **dynamic programming (DP)**, trong đó:

# > `dp[i]` = tổng năng lượng lớn nhất nếu bắt đầu tại vị trí `i`.

# Công thức quy hoạch động:

# ```
# dp[i] = energy[i] + dp[i + k] nếu i + k < n
# dp[i] = energy[i] nếu i + k >= n
# ```

# → Nghĩa là: nếu có thể nhảy tiếp (i + k còn trong mảng), thì cộng thêm năng lượng từ `i + k`.
# Ngược lại, nếu nhảy ra ngoài mảng thì dừng lại.

# ---

# ### ✅ **Code có chú thích chi tiết:**

from typing import List
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # dp[i] sẽ lưu tổng năng lượng tối đa khi bắt đầu từ phòng i
        dp = energy[:]  # sao chép mảng energy để không thay đổi mảng gốc

        # Duyệt ngược từ (n - k - 1) -> 0
        # Vì dp[i] phụ thuộc vào dp[i + k], nên ta cần tính dp[i + k] trước
        for i in range(len(energy) - k - 1, -1, -1):
            # Cộng thêm năng lượng nếu nhảy tiếp được sang i + k
            dp[i] += dp[i + k]

        # Kết quả là giá trị lớn nhất trong dp
        # Vì ta có thể bắt đầu ở bất kỳ vị trí nào
        return max(dp)


# ---

# ### 🔢 **Ví dụ minh họa:**

# ```
# energy = [5, 2, -10, -5, 1]
# k = 3
# ```

# Bắt đầu:

# ```
# dp = [5, 2, -10, -5, 1]
# ```

# Duyệt ngược:

# | i | dp[i] trước | dp[i + k] | dp[i] sau | dp mảng hiện tại   |
# | - | ----------- | --------- | --------- | ------------------ |
# | 1 | 2           | 1         | 3         | [5, 3, -10, -5, 1] |
# | 0 | 5           | -5        | 0         | [0, 3, -10, -5, 1] |

# Cuối cùng:

# ```
# max(dp) = 3
# ```

# ✅ **Output:**

# ```python
# 3
# ```

# ---

# ### ⚙️ **Độ phức tạp:**

# * **Thời gian:** `O(n)` — chỉ duyệt qua mảng 1 lần.
# * **Bộ nhớ:** `O(n)` (hoặc `O(1)` nếu dùng chính mảng `energy` thay vì `dp`).

# ---

# ### 💡 **Ghi chú mở rộng:**

# Nếu muốn tối ưu bộ nhớ, ta có thể viết ngắn gọn hơn:

# ```python
# class Solution:
#     def maximumEnergy(self, energy: List[int], k: int) -> int:
#         for i in range(len(energy) - k - 1, -1, -1):
#             energy[i] += energy[i + k]
#         return max(energy)
# ```

# → Kết quả y hệt, vì ta chỉ cần giữ tổng năng lượng tại mỗi vị trí.

# ---

# Bạn có muốn mình minh họa **cách thuật toán này hoạt động bằng sơ đồ dòng chảy (flow diagram)** không?

# ---

# ### 🧩 **Đề bài:**

# Bạn được cho:

# * Một **mảng `energy`** gồm `n` phần tử, trong đó `energy[i]` biểu thị **năng lượng** bạn có thể nhận được khi đứng ở **phòng i** (room i).
# * Một số nguyên `k`.

# Bạn có thể **bắt đầu ở bất kỳ phòng nào từ 0 đến n-1**, và sau đó **di chuyển đến các phòng có chỉ số tăng thêm `k` mỗi lần** — tức là từ `i` bạn có thể đi đến `i + k`, `i + 2k`, … **chừng nào còn trong phạm vi mảng**.

# Mục tiêu là:
# 👉 **Chọn điểm bắt đầu** sao cho tổng năng lượng thu được là **lớn nhất có thể**.

# ---

# ### 📘 **Cụ thể:**

# * Khi bạn đứng ở vị trí `i`, bạn nhận `energy[i]`.
# * Sau đó bạn có thể tiếp tục đến `i + k`, `i + 2k`, …
# * Tổng năng lượng là **tổng tất cả giá trị** `energy[i]` bạn đi qua.

# ---

# ### 🔢 **Ví dụ:**

# #### Input:

# ```python
# energy = [5, 2, -10, -5, 1]
# k = 3
# ```

# #### Giải thích:

# Bạn có thể chọn **bắt đầu ở bất kỳ vị trí nào:**

# | Bắt đầu | Các phòng bạn đi qua | Tổng năng lượng |
# | ------- | -------------------- | --------------- |
# | 0       | [0, 3] → 5 + (-5)    | 0               |
# | 1       | [1, 4] → 2 + 1       | 3               |
# | 2       | [2] → -10            | -10             |
# | 3       | [3] → -5             | -5              |
# | 4       | [4] → 1              | 1               |

# → Giá trị lớn nhất là **3** (khi bắt đầu ở vị trí 1).

# #### Output:

# ```python
# 3
# ```

# ---

# ### 💡 **Ý tưởng: Dynamic Programming**

# Ta có thể định nghĩa:

# ```
# dp[i] = tổng năng lượng tối đa có thể thu được nếu bắt đầu từ phòng i.
# ```

# Khi đó:

# ```
# dp[i] = energy[i] + (dp[i + k] nếu i + k < n, ngược lại là 0)
# ```

# Vì ta chỉ có thể đi **từ i → i + k**, ta duyệt **ngược từ cuối về đầu** để cập nhật `dp`.

# Cuối cùng, đáp án là:

# ```
# max(dp[i] for i in range(n))
# ```

# ---

# ### 🧮 **Code minh họa (Python):**

# ```python
# class Solution:
#     def maximumEnergy(self, energy: List[int], k: int) -> int:
#         n = len(energy)
#         dp = energy[:]  # sao chép mảng ban đầu
#         for i in range(n - k - 1, -1, -1):
#             dp[i] += dp[i + k]
#         return max(dp)
# ```

# ---

# ### 🚀 **Tóm tắt:**

# * Mỗi lần bạn chỉ có thể nhảy cách `k` phòng.
# * Bắt đầu ở vị trí `i`, bạn thu năng lượng `energy[i] + energy[i+k] + ...`.
# * Duyệt ngược và tính tổng cộng dồn theo bước `k`.
# * Lấy giá trị lớn nhất.

# ---

# Bạn có muốn mình giải thích thêm **vì sao phải duyệt ngược (từ n-k-1 về 0)** và **cách tối ưu bộ nhớ** không?
