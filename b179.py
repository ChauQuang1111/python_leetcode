# // // ### 🧠 Bài 67 — **Add Binary** (15/02/2026)

# // Mình sẽ **giải thích thuật toán trong đoạn code của bạn theo từng bước**, để bạn hiểu rõ cách cộng nhị phân hoạt động bên trong 👇

# OK 👍 Mình sẽ **giải thích thuật toán + thêm chú thích trực tiếp vào code Python** để bạn nhìn là hiểu ngay cách nó chạy.

# ---

# # 🧠 Giải thích thuật toán Add Binary (Python)

# Mục tiêu:
# ➡️ Cộng 2 chuỗi nhị phân `a` và `b` → trả về chuỗi nhị phân kết quả.

# Ý tưởng giống hệt cộng tay:

# * Đi từ **phải → trái**
# * Cộng từng bit
# * Có **carry (số nhớ)**

# ---

# # 🧾 Code đã thêm chú thích chi tiết

# ```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # i trỏ vào cuối chuỗi a
        # j trỏ vào cuối chuỗi b
        i, j = len(a) - 1, len(b) - 1

        # Biến nhớ khi cộng (carry)
        carry = 0

        # Danh sách lưu kết quả (dạng list cho nhanh)
        res = []

        # Lặp khi:
        # - còn bit trong a
        # - hoặc còn bit trong b
        # - hoặc còn carry
        while i >= 0 or j >= 0 or carry:

            # Tổng ban đầu = carry trước đó
            total = carry

            # Nếu còn bit trong a
            if i >= 0:
                # Chuyển ký tự '0'/'1' → số nguyên
                total += int(a[i])
                i -= 1   # dịch sang trái

            # Nếu còn bit trong b
            if j >= 0:
                total += int(b[j])
                j -= 1   # dịch sang trái

            # Lấy bit kết quả hiện tại
            # total % 2 chỉ cho ra 0 hoặc 1
            res.append(str(total % 2))

            # Tính carry cho lần cộng tiếp theo
            carry = total // 2

        # Vì kết quả đang ngược → đảo lại
        # reversed(res) → đảo list
        # join → ghép thành chuỗi
        return ''.join(reversed(res))
# ```

# ---

# # 🔄 Mô phỏng chạy từng bước

# ### Ví dụ

# ```
# a = "1010"
# b = "1011"
# ```

# | Bước    | total | append | carry | res   |
# | ------- | ----- | ------ | ----- | ----- |
# | 0+1+1=2 | 2     | 0      | 1     | 0     |
# | 1+0+1=2 | 2     | 0      | 1     | 00    |
# | 0+1+1=2 | 2     | 0      | 1     | 000   |
# | 1+1+1=3 | 3     | 1      | 1     | 0001  |
# | carry   | 1     | 1      | 0     | 00011 |

# Reverse → `10101`

# ---

# 📌 Giải thích các dòng quan trọng

### 1️⃣ Điều kiện while

# ```python
# while i >= 0 or j >= 0 or carry:
# ```

# Đảm bảo:

# * Không bỏ sót bit
# * Không quên carry cuối

# ---

# ### 2️⃣ Lấy bit nhị phân

# ```python
# total % 2
# ```

# | total | bit |
# | ----- | --- |
# | 0     | 0   |
# | 1     | 1   |
# | 2     | 0   |
# | 3     | 1   |

# ---

# ### 3️⃣ Tính carry

# ```python
# carry = total // 2
# ```

# | total | carry |
# | ----- | ----- |
# | 0     | 0     |
# | 1     | 0     |
# | 2     | 1     |
# | 3     | 1     |

# ---

# # ⏱️ Độ phức tạp

# * **Time:** `O(n)`
# * **Space:** `O(n)`

# (n = độ dài chuỗi lớn hơn)

# ---

# 🆚 So sánh nhanh Java vs Python

# | Java          | Python     |
# | ------------- | ---------- |
# | StringBuilder | list       |
# | reverse()     | reversed() |
# | char - '0'    | int(char)  |
# | /             | //         |

# ---

# Nếu bạn muốn mình làm tiếp:

# * Thêm `main` Python nhập từ bàn phím
# * Viết version **không dùng reversed**
# * Dùng **zfill** để pad chuỗi
# * Giải thích bằng sơ đồ bit

# Bạn muốn đào sâu phần nào? 🚀




# // ---

# import java.util.*;

# public class b180 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         String a = sc.nextLine();

#         String b = sc.nextLine();

#         // Gọi hàm cộng nhị phân
#         String result = addBinary(a, b);

#         // In kết quả
#         System.out.println("Tong nhi phan: " + result);

#         sc.close();
#     }

#     public static String addBinary(String a, String b) {

#         // Dùng để lưu kết quả (nối chuỗi nhanh hơn String)
#         StringBuilder res = new StringBuilder();

#         // Con trỏ i trỏ vào cuối chuỗi a
#         int i = a.length() - 1;

#         // Con trỏ j trỏ vào cuối chuỗi b
#         int j = b.length() - 1;

#         // Biến nhớ (carry) khi cộng nhị phân
#         int carry = 0;

#         // Lặp khi còn bit ở a hoặc b hoặc còn carry
#         while (i >= 0 || j >= 0 || carry == 1) {

#             // Tổng ban đầu = carry trước đó
#             int sum = carry;

#             // Nếu còn bit trong a thì cộng vào sum
#             if (i >= 0) {
#                 // char → int bằng cách trừ '0'
#                 sum += a.charAt(i) - '0';
#                 i--; // dịch sang trái
#             }

#             // Nếu còn bit trong b thì cộng vào sum
#             if (j >= 0) {
#                 sum += b.charAt(j) - '0';
#                 j--; // dịch sang trái
#             }

#             // Lấy bit kết quả (0 hoặc 1)
#             res.append(sum % 2);

#             // Tính carry cho lần cộng tiếp theo
#             carry = sum / 2;
#         }

#         // Đảo chuỗi vì ta append từ phải → trái
#         return res.reverse().toString();
#     }
# }

# // ## 📌 Mục tiêu của hàm

# // ```java
# // public String addBinary(String a, String b)
# // ```

# // 👉 Cộng 2 chuỗi nhị phân `a` và `b` → trả về **chuỗi nhị phân kết quả**.

# // ---

# // ## 🧱 Khởi tạo biến

# // ```java
# // StringBuilder res = new StringBuilder();
# // ```

# // * Dùng để **lưu kết quả**.
# // * Dùng `StringBuilder` vì:

# // * Nối chuỗi nhanh hơn `String`.
# // * Sau cùng sẽ `reverse()`.

# // ---

# // ```java
# // int i = a.length() - 1;
# // int j = b.length() - 1;
# // ```

# // * `i` trỏ vào **bit cuối của a**.
# // * `j` trỏ vào **bit cuối của b**.

# // 👉 Vì cộng nhị phân phải đi **từ phải → trái**.

# // ---

# // ```java
# // int carry = 0;
# // ```

# // * Biến **nhớ** (giống cộng thập phân).
# // * Ví dụ: `1 + 1 = 10` → ghi `0`, nhớ `1`.

# // ---

# // ## 🔁 Vòng lặp chính

# // ```java
# // while(i >= 0 || j >= 0 || carry == 1)
# // ```

# // Lặp khi còn ít nhất 1 trong 3 điều kiện:

# // 1. `i >= 0` → còn bit trong `a`
# // 2. `j >= 0` → còn bit trong `b`
# // 3. `carry == 1` → còn số nhớ

# // 👉 Điều kiện này đảm bảo:

# // * Không bỏ sót bit
# // * Không quên cộng số nhớ cuối

# // ---

# // ## 🧮 Tính tổng từng bit

# // ```java
# // int sum = carry;
# // ```

# // * Khởi đầu tổng = số nhớ trước đó.

# // ---

# // ### Nếu còn bit trong `a`

# // ```java
# // if(i >= 0) sum += a.charAt(i--) - '0';
# // ```

# // Giải thích:

# // * `a.charAt(i)` → lấy ký tự `'0'` hoặc `'1'`
# // * Trừ `'0'` để chuyển sang số:

# // | Ký tự | - '0' | Kết quả |
# // | ----- | ----- | ------- |
# // | '0' | 48-48 | 0 |
# // | '1' | 49-48 | 1 |

# // 👉 Sau đó `i--` để dịch sang trái.

# // ---

# // ### Nếu còn bit trong `b`

# // ```java
# // if(j >= 0) sum += b.charAt(j--) - '0';
# // ```

# // Tương tự như trên.

# // ---

# // ## ➗ Lấy bit kết quả

# // ```java
# // res.append(sum % 2);
# // ```

# // Nhị phân base 2 nên:

# // | sum | sum % 2 | Ghi |
# // | --- | ------- | --- |
# // | 0 | 0 | 0 |
# // | 1 | 1 | 1 |
# // | 2 | 0 | 0 |
# // | 3 | 1 | 1 |

# // 👉 `% 2` = bit hiện tại.

# // ---

# // ## 🔁 Cập nhật số nhớ

# // ```java
# // carry = sum / 2;

# // | sum | sum / 2 | carry |
# // | --- | ------- | ----- |
# // | 0 | 0 | 0 |
# // | 1 | 0 | 0 |
# // | 2 | 1 | 1 |
# // | 3 | 1 | 1 |

# // ---

# // ## 🔚 Đảo chuỗi

# // ```java
# // return res.reverse().toString();
# // ```

# // Vì:

# // * Bạn append từ **phải → trái**.
# // * Nên kết quả bị ngược → phải `reverse()`.

# // ---

# // ## 🧩 Ví dụ chạy từng bước

# // ### Input

# // ```
# // a = "1010"
# // b = "1011"
# // ```

# // ### Bảng mô phỏng

# // | i | j | carry | sum | append | res |
# // | - | - | ----- | ------- | ------ | ----- |
# // | 3 | 3 | 0 | 0+1+1=2 | 0 | 0 |
# // | 2 | 2 | 1 | 1+0+1=2 | 0 | 00 |
# // | 1 | 1 | 1 | 1+1+1=3 | 1 | 001 |
# // | 0 | 0 | 1 | 1+0+1=2 | 0 | 0010 |
# // | - | - | 1 | 1 | 1 | 00101 |

# // Reverse → `10101`

# // ---

# // ## ⏱️ Độ phức tạp

# // * **Time:** `O(max(n, m))`
# // * **Space:** `O(max(n, m))`

# // Vì duyệt mỗi chuỗi 1 lần.

# // ---

# // ## 💡 Ý tưởng cốt lõi của thuật toán

# // 1. Dùng 2 con trỏ từ phải sang trái.
# // 2. Cộng từng bit + carry.
# // 3. Lưu `sum % 2`.
# // 4. Nhớ `sum / 2`.
# // 5. Reverse kết quả.

# // ---

# // Nếu bạn muốn, mình có thể:

# // * Viết lại bằng **while → for**
# // * Không dùng `StringBuilder`
# // * Dùng **BigInteger**
# // * Vẽ sơ đồ bit trực quan hơn

# // Bạn muốn
# // đào sâu
# // phần nào?🚀

# // Đây là một bài rất phổ biến trên LeetCode. Mình sẽ **giải thích đề bài bằng
# // tiếng Việt dễ hiểu** nhé.

# // ---

# // ## 📌 Nội dung đề bài

# // Bạn được cho **2 chuỗi nhị phân** `a` và `b`.

# // * Mỗi chuỗi chỉ gồm ký tự:

# // * `'0'`
# // * `'1'`
# // * Nhiệm vụ của bạn: **Cộng hai số nhị phân này lại** và trả về **kết quả cũng
# // ở dạng chuỗi nhị phân**.

# // ---

# // ## 🔢 Ví dụ minh họa

# // ### Ví dụ 1

# // ```
# // Input: a = "11"
# // b = "1"

# // Output: "100"
# // ```

# // **Giải thích:**

# // ```
# // 11 (3 trong hệ thập phân)
# // + 1 (1 trong hệ thập phân)
# // ------
# // 100 (4 trong hệ thập phân)
# // ```

# // ---

# // ### Ví dụ 2

# // ```
# // Input: a = "1010"
# // b = "1011"

# // Output: "10101"
# // ```

# // **Cộng từng bit từ phải sang trái:**

# // ```
# // 1010
# // + 1011
# // -------
# // 10101
# // ```

# // ---

# // ## ⚙️ Quy tắc cộng nhị phân (giống cộng thập phân nhưng base 2)

# // | Phép cộng | Kết quả | Nhớ |
# // | --------- | ------- | --- |
# // | 0 + 0 | 0 | 0 |
# // | 0 + 1 | 1 | 0 |
# // | 1 + 0 | 1 | 0 |
# // | 1 + 1 | 0 | 1 |
# // | 1 + 1 + 1 | 1 | 1 |

# // 👉 Tức là:

# // * Tổng ≥ 2 → ghi `0` hoặc `1` tùy trường hợp, và **nhớ 1** sang bit bên trái.

# // ---

# // ## 🧩 Bạn cần làm gì trong bài này?

# // 1. Đọc 2 chuỗi `a` và `b`.
# // 2. Cộng từ **phải → trái** (bit cuối).
# // 3. Xử lý **carry (số nhớ)**.
# // 4. Nếu cộng xong vẫn còn nhớ → thêm `1` phía trước.
# // 5. Trả về chuỗi kết quả.

# // ---

# // ## 📏 Ràng buộc (Constraints)

# // * `1 <= a.length, b.length <= 10^4`
# // * Chuỗi chỉ chứa `0` và `1`.
# // * Không có số 0 vô nghĩa ở đầu (trừ khi là `"0"`).

# // ---

# // ## 💡 Ý tưởng cốt lõi

# // Bài này kiểm tra bạn về:

# // * Xử lý chuỗi
# // * Mô phỏng phép cộng
# // * Dùng biến **carry**
# // * Duyệt từ phải sang trái

# // ---

# // Nếu bạn muốn, mình có thể:

# // * Viết code Java / Python / C++
# // * Vẽ sơ đồ cộng bit-by-bit
# // * Tối ưu cách làm (StringBuilder, BigInteger…)

# // Bạn muốn mình giải thích tiếp theo hướng nào? 🚀
