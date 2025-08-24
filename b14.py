# 1493. Longest Subarray of 1's After Deleting One Element(24/08/2025)
from typing import List
class Solution:
    def longestSubarray(self,nums: list[int]) -> int:
        if 0 not in nums:
            return len(nums) - 1
        if len(nums) == 1 or 1 not in nums:
            return 0
        
        list_with_max_long = [0]
        temp_count = 0
        zeros_count = 0
        
        
        
        for num in nums[nums.index(1):]:
            if num != 0:
                temp_count +=1
            elif num == 0:
                zeros_count +=1   
                list_with_max_long.append(temp_count)
                list_with_max_long.append(temp_count-list_with_max_long[-2])
                if len(list_with_max_long) > 3:
                    temp_count -=list_with_max_long[-3]
        list_with_max_long.append(temp_count)    
            
        
        return (max(list_with_max_long))





# ### Phân tích và giải thích thuật toán

# Đoạn mã bạn cung cấp dường như đang cố gắng giải bài toán "Longest Subarray of 1s After Deleting One Element" (LeetCode 1493). Tuy nhiên, thuật toán này phức tạp, khó hiểu và có thể không chính xác.

# Tôi sẽ giải thích cách nó hoạt động và chỉ ra những điểm chưa hợp lý.

# -----

# ### Phân tích từng phần của đoạn mã

# 1.  **Xử lý các trường hợp đặc biệt (Special cases)**

#     ```python
#     if 0 not in nums:
#         return len(nums) - 1
#     if len(nums) == 1 or 1 not in nums:
#         return 0
#     ```

#       * **`if 0 not in nums:`**: Nếu mảng chỉ chứa toàn số `1`, bạn phải xóa một phần tử. Do đó, độ dài của mảng con dài nhất sẽ là `len(nums) - 1`. Đây là logic đúng.
#       * **`if len(nums) == 1 or 1 not in nums:`**: Nếu mảng chỉ có một phần tử hoặc không có số `1` nào, không thể tạo ra một mảng con chỉ gồm số `1`. Kết quả là `0`. Đây cũng là logic đúng.

# 2.  **Khởi tạo biến**

#     ```python
#     list_with_max_long = [0]
#     temp_count = 0
#     zeros_count = 0
#     ```

#       * `list_with_max_long`: Một danh sách để lưu trữ độ dài các mảng con.
#       * `temp_count`: Đếm số lượng số `1` liên tiếp.
#       * `zeros_count`: Đếm số lượng số `0`.

# 3.  **Vòng lặp chính và logic không rõ ràng**

#     ```python
#     for num in nums[nums.index(1):]:
#         if num != 0:
#             temp_count +=1
#         elif num == 0:
#             zeros_count +=1   
#             list_with_max_long.append(temp_count)
#             list_with_max_long.append(temp_count-list_with_max_long[-2])
#             if len(list_with_max_long) > 3:
#                 temp_count -=list_with_max_long[-3]
#     ```

    #   * **`for num in nums[nums.index(1):]`**: Vòng lặp bắt đầu từ phần tử `1` đầu tiên trong mảng. Điều này có thể bỏ qua một mảng con các số `1` ở đầu nếu nó đứng sau số `0`, điều này không hiệu quả. Ví dụ: `[0, 1, 1, 1]`.
    #   * **`if num != 0:`**: Tăng `temp_count` nếu phần tử là `1`.
#       * **`elif num == 0:`**: Đây là phần phức tạp và khó hiểu nhất. Khi gặp một số `0`, thuật toán thực hiện:
#           * `list_with_max_long.append(temp_count)`: Lưu lại `temp_count` (số `1` trước số `0` này).
#           * `list_with_max_long.append(temp_count - list_with_max_long[-2])`: Thêm một giá trị nữa vào danh sách. Logic của phép tính này rất khó hiểu và dường như không liên quan đến việc tính tổng hai mảng con số `1` xung quanh số `0`. `list_with_max_long[-2]` là giá trị `temp_count` vừa được thêm vào trước đó, nên phép tính này luôn trả về `0`, không có ý nghĩa.
#           * `if len(list_with_max_long) > 3: temp_count -= list_with_max_long[-3]`: Lại một logic phức tạp và dường như không chính xác khác. Nó cố gắng trừ đi một giá trị nào đó từ `temp_count` nhưng không rõ để làm gì.

# 4.  **Kết quả cuối cùng**

#     ```python
#     list_with_max_long.append(temp_count)    
#     return (max(list_with_max_long))
#     ```

#       * Sau vòng lặp, `temp_count` cuối cùng được thêm vào danh sách.
#       * Cuối cùng, hàm trả về giá trị lớn nhất trong `list_with_max_long`. Vì danh sách này chứa những giá trị không được tính toán đúng cách, kết quả có thể sai.

# ### Kết luận và cách tiếp cận đúng

# Thuật toán này **không giải quyết bài toán một cách hiệu quả và chính xác**. Logic xử lý khi gặp số `0` quá phức tạp và không tuân theo một mô hình rõ ràng. Việc trừ đi các giá trị trong danh sách `list_with_max_long` khiến `temp_count` không còn đại diện cho số `1` liên tiếp nữa.

# Để giải quyết bài toán này, bạn có thể sử dụng một thuật toán đơn giản hơn nhiều:

# 1.  **Duyệt mảng và lưu lại độ dài của các mảng con số `1` liên tiếp.** Bạn có thể dùng một biến đếm, khi gặp `0` thì lưu lại biến đếm và reset nó.
# 2.  **Tính toán kết quả.** Sau khi có danh sách độ dài các mảng con số `1`, bạn có thể:
#       * Tìm độ dài lớn nhất của một mảng con (trường hợp không xóa `0`).
#       * Tìm tổng của hai mảng con số `1` liền kề (ngăn cách bởi một số `0`).
# 3.  **Kết quả cuối cùng** sẽ là giá trị lớn nhất trong số các kết quả tính được.

# Cách tiếp cận hiệu quả nhất cho bài toán này là sử dụng **kỹ thuật cửa sổ trượt (sliding window)**, chỉ cần một lần duyệt mảng. Bạn có thể giữ một cửa sổ chỉ chứa tối đa một số `0`.