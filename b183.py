# //  Bài **Count Binary Substrings**(19/02/2026)

# Ok 👌 mình sẽ:

# 1. **Giải thích thuật toán Python của bài 696**
# 2. **Thêm chú thích trực tiếp vào code**
# 3. Giải thích theo đúng tên biến `now / prev / flag` bạn đang dùng

# ---

# # 🧠 Ý tưởng thuật toán (giống Java bạn học)

# Ta **không duyệt mọi substring** (O(n²)).

# Thay vào đó:

# * Đếm độ dài các nhóm `0` và `1` liên tiếp
# * Với mỗi cặp nhóm kề nhau → cộng:

# ```
# min(độ dài nhóm trước, nhóm hiện tại)
# ```

# ---

# # 📊 Ví dụ trực quan

# ```
# s = "00110011"

# Nhóm:
# 00 | 11 | 00 | 11
#  2    2    2    2

# Kết quả:
# 2 + 2 + 2 = 6
# ```

# ---

# # 🔤 Ý nghĩa biến trong code

# | Biến   | Ý nghĩa                 |
# | ------ | ----------------------- |
# | `now`  | Độ dài nhóm hiện tại    |
# | `prev` | Độ dài nhóm trước       |
# | `flag` | Ký tự của nhóm hiện tại |
# | `res`  | Tổng substring hợp lệ   |

# ---

# # 🧾 Code đã thêm chú thích chi tiết

# ```python
class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        # Nếu chuỗi rỗng → không có substring hợp lệ
        if not s:
            return 0

        # now  : độ dài nhóm hiện tại
        # flag : ký tự của nhóm hiện tại (0 hoặc 1)
        now, flag = 0, s[0]

        # prev : độ dài nhóm trước đó
        prev = 0

        # res : tổng số substring hợp lệ
        res = 0

        # Duyệt từng ký tự trong chuỗi
        for x in s:

            # Nếu ký tự hiện tại giống nhóm đang xét
            if x == flag:

                # Tăng độ dài nhóm hiện tại
                now += 1

            else:
                # Nếu khác → đổi nhóm

                # Cộng số substring hợp lệ giữa 2 nhóm
                # Công thức: min(nhóm trước, nhóm hiện tại)
                res += min(now, prev)

                # Cập nhật nhóm trước = nhóm hiện tại
                prev = now

                # Reset nhóm hiện tại = 1 (bắt đầu nhóm mới)
                now = 1

                # Cập nhật ký tự nhóm mới
                flag = x

        # Sau khi duyệt xong → còn cặp nhóm cuối chưa cộng
        res += min(now, prev)

        # Trả kết quả
        return res
# ```

# ---

# # 🔁 Chạy tay ví dụ

# Chuỗi:

# ```
# s = "0011"
# ```

# ---

# ## Bước nhóm

# | Ký tự | flag | now | prev | res |
# | ----- | ---- | --- | ---- | --- |
# | 0     | 0    | 1   | 0    | 0   |
# | 0     | 0    | 2   | 0    | 0   |
# | 1     | đổi  | 1   | 2    | 0   |
# | 1     | 1    | 2   | 2    | 0   |

# Kết thúc:

# ```
# res += min(2,2) = 2
# ```

# 👉 Kết quả = **2**

# Substring:

# ```
# 01
# 0011
# ```

# ---

# # ⚠️ Vì sao dùng `min(now, prev)` ?

# Giả sử:

# ```
# 0001111
#  3   4
# ```

# Substring hợp lệ tối đa:

# ```
# 000111  (3 cặp)
# ```

# Không thể lấy 4 vì thiếu 0.

# Nên phải lấy nhóm ngắn hơn → `min`.

# ---

# # ⏱️ Độ phức tạp

# * Time: **O(n)** — duyệt 1 lần
# * Space: **O(1)** — chỉ dùng biến

# ---

# 🧩 So sánh nhanh Java vs Python

# | Java         | Python | Ý nghĩa       |
# | ------------ | ------ | ------------- |
# | sequence     | now    | nhóm hiện tại |
# | lastSequence | prev   | nhóm trước    |
# | sChar[i]     | x      | ký tự         |
# | count        | res    | kết quả       |

# ---

# Nếu bạn muốn mình làm tiếp:

# * Vẽ timeline biến chạy từng bước
# * Viết brute force để so sánh
# * Chuyển Python → Java / C++
# * Giải thích vì sao không cần lưu mảng group

# Bạn muốn đào sâu phần nào?


# // Ok👍mình sẽ**thêm hàm`main`dùng`Scanner`+chú thích chi tiết từng dòng**vào đúng style code bạn đang viết.

# // ---

# // ```java

# import java.util.*;

# public class b184 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         String s = sc.nextLine();

#         // Gọi hàm đếm substring
#         int result = countBinarySubstrings(s);

#         // In kết quả
#         System.out.println("So binary substring hop le = " + result);

#         // Đóng Scanner
#         sc.close();
#     }

#     // Hàm đếm số binary substring hợp lệ
#     public static int countBinarySubstrings(String s) {

#         // Chuyển chuỗi sang mảng ký tự để duyệt nhanh hơn
#         var sChar = s.toCharArray();

#         // Biến lưu tổng số substring hợp lệ
#         var count = 0;

#         // Độ dài nhóm hiện tại (current sequence)
#         var sequence = 1;

#         // Độ dài nhóm trước đó (previous sequence)
#         var lastSequence = 0;

#         // Duyệt từ ký tự thứ 2 → hết chuỗi
#         for (int left = 1; left < sChar.length; left++) {

#             // Nếu cùng ký tự → vẫn cùng nhóm
#             if (sChar[left] == sChar[left - 1]) {

#                 // Tăng độ dài nhóm hiện tại
#                 sequence += 1;

#             } else {
#                 // Nếu khác ký tự → đổi nhóm

#                 // Cộng số substring hợp lệ giữa 2 nhóm kề nhau
#                 // Công thức: min(nhóm trước, nhóm hiện tại)
#                 count += Math.min(lastSequence, sequence);

#                 // Cập nhật nhóm trước = nhóm hiện tại
#                 lastSequence = sequence;

#                 // Reset nhóm hiện tại = 1 (bắt đầu nhóm mới)
#                 sequence = 1;
#             }
#         }

#         // Sau khi duyệt xong vẫn còn 1 cặp nhóm cuối chưa cộng
#         count += Math.min(lastSequence, sequence);

#         // Trả về kết quả
#         return count;
#     }
# }

# // ---

# // #🧪

# // Ví dụ
# // chạy chương trình

# // **Input**

# // ```
# // Nhap chuoi
# // nhi phan:00110011```

# // **Output**

# // ```
# // So binary
# // substring hop le=6```

# // ---

# // #📌
# // Tóm tắt
# // luồng chạy

# // 1.`main()` nhập chuỗi bằng `Scanner`
# // 2. Gọi `countBinarySubstrings(s)`
# // 3. Hàm xử lý:

# // * Đếm độ dài từng nhóm 0/1
# // * Cộng `min(group trước, group sau)`
# // 4. Trả kết quả về `main`
# // 5. In ra màn hình

# // ---

# // Nếu bạn muốn mình:

# // * Viết lại dùng `while` thay `for`
# // * Thêm kiểm tra input

# // hợp lệ (chỉ 0/1)
# // * In luôn các substring hợp lệ để debug

# // Cứ nói mình làm tiếp 👍

# // Ok mình sẽ **giải thích thuật toán trong đoạn code của bạn theo từng bước, dễ
# // hiểu + bám sát biến trong code** 👇

# // ---

# // # 🧠 Ý tưởng tổng thể

# // Ta **không liệt kê substring** (vì O(n²) rất chậm).

# // Thay vào đó:

# // 👉 Chỉ cần đếm **độ dài các nhóm 0/1 liên tiếp**
# // Rồi cộng:

# // ```
# // min(nhóm trước, nhóm sau)
# // ```

# // ---

# // # 🔤 Ý nghĩa các biến trong code

# // ```java
# // var sChar = s.toCharArray();
# // ```

# // ➡️ Chuyển chuỗi thành mảng ký tự để duyệt nhanh hơn.

# // ---

# // ```java
# // var count = 0;
# // ```

# // ➡️ Tổng số substring hợp lệ.

# // ---

# // ```java
# // var sequence = 1;
# // ```

# // ➡️ Độ dài **nhóm hiện tại** (current group).

# // Ví dụ đang duyệt `"000"` → sequence = 3

# // ---

# // ```java
# // var lastSequence = 0;
# // ```

# // ➡️ Độ dài **nhóm trước đó**.

# // Dùng để tính:

# // ```
# // min(lastSequence, sequence)
# // ```

# // ---

# // # 🔁 Vòng lặp chính

# // ```java
# // for (int left = 1; left < sChar.length; left++)
# // ```

# // Duyệt từ ký tự thứ 2 → so với ký tự trước.

# // ---

# // ## 📌 TH1 — Cùng ký tự

# // ```java
# // if (sChar[left] == sChar[left - 1]) {
# // sequence += 1;
# // }
# // ```

# // 👉 Vẫn cùng nhóm → tăng độ dài nhóm hiện tại.

# // Ví dụ:

# // ```
# // 000
# // ↑
# // sequence tăng dần: 1 → 2 → 3
# // ```

# // ---

# // ## 📌 TH2 — Khác ký tự (đổi nhóm)

# // ```java
# // else {
# // count += Math.min(lastSequence, sequence);
# // lastSequence = sequence;
# // sequence = 1;
# // }
# // ```

# // Khi đổi từ `0 → 1` hoặc `1 → 0`:

# // ### Bước 1 — Cộng kết quả

# // ```java
# // count += Math.min(lastSequence, sequence);
# // ```

# // Vì ta đã có 2 nhóm kề nhau:

# // * Nhóm trước: `lastSequence`
# // * Nhóm hiện tại: `sequence`

# // Số substring hợp lệ giữa 2 nhóm = min(2 nhóm)

# // ---

# // ### Bước 2 — Cập nhật nhóm trước

# // ```java
# // lastSequence = sequence;
# // ```

# // Nhóm hiện tại trở thành nhóm trước.

# // ---

# // ### Bước 3 — Reset nhóm mới

# // ```java
# // sequence = 1;
# // ```

# // Bắt đầu đếm nhóm mới.

# // ---

# // # 🧾 Ví dụ chạy tay

# // Chuỗi:

# // ```
# // s = "00110011"
# // ```

# // ---

# // ## Bước nhóm

# // | Ký tự | sequence | lastSequence | count |
# // | ----- | -------- | ------------ | ----- |
# // | 0 | 1 | 0 | 0 |
# // | 0 | 2 | 0 | 0 |
# // | 1 | 1 | 2 | 0 |
# // | 1 | 2 | 2 | 0 |
# // | đổi | | | +2 |

# // Giải thích:

# // * Nhóm `00` và `11`
# // * min(2,2) = 2

# // ---

# // Tiếp:

# // | Nhóm | min | count |
# // | ------- | --- | ----- |
# // | 11 & 00 | 2 | 4 |
# // | 00 & 11 | 2 | 6 |

# // ---

# // # ⚠️ Dòng quan trọng cuối

# // ```java
# // count += Math.min(lastSequence, sequence);
# // ```

# // Tại sao cần?

# // Vì vòng lặp **không cộng cho cặp nhóm cuối**.

# // Ví dụ:

# // ```
# // 000111
# // ```

# // Đổi nhóm ở giữa → đã cộng
# // Nhưng sau khi loop kết thúc → chưa cộng lần cuối.

# // Nên phải cộng thêm ngoài vòng lặp.

# // ---

# // # 📊 Độ phức tạp

# // * Time: **O(n)** — duyệt 1 lần
# // * Space: **O(1)** — không dùng mảng phụ

# // ---

# // # 🧩 Tóm tắt thuật toán

# // 1. Đếm độ dài nhóm hiện tại (`sequence`)
# // 2. Khi đổi nhóm:

# // * Cộng `min(lastSequence, sequence)`
# // * Cập nhật `lastSequence`
# // 3. Reset nhóm mới
# // 4. Sau loop → cộng lần cuối

# // ---

# // # 🔍 Nhìn trực quan

# // Chuỗi:

# // ```
# // 00110011
# // ```

# // Nhóm:

# // ```
# // 00 | 11 | 00 | 11
# // 2 2 2 2
# // ```

# // Tính:

# // ```
# // min(2,2) + min(2,2) + min(2,2)
# // = 2 + 2 + 2
# // = 6
# // ```

# // ---

# // Nếu bạn muốn mình giải thích thêm:

# // * Vì sao công thức `min` đúng (chứng minh)
# // * So sánh với brute force O(n²)
# // * Viết lại bằng while loop (theo style bạn hay dùng)

# // Bạn muốn đào sâu phần nào tiếp?

# // ---

# // ## 🧠 Yêu cầu đề bài

# // Cho một chuỗi nhị phân `s` (chỉ gồm ký tự `'0'` và `'1'`).

# // Hãy **đếm số lượng substring (chuỗi con liên tiếp)** thỏa mãn:

# // 1. Số lượng `0` và `1` **bằng nhau**
# // 2. Các ký tự `0` và `1` trong substring phải **đứng thành từng nhóm liên
# // tiếp**

# // ---

# // ## 🔎 Hiểu “substring hợp lệ” là gì?

# // Substring hợp lệ phải có dạng như:

# // * `"01"` hoặc `"10"`
# // * `"0011"` hoặc `"1100"`
# // * `"000111"` hoặc `"111000"`

# // 👉 Tức là:

# // * Một nhóm `0` liên tiếp + một nhóm `1` liên tiếp (hoặc ngược lại)
# // * Độ dài 2 nhóm phải bằng nhau

# // ---

# // ## 📌 Ví dụ 1

# // **Input:**
# // `s = "00110011"`

# // Ta liệt kê các substring hợp lệ:

# // * `"0011"`
# // * `"01"`
# // * `"1100"`
# // * `"10"`
# // * `"0011"`
# // * `"01"`

# // 👉 Tổng cộng: **6**

# // **Output:** `6`

# // ---

# // ## 📌 Ví dụ 2

# // **Input:**
# // `s = "10101"`

# // Các substring hợp lệ:

# // * `"10"`
# // * `"01"`
# // * `"10"`
# // * `"01"`

# // 👉 Tổng: **4**

# // **Output:** `4`

# // ---

# // ## ⚠️ Lưu ý quan trọng

# // Substring **phải liên tiếp** nhé (không được nhảy vị trí).

# // Ví dụ trong `"0011"`:

# // * `"01"` ở giữa là hợp lệ (liên tiếp)
# // * Nhưng lấy `0` đầu và `1` cuối → ❌ không tính

# // ---

# // ## 🧩 Ý tưởng cốt lõi của bài

# // Thay vì xét mọi substring (rất chậm), ta quan sát:

# // Chuỗi nhị phân luôn có dạng các **group**:

# // Ví dụ:

# // `s = "0011100"`

# // Nhóm lại:

# // * `"00"` → độ dài 2
# // * `"111"` → độ dài 3
# // * `"00"` → độ dài 2

# // Ta có mảng độ dài nhóm: `[2, 3, 2]`

# // ---

# // ### 🔢 Công thức đếm

# // Số substring hợp lệ giữa **2 nhóm kề nhau** là:

# // ```
# // min(độ dài nhóm trước, độ dài nhóm sau)
# // ```

# // Vì chỉ ghép được tối đa bằng nhóm ngắn hơn.

# // ---

# // ### Áp dụng ví dụ

# // `[2, 3, 2]`

# // * Giữa 2 và 3 → min = 2
# // * Giữa 3 và 2 → min = 2

# // Tổng = `2 + 2 = 4`

# // ---

# // ## 🪜 Tóm tắt cách làm

# // 1. Duyệt chuỗi, đếm độ dài từng nhóm `0` / `1`
# // 2. Lưu vào list
# // 3. Với mỗi cặp nhóm kề nhau:

# // * Cộng `min(group[i], group[i+1])`
# // 4. Tổng là kết quả

# // ---

# // ## 🧾 Ví dụ minh họa nhanh

# // `s = "00011100"`

# // Nhóm:

# // * 3 (`000`)
# // * 3 (`111`)
# // * 2 (`00`)

# // Tính:

# // * min(3,3) = 3
# // * min(3,2) = 2

# // 👉 Kết quả = **5**

# // ---

# // Nếu bạn muốn, mình có thể:

# // * Giải từng bước bằng hình minh họa
# // * Viết code Java / Python / C++
# // * Phân tích độ phức tạp O(n)

# // Bạn muốn mình làm phần nào tiếp theo?
