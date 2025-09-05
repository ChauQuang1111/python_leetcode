
#  2749. Minimum Operations to Make the Integer Zero(05/09/2025)

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
 
     

        for i in range(61):
            target = num1 - num2 * i
            if target >= 0 and target.bit_count() <= i <= target:
                return i
        
        return -1

# Rồi 👍 mình giải thích chi tiết cho bạn đoạn Python này:

# ---

# ### Code của bạn:

# ```python
# class Solution:
#     def makeTheIntegerZero(self, num1: int, num2: int) -> int:
#         for i in range(61):
#             target = num1 - num2 * i
#             if target >= 0 and target.bit_count() <= i <= target:
#                 return i
#         return -1
# ```

# ---

# ### Ý tưởng thuật toán

# * Ta muốn chọn **i phép trừ** để cuối cùng số còn lại (`target`) có thể viết được bằng tổng các **lũy thừa của 2**.
# * Điều kiện quan trọng:

#   1. `target >= 0` → vì target âm thì không thể biểu diễn được.
#   2. `target.bit_count()` = số **bit 1** trong nhị phân của `target`.

#      * Đây là số lượng lũy thừa của 2 tối thiểu cần để ghép thành `target`.
#      * Ví dụ: `13 = 1101₂` có 3 bit 1 → cần ít nhất 3 số hạng: `8 + 4 + 1`.
#   3. `target.bit_count() <= i` → nghĩa là số phép `i` đủ để tách ra. Nếu `i` nhỏ hơn số bit 1 thì không thể.
#   4. `i <= target` → vì bạn không thể dùng nhiều hơn `target` số hạng (mỗi số hạng tối thiểu là 1).

# → Nếu cả 4 điều kiện đều đúng, thì trả về ngay `i`.



# ### Giải thích dòng:

# ```python
# if target >= 0 and target.bit_count() <= i <= target:
#     return i
# ```

# * `target >= 0`: đảm bảo kết quả sau khi trừ không âm.
# * `target.bit_count() <= i`: số lượng bit 1 nhỏ hơn hoặc bằng số phép i → tức là i đủ để “chia nhỏ” target thành các lũy thừa của 2.
# * `i <= target`: số phép i không được nhiều hơn giá trị target (ví dụ target = 5 thì không thể chia thành 6 số hạng dương).

# Nếu tất cả điều kiện thỏa mãn → ta đã tìm ra số phép trừ nhỏ nhất để biến `num1` về 0 theo quy tắc bài toán.

# ---

# 📌 Ví dụ chạy:
# `num1 = 3, num2 = -2`

# * i=3 → `target = 3 - (-2)*3 = 9`, nhị phân `1001₂`, `bit_count=2`.
# * Kiểm tra:

#   * target = 9 ≥ 0 ✅
#   * bit\_count = 2 ≤ i = 3 ✅
#   * i = 3 ≤ target = 9 ✅
#     → return 3.




# // Ý nghĩa
# // bài toán

# // Bạn được
# // cho hai
# // số nguyên
# // không âm`num1`và`num2`.Trong**
# // một phép**
# // bạn có
# // thể chọn
# // một số nguyên`i`
# // trong khoảng`[0,60]`và**trừ**vào`num1`
# // giá trị`num2+2^i`.
# // Mục tiêu:tìm**
# // số phép
# // ít nhất**
# // để làm`num1`bằng`0`.
# // Nếu không thể,
# // trả về`-1`.([leetcode.com][1],[Progiez][2])

# // #
# // Suy luận

# // chính (intuition)

# // Nếu ta thực hiện đúng `k`

# // phép (với các mũ `i1, i2, ..., ik`), thì:

# // ```
# // num1 - ( (num2 + 2^{i1}) + (num2 + 2^{i2}) + ... + (num2 + 2^{ik}) ) = 0
# // ```

# // Suy ra:

# // ```
# // num1 - k * num2 = 2^{i1} + 2^{i2} + ... + 2^{ik} (ghi là target)
# // ```

# // Vậy `target = num1 - k * num2` phải là một số **không âm** và phải có dạng là
# // **tổng của đúng k lũy thừa của 2** (lũy thừa có thể lặp). ([walkccc.me][3],
# // [AlgoMonster][4])

# // Từ điều đó ta có hai điều kiện

# // cần thiết (và cũng đủ trong bối cảnh này):

# // 1. `target >= 0` (vì tổng các 2^i là không âm).
# // 2. Số bit `1` trong biểu diễn nhị phân của `target` (popcount) **phải ≤ k**
# // (vì popcount là số lượng lũy thừa 2 khác nhau tối thiểu để biểu diễn
# // `target`; nếu popcount ≤ k thì ta có thể phân tách/nhân bản một vài `2^0` để
# // đạt đúng k số hạng).
# // 3. `target >= k` vì mỗi lũy thừa 2 có giá trị ≥ 1, tổng k phần tử ≥ k. (điều
# // này đảm bảo có thể có đúng k phần tử).

# // Nếu tồn tại một `k` thỏa 3 điều trên thì đáp án là `k`; nếu không có `k` nào
# // thỏa trong phạm vi hợp

# // lý (ví dụ kiểm tra k từ `0` đến `60`) thì trả về `-1`. ([walkccc.me][3],
# // [AlgoMonster][4])

# // #

# // Thuật toán (ngắn gọn)

# // Duyệt `k` từ `0` tới `60` (vì i ∈ \[0,60], không cần k lớn hơn 60 trong thực
# // tế):

# // * `target = num1 - k * num2`
# // * nếu `target < 0` →

# // bỏ qua (không hợp lệ)
# // * nếu `popcount(target) <= k <= target` → trả `k`
# // Sau khi kiểm tra hết, nếu không tìm được thì trả `-1`. ([walkccc.me][3])

# // # Ví dụ nhanh

# // * `num1 = 10, num2 = 6`

# // * Với `k = 1`: `target = 10 - 1*6 = 4`. `popcount(4) = 1`, và `1 <= 4` → thỏa
# // → trả `1`. (Thực tế chọn `i = 2` vì `2^2 = 4`, 10 - (6+4) = 0.)
# // * `num1 = 1, num2 = 2` → với mọi `k` nhỏ `target` sẽ âm hoặc không thỏa → trả
# // `-1`.

# // # Độ phức tạp

# // Ta thử tối đa \~61 giá trị `k`, mỗi lần tính `target` và `popcount`

# // là O(1) (với số bit cố định), nên độ phức tạp là **O(1)** (thực tế O(60) ≈
# // hằng số). Bộ nhớ O(1). ([walkccc.me][3])

# // ##1.
# // Nhắc lại
# // yêu cầu

# // Sau khi
# // thực hiện đúng`k`
# // phép trừ, ta
# // có công thức:

# // ```num1-k*num2=2^i1+2^i2+...+2^ik```

# // Ký hiệu:

# // ```target=num1-k*num2```

# // Nghĩa là
# // ta cần
# // kiểm tra xem**`target`
# // có thể
# // biểu diễn
# // thành tổng
# // của đúng`k`
# // lũy thừa của 2 không**.

# // ---

# // ##2.
# // Vai trò
# // của nhị
# // phân

# // Mọi
# // số nguyên`target`
# // đều có một**dạng nhị phân**.

# // Ví dụ:

# // *`target=13`→
# // nhị phân`1101₂=8+4+1`.⇒
# // muốn viết
# // thành tổng
# // lũy thừa của 2
# // thì ít
# // nhất phải dùng 3

# // số (8, 4, 1).

# // * `target = 8` → nhị phân `1000₂ = 2^3`.
# // ⇒ chỉ cần 1 số.

# // ---

# // ## 3. Liên hệ với `bitCount`

# // * **`Long.bitCount(target)` đếm số lượng bit `1` trong nhị phân của
# // `target`.**
# // * Chính con số này = **số lượng tối thiểu** các lũy thừa 2 cần để tạo ra
# // `target`.

# // 👉 Vì vậy:

# // * Nếu `bitCount(target) > k` → không thể, vì bạn chỉ có k số hạng mà đã cần
# // nhiều hơn.
# // * Nếu `bitCount(target) ≤ k` → có thể, vì bạn có thể “chia nhỏ” thêm để đạt
# // đúng k.

# // ---

# // ## 4. Điều kiện đầy đủ trong code

# // Trong code có kiểm tra:

# // ```java
# // if (bits <= k && k <= target)
# // ```

