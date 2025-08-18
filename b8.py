from typing import List

class Solution:
    EPS = 1e-6   # sai số cho số thực

    def judgePoint24(self, cards: List[int]) -> bool:
        A = [float(x) for x in cards]   # chuyển sang float
        return self.backtrack(A, len(A))

    def backtrack(self, A: List[float], n: int) -> bool:
        if n == 1:
            return abs(A[0] - 24) < self.EPS

        for i in range(n):
            for j in range(i + 1, n):
                a, b = A[i], A[j]

                # "xoá" phần tử j bằng cách thay bằng cuối mảng
                A[j] = A[n - 1]

                # Thử tất cả phép toán
                A[i] = a + b
                if self.backtrack(A, n - 1):
                    return True

                A[i] = a - b
                if self.backtrack(A, n - 1):
                    return True

                A[i] = b - a
                if self.backtrack(A, n - 1):
                    return True

                A[i] = a * b
                if self.backtrack(A, n - 1):
                    return True

                if abs(b) > self.EPS:
                    A[i] = a / b
                    if self.backtrack(A, n - 1):
                        return True

                if abs(a) > self.EPS:
                    A[i] = b / a
                    if self.backtrack(A, n - 1):
                        return True

                # backtrack: khôi phục lại giá trị cũ
                A[i], A[j] = a, b

        return False