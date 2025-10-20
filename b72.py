# // 2011. Final Value of Variable After Performing Operations(20/10/2025)
from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0  # Giá trị ban đầu của biến X là 0

        # Duyệt qua từng thao tác trong danh sách operations
        for op in operations:
            # Nếu chuỗi chứa "++", tăng X lên 1
            if "++" in op:
                X += 1
            else:  # Ngược lại là "--", giảm X đi 1
                X -= 1

        return X  # Trả về giá trị cuối cùng của X










# import java.util.*;

# public class b73 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int n = sc.nextInt();
#         sc.nextLine();

#         String[] operations = new String[n];
#         for (int i = 0; i < n; i++) {
#             operations[i] = sc.nextLine().trim();
#         }

#         int result = finalValueAfterOperations(operations);

#         System.out.println(result);

#         sc.close();
#     }

#     public static int finalValueAfterOperations(String[] operations) {
#         int X = 0; // Khởi tạo giá trị ban đầu của X là 0

#         // Duyệt qua từng chuỗi trong mảng operations
#         for (String op : operations) {
#             // Nếu chuỗi chứa "++" → tăng X lên 1
#             if (op.contains("++")) {
#                 X++;
#             } else { // Ngược lại là "--" → giảm X đi 1
#                 X--;
#             }
#         }

#         // Trả về giá trị cuối cùng của X sau tất cả các thao tác
#         return X;
#     }
# }

# // Tất nhiên😊—mình sẽ giải thích**thuật toán trong code**này một cách thật dễ
# // hiểu👇

# // ---

# // ##🧠**Mục tiêu của bài**

# // Tính**giá trị cuối cùng của biến`X`**sau khi thực hiện một loạt thao tác
# // tăng(`++`)hoặc giảm(`--`)theo danh sách`operations`.Ban đầu:`X=0`.

# // ---

# // ##🔍**Giải thích từng dòng trong code**

# // ```java
# // class Solution {
# // public int finalValueAfterOperations(String[] operations) {
# // int X = 0;
# // ```

# // * Khởi tạo biến `X = 0`
# // → Đây là giá trị ban đầu mà đề bài cho.

# // ---

# // ```java
# // for (String op : operations) {
# // ```

# // * Duyệt qua **từng chuỗi** trong mảng `operations`.
# // Mỗi chuỗi `op` là một thao tác, ví dụ `"++X"`, `"X++"`, `"--X"`, `"X--"`.

# // ---

# // ```java
# // if (op.contains("++")) {
# // X++;
# // } else {
# // X--;
# // }
# // ```

# // * Ở đây, nếu chuỗi `op` **chứa “++”**, có nghĩa là đây là **thao tác tăng**
# // → ta thực hiện `X++` (tăng giá trị X lên 1).

# // * Ngược lại, nếu không chứa `"++"`, thì chắc chắn là `"--"`
# // → ta thực hiện `X--` (giảm giá trị X đi 1).

# // ✅ Cách này **đơn giản và hiệu quả**, vì ta chỉ cần kiểm tra `"++"` thay vì so
# // sánh toàn bộ chuỗi.

# // ---

# // ```java
# // return X;
# // ```

# // * Sau khi duyệt hết tất cả thao tác, trả về **giá trị cuối cùng của X**.

# // ---

# // ## ⚙️ **Độ phức tạp**

# // * **Thời gian:** O(n), với `n` là số phần tử trong mảng `operations`.
# // → Mỗi thao tác chỉ cần kiểm tra chuỗi `"++"` đúng 1 lần.
# // * **Bộ nhớ:** O(1) — chỉ dùng 1 biến `X`.

# // ---

# // ## 🎯 **Ví dụ minh họa**

# // Input:

# // ```java
# // operations = ["--X", "X++", "X++"];
# // ```

# // Bước thực hiện:

# // | Thao tác | Trước | Sau |
# // | -------- | ----- | --- |
# // | `--X` | 0 | -1 |
# // | `X++` | -1 | 0 |
# // | `X++` | 0 | 1 |

# // 👉 **Kết quả cuối cùng:** `X = 1`

# // ---

# // ### ✅ **Tóm tắt ý tưởng**

# // > Thuật toán duyệt từng thao tác trong mảng.
# // > Nếu thao tác là tăng (`++`) → cộng 1.
# // > Nếu thao tác là giảm (`--`) → trừ 1.
# // > Cuối cùng trả về kết quả.

# // ---


