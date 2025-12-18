
# # // 3652. Best Time to Buy and Sell Stock using Strategy(18/12/2025)
# # // Mình sẽ **giải thích đề bài 3652 – Best Time to Buy and Sell Stock using Strategy** **bằng tiếng Việt, rõ ràng, đúng bản chất**, để bạn đọc đề là hiểu ngay nên làm gì 👇
# Mình sẽ làm **đúng 2 việc bạn yêu cầu**:

# 1. ✅ **Giải thích thuật toán từ bản chất → chi tiết**
# 2. ✅ **Viết lại code có chú thích từng khối, từng dòng quan trọng**

# Không bỏ sót bước nào 👍

# ---

# # I. GIẢI THÍCH THUẬT TOÁN (DỄ HIỂU)

# ## 1. Bài toán đang làm gì?

# * `prices[i]` : giá ngày `i`
# * `strategy[i]` ∈ `{ -1, 0, 1 }`

#   * `1`  → Buy
#   * `-1` → Sell
#   * `0`  → Hold
# * Ta được **chọn 1 đoạn liên tiếp dài `k`** và **đảo chiến lược trong đoạn đó**
# * Mỗi giao dịch cần **2 hành động** → số ngày ảnh hưởng thật sự = `m = k // 2`

# ---

# ## 2. Lợi nhuận ban đầu (KHÔNG đảo)

# ```python
# A[i] = strategy[i] * prices[i]
# base = sum(A)
# ```

# | strategy | Ý nghĩa | A[i]   |
# | -------- | ------- | ------ |
# | 1        | Buy     | +price |
# | -1       | Sell    | -price |
# | 0        | Hold    | 0      |

# 👉 `base` = lợi nhuận nếu **không làm gì thêm**

# ---

# ## 3. Nếu đảo chiến lược trong đoạn dài `k` thì sao?

# Chiến lược bị đảo:

# ```text
# strategy[i] → -strategy[i]
# ```

# Thay đổi lợi nhuận tại ngày `i`:

# ```text
# delta = (-strategy[i] * price[i]) - (strategy[i] * price[i])
#       = -2 * strategy[i] * price[i]
# ```

# ⚠️ Nhưng không cộng thẳng như vậy
# 👉 Vì **chỉ nửa sau của đoạn mới sinh lợi thật**

# ---

# ## 4. Vì sao chỉ dùng nửa sau đoạn (`m = k//2`)?

# * Một giao dịch = **Buy + Sell**
# * Nửa đầu tạo vị thế
# * **Nửa sau mới đóng vị thế → sinh lời**

# 👉 Vì vậy ta chỉ cộng `prices[m … k-1]`

# ---

# ## 5. Công thức lợi nhuận tăng thêm (delta)

# Với cửa sổ bắt đầu tại `l`:

# ```text
# delta =
# (sum prices của [l+m, l+k-1])
# − (sum A của [l, l+k-1])
# ```

# ---

# ## 6. Sliding Window O(n)

# * `sumA`  = tổng `A` trong đoạn dài `k`
# * `sumP2` = tổng giá của **nửa sau**
# * Trượt cửa sổ từng bước → tìm `bestDelta`

# ---

# ## 7. Kết quả cuối

# ```python
# return base + max(0, bestDelta)
# ```

# * Nếu đảo không có lợi → không đảo
# * Ngược lại → cộng thêm lợi nhuận tốt nhất

# ---

# # II. CODE PYTHON + CHÚ THÍCH CHI TIẾT

# ```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        # m: số ngày thực sự tạo lợi nhuận (mỗi giao dịch cần 2 ngày)
        m = k // 2
        
        # -------------------------------
        # 1. Lợi nhuận ban đầu (không đảo)
        # -------------------------------
        # A[i] = lợi nhuận tại ngày i theo strategy gốc
        A = [strategy[i] * prices[i] for i in range(n)]
        base = sum(A)

        # --------------------------------------------
        # 2. Sliding window tìm lợi nhuận tăng thêm
        # --------------------------------------------

        # Tổng A của cửa sổ đầu tiên [0 .. k-1]
        sumA = sum(A[:k])

        # Tổng giá của nửa sau cửa sổ [m .. k-1]
        sumP2 = sum(prices[m:k])

        # Lợi nhuận tăng thêm khi đảo cửa sổ đầu tiên
        bestDelta = sumP2 - sumA

        # --------------------------------------------
        # 3. Trượt cửa sổ sang phải
        # --------------------------------------------
        for l in range(1, n - k + 1):
            # Cập nhật tổng A của cửa sổ mới
            sumA += A[l + k - 1] - A[l - 1]

            # Cập nhật tổng giá của nửa sau
            sumP2 += prices[l + k - 1] - prices[l + m - 1]

            # Lợi nhuận tăng thêm nếu đảo đoạn [l .. l+k-1]
            cur = sumP2 - sumA

            # Cập nhật giá trị tốt nhất
            if cur > bestDelta:
                bestDelta = cur

        # Nếu đảo không có lợi → không đảo
        if bestDelta < 0:
            bestDelta = 0

        # Tổng lợi nhuận = ban đầu + lợi nhuận tăng thêm
        return base + bestDelta
