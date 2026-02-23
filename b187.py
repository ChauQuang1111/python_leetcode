# # // // ### 📘 Check If a String Contains All Binary Codes of Size K(23/02/2026)


# Mình sẽ giải thích **3 cách** từ dễ hiểu → tối ưu, rồi thêm chú thích chi tiết vào code cách 3 (bitmask – nhanh nhất).

# ---

# # 🥉 Cách 1 – Dùng substring + set

# ```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        vis = set()                 # Lưu các substring độ dài k đã gặp

        for i in range(n-k+1):      # Duyệt tất cả cửa sổ độ dài k
            tmp = s[i:i+k]          # Lấy substring
            if tmp in vis:
                continue
            vis.add(tmp)            # Thêm vào set

        return len(vis) == 2**k     # Kiểm tra có đủ 2^k chuỗi không
# ```

# ## 🧠 Ý tưởng

# * Có tất cả `2^k` chuỗi nhị phân độ dài k.
# * Duyệt từng substring độ dài k.
# * Đưa vào set.
# * Nếu size set == `2^k` → đủ.

# ## ⏱ Độ phức tạp

# * Time: **O(n * k)** (vì cắt chuỗi tốn O(k))
# * Space: O(2^k)

# ---

# # 🥈 Cách 2 – Dùng deque (Sliding Window)

# ```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        from collections import deque

        n = len(s)
        s = list(s)

        cur = deque(s[:k])      # Cửa sổ đầu tiên
        vis = set()
        vis.add(tuple(cur))     # Thêm vào set

        for i in range(k, n):
            cur.popleft()       # Bỏ phần tử trái
            cur.append(s[i])    # Thêm phần tử phải

            x = tuple(cur)
            if x in vis:
                continue
            vis.add(x)

        return len(vis) == 2 ** k
# ```

# ## 🧠 Ý tưởng

# * Không cắt substring nữa.
# * Dùng cửa sổ trượt.
# * Mỗi lần chỉ bỏ trái, thêm phải.

# ## ⏱ Độ phức tạp

# * Time: **O(n)**
# * Nhưng vẫn phải convert tuple → hơi tốn chi phí.

# ---

# # 🥇 Cách 3 – Bitmask (TỐI ƯU NHẤT)

# 🔥 Đây là cách nhanh nhất.

# ---

# ## 💡 Ý tưởng chính

# Mỗi chuỗi nhị phân độ dài k có thể biểu diễn bằng một số nguyên:

# Ví dụ k = 3:

# | Chuỗi | Giá trị |
# | ----- | ------- |
# | 000   | 0       |
# | 001   | 1       |
# | 010   | 2       |
# | 011   | 3       |
# | 100   | 4       |
# | 101   | 5       |
# | 110   | 6       |
# | 111   | 7       |

# → Tổng cộng `2^k` số.

# Ta dùng:

# ```
# mask = số nguyên đại diện cho cửa sổ hiện tại
# ```

# ---

# # 🧠 Giải thích chi tiết code (có chú thích đầy đủ)

# ```python
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)

        # Nếu chuỗi quá ngắn thì chắc chắn không đủ
        if n < k:
            return False

        # need = tổng số chuỗi nhị phân độ dài k
        # 1 << k = 2^k
        need = 1 << k

        # Nếu số cửa sổ có thể tạo < need thì chắc chắn thiếu
        if n - k + 1 < need:
            return False

        # Mảng đánh dấu đã gặp số nào chưa
        seen = [False] * need

        mask = 0          # Lưu giá trị nhị phân hiện tại
        full = need - 1   # Bitmask giữ lại k bit cuối (vd 111 nếu k=3)
        cnt = 0           # Đếm số chuỗi khác nhau đã gặp

        for i, ch in enumerate(s):

            # Dịch trái 1 bit
            # & full để chỉ giữ lại k bit cuối
            # | (ch == '1') để thêm bit mới vào
            mask = ((mask << 1) & full) | (ch == '1')

            # Khi chưa đủ k ký tự đầu tiên thì bỏ qua
            if i < k - 1:
                continue

            # Nếu chuỗi này chưa từng thấy
            if not seen[mask]:
                seen[mask] = True
                cnt += 1

                # Nếu đã đủ tất cả chuỗi
                if cnt == need:
                    return True

        return False


# ---

# # 🔥 Giải thích dòng quan trọng nhất

# ```python
# mask = ((mask << 1) & full) | (ch == '1')
# ```

# Giả sử k = 3
# full = 111 (7)

# Ví dụ đang có:

# ```
# mask = 101
# ```

# Thêm bit mới = 1

# ### Bước 1: shift trái

# ```
# 101 << 1 = 1010
# ```

# ### Bước 2: giữ lại 3 bit cuối

# ```
# 1010 & 111 = 010
# ```

