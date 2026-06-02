# // // Bài “Earliest Finish Time for Land and Water Rides I” của LeetCode yêu cầu tìm thời điểm sớm nhất có thể hoàn thành 2 trò chơi, gồm:



# // // 1 trò thuộc nhóm Land rides (trò trên cạn)

# // // 1 trò thuộc nhóm Water rides (trò dưới nước)

# // // (LeetCode)



# // // Ý nghĩa các mảng

# // // landStartTime[i]

# // // Thời điểm sớm nhất trò land thứ i được mở.



# // // landDuration[i]

# // // Thời gian chơi trò land thứ i.



# // // waterStartTime[j]

# // // Thời điểm sớm nhất trò water thứ j được mở.



# // // waterDuration[j]

# // // Thời gian chơi trò water thứ j.

# // // Quy tắc

# // // Bạn phải chơi:



# // // Chính xác 1 trò land

# // // Chính xác 1 trò water

# // // Và có thể chọn thứ tự:



# // // Land -> Water

# // // hoặc

# // // Water -> Land

# // // Nếu trò thứ hai chưa mở cửa khi bạn chơi xong trò đầu tiên thì phải đợi.

# // // Ví dụ 1

# // // landStartTime = [2,8]

# // // landDuration  = [4,1]



# // // waterStartTime = [6]

# // // waterDuration  = [3]

# // // Chọn Land 0 -> Water 0

# // // Land 0:



# // // bắt đầu = 2

# // // kết thúc = 2 + 4 = 6

# // // Water 0 mở lúc:



# // // 6

# // // Nên chơi ngay:



# // // bắt đầu = 6

# // // kết thúc = 6 + 3 = 9

# // // Tổng thời gian hoàn thành:



# // // 9

# // // Chọn Water 0 -> Land 1

# // // Water 0:



# // // bắt đầu = 6

# // // kết thúc = 9

# // // Land 1 mở lúc:



# // // 8

# // // Nhưng lúc này đã là:



# // // 9

# // // Nên bắt đầu lúc:



# // // 9

# // // Kết thúc:



# // // 9 + 1 = 10

# // // Kết quả nhỏ nhất trong tất cả các cách là:



# // // 9

# // // Công thức tính

# // // Giả sử:



# // // Land i trước

# // // Water j sau

# // // Thời gian kết thúc land:



# // // endLand = landStartTime[i] + landDuration[i]

# // // Thời gian bắt đầu water:



# // // startWater = max(endLand, waterStartTime[j])

# // // (vì phải đợi cả 2 điều kiện:



# // // chơi xong land

# // // water đã mở)

# // // Thời gian hoàn thành:



# // // finish =

# // // max(endLand, waterStartTime[j])

# // // + waterDuration[j]

# // // Tương tự phải thử luôn trường hợp:



# // // Water -> Land

# // // Ý tưởng bài toán

# // // Vì:



# // // n, m <= 100

# // // nên có thể brute force:



# // // thử mọi land

# // // thử mọi water

# // // thử cả 2 thứ tự

# // // Tính thời gian hoàn thành và lấy nhỏ nhất.

# // // Độ phức tạp:



# // // O(n * m)

# // // với 100 * 100 = 10000, hoàn toàn đủ nhanh. (LeetCode)


# // Đầu tiên, hãy hiểu ý tưởng của hàm solve().



# // Hàm solve()

# // private int solve(

# //     int[] start1,

# //     int[] duration1,

# //     int[] start2,

# //     int[] duration2

# // )

# // Hàm này giả sử:



# // Nhóm 1 chơi trước

# // → Nhóm 2 chơi sau

# // Ví dụ:



# // solve(landStartTime, landDuration,

# //       waterStartTime, waterDuration)

# // nghĩa là:



# // Land → Water

# // Bước 1: Tìm thời gian kết thúc sớm nhất của trò đầu tiên

# // int finish1 = Integer.MAX_VALUE;



# // for (int i = 0; i < start1.length; i++) {

# //     finish1 = Math.min(

# //         finish1,

# //         start1[i] + duration1[i]

# //     );

# // }

# // Ý nghĩa

# // Tính:



# // finish1 = min(start1[i] + duration1[i])

# // Tức là tìm trò trong nhóm 1 có thời gian kết thúc sớm nhất.

# // Ví dụ:



# // start1    = [2, 8]

# // duration1 = [4, 1]

# // Ta có:



# // Trò 0: 2 + 4 = 6

# // Trò 1: 8 + 1 = 9

# // nên



# // finish1 = 6

# // Bước 2: Chọn trò thứ hai

# // int finish2 = Integer.MAX_VALUE;

# // Duyệt mọi trò của nhóm 2:



# // for (int i = 0; i < start2.length; i++)

# // Thời điểm bắt đầu trò thứ hai:



# // Math.max(start2[i], finish1)

# // Vì:



# // trò thứ hai chỉ mở từ start2[i]

# // phải đợi chơi xong trò đầu tiên tại finish1

