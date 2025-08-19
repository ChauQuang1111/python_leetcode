# // 2348. Number of Zero-Filled Subarrays (19/08/2025)
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        # 1 = 1
        # 2 = 3
        # 3 = 6
        # 4 = 10

        # n ( n+1) / 2

        length_of_zero = 0
        total = 0

        for num in nums:

            if(num == 0):
                length_of_zero += 1
            else:
                if(length_of_zero != 0):
                    total += (length_of_zero * (length_of_zero + 1)) // 2
                    length_of_zero = 0
        
        if(length_of_zero != 0):
            total += (length_of_zero * (length_of_zero + 1)) // 2
        
        return total

        # Dựa trên đoạn mã Python bạn cung cấp, đây là giải thích thuật toán để đếm số dãy con chỉ chứa số 0.

# ---

# ### Tổng quan thuật toán

# Thuật toán này hoạt động bằng cách xác định các chuỗi số 0 liên tiếp, sau đó áp dụng một công thức toán học để tính tổng số dãy con có thể tạo ra từ mỗi chuỗi đó. Nó duyệt qua mảng một lần, tính toán tổng cuối cùng và không cần lưu trữ bất kỳ dãy con nào.

# ### Phân tích chi tiết

# Thuật toán sử dụng hai biến:
# * `length_of_zero`: Theo dõi độ dài của chuỗi số 0 liên tiếp hiện tại.
# * `total`: Tổng số dãy con toàn số 0 được tìm thấy.

# Các bước của thuật toán:

# 1.  **Duyệt mảng**: Thuật toán đi qua từng phần tử (`num`) trong mảng `nums`.

# 2.  **Đếm độ dài chuỗi số 0**:
#     * Nếu `num` là `0`, biến `length_of_zero` sẽ được tăng lên 1. Điều này giúp theo dõi độ dài của chuỗi số 0 liên tiếp.
#     * Nếu `num` khác `0`, điều này có nghĩa là chuỗi số 0 liên tiếp vừa kết thúc.

# 3.  **Tính toán và cộng dồn**:
    * Khi chuỗi số 0 kết thúc (do gặp một số khác 0), thuật toán sẽ tính toán số dãy con từ chuỗi đó. Số dãy con từ một chuỗi có độ dài `n` là tổng của các số nguyên từ 1 đến `n`, công thức là `n * (n + 1) / 2`.
    * Công thức này chính là lý do bạn thấy các dòng ghi chú như `# 1 = 1`, `# 2 = 3`, `# 3 = 6`, ... trong đoạn mã.
    * Giá trị này được cộng vào biến `total`. Sau đó, `length_of_zero` được **đặt lại về 0** để bắt đầu đếm chuỗi số 0 mới.

# 4.  **Xử lý trường hợp cuối cùng**:
#     * Vòng lặp `for` sẽ kết thúc, nhưng có khả năng mảng kết thúc bằng một hoặc nhiều số 0.
#     * Đoạn mã `if(length_of_zero != 0)` ở cuối là để xử lý trường hợp này. Nó đảm bảo rằng nếu có một chuỗi số 0 ở cuối mảng, số dãy con từ chuỗi đó vẫn được tính toán và cộng vào `total`.

# ### Ví dụ minh họa

# Hãy xem xét mảng `[1, 0, 0, 2, 0, 0, 0]`:

# * **`num` = 1**: `num` khác 0. `length_of_zero` vẫn là 0.
# * **`num` = 0**: `length_of_zero` = 1.
# * **`num` = 0**: `length_of_zero` = 2.
# * **`num` = 2**: `num` khác 0. Chuỗi số 0 liên tiếp đầu tiên đã kết thúc.
#     * `length_of_zero` hiện tại là 2.
#     * Tính tổng: `(2 * (2 + 1)) / 2 = 3`.
#     * `total` = 3.
#     * `length_of_zero` được reset về 0.
# # * **`num` = 0**: `length_of_zero` = 1.
# * **`num` = 0**: `length_of_zero` = 2.
# * **`num` = 0**: `length_of_zero` = 3.
# * **Vòng lặp kết thúc**: `length_of_zero` = 3.
#     * Kiểm tra `if(length_of_zero != 0)`. Điều kiện đúng.
#     * Tính tổng: `(3 * (3 + 1)) / 2 = 6`.
#     * `total` = `3` + `6` = `9`.

# Cuối cùng, thuật toán trả về `9`, là tổng số dãy con có toàn số 0.

# ### Ưu điểm của thuật toán

# * **Hiệu quả về thời gian**: Chỉ duyệt qua mảng một lần, do đó độ phức tạp thời gian là **O(n)**.
# * **Hiệu quả về không gian**: Chỉ sử dụng một vài biến đơn giản, độ phức tạp không gian là **O(1)**.
# * **Dễ hiểu**: Logic rất rõ ràng, tách biệt quá trình đếm độ dài chuỗi và tính tổng cuối cùng.



        