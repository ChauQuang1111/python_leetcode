# 1304. Find N Unique Integers Sum up to Zero(07/09/2025)
from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        
        # Thêm các cặp số đối nhau
        # Vòng lặp này sẽ chạy từ 1 cho đến n // 2 (lấy phần nguyên)
        # Ví dụ: nếu n = 5, n // 2 = 2. Vòng lặp sẽ chạy với i = 1, 2.
        # Tạo các cặp (1, -1) và (2, -2).
        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-i)
            
        # Nếu n là số lẻ, thêm 0 vào mảng
        # Ví dụ: n = 5, n % 2 = 1. Thêm 0 vào.
        # Kết quả: [1, -1, 2, -2, 0]
        if n % 2 == 1:
            result.append(0)
            
        return result

# Đây là một câu hỏi rất hay. Dòng code `if n % 2 == 1: result.append(0)` là để xử lý trường hợp đặc biệt khi `n` là một số lẻ.

# Hãy xem lại mục tiêu của chúng ta: **tạo `n` số nguyên duy nhất có tổng bằng 0.**

# ### Tại sao cần thêm số 0?

# Thuật toán chính của bạn là tạo ra các cặp số đối nhau (ví dụ: `[1, -1]`, `[2, -2]`). Tổng của mỗi cặp này luôn bằng 0.

# * **Khi `n` là số chẵn**:
#     * Ví dụ: `n = 4`.
#     * Bạn cần 4 số.
#     * Vòng lặp `for` sẽ tạo ra `4 / 2 = 2` cặp số đối nhau: `[1, -1]` và `[2, -2]`.
#     * Kết quả là `[1, -1, 2, -2]`. Tổng của chúng là `0`, và có đủ 4 số. Mọi thứ đều hoàn hảo, không cần làm gì thêm.

# * **Khi `n` là số lẻ**:
#     * Ví dụ: `n = 5`.
#     * Bạn cần 5 số.
#     * Vòng lặp `for` sẽ tạo ra `5 // 2 = 2` cặp số đối nhau: `[1, -1]` và `[2, -2]`.
#     * Lúc này, bạn mới có 4 số. Tổng của chúng là `0`, nhưng bạn **thiếu một số**.
#     * Số bạn cần thêm vào phải là một số duy nhất và không làm thay đổi tổng. **Số 0** là lựa chọn hoàn hảo.
#     * Sau khi thêm `0`, mảng trở thành `[1, -1, 2, -2, 0]`. Tổng vẫn bằng `0`, và bây giờ bạn đã có đủ 5 số duy nhất.

# Vì vậy, dòng code `if n % 2 == 1:` là điều kiện để kiểm tra nếu `n` là số lẻ (phép chia cho 2 có dư là 1). Nếu đúng, nó sẽ thêm số 0 vào mảng để hoàn thành nhiệm vụ.
# Đây là một câu hỏi rất hay. Dòng code `for i in range(1, n // 2 + 1):` có thể hơi khó hiểu nếu bạn chưa quen với cách hoạt động của `range()` và phép chia lấy phần nguyên `//`.

# Hãy cùng đi qua một ví dụ cụ thể để bạn thấy nó hoạt động như thế nào.

# ---

# ### Phân tích `range(1, n // 2 + 1)`

# Dòng code này dùng để tạo ra một chuỗi số, bắt đầu từ 1. Số cuối cùng của chuỗi được xác định bởi `n`.

# * `//`: Phép chia lấy phần nguyên. Ví dụ: `7 // 2` sẽ bằng `3`.
# * `range(start, stop)`: Hàm này tạo ra một chuỗi số bắt đầu từ `start` và kết thúc tại `stop - 1`.

# ---

# ### Ví dụ 1: `n = 5` (số lẻ)

# 1.  Đầu tiên, Python tính giá trị của `n // 2`:
#     `5 // 2` bằng **`2`**.
# 2.  Tiếp theo, biểu thức trở thành `range(1, 2 + 1)`, tức là `range(1, 3)`.
# 3.  Hàm `range(1, 3)` sẽ tạo ra chuỗi các số: **`1, 2`**.
# 4.  Vòng lặp `for` sẽ chạy hai lần, với `i` lần lượt là `1` và `2`.

# * Khi `i = 1`, code sẽ thêm `1` và `-1` vào mảng.
# * Khi `i = 2`, code sẽ thêm `2` và `-2` vào mảng.

# Mảng tạm thời của bạn lúc này là `[1, -1, 2, -2]`. Sau đó, chương trình sẽ thêm số 0 vào vì `n` là số lẻ, kết quả cuối cùng là `[1, -1, 2, -2, 0]`.

# ### Ví dụ 2: `n = 4` (số chẵn)

# 1.  Python tính giá trị của `n // 2`:
#     `4 // 2` bằng **`2`**.
# 2.  Biểu thức trở thành `range(1, 2 + 1)`, tức là `range(1, 3)`.
# 3.  Hàm `range(1, 3)` sẽ tạo ra chuỗi các số: **`1, 2`**.
# 4.  Vòng lặp `for` sẽ chạy hai lần, với `i` lần lượt là `1` và `2`.

# * Khi `i = 1`, code sẽ thêm `1` và `-1` vào mảng.
# * Khi `i = 2`, code sẽ thêm `2` và `-2` vào mảng.

# Mảng kết quả là `[1, -1, 2, -2]`. Vì `n` là số chẵn, không cần thêm số 0.

# ### Tóm lại

