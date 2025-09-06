# 3495. Minimum Operations to Make Array Elements Zero(06/09/2025)
from typing import List
from bisect import bisect_right

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        wexondrivas = queries  # chỉ là alias cho queries

        # Tạo danh sách các mốc lũy thừa của 4: 1, 4, 16, 64, ...
        pow4 = [1]
        while pow4[-1] <= 10 ** 9:
            pow4.append(pow4[-1] * 4)

        # prefix[i] = tổng số lần chia từ 1 đến pow4[i]-1
        prefix = [0]
        for i in range(len(pow4) - 1):
            # mỗi khoảng [4^i, 4^(i+1)-1] có độ dài 3*4^i
            # và mỗi số trong khoảng này cần (i+1) lần chia
            prefix.append(prefix[-1] + (i + 1) * 3 * pow4[i])

        # Hàm F(n): tính tổng số lần chia từ 1 → n
        def F(n: int) -> int:
            if n <= 0:
                return 0
            # tìm k sao cho 4^k <= n < 4^(k+1)
            k = bisect_right(pow4, n) - 1
            # lấy prefix[k] (tổng đến 4^k - 1)
            # cộng thêm phần dư [4^k, n], mỗi số cần (k+1) lần chia
            return prefix[k] + (k + 1) * (n - pow4[k] + 1)

        ans = 0
        # duyệt từng query
        for l, r in wexondrivas:
            # tổng số lần chia trong đoạn [l, r]
            s = F(r) - F(l - 1)
            # mỗi thao tác xử lý 2 số => kết quả = ceil(s/2)
            ans += (s + 1) // 2
        return ans

# `from bisect import bisect_right` nghĩa là:

# 👉 Ta **import hàm `bisect_right` từ module `bisect`** trong Python.

# ---

# ### `bisect_right` dùng để làm gì?

# * Đây là hàm **tìm vị trí chèn** phần tử vào trong một mảng **đã sắp xếp tăng dần** sao cho vẫn giữ đúng thứ tự.
# * Khác với `bisect_left` ở chỗ:

#   * `bisect_left`: nếu giá trị đã tồn tại, nó sẽ chèn **trước** phần tử đầu tiên bằng giá trị đó.
#   * `bisect_right`: nếu giá trị đã tồn tại, nó sẽ chèn **sau** phần tử cuối cùng bằng giá trị đó.


### Cú pháp:

# ```python
# pos = bisect_right(a, x)
# ```

# * `a`: danh sách đã **sắp xếp tăng dần**.
# * `x`: giá trị cần tìm vị trí chèn.
# * `pos`: vị trí index để chèn `x` vào `a`.



### Ví dụ:

# ```python
# from bisect import bisect_right

# arr = [1, 4, 16, 64]
# print(bisect_right(arr, 16))  # 3
# print(bisect_right(arr, 15))  # 2
# print(bisect_right(arr, 70))  # 4
# ```

# 👉 Giải thích:

# * `bisect_right(arr, 16) = 3` vì `16` nằm ở index 2, hàm trả về vị trí ngay sau nó (index 3).
# * `bisect_right(arr, 15) = 2` vì `15` nhỏ hơn `16` ⇒ vị trí chèn là trước `16`.
# * `bisect_right(arr, 70) = 4` vì `70` lớn hơn tất cả ⇒ chèn ở cuối mảng.

# ---

# ### Trong code của bạn:

# ```python
# k = bisect_right(pow4, n) - 1
# ```

# * `pow4 = [1, 4, 16, 64, ...]`.
# * `bisect_right(pow4, n)` tìm vị trí chèn `n` vào `pow4`.
# * `-1` để lấy đúng **tầng k** mà `n` thuộc về.

# Ví dụ:

# * Nếu `n = 20` → `bisect_right([1, 4, 16, 64], 20) = 3` → `k = 2`.
# * Nghĩa là `20` nằm trong tầng `2` (vì `16 ≤ 20 < 64`).