# ### Bước 3: thêm bit mới

# ```
# 010 | 1 = 011
# ```

# → cửa sổ mới = 011

# ⚡ Không cần substring
# ⚡ Không cần tuple
# ⚡ Không cần set
# ⚡ Tất cả là phép toán bit

# ---

# # 🚀 So sánh 3 cách

# | Cách      | Time  | Nhanh    |
# | --------- | ----- | -------- |
# | Substring | O(nk) | ❌        |
# | Deque     | O(n)  | ⚠        |
# | Bitmask   | O(n)  | ✅ TỐI ƯU |

# ---

# # 🎯 Tóm lại

# Bài này bản chất là:

# > Kiểm tra có đủ 2^k mẫu khác nhau hay không.

# Cách bitmask giúp:

# * Đại diện mỗi chuỗi bằng 1 số
# * Cập nhật cửa sổ trong O(1)
# * Không tạo object mới

# ---

# Nếu bạn muốn mình:

# * Vẽ minh họa từng bước mask chạy với ví dụ cụ thể
# * Giải thích tại sao `(ch == '1')` hoạt động được
# * Hoặc viết lại theo phong cách dễ hiểu hơn cho người mới

# Nói mình biết nhé 🔥




# // Ok mình sẽ:

# // 1.✅Giải thích thuật toán từng bước 2.✅Thêm chú thích trực tiếp vào code 3.✅Viết thêm hàm`main`dùng`Scanner`4.✅Giải thích vì sao dùng bitmask lại tối ưu

# // ---

# // #🔥Ý tưởng thuật toán(Bitmask+Sliding Window)

# // Thay vì dùng`substring`(tốn O(k)mỗi lần),ta:

# // *Dùng**số nguyên`hash`**để biểu diễn chuỗi nhị phân độ dài k*Dùng**bit manipulation**để cập nhật cửa sổ trượt*Mỗi substring độ dài k sẽ tương ứng với 1 số từ`0→2^k-1`

# // ---

# // ##🎯Ý nghĩa các biến quan trọng

# // |Biến|Ý nghĩa||--------------------|------------------------------------||`need=1<<k`|Tổng số chuỗi cần có=2^k||`allOnes=need-1`|Bitmask giữ lại k bit cuối||`hash`|Giá trị nhị phân hiện tại của cửa sổ||`seen[]`|Đánh dấu đã gặp substring nào||`count`|Đếm số chuỗi khác nhau đã gặp|

# // ---

# // #💡Giải thích từng dòng quan trọng

# // ###1 ️⃣`1<<k`

# // Ví dụ k=3

# // ```1<<3=1000(nhị phân)=8```

# // →Có 8 chuỗi nhị phân độ dài 3

# // ---

# // ###2 ️⃣Cách cập nhật hash

# // ```java hash=((hash<<1)&allOnes)|(s.charAt(i)-'0');```

# // Giả sử k=3

# // Window đang là:`101`

# // ```hash=101(5)```

# // Thêm bit mới=1

# // B1:shift trái

# // ```101<<1=1010```

# // B2:&allOnes(111)để giữ lại 3 bit cuối

# // ```1010&111=010```

# // B3:OR bit mới

# // ```010|1=011```

# // →window mới=011

# // 👉Không cần substring→cực nhanh O(1)

# // ---

# // #✅Code có chú thích+main dùng Scanner

# // ```java

# import java.util.*;

# public class b188 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         String s = sc.nextLine();

#         // Nhập k
#         int k = sc.nextInt();

#         boolean result = hasAllCodes(s, k);

#         System.out.println(result);

#         sc.close();
#     }

#     // Hàm kiểm tra có đủ tất cả chuỗi nhị phân độ dài k không
#     public static boolean hasAllCodes(String s, int k) {
#         // need = 2^k (tổng số chuỗi nhị phân độ dài k)
#         int need = 1 << k;

#         int n = s.length();

#         // Nếu chuỗi quá ngắn thì chắc chắn false
#         // n-k+1 là số substring độ dài k có thể tạo
#         if (n < k || n - k + 1 < need)
#             return false;

#         // Mảng đánh dấu đã gặp chuỗi nào chưa
#         boolean[] seen = new boolean[need];

#         int hash = 0; // giá trị nhị phân hiện tại của cửa sổ
#         int allOnes = need - 1; // bitmask giữ lại k bit cuối
#         int count = 0; // đếm số chuỗi khác nhau đã thấy

#         for (int i = 0; i < n; i++) {

#             // Dịch trái 1 bit để thêm bit mới
#             // & allOnes để chỉ giữ lại k bit cuối
#             // OR bit hiện tại (0 hoặc 1)
#             hash = ((hash << 1) & allOnes) | (s.charAt(i) - '0');

