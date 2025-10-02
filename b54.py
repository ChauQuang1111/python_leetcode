# 3100. Water Bottles II(02/10/2025)

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = numBottles        # tổng số chai đã uống ban đầu
        numEmpty = numBottles   # số vỏ chai ban đầu (vì uống hết rồi)

        # tiếp tục đổi khi số vỏ đủ để đổi ra 1 chai mới
        while numEmpty >= numExchange:
            res += 1                    # uống thêm 1 chai mới
            numEmpty -= numExchange - 1 # đổi ra 1 chai mới:
                                        #   mất numExchange vỏ,
                                        #   nhưng sau khi uống chai mới sẽ có lại 1 vỏ
                                        # => thực chất số vỏ giảm đi (numExchange - 1)
            numExchange += 1            # lần sau cần nhiều vỏ hơn mới đổi được

        return res
# ```

# ---

# ### Ý tưởng thuật toán

# * **Khởi tạo**:

#   * `res = numBottles`: vì ban đầu uống ngay số chai có sẵn.
#   * `numEmpty = numBottles`: sau khi uống hết thì số vỏ bằng số chai ban đầu.

# * **Vòng lặp** `while numEmpty >= numExchange`:

#   * Nếu còn đủ vỏ để đổi, thì:

#     1. Đổi được 1 chai mới → `res += 1`.
#     2. Khi đổi: mất `numExchange` vỏ, nhưng uống xong lại có thêm 1 vỏ.

#        * Vì vậy, số vỏ thực sự giảm đi `numExchange - 1`.
#     3. Sau mỗi lần đổi, yêu cầu `numExchange` tăng thêm 1 (đề bài).

# * **Kết thúc**: khi số vỏ < số vỏ cần thiết để đổi, không thể đổi thêm nữa → trả về `res`.

# ---

# ### Ví dụ minh hoạ

# Giả sử: `numBottles = 4, numExchange = 2`.

# 1. Uống 4 chai ban đầu → `res = 4, numEmpty = 4`.
# 2. Đủ 2 vỏ để đổi:

#    * Đổi lấy 1 chai → `res = 5`.
#    * Vỏ: `numEmpty = 4 - (2 - 1) = 3`.
#    * `numExchange = 3`.
# 3. Tiếp tục: `numEmpty = 3 >= 3`

#    * Đổi lấy 1 chai → `res = 6`.
#    * Vỏ: `numEmpty = 3 - (3 - 1) = 1`.
#    * `numExchange = 4`.
# 4. Dừng vì `numEmpty = 1 < 4`.

# 👉 Kết quả = **6 chai**.

# ---

# Bạn có muốn mình vẽ thêm **bảng trạng thái (res, numEmpty, numExchange)** cho từng vòng lặp để dễ hình dung hơn không?

# // ###1.
# // Bài toán
# // yêu cầu

# // Bạn có:

# // *`numBottles`
# // chai nước

# // ban đầu (uống ngay được hết).
# // * Mỗi lần muốn đổi 1 chai mới thì cần **numExchange** vỏ chai rỗng.
# // * Sau **mỗi lần đổi thành công**, yêu cầu số vỏ để đổi sẽ **tăng thêm 1**
# // (`numExchange++`).
# // * Hỏi tổng cộng bạn có thể uống được bao nhiêu chai?

# // ---

# // ### 2. Ý tưởng

# // * Uống hết `numBottles` ban đầu → tổng số chai uống được = `ans =
# // numBottles`.

# // * Sau đó, ta còn `empty = numBottles` cái vỏ.

# // * Chừng nào số vỏ còn lại `>= numExchange` thì ta có thể đổi thêm 1 chai mới.

# // * Mỗi lần đổi thì:

# // 1. Dùng `numExchange` cái vỏ → `empty -= numExchange`.
# // 2. Đổi được 1 chai mới, uống nó → `ans++`.
# // 3. Uống xong chai đó → thêm 1 vỏ mới → `empty++`.
# // 4. Lần đổi tiếp theo khó hơn, cần thêm 1 vỏ nữa → `numExchange++`.

# // * Khi `empty < numExchange`, dừng lại vì không thể đổi thêm.

# // ---

# // ### 3. Ví dụ minh họa

# // Giả sử: `numBottles = 10`, `numExchange = 3`

# // * Bước 0: Uống 10 chai đầu → `ans = 10`, `empty = 10`.
# // * Bước 1: `empty=10 ≥ 3` → đổi 3 vỏ lấy 1 chai.

# // * `empty = 10-3+1=8`, `ans=11`, `numExchange=4`.
# // * Bước 2: `empty=8 ≥ 4` → đổi 4 vỏ.

# // * `empty=8-4+1=5`, `ans=12`, `numExchange=5`.
# // * Bước 3: `empty=5 ≥ 5` → đổi 5 vỏ.

# // * `empty=5-5+1=1`, `ans=13`, `numExchange=6`.
# // * Bước 4: `empty=1 < 6` → dừng.

# // 👉 Kết quả: `ans=13`.