# ---

# 👉 Tóm lại: `bisect_right` giúp xác định `n` nằm ở **tầng nào của cây 4-ary**.






# Ok, mình sẽ giải thích lại **từng bước rõ ràng, dễ hiểu** từ đoạn code Python mà bạn gửi 👇

# ---

# ## Đề bài (nhắc lại ngắn gọn)

# Bạn có một **cây 4-ary vô hạn** (mỗi node có 4 con).
# Đánh số các cạnh của cây theo BFS (tầng này sang tầng khác, trái qua phải).
# Mỗi query `[l, r]` hỏi: từ cạnh số `l` đến `r`, có bao nhiêu cạnh cần **đảo chiều** để biến cây thành *cây đối xứng*.

# ---

# ## Giải thích code

# ### 1. Tạo mảng `pow4`

# ```python
# pow4 = [1]
# while pow4[-1] <= 10 ** 9:
#     pow4.append(pow4[-1] * 4)
# ```

# 👉 `pow4` chứa các lũy thừa của 4:

# ```
# pow4 = [1, 4, 16, 64, 256, ...]
# ```

# * `pow4[k]` chính là **số node** của tầng `k` trong cây.
# * Vì cây 4-ary: tầng `0` có `1` node (gốc), tầng `1` có `4` node, tầng `2` có `16` node, v.v.

# ---

# ### 2. Mảng `prefix`

# ```python
# prefix = [0]
# for i in range(len(pow4) - 1):
#     prefix.append(prefix[-1] + (i + 1) * 3 * pow4[i])
# ```

# * `prefix[k]` lưu **tổng số thao tác cần thiết** để xử lý **toàn bộ các cạnh từ tầng 0 → tầng k-1**.
# * Ở tầng `i` có `3 * pow4[i]` cạnh (vì mỗi node ở tầng `i` có 4 con ⇒ 4 cạnh, nhưng ta chỉ xét 3 cạnh cần lật để đối xứng).
# * Mỗi tầng được nhân thêm `(i+1)` vì tầng càng sâu, chỉ số cạnh càng lớn.

# Ví dụ:

# * `prefix[0] = 0` (chưa có cạnh nào).
# * `prefix[1] = (1) * 3 * pow4[0] = 3`.
# * `prefix[2] = prefix[1] + (2) * 3 * pow4[1] = 3 + 2*12 = 27`.

# ---

# ### 3. Hàm `F(n)`

# ```python
# def F(n: int) -> int:
#     if n <= 0:
#         return 0
#     k = bisect_right(pow4, n) - 1
#     return prefix[k] + (k + 1) * (n - pow4[k] + 1)
# ```

# 👉 Ý nghĩa: `F(n)` tính **tổng số thao tác cần thiết từ cạnh 1 → cạnh n**.

# * `k = bisect_right(pow4, n) - 1`:
#   tìm xem `n` nằm ở tầng nào của cây.
# * `prefix[k]`: tổng các cạnh từ các tầng trước `k`.
# * `(k+1) * (n - pow4[k] + 1)`: cộng thêm số cạnh **ở tầng k** (chỉ tính đến cạnh số `n`).

# Ví dụ:

# * `F(1)` = số thao tác từ cạnh `1`.
# * `F(20)` = tổng thao tác từ cạnh `1 → 20`.

# ---

# ### 4. Tính kết quả cho từng query

# ```python
# ans = 0
# for l, r in wexondrivas:
#     s = F(r) - F(l - 1)
#     ans += (s + 1) // 2
# ```

# * Với mỗi query `[l, r]`:

#   * `F(r) - F(l-1)` = tổng thao tác cho đoạn `[l, r]`.
#   * `(s+1)//2`: chia đôi vì ta chỉ cần **ít nhất một nửa số cạnh** đảo chiều để thành đối xứng.

# ---

# ## Tóm tắt ngắn gọn

