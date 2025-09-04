# 3516. Find Closest Person(04/09/2025)

class Solution:
    def findClosestPerson(self, x: int, y: int, z: int) -> int:
        d1 = abs(x - z)
        d2 = abs(y - z)

        if d1 == d2:
            return 0
        elif d1 < d2:
            return 1
        else:
            return 2


### Phân tích bài toán theo ví dụ bạn cung cấp

#### Tóm tắt bài toán

# Bạn có ba người tại các vị trí trên một trục số, được xác định bởi các biến `x`, `y`, và `z`.

# * **Người 1:** ở vị trí `x`
# * **Người 2:** ở vị trí `y`
# * **Người 3:** ở vị trí `z`

# Hai người đầu tiên (`x` và `y`) đang cố gắng di chuyển để gặp người thứ ba (`z`). Họ di chuyển với tốc độ 1 đơn vị mỗi bước.

# Bạn cần tìm xem người nào trong số hai người đầu tiên (`x` hoặc `y`) sẽ đến vị trí của người thứ ba (`z`) **sớm hơn**.

# #### Cách giải quyết

# Để tìm ra người nào đến sớm hơn, bạn cần tính thời gian (số bước) mà mỗi người cần để di chuyển đến vị trí `z`.

# Thời gian di chuyển bằng chính khoảng cách giữa hai điểm. Khoảng cách giữa hai điểm trên một trục số được tính bằng công thức giá trị tuyệt đối: $|a - b|$.

# 1.  **Tính thời gian di chuyển của Người 1:**
#     * Vị trí của Người 1 là `x`.
#     * Vị trí của Người 3 là `z`.
#     * Khoảng cách (và thời gian) là: $|x - z|$

# 2.  **Tính thời gian di chuyển của Người 2:**
#     * Vị trí của Người 2 là `y`.
#     * Vị trí của Người 3 là `z`.
#     * Khoảng cách (và thời gian) là: $|y - z|$

# 3.  **So sánh thời gian:**
#     * Nếu $|x - z| < |y - z|$, Người 1 đến sớm hơn.
#     * Nếu $|y - z| < |x - z|$, Người 2 đến sớm hơn.
#     * Nếu $|x - z| = |y - z|$, cả hai đến cùng lúc.

# #### Áp dụng vào ví dụ

# * **Đầu vào:** `x = 2`, `y = 7`, `z = 4`

# 1.  **Thời gian của Người 1:**
#     * Khoảng cách từ 2 đến 4: $|2 - 4| = |-2| = 2$ bước.

# 2.  **Thời gian của Người 2:**
#     * Khoảng cách từ 7 đến 4: $|7 - 4| = |3| = 3$ bước.

# 3.  **So sánh:**
#     * `2 < 3`
#     * Vì Người 1 chỉ mất 2 bước, trong khi Người 2 mất 3 bước, nên Người 1 đến vị trí `z` sớm hơn.

# **Kết quả:**
# Vì Người 1 đến sớm hơn, đầu ra là **1**.