# Dòng code `for i in range(1, n // 2 + 1):` là một cách thông minh để tạo ra chính xác `n // 2` cặp số đối nhau, đảm bảo tổng của chúng bằng 0. Số cặp này sẽ đủ cho trường hợp `n` chẵn và thiếu một phần tử cho trường hợp `n` lẻ, giúp bạn dễ dàng xử lý bằng một câu lệnh `if` riêng biệt.
# Bạn muốn tôi giải thích ý nghĩa của hai dòng code sau trong thuật toán Python để tìm `n` số nguyên duy nhất có tổng bằng 0:

# 1.  `for i in range(1, n // 2 + 1):`
# 2.  `if n % 2 == 1:`

# ### Giải thích chi tiết

# #### 1. `for i in range(1, n // 2 + 1):`

# * **Mục đích**: Vòng lặp này được sử dụng để tạo ra các cặp số đối nhau (ví dụ: `1` và `-1`, `2` và `-2`,...).
# * **`n // 2`**: Phép toán này là phép chia lấy phần nguyên.
#     * Ví dụ:
#         * Nếu `n = 4` (số chẵn), `4 // 2 = 2`.
#         * Nếu `n = 5` (số lẻ), `5 // 2 = 2`.
# * **`range(1, ... + 1)`**: Hàm `range` trong Python tạo ra một chuỗi số.
#     * `range(start, stop)` tạo ra chuỗi số từ `start` đến `stop-1`.
#     * Vì vậy, `range(1, n // 2 + 1)` sẽ tạo ra một chuỗi các số từ `1` đến `n // 2`.
# * **Lý do**:
#     * Mỗi lần lặp, biến `i` sẽ lấy một giá trị từ `1` đến `n // 2`.
#     * Bên trong vòng lặp, chúng ta thêm `i` và `-i` vào mảng kết quả.
#     * Do đó, chúng ta tạo ra `n // 2` cặp số đối nhau. Tổng của mỗi cặp là `0`, và tổng của tất cả các cặp cũng là `0`.

# #### 2. `if n % 2 == 1:`

# * **Mục đích**: Dòng này kiểm tra xem `n` có phải là một số lẻ hay không.
# * **`n % 2`**: Phép toán này là phép chia lấy dư.
#     * Nếu `n` là số chẵn, `n % 2` sẽ bằng `0`.
#     * Nếu `n` là số lẻ, `n % 2` sẽ bằng `1`.
# * **Lý do**:
#     * Khi `n` là số chẵn, `n // 2` cặp số đối nhau đã đủ để tạo ra `n` phần tử. Tổng của chúng là 0.
#     * Khi `n` là số lẻ, `n // 2` cặp số đối nhau chỉ tạo ra `n-1` phần tử. Chúng ta còn thiếu một phần tử.
#     * Để tổng của `n` số vẫn bằng `0`, phần tử còn lại phải là `0`.
#     * Do đó, câu lệnh `if` này được sử dụng để xử lý trường hợp `n` lẻ bằng cách thêm số `0` vào mảng kết quả.

# ### Tóm tắt

# * Dòng **`for`** để xây dựng các cặp số đối nhau, đảm bảo phần lớn tổng bằng 0.
# * Dòng **`if`** để xử lý trường hợp đặc biệt khi `n` là số lẻ, bằng cách thêm số 0 để hoàn thành mảng và giữ tổng bằng 0.














### Giải thích đề bài: Find N Unique Integers Sum up to Zero

# Đề bài **1304. Find N Unique Integers Sum up to Zero** yêu cầu bạn tạo một mảng chứa **`n`** số nguyên duy nhất có tổng bằng 0.

# ---

# ### Phân tích Yêu cầu

# 1.  **Số lượng phần tử**: Bạn cần tạo một mảng có đúng `n` phần tử. `n` là một số nguyên dương.
# 2.  **Tính duy nhất (Unique)**: Tất cả các số trong mảng phải là duy nhất. Không được có hai số giống nhau.
# 3.  **Tổng bằng 0**: Tổng của tất cả các phần tử trong mảng phải bằng 0.

# ### Ví dụ để hiểu rõ hơn

# * Nếu `n = 1`: Bạn chỉ cần một số. Số `0` là một lựa chọn hoàn hảo vì nó duy nhất và tổng của nó là `0`.
# * Nếu `n = 2`: Bạn cần hai số duy nhất có tổng bằng 0. Cặp số đối nhau là một giải pháp. Ví dụ: `[1, -1]`. Tổng của chúng là `1 + (-1) = 0`.
# * Nếu `n = 3`: Bạn cần ba số duy nhất có tổng bằng 0. Bạn có thể sử dụng cặp đối nhau và số 0. Ví dụ: `[1, -1, 0]`. Tổng của chúng là `1 + (-1) + 0 = 0`.
# * Nếu `n = 4`: Bạn cần bốn số. Bạn có thể sử dụng hai cặp số đối nhau. Ví dụ: `[1, -1, 2, -2]`. Tổng của chúng là `1 + (-1) + 2 + (-2) = 0`.

# ### Thuật toán chung

# Dựa trên các ví dụ trên, một phương pháp đơn giản và hiệu quả để giải quyết bài toán này là sử dụng các cặp số đối nhau.

# 1.  **Trường hợp `n` lẻ**:
#     * Sử dụng số `0` làm một phần tử.
#     * Phần còn lại là `n-1` phần tử, là một số chẵn.
#     * Bạn có thể tạo `(n-1)/2` cặp số đối nhau. Ví dụ: `[1, -1]`, `[2, -2]`, v.v.

# 2.  **Trường hợp `n` chẵn**:
#     * Bạn không cần sử dụng số 0.
#     * Bạn có thể tạo `n/2` cặp số đối nhau. Ví dụ: `[1, -1]`, `[2, -2]`, ..., `[n/2, -n/2]`.

# Cách tiếp cận này đảm bảo rằng tổng của tất cả các số luôn bằng 0 và các số luôn là duy nhất.