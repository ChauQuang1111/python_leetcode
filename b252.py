# Earliest Finish Time for Land and Water Rides II(03/06/2026)
# Bài "Earliest Finish Time for Land and Water Rides II" yêu cầu:



# Có 2 nhóm trò chơi:

# Land rides (trò trên cạn)

# Water rides (trò dưới nước)

# Mỗi trò có:

# startTime: thời điểm sớm nhất được phép bắt đầu.

# duration: thời gian chơi.

# Du khách phải chơi:

# ✅ đúng 1 trò trên cạn

# và

# ✅ đúng 1 trò dưới nước

# Theo bất kỳ thứ tự nào:



# Land → Water

# Water → Land

# Mục tiêu:

# 👉 Tìm thời điểm sớm nhất hoàn thành cả hai trò.

# Ví dụ 1

# landStartTime = [2,8]

# landDuration  = [4,1]



# waterStartTime = [6]

# waterDuration  = [3]

# Chọn land 0 trước

# Land 0:

# bắt đầu = 2

# kết thúc = 2 + 4 = 6

# Sau đó chơi water 0:



# water mở lúc 6

# ta đến lúc 6



# bắt đầu = 6

# kết thúc = 6 + 3 = 9

# Hoàn thành lúc:



# 9

# Chọn land 1 trước

# Land 1:

# bắt đầu = 8

# kết thúc = 9

# Water đã mở từ lúc 6 nên:



# bắt đầu water = 9

# kết thúc = 12

# Tệ hơn.

# Chọn water trước

# Water:

# 6 -> 9

# Sau đó:



# Land 0:

# 9 -> 13



# Land 1:

# 9 -> 10

# Tốt nhất là 10.

# Kết quả cuối cùng:



# min(9,10)=9

# Ý tưởng quan trọng

# Giả sử ta quyết định:



# Land -> Water

# Khi đó:



# Bước 1

# Tìm trò land nào kết thúc sớm nhất.



# finishLand = min(

#     landStartTime[i] + landDuration[i]

# )

# Giả sử:



# finishLand = 6

# Bước 2

# Xét từng water ride.

# Nếu water mở trước khi ta tới:



# waterStart <= finishLand

# thì chơi ngay.

# Ngược lại phải đợi.

# Thời điểm bắt đầu water:



# max(finishLand, waterStart)

# Thời điểm kết thúc:



# max(finishLand, waterStart)

# + waterDuration

# Lấy nhỏ nhất trong tất cả water rides.

# Tại sao chỉ cần xét land kết thúc sớm nhất?

# Giả sử có hai land rides:



# A kết thúc lúc 5

# B kết thúc lúc 8

# Sau khi chơi land xong mới được chơi water.

# Rõ ràng:



# đến water lúc 5

# luôn không tệ hơn



# đến water lúc 8

# Vì đến sớm hơn hoặc bằng.

# Do đó nếu chọn thứ tự:



# Land -> Water

# thì chỉ cần biết:



# minEndLand

# (tức thời gian kết thúc land sớm nhất).

# Tương tự cho:



# Water -> Land

# Công thức

# Land → Water

# minEndLand =

# min(landStartTime[i] + landDuration[i])



# ans1 =

# min(

#     max(minEndLand, waterStartTime[j])

#     + waterDuration[j]

# )

# Water → Land

# minEndWater =

# min(waterStartTime[j] + waterDuration[j])



# ans2 =

# min(

#     max(minEndWater, landStartTime[i])

#     + landDuration[i]

# )

# Đáp án

# min(ans1, ans2)

# Độ phức tạp:



# O(n + m)

# vì chỉ cần duyệt mỗi mảng một lần. 

# Thuật toán dựa trên nhận xét quan trọng:



# Nếu đã quyết định thứ tự là First → Second, thì ở nhóm First ta luôn nên chọn trò có thời điểm kết thúc sớm nhất.

# Vì kết thúc First càng sớm thì càng có cơ hội bắt đầu trò Second sớm hơn.

# Hàm earliestFinishTime

# Hàm này tính:



# First rides -> Second rides

# Ví dụ:



# earliestFinishTime(

#     landStartTime,

#     landDuration,

#     waterStartTime,

#     waterDuration

# )

# nghĩa là:



# Land -> Water

# Code có chú thích

from math import inf
def earliestFinishTime(firstStartTime, firstDuration,

                       secondStartTime, secondDuration):



    # Tìm thời điểm kết thúc sớm nhất của nhóm First

    earliest_first_end = inf



    for i, start in enumerate(firstStartTime):



        # thời điểm kết thúc ride thứ i

        end = start + firstDuration[i]



        # cập nhật kết thúc sớm nhất

        if earliest_first_end > end:

            earliest_first_end = end



    # Sau khi hoàn thành First,

    # thử ghép với từng ride của nhóm Second

    earliest_end = inf



    for i, start in enumerate(secondStartTime):



        # Nếu ride Second đã mở trước khi ta đến

        # thì bắt đầu ngay lúc earliest_first_end

        #

        # Nếu chưa mở

        # thì phải đợi đến start

        begin_second = max(start, earliest_first_end)



        # thời điểm hoàn thành cả hai ride

        end = begin_second + secondDuration[i]



        # lấy đáp án nhỏ nhất

        if earliest_end > end:

            earliest_end = end



    return earliest_end





class Solution:



    def earliestFinishTime(

        self,

        landStartTime,

        landDuration,

        waterStartTime,

        waterDuration

    ):



        # Trường hợp 1:

        # Land -> Water

        land_then_water = earliestFinishTime(

            landStartTime,

            landDuration,

            waterStartTime,

            waterDuration

        )



        # Trường hợp 2:

        # Water -> Land

        water_then_land = earliestFinishTime(

            waterStartTime,

            waterDuration,

            landStartTime,

            landDuration

        )



        # Chọn thời điểm hoàn thành sớm nhất

        return min(land_then_water, water_then_land)

# Minh họa

# landStartTime = [2, 8]

# landDuration  = [4, 1]



# waterStartTime = [6]

# waterDuration  = [3]

# Bước 1: Land -> Water

# Tìm land kết thúc sớm nhất:



# Ride 0: 2 + 4 = 6

# Ride 1: 8 + 1 = 9



# earliest_first_end = 6

# Bước 2: Ghép với Water

# Water:



# start = 6

# duration = 3

# Bắt đầu:



# max(6, 6) = 6

# Kết thúc:



# 6 + 3 = 9

# Land -> Water = 9

# Bước 3: Water -> Land

# Water kết thúc sớm nhất:



# 6 + 3 = 9

# Sau đó thử từng Land:



# Land 0:

# max(9,2)+4 = 13



# Land 1:

# max(9,8)+1 = 10

# Water -> Land = 10

# Kết quả

# min(9, 10) = 9

# Độ phức tạp

# Giả sử:



# n = số land rides

# m = số water rides

# Mỗi lần gọi earliestFinishTime:



# O(n + m)

# Gọi 2 lần:



# O(2(n+m))

# bỏ hằng số:



# O(n + m)

# Bộ nhớ:



# O(1)

# vì chỉ dùng vài biến phụ.