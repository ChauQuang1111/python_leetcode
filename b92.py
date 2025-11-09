# // 2169. Count Operations to Obtain Zero(09/11//2025)
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        res = 0  # Biến đếm tổng số lần trừ
        
        # Lặp đến khi một trong hai số bằng 0
        while num1 != 0 and num2 != 0:
            # Số lần có thể trừ num2 khỏi num1
            res += num1 // num2

            # Cập nhật num1 thành phần dư sau phép chia
            num1 %= num2

            # Hoán đổi hai số để tiếp tục (giống thuật toán Euclid)
            num1, num2 = num2, num1

        return res  # Trả về tổng số bước

# // Rất hay 👏 Bài **2169. Count Operations to Obtain Zero** là một bài **toán mô phỏng (simulation problem)** khá cơ bản nhưng dễ gây nhầm nếu không hiểu rõ quy tắc.
# Rất hay 👏 — mình sẽ giải thích **thuật toán của đoạn code này** chi tiết nhất có thể nhé:

# ---

# ### 🧩 Bài toán:

# > Cho hai số nguyên dương `num1` và `num2`.
# > Lặp lại thao tác sau cho đến khi **một trong hai số bằng 0**:
# >
# > * Nếu `num1 ≥ num2`, thay `num1 = num1 - num2`.
# > * Ngược lại, thay `num2 = num2 - num1`.
# >   Mỗi lần trừ được tính là **1 phép toán**.
# >   → Hỏi tổng số phép toán cần thực hiện.

# ---

# ### 🔢 Ví dụ trực quan:

# Giả sử `num1 = 10, num2 = 3`.

# Ta làm như sau:

# | Bước       | num1 | num2 | Thao tác   | Số lần trừ (res)  |
# | ---------- | ---- | ---- | ---------- | ----------------- |
# | 1          | 10   | 3    | 10 - 3 = 7 | 1                 |
# | 2          | 7    | 3    | 7 - 3 = 4  | 2                 |
# | 3          | 4    | 3    | 4 - 3 = 1  | 3                 |
# | 4          | 3    | 1    | 3 - 1 = 2  | 4                 |
# | 5          | 2    | 1    | 2 - 1 = 1  | 5                 |
# | 6          | 1    | 1    | 1 - 1 = 0  | 6                 |
# | ✅ Kết thúc | 0    | 1    | -          | Tổng cộng = **6** |

# ---

# ### 💡 Tối ưu hóa:

# Cách trên lặp đi lặp lại rất chậm nếu `num1` lớn.
# Ví dụ `num1 = 1000000`, `num2 = 1` → phải trừ 1 **một triệu lần** 😅

# Để nhanh hơn, ta nhận ra:

# * Mỗi lần trừ `num2` khỏi `num1` tương đương **một phép chia lấy phần nguyên**:

#   ```
#   num1 // num2  ← số lần có thể trừ
#   num1 % num2   ← phần còn lại sau khi trừ hết
#   ```
# * Sau đó, ta **hoán đổi** hai số lại, vì quy tắc lặp lại y hệt (giống **thuật toán Euclid** dùng để tính GCD).

# ---

# ### ⚙️ Cách hoạt động của code:

# ```java
# while (num1 != 0 && num2 != 0) {
#     res += num1 / num2;  // Số lần trừ num2 khỏi num1
#     num1 %= num2;        // Cập nhật num1 thành phần dư
#     // Hoán đổi 2 số để tiếp tục quá trình
#     int temp = num1;
#     num1 = num2;
    # num2 = temp;
# }
# ```

# * Mỗi vòng lặp làm tương đương **nhiều phép trừ một lúc**.
# * Lặp đến khi một trong hai số = 0 → dừng.

# ---

# ### 🧠 Tóm tắt ý tưởng:

# * Đây là **thuật toán Euclid mở rộng**.
# * Thay vì tính GCD, ta đếm **tổng số phép trừ** mà quá trình Euclid thực hiện.
# * Độ phức tạp: `O(log(min(num1, num2)))` — cực nhanh.

# ---

# 👉 **Kết luận:**
# Thuật toán dùng chia và phần dư để mô phỏng việc trừ dần số lớn hơn cho đến khi một số bằng 0,
# và tổng hợp tất cả số lần trừ này chính là đáp án.

# ---

# Bạn có muốn mình viết thêm **hàm main + chú thích từng dòng code Java** để bạn chạy và quan sát kết quả không?

# // Dưới đây là phần **giải thích chi tiết đề bài + ví dụ minh họa** 👇
# import java.util.Scanner;

# public class b93 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int num1 = sc.nextInt();

#         int num2 = sc.nextInt();

#         int result = countOperations(num1, num2);

#         // In kết quả
#         System.out.println(result);

#         sc.close();
#     }

#     public static int countOperations(int num1, int num2) {
#         int res = 0; // Biến đếm tổng số lần trừ

#         // Lặp đến khi 1 trong 2 số bằng 0
#         while (num1 != 0 && num2 != 0) {
#             // Số lần có thể trừ num2 khỏi num1
#             res += num1 / num2;

#             // Cập nhật num1 thành phần dư (sau khi trừ nhiều lần)
#             num1 %= num2;

#             // Hoán đổi vị trí để tiếp tục vòng lặp (giống Euclid)
#             int temp = num1;
#             num1 = num2;
#             num2 = temp;
#         }

#         return res; // Trả về tổng số lần trừ
#     }
# }

# // ---

# // ## 🧩 **Đề bài:**

# // Bạn được cho **hai số nguyên dương `num1` và `num2`**.

# // Mỗi **bước (operation)**, bạn thực hiện như sau:

# // * Nếu `num1 >= num2`, thì:

# // ```
# // num1 = num1 - num2
# // ```
# // * Ngược lại (tức là `num1 < num2`), thì:

# // ```
# // num2 = num2 - num1
# // ```

# // Bạn phải **lặp lại quá trình này cho đến khi ít nhất một trong hai số trở
# // thành 0**,
# // và **trả về số bước (operation)** đã thực hiện.

# // ---

# // ## 📘 **Yêu cầu:**

# // Viết hàm:

# // ```java
# // int countOperations(int num1, int num2);
# // ```

# // Trả về **số bước cần để ít nhất một số bằng 0**.

# // ---

# // ## 🧮 **Ví dụ minh họa:**

# // ### Ví dụ 1:

# // ```
# // Input: num1 = 2, num2 = 3
# // ```

# // **Quá trình:**

# // | Bước | num1 | num2 | Giải thích |
# // | ---- | ---- | ---- | ------------------------------ |
# // | 1 | 2 | 3 | num1 < num2 ⇒ num2 = 3 - 2 = 1 |
# // | 2 | 2 | 1 | num1 ≥ num2 ⇒ num1 = 2 - 1 = 1 |
# // | 3 | 1 | 1 | num1 ≥ num2 ⇒ num1 = 1 - 1 = 0 |

# // → Dừng lại (vì num1 = 0)

# // ✅ **Kết quả: 3 bước**

# // ---

# // ### Ví dụ 2:

# // ```
# // Input: num1 = 10, num2 = 10
# // ```

# // **Bước 1:**
# // num1 ≥ num2 ⇒ num1 = 10 - 10 = 0
# // → Dừng lại.

# // ✅ **Kết quả: 1 bước**

# // ---

# // ### Ví dụ 3:

# // ```
# // Input: num1 = 5, num2 = 1
# // ```

# // **Quá trình:**

# // | Bước | num1 | num2 | Giải thích |
# // | ---- | ---- | ---- | ------------------------------ |
# // | 1 | 5 | 1 | num1 ≥ num2 ⇒ num1 = 5 - 1 = 4 |
# // | 2 | 4 | 1 | num1 = 3 |
# // | 3 | 3 | 1 | num1 = 2 |
# // | 4 | 2 | 1 | num1 = 1 |
# // | 5 | 1 | 1 | num1 = 0 |

# // ✅ **Kết quả: 5 bước**

# // ---

# // ## 💡 **Nhận xét & Tối ưu:**

# // * Đây là **bài toán tương tự thuật toán Euclid tìm GCD**, nhưng thay vì chia
# // lấy dư, ta trừ liên tục.
# // * Có thể **tối ưu** bằng cách tính nhanh số lần trừ mỗi bước:

# // ```java
# // operations += num1 / num2;
# // num1 %= num2;
# // ```

# // (giống như dùng phép chia thay vì trừ từng lần).

# // ---

# // ## 🚀 **Tóm tắt ý tưởng:**

# // > Lặp lại: trừ số nhỏ hơn từ số lớn hơn
# // > → đếm số lần
# // > → dừng khi 1 trong 2 số = 0.

# // Rất hay 👍 — đoạn code này là phiên bản **tối ưu** của thuật toán “Count
# // Operations to Obtain Zero” (LeetCode 2169), dựa trên **thuật toán Euclid
# // (tính GCD)** nhưng thay vì chỉ tìm ước chung lớn nhất, nó **đếm số bước trừ**
# // cần thực hiện.

# // Cùng phân tích từng phần nhé 👇

# // ---

# // ### 🧩 Mục tiêu bài toán:

# // Bạn có hai số nguyên dương `num1` và `num2`.
# // Ở mỗi bước:

# // * Nếu `num1 >= num2` → trừ `num1 -= num2`
# // * Ngược lại → trừ `num2 -= num1`

# // Lặp lại cho đến khi **một trong hai số = 0**,
# // và yêu cầu đếm **tổng số lần trừ**.

# // ---

# // ### 💡 Ý tưởng tối ưu:

# // Thay vì **trừ từng lần một** (rất chậm nếu chênh lệch lớn),
# // ta nhận ra có thể **tính nhanh số lần trừ bằng phép chia**.

# // Ví dụ:

# // ```
# // num1 = 10, num2 = 3
# // 10 - 3 = 7
# // 7 - 3 = 4
# // 4 - 3 = 1 → (3 lần trừ)
# // ```

# // => 10 / 3 = 3 lần trừ, dư lại 10 % 3 = 1
# // Tức là chỉ cần **num1 / num2** bước trừ là đủ.

# // ---

# // ### 🔍 Phân tích từng dòng code:

# // ```java
# // public int countOperations(int num1, int num2) {
# // int res = 0; // Đếm tổng số lần trừ
# // ```

# // ---

# // ```java
# // while (num1 != 0 && num2 != 0) {
# // ```

# // 👉 Lặp cho đến khi **một trong hai số bằng 0**.

# // ---

# // ```java
# // res += num1 / num2;
# // num1 %= num2;
# // ```

# // * `num1 / num2`: số lần ta có thể trừ `num2` khỏi `num1`.
# // * `num1 %= num2`: phần dư sau khi trừ nhiều lần (tức là `num1` mới).

# // ---

# // ```java
# // int temp = num1;
# // num1 = num2;
# // num2 = temp;
# // ```

# // 👉 Đảo chỗ để đảm bảo **luôn trừ số lớn hơn cho số nhỏ hơn**
# // (giống như các bước trong thuật toán **Euclid**).

# // ---

# // ### 🧮 Ví dụ minh họa:

# // ```
# // num1 = 10, num2 = 3
# // ```

# // | Bước | num1 | num2 | num1/num2 | num1%num2 | res |
# // | ---- | ---- | ---- | --------- | --------- | --- |
# // | 1 | 10 | 3 | 3 | 1 | +3 |
# // | 2 | 3 | 1 | 3 | 0 | +3 |

# // ➡ Tổng cộng `res = 6` bước.

# // (Tức là: 10−3−3−3 = 1 → 3−1−1−1 = 0)

# // ---

# // ### 🧠 Tổng kết:

# // * Dựa trên **thuật toán Euclid**.
# // * Dùng phép **chia và chia lấy dư** để tính nhanh số lần trừ.
# // * Độ phức tạp: **O(log n)** (thay vì O(n) nếu trừ từng bước).

# // ---

# // Bạn có muốn mình thêm **phiên bản có Scanner và chú thích từng dòng** vào
# // code Java này không?
