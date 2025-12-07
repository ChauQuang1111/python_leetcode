# # // 1523. Count Odd Numbers in an Interval Range(07/12/2025)
# # // Dưới đây là **giải thích rõ ràng – dễ hiểu** cho đề bài **1523. Count Odd Numbers in an Interval Range** trên LeetCode.
# # // Dưới đây là**giải thích thuật toán**,kèm**code đầy đủ có hàm`main`dùng`Scanner`**,và**chú thích từng dòng**giúp bạn hiểu rõ.
# Dưới đây là **giải thích thuật toán** + **code có chú thích từng dòng** để bạn hiểu rõ cách hoạt động.

# ---

# # ✅ **Giải thích thuật toán**

# Bài toán:
# Đếm xem trong đoạn `[low, high]` có bao nhiêu số lẻ.

# Thuật toán này làm theo tư duy **đếm số phần tử trong đoạn**, rồi xử lý theo **chẵn/lẻ**:

# ---

# ## 1️⃣ Tính số lượng phần tử trong đoạn

# ```python
# cnt = high - low + 1
# ```

# Ví dụ: low=4, high=9
# → 6 số: 4,5,6,7,8,9

# ---

# ## 2️⃣ Nếu số lượng phần tử (`cnt`) là **chẵn**

# Trong 1 cặp 2 số liên tiếp → có 1 số lẻ, 1 số chẵn.

# → Nếu `cnt` chẵn thì số lẻ = `cnt/2`

# Ví dụ: 6 số ⇒ 3 số lẻ

# ---

# ## 3️⃣ Nếu số lượng phần tử (`cnt`) là **lẻ**

# Luôn có **một số nằm ở giữa**, ta xem số đó có phải số lẻ hay không:

# ### 🔹 TH1: Nếu `low` là số **chẵn**

# → Dãy dạng: chẵn – lẻ – chẵn – lẻ – ... – chẵn
# → Số lẻ = `floor(cnt / 2)`

# ### 🔹 TH2: Nếu `low` là số **lẻ**

# → Dãy dạng: lẻ – chẵn – lẻ – chẵn – ... – lẻ
# → Số lẻ = `ceil(cnt / 2)`

# ---

# # ✅ **Code Python (đã thêm chú thích từng dòng)**

# ```python
import math

class Solution:
    def countOdds(self, low: int, high: int) -> int:

        # Số lượng phần tử trong đoạn [low, high]
        cnt = high - low + 1

        # Nếu cnt là số lẻ
        if cnt % 2 == 1:

            # TH1: low là số chẵn → dãy bắt đầu bằng chẵn
            # Ví dụ: 4,5,6,...  -> lẻ nằm ở vị trí 1,3,5...
            if low % 2 == 0:
                return math.floor(cnt / 2)

            # TH2: low là số lẻ → dãy bắt đầu bằng lẻ
            # Ví dụ: 5,6,7,... -> nhiều hơn 1 số lẻ
            else:
                return math.ceil(cnt / 2)

        # Nếu cnt là số chẵn thì đúng 1 nửa là số lẻ
        return cnt // 2

# # 🔍 Ví dụ minh họa

# ### Input:

# ```
# low = 3
# high = 7
# ```

# | Số | Lẻ? |
# | -- | --- |
# | 3  | ✔   |
# | 4  | ✖   |
# | 5  | ✔   |
# | 6  | ✖   |
# | 7  | ✔   |

# `cnt = 5` (lẻ)
# `low = 3` (lẻ) → dùng `ceil(5/2) = 3`

# ✔ Kết quả: **3 số lẻ**

# ---

# Nếu bạn muốn mình viết **phiên bản tối ưu O(1)** hoặc **so sánh 2 thuật toán**, mình làm tiếp cho bạn nhé!

# // ---

# // #✅**Giải thích thuật toán**

# // Công thức dùng trong bài:

# // ```java(high+1)/2-(low/2)```

# // Ý nghĩa:

# // ###1 ️⃣`(x/2)`đếm**bao nhiêu số chẵn**từ 0 đến x

# // →hoặc nói cách khác,`x/2`cũng cho biết**bao nhiêu số lẻ**từ 1 đến x−1.

# // ###2 ️⃣Số lượng số lẻ từ 1 đến high:

# // ```(high+1)/2```