# // * `bits <= k`: đảm bảo bạn có thể tạo ra `target` bằng nhiều nhất k số hạng.
# // * `k <= target`: đảm bảo không yêu cầu quá nhiều số hạng, vì mỗi số hạng nhỏ
# // nhất là 1 → tổng của k số ≥ k.

# // ---

# // ## 5. Ví dụ minh họa trực tiếp

# // Giả sử `num1 = 10, num2 = 6`

# // * Thử với `k = 1`:

# // * `target = 10 - 1*6 = 4`.
# // * `bitCount(4) = 1`.
# // * Điều kiện: `1 ≤ 1` và `1 ≤ 4` → **đúng**.
# // * Ta chọn số hạng duy nhất là `2^2 = 4`.

# // Nếu không có `bitCount`, ta không biết `target` cần bao nhiêu lũy thừa tối
# // thiểu để biểu diễn.

# // ---

# // ✅ Tóm lại:

# // * `Long.bitCount(target)` chính là công cụ để kiểm tra **số lượng tối thiểu
# // lũy thừa 2 cần để tạo ra target**.
# // * Nó liên quan trực tiếp đến yêu cầu bài toán, vì ta cần biết có thể dùng
# // **đúng k lũy thừa 2** hay không.

# // ---

# // Bạn có muốn mình **vẽ một bảng nhỏ** (target, nhị phân, bitCount, có tạo được
# // với k hay không) để nhìn rõ mối liên hệ này hơn không?
# // Ok, mình sẽ **giải thích rõ ràng từng bước code này** để bạn nắm chắc 👇

# // ---

# // ### Code bạn có:

# // ```java
# // class Solution {
# // public int makeTheIntegerZero(int num1, int num2) {

# // for (int k = 1; k <= 60; k++) { // thử số phép k từ 1 → 60
# // long target = (long) num1 - (long) k * num2;
# // if (target < 0) continue; // target phải không âm
# // int bits = Long.bitCount(target); // popcount (số bit 1)
# // if (bits <= k && k <= target) {
# // return k;
# // }
# // }
# // return -1;
# // }
# // }
# // ```

# // ---

# // ### 1. Vòng lặp `for (int k = 1; k <= 60; k++)`

# // * `k` là số

# // bước (số phép trừ bạn dùng).
# // * Ta thử tất cả `k` từ **1 đến 60** vì đề bài cho phép chọn số mũ `i` trong
# // `[0,60]`, nên không cần xét nhiều hơn.

# // ---

# // ### 2. `long target = (long) num1 - (long) k * num2;`

# // * Sau `k` phép, ta đã trừ đi `k * num2` từ `num1`.
# // * Số còn lại (`target`) phải được tạo thành từ **tổng k số dạng 2^i**.
# // * Dùng `long` để tránh tràn số khi `num1` và `num2` lớn.

# // ---

# // ### 3. `if (target < 0) continue;`

# // * Nếu `target < 0` thì không thể, bỏ qua `k` này.
# // * Vì tổng các lũy thừa 2 luôn không âm.

# // ---

# // ### 4. `int bits = Long.bitCount(target);`

# // * `Long.bitCount(target)` = số lượng **bit 1** trong nhị phân của `target`.
# // * Đây chính là số lượng **tối thiểu** lũy thừa 2 cần để ghép thành `target`.

# // Ví dụ:

# // * `target = 13` → `1101₂` → có 3 bit 1 → cần ít nhất 3

# // số hạng (8 + 4 + 1).
# // * `target = 8` → `1000₂` → có 1 bit 1 → cần ít nhất 1 số hạng.

# // ---

# // ### 5. `if (bits <= k && k <= target)`

# // * **Điều kiện để hợp lệ:**

# // 1. `bits <= k`:
# // → Nếu cần ít số hạng hơn hoặc bằng k, thì có thể chia nhỏ ra để đủ đúng k.
# // (Ví dụ: 8 = 2^3, nếu cần 3 số thì tách 8 → 4+2+2).
# // 2. `k <= target`:
# // → Mỗi lũy thừa ≥ 1, nên tổng k lũy thừa ≥ k.
# // Nếu k > target thì

# // không thể (ví dụ: target = 3 mà k = 5 thì vô lý).

# // * Nếu cả 2 đúng → trả về `k`

# // ngay (vì đây là số phép nhỏ nhất tìm được).

# // ---

# // ### 6. `return -1;`

# // * Nếu thử hết `k = 1…60` mà không có cái nào hợp → trả về `-1`.

# // ---

# // ### Ví dụ minh họa

# // **num1 = 10, num2 = 6**

# // * Với `k = 1`:
# // `target = 10 - 1*6 = 4`
# // `bits = 1` (100₂)
# // Điều kiện: `1 ≤ 1` và `1 ≤ 4` → đúng → trả về `1`.

# // **num1 = 1, num2 = 2**

# // * Với `k = 1`: `target = -1` → bỏ.
# // * Với mọi `k > 1`: `target` luôn âm.
# // → Không có k hợp lệ → trả về `-1`.

# // ---

# // ✅ **Tóm lại:**
# // Thuật toán duyệt tất cả số bước k, tính phần còn lại (`target`) sau khi trừ k
# // lần `num2`.
# // Rồi kiểm tra xem `target` có thể biểu diễn được bằng **đúng k lũy thừa của
# // 2** không (dùng `bitCount` để kiểm tra).
# // Nếu có thì trả về k nhỏ nhất, nếu không thì trả `-1`.
# // Ok 👍 mình chạy ví dụ **num1 = 5, num2 = 7** theo đúng code Java trên nhé.

# // ---

# // ### Bắt đầu vòng lặp

# // #### k = 1

# // ```
# // target = 5 - 1*7 = -2 (âm) → bỏ qua
# // ```

# // #### k = 2

# // ```
# // target = 5 - 2*7 = -9 (âm) → bỏ qua
# // ```

# // #### k = 3

# // ```
# // target = 5 - 3*7 = -16 (âm) → bỏ qua
# // ```

# // 👉 Cứ tiếp tục như vậy, vì num2 = 7 dương, nên càng tăng k thì target = 5 -
# // k\*7 sẽ càng âm hơn.

# // ---

# // ### Kết quả

# // * Không có k nào cho target ≥ 0.
# // * Do đó **không thể** thỏa mãn điều kiện.

# // 👉 Output = **-1**.

# // ---

# // 📌 Tóm lại: Nếu `num2` lớn và dương, sau khi trừ nhiều lần thì `target` sẽ âm
# // ngay, nên không có cách nào để biểu diễn target thành tổng các lũy thừa của 2
# // → trả về -1.

# // ---

# // Rồi 👍 mình sẽ lấy ví dụ **Input: num1 = 3, num2 = -2** và chạy theo code
# // Java ở trên cho bạn thấy.

# // ---

# // ### Code logic nhắc lại

# // ```java
# // for (int k = 1; k <= 60; k++) {
# // target = num1 - k * num2;
# // if (target < 0) continue;
# // bits = Long.bitCount(target);
# // if (bits <= k && k <= target) return k;
# // }
# // return -1;
# // ```

# // ---

# // ### Bắt đầu chạy:

# // #### Thử k = 1

# // ```
# // target = 3 - 1*(-2) = 3 + 2 = 5
# // binary(5) = 101₂
# // bits = 2
# // ```

# // Điều kiện:

# // * bits = 2 ≤ k = 1 ❌ (sai)
# // → không chọn.

# // ---

# // #### Thử k = 2

# // ```
# // target = 3 - 2*(-2) = 3 + 4 = 7
# // binary(7) = 111₂
# // bits = 3
# // ```

# // Điều kiện:

# // * bits = 3 ≤ k = 2 ❌ (sai).

# // ---

# // #### Thử k = 3

# // ```
# // target = 3 - 3*(-2) = 3 + 6 = 9
# // binary(9) = 1001₂
# // bits = 2
# // ```

# // Điều kiện:

# // * bits = 2 ≤ k = 3 ✅
# // * k = 3 ≤ target = 9 ✅
# // → Thỏa mãn → **return 3**.

# // ---

# // ### Kết quả:

# // 👉 Output = **3**

# // ---

# // ✅ Giải thích trực quan:

# // * Sau 3 bước (k = 3), ta có target = 9.
# // * 9 = 8 + 1 = 2³ + 2⁰ → đúng dạng tổng các lũy thừa của 2.
# // * Và số

# // số hạng (2) ≤ k (3).

# // ---