# // nên lấy lớn hơn trong hai thời điểm.

# // Ví dụ



# // finish1 = 6



# // waterStart = 10

# // duration = 3

# // thì



# // bắt đầu water = max(10,6)=10



# // kết thúc = 10+3=13

# // Đoạn code:



# // finish2 = Math.min(

# //     finish2,

# //     Math.max(start2[i], finish1)

# //         + duration2[i]

# // );

# // nghĩa là:



# // Thử tất cả các trò nhóm 2

# // Lấy trò cho thời gian hoàn thành nhỏ nhất

# // Trả về

# // return finish2;

# // Đây là thời gian hoàn thành sớm nhất nếu:



# // Nhóm 1 → Nhóm 2

# // Hàm chính

# // int land_water = solve(

# //     landStartTime,

# //     landDuration,

# //     waterStartTime,

# //     waterDuration

# // );

# // Tính:



# // Land → Water

# // int water_land = solve(

# //     waterStartTime,

# //     waterDuration,

# //     landStartTime,

# //     landDuration

# // );

# // Tính:



# // Water → Land

# // return Math.min(

# //     land_water,

# //     water_land

# // );

# // Lấy kết quả tốt hơn.

# // Ví dụ chạy tay

# // landStart    = [2,8]

# // landDuration = [4,1]



# // waterStart   = [6]

# // waterDuration= [3]

# // Land → Water

# // Land kết thúc:



# // 2+4=6

# // 8+1=9



# // finish1=6

# // Water:



# // start=max(6,6)=6



# // finish=6+3=9

# // Kết quả:



# // land_water=9

# // Water → Land

# // Water:



# // 6+3=9



# // finish1=9

# // Land:



# // Land0:

# // max(2,9)+4=13



# // Land1:

# // max(8,9)+1=10

# // nhỏ nhất:



# // water_land=10

# // Kết quả cuối:



# // min(9,10)=9

# // Điểm mấu chốt của thuật toán

# // Tác giả nhận ra rằng:



# // Với trò chơi thứ nhất, chỉ cần quan tâm trò nào kết thúc sớm nhất.

# // Sau khi biết thời điểm kết thúc sớm nhất đó (finish1), chỉ việc chọn trò thứ hai sao cho thời gian hoàn thành nhỏ nhất.

# // Do đó không cần thử mọi cặp (land, water) như brute force O(n*m), mà chỉ cần:



# // Tìm finish1: O(n)

# // Tìm finish2: O(m)



# // => O(n+m)

# // rất tối ưu.



# import java.util.*;

# public class b252 {
#  static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int n = sc.nextInt();

#         int[] landStartTime = new int[n];
#         int[] landDuration = new int[n];

#         // Nhập thời điểm mở của các trò Land
#         for (int i = 0; i < n; i++) {
#             landStartTime[i] = sc.nextInt();
#         }

#         // Nhập thời gian chơi các trò Land
#         for (int i = 0; i < n; i++) {
#             landDuration[i] = sc.nextInt();
#         }

#         // Nhập số lượng trò Water
#         int m = sc.nextInt();

#         int[] waterStartTime = new int[m];
#         int[] waterDuration = new int[m];

#         // Nhập thời điểm mở của các trò Water
#         for (int i = 0; i < m; i++) {
#             waterStartTime[i] = sc.nextInt();
#         }

#         // Nhập thời gian chơi các trò Water
#         for (int i = 0; i < m; i++) {
#             waterDuration[i] = sc.nextInt();
#         }

#         // Tính kết quả
#         int answer = earliestFinishTime(
#                 landStartTime,
#                 landDuration,
#                 waterStartTime,
#                 waterDuration);

#         System.out.println(answer);

#         sc.close();
#     }
#  /**
#      * Hàm tính thời gian hoàn thành sớm nhất khi:
#      * Nhóm 1 -> Nhóm 2
#      */
#     public static int solve(
#             int[] start1,
#             int[] duration1,
#             int[] start2,
#             int[] duration2) {

#         // Thời gian kết thúc sớm nhất của một trò trong nhóm 1
#         int finish1 = Integer.MAX_VALUE;

#         for (int i = 0; i < start1.length; i++) {

#             // Thời điểm kết thúc trò i của nhóm 1
#             int finishTime = start1[i] + duration1[i];

#             // Lưu lại thời gian kết thúc nhỏ nhất
#             finish1 = Math.min(finish1, finishTime);
#         }

#         // Thời gian hoàn thành sớm nhất sau khi chơi thêm nhóm 2
#         int finish2 = Integer.MAX_VALUE;

#         for (int i = 0; i < start2.length; i++) {

#             // Chỉ có thể bắt đầu trò thứ 2 khi:
#             // 1. Trò đó đã mở cửa
#             // 2. Đã chơi xong trò đầu tiên
#             int startTime = Math.max(start2[i], finish1);

# #             // Thời gian kết thúc trò thứ 2
# #             int finishTime = startTime + duration2[i];

