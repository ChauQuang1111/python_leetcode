# // // Binary Watch(17/02/2026)
# // // ## 🧭 LeetCode – **Binary Watch** (Giải thích đề bài dễ hiểu)

# Ok 👍 — đây là lời giải **Python one-liner + bit manipulation** của bài **401. Binary Watch**.
# Mình sẽ:

# 1. Giải thích ý tưởng thuật toán
# 2. Phân tích từng phần expression
# 3. Viết lại code có chú thích chi tiết

# ---

# # 1️⃣ Ý tưởng thuật toán

# Thay vì:

# * Sinh LED bằng đệ quy (như Java bạn làm)
# * Hoặc backtracking

# Code này dùng cách **brute force thông minh**:

# 👉 Duyệt toàn bộ thời gian hợp lệ:

# ```
# Giờ:   0 → 11
# Phút:  0 → 59
# ```

# Tổng = 12 × 60 = **720 trường hợp** (rất nhỏ)

# Với mỗi thời gian:

# * Ghép giờ + phút thành số nhị phân 10 bit
# * Đếm số bit 1
# * Nếu = `n` → lấy thời gian đó

# ---

# # 2️⃣ Phân tích dòng code chính

# ```python
# return [f'{h}:{m:02d}' for h in range(12) for m in range(60)
#         if (h<<6 | m).bit_count() == n]
# ```

# Đây là **List Comprehension** gồm 3 phần:

# ---

# ## 2.1 Duyệt giờ

# ```python
# for h in range(12)
# ```

# → 0 → 11

# ---

# ## 2.2 Duyệt phút

# ```python
# for m in range(60)
# ```

# → 0 → 59

# ---

# ## 2.3 Ghép giờ + phút thành nhị phân

# ```python
# (h << 6 | m)
# ```

# ### Vì sao shift 6?

# Binary Watch có:

# * 4 bit giờ
# * 6 bit phút

# Ta đẩy giờ sang trái 6 bit để nhường chỗ cho phút.

# ---

# ### Ví dụ

# Giả sử:

# ```
# h = 3  -> 0011
# m = 5  -> 000101
# ```

# Shift:

# ```
# h << 6 = 0011 000000
# ```

# OR với phút:

# ```
# 0011 000000
# 0000 000101
# ------------
# 0011 000101
# ```

# → Đây là 10 bit của đồng hồ.

# ---

# ## 2.4 Đếm số bit 1

# ```python
# .bit_count()
# ```

# Hàm built-in Python (3.8+):

# → Đếm số bit 1 trong số nguyên.

# Ví dụ:

# ```
# (3<<6 | 5) = 197
# 197 = 11000101
# bit_count = 4
# ```

# ---

# ## 2.5 Điều kiện lọc

# ```python
# if bit_count == n
# ```

# → Chỉ lấy thời gian có đúng `n` LED sáng.

# ---

# ## 2.6 Format chuỗi thời gian

# ```python
# f'{h}:{m:02d}'
# ```

# Ý nghĩa:

# * `h` → giờ
# * `m:02d` → phút 2 chữ số

# Ví dụ:

# ```
# 5  -> 05
# 23 -> 23
# ```

# ---

# # 3️⃣ Code có chú thích chi tiết

# ```python
from typing import List

class Solution:
    def readBinaryWatch(self, n: int) -> List[str]:
        
        # List comprehension duyệt tất cả thời gian hợp lệ
        return [
            
            # Format thời gian: giờ : phút (2 chữ số)
            f'{h}:{m:02d}'
            
            # Duyệt giờ từ 0 → 11 (4 LED)
            for h in range(12)
            
            # Duyệt phút từ 0 → 59 (6 LED)
            for m in range(60)
            
            # Ghép giờ + phút thành số nhị phân 10 bit
            # h << 6 : đẩy giờ sang trái 6 bit
            # | m    : OR với phút
            # => tạo số biểu diễn LED đồng hồ
            
            # bit_count() : đếm số bit 1 (số LED sáng)
            if (h << 6 | m).bit_count() == n
        ]
# ```

# ---

# # 4️⃣ Minh họa trực quan

# Giả sử:

# ```
# n = 2
# h = 1  -> 0001
# m = 2  -> 000010
# ```

# Ghép:

# ```
# 0001 000010
# ```

# Bit 1 = 2 → hợp lệ → `"1:02"`

# ---