# // ---

# // ### 4. Độ phức tạp

# // * Mỗi vòng lặp chỉ thực hiện một số phép tính đơn giản.
# // * Trong trường hợp xấu nhất, số lần lặp ≈ số chai uống được → **O(ans)**.
# // * Vì `ans ≤ numBottles + numExchange` nên chạy rất nhanh.

# // ---

# // Bạn có muốn mình vẽ **bảng trạng thái từng vòng lặp** (giá trị của `empty`,
# // `numExchange`, `ans`) để dễ nhìn hơn không?
# // Mình giải thích đề **3100. Water Bottles II** cho bạn nhé — sau đó nếu bạn
# // muốn, mình có thể viết code mẫu và giải thuật từng bước.

# // ---

# // ##

# // Đề bài (Water Bottles II) — Giải thích

# // > Cho hai số nguyên `numBottles` và `numExchange`.
# // > `numBottles` là số chai nước **đầy** bạn có ban đầu.
# // > Bạn có thể thực hiện các thao tác sau:
# // >
# // > 1. Uống bất kỳ số chai nước đầy nào → chai đó trở thành chai **rỗng**.
# // > 2. Đổi `numExchange` chai rỗng để lấy 1 chai nước đầy. Sau khi đổi, bạn
# // **tăng numExchange lên 1**.
# // >
# // > Lưu ý: bạn không thể đổi nhiều “lô” chai rỗng sử dụng cùng một giá trị
# // `numExchange` trong cùng một chuỗi

# // thao tác (tức là sau mỗi lần đổi, `numExchange` thay đổi).
# // >
# // > Hỏi: bạn có thể uống được tối đa bao nhiêu chai nước?

# // ---

# // ### Khác biệt so với

# // Water Bottles (phiên bản 1518)

# // Ở phiên bản 1518 thông thường:

# // * Bạn có `numExchange` cố định: cứ `numExchange` chai rỗng thì đổi 1 chai
# // mới, và cứ làm mãi như thế.
# // * Ở phiên bản **II (3100)**: sau mỗi lần đổi `numExchange` chai rỗng, bạn
# // **tăng `numExchange` lên 1**. Tức là lần sau bạn cần nhiều chai rỗng hơn để
# // đổi tiếp.

# // Ví dụ: nếu `numExchange = 3` ban đầu:

# // * Lần đầu: đổi 3 chai rỗng lấy 1 chai mới, sau đó **numExchange = 4**.
# // * Lần kế: nếu bạn muốn đổi tiếp, bạn phải có 4

# // chai rỗng (không còn là 3).
# // * Sau lần đổi thứ hai, numExchange = 5, và cứ thế tiếp tục.

# // ---

# // ### Ví dụ từ đề

# // Ví dụ 1: `numBottles = 13, numExchange = 6` → Output = 15
# // Ví dụ 2: `numBottles = 10, numExchange = 3` → Output = 13
# // (đã có trong giải thích của tài liệu LeetCode) ([GitHub][1])

# // ---

# // ### Ý tưởng giải

# // * Ban đầu bạn uống hết `numBottles` chai → đó là số tối thiểu bạn uống được.

# // * Gọi `ans = numBottles`.

# // * Bạn có `empty = numBottles` chai rỗng.

# // * Khi nào `empty >= numExchange`, bạn có thể đổi:

# // 1. Dùng `numExchange` chai rỗng → lấy 1 chai đầy.
# // 2. Uống chai mới này → tăng `ans` thêm 1.
# // 3. Khi uống xong, chai mới thành 1 chai rỗng → nên `empty` giảm
# // `numExchange`, nhưng lại tăng 1 do cái mới uống → net là `empty = empty -
# // numExchange + 1`.
# // 4. Sau khi đổi thành công, `numExchange += 1` (điều kiện đổi trong lần sau
# // khó hơn).

# // * Lặp lại cho đến khi `empty < numExchange` → không thể đổi thêm nữa.

# // ---

# // ### Mã giả / Cách viết

# // Ví dụ Python:

# // ```python
# // class Solution:
# // def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
# // ans = numBottles
# // empty = numBottles

# // while empty >= numExchange:
# // # đổi và uống
# // empty = empty - numExchange # dùng một lô chai rỗng
# // numExchange += 1 # tăng yêu cầu đổi cho lần sau
# // ans += 1 # bạn uống chai mới vừa đổi
# // empty += 1 # chai đó khi uống trở thành vỏ

# // return ans
# // ```

# // — hoặc viết gọn hơn:

# // ```python
# // while numBottles >= numExchange:
# // numBottles = numBottles - numExchange + 1
# // numExchange += 1
# // ans += 1
# // ```

# // (Ung dung `numBottles` để đại diện số chai + rỗng còn “sử dụng được”)
# // ([GitHub][1])

# // ---

# // Nếu bạn muốn, mình có thể viết code Java/Python hoàn chỉnh cho 3100 và giải
# // thuật chi tiết từng bước cho một ví dụ cụ thể để bạn hiểu sâu hơn không?