# 1. `pow4`: lưu số node theo từng tầng (1, 4, 16, …).
# 2. `prefix`: cộng dồn số thao tác cần cho các tầng trước.
# 3. `F(n)`: tổng thao tác cần cho các cạnh từ `1 → n`.
# 4. Query `[l, r]` = `F(r) - F(l-1)`, sau đó lấy nửa để tính số cạnh cần đảo.

# ---

# 👉 Hiểu đơn giản:

# * Ta xây công thức tính nhanh `F(n)` thay vì duyệt từng cạnh.
# * Nhờ `pow4` và `prefix`, mỗi query trả lời trong `O(log n)` thay vì `O(n)`.





# // Hay,

# // bạn để
# // ý rất kỹ👍
# // mình giải
# // thích rõ chỗ`4L`
# // này nhé:

# // Trong code:

# // ```java while(x<=query[1]*4L)
# // {
# // ```

# // ---

# // ### 1. Tại sao lại nhân với `4`?

# // Như mình giải thích, ta đang xét các **mốc lũy thừa của 4**:

# // ```
# // 1, 4, 16, 64, ...
# // ```

# // Khi xử lý đoạn `[l, r]`, ta muốn bao phủ hết đoạn này bằng các mốc.

# // * Nếu dừng ở `x <= query[1]`, thì có thể bị thiếu đoạn cuối cùng.
# // * Vì thế, nhân thêm `4` để chắc chắn là **mốc cuối cùng (lớn hơn r) đã được
# // xét**, đảm bảo vòng lặp bao trùm hết `[l, r]`.

# // ---

# // ### 2. Tại sao viết `4L` mà không phải `4`?

# // * `query[1]` là `int`.
# // * Nếu viết `query[1] * 4`, kết quả là `int`, có thể bị **tràn số** khi
# // `query[1]` lớn (vì `int` chỉ tối đa \~2.1 tỉ).
# // * Viết `4L` ép kiểu về `long`, nên `query[1] * 4L` là `long`, an toàn khi so
# // sánh với `x` (vốn là `long`).

# // ---

# // ✅ Tóm lại:

# // ```java
# // while (x <= query[1] * 4L)
# // ```

# // * `*4` để đảm bảo lấy đủ các mốc 4^k bao trùm đến sau r.
# // * `L` để ép kiểu về `long`, tránh tràn số và đồng bộ kiểu dữ liệu với biến
# // `x`.

# // À mình
# // giải thích
# // kỹ hơn
# // chỗ này nhé👌

# // Trong code:

# // ```java
# // long x = 1; // mốc ban đầu
# // ```

# // Sau đó
# // trong vòng while
# // ta có:

# // ```
# // java x*=4;```

# // →
# // Nghĩa là
# // các giá
# // trị của`x`
# // sẽ lần
# // lượt là:

# // ```1→4→16→64→256→...```

# // Đây chính là**các lũy
# // thừa của 4**:

# // $$
# // x = 4^0,4^1,4^2,4^3,...$$

# // ---

# // ###
# // Ý nghĩa
# // của mốc`x`

# // Nó dùng
# // để chia
# // dải số nguyên`[l,r]`
# // thành từng**khoảng**
# // mà trong
# // mỗi khoảng,**số lần chia 4
# // để về 0
# // là giống nhau**.

# // Ví dụ:

# // *
# // Các số trong**\[1,3]**
# // chỉ cần**1
# // lần chia**(`n/4=0`).*
# // Các số trong**\[4,15]**cần**2
# // lần chia**(`n/4→n/16→0`).*
# // Các số trong**\[16,63]**cần**3
# // lần chia**.*
# // Các số trong**\[64,255]**cần**4
# // lần chia**.

# // 📌
# // Nhận xét:
# // Các khoảng
# // này đúng
# // bằng các đoạn\[1,4),\[4,16),\[16,64),\[64,256),…→
# // chính là
# // các mốc
# // lũy thừa của 4.

