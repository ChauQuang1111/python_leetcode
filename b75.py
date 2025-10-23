# // 3461. Check If Digits Are Equal in String After Operations I(23/10/2025)
# Rất hay 👏
# Đây là **phiên bản tối ưu O(n)** của bài *LeetCode 3461 – Check If Digits Are Equal in String After Operations I*,
# sử dụng **toán tổ hợp và modulo 10** để tránh phải mô phỏng từng bước (O(n²)).

# Cùng mình **giải thích chi tiết thuật toán và thêm chú thích trực tiếp vào code** nhé 👇

# ---

# ```python
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)

        # 🔹 Trường hợp cơ bản: nếu chuỗi có <= 3 chữ số
        # thì sau vài phép cộng mod 10, hai chữ số đầu-cuối sẽ là kết quả cuối cùng.
        # Vì vậy chỉ cần so sánh s[0] và s[-1].
        if n <= 3:
            return s[0] == s[-1]

        # v1, v2 là hai giá trị "tổ hợp có trọng số" (sẽ giải thích ở dưới)
        v1 = v2 = 0

        # c = hệ số tổ hợp C(n-2, i) ban đầu (khởi tạo = 1)
        c = 1

        # ✨ Chuyển chuỗi thành danh sách số nhanh hơn int(ch)
        # vì ord('0') == 48 → ord(ch) - 48 cho ta giá trị số nguyên 0–9
        s_int = [ord(ch) - 48 for ch in s]

        # n1 = n - 1 dùng nhiều lần để giảm phép tính
        n1 = n - 1

        # 🔸 Ý tưởng toán học:
        # Sau (n-2) phép gộp, mỗi chữ số s[i] sẽ có trọng số C(n-2, i) trong kết quả cuối cùng.
        # Hai chữ số cuối cùng (vị trí 0 và 1 sau rút gọn)
        # có thể biểu diễn như tổng tổ hợp của các chữ số đầu-cuối.
        # => Nếu (v1 - v2) chia hết cho 10 → hai chữ số cuối giống nhau.
        #
        # v1: cộng từ trái sang phải
        # v2: cộng từ phải sang trái
        for i in range(n):
            v1 += s_int[i] * c          # cộng theo hướng trái → phải
            v2 += s_int[n1 - i] * c     # cộng theo hướng phải → trái
            # Cập nhật hệ số tổ hợp C(n-2, i+1) từ C(n-2, i)
            # công thức: C(k, i+1) = C(k, i) * (k - i) / (i + 1)
            c = c * (n1 - 2 - i) // (i + 1)

        # 🔹 Nếu hiệu hai tổng chia hết cho 10 → hai chữ số cuối cùng bằng nhau
        return (v1 - v2) % 10 == 0
# ```

# ---

# ### 🧩 Giải thích thuật toán (trực quan hơn)

# Thay vì mô phỏng từng vòng `(a[i] + a[i+1]) % 10`,
# ta có thể chứng minh rằng **mỗi chữ số ban đầu s[i]** sẽ ảnh hưởng đến **chữ số cuối cùng**
# với trọng số là **C(n-2, i)** (hệ số tổ hợp).

# > Vì ở mỗi lần “rút gọn”, chữ số ở vị trí i sẽ được cộng dồn lên theo dạng tam giác Pascal.

# Vì vậy, hai chữ số cuối cùng `x` và `y` sẽ là:

# ```
# x = ∑ s[i] * C(n-2, i)
# y = ∑ s[n-1-i] * C(n-2, i)
# ```

# → Nếu `(x - y) % 10 == 0`, thì `x` và `y` giống nhau.

# ---

# ### ⚙️ Độ phức tạp

# | Thành phần | Độ phức tạp                   |
# | ---------- | ----------------------------- |
# | Thời gian  | **O(n)**                      |
# | Bộ nhớ     | **O(1)** (không cần mảng phụ) |

# ---

### 🧠 Ví dụ minh họa

# `Input: s = "3902"`

# * n = 4
# * C(2, i): [1, 2, 1]
# * `v1 = 3*1 + 9*2 + 0*1 + 2*0 = 21`
# * `v2 = 2*1 + 0*2 + 9*1 + 3*0 = 11`
# * `(v1 - v2) % 10 = (21 - 11) % 10 = 0 → True`

# ✅ Output: `true`

# ---

# Bạn có muốn mình **vẽ sơ đồ tam giác Pascal** để minh họa rõ hơn vì sao xuất hiện tổ hợp `C(n-2, i)` trong công thức này không?

# import java.util.*;

# public class b76 {
#   static Scanner sc = new Scanner(System.in);

#   public static void main(String[] args) {
#     String s = sc.nextLine();

#     boolean result = hasSameDigits(s);

#     System.out.println(result);

#     sc.close();
#   }

#   // Hàm chính để kiểm tra hai chữ số cuối cùng có bằng nhau không
#   public static boolean hasSameDigits(String s) {
#     int[] arr = new int[s.length()];

#     // ✅ Bước 1: Chuyển chuỗi thành mảng số nguyên
#     for (int i = 0; i < arr.length; i++)
#       arr[i] = s.charAt(i) - '0'; // chuyển ký tự '0'-'9' thành 0-9

#     // ✅ Bước 2: Lặp cho đến khi chỉ còn 2 phần tử
#     for (int length = arr.length; length > 2; length--) {
#       // Với mỗi cặp liền kề, tính (a[i] + a[i+1]) % 10
#       for (int i = 0; i < length - 1; i++) {
#         arr[i] = (arr[i] + arr[i + 1]) % 10;
#       }
#     }

#     // ✅ Bước 3: So sánh hai chữ số cuối cùng
#     return arr[0] == arr[1];
#   }
# }

# // Dưới đây là phần **giải thích chi tiết đề bài** của bài 3461. Check If Digits
# // Are Equal in String After Operations I — bạn xem kỹ rồi nếu muốn mình có thể
# // tiếp phần *ý tưởng giải* hoặc *cài code mẫu* nhé.

# // ---

# // ### 📌 Đề bài

# // Bạn được cho một chuỗi `s` chỉ gồm các ký tự số (0-9).
# // Thực hiện thao tác lặp lại nhiều lần cho tới khi chuỗi chỉ còn **chính xác 2
# // chữ số** như sau:

# // * Mỗi lần, từ vị trí đầu tiên của chuỗi, với mỗi cặp hai chữ số liền kề, lấy
# // tổng của chúng mod 10.
# // * Từ chuỗi ban đầu, tạo ra chuỗi mới là tất cả kết quả của các tính toán này,
# // giữ nguyên thứ tự.
# // * Thay thế chuỗi hiện tại bằng chuỗi mới.
# // Khi chuỗi còn 2 chữ số thì dừng lại.
# // Cuối cùng: nếu hai chữ số còn lại **giống nhau** thì trả về `true`, ngược lại
# // `false`.
# // ([AlgoMonster][1])

# // ---

# // ### 🧮 Ví dụ

# // * Ví dụ 1: `s = "3902"`

# // * Lần 1: cặp (3,9)→(3+9)%10=2; (9,0)→9; (0,2)→2 → chuỗi mới = `"292"`
# // ([Progiez][2])
# // * Lần 2: cặp (2,9)→1; (9,2)→1 → chuỗi mới = `"11"`
# // * Còn 2 chữ số, và `"11"` có hai chữ số giống nhau → trả về `true`.
# // * Ví dụ 2: `s = "34789"`

# // * Thực hiện lần lượt sẽ còn chuỗi `"48"` cuối cùng, và vì `4 != 8` nên trả về
# // `false`. ([Progiez][2])

# // ---

# // ### 🔍 Giải thích chi tiết

# // * Chuỗi ban đầu dài `n`.
# // * Mỗi lần thao tác sẽ giảm độ dài chuỗi đi **1** (vì mỗi cặp liền kề tạo ra
# // một phần tử mới).
# // → Nếu `n` là độ dài ban đầu, sau `n-2` lần thì chuỗi còn 2 chữ số.
# // ([AlgoMonster][1])
# // * Công thức mỗi phần tử mới tại lần i: nếu chuỗi hiện tại là `a[0..k]` (k+1
# // phần tử), thì mới sẽ là bảng `b[0..k-1]` với `b[j] = (a[j] + a[j+1]) % 10`.
# // * Dừng khi chỉ còn 2 phần tử, so sánh `a[0] == a[1]`.

# // ---

# // ### ✅ Những điểm cần lưu ý

# // * Luôn dùng `% 10` khi tính tổng. Nếu bỏ mod thì có thể ra 2 chữ số hoặc lớn
# // hơn 9, sai yêu cầu. ([AlgoMonster][1])
# // * Vì chuỗi có thể ban đầu khá dài, mô phỏng trực tiếp sẽ tốn thời gian ~
# // O(n²) trong trường hợp dài `n`. (n + (n-1) + (n-2) + … ~ O(n²)).
# // ([AlgoMonster][1])
# // * Đề bài định rõ “chỉ gồm chữ số” và “thực hiện cho đến khi còn chính xác hai
# // chữ số”. ([LeetCode][3])

# // ---

# // Nếu bạn muốn, mình **có thể giải thích thêm** về cách tối ưu hơn (nếu có),
# // hoặc **viết code mẫu** (Python, C++ hoặc Java) cho bài này — bạn muốn theo
# // ngôn ngữ nào?

# // Rất hay 👏
# // Đây là **phiên bản tối ưu hơn** của bài *LeetCode 3461 – Check If Digits Are
# // Equal in String After Operations I*.
# // Cùng mình **phân tích chi tiết thuật toán** nhé.

# // ---

# // ## 🧠 Ý tưởng cốt lõi

# // Mục tiêu:

# // > Bắt đầu với chuỗi số `s`, lặp lại việc lấy `(a[i] + a[i+1]) % 10` cho đến
# // khi còn 2 chữ số, rồi kiểm tra chúng có bằng nhau không.

# // Thay vì tạo chuỗi mới sau mỗi vòng (gây tốn bộ nhớ và thời gian), ta có thể
# // **tính trực tiếp trên cùng một mảng `arr`** — *chính là ý tưởng trong code
# // của bạn*.

# // ---

# // ## 🔍 Giải thích từng bước

# // ### 1️⃣ Chuyển chuỗi sang mảng số nguyên

# // ```java
# // for (int i = 0; i < arr.length; i++)
# // arr[i] = s.charAt(i) - '0';
# // ```

# // → Mỗi ký tự `'0'`–`'9'` trong `s` được đổi thành số 0–9 tương ứng.
# // Ví dụ:
# // `s = "3902"` → `arr = [3, 9, 0, 2]`

# // ---

# // ### 2️⃣ Lặp dần rút gọn chuỗi

# // ```java
# // for (int length = arr.length; length > 2; length--) {
# // for (int i = 0; i < length - 1; i++) {
# // arr[i] = (arr[i] + arr[i + 1]) % 10;
# // }
# // }
# // ```

# // Ở mỗi vòng `length`:

# // * `arr[i]` được cập nhật thành `(arr[i] + arr[i+1]) % 10`.
# // * Sau mỗi vòng, ta **giảm chiều dài hữu dụng của mảng đi 1**, vì đã rút gọn
# // xong một lớp.

# // > 🔹 Không cần tạo mảng mới — chỉ “ghi đè” trực tiếp lên `arr`.

# // ### 🔄 Ví dụ minh họa

# // `arr = [3, 9, 0, 2]`

# // | Bước | Chiều dài | Tính toán | Kết quả `arr` (phần có ý nghĩa) |
# // | ------- | --------- | ---------------------------------- |
# // ------------------------------- |
# // | Ban đầu | 4 | | [3, 9, 0, 2] |
# // | 1 | 4→3 | (3+9)%10=2, (9+0)%10=9, (0+2)%10=2 | [2, 9, 2, …] |
# // | 2 | 3→2 | (2+9)%10=1, (9+2)%10=1 | [1, 1, …] |

# // Còn lại `[1,1]` → hai chữ số giống nhau ✅ → `true`.

# // ---

# // ### 3️⃣ Kiểm tra hai chữ số cuối cùng

# // ```java
# // return arr[0] == arr[1];
# // ```

# // Khi vòng lặp kết thúc, hai phần tử đầu tiên trong `arr` chính là hai chữ số
# // còn lại sau khi rút gọn.

# // ---

# // ## ⚙️ Độ phức tạp

# // | Loại | Phân tích | Độ phức tạp |
# // | ------------- | ------------------------------------------------- |
# // ----------- |
# // | **Thời gian** | Tổng số phép cộng ~ n + (n-1) + ... + 3 ≈ O(n²/2) |
# // **O(n²)** |
# // | **Bộ nhớ** | Dùng 1 mảng cố định, không tạo mới | **O(n)** |

# // ---

# // ## ✅ Ưu điểm

# // * Không cần tạo chuỗi mới (hiệu quả hơn bản dùng `StringBuilder`).
# // * Dễ hiểu, trực quan, đúng với mô phỏng của đề.
# // * Có thể dễ dàng in trung gian để debug nếu cần.

# // ---

# // Nếu bạn muốn, mình có thể chỉ cách **rút gọn công thức để làm O(n)** (không
# // cần mô phỏng từng bước) — dùng **toán tổ hợp + modulo 10**.
# // Bạn có muốn mình trình bày cách tối ưu đó không?