#             // Khi đã đủ k ký tự đầu tiên
#             if (i >= k - 1) {

#                 // Nếu chuỗi này chưa từng gặp
#                 if (!seen[hash]) {
#                     seen[hash] = true;
#                     count++;

#                     // Nếu đã đủ 2^k chuỗi
#                     if (count == need)
#                         return true;
#                 }
#             }
#         }

#         return false;
#     }

# }

# // O(n)
# // ```

# // Mỗi ký tự xử lý 1 lần

# // ### Space Complexity:

# // ```
# // O(2^k)
# // ```

# // Dùng mảng boolean

# // ---

# // # 🧠 Vì sao cách này mạnh hơn substring?

# // | Cách | Độ phức tạp |
# // | --------- | ----------- |
# // | substring | O(n * k) |
# // | bitmask | O(n) |

# // Khi k lớn → substring sẽ chậm rõ rệt

# // ---

# // Nếu bạn muốn mình:

# // * Vẽ sơ đồ bit shifting cho bạn dễ hình dung hơn
# // * Viết lại theo style bạn thích dùng while thay for
# // * Giải thích lại phần `& allOnes` theo cách trực quan hơn

# // Nói mình biết nhé 🔥

# // (LeetCode 1461)

# // ---

# // ## 🧠 Đề bài nói gì?

# // Bạn được cho:

# // * Một **chuỗi nhị phân** `s` (chỉ gồm `'0'` và `'1'`)
# // * Một số nguyên `k`

# // 👉 Nhiệm vụ:
# // Kiểm tra xem **tất cả các chuỗi nhị phân có độ dài k** có xuất hiện trong `s`
# // hay không.

# // Nếu **có đủ tất cả** → trả về `true`
# // Nếu **thiếu ít nhất một chuỗi** → trả về `false`

# // ---

# // ## 🔍 Ví dụ 1

# // ```
# // Input: s = "00110110", k = 2
# // Output: true
# // ```

# // ### Vì sao?

# // Với `k = 2`, tất cả chuỗi nhị phân độ dài 2 là:

# // ```
# // 00
# // 01
# // 10
# // 11
# // ```

# // Bây giờ kiểm tra trong `s = "00110110"`:

# // | Vị trí | Substring độ dài 2 |
# // | ------ | ------------------ |
# // | 0-1 | 00 |
# // | 1-2 | 01 |
# // | 2-3 | 11 |
# // | 3-4 | 10 |
# // | 4-5 | 01 |
# // | 5-6 | 11 |
# // | 6-7 | 10 |

# // ✅ Ta thấy đủ: `00, 01, 10, 11`
# // → Trả về **true**

# // ---

# // ## 🔍 Ví dụ 2

# // ```
# // Input: s = "0110", k = 2
# // Output: false
# // ```

# // Các chuỗi cần có vẫn là:

# // ```
# // 00
# // 01
# // 10
# // 11
# // ```

# // Substring trong `"0110"`:

# // ```
# // 01
# // 11
# // 10
# // ```

# // ❌ Thiếu `00`
# // → Trả về **false**

# // ---

# // ## 🎯 Ý nghĩa bài toán

# // Với độ dài `k`, sẽ có:

# // [
# // 2^k
# // ]

# // chuỗi nhị phân khác nhau.

# // Ví dụ:

# // * k = 1 → 2 chuỗi (0,1)
# // * k = 2 → 4 chuỗi
# // * k = 3 → 8 chuỗi
# // * k = 4 → 16 chuỗi

# // 👉 Bạn cần kiểm tra xem chuỗi `s` có chứa đủ **2^k** substring khác nhau hay
# // không.

# // ---

# // ## ⚠ Điều quan trọng cần hiểu

# // Nếu:

# // ```
# // s.length() < k
# // ```

# // → chắc chắn trả về `false`
# // (vì không thể tạo substring độ dài k)

# // ---

# // ## 💡 Tư duy đơn giản

# // 1. Duyệt từ i = 0 đến s.length - k
# // 2. Lấy substring độ dài k
# // 3. Lưu vào HashSet
# // 4. Nếu size của HashSet == 2^k → true
# // 5. Ngược lại → false

# // ---

# // ## 🧠 Tóm lại

# // Bài này kiểm tra:

# // > Chuỗi s có chứa đủ tất cả các chuỗi nhị phân độ dài k hay không?

# // Nó thuộc dạng:

# // * Sliding window
# // * HashSet
# // * Bit manipulation (cách tối ưu hơn)

# // ---

# // Nếu bạn muốn mình giải thích thêm:

# // * 🚀 Cách tối ưu O(n)
# // * 🚀 Cách dùng bitmask thay vì substring
# // * 🚀 Code Java (theo style bạn thích dùng Scanner + while)

# // Bạn muốn mình đi theo hướng nào?
