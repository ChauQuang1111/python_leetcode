# Bài Concatenate Non-Zero Digits and Multiply by Sum II (08/07/2026)
# Ý tưởng của đề bài là:



# Cho một số nguyên (N). Thực hiện các bước sau cho đến khi số chỉ còn 1 chữ số.

# Ở mỗi bước:



# Lấy tất cả các chữ số khác 0 của số hiện tại.

# Ghép (concatenate) các chữ số đó theo đúng thứ tự để tạo thành một số mới.

# Tính tổng các chữ số của số hiện tại.

# Nhân số ghép được với tổng đó để tạo ra số mới.

# Lặp lại.

# Cuối cùng, in ra chữ số cuối cùng thu được.

# Ví dụ

# Giả sử

# [

# N = 12034

# ]

# Bước 1

# Các chữ số:



# 1 2 0 3 4

# Ghép các chữ số khác 0

# Bỏ số 0:



# 1 2 3 4

# Ghép lại:



# 1234

# Tổng các chữ số

# 1 + 2 + 0 + 3 + 4 = 10

# Nhân

# 1234 × 10 = 12340

# Số mới là



# 12340

# Bước tiếp theo

# Số hiện tại:



# 12340

# Ghép các chữ số khác 0:



# 1234

# Tổng:



# 1+2+3+4+0=10

# Nhân:



# 1234×10=12340

# Lúc này sẽ lặp lại mãi.

# (Nếu đây đúng là đề bạn đang làm thì đề sẽ có thêm điều kiện để tránh trường hợp này, hoặc yêu cầu số bước, hoặc giới hạn khác.)

# Ví dụ khác

# Giả sử



# N = 105

# Lần 1

# Ghép chữ số khác 0



# 15

# Tổng



# 1+0+5=6

# Nhân



# 15×6=90

# Lần 2

# 90

# Ghép chữ số khác 0



# 9

# Tổng



# 9+0=9

# Nhân



# 9×9=81

# Lần 3

# 81

# Ghép



# 81

# Tổng



# 8+1=9

# Nhân



# 81×9=729

# ...

# Ý nghĩa các từ trong tên bài

# Concatenate = ghép các chữ số lại thành một số.

# Ví dụ:



# 1, 4, 8 → 148

# Non-Zero Digits = chỉ lấy các chữ số khác 0.

# Multiply by Sum = nhân với tổng các chữ số.

# II = phiên bản thứ hai của bài toán (thường khó hơn phiên bản I).

# Bạn có thể gửi link đề bài hoặc ảnh đề đầy đủ được không?

# Có khá nhiều bài có tên gần giống nhau. Nếu bạn gửi đề đầy đủ, mình sẽ giải thích từng dòng của đề và ý tưởng giải mà không làm lộ lời giải ngay.

# Đoạn code này giải bài toán bằng Prefix Sum + Prefix Concatenation + Prefix Count, giúp trả lời mỗi query trong O(1) sau khi tiền xử lý.

# Ý tưởng

# Với mỗi truy vấn [l, r] cần tính



# Tổng các chữ số trong đoạn s[l:r].

# Ghép các chữ số khác 0 trong đoạn đó.

# Kết quả =

# [

# (\text{số ghép}) \times (\text{tổng chữ số}) \bmod (10^9+7)

# ]

# Nếu mỗi query đều duyệt từ l đến r thì



# Time = O(n*m) (TLE).

# Ta phải tiền xử lý.

# Code có chú thích
from typing import List

MOD = 10 ** 9 + 7

# pow10[i] = 10^i mod MOD

# Dùng để "dịch trái" số khi lấy đoạn con.

pow10 = [1] * 100001

for i in range(1, 100001):

    pow10[i] = pow10[i - 1] * 10 % MOD