# #             // Lấy thời gian hoàn thành nhỏ nhất
# #             finish2 = Math.min(finish2, finishTime);
# #         }

# #         return finish2;
# #     }

# #     public static int earliestFinishTime(
# #             int[] landStartTime,
# #             int[] landDuration,
# #             int[] waterStartTime,
# #             int[] waterDuration) {

# #         // Trường hợp Land -> Water
# #         int landWater = solve(
# #                 landStartTime,
# #                 landDuration,
# #                 waterStartTime,
# #                 waterDuration);

# #         // Trường hợp Water -> Land
# #         int waterLand = solve(
# #                 waterStartTime,
# #                 waterDuration,
# #                 landStartTime,
# #                 landDuration);

# #         // Chọn kết quả nhỏ nhất
# #         return Math.min(landWater, waterLand);
# #     }

# # }


# Đây là một lời giải tối ưu O(n + m).

# Ý tưởng chính:



# Nếu chơi Land → Water, ta chỉ cần biết trò Land nào kết thúc sớm nhất.

# Sau đó xét từng trò Water để tìm thời gian hoàn thành nhỏ nhất.

# Tương tự cho Water → Land.

# Code có chú thích

class Solution:

    def earliestFinishTime(

        self,

        landStartTime,

        landDuration,

        waterStartTime,

        waterDuration

    ):



        # ==================================================

        # BƯỚC 1: Tìm thời gian kết thúc sớm nhất của 1 trò Land

        # finish = start + duration

        # ==================================================

        fast_land_time = min(

            [s + d for s, d in zip(landStartTime, landDuration)]

        )



        # ==================================================

        # BƯỚC 2: Sau khi chơi xong Land sớm nhất,

        # tìm thời gian hoàn thành nhỏ nhất khi chơi Water

        #

        # Nếu Water mở sau thời điểm finish_land:

        #     bắt đầu tại s

        #     kết thúc = s + d

        #

        # Nếu Water đã mở trước đó:

        #     phải đợi finish_land

        #     kết thúc = finish_land + d

        # ==================================================

        fast_land_and_water_time = min(

            [

                s + d

                if s >= fast_land_time

                else fast_land_time + d

                for s, d in zip(waterStartTime, waterDuration)

            ]

        )



        # ==================================================

        # BƯỚC 3: Tìm thời gian kết thúc sớm nhất của 1 trò Water

        # ==================================================

        fast_water_time = min(

            [s + d for s, d in zip(waterStartTime, waterDuration)]

        )



        # ==================================================

        # BƯỚC 4: Sau khi chơi xong Water sớm nhất,

        # tìm thời gian hoàn thành nhỏ nhất khi chơi Land

        # ==================================================

        fast_water_and_land_time = min(

            [

                s + d

                if s >= fast_water_time

                else fast_water_time + d

                for s, d in zip(landStartTime, landDuration)

            ]

        )



        # ==================================================

        # So sánh:

        # Land -> Water

        # Water -> Land

        # ==================================================

        return min(

            fast_water_and_land_time,

            fast_land_and_water_time

        )

# Ví dụ chạy tay

# landStartTime = [2, 8]

# landDuration  = [4, 1]



# waterStartTime = [6]

# waterDuration  = [3]

# Tìm Land kết thúc sớm nhất

# 2 + 4 = 6

# 8 + 1 = 9

# fast_land_time = 6

# Land → Water

# Water:



# start = 6

# duration = 3

# Do:



# 6 >= 6

# nên:



# finish = 6 + 3 = 9

# fast_land_and_water_time = 9

# Tìm Water kết thúc sớm nhất

# 6 + 3 = 9

# fast_water_time = 9

# Water → Land

# Land 0

# start = 2 < 9



# finish = 9 + 4 = 13

# Land 1

# start = 8 < 9



# finish = 9 + 1 = 10

# fast_water_and_land_time = 10

# Kết quả

# min(9, 10) = 9

# Tại sao chỉ cần trò kết thúc sớm nhất?

# Giả sử có hai trò Land:



# A kết thúc lúc 6

# B kết thúc lúc 10

# Nếu chọn B thì:



# bắt đầu trò Water không thể sớm hơn khi chọn A

# vì mọi thời điểm bắt đầu Water đều phụ thuộc:



# max(waterStartTime, finishLand)

# mà:



# finishLand(A) <= finishLand(B)

# nên chọn trò Land kết thúc sớm nhất luôn tốt nhất hoặc bằng mọi lựa chọn khác.

# Do đó không cần thử mọi cặp (Land, Water).

# Độ phức tạp

# Giả sử:



# n = số trò Land

# m = số trò Water

# Tìm fast_land_time: O(n)

# Tìm fast_land_and_water_time: O(m)

# Tìm fast_water_time: O(m)

# Tìm fast_water_and_land_time: O(n)

# Tổng:



# O(n + m)

# Bộ nhớ phụ:



# O(1)

# (nếu thay list comprehension bằng generator expression thì không tạo danh sách tạm).