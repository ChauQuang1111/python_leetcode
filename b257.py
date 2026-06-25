# Count Subarrays With Majority Element I(25/06/2026)



# Đề bài

# Cho một mảng số nguyên nums.

# Hãy đếm số lượng mảng con liên tiếp (subarray) mà trong đó tồn tại một phần tử chiếm đa số (majority element).

# Majority Element là gì?

# Một phần tử được gọi là majority element nếu số lần xuất hiện của nó lớn hơn một nửa độ dài của mảng con.

# Công thức:

# Nếu mảng con có độ dài len thì phần tử x là majority khi:

# # [

# # count(x) > \frac{len}{2}

# # ]

# # Ví dụ 1

# nums = [1,2,1]

# Các mảng con:



# [1]       -> 1 xuất hiện 1/1 => majority

# [2]       -> 2 xuất hiện 1/1 => majority

# [1]       -> 1 xuất hiện 1/1 => majority



# [1,2]     -> 1 xuất hiện 1 lần, 2 xuất hiện 1 lần

#              không ai > 2/2 = 1 => không có majority



# [2,1]     -> tương tự => không có majority



# [1,2,1]   -> 1 xuất hiện 2 lần

#              2 > 3/2 = 1.5 => có majority

# Kết quả:



# 4

# Ví dụ 2

# # nums = [3,3,3]

# # Các mảng con:



# # [3]

# # [3]

# # [3]

# # [3,3]

# # [3,3]

# # [3,3,3]

# # Trong tất cả các mảng con trên, số 3 đều xuất hiện nhiều hơn một nửa độ dài.

# # Kết quả:



# # 6

# # Ví dụ 3

# # nums = [1,2,3]

# # Các mảng con:



# # [1] -> có majority

# # [2] -> có majority

# # [3] -> có majority



# # [1,2] -> không

# # [2,3] -> không

# # [1,2,3] -> không

# # Kết quả:



# # 3

# # Điều cần đếm

# # Ta cần đếm số cặp (l, r) sao cho:



# # subarray = nums[l...r]

# # và tồn tại một giá trị x thỏa:



# # số lần xuất hiện của x trong nums[l...r]

# # >

# # (r - l + 1)/2

# # Ý tưởng brute force

# # Với mỗi vị trí bắt đầu l:



# # Mở rộng điểm kết thúc r

# # Dùng HashMap đếm tần suất

# # Kiểm tra tần suất lớn nhất có vượt quá len/2 không

# for (int l = 0; l < n; l++) {

#     Map<Integer,Integer> freq = new HashMap<>();



#     for (int r = l; r < n; r++) {

#         freq.put(nums[r], freq.getOrDefault(nums[r],0)+1);



#         int len = r - l + 1;



#         if (maxFreq > len/2)

#             ans++;

#     }

# }

# Độ phức tạp:



# O(n²)

# (với việc cập nhật maxFreq phù hợp).

# Nếu bạn gửi nguyên văn đề LeetCode "Count Subarrays With Majority Element I" (vì có nhiều phiên bản I và II), mình có thể giải thích chi tiết hơn về input, output và ý tưởng tối ưu của bài đó.

# Đây là lời giải cho bài Count Subarrays With Majority Element I trên LeetCode.



# Ý tưởng chính

# Ta cần đếm số mảng con mà target là majority element.

# Điều kiện:



# count(target) > length(subarray) / 2

# Bước 1: Chuyển đổi mảng

# Ta biến đổi mỗi phần tử:



# target  -> +1

# khác target -> -1

# Ví dụ:



# nums   = [1,3,2,3,3]

# target = 3



# => [-1,+1,-1,+1,+1]

# Bước 2: Ý nghĩa prefix sum

# Gọi:



# prefix[i] = tổng từ đầu đến i

# Khi đó với một mảng con [l..r]:



# sum(l,r) = prefix[r] - prefix[l-1]

# Ta có:



# sum(l,r)

# =

# số target

# -

# số phần tử khác target

# Nếu target là majority:



# số target > số khác

# ⇔



# số target - số khác > 0

# ⇔



# sum(l,r) > 0

# Như vậy bài toán trở thành:



# Đếm số đoạn con có tổng dương.

# Bước 3: Prefix sum

# Ta duy trì:



# pre = prefix sum hiện tại

# Mỗi lần:



# if num == target:

#     pre += 1

# else:

#     pre -= 1

# Bước 4: Điều kiện đếm

# Ta cần số lượng chỉ số trước đó j sao cho:



# prefix[j] < prefix[i]

# vì



# prefix[i] - prefix[j] > 0

# => đoạn (j+1 .. i) có tổng dương.

# Vai trò của cnt và acc

# cnt[x]

# cnt[x] = số lần prefix sum = x đã xuất hiện

# acc[x]

# acc[x]

# =

# cnt[0] + cnt[1] + ... + cnt[x]

# Tức là tổng tích lũy.

# Nhờ đó:



# acc[pre-1]

# chính là số prefix nhỏ hơn pre.

# Đó là số đoạn con kết thúc tại vị trí hiện tại mà target là majority.

# Code có chú thích

from typing import List
class Solution:

    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:



        n = len(nums)



        # prefix sum có thể nằm trong [-n, n]

        # dịch sang phải để tránh index âm

        OFFSET = n + 1



        # cnt[x] = số lần prefix sum = x

        cnt = [0] * (2 * n + 2)



        # acc[x] = tổng cnt[0..x]

        acc = [0] * (2 * n + 2)



        # prefix sum ban đầu = 0

        pre = OFFSET



        # có 1 prefix sum = 0 trước khi duyệt

        cnt[pre] = 1

        acc[pre] = 1



        res = 0



        for num in nums:



            # target được xem là +1

            if num == target:

                pre += 1

            else:

                pre -= 1



            # lưu prefix hiện tại

            cnt[pre] += 1



            # cập nhật prefix-count tích lũy

            acc[pre] = acc[pre - 1] + cnt[pre]



            # acc[pre-1]

            # = số prefix sum nhỏ hơn prefix hiện tại

            # => số đoạn con kết thúc ở đây

            # mà target là majority

            res += acc[pre - 1]



        return res

# Ví dụ chạy tay

# nums = [3,1,3]

# target = 3

# Chuyển thành:



# [+1,-1,+1]

# Prefix:



# 0

# 1

# 0

# 1

# Ta đếm số cặp:



# prefix[j] < prefix[i]

# Các cặp hợp lệ:



# 0 -> 1

# 0 -> 1

# 0 -> 1

# Tương ứng các đoạn:



# [3]

# [3,1,3]

# [3]

# Có 3 đoạn mà 3 là majority.

# Tuy nhiên, đoạn code bạn đưa thực ra là một cách cài đặt khá "lạ". Nếu xem kỹ, acc chỉ được cập nhật tại vị trí pre, nên để chạy đúng cần duy trì cấu trúc prefix-frequency đầy đủ (thường dùng Fenwick Tree/BIT hoặc Segment Tree). Phiên bản chuẩn của lời giải LeetCode thường dùng Fenwick Tree để đếm số prefix sum nhỏ hơn prefix hiện tại trong O(n log n).