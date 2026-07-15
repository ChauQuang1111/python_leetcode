#  GCD of Odd and Even Sums (15/07/2026)

# Đề bài
# Cho một số nguyên n.
# Hãy tính:

# sumOdd: tổng của n số lẻ dương đầu tiên.
# sumEven: tổng của n số chẵn dương đầu tiên.
# Sau đó trả về GCD (ƯCLN) của hai tổng này. (LeetCode)
# Ví dụ
# Input

# n = 4
# Bước 1: Tính tổng số lẻ
# 4 số lẻ đầu tiên là:

# 1, 3, 5, 7
# Tổng:

# 1 + 3 + 5 + 7 = 16
# Nên

# sumOdd = 16
# Bước 2: Tính tổng số chẵn
# 4 số chẵn đầu tiên là:

# 2, 4, 6, 8
# Tổng:

# 2 + 4 + 6 + 8 = 20
# Nên

# sumEven = 20
# Bước 3: Tính GCD
# gcd(16, 20) = 4
# Kết quả:

# 4
# Điều đề bài muốn bạn làm
# Nếu làm theo đúng mô tả, bạn sẽ:

# Tính tổng n số lẻ đầu tiên.
# Tính tổng n số chẵn đầu tiên.
# Tính gcd(sumOdd, sumEven).
# Nhưng vì đây là bài Easy, mục tiêu là nhận ra quy luật toán học.
# Ta có:

# Tổng n số lẻ đầu tiên:
# [
# 1+3+5+\cdots+(2n-1)=n^2
# ]
# Tổng n số chẵn đầu tiên:
# [
# 2+4+6+\cdots+2n=n(n+1)
# ]
# Do đó
# [
# \gcd(n^2,;n(n+1))
# = n \times \gcd(n,;n+1)
# ]
# Mà hai số liên tiếp luôn nguyên tố cùng nhau:
# [
# \gcd(n,;n+1)=1
# ]
# Suy ra
# [
# \boxed{\gcd(sumOdd,;sumEven)=n}
# ]
# Vì vậy lời giải chỉ cần:

# class Solution {
# public:
#     int gcdOfOddEvenSums(int n) {
#         return n;
#     }
# };
# Độ phức tạp: O(1) thời gian và O(1) bộ nhớ. (LeetCode)

# 3658. GCD of Odd and Even Sums
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n