# ```

# ---

# # III. TÓM TẮT 1 CÂU (RẤT QUAN TRỌNG)

# > **Bài này biến “đảo strategy” thành “tìm đoạn dài k có (tổng giá nửa sau − tổng lợi nhuận gốc) lớn nhất” bằng sliding window.**

# ---

# Nếu bạn muốn:

# * 🔹 Chạy **ví dụ số từng bước**
# * 🔹 So sánh **Java vs Python**
# * 🔹 Viết lại theo **DP để đối chiếu**

# 👉 Cứ nói, mình làm tiếp cho bạn 👌



# import java.util.*;
# public class b121 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         // Nhập số ngày
#         int n = sc.nextInt();

#         int[] prices = new int[n];
#         int[] strategy = new int[n];

#         // Nhập giá cổ phiếu
#         for (int i = 0; i < n; i++) {
#             prices[i] = sc.nextInt();
#         }

#         // Nhập strategy (-1, 0, 1)
#         for (int i = 0; i < n; i++) {
#             strategy[i] = sc.nextInt();
#         }

#         // Nhập k
#         int k = sc.nextInt();

#         long result = maxProfit(prices, strategy, k);
#         System.out.println(result);
#     }

#     // Hàm giải bài toán
#     public static long maxProfit(int[] prices, int[] strategy, int k) {
#         int n = prices.length;

#         // sum: lợi nhuận ban đầu nếu KHÔNG đảo strategy
#         long sum = 0;

#         // kk: số ngày ảnh hưởng thực sự (mỗi giao dịch cần 2 ngày)
#         int kk = k / 2;

#         // current: lợi nhuận tăng thêm khi đảo đoạn hiện tại
#         long current = 0;

#         // max: lợi nhuận tăng thêm lớn nhất trong các đoạn
#         long max = 0;

#         /*
#          * =======================
#          * 1. Xử lý kk ngày đầu
#          * =======================
#          */
#         for (int i = 0; i < kk; i++) {
#             int val = prices[i] * strategy[i];

#             // cộng lợi nhuận ban đầu
#             sum += val;

#             // lợi nhuận tăng thêm nếu đảo strategy tại ngày i
#             current += prices[i] - val;
#         }

#         /*
#          * =======================
#          * 2. Mở rộng đến đủ k ngày
#          * =======================
#          */
#         for (int i = kk; i < k; i++) {
#             int val = prices[i] * strategy[i];

#             sum += val;

#             // thêm ngày mới, bỏ ảnh hưởng ngày i - kk
#             current += prices[i] - val - prices[i - kk];
#         }

#         // cập nhật max cho cửa sổ đầu tiên
#         max = Math.max(max, current);

#         /*
#          * =======================
#          * 3. Trượt cửa sổ trên toàn mảng
#          * =======================
#          */
#         for (int i = k; i < n; i++) {
#             int val = prices[i] * strategy[i];

#             sum += val;

#             // Sliding window:
#             // + thêm ngày i
#             // - bỏ ngày i - kk
#             // + hoàn lại lợi nhuận gốc của ngày i - k
#             current += prices[i]
#                     - val
#                     - prices[i - kk]
#                     + prices[i - k] * strategy[i - k];

#             // cập nhật lợi nhuận tăng thêm lớn nhất
#             max = Math.max(max, current);
#         }

#         // tổng lợi nhuận = ban đầu + tăng thêm tốt nhất
#         return sum + max;
#     }

# }

# // ---

# // ## 1. Tên bài nói lên điều gì?

# // **Best Time to Buy and Sell Stock using Strategy**

# // 👉 Không chỉ mua–bán bình thường
# // 👉 Mà phải **làm theo CHIẾN LƯỢC (strategy)** được cho trong đề

# // ---

# // ## 2. Nội dung cốt lõi của đề bài

# // Bạn được cho:

# // * Một mảng `prices`

# // * `prices[i]` = giá cổ phiếu ở **ngày i**
# // * Một chuỗi `strategy`

# // * `strategy[i]` mô tả **bạn phải làm gì ở ngày i**

