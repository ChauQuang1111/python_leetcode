# // 166. Fraction to Recurring Decimal(24/09/2025)
# Rất hay 👌 mình sẽ giải thích **thuật toán** trước, rồi thêm **chú thích chi tiết trong code** để bạn dễ hiểu.

# ---

# ## 🚀 Ý tưởng thuật toán (LeetCode 166. Fraction to Recurring Decimal)

# 1. **Xử lý dấu**:

#    * Nếu tử và mẫu khác dấu → kết quả âm.
#    * Dùng XOR `(numerator < 0) ^ (denominator < 0)` để kiểm tra.

# 2. **Chia lấy phần nguyên**:

#    * `numerator // denominator` → phần nguyên.
#    * `remainder = numerator % denominator` → dư.

# 3. **Nếu chia hết** (`remainder == 0`) → không có phần thập phân → trả kết quả luôn.

# 4. **Xử lý phần thập phân**:

#    * Dùng một **HashMap `seen`** để lưu: `remainder → vị trí trong chuỗi`.
#    * Mỗi vòng lặp:

#      * Nhân `remainder *= 10`.
#      * Lấy `remainder // denominator` làm một chữ số thập phân.
#      * Cập nhật `remainder %= denominator`.
#    * Nếu tại một thời điểm `remainder` đã thấy trong `seen` → nghĩa là chu kỳ bắt đầu → chèn dấu `"("` tại vị trí trước đó và thêm `")"` ở cuối.

# 5. **Ghép lại thành chuỗi kết quả**.

# ---

# ## 📝 Code Python có chú thích

