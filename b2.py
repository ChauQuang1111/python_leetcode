#  13/08/2025
# 1390. Four Divisors


def sumFourDivisors(nums):
    total_sum = 0
    for num in nums:
        smallest_divisor = 0
        # Tìm ước số nhỏ nhất (lớn hơn 1) của num
        for divisor in range(2, int(num**0.5) + 1,1):
            if num % divisor == 0:
                if smallest_divisor == 0:
                    smallest_divisor = divisor
                else:
                    # Nếu tìm thấy ước số thứ hai, num có nhiều hơn 4 ước số
                    smallest_divisor = 0
                    break
        
        # Nếu num có chính xác 4 ước số, tính tổng và cộng vào tổng cuối
        if smallest_divisor > 0 and smallest_divisor * smallest_divisor != num:
            other_divisor = num // smallest_divisor
            total_sum += 1 + num + smallest_divisor + other_divisor

    return total_sum

# Ví dụ sử dụng
numbers = [21, 4, 7, 12, 10]
res = sumFourDivisors(numbers)
print( res)
# giải thích chỗ không hiểu :
# Bạn hoàn toàn có thể viết như vậy, nhưng trong Python, range(start, stop, step) có một quy tắc đặc biệt.
# Khi bạn không điền tham số step, giá trị mặc định của nó là 1.
# Do đó, range(2, int(num**0.5) + 1, 1) và range(2, int(num**0.5) + 1) cho kết quả hoàn toàn giống nhau.