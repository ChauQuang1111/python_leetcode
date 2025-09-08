# 1317. Convert Integer to the Sum of Two No-Zero Integers(08/09/2025)
from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # Vòng lặp từ 1 đến n để tìm số A
        for A in range(1, n):
            B = n - A
            
            # Kiểm tra xem cả A và B có phải là "số không chứa số 0" không
            if self.isNoZero(A) and self.isNoZero(B):
                # Nếu cả hai đều thỏa mãn, trả về danh sách [A, B]
                return [A, B]
        
        return [] # Trường hợp này sẽ không bao giờ xảy ra theo đề bài
    
    # Hàm phụ trợ để kiểm tra một số có chứa chữ số 0 hay không
    def isNoZero(self, num: int) -> bool:
        # Cách 1: Chuyển số thành chuỗi và kiểm tra ký tự '0'
        # return '0' not in str(num)
        
        # Cách 2: Duyệt từng chữ số của số (hiệu quả hơn)
        while num > 0:
            if num % 10 == 0:
                return False
            num //= 10
            
        return True