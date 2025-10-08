# 2300. Successful Pairs of Spells and Potions(08/10/2025)
# Rất hay — bạn đang hỏi về **một lời giải khác** cho bài **2300. Successful Pairs of Spells and Potions** mà **không dùng binary search**, mà dùng **đếm tần suất + mảng tích lũy (prefix sum / cumulative sum)** ✅

# Dưới đây là **phiên bản đã thêm chú thích chi tiết từng dòng** + **giải thích thuật toán đầy đủ** 👇

# ---

# ### ✅ Code có chú thích

# ```python
# from typing import List
from typing import List
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        max_spells = max(spells)  # 1️⃣ Tìm giá trị spell lớn nhất để xác định kích thước mảng đếm
        smaller_count = [0] * (max_spells + 1)  # 2️⃣ Mảng đếm số potion có thể ghép với spell >= giá trị nào đó

        # 3️⃣ Với mỗi potion, tính "giá trị spell tối thiểu" cần để tạo ra cặp thành công
        for num in potions:
            curr = success // num  # Spell cần ít nhất là success / num (làm tròn lên)
            if success % num != 0:  # Nếu không chia hết → phải làm tròn lên
                curr += 1
            if curr > max_spells:   # Nếu spell lớn nhất vẫn không đủ mạnh → bỏ qua
                continue
            smaller_count[curr] += 1  # Spell từ curr trở lên đều "thành công" với potion này

        # 4️⃣ Tính tổng tích lũy để biết với mỗi spell ≤ x, có bao nhiêu potion thành công
        for i in range(1, len(smaller_count)):
            smaller_count[i] += smaller_count[i - 1]

        # 5️⃣ Với mỗi spell, lấy ra số potion thỏa điều kiện
        ans = []
        for num in spells:
            ans.append(smaller_count[num])
        return ans
# ```

# ---

# ### 🧠 Giải thích thuật toán

# #### 🎯 Mục tiêu

# Ta cần đếm **số lượng potions** sao cho:

# ```
# spell * potion >= success
# ```

# ---

# #### 🧩 Ý tưởng chính

# Thay vì duyệt hoặc tìm nhị phân, ta **chuyển hướng vấn đề**:

# * Với mỗi `potion`, ta tính **giá trị spell nhỏ nhất cần thiết** để thành công:

#   ```
#   spell_min = ceil(success / potion)
#   ```
# * Tức là:
#   Nếu `spell >= spell_min` → cặp này **thành công**.
#   Nếu `spell < spell_min` → **thất bại**.

# ---

# #### ⚙️ Cách hoạt động cụ thể

# | potion | success | success // potion | Cần làm tròn | spell_min |
# | :----: | :-----: | :---------------: | :----------: | :-------: |
# |    2   |    10   |         5         |   ✅ +1 → 6   |     6     |
# |    3   |    10   |         3         |   ✅ +1 → 4   |     4     |
# |    5   |    10   |         2         |       ❌      |     2     |

# Vậy:

# * Potion có `spell_min = 6`: chỉ spell ≥ 6 thành công.
# * Potion có `spell_min = 4`: chỉ spell ≥ 4 thành công.
# * Potion có `spell_min = 2`: chỉ spell ≥ 2 thành công.

# Ta **tăng đếm tại chỉ số `spell_min`** → nghĩa là mọi spell từ giá trị đó trở lên **được cộng thêm 1** potion thành công.

# ---

# #### 🔄 Sau đó dùng prefix sum:

# * `smaller_count[i]` = tổng số potion có thể ghép thành công với spell ≤ i.

# ---

# #### 🧮 Ví dụ cụ thể

# ```
# spells = [3, 5, 10]
# potions = [2, 3, 5]
# success = 10
# ```

# **Bước 1:**

# | Potion | success // num | Làm tròn | spell_min | Ghi vào mảng smaller_count |
# | :----- | :------------- | :------- | :-------- | :------------------------- |
# | 2      | 5              | +1       | 6         | smaller_count[6] += 1      |
# | 3      | 3              | +1       | 4         | smaller_count[4] += 1      |
# | 5      | 2              | 0        | 2         | smaller_count[2] += 1      |

# **smaller_count (ban đầu):**

# ```
# [0, 0, 1, 0, 1, 0, 1]
# ```

# **Bước 2: Tính tổng tích lũy**

# ```
# [0, 0, 1, 1, 2, 2, 3]
# ```

# **Bước 3: Lấy kết quả cho từng spell**

# | Spell | smaller_count[spell] | Kết quả     |
# | :---- | :------------------- | :---------- |
# | 3     | 1                    | ✅ 1 potion  |
# | 5     | 2                    | ✅ 2 potions |
# | 10    | 3                    | ✅ 3 potions |

# → **Output:** `[1, 2, 3]`

# ---

# ### ⚖️ Độ phức tạp

# * **Thời gian:** `O(max(spells) + len(potions))`
#   (Nhanh hơn `O(n log n)` của cách binary search nếu giá trị spell nhỏ)
# * **Không gian:** `O(max(spell))`

# ---

# 👉 **Tóm lại**:
# Thuật toán này dùng **mảng đếm + prefix sum** để thay thế cho **binary search**, giúp tối ưu khi `max(spells)` nhỏ hơn số lượng phần tử.

# ---

# Bạn có muốn mình vẽ **biểu đồ minh họa (trục spell và số potion thành công)** để dễ hình dung hơn không?

# Dĩ nhiên 😊 — đây là **giải thích chi tiết đề bài LeetCode 2300: “Successful Pairs of Spells and Potions”**

# ---

# ### 🧩 **Đề bài**

# Bạn được cho:

# * Một mảng **spells** gồm `n` phần tử (mỗi phần tử là *sức mạnh phép thuật*).
# * Một mảng **potions** gồm `m` phần tử (mỗi phần tử là *sức mạnh thuốc tiên*).
# * Một số nguyên **success** — đây là *mức ngưỡng thành công*.

# Một cặp `(spell, potion)` được gọi là **thành công (successful)** nếu:

# ```
# spell * potion >= success
# ```

# ---

# ### 🎯 **Yêu cầu**

# Với **mỗi spell** trong mảng `spells`, hãy **đếm** xem có bao nhiêu potion trong `potions` sao cho cặp đó là *thành công*.

# Trả về một mảng `ans` có cùng độ dài với `spells`, trong đó:

# ```
# ans[i] = số lượng potion sao cho spells[i] * potion >= success
# ```

# ---

# ### 💡 **Ví dụ**

# #### 🧮 Input:

# ```python
# spells = [5, 1, 3]
# potions = [1, 2, 3, 4, 5]
# success = 7
# ```

# #### ✅ Output:

# ```python
# [4, 0, 3]
# ```

# #### 🔍 Giải thích:

# * Spell = 5:

#   * 5×1=5 ❌
#   * 5×2=10 ✅
#   * 5×3=15 ✅
#   * 5×4=20 ✅
#   * 5×5=25 ✅
#     → Có **4 potion thành công**

# * Spell = 1:

#   * 1×1=1 ❌
#   * 1×2=2 ❌
#   * 1×3=3 ❌
#   * 1×4=4 ❌
#   * 1×5=5 ❌
#     → Có **0 potion thành công**

# * Spell = 3:

#   * 3×1=3 ❌
#   * 3×2=6 ❌
#   * 3×3=9 ✅
#   * 3×4=12 ✅
#   * 3×5=15 ✅
#     → Có **3 potion thành công**

# ➡️ Kết quả: `[4, 0, 3]`

# ---

# ### ⚙️ **Tư duy giải**

# 1. Sắp xếp `potions` tăng dần.
# 2. Với mỗi `spell`, tìm potion nhỏ nhất sao cho `spell * potion >= success`.
# 3. Dùng **binary search** (tìm kiếm nhị phân) để nhanh hơn (O(n log m)).

# Ví dụ:

# ```python
# import bisect

# def successfulPairs(spells, potions, success):
#     potions.sort()
#     m = len(potions)
#     res = []

#     for s in spells:
#         # Tìm vị trí đầu tiên trong potions sao cho s * potions[idx] >= success
#         idx = bisect.bisect_left(potions, success / s)
#         res.append(m - idx)
    
#     return res
# ```

# ---

# Nếu bạn muốn, mình có thể **giải thích chi tiết từng dòng code** hoặc **vẽ bảng mô phỏng chạy ví dụ** cho bài này — bạn muốn phần nào trước?
