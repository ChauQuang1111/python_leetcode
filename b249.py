# Destroying Asteroids (31/05/2026)

# Đề bài

# Bạn có:



# Một hành tinh có khối lượng ban đầu mass.

# Một mảng asteroids, trong đó asteroids[i] là khối lượng của tiểu hành tinh thứ i.

# Quy tắc:



# Bạn có thể chọn phá hủy các tiểu hành tinh theo bất kỳ thứ tự nào.

# Nếu khối lượng hiện tại của hành tinh lớn hơn hoặc bằng khối lượng của tiểu hành tinh:

# Hành tinh phá hủy được tiểu hành tinh đó.

# Khối lượng của hành tinh tăng thêm đúng bằng khối lượng tiểu hành tinh.

# mass = mass + asteroids[i]

# Nếu khối lượng hiện tại của hành tinh nhỏ hơn khối lượng tiểu hành tinh:

# Hành tinh bị phá hủy.

# Không thể tiếp tục.

# Yêu cầu:



# Trả về true nếu có thể phá hủy tất cả các tiểu hành tinh, ngược lại trả về false.

# Ví dụ 1

# mass = 10

# asteroids = [3, 9, 19, 5, 21]

# Sắp xếp tăng dần:



# [3, 5, 9, 19, 21]

# Quá trình:



# mass = 10



# 10 >= 3  => mass = 13

# 13 >= 5  => mass = 18

# 18 >= 9  => mass = 27

# 27 >= 19 => mass = 46

# 46 >= 21 => mass = 67

# Phá hủy được tất cả ⇒



# true

# Ví dụ 2

# mass = 5

# asteroids = [4, 9, 23, 4]

# Sắp xếp:



# [4, 4, 9, 23]

# Quá trình:



# 5 >= 4  => mass = 9

# 9 >= 4  => mass = 13

# 13 >= 9 => mass = 22

# 22 < 23

# Không phá được tiểu hành tinh cuối ⇒



# false

# Ý tưởng chính

# Để có cơ hội sống sót cao nhất:



# Luôn phá những tiểu hành tinh nhỏ nhất trước.

# Vì sau mỗi lần phá hủy, khối lượng của hành tinh sẽ tăng lên.

# Do đó lời giải là:



# Sắp xếp asteroids tăng dần.

# Duyệt từ nhỏ đến lớn:

# Nếu mass < asteroid ⇒ false.

# Ngược lại mass += asteroid.

# Duyệt hết ⇒ true.

# Độ phức tạp:



# Sắp xếp: O(n log n)

# Duyệt: O(n)

# Tổng cộng:



# O(n log n)

# Đây là một cách giải không cần sắp xếp. Ý tưởng là liên tục ăn những tiểu hành tinh mà hành tinh hiện tại có thể ăn được, sau mỗi vòng lặp khối lượng sẽ tăng lên và có thể ăn được thêm các tiểu hành tinh lớn hơn.



# Code có chú thích
from typing import List
class Solution:

    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:



        # Khối lượng lớn nhất trong tất cả các tiểu hành tinh

        mx = max(asteroids)



        # Tiếp tục cho đến khi không còn tiểu hành tinh nào

        while asteroids:



            # Lưu các tiểu hành tinh chưa ăn được ở vòng hiện tại

            uneaten = []



            # Duyệt toàn bộ danh sách

            for aster in asteroids:



                # Nếu khối lượng hiện tại nhỏ hơn tiểu hành tinh

                # thì chưa thể phá hủy nó

                if mass < aster:

                    uneaten.append(aster)



                # Có thể phá hủy được

                else:

                    mass += aster



                    # Nếu khối lượng hiện tại đã lớn hơn hoặc bằng

                    # tiểu hành tinh lớn nhất

                    # thì chắc chắn sẽ ăn được tất cả phần còn lại

                    if mass >= mx:

                        return True



            # Nếu sau một vòng lặp không ăn được thêm tiểu hành tinh nào

            # => bị kẹt, không thể tăng khối lượng nữa

            if len(uneaten) == len(asteroids):

                return False



            # Chỉ giữ lại những tiểu hành tinh chưa ăn được

            # để xử lý ở vòng tiếp theo

            asteroids = uneaten



        # Ăn hết tất cả tiểu hành tinh

        return True

# Thuật toán hoạt động như thế nào?

# Ví dụ:



# mass = 10

# asteroids = [20, 5, 3, 50]

# Vòng 1

# mass = 10



# 20  -> chưa ăn được

# 5   -> ăn được => mass = 15

# 3   -> ăn được => mass = 18

# 50  -> chưa ăn được



# uneaten = [20, 50]

# Vòng 2

# mass = 18



# 20 -> chưa ăn được

# 50 -> chưa ăn được

# Không ăn được tiểu hành tinh nào mới:



# len(uneaten) == len(asteroids)

# => Trả về False.

# Ví dụ khác:



# mass = 10

# asteroids = [20, 5, 3, 15]

# Vòng 1

# 20 -> chưa ăn được

# 5  -> mass = 15

# 3  -> mass = 18

# 15 -> mass = 33

# Lúc này:



# mx = 20

# mass = 33 >= 20

# Vì hành tinh đã lớn hơn tiểu hành tinh lớn nhất nên chắc chắn ăn được tất cả những tiểu hành tinh còn lại.



# return True

# Ý nghĩa của điều kiện

# if mass >= mx:

#     return True

# Giả sử:



# mx = 100

# mass = 120

# Mọi tiểu hành tinh còn lại đều có:



# asteroid <= 100

# Do đó:



# mass >= asteroid

# nên hành tinh sẽ ăn được tất cả chúng.

# Độ phức tạp

# Giả sử có n tiểu hành tinh.



# Mỗi vòng lặp duyệt toàn bộ danh sách còn lại.

# Trong trường hợp xấu nhất chỉ ăn được 1 tiểu hành tinh mỗi vòng.

# Khi đó số phép xử lý là:



# n + (n-1) + (n-2) + ... + 1

# 1+2+3+\cdots+n=\frac{n(n+1)}{2}

# Nên độ phức tạp là:



# O(n²)

# Trong khi lời giải chuẩn là:



# Sắp xếp tăng dần.

# Ăn từ nhỏ đến lớn.

# Độ phức tạp:



# O(n log n)

# nên nhanh hơn đáng kể khi n lớn.