# // Mỗi ký tự trong `strategy` có thể là:

# // | Ký tự | Ý nghĩa |
# // | ----- | ------------------------------- |
# // | `'B'` | **Buy** – bắt buộc phải mua |
# // | `'S'` | **Sell** – bắt buộc phải bán |
# // | `'H'` | **Hold** – không được giao dịch |

# // ---

# // ## 3. Quy tắc giao dịch (rất quan trọng)

# // 1. ❗ **Mỗi thời điểm chỉ được giữ tối đa 1 cổ phiếu**
# // 2. ❗ **Không được bán khi chưa mua**
# // 3. ❗ Phải **tuân thủ strategy tuyệt đối**
# // 4. Lợi nhuận = tổng (giá bán − giá mua)

# // ---

# // ## 4. Bài toán hỏi gì?

# // 👉 Sau khi thực hiện **đúng strategy**,
# // 👉 **lợi nhuận lớn nhất có thể đạt được là bao nhiêu?**

# // Nếu không thể thực hiện strategy hợp lệ → lợi nhuận = `0`

# // ---

# // ## 5. Ví dụ minh họa đơn giản

# // ### Ví dụ

# // ```
# // prices = [3, 2, 6, 5, 0, 3]
# // strategy = "BHSBHS"
# // ```

# // Diễn giải theo ngày:

# // | Ngày | Giá | Strategy | Hành động |
# // | ---- | --- | -------- | ----------- |
# // | 0 | 3 | B | Mua |
# // | 1 | 2 | H | Giữ |
# // | 2 | 6 | S | Bán → lãi 3 |
# // | 3 | 5 | B | Mua |
# // | 4 | 0 | H | Giữ |
# // | 5 | 3 | S | Bán → lãi 3 |

# // 👉 Tổng lợi nhuận = **6**

# // ---

# // ## 6. Bản chất bài toán

# // 👉 Đây là bài **mô phỏng + DP đơn giản**

# // Ta cần theo dõi:

# // * Đang **có cổ phiếu** hay **không**
# // * Lợi nhuận hiện tại
# // * Kiểm tra xem hành động theo strategy có hợp lệ không

# // ---

# // ## 7. Tư duy giải (chưa cần code)

# // ### Trạng thái cần theo dõi

# // * `cash` : lợi nhuận khi **không giữ cổ phiếu**
# // * `hold` : lợi nhuận khi **đang giữ cổ phiếu**

# // ---

# // ### Theo từng ngày

# // | Strategy | Xử lý |
# // | -------- | --------------------- |
# // | `'B'` | `hold = cash - price` |
# // | `'S'` | `cash = hold + price` |
# // | `'H'` | Không làm gì |

# // ⚠️ Nếu gặp hành động **không hợp lệ** (ví dụ bán khi chưa mua) → bỏ qua / kết
# // quả = 0

# // ---

# // ## 8. Khác gì với Stock I / II / V?

# // | Bài | Khác biệt |
# // | ------------------------ | ----------------------------------- |
# // | Stock I / II | Tự chọn ngày mua bán |
# // | Stock V | Tự chọn + có Long/Short |
# // | **Stock using Strategy** | ❗ **Bị ép hành động theo strategy** |

# // ---

# // ## 9. Tóm tắt 1 câu (rất quan trọng)

# // > **Bài này không hỏi “nên mua bán khi nào”, mà hỏi “làm đúng chiến lược thì
# // lãi được bao nhiêu”.**

# // ---

# // Nếu bạn muốn:

# // * ✅ Mình giải **từng dòng code mẫu**
# // * ✅ Mô phỏng bằng bảng ngày–tiền
# // * ✅ So sánh với Stock V để khỏi nhầm

# // 👉 Cứ nói, mình làm tiếp cho bạn 👍
# // Mình giải thích **thuật toán của đoạn code này từ gốc → ngọn**, vì đây
# // **không phải DP cổ điển**, mà là **sliding window + biến đổi lợi nhuận** (rất
# // dễ rối nếu không nhìn đúng bản chất).

# // ---

# // # 1. Hiểu lại đề bài (rất ngắn gọn)

# // * `prices[i]` : giá ngày `i`
# // * `strategy[i]` ∈ {`-1`, `0`, `1`}

# // * `1` → **Buy**
# // * `-1` → **Sell**
# // * `0` → **Hold**
# // * `k` : độ dài **đoạn chiến lược được phép đảo ngược**

# // 👉 Ta được phép **chọn đúng 1 đoạn dài k** và **đảo ngược chiến lược trong
# // đoạn đó**
# // 👉 Mục tiêu: **tối đa hóa lợi nhuận**

# // ---

