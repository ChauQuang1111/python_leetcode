# Jump Game IV(18/05/2026)



# ---

# ## Đề bài

# Cho một mảng số nguyên `arr`.

# Bạn đang đứng ở vị trí đầu tiên `index = 0`.

# Từ vị trí `i`, bạn có thể nhảy đến:

# * `i + 1` nếu còn trong mảng
# * `i - 1` nếu còn trong mảng
# * bất kỳ vị trí `j` nào sao cho:

# [
# arr[i] = arr[j] \quad \text{và} \quad i \ne j
# ]

# Mục tiêu:

# 👉 Tìm **số bước nhảy ít nhất** để đi từ vị trí `0` đến vị trí cuối cùng `n - 1`.

# ---

# # Ví dụ

# ## Example 1

# ```text
# arr = [100,-23,-23,404,100,23,23,23,3,404]
# ```

# Kết quả:

# ```text
# 3
# ```

# ### Giải thích

# Có thể đi:

# ```text
# index 0 -> index 4 -> index 3 -> index 9
# ```

# Vì:

# * `arr[0] = 100`
# * `arr[4] = 100`

# nên nhảy trực tiếp từ `0` sang `4`.

# Tiếp theo:

# * `arr[4] + jump -> index 3`
# * `arr[3] = 404`
# * `arr[9] = 404`

# nên nhảy tiếp sang `9`.

# Tổng cộng: **3 bước**.

# ---

# # Ý tưởng của bài

# Đây là bài tìm:

# > số bước ít nhất từ điểm A đến điểm B

# ➡️ thường dùng:

# # BFS (Breadth First Search)

# Vì mỗi lần nhảy được xem như đi qua 1 cạnh của graph.

# ---

# # Các kiểu nhảy

# Từ index `i`, có 3 loại cạnh:

# ## 1. Sang trái

# ```text
# i -> i - 1
# ```

# ---

# ## 2. Sang phải

# ```text
# i -> i + 1
# ```

# ---

# ## 3. Nhảy tới index có cùng giá trị

# Ví dụ:

# ```text
# arr = [7,6,9,6,9,6,9,7]
# ```

# Từ:

# ```text
# index 0 (value = 7)
# ```

# có thể nhảy tới:

# ```text
# index 7
# ```

# vì cùng giá trị `7`.

# ---

# # Điều khó của bài

# Nếu mỗi lần lại đi tìm toàn bộ index có cùng giá trị thì rất chậm.

# Ví dụ:

# ```text
# [7,7,7,7,7,7,7....]
# ```

# ---

# # Cách tối ưu

# Ta dùng:

# ```java
# HashMap<Integer, List<Integer>>
# ```

# để lưu:

# ```text
# value -> danh sách index
# ```

# Ví dụ:

# ```text
# 100 -> [0,4]
# 404 -> [3,9]
# 23 -> [5,6,7]
# ```

# ---

# # BFS hoạt động thế nào

# Ta bắt đầu từ:

# ```text
# index = 0
# ```

# Sau đó:

# * đưa vào queue
# * mỗi lần lấy ra:

#   * xét trái
#   * xét phải
#   * xét các index cùng value

# Nếu tới `n - 1`:

# ✅ trả về số bước.

# ---

# # Tại sao phải xóa list sau khi dùng?

# Ví dụ:

# ```text
# 23 -> [5,6,7]
# ```

# Nếu đã xử lý value `23` rồi mà không xóa:

# thì lần sau gặp lại `23` sẽ duyệt lại toàn bộ list → TLE.

# Nên thường có:

# ```java
# map.remove(arr[i]);
# ```

# hoặc:

# ```java
# map.get(arr[i]).clear();
# ```

# để tránh duyệt lại.

# ---

# # Độ phức tạp

# Nếu tối ưu đúng:

# * Time:

# [
# O(n)
# ]

# * Space:

# [
# O(n)
# ]

# ---

# # Ý tưởng ngắn gọn

# * Xem mỗi index là 1 node
# * Có thể đi:

#   * trái
#   * phải
#   * cùng giá trị
# * Dùng BFS để tìm đường ngắn nhất
# * Dùng HashMap để nhảy nhanh đến các index cùng value
# * Xóa list đã dùng để tránh TLE


