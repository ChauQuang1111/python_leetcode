# 3021. Alice and Bob Playing Flower Game(29/08/2025)

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # Mục tiêu là tìm số cách để tổng số hoa là số lẻ.
        # Tổng của hai số là số lẻ khi một số là lẻ và số kia là chẵn.
        
        # --- Tính toán số lượng số chẵn và lẻ cho Alice ---
        # Alice có thể chọn từ 1 đến n bông hoa.

        # odd_n: Số lượng số lẻ trong khoảng từ 1 đến n.
        # Ví dụ: nếu n=5, số lẻ là 1, 3, 5. odd_n = (5 + 1) // 2 = 3.
        # Nếu n=4, số lẻ là 1, 3. odd_n = (4 + 1) // 2 = 2.
        odd_n = (n + 1) // 2
        
        # even_n: Số lượng số chẵn trong khoảng từ 1 đến n.
        # Ví dụ: nếu n=5, số chẵn là 2, 4. even_n = 5 // 2 = 2.
        # Nếu n=4, số chẵn là 2, 4. even_n = 4 // 2 = 2.
        even_n = n // 2
        
        # --- Tính toán số lượng số chẵn và lẻ cho Bob ---
        # Bob có thể chọn từ 1 đến m bông hoa.

        # odd_m: Số lượng số lẻ trong khoảng từ 1 đến m.
        odd_m = (m + 1) // 2
        
        # even_m: Số lượng số chẵn trong khoảng từ 1 đến m.
        even_m = m // 2
        
        # --- Tính tổng số cách hợp lệ ---
        
        # ways_odd_even: Số cách khi Alice chọn số lẻ VÀ Bob chọn số chẵn.
        # Sử dụng quy tắc nhân: số cách của Alice nhân với số cách của Bob.
        ways_odd_even = odd_n * even_m
        
        # ways_even_odd: Số cách khi Alice chọn số chẵn VÀ Bob chọn số lẻ.
        # Tương tự, sử dụng quy tắc nhân.
        ways_even_odd = even_n * odd_m
        
        # Tổng số cách hợp lệ là tổng của hai trường hợp riêng biệt trên.
        return ways_odd_even + ways_even_odd









# Đoạn code này giải quyết bài toán "Alice and Bob Playing Flower Game" bằng cách sử dụng một phương pháp toán học trực tiếp.

# ### Giải thích thuật toán

# Mục tiêu của bài toán là tìm số cặp số `(x, y)` sao cho `x + y` là một số lẻ. Dựa trên các quy tắc toán học, tổng của hai số chỉ là số lẻ khi một số là lẻ và số còn lại là chẵn.

# Thuật toán này chia bài toán thành hai trường hợp chính, tính số cách cho mỗi trường hợp, và sau đó cộng chúng lại để có kết quả cuối cùng.

# 1.  **Trường hợp 1**: Alice chọn số hoa lẻ, Bob chọn số hoa chẵn.
#     * Thuật toán tính số lượng số lẻ mà Alice có thể chọn từ `1` đến `n`. Công thức **`(n + 1) // 2`** sẽ cho kết quả chính xác. Ví dụ:
#         * Nếu `n = 5`, các số lẻ là `1, 3, 5` (3 số).
#         * Nếu `n = 4`, các số lẻ là `1, 3` (2 số).
#     * Tương tự, nó tính số lượng số chẵn mà Bob có thể chọn từ `1` đến `m` bằng công thức **`m // 2`**.
#     * Số cách cho trường hợp này là tích của hai số trên: `odd_n * even_m`.

# 2.  **Trường hợp 2**: Alice chọn số hoa chẵn, Bob chọn số hoa lẻ.
#     * Thuật toán tính số lượng số chẵn mà Alice có thể chọn từ `1` đến `n` bằng công thức **`n // 2`**.
#     * Số lượng số lẻ mà Bob có thể chọn từ `1` đến `m` là **`(m + 1) // 2`**.
#     * Số cách cho trường hợp này là tích của hai số trên: `even_n * odd_m`.

# Cuối cùng, thuật toán trả về tổng số cách của cả hai trường hợp. Do hai trường hợp này không chồng lấn lên nhau, việc cộng chúng lại sẽ cho ra tổng số cách hợp lệ duy nhất.


# ### Chú thích từng dòng mã

# * `odd_n = (n + 1) // 2`: Tính số lượng số lẻ mà Alice có thể chọn từ `1` đến `n`.
# * `even_n = n // 2`: Tính số lượng số chẵn mà Alice có thể chọn từ `1` đến `n`.
# * `odd_m = (m + 1) // 2`: Tính số lượng số lẻ mà Bob có thể chọn từ `1` đến `m`.
# * `even_m = m // 2`: Tính số lượng số chẵn mà Bob có thể chọn từ `1` đến `m`.
# * `ways_odd_even = odd_n * even_m`: Tổng số cách khi Alice chọn lẻ và Bob chọn chẵn.
# * `ways_even_odd = even_n * odd_m`: Tổng số cách khi Alice chọn chẵn và Bob chọn lẻ.
# * `return ways_odd_even + ways_even_odd`: Trả về tổng số cách hợp lệ của cả hai trường hợp.