# ```python
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Trường hợp đặc biệt: tử số = 0 thì kết quả chắc chắn là "0"
        if numerator == 0:
            return "0"

        result = []  # danh sách để xây chuỗi kết quả

        # Kiểm tra dấu: nếu tử và mẫu trái dấu thì thêm dấu "-"
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        # Lấy trị tuyệt đối để tính toán dễ dàng
        numerator, denominator = abs(numerator), abs(denominator)

        # Phần nguyên của phép chia
        result.append(str(numerator // denominator))
        remainder = numerator % denominator  # lấy dư

        # Nếu chia hết thì không có phần thập phân → trả kết quả luôn
        if remainder == 0:
            return "".join(result)

        # Nếu còn dư → chắc chắn có phần thập phân
        result.append(".")

        # HashMap lưu: remainder → vị trí trong kết quả (để phát hiện chu kỳ)
        seen = {}

        # Lặp đến khi dư = 0 (chấm dứt) hoặc dư lặp lại (chu kỳ)
        while remainder != 0:
            # Nếu dư đã xuất hiện trước đó → tìm thấy chu kỳ
            if remainder in seen:
                idx = seen[remainder]  # vị trí bắt đầu của chu kỳ
                result.insert(idx, "(")  # chèn "(" vào trước
                result.append(")")      # chèn ")" vào sau
                break

            # Lưu vị trí hiện tại của dư
            seen[remainder] = len(result)

            # Tiếp tục chia
            remainder *= 10
            result.append(str(remainder // denominator))  # thêm 1 chữ số thập phân
            remainder %= denominator  # cập nhật dư mới

        # Nối danh sách thành chuỗi kết quả
        return "".join(result)
# ```

# ---

# ## 🔎 Ví dụ minh họa

# * `numerator = 2, denominator = 3`

#   * `2 ÷ 3 = 0`, dư `2`
#   * Nhân `2*10 = 20`, `20 ÷ 3 = 6`, dư `2` → dư lặp lại
#   * → kết quả `"0.(6)"`

# * `numerator = 1, denominator = 2`

#   * `1 ÷ 2 = 0`, dư `1`
#   * Nhân `1*10 = 10`, `10 ÷ 2 = 5`, dư `0` → hết
#   * → kết quả `"0.5"`

# ---

# 👉 Bạn có muốn mình viết thêm **hàm `main` (Python) để nhập `numerator, denominator` rồi gọi hàm trên** không?

# import java.util.*;

# class b46 {

#     // Hàm main test với Scanner
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {

#         int numerator = sc.nextInt();

#         int denominator = sc.nextInt();

#         String result = fractionToDecimal(numerator, denominator);

#         System.out.println(result);

#         sc.close();
#     }

#     public static String fractionToDecimal(int numerator, int denominator) {
#         // B1: Convert sang long để tránh tràn số
#         long lnum = numerator, lden = denominator;

#         // B2: Nếu tử số = 0 → kết quả là "0"
#         if (lnum == 0) {
#             return "0";
#         }

#         // B3: Nếu chia hết → trả về số nguyên
#         if (lnum % lden == 0) {
#             return Long.toString(lnum / lden);
#         }

#         // B4: StringBuilder để xây kết quả
#         StringBuilder number = new StringBuilder();

#         // B5: Xử lý dấu (chỉ âm nếu đúng 1 số âm)
#         if ((lden < 0) ^ (lnum < 0)) {
#             number.append('-');
#         }

#         // B6: Lấy trị tuyệt đối tử và mẫu
#         lnum = Math.abs(lnum);
#         lden = Math.abs(lden);

#         // B7: Lấy phần nguyên
#         number.append(lnum / lden);
#         number.append('.'); // thêm dấu thập phân

#         // B8: Rút gọn phân số bằng GCD
#         long GCD = gcd(lnum, lden);
#         lnum /= GCD;
#         lden /= GCD;

#         // B9: Lấy phần dư ban đầu để bắt đầu chia tiếp
#         lnum %= lden;
#         lnum *= 10;

#         // B10: Kiểm tra mẫu chỉ có 2 và 5 → số thập phân hữu hạn
#         int twos = 0, fives = 0;
#         long temp = lden;

#         while (temp % 2 == 0) {
#             twos++;
#             temp /= 2;
#         }
#         while (temp % 5 == 0) {
#             fives++;
#             temp /= 5;
#         }

#         // B11: Nếu mẫu chỉ có 2 và/hoặc 5
#         if (temp == 1) {
#             while (lnum != 0) {
#                 number.append(lnum / lden);
#                 lnum = (lnum % lden) * 10;
#             }
#         } else {
#             // B12: Xử lý phần không lặp (do 2 và 5)
#             int nonRepLen = Math.max(twos, fives);
#             for (int i = 0; i < nonRepLen; i++) {
#                 number.append(lnum / lden);
#                 lnum = (lnum % lden) * 10;
#             }

#             // B13: Phát hiện chu kỳ bằng remainder
#             long initRem = lnum;
#             StringBuilder repeating = new StringBuilder();

#             do {
#                 repeating.append(lnum / lden);
#                 lnum = (lnum % lden) * 10;
#             } while (lnum != initRem);

#             // B14: Thêm ngoặc cho phần lặp
#             number.append('(').append(repeating.toString()).append(')');
#         }

#         // B15: Trả về kết quả cuối
#         return number.toString();
#     }

#     // Hàm GCD (Ước chung lớn nhất)
#     public static long gcd(long a, long b) {
#         return (b == 0) ? a : gcd(b, a % b);
#     }
# }

# // Rất hay 👍 bạn đã viết một phiên bản giải khá chi tiết cho **166. Fraction to
# // Recurring Decimal**.
# // Mình sẽ giải thích từng **bước trong thuật toán** của bạn nhé:

# // ---

# // ## 📌 Ý tưởng chính

# // Bài toán:

# // * Cho `numerator` (tử số) và `denominator` (mẫu số).
# // * Trả về chuỗi biểu diễn phân số dạng số thập phân.
# // * Nếu phần thập phân lặp lại vô hạn → phải đặt trong `(...)`.
# // * Ví dụ:

# // * `1/2 = "0.5"` (kết thúc, vì mẫu chỉ chứa thừa số 2).
# // * `1/3 = "0.(3)"` (chu kỳ vô hạn).
# // * `4/333 = "0.(012)"`.

# // ---

# // ## 📌 Giải thích code theo các bước

# // ### **Bước 1 - 3: Trường hợp đặc biệt**

# // ```java
# // if (lnum == 0) return "0";
# // if (lnum % lden == 0) return Long.toString(lnum / lden);
# // ```

# // 👉 Nếu tử số = 0 thì kết quả là `"0"`.
# // 👉 Nếu chia hết thì trả về số nguyên luôn.

# // ---

# // ### **Bước 5 - 7: Xử lý dấu và phần nguyên**

# // ```java
# // if ((lden < 0) ^ (lnum < 0)) number.append('-');
# // lnum = Math.abs(lnum);
# // lden = Math.abs(lden);

# // number.append(lnum / lden);
# // number.append('.');
# // ```

# // 👉 Dùng XOR `^` để xét dấu: chỉ một số âm → kết quả âm.
# // 👉 Lấy phần nguyên (`lnum / lden`), thêm dấu `.` để bắt đầu phần thập phân.

# // ---

# // ### **Bước 8 - 9: Rút gọn phân số và lấy phần dư**

# // ```java
# // long GCD = gcd(lnum, lden);
# // lnum /= GCD;
# // lden /= GCD;

# // lnum %= lden; // phần dư
# // lnum *= 10; // chuẩn bị chia tiếp
# // ```

# // 👉 Rút gọn tử và mẫu để đơn giản hơn.
# // 👉 Sau đó tính phần dư ban đầu để bắt đầu chia thập phân.

# // ---

# // ### **Bước 10 - 11: Kiểm tra số thập phân hữu hạn**

# // ```java
# // while (temp % 2 == 0) { twos++; temp /= 2; }
# // while (temp % 5 == 0) { fives++; temp /= 5; }
# // ```

# // 👉 Nếu mẫu chỉ có thừa số 2 và/hoặc 5 → số thập phân **kết thúc**.
# // Ví dụ:

# // * `1/2 = 0.5`
# // * `1/8 = 0.125`
# // * `1/20 = 0.05`

# // Khi đó chỉ cần chia hết phần dư và nối kết quả.

# // ---

# // ### **Bước 12 - 14: Xử lý số thập phân vô hạn tuần hoàn**

# // Nếu mẫu có thừa số khác 2,5 → chắc chắn có chu kỳ.
# // Ví dụ:

# // * `1/3 = 0.(3)`
# // * `1/6 = 0.1(6)`

# // 1. **Lấy phần không lặp** (do ảnh hưởng của 2 và 5):

# // ```java
# // int nonRepLen = Math.max(twos, fives);
# // for (int i = 0; i < nonRepLen; i++) {
# // number.append(lnum / lden);
# // lnum = (lnum % lden) * 10;
# // }
# // ```

# // 2. **Dùng remainder (phần dư) để phát hiện chu kỳ**:

# // ```java
# // long initRem = lnum;
# // StringBuilder repeating = new StringBuilder();

# // do {
# // repeating.append(lnum / lden);
# // lnum = (lnum % lden) * 10;
# // } while (lnum != initRem);
# // ```

# // 👉 Khi remainder lặp lại → bắt đầu chu kỳ.

# // 3. **Thêm dấu ngoặc `()` vào phần lặp**:

# // ```java
# // number.append('(').append(repeating.toString()).append(')');
# // ```

# // ---

# // ### **Bước 15: Trả về kết quả**

# // ```java
# // return number.toString();
# // ```

# // ---

# // ## 📌 Ví dụ minh họa

# // ### Ví dụ 1: `1/2`

# // * GCD(1,2)=1 → rút gọn.
# // * Mẫu = 2 → chỉ chứa thừa số 2 → số hữu hạn.
# // * Kết quả: `"0.5"` ✅

# // ---

# // ### Ví dụ 2: `1/3`

# // * GCD(1,3)=1.
# // * Mẫu = 3 → có thừa số khác 2,5 → vô hạn tuần hoàn.
# // * Chia: `1/3 = 0.333...`
# // * remainder lặp lại → phát hiện chu kỳ `"3"`.
# // * Kết quả: `"0.(3)"` ✅

# // ---

# // ### Ví dụ 3: `4/333`

# // * GCD(4,333)=1.
# // * Mẫu = 333 → có thừa số khác 2,5.
# // * Long division:

# // * `40 / 333 = 0` remainder = 40
# // * `400 / 333 = 1` remainder = 67
# // * `670 / 333 = 2` remainder = 4
# // * Quay lại remainder = 40 → phát hiện chu kỳ `(012)`
# // * Kết quả: `"0.(012)"` ✅

# // ---

# // 👉 Thuật toán của bạn phức tạp hơn bản chuẩn của LeetCode (dùng `HashMap` lưu
# // remainder). Nhưng nó vẫn **hoạt động đúng**:

# // * Kiểm tra mẫu → quyết định hữu hạn hay vô hạn.
# // * Nếu vô hạn → tìm chu kỳ bằng remainder.

# // ---

# // Bạn có muốn mình viết lại một **phiên bản rút gọn hơn (dùng HashMap)** để dễ
# // hiểu hơn không?

# // Ok 👍, mình giải thích đề **LeetCode 166: Fraction to Recurring Decimal** cho
# // bạn nha:

# // ---

# // ### 📌 Đề bài:

# // Bạn được cho **hai số nguyên** `numerator` (tử số) và `denominator` (mẫu số).
# // Hãy trả về **kết quả của phép chia** dưới dạng **chuỗi thập phân**.

# // * Nếu kết quả là số thập phân **hữu hạn** → trả về bình thường.
# // * Nếu kết quả là số thập phân **vô hạn tuần hoàn** → đặt phần lặp lại trong
# // **ngoặc tròn**.

# // ---

# // ### 📌 Ví dụ:

# // 1.

# // ```
# // Input: numerator = 1, denominator = 2
# // Output: "0.5"
# // ```

# // Giải thích: `1 ÷ 2 = 0.5` (số thập phân hữu hạn).

# // ---

# // 2.

# // ```
# // Input: numerator = 2, denominator = 3
# // Output: "0.(6)"
# // ```

# // Giải thích: `2 ÷ 3 = 0.666...`, số `6` lặp lại vô hạn → viết thành `"0.(6)"`.

# // ---

# // 3.

# // ```
# // Input: numerator = 4, denominator = 333
# // Output: "0.(012)"
# // ```

# // Giải thích: `4 ÷ 333 = 0.012012012...`, chuỗi `"012"` lặp lại vô hạn →
# // `"0.(012)"`.

# // ---

# // 4.

# // ```
# // Input: numerator = 1, denominator = 5
# // Output: "0.2"
# // ```

# // Giải thích: `1 ÷ 5 = 0.2` (số thập phân hữu hạn).

# // ---

# // ### 📌 Ý chính của bài toán:

# // 1. Trả về kết quả phép chia dưới dạng chuỗi.
# // 2. Nếu phần thập phân lặp lại, phải tìm được **chu kỳ lặp** và đặt nó trong
# // ngoặc.
# // 3. Xử lý được cả số âm.
# // 4. Xử lý mẫu số chia hết hoặc không chia hết.

# // ---

# // 👉 Nói ngắn gọn:

# // * Đây là một bài toán mô phỏng phép chia dài (long division).
# // * Dùng **hashmap** để lưu lại phần dư (remainder) tại mỗi bước chia.
# // * Nếu một remainder lặp lại → từ đó trở đi số sẽ lặp lại vô hạn.

# // ---

# // Bạn có muốn mình viết **thuật toán step-by-step bằng ví dụ `2/3`** để thấy
# // cách tìm được phần `(6)` không?