# // # 2. Ý tưởng lõi của thuật toán

# // ### Bước 1 – Lợi nhuận ban đầu (KHÔNG đảo)

# // ```java
# // sum += prices[i] * strategy[i];
# // ```

# // Giải thích:

# // | strategy | Ý nghĩa | prices[i] * strategy[i] |
# // | -------- | ------- | ----------------------- |
# // | 1 | Buy | +prices[i] |
# // | -1 | Sell | -prices[i] |
# // | 0 | Hold | 0 |

# // 👉 `sum` = **lợi nhuận ban đầu nếu KHÔNG đảo gì cả**

# // ---

# // # 3. Đảo chiến lược nghĩa là gì?

# // Giả sử:

# // ```text
# // Ban đầu: strategy[i]
# // Sau đảo: -strategy[i]
# // ```

# // ### Mức lời THAY ĐỔI tại ngày `i`

# // ```text
# // delta = prices[i] * (-strategy[i]) - prices[i] * strategy[i]
# // = -2 * prices[i] * strategy[i]
# // ```

# // Nhưng code không viết thế ❌
# // 👉 code viết lại cho **dễ cộng dồn**

# // ---

# // # 4. Biến `current` là gì?

# // 👉 `current` = **lợi nhuận tăng thêm** nếu ta đảo đoạn đang xét

# // ```java
# // current += prices[i] - prices[i] * strategy[i];
# // ```

# // | strategy | prices - prices*strategy | Ý nghĩa |
# // | --------- | ------------------------ | ---------- |
# // | 1 (Buy) | 0 | Buy → Sell |
# // | -1 (Sell) | 2*price | Sell → Buy |
# // | 0 (Hold) | price | Hold → Buy |

# // 👉 Đây chính là **lãi phụ do đảo**

# // ---

# // # 5. Vì sao có `kk = k / 2`?

# // ⚠️ Vì:

# // * Mỗi giao dịch gồm **1 Buy + 1 Sell**
# // * Đoạn dài `k` chỉ tạo ra **tối đa k/2 giao dịch hợp lệ**

# // ```java
# // int kk = k / 2;
# // ```

# // 👉 Ta chỉ cần quan tâm **kk ngày đầu ảnh hưởng thực sự**

# // ---

# // # 6. Ba vòng for làm gì?

# // ---

# // ## 🔹 Vòng 1: Khởi tạo cửa sổ đầu tiên

# // ```java
# // for (int i = 0; i < kk; i++) {
# // val = prices[i] * strategy[i];
# // sum += val;
# // current += prices[i] - val;
# // }
# // ```

# // 👉

# // * Tính `sum` ban đầu
# // * Tính `current` cho **cửa sổ đầu tiên**

# // ---

# // ## 🔹 Vòng 2: Mở rộng đến đủ k phần tử

# // ```java
# // for (int i = kk; i < k; i++) {
# // current += prices[i] - val - prices[i - kk];
# // }
# // ```

# // 👉 Sliding window:

# // * Thêm ngày mới
# // * Loại ảnh hưởng ngày cũ `i - kk`

# // ---

# // ## 🔹 Vòng 3: Trượt cửa sổ trên toàn mảng

# // ```java
# // for (int i = k; i < n; i++) {
# // current += prices[i]
# // - prices[i] * strategy[i]
# // - prices[i - kk]
# // + prices[i - k] * strategy[i - k];

# // max = Math.max(max, current);
# // }
# // ```

# // 👉 Mỗi bước:

# // * Thêm ngày mới vào đoạn đảo
# // * Bỏ ngày cũ ra khỏi đoạn đảo
# // * Cập nhật **lợi nhuận đảo lớn nhất**

# // ---

# // # 7. Kết quả cuối cùng

# // ```java
# // return sum + max;
# // ```

# // | Thành phần | Ý nghĩa |
# // | ----------- | ----------------------------------- |
# // | `sum` | lợi nhuận ban đầu |
# // | `max` | lợi nhuận tăng thêm tốt nhất do đảo |
# // | `sum + max` | **kết quả tối ưu** |

# // ---

# // # 8. Tóm tắt 1 câu (rất quan trọng)

# // > **Bài này biến bài toán “đảo strategy” thành “tìm đoạn con dài k có lợi
# // nhuận tăng thêm lớn nhất” bằng sliding window.**

# // ---

# // Nếu bạn muốn:

# // * ✅ Mình vẽ **ví dụ số chạy từng dòng**
# // * ✅ So sánh với **DP version**
# // * ✅ Giải thích vì sao `prices[i - kk]` xuất hiện

# // 👉 Nói mình biết, mình làm tiếp cho bạn 👍