# # 5️⃣ Độ phức tạp

# * Duyệt: 12 × 60 = 720
# * Mỗi lần đếm bit: O(1)

# 👉 Time: **O(720) ≈ O(1)**
# 👉 Space: phụ thuộc output

# Rất nhanh hơn backtracking.

# ---

# # 6️⃣ So sánh với code Java của bạn

# | Cách             | Ý tưởng         | Độ khó    |
# | ---------------- | --------------- | --------- |
# | Backtracking     | Sinh LED        | Khó       |
# | Bit brute force  | Duyệt thời gian | Dễ        |
# | Python one-liner | Bit + format    | Ngắn nhất |

# ---

# # 7️⃣ Viết lại dạng dễ đọc (không one-liner)

# ```python
class Solution:
    def readBinaryWatch(self, n: int):
        
        ans = []
        
        for h in range(12):        # duyệt giờ
            for m in range(60):    # duyệt phút
                
                # Ghép giờ + phút thành 10 bit
                num = (h << 6) | m
                
                # Đếm số LED sáng
                if num.bit_count() == n:
                    
                    # Format phút 2 chữ số
                    time = f'{h}:{m:02d}'
                    
                    ans.append(time)
        
        return ans
# ```

# ---

# Nếu bạn muốn mình giải thích thêm:

# * Vì sao dùng `<< 6` mà không phải 4
# * Cách làm bằng bitmask thuần
# * Viết lại sang Java / C++
# * So sánh hiệu năng 3 cách

# Bạn muốn đào sâu phần nào tiếp?


# // // ### 1️⃣ Đồng hồ Binary Watch là gì?

# import java.util.*;

# public class b182 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int turnedOn = sc.nextInt();

#         // Gọi hàm giải bài
#         List<String> result = readBinaryWatch(turnedOn);

#         for (String time : result) {
#             System.out.println(time);
#         }

#         sc.close();
#     }

#     // Hàm chính của bài LeetCode
#     public static List<String> readBinaryWatch(int turnedOn) {

#         // Danh sách lưu kết quả thời gian hợp lệ
#         List<String> ans = new ArrayList<>();

#         // Nếu số LED bật quá lớn thì không có kết quả
#         if (turnedOn > 8) {
#             return ans;
#         }

#         // Gọi đệ quy sinh giờ
#         recurhour(ans, new StringBuilder(), 0, 4, turnedOn, 0);

#         return ans;
#     }

#     /*
#      * Hàm đệ quy sinh giờ từ 4 LED
#      * total : tổng giờ hiện tại
#      * bitno : số LED giờ còn xét
#      * limit : tổng LED cần bật
#      * on : số LED đã bật
#      */
#     public static void recurhour(List<String> ans, StringBuilder ds,
#             int total, int bitno, int limit, int on) {

#         // Khi đã xét hết 4 LED giờ
#         if (bitno == 0) {

#             // Nếu giờ > 11 thì không hợp lệ
#             if (total > 11) {
#                 return;
#             }

#             // Thêm giờ vào chuỗi
#             if (total == 11) {
#                 ds.append("11");
#             } else if (total == 10) {
#                 ds.append("10");
#             } else {
#                 ds.append((char) (total + '0'));
#             }

#             // Thêm dấu :
#             ds.append(':');

#             // Sinh phút từ 6 LED
#             recurmin(ans, ds, 0, 6, limit, on, ds.length());

#             // Backtrack chuỗi
#             ds.setLength(0);
#             return;
#         }

#         // Giá trị nếu bật LED hiện tại
#         int ntotal = total + (1 << (bitno - 1));

#         // Nhánh 1: bật LED (nếu chưa vượt limit)
#         if (on < limit) {
#             recurhour(ans, ds, ntotal, bitno - 1, limit, on + 1);
#         }

#         // Nhánh 2: không bật LED
#         recurhour(ans, ds, total, bitno - 1, limit, on);
#     }

#     /*
#      * Hàm đệ quy sinh phút từ 6 LED
#      * total : tổng phút hiện tại
#      * bitno : số LED phút còn xét
#      * limit : tổng LED cần bật
#      * on : số LED đã bật
#      * len : vị trí để backtrack StringBuilder
#      */
#     public static void recurmin(List<String> ans, StringBuilder ds,
#             int total, int bitno, int limit, int on, int len) {

#         // Khi đã xét hết 6 LED phút
#         if (bitno == 0) {