# // Ví dụ:high=7→(7+1)/2=4 số lẻ→1,3,5,7 high=8→(8+1)/2=4 số lẻ→1,3,5,7

# // ###3 ️⃣Số lượng số lẻ từ 1 đến low−1:

# // ```low/2```

# // NOTE:low=4→4/2=2 số lẻ⇒1,3 low=5→5/2=2 số lẻ⇒1,3(đúng vì 5 chưa được tính vào)

# // ###4 ️⃣Số lẻ nằm trong đoạn[low,high]:

# // ```(#số lẻ đến high)−(#số lẻ đến low−1)```

# // →chính là:

# // ```java(high+1)/2-(low/2)```

# // **Thuật toán O(1),nhanh nhất,không dùng vòng lặp.**

# // ---

# // #✅**Code hoàn chỉnh(Java)**

# // ###➤Có`main`

# // ###➤Dùng`Scanner`

# // ###➤Có chú thích từng dòng

# import java.util.Scanner;

# public class b111 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int low = sc.nextInt();
#         int high = sc.nextInt();
#         System.out.println(countOdds(low, high));
#     }

#     // Hàm đếm số lẻ trong khoảng [low, high]
#     public static int countOdds(int low, int high) {
#         // (high + 1) / 2 = số lượng số lẻ từ 1 đến high
#         // (low / 2) = số lượng số lẻ từ 1 đến low - 1
#         // Hiệu = số lẻ trong khoảng [low, high]
#         return (high + 1) / 2 - (low / 2);
#     }

# }

# // # 🔍 Ví dụ chạy thử

# // Input:

# // ```
# // low = 3
# // high = 7
# // ```

# // * (7 + 1) / 2 = 4
# // * 3 / 2 = 1
# // * 4 − 1 = **3 số lẻ**

# // Output:

# // ```
# // 3
# // ```

# // ---

# // Nếu bạn muốn mình viết thêm **phiên bản không cần đối tượng (dùng static)**
# // hoặc **giải thích bằng hình minh hoạ**, mình làm tiếp cho bạn nhé!

# // ---

# // # ✅ **Giải thích đề bài**

# // Bạn được cho **hai số nguyên**:

# // * `low`
# // * `high`

# // Chúng tạo thành một **khoảng [low, high]** (bao gồm cả 2 đầu).

# // 👉 Nhiệm vụ: **Đếm có bao nhiêu số lẻ trong khoảng đó.**

# // ---

# // # ✨ Ví dụ

# // **Ví dụ 1:**

# // ```
# // Input: low = 3, high = 7
# // ```

# // Các số trong khoảng: 3, 4, 5, 6, 7
# // Số lẻ: **3, 5, 7 → tổng: 3 số**

# // ---

# // **Ví dụ 2:**

# // ```
# // Input: low = 8, high = 10
# // ```

# // Trong khoảng: 8, 9, 10
# // Số lẻ: **9 → tổng: 1 số**

# // ---

# // # ❗ Lưu ý

# // * Khoảng này **bao gồm** cả `low` và `high`.
# // * Chỉ cần đếm **số lẻ**, không phải liệt kê.

# // ---

# // # 🧠 Ý tưởng giải nhanh nhất

# // Số lượng phần tử của đoạn [low, high]:

# // ```
# // n = high - low + 1
# // ```

# // Số lẻ ≈ một nửa số lượng, nhưng phụ thuộc vào low và high có phải số lẻ hay
# // không.

# // ### Công thức chuẩn (LeetCode solution):

# // ```
# // Nếu low và high đều là số lẻ → kết quả = (high - low) / 2 + 1
# // Ngược lại → kết quả = (high - low + 1) / 2
# // ```

# // ---

# // # 📌 Ví dụ kiểm tra nhanh

# // **low = 4, high = 9**

# // Số lượng = 6
# // low chẵn – high lẻ → áp dụng công thức thứ 2:

# // ```
# // odds = (9 - 4 + 1) / 2 = 6 / 2 = 3
# // ```

# // Thực tế:
# // 4, 5, 6, 7, 8, 9
# // → số lẻ: 5, 7, 9 → đúng 3.

# // ---

# // Nếu bạn muốn mình giải thích **vì sao công thức đúng**, hoặc viết **code
# // Java/Python/C++** tối ưu 100%, mình làm tiếp nhé!