from typing import List
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # số phần tử của mảng
        n = len(arr)
        # nếu chỉ có 1 phần tử

        # đang ở đầu cũng là cuối -> không cần nhảy

        if n <= 1:

            return 0



        # HashMap:

        # value -> danh sách index có cùng value

        #

        # ví dụ:

        # arr = [100,-23,-23,404,100]

        #

        # {

        #   100: [0,4],

        #   -23: [1,2],

        #   404: [3]

        # }

        valueToIdx = {}



        # duyệt từng phần tử để build map

        for i, num in enumerate(arr):



            # nếu value đã tồn tại

            # append thêm index

            if num in valueToIdx:

                valueToIdx[num].append(i)



            # nếu chưa có

            # tạo list mới

            else:

                valueToIdx[num] = [i]



        # visited dùng để tránh duyệt lại

        #

        # ban đầu:

        # 0 là điểm bắt đầu

        # n-1 là điểm kết thúc

        visited = {0, n - 1}



        # số bước nhảy

        jumps = 0



        # Bidirectional BFS

        #

        # start:

        # BFS từ đầu mảng

        start = set([0])



        # end:

        # BFS từ cuối mảng

        end = set([n - 1])



        # khi còn node để duyệt

        while start:



            # luôn mở rộng phía nhỏ hơn

            # để tối ưu tốc độ

            if len(start) > len(end):

                start, end = end, start



            # queue của level tiếp theo

            nextQ = set()



            # duyệt từng index hiện tại

            for i in start:



                # -----------------------------------

                # 1. NHẢY TỚI CÁC INDEX CÙNG VALUE

                # -----------------------------------



                # lấy toàn bộ index có cùng giá trị arr[i]

                for j in valueToIdx[arr[i]]:



                    # nếu gặp phía bên kia

                    # nghĩa là 2 BFS đã gặp nhau

                    # -> tìm được đường ngắn nhất

                    if j in end:

                        return jumps + 1



                    # nếu chưa visited

                    if j not in visited:



                        # thêm vào level tiếp theo

                        nextQ.add(j)



                        # đánh dấu đã thăm

                        visited.add(j)



                # rất quan trọng

                #

                # clear để tránh duyệt lại

                #

                # nếu không:

                # mỗi lần gặp cùng value

                # sẽ duyệt lại toàn bộ list

                # -> TLE

                valueToIdx[arr[i]].clear()



                # -----------------------------------

                # 2. NHẢY SANG TRÁI / PHẢI

                # -----------------------------------



                # nếu trái hoặc phải gặp phía BFS còn lại

                if i - 1 in end or i + 1 in end:

                    return jumps + 1



                # xét index bên trái

                if i - 1 >= 0 and i - 1 not in visited:



                    nextQ.add(i - 1)

                    visited.add(i - 1)



                # xét index bên phải

                if i + 1 < n and i + 1 not in visited:



                    nextQ.add(i + 1)

                    visited.add(i + 1)



            # đi sang level tiếp theo

            jumps += 1



            # cập nhật queue mới

            start = nextQ



        # không tìm được đường

        return -1

# Ý tưởng thuật toán

# Bài này dùng:



# Bidirectional BFS

# Thay vì BFS từ một phía:



# 0 -> n-1

# ta BFS từ cả 2 phía:

# 0 <-----> n-1

# Khi hai phía gặp nhau:

# ✅ tìm được đáp án.

# Tại sao nhanh hơn BFS thường?

# Ví dụ:



# BFS thường:

# [

# O(b^d)

# ]

# Bidirectional BFS:

# [

# O(b^{d/2})

# ]

# Nhanh hơn rất nhiều khi graph lớn.

# Các bước chính

# 1. Build map

# valueToIdx[value] = [list index]

# để nhảy nhanh tới các vị trí cùng value.

# 2. BFS từ 2 đầu

# start = {0}

# end = {n-1}

# 3. Expand phía nhỏ hơn

# if len(start) > len(end):

#     start, end = end, start

# Giúp giảm số node phải duyệt.

# 4. Từ mỗi index có thể:

# đi trái

# đi phải

# đi tới index cùng value

# 5. Nếu gặp phía còn lại

# if j in end:

# => hai BFS gặp nhau

# => return số bước.