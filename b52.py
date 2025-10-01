#  // 1518. Water Bottles(01/10/2025)

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles  # tổng số chai uống được ban đầu
        empty = numBottles  # số vỏ chai còn lại sau khi uống

        # khi còn đủ vỏ để đổi
        while empty >= numExchange:
            newBottles = empty // numExchange   # số chai mới đổi được
            total += newBottles                 # cộng thêm số chai mới vào tổng
            empty = empty % numExchange + newBottles  # vỏ dư + vỏ từ chai mới

        return total



# import java.util.Scanner;

# class b53 {
#     public static void main(String[] args) {
#         Scanner sc = new Scanner(System.in);

#         // Nhập số chai nước ban đầu
#         System.out.print("Nhập số chai ban đầu: ");
#         int numBottles = sc.nextInt();

#         // Nhập số vỏ cần để đổi 1 chai
#         System.out.print("Nhập số vỏ để đổi 1 chai: ");
#         int numExchange = sc.nextInt();

#         int result = numWaterBottles(numBottles, numExchange);

#         System.out.println("Tổng số chai uống được: " + result);

#         sc.close();
#     }

#     public static int numWaterBottles(int numBottles, int numExchange) {
#         int total = numBottles; // số chai uống được ban đầu
#         int empty = numBottles; // số vỏ chai hiện có sau khi uống

#         // khi còn đủ vỏ để đổi
#         while (empty >= numExchange) {
#             int newBottles = empty / numExchange; // số chai mới đổi được
#             total += newBottles; // cộng thêm vào tổng số chai đã uống
#             empty = empty % numExchange + newBottles; // vỏ còn dư + vỏ từ chai mới
#         }

#         return total;
#     }
# }

# // Ok 👍 mình sẽ giải thích thuật toán trong code bạn đưa.

# // ---

# // ### **Mục tiêu bài toán**

# // Bạn có `numBottles` chai nước ban đầu. Uống hết chúng → có `numBottles` cái
# // vỏ.
# // Cứ mỗi `numExchange` cái vỏ thì đổi được **1 chai nước mới**.
# // Hỏi: tổng cộng bạn có thể uống được bao nhiêu chai?

# // ---

# // ### **Thuật toán trong code**

# // ```java
# // int total = numBottles; // tổng số chai uống được ban đầu
# // int empty = numBottles; // số vỏ chai sau khi uống hết
# // ```

# // * Lúc đầu bạn uống hết `numBottles` chai → tổng = `numBottles`.
# // * Sau đó bạn còn `numBottles` cái vỏ.

# // ---

# // ```java
# // while (empty >= numExchange) {
# // int newBottles = empty / numExchange;
# // total += newBottles;
# // empty = empty % numExchange + newBottles;
# // }
# // ```

# // * **Vòng lặp**: chừng nào số vỏ `empty` còn đủ để đổi (`>= numExchange`) thì
# // tiếp tục.
# // * `newBottles = empty / numExchange`: số chai mới đổi được.
# // * `total += newBottles`: cộng thêm số chai mới uống vào tổng.
# // * `empty = empty % numExchange + newBottles`:

# // * `empty % numExchange`: số vỏ **dư lại** không đủ để đổi.
# // * `+ newBottles`: số vỏ mới có được sau khi uống các chai vừa đổi.

# // 👉 Sau mỗi vòng, bạn lại có một lượng vỏ mới, tiếp tục đổi nếu đủ.

# // ---

# // ### **Khi nào dừng?**

# // * Khi `empty < numExchange` → không đủ vỏ để đổi thêm chai mới → thoát vòng
# // lặp.

# // ---

# // ### **Ví dụ chạy (numBottles=9, numExchange=3)**

# // * B1: `total=9`, `empty=9`.
# // * B2: `newBottles=9/3=3`, `total=12`, `empty=3+0=3`.
# // * B3: `newBottles=3/3=1`, `total=13`, `empty=1`.
# // * Dừng vì `1 < 3`.
# // 👉 Kết quả: **13** chai.

# // ---

# // ### **Độ phức tạp**

# // * Vòng lặp chạy mỗi lần giảm số vỏ, nên tối đa chạy `O(numBottles)` lần.
# // * Không dùng thêm cấu trúc dữ liệu → **O(1) bộ nhớ**.

# // ---

# // Bạn có muốn mình rút gọn thuật toán này thành **công thức toán học 1 dòng**
# // để không cần vòng `while` không?