# // Vậy nên`x`
# // chạy qua
# // các mốc**1,4,16,64,...**
# // để giúp
# // ta xác
# // định ranh
# // giới giữa
# // những đoạn
# // có cùng
# // số bước chia.

# // Ok,
# // mình giải
# // thích đề bài**3495.
# // Minimum Operations
# // to Make
# // Array Elements

# // Zero (Hard)** cho bạn thật dễ hiểu nhé 👍

# // ---

# // ### Đề bài nói gì?

# // Bạn được cho một mảng `queries`, mỗi phần tử `queries[i] = [l, r]`.
# // Với mỗi truy vấn `[l, r]`, ta tạo ra một mảng `nums = [l, l+1, ..., r]`.

# // Bây giờ ta cần thực hiện **các phép biến đổi** trên mảng `nums` cho đến khi
# // **tất cả phần tử = 0**.

# // ---

# // ### Phép biến đổi là gì?

# // Trong **một lần thao tác**, ta chọn **2 số bất kỳ**

# // trong mảng (giả sử là `a` và `b`),
# // rồi thay cả 2 số đó bằng:

# // * `floor(a / 4)`
# // * `floor(b / 4)`

# // (Nghĩa là chia cho 4 và làm tròn xuống).

# // Ta lặp lại thao tác này cho đến khi toàn bộ mảng trở thành `0`.

# // ---

# // ### Nhiệm vụ của bạn:

# // * Với **mỗi query `[l, r]`**, tính số thao tác tối thiểu cần thực hiện để
# // biến toàn bộ mảng `[l, ..., r]` thành 0.
# // * Sau đó, cộng kết quả của tất cả các query lại và trả về.

# // ---

# // ### Ví dụ

# // Giả sử:

# // ```
# // queries = [[1,2], [2,4]]
# // ```

# // #### Query 1: \[1, 2]

# // Mảng ban đầu: `[1, 2]`

# // * 1 chia 4 → 0
# // * 2 chia 4 → 0
# // → Sau **1 lần thao tác** cả mảng thành `[0, 0]`.

# // 👉 Kết quả query 1 = 1

# // ---

# // #### Query 2: \[2, 3, 4]

# // Mảng ban đầu: `[2, 3, 4]`

# // * Với số 2: 2 → 0 (chỉ 1 lần chia)
# // * Với số 3: 3 → 0 (1 lần chia)
# // * Với số 4: 4 → 1 → 0 (cần 2 lần chia)

# // Tổng cộng có **4 “lần chia” riêng lẻ**.
# // Vì mỗi thao tác xử lý **2 số một lúc**, nên số thao tác tối thiểu là:

# // ```
# // ceil(4 / 2) = 2
# // ```

# // 👉 Kết quả query 2 = 2

# // ---

# // ### Tổng kết

# // ```
# // queries = [[1,2], [2,4]]
# // query 1 → 1 thao tác
# // query 2 → 2 thao tác
# // Kết quả cuối cùng = 1 + 2 = 3
# // ```

# // ---

# // 👉 Như vậy, đề bài yêu cầu ta:

# // * Với từng `[l, r]`, đếm số lần “chia cho 4 đến khi về 0” cho tất cả các số
# // trong khoảng.
# // * Sau đó, vì **mỗi thao tác xử lý được 2 số cùng lúc**, nên ta lấy `(tổng số
# // lần chia + 1) // 2`.
# // * Cuối cùng cộng kết quả của tất cả các query lại.

# // ---

# // Bạn có muốn mình vẽ **sơ đồ trực quan** cho ví

# // dụ này (kiểu cây chia số → 0) để dễ hình dung hơn không?
# // À 👌 đúng rồi, để mình chỉnh lại cho bạn.

# // Bạn đưa **`queries = [[1,2], [2,4]]`**.
# // Nghĩa là:

# // * Query 1 = `[1,2]` → mảng = `[1, 2]`
# // * Query 2 = `[2,4]` → mảng = `[2, 3, 4]`

