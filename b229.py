# # Bài **“Separate the Digits in an Array”**(11/05/2026)

# ## Giải thích thuật toán

# Bài toán yêu cầu:

# * Duyệt từng số trong mảng
# * Tách từng chữ số của số đó
# * Đưa các chữ số vào mảng kết quả theo đúng thứ tự

# ---

# # Ví dụ

# ```python id="qg3f5d"
# nums = [13, 25, 83]
# ```

# Ta xử lý:

# ```text id="2qkcck"
# 13 -> 1, 3
# 25 -> 2, 5
# 83 -> 8, 3
# ```

# Kết quả:

# ```python id="jlwmyl"
# [1, 3, 2, 5, 8, 3]
# ```

# ---

# # Ý tưởng thuật toán

# Code sử dụng cách đơn giản nhất:

# ## Bước 1

# Duyệt từng số trong mảng.

# ```python id="njlwmq"
# for num in nums:
# ```

# ---

# ## Bước 2

# Chuyển số thành chuỗi.

# Ví dụ:

# ```python id="j3n05v"
# str(25)
# ```

# →

# ```text id="fml72n"
# "25"
# ```

# ---

# ## Bước 3

# Duyệt từng ký tự trong chuỗi.

# ```python id="6gr4a3"
# for digit in str(num):
# ```

# Ví dụ:

# ```text id="j6n4l4"
# "25"
# ```

# ta lấy được:

# ```text id="b3f9v6"
# '2'
# '5'
# ```

# ---

# ## Bước 4

# Ép kiểu ký tự thành số nguyên rồi thêm vào mảng kết quả.

# ```python id="sijvko"
# solution.append(int(digit))
# ```

# Ví dụ:

# ```python id="kk7v2u"
# int('2') -> 2
# ```

# ---

# # Mô phỏng từng bước

# ## Input

# ```python id="2oq1cv"
# nums = [13, 25]
# ```

# ---

# ## Lần 1

# ```python id="zhd5a4"
# num = 13
# ```

# Chuyển thành:

# ```text id="vd9p6h"
# "13"
# ```

# Duyệt:

# ```text id="x1rll1"
# '1' -> 1
# '3' -> 3
# ```

# Mảng:

# ```python id="f55h08"
# [1, 3]
# ```

# ---

# ## Lần 2

# ```python id="a0pkzf"
# num = 25
# ```

# Duyệt:

# ```text id="i4hcn0"
# '2' -> 2
# '5' -> 5
# ```

# Kết quả cuối:

# ```python id="y37mlj"
# [1, 3, 2, 5]
# ```

# ---

# # Code có chú thích

# ```python
# class Solution:

#     # Hàm tách từng chữ số trong mảng
#     def separateDigits(self, nums: list[int]) -> list[int]:

#         # Mảng lưu kết quả
#         solution: list[int] = []

#         # Duyệt từng số trong mảng
#         for num in nums:

#             # Chuyển số thành chuỗi
#             # Ví dụ: 25 -> "25"
#             for digit in str(num):

#                 # digit là ký tự
#                 # Ví dụ: '2', '5'

#                 # Chuyển ký tự thành số nguyên
#                 # rồi thêm vào mảng kết quả
#                 solution.append(int(digit))

#         # Trả về kết quả
#         return solution
# ```

# ---

# # Độ phức tạp

# ## Time Complexity

# Mỗi chữ số được duyệt đúng 1 lần:

# ```text id="l2r7y9"
# O(total digits)
# ```

# ---

# ## Space Complexity

# Mảng kết quả lưu toàn bộ chữ số:

# ```text id="wdpry2"
# O(total digits)
# ```


# # Cho một mảng số nguyên `nums`.
# # Hãy tách từng chữ số của mỗi phần tử trong mảng theo đúng thứ tự xuất hiện và tạo thành một mảng mới.

# # Ví dụ:

# # ```text
# # nums = [13, 25, 83, 77]
# # ```

# # * `13` → tách thành `1, 3`
# # * `25` → tách thành `2, 5`
# # * `83` → tách thành `8, 3`
# # * `77` → tách thành `7, 7`

# # Kết quả:

# # ```text
# # [1,3,2,5,8,3,7,7]
# # ```

# # ---

# # ## Ý nghĩa đề bài

# # Ta duyệt từng số trong mảng:

# # Ví dụ số:

# # ```text
# # 409
# # ```

# # Ta phải lấy ra:

# # ```text
# # 4, 0, 9
# # ```

# # rồi thêm vào mảng kết quả.

# # ---

# # ## Lưu ý quan trọng

# # ### 1. Giữ nguyên thứ tự

# # Ví dụ:

# # ```text
# # nums = [12, 34]
# # ```

# # Kết quả phải là:

# # ```text
# # [1,2,3,4]
# # ```

# # KHÔNG phải:

# # ```text
# # [2,1,4,3]
# # ```

# # ---

# # ### 2. Tách từng chữ số

# # Một số có nhiều chữ số phải được tách riêng từng số.

# # Ví dụ:

# # ```text
# # 507
# # ```

# # →

# # ```text
# # 5,0,7
# # ```

# # ---

# # ## Cách làm đơn giản

# # ### Cách dễ hiểu nhất

# # * Chuyển số thành chuỗi
# # * Duyệt từng ký tự
# # * Đổi lại thành số nguyên
# # * Thêm vào kết quả

# # ---

# # ## Ví dụ từng bước

# # ```text
# # nums = [13,25]
# # ```

# # ### Bước 1:

# # Lấy `13`

# # ```text
# # "13"
# # ```

# # Duyệt:

# # * `'1'` → 1
# # * `'3'` → 3

# # Kết quả hiện tại:

# # ```text
# # [1,3]
# # ```

# # ---

# # ### Bước 2:

# # Lấy `25`

# # ```text
# # "25"
# # ```

# # Duyệt:

# # * `'2'` → 2
# # * `'5'` → 5

# # Kết quả cuối:

# # ```text
# # [1,3,2,5]
# # ```

# # ---

# # ## Độ khó

# # Đây là bài dễ (Easy) trên LeetCode, chủ yếu luyện:

# # * duyệt mảng
# # * xử lý chuỗi
# # * thao tác với chữ số

# # ---

# # ## Java code mẫu

# # ```java
# # class Solution {
# #     public int[] separateDigits(int[] nums) {

# #         ArrayList<Integer> list = new ArrayList<>();

# #         for (int num : nums) {

# #             String s = String.valueOf(num);

# #             for (char c : s.toCharArray()) {
# #                 list.add(c - '0');
# #             }
# #         }

# #         int[] result = new int[list.size()];

# #         for (int i = 0; i < list.size(); i++) {
# #             result[i] = list.get(i);
# #         }

# #         return result;
# #     }
# # }
# # ```
class Solution:

    # Hàm tách từng chữ số trong mảng
    def separateDigits(self, nums: list[int]) -> list[int]:

        # Mảng lưu kết quả
        solution: list[int] = []

        # Duyệt từng số trong mảng
        for num in nums:

            # Chuyển số thành chuỗi
            # Ví dụ: 25 -> "25"
            for digit in str(num):

                # digit là ký tự
                # Ví dụ: '2', '5'

                # Chuyển ký tự thành số nguyên
                # rồi thêm vào mảng kết quả
                solution.append(int(digit))

        # Trả về kết quả
        return solution