#             // Phải bật đúng số LED yêu cầu
#             if (on != limit) {
#                 return;
#             }

#             // Nếu phút > 59 thì không hợp lệ
#             if (total > 59) {
#                 return;
#             }

#             // Format phút 2 chữ số
#             if (total >= 10) {
#                 ds.append((char) (total / 10 + '0'));
#                 ds.append((char) (total % 10 + '0'));
#             } else {
#                 ds.append('0');
#                 ds.append((char) (total + '0'));
#             }

#             // Thêm vào kết quả
#             ans.add(ds.toString());

#             // Backtrack chuỗi về sau dấu :
#             ds.setLength(len);
#             return;
#         }

#         // Giá trị nếu bật LED hiện tại
#         int ntotal = total + (1 << (bitno - 1));

#         // Nhánh 1: bật LED
#         if (on < limit) {
#             recurmin(ans, ds, ntotal, bitno - 1, limit, on + 1, len);
#         }

#         // Nhánh 2: không bật LED
#         recurmin(ans, ds, total, bitno - 1, limit, on, len);

#     }

# }
# // từ tổng quan ➜ chi tiết ➜ luồng chạy**.

# // ---

# // # 1️⃣ Ý tưởng chính của thuật toán

# // Bạn đang dùng **Backtracking / Đệ quy sinh bit** để:

# // * Chọn LED nào sáng
# // * Tính tổng giờ + phút từ các LED đó
# // * Nếu số LED sáng = `turnedOn` → lưu thời gian

# // 👉 Tức là **không duyệt giờ/phút trực tiếp** mà sinh nhị phân.

# // ---

# // # 2️⃣ Cấu trúc tổng thể

# // ```java
# // readBinaryWatch()
# // └── recurhour() // sinh giờ (4 LED)
# // └── recurmin() // sinh phút (6 LED)
# // ```

# // Luồng:

# // 1. Sinh mọi cách bật LED giờ
# // 2. Với mỗi giờ hợp lệ → sinh tiếp LED phút
# // 3. Nếu đủ số LED sáng → lưu kết quả

# // ---

# // # 3️⃣ Hàm chính

# // ```java
# // public List<String> readBinaryWatch(int turnedOn)
# // ```

# // ### Việc làm:

# // ```java
# // List<String> ans = new ArrayList<>();
# // ```

# // → Lưu kết quả.

# // ```java
# // if(turnedOn > 8) return ans;
# // ```

# // 📌 Tối đa chỉ có:

# // * 4 LED giờ
# // * 6 LED phút

# // Nhưng giờ tối đa = 11 → không thể bật quá nhiều LED giờ.
# // Check này để cắt sớm (dù chuẩn là >10 mới vô nghĩa).

# // ---

# // Gọi đệ quy sinh giờ:

# // ```java
# // recurhour(ans, new StringBuilder(), 0, 4, turnedOn, 0);
# // ```

# // Tham số:

# // | Biến | Ý nghĩa |
# // | ----- | ----------------- |
# // | ans | danh sách kết quả |
# // | ds | chuỗi đang build |
# // | total | tổng giờ hiện tại |
# // | bitno | số LED còn xét |
# // | limit | số LED cần bật |
# // | on | số LED đã bật |

# // ---

# // # 4️⃣ Hàm sinh giờ – `recurhour`

# // ```java
# // void recurhour(..., int total, int bitno, int limit, int on)
# // ```

# // ## Ý nghĩa bit

# // 4 LED giờ:

# // | bit | giá trị |
# // | --- | ------- |
# // | 3 | 8 |
# // | 2 | 4 |
# // | 1 | 2 |
# // | 0 | 1 |

# // ---

# // ## Base case

# // ```java
# // if(bitno == 0)
# // ```

# // → Đã xét xong 4 LED.

# // ### Check giờ hợp lệ

# // ```java
# // if(total > 11) return;
# // ```

# // ---

# // ### Ghi giờ vào chuỗi

# // ```java
# // if(total == 11) ds.append("11");
# // else if(total == 10) ds.append("10");
# // else ds.append((char)(total + '0'));
# // ```

# // 📌 Vì giờ chỉ 0–11 nên xử lý char cho nhanh.

# // Thêm dấu :

# // ```java
# // ds.append(':');
# // ```

# // ---

# // ### Sang sinh phút

# // ```java
# // recurmin(ans, ds, 0, 6, limit, on, ds.length());
# // ```

# // ---

# // ### Reset chuỗi

# // ```java
# // ds.setLength(0);
# // ```

# // Để backtrack.

# // ---

# // # 5️⃣ Nhánh đệ quy giờ

# // ```java
# // int ntotal = total + (1 << (bitno-1));
# // ```

# // 👉 Nếu bật LED này → cộng giá trị.

# // ---

# // ## Nhánh 1: Bật LED

# // ```java
# // if(on < limit)
# // recurhour(... ntotal, bitno-1, ..., on+1);
# // ```

# // Chỉ bật nếu chưa vượt số LED cần.

# // ---

# // ## Nhánh 2: Không bật

# // ```java
# // recurhour(... total, bitno-1, ..., on);
# // ```

# // ---

# // 📌 Đây là **cây nhị phân chọn / không chọn**.

# // ---

# // # 6️⃣ Hàm sinh phút – `recurmin`

# // Tương tự giờ nhưng:

# // * 6 LED
# // * Giới hạn 59
# // * Phải đủ `turnedOn`

# // ---

# // ## Base case

# // ```java
# // if(bitno == 0)
# // ```

# // ### Check số LED

# // ```java
# // if(on != limit) return;
# // ```

# // 📌 Phải bật đúng số LED yêu cầu.

# // ---

# // ### Check phút hợp lệ

# // ```java
# // if(total > 59) return;
# // ```

# // ---

# // ## Format phút

# // ```java
# // if(total >= 10){
# // ds.append((char)(total/10 + '0'));
# // ds.append((char)(total%10 + '0'));
# // }else{
# // ds.append('0');
# // ds.append((char)(total + '0'));
# // }
# // ```

# // 👉 Đảm bảo dạng `MM`.

# // Ví dụ:

# // * 5 → `05`
# // * 23 → `23`

# // ---

# // ## Lưu kết quả

# // ```java
# // ans.add(ds.toString());
# // ```

# // ---

# // ## Backtrack chuỗi

# // ```java
# // ds.setLength(len);
# // ```

# // `len` = vị trí sau dấu `:`.

# // ---

# // # 7️⃣ Nhánh đệ quy phút

# // Giống giờ:

# // ```java
# // int ntotal = total + (1 << (bitno-1));
# // ```

# // ### Bật LED

# // ```java
# // if(on < limit)
# // recurmin(... ntotal, bitno-1, ..., on+1);
# // ```

# // ### Không bật

# // ```java
# // recurmin(... total, bitno-1, ..., on);
# // ```

# // ---

# // # 8️⃣ Luồng chạy ví dụ

# // Giả sử:

# // ```
# // turnedOn = 1
# // ```

# // ---

# // ## Sinh giờ

# // Cây chọn:

# // ```
# // 0000 -> 0h
# // 0001 -> 1h
# // 0010 -> 2h
# // 0100 -> 4h
# // 1000 -> 8h
# // ...
# // ```

# // Mỗi giờ → sang sinh phút với số LED còn lại.

# // ---

# // Ví dụ:

# // * Chọn giờ = 1 LED → phút phải = 0 LED → `1:00`
# // * Chọn giờ = 0 LED → phút = 1 LED → `0:01`

# // ---

# // # 9️⃣ Độ phức tạp

# // Số trạng thái:

# // ```
# // 2^4 * 2^6 = 1024
# // ```

# // → Nhỏ → chạy rất nhanh.

# // Time: **O(1024)** ≈ O(1)

# // ---

# // # 🔟 Tóm tắt thuật toán

# // ✔ Sinh mọi cách bật LED giờ
# // ✔ Tính tổng giờ
# // ✔ Nếu hợp lệ → sinh LED phút
# // ✔ Đủ số LED → lưu kết quả

# // ---

# // # 1️⃣1️⃣ Điểm hay trong code bạn

# // * Dùng bit shift `(1 << k)` chuẩn
# // * Dùng `StringBuilder` để backtrack
# // * Cắt sớm khi:

# // * Giờ > 11
# // * Phút > 59
# // * LED > limit

# // ---

# // Nếu bạn muốn mình giải thích thêm:

# // * Vẽ cây đệ quy
# // * Dry run turnedOn = 2
# // * So sánh với brute force
# // * Tối ưu code

# // Bạn muốn mình đi sâu phần nào?

# // // Binary Watch là đồng hồ mà **giờ** và **phút** được biểu diễn bằng **đèn
# // LED nhị phân** (0 = tắt, 1 = sáng).

# // // * Có **10 đèn LED** tổng cộng:

# // // * **4 đèn** bên trái → biểu diễn **giờ (0–11)**
# // // * **6 đèn** bên phải → biểu diễn **phút (0–59)**

# // // ---

# // // ### 2️⃣ Ý nghĩa từng hàng đèn

# // // #### 🕒 Hàng giờ (4 LED)

# // // Giá trị lần lượt là:

# // // | LED | Giá trị |
# // // | --- | ------- |
# // // | 1 | 8 |
# // // | 2 | 4 |
# // // | 3 | 2 |
# // // | 4 | 1 |

# // // 👉 Ví dụ:

# // // * Sáng 8 + 2 = **10 giờ**

# // // ---

# // // #### ⏱️ Hàng phút (6 LED)

# // // | LED | Giá trị |
# // // | --- | ------- |
# // // | 1 | 32 |
# // // | 2 | 16 |
# // // | 3 | 8 |
# // // | 4 | 4 |
# // // | 5 | 2 |
# // // | 6 | 1 |

# // // 👉 Ví dụ:

# // // * Sáng 32 + 8 + 1 = **41 phút**

# // // ---

# // // ### 3️⃣ Yêu cầu đề bài (LeetCode)

# // // > Cho một số nguyên `turnedOn` = số lượng đèn LED đang sáng.
# // // > Hãy trả về **tất cả các thời gian hợp lệ** mà đồng hồ có thể hiển thị.

# // // 📌 Điều kiện hợp lệ:

# // // * Giờ: `0 → 11`
# // // * Phút: `0 → 59`
# // // * Định dạng: `"H:MM"`

# // // * Ví dụ: `3:07` (phút phải đủ 2 chữ số)

# // // ---

# // // ### 4️⃣ Ví dụ đề bài

# // // #### Ví dụ 1

# // // ```
# // // Input: turnedOn = 1
# // // ```

# // // 👉 Chỉ có 1 đèn sáng → các khả năng:

# // // * Bật LED giờ:

# // // * 1 → 1:00
# // // * 2 → 2:00
# // // * 4 → 4:00
# // // * 8 → 8:00

# // // * Bật LED phút:

# // // * 1 → 0:01
# // // * 2 → 0:02
# // // * 4 → 0:04
# // // * 8 → 0:08
# // // * 16 → 0:16
# // // * 32 → 0:32

# // // ➡️ Output gồm các chuỗi thời gian này.

# // // ---

# // // #### Ví dụ 2

# // // ```
# // // Input: turnedOn = 2
# // // ```

# // // 👉 Có 2 đèn sáng → phải xét:

# // // * 2 đèn ở giờ
# // // * 2 đèn ở phút
# // // * 1 giờ + 1 phút

# // // Rồi cộng giá trị lại → lọc thời gian hợp lệ.

# // // ---

# // // ### 5️⃣ Bản chất bài toán

# // // Thực chất bạn cần:

# // // 1. Duyệt tất cả giờ từ `0 → 11`
# // // 2. Duyệt tất cả phút từ `0 → 59`
# // // 3. Đếm số bit 1 trong:

# // // ```
# // // hour + minute
# // // ```
# // // 4. Nếu tổng bit 1 = `turnedOn` → lấy thời gian đó

# // // ---

# // // ### 6️⃣ Ví dụ minh họa bit

# // // Giả sử:

# // // ```
# // // hour = 3 -> 0011 (2 bit 1)
# // // minute = 5 -> 000101 (2 bit 1)
# // // ```

# // // Tổng = 4 LED sáng.

# // // ---

# // // ### 7️⃣ Tóm tắt đề bài

# // // * Có 10 LED (4 giờ + 6 phút)
# // // * Cho số LED đang sáng
# // // * Liệt kê tất cả thời gian hợp lệ
# // // * Dùng kiến thức:

# // // * Bit manipulation **hoặc**
# // // * Brute force + đếm bit

# // // ---

# // // Nếu bạn muốn, mình có thể:

# // // * Viết code Java / Python / C++
# // // * Giải từng bước brute force
# // // * Giải bằng backtracking / bitmask

# // // Bạn muốn mình giải theo cách nào?