class Solution:

    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:



        n = len(s)



        # prefix tổng chữ số

        prefix_sum = [0] * (n + 1)



        # prefix của số được ghép từ các chữ số khác 0

        prefix_concat = [0] * (n + 1)



        # prefix đếm bao nhiêu chữ số khác 0

        prefix_count = [0] * (n + 1)



        # -------------------------

        # Tiền xử lý

        # -------------------------

        for i, c in enumerate(s):



            d = int(c)



            # Tổng chữ số

            prefix_sum[i + 1] = prefix_sum[i] + d



            # Nếu d khác 0 thì ghép thêm vào cuối

            #

            # VD:

            # trước là 123

            # gặp 4

            #

            # 123 -> 1234

            #

            if d > 0:

                prefix_concat[i + 1] = (

                    prefix_concat[i] * 10 + d

                ) % MOD

            else:

                # gặp số 0 thì bỏ qua

                prefix_concat[i + 1] = prefix_concat[i]



            # Đếm số chữ số khác 0

            prefix_count[i + 1] = prefix_count[i] + (d > 0)



        ans = [0] * len(queries)



        # -------------------------

        # Trả lời từng query

        # -------------------------

        for i, (l, r) in enumerate(queries):



            # Có bao nhiêu chữ số khác 0 trong đoạn

            #

            # Ví dụ

            #

            # s = 102304

            #

            # đoạn = 0230

            #

            # chỉ có 2 và 3

            #

            length = prefix_count[r + 1] - prefix_count[l]



            # Tổng chữ số đoạn [l,r]

            total = prefix_sum[r + 1] - prefix_sum[l]



            # Lấy số ghép của đoạn [l,r]

            #

            # prefix_concat[r+1]

            #

            # = prefix trước l

            # + phần cần lấy

            #

            # Muốn bỏ prefix trước l

            # phải nhân với 10^(độ dài đoạn)

            #

            concat = (

                prefix_concat[r + 1]

                - prefix_concat[l] * pow10[length]

            ) % MOD



            ans[i] = concat * total % MOD



        return ans

# Điều khó hiểu nhất: prefix_concat

# Ví dụ



# s = "102304"

# Ta xây dựng



# i      0 1 2 3 4 5

# digit  1 0 2 3 0 4

# prefix_concat



# ban đầu = 0



# 1

# ↓



# 1



# 0

# ↓



# 1



# 2

# ↓



# 12



# 3

# ↓



# 123



# 0

# ↓



# 123



# 4

# ↓



# 1234

# Kết quả



# prefix_concat



# 0

# 1

# 1

# 12

# 123

# 123

# 1234

# Giả sử query lấy



# [2,5]



# chuỗi = 2304



# bỏ 0



# => 234

# Ta có



# prefix_concat[6] = 1234



# prefix_concat[2] = 1

# Nếu chỉ lấy



# 1234 - 1 = 1233

# thì sai.

# Vì số 1 đang nằm ở hàng nghìn.

# Ta phải dịch trái:



# 1 × 10^3 = 1000

# (do đoạn cần lấy có 3 chữ số khác 0)

# nên



# 1234

# -1000

# ------

# 234

# Đó là lý do có công thức



# concat = prefix_concat[r+1] - prefix_concat[l] * pow10[length]

# Vì sao cần prefix_count?

# Để biết phải nhân với 10^bao_nhiêu.

# Ví dụ



# 102304

# đoạn



# 0230

# không phải dài 4.

# Sau khi bỏ số 0 chỉ còn



# 23

# nên phải nhân



# 10²

# không phải



# 10⁴

# Do đó



# length = prefix_count[r+1] - prefix_count[l]

# chính là số lượng chữ số khác 0 trong đoạn, dùng để xác định số mũ của 10 khi loại bỏ phần tiền tố trong prefix_concat.

# Độ phức tạp

# Tiền xử lý:

# prefix_sum: O(n)

# prefix_concat: O(n)

# prefix_count: O(n)

# Mỗi truy vấn:

# Chỉ gồm vài phép trừ, nhân và lấy modulo: O(1)

# Tổng thời gian: O(n + m), với n là độ dài chuỗi và m là số lượng truy vấn. Bộ nhớ sử dụng: O(n).