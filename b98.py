# 3234. Count the Number of Substrings With Dominant Ones(15/11/2025)
# Dưới đây là **giải thích đề bài LeetCode 3234 — Count the Number of Substrings With Dominant Ones** một cách **rõ ràng – dễ hiểu**.
# Dưới đây là **giải thích đề bài**, **giải thích thuật toán**, và **code đã được chú thích đầy đủ** để bạn hiểu rõ từng bước.

# ---

# # ✅ **Giải thích đề bài (LeetCode 3234 — Count the Number of Substrings With Dominant Ones)**

# Một chuỗi nhị phân `s` có **substring chủ đạo bởi số 1** (dominant ones) nếu:

# [
# #ones ; \ge ; (#zeros)^2
# ]

# Tức là:

# * Nếu substring có **nhiều số 0**, thì số 1 phải **nhiều hơn bình phương số 0**.
# * Nếu substring không có số 0 ⇒ luôn thỏa mãn, vì `(#zeros)^2 = 0`.

# 👉 **Nhiệm vụ:** Đếm có bao nhiêu substring thỏa điều kiện trên.

# ---

# # ⚠️ Bài này rất khó (Hard).

# * Số lượng substring = O(n²) → n có thể tới 2×10⁵ → không thể duyệt brute force.
# * Điều kiện `ones ≥ zeros²` là phi tuyến → không dễ dùng kỹ thuật 2 con trỏ.

# Solution bạn đưa là một thuật toán tối ưu với **nhảy chỉ mục (jumping)** dựa trên:

# * prefix sum của số 0
# * danh sách vị trí các số 0 và số 1
# * nhảy theo điều kiện toán học để bỏ qua những điểm không cần xét

# ---

# # 🚀 **Ý tưởng chính của thuật toán**

# ## 1️⃣ Ta giữ:

# * `cumZeros[i]` = số lượng số 0 trong đoạn s[0..i-1]
# * `posZeros[]` = danh sách vị trí số 0
# * `posOnes[]` = danh sách vị trí số 1

# ## 2️⃣ Khi đang đứng tại vị trí `i`, thuật toán:

# * Xét các substring kết thúc tại `i`: `[left, i]`
# * Nhưng không xét tuần tự từ `i→0`
#   → **nhảy (jump)** để bỏ qua hàng loạt vị trí không hợp lệ.

# ## 3️⃣ Hai hướng nhảy:

# * **nhảy theo số 0** nếu `(zeros² <= ones)` thỏa
# * **nhảy theo số 1** nếu chưa thỏa điều kiện

# ## 4️⃣ Mỗi lần nhảy, ta có thể:

# * cộng trực tiếp nhiều substring 1 lượt (không cần đếm từng cái)
# * tối ưu về thời gian

# ---

# # ✅ Code Python đã được chú thích đầy đủ

# ```python
from math import ceil
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        # cumZeros[i] = số lượng số 0 trong s[0..i-1]
        cumZeros = [0] * (n + 1)

        # vị trí của các số 0 và 1
        posZeros = [-1]
        posOnes = [-1]

        res = 0

        for i, c in enumerate(s):

            # --- cập nhật số 0 / số 1 hiện tại ---
            if c == '1':
                posOnes.append(i)
                res += 1   # substring (i,i) luôn hợp lệ (1 >= 0^2)
                curZeros = cumZeros[i]
                curOnes = i - curZeros + 1
                left = posZeros[curZeros - 1]   # nhảy theo vị trí zero
            else:
                posZeros.append(i)
                curZeros = cumZeros[i] + 1
                curOnes = i - curZeros + 1
                left = posOnes[curOnes]        # nhảy theo vị trí one

            # cập nhật prefix sum số 0
            cumZeros[i + 1] = curZeros

            right = i

            # --- Bắt đầu nhảy ngược để tìm left ---
            while left >= 0:
                countZero = curZeros - cumZeros[left]           # số zero trong [left..i]
                countOne = (i - left + 1) - countZero           # số one trong [left..i]
                sqZero = countZero * countZero

                # Nếu thỏa điều kiện ones >= zeros^2
                if sqZero <= countOne:

                    if s[left] == "1":
                        res += 1              # chỉ cộng substring [left, i]
                    else:
                        res += right - left   # cộng nhiều substring một lần

                    # Cập nhật right để tránh đếm trùng
                    right = left

                    # Tính toán vị trí zero tiếp theo để nhảy
                    nextZero = curZeros - ceil((countOne + 1) ** 0.5) + 1
                    left = posZeros[nextZero] if nextZero >= 0 else -1

                else:
                    # Không thỏa điều kiện
                    if s[left] == "0":
                        res += right - left - 1

                    right = left

                    # nhảy theo số 1
                    nextOne = curOnes - sqZero + 1
                    left = posOnes[nextOne] if nextOne >= 0 else -1

            # Nếu cả đoạn từ 0..i đều hợp lệ thì cộng tất cả substring
            if curZeros * curZeros <= curOnes:
                res += right

        return res
# ```

# ---

# # 📌 Giải thích ngắn gọn dễ hiểu

# ### Tại mỗi `i`, ta muốn đếm số substring kết thúc tại `i`:

# ```
# [left, i]
# [left+1, i]
# ...
# [i, i]
# ```

# Nhưng không duyệt từng cái.

# Thay vào đó:

# * dùng toán học suy ra “điểm breakpoint” mà từ đó trở đi tất cả substring đều thỏa hoặc đều không thỏa.
# * nhảy bằng cách dùng chỉ số của zeros/ones trong posZeros và posOnes.

# → Mỗi vòng lặp while chỉ chạy O(√n) lần, tổng thể O(n√n).

# ---

# # Nếu bạn muốn:

# 👉 Mình có thể vẽ sơ đồ minh họa từng bước chạy thuật toán
# 👉 Hoặc viết lại phiên bản **ngắn gọn / dễ hiểu hơn** (nhưng có thể chậm hơn)
# 👉 Hoặc viết lại bằng **Java**

# Bạn cần loại nào?

# ---

# # 🧩 **3234. Count the Number of Substrings With Dominant Ones**

# Bạn được cho một chuỗi nhị phân `s` gồm `'0'` và `'1'`.

# Một **substring** (chuỗi con liên tiếp) được gọi là **DOMINANT ONES** nếu:

# ### 👉 **Số lượng '1' trong substring ≥ (độ dài substring)²**

# Nhiệm vụ:
# ➡️ **Đếm xem có bao nhiêu substring thỏa điều kiện trên.**

# ---

# # 🔍 Ví dụ minh họa

# Giả sử:

# ```
# s = "110"
# ```

# Tất cả substring:

# 1. `"1"` → 1 one → length = 1 → 1 ≥ 1² = 1 ✔
# 2. `"1"` → 1 ≥ 1 ✔
# 3. `"0"` → 0 ≥ 1 ✘
# 4. `"11"` → 2 ones → length = 2 → 2 ≥ 4 ✘
# 5. `"10"` → 1 ≥ 4 ✘
# 6. `"110"` → 2 ≥ 9 ✘

# ➡️ Tổng: **2 substring hợp lệ**

# ---

# # 🎯 Điều kiện quan trọng

# Substring `s[l..r]` (từ l đến r) có chiều dài `k = r - l + 1`.

# Điều kiện:

# ```
# số lượng '1' ≥ k² 
# ```

# Ví dụ:

# | substring | length k | ones | k² | hợp lệ? |
# | --------- | -------- | ---- | -- | ------- |
# | "1"       | 1        | 1    | 1  | ✔       |
# | "11"      | 2        | 2    | 4  | ✘       |
# | "1111"    | 4        | 4    | 16 | ✘       |
# | "11111"   | 5        | 5    | 25 | ✘       |

# Bạn thấy rằng **chiều dài tăng nhanh hơn số 1**, nên chỉ substring rất ngắn mới có thể hợp lệ.

# ---

# # ⚠️ Nhận xét quan trọng

# Vì `k²` tăng RẤT NHANH, nên khi `k > sqrt(n)`, substring gần như chắc chắn không hợp lệ.

# → giải pháp sẽ tập trung vào:

# * duyệt theo số lượng ‘1’
# * hoặc duyệt k nhỏ

# ---

# # 💡 Tóm tắt đề bài → rất khó nếu duyệt brute force

# Số substring = O(n²) → với n = 2e5, duyệt tất cả sẽ TLE.

# Nhưng dựa vào điều kiện `ones ≥ k²` → **k rất nhỏ**, chỉ khoảng ≤ 450.

# Nên ta chỉ duyệt k nhỏ và đếm substring hợp lệ.

# ---

# # 📌 Nếu bạn muốn, mình có thể:

# ✔ Giải thích thuật toán tối ưu
# ✔ Viết code Python / Java
# ✔ Giải thích code dòng-từng-dòng

# Chỉ cần bạn nói: **"giải thích thuật toán"** hoặc **"viết code Java"** nhé!