# // 👉 Số **3** xuất hiện là vì đề bài định nghĩa: với query `[l, r]` thì ta lấy
# // **tất cả các số nguyên từ l đến

# // r (bao gồm cả l và r)**.

# // Ví dụ:

# // * `[1,2]` → `[1,2]`
# // * `[2,4]` → `[2,3,4]`

# // Nên số 3 là do khoảng `[2,4]` chứa luôn nó, chứ không phải mình tự thêm.

# // ---

# // Ok 👍 mình giải thích rõ ràng và chậm rãi đoạn **query 1 = \[1,2]** cho bạn
# // nhé.

# // ---

# // ### Query 1: `[1, 2]`

# // Từ query này, ta tạo mảng:

# // ```
# // nums = [1, 2]
# // ```

# // ---

# // ### Quy tắc thao tác

# // * Mỗi thao tác: chọn 2 số `a, b` trong mảng, thay chúng bằng `floor(a/4)` và
# // `floor(b/4)`.
# // * Mục tiêu: đưa toàn bộ mảng về `[0,0]`.

# // ---

# // ### Thực hiện

# // Mảng hiện tại: `[1, 2]`

# // 👉 Ta chọn luôn cả 2 số (vì chỉ có 2 phần tử thôi):

# // * Với số `1`:
# // `floor(1 / 4) = 0`

# // * Với số `2`:
# // `floor(2 / 4) = 0`

# // Sau 1 thao tác, mảng biến thành:

# // ```
# // [0, 0]
# // ```

# // ---

# // ### Kết luận

# // * Chỉ cần **1 lần thao tác** là toàn bộ mảng thành 0.
# // 👉 Kết quả cho query `[1,2]` là **1**.

# // ---

# // Bạn có muốn mình giải thích thêm **tại sao không thể ít hơn 1 thao tác**
# // không (tức là bắt buộc phải làm ít nhất 1 lần)?
# // Rồi 👍 mình sẽ diễn giải lại đoạn này thật chặt chẽ để bạn dễ hình dung.

# // ---

# // ### Query 2: `[2, 4]`

# // → Mảng tạo ra là:

# // ```
# // nums = [2, 3, 4]
# // ```

# // ---

# // ## 🔹 Bước 1: Đếm số lần **chia cho 4** để mỗi số về 0

# // * **Số 2**
# // 2 ÷ 4 = 0 → chỉ cần **1 lần chia**

# // * **Số 3**
# // 3 ÷ 4 = 0 → cũng chỉ cần **1 lần chia**

# // * **Số 4**
# // 4 ÷ 4 = 1
# // 1 ÷ 4 = 0
# // → cần **2 lần chia**

# // 👉 Tổng cộng: `1 + 1 + 2 = 4 lần chia riêng lẻ`

# // ---

# // ## 🔹 Bước 2: Liên hệ với “một thao tác” của đề bài

# // * Đề bài không cho ta **chia từng số riêng lẻ**, mà bắt buộc phải chọn **2 số
# // một lúc** để xử lý.
# // * Một thao tác tương đương với **2 lần chia** (vì xử lý 2 số).

# // Vậy, muốn thực hiện đủ **4 lần chia riêng lẻ** cho `[2,3,4]`, ta cần:

# // ```
# // số thao tác tối thiểu = ceil(4 / 2) = 2
# // ```

# // ---

# // ## ✅ Kết quả cho Query `[2,4]` = 2

# // ---

# // 📌 Cách hiểu:

# // * **Bước 1**: Đếm xem mỗi số phải chia bao nhiêu lần mới về 0.
# // * **Bước 2**: Vì mỗi thao tác xử lý được 2 số, nên số thao tác = tổng số lần
# // chia riêng lẻ / 2 (làm tròn lên).

# // ---

# // Bạn có muốn mình **mô phỏng cụ thể 2 thao tác** cho `[2,3,4]` (chọn số nào ở
# // thao tác 1, thao tác 2) để thấy rõ hơn không?
