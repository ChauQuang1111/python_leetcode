# Minimum Cost of Buying Candies With Discount (01/06/2026)

# Đề bài

# Một cửa hàng bán kẹo có chương trình khuyến mãi:


# Khi bạn mua 2 viên kẹo, bạn sẽ được 1 viên kẹo miễn phí.

# Điều kiện:

# Viên kẹo miễn phí phải có giá nhỏ hơn hoặc bằng giá của viên kẹo rẻ nhất trong 2 viên bạn mua.

# Bạn có thể mua kẹo theo bất kỳ thứ tự nào.

# Mảng cost[i] cho biết giá của viên kẹo thứ i.

# Yêu cầu:

# Tính số tiền ít nhất cần trả để mua tất cả các viên kẹo.

# Ví dụ 1

# cost = [1,2,3]

# Ta có thể:


# Mua kẹo giá 3 và 2

# Nhận miễn phí kẹo giá 1

# Số tiền phải trả:

# 3 + 2 = 5

# Kết quả:

# 5

# Ví dụ 2

# cost = [6,5,7,9,2,2]

# Sắp xếp giảm dần:

# [9,7,6,5,2,2]

# Nhóm 3 viên một:

# 9,7,6  -> miễn phí 6

# 5,2,2  -> miễn phí 2

# Tiền phải trả:

# 9 + 7 + 5 + 2 = 23

# Kết quả:

# 23

# Ý tưởng

# Để được giảm giá nhiều nhất:

# Ta muốn viên được miễn phí có giá càng lớn càng tốt.

# Vì vậy nên sắp xếp mảng theo thứ tự giảm dần.

# Ví dụ:

# [9,7,6,5,4,3]

# Ghép:

# 9,7,6  -> miễn phí 6

# 5,4,3  -> miễn phí 3

# Ta chỉ cần cộng:

# 9 + 7 + 5 + 4 = 25

# Bỏ qua các phần tử ở vị trí:

# 2, 5, 8, ...

# (tức là mỗi phần tử thứ 3 sau khi sắp xếp giảm dần).

# Thuật toán

# Sắp xếp cost giảm dần.

# Duyệt mảng:

# Cứ 3 viên kẹo thì:

# Trả tiền 2 viên đầu.

# Viên thứ 3 miễn phí.

# Trả về tổng tiền phải trả.

# Ví dụ trực quan

# cost = [1,3,2,4,5]

# Sắp xếp giảm dần:

# [5,4,3,2,1]

# Nhóm:

# 5,4,3 -> miễn phí 3

# 2,1   -> trả cả 2

# Tiền phải trả:

# 5 + 4 + 2 + 1 = 12

# Đáp án:

# 12

# Mấu chốt của bài là: sắp xếp giảm dần rồi bỏ qua mỗi phần tử thứ 3, vì đó là viên kẹo được miễn phí.

# Đây là lời giải của bạn với chú thích chi tiết từng bước:


from typing import List
class Solution:

    def minimumCost(self, cost: List[int]) -> int:



        # Sắp xếp giá kẹo theo thứ tự tăng dần

        cost.sort()



        # Biến lưu tổng số tiền phải trả

        total = 0



        # Bắt đầu từ viên kẹo đắt nhất

        i = len(cost) - 1



        # Duyệt từ phải sang trái

        while i >= 0:



            # Trả tiền cho viên kẹo đắt nhất trong nhóm

            total += cost[i]



            # Nếu còn viên thứ hai trong nhóm

            if i - 1 >= 0:

                # Trả tiền cho viên này

                total += cost[i - 1]



            # Bỏ qua viên thứ ba (được miễn phí)

            i -= 3



        return total

# Ý tưởng thuật toán

# Sau khi sắp xếp tăng dần:



# cost = [1, 2, 3, 4, 5, 6]

# Ta duyệt từ cuối mảng:



# 6, 5, 4

# ↑  ↑  miễn phí



# 3, 2, 1

# ↑  ↑  miễn phí

# Ta chỉ cộng:



# 6 + 5 + 3 + 2 = 16

# Mô phỏng từng bước

# Ví dụ:



# cost = [6,5,7,9,2,2]

# Sau khi sort:



# [2,2,5,6,7,9]

# Ban đầu:



# i = 5

# total = 0

# Lần 1

# i = 5

# Nhóm:



# 9, 7, 6

# Trả:



# 9 + 7 = 16

# Miễn phí:



# 6

# Cập nhật:



# total = 16

# i = 2

# Lần 2

# i = 2

# Nhóm:



# 5, 2, 2

# Trả:



# 5 + 2 = 7

# Miễn phí:



# 2

# Cập nhật:



# total = 23

# i = -1

# Dừng.

# Kết quả:



# 23

# Tại sao i -= 3?

# Mỗi lần ta xử lý một nhóm gồm:



# [đắt nhất] [đắt nhì] [miễn phí]

# Tức là 3 viên kẹo.

# Ví dụ:



# 9 7 6 5 2 2

# ↑ ↑ x

# Sau khi xử lý nhóm đầu:



# 5 2 2

# ↑ ↑ x

# Nên phải nhảy qua 3 phần tử:



# i -= 3

# Độ phức tạp

# Sắp xếp:

# O(n log n)

# Duyệt mảng:

# O(n)

# Tổng:



# O(n log n)

# Bộ nhớ phụ:

# O(1)

# (nếu không tính bộ nhớ dùng cho việc sắp xếp).