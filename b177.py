# # // 3714. Longest Balanced Substring II(13/02/2026)

# Ok 👍 — mình sẽ **giải thích thuật toán từ code Python bạn đưa** rồi viết lại **bản có chú thích chi tiết ngay trong code** để bạn học/trace dễ hơn.

# ---

# # 🧠 Ý tưởng tổng thể của thuật toán

# Chuỗi chỉ gồm: `a, b, c`
# Balanced substring khi:

# ```
# count(a) = count(b) = count(c)
# ```

# Nhưng đề II cho phép cả:

# | Loại balanced | Điều kiện        |
# | ------------- | ---------------- |
# | 1 ký tự       | chỉ 1 loại       |
# | 2 ký tự       | số lần bằng nhau |
# | 3 ký tự       | a = b = c        |

# Code Python này **gộp xử lý trong 1 vòng lặp**, thay vì tách 3 hàm như bản Java.

# ---

# # 🔑 Kỹ thuật chính

# ## 1️⃣ Prefix count 3 ký tự

# ```python
# ar=[0]*3
# ```

# Lưu số lần xuất hiện:

# ```
# ar[0] = count(a)
# ar[1] = count(b)
# ar[2] = count(c)
# ```

# ---

# ## 2️⃣ Chuẩn hóa prefix (normalize)

# ```python
# mi=min(ar)
# if(mi)>0:
#     ar[0]-=mi
#     ar[1]-=mi
#     ar[2]-=mi
# ```

# Ý nghĩa:

# Nếu tại 2 vị trí có:

# ```
# (a,b,c) = (5,3,2)
# (a,b,c) = (3,1,0)
# ```

# Sau khi trừ min:

# ```
# (3,1,0)
# (3,1,0)
# ```

# → trạng thái giống nhau
# → substring giữa chúng balanced 3 ký tự.

# ---

# ## 3️⃣ Hash trạng thái prefix

# ```python
# d={(0,0,0):-1}
# ```

# Map:

# ```
# (prefix_state) → first index
# ```

# Nếu gặp lại → balanced substring.

# ---

# # 🔎 Phần xử lý balanced 1 & 2 ký tự

# Dùng:

# ```python
# last=[-1,-1]
# last2=[-1,-1]
# findlongest()
# ```

# Ý tưởng:

# * Theo dõi block ký tự liên tiếp
# * Khi chỉ có 2 loại → gọi hàm prefix 2 ký tự

# ---

# 📌 Hàm `findlongest(st,en)`

# Tìm balanced trong đoạn chỉ có **2 ký tự**.

# Kỹ thuật:

# ```
# +1 / -1 prefix sum
# ```

# ---

# # ✍️ Code đã thêm chú thích chi tiết

# ```python
class Solution:
    def longestBalanced(self, s: str) -> int:

        # =====================================================
        # d: lưu trạng thái prefix 3 ký tự đầu tiên xuất hiện
        # key = (count_a, count_b, count_c) đã chuẩn hóa
        # =====================================================
        d = {(0,0,0):-1}

        # last: ký tự gần nhất và vị trí của nó
        last = [-1,-1]

        # last2: lưu 2 loại ký tự gần nhất
        last2 = [-1,-1]

        # vị trí bắt đầu đoạn chỉ có 2 ký tự
        last2i = 0

        a = ord('a')

        # mảng đếm số lần xuất hiện a,b,c
        ar = [0]*3

        ma = 0   # kết quả lớn nhất

        # =====================================================
        # HÀM TÌM BALANCED TRONG ĐOẠN CHỈ CÓ 2 KÝ TỰ
        # prefix sum +1 / -1
        # =====================================================
        def findlongest(st, en):

            swap = -1          # dùng để đổi +1 / -1 khi đổi ký tự
            d3 = {0:st-1}     # map prefix → first index
            total = 0
            mal = 0
            last = -1

            for i in range(st, en):

                v = ord(s[i]) - ord('a')

                # nếu đổi ký tự → đổi dấu
                if v != last:
                    last = v
                    swap *= -1

                total += swap

                # nếu prefix đã xuất hiện → balanced
                if total in d3:
                    mal = max(i - d3[total], mal)
                else:
                    d3[total] = i

            return mal

        # =====================================================
        # DUYỆT TOÀN BỘ CHUỖI
        # =====================================================
        for ind, le in enumerate(s):

            v = ord(le) - a

            # tăng đếm ký tự
            ar[v] += 1

            # ---------------------------------
            # CHUẨN HÓA PREFIX (3 ký tự)
            # ---------------------------------
            mi = min(ar)
            if mi > 0:
                ar[0] -= mi
                ar[1] -= mi
                ar[2] -= mi

            t = tuple(ar)

            # nếu trạng thái đã xuất hiện
            if t in d:
                ma = max(ind - d[t], ma)
            else:
                d[t] = ind

            # ---------------------------------
            # XỬ LÝ BLOCK KÝ TỰ (1 & 2 ký tự)
            # ---------------------------------
            if v != last[0]:

                # độ dài block 1 ký tự
                lelast = ind - last[1]
                ma = max(ma, lelast)

                # nếu xuất hiện ký tự thứ 3
                if v not in last2:

                    last2 = [last[0], v]

                    # xử lý balanced 2 ký tự đoạn trước
                    if (ind - last2i > ma):
                        ma = max(findlongest(last2i, ind), ma)

                    last2i = last[1]

                # cập nhật last
                last = [v, ind]

        # =====================================
        # XỬ LÝ ĐOẠN CUỐI
        # =====================================
        ma = max(findlongest(last2i, ind+1), ma)

        # block 1 ký tự cuối
        ma = max(ind+1 - last[1], ma)

        return ma
# ```

# ---

# # 📊 Tóm tắt tư duy thuật toán

# | Phần    | Kỹ thuật                 |
# | ------- | ------------------------ |
# | 3 ký tự | prefix count + normalize |
# | 2 ký tự | prefix sum ±1            |
# | 1 ký tự | đếm block liên tiếp      |
# | Hash    | lưu first occurrence     |

# ---

# # ⏱️ Độ phức tạp

# * Time: **O(n)**
# * Space: **O(n)**

# Vì mỗi prefix chỉ lưu 1 lần.

# ---

# 🔥 So sánh nhanh Java vs Python

# | Bản    | Cách làm        |
# | ------ | --------------- |
# | Java   | tách 3 hàm      |
# | Python | gộp 1 vòng      |
# | Java   | hash số lớn     |
# | Python | tuple normalize |

# ---

# Nếu bạn muốn mình làm tiếp, mình có thể:

# * Trace từng bước với ví dụ `"abccba"`
# * Vẽ bảng prefix normalize
# * Viết lại bản Python dễ hiểu hơn (ít trick)
# * So sánh với brute force O(n²)

# Bạn muốn mình giải sâu phần nào nhất?



# import java.util.*;

# /*
#  * Bài 3714 - Longest Balanced Substring II
#  * Chuỗi chỉ gồm: a, b, c
#  * Balanced = các ký tự xuất hiện số lần bằng nhau
#  */

# public class b178 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         String s = sc.nextLine();

#         int result = longestBalanced(s);

#         // In kết quả
#         System.out.println(result);

#         sc.close();
#     }

#     public static int longestBalanced(String s) {

#         int a = 0; // kết quả lớn nhất
#         char[] c = s.toCharArray(); // đổi sang mảng char cho nhanh

#         // =========================
#         // 1. XÉT BALANCED 1 KÝ TỰ
#         // =========================
#         // Tìm đoạn dài nhất chỉ gồm a hoặc b hoặc c
#         for (char x = 'a'; x <= 'c'; x++) {
#             a = Math.max(a, get1(c, x));
#         }

#         // =========================
#         // 2. XÉT BALANCED 2 KÝ TỰ
#         // =========================
#         // Các cặp: (a,b), (a,c), (b,c)
#         a = Math.max(
#                 Math.max(a, get2(c, 'a', 'b', a)),
#                 Math.max(get2(c, 'a', 'c', a),
#                         get2(c, 'b', 'c', a)));

#         // =========================
#         // 3. XÉT BALANCED 3 KÝ TỰ
#         // =========================
#         a = Math.max(a, get3(c, a));

#         return a;
#     }

#     // =========================================================
#     // HÀM 1 — BALANCED 1 KÝ TỰ
#     // Tìm đoạn dài nhất chỉ gồm ký tự x
#     // =========================================================
#     public static int get1(char[] c, char x) {

#         int a = 0; // max length
#         int b = 0; // độ dài đoạn hiện tại

#         for (char y : c) {

#             if (x == y) {
#                 b++; // gặp đúng ký tự → tăng độ dài
#             } else if (b > 0) {
#                 a = Math.max(a, b); // cập nhật max
#                 b = 0; // reset đoạn
#             }
#         }

#         // phòng trường hợp đoạn dài nhất ở cuối chuỗi
#         return Math.max(a, b);
#     }

#     // =========================================================
#     // HÀM 2 — BALANCED 2 KÝ TỰ
#     // count(x) = count(y)
#     // Dùng prefix sum
#     // =========================================================
#     public static int get2(char[] c, char x, char y, int max) {

#         int clear = -1; // vị trí reset khi gặp ký tự khác
#         int a = 0; // kết quả
#         int v = c.length; // prefix sum (offset để tránh âm)
#         int t;

#         // Map lưu vị trí xuất hiện đầu của mỗi prefix sum
#         int[] map = new int[(c.length << 1) + 1];
#         Arrays.fill(map, -2);

#         map[v] = -1; // prefix = 0 tại index -1

#         for (int i = 0; i < c.length; i++) {

#             // Nếu gặp ký tự KHÁC x,y → reset
#             if (c[i] != x && c[i] != y) {

#                 clear = i;
#                 v = c.length; // reset prefix
#                 map[v] = clear;
#             } else {

#                 // prefix sum
#                 if (c[i] == x)
#                     v++;
#                 else
#                     v--;

#                 // Nếu prefix chưa xuất hiện sau lần clear
#                 if (map[v] < clear) {
#                     map[v] = i;
#                 }

#                 // Nếu prefix = 0 → balanced từ clear
#                 else if (v == c.length) {
#                     t = i - clear;
#                     a = Math.max(a, t);
#                 }

#                 // balanced từ lần xuất hiện đầu
#                 else {
#                     t = i - map[v];
#                     a = Math.max(a, t);
#                 }
#             }
#         }

#         return a;
#     }

#     // =========================================================
#     // HÀM 3 — BALANCED 3 KÝ TỰ
#     // count(a) = count(b) = count(c)
#     // Dùng prefix sum 2 chiều (hash thành 1 số)
#     // =========================================================
#     public static int get3(char[] c, int max) {

#         int a = max;
#         int t;

#         int pow = 1_000_000;

#         // Giá trị hash ban đầu (offset lớn để tránh âm)
#         long v = 1_000_001_000_000L;

#         Map<Long, Integer> map = new HashMap<>();
#         map.put(v, -1);

#         for (int i = 0; i < c.length; i++) {

#             // Encode prefix
#             if (c[i] == 'a')
#                 v += pow + 1;
#             else if (c[i] == 'b')
#                 v -= pow;
#             else
#                 v--;

#             // Nếu trạng thái đã xuất hiện → balanced
#             if (map.containsKey(v)) {
#                 t = i - map.get(v);
#                 a = Math.max(a, t);
#             } else {
#                 map.put(v, i);
#             }
#         }

#         return a;
#     }
# }

# // Ok, mình sẽ **giải thích thuật toán trực tiếp từ code bạn đưa** (đây là lời
# // giải tối ưu cho bài *Longest Balanced Substring II* với chuỗi chỉ gồm `a, b,
# // c`).

# // ---

# // # 🧠 Ý tưởng tổng thể của lời giải

# // Balanced substring trong bài này được hiểu là:

# // > Substring mà **tất cả ký tự xuất hiện số lần bằng nhau**.

# // Vì chuỗi chỉ có 3 ký tự `a, b, c`, nên ta xét 3 trường hợp:

# // | Trường hợp | Điều kiện balanced |
# // | ---------- | ------------------- |
# // | 1 ký tự | chỉ gồm 1 loại |
# // | 2 ký tự | số lần x = số lần y |
# // | 3 ký tự | số lần a = b = c |

# // 👉 Vì vậy code chia làm 3 hàm:

# // * `get1()` → balanced 1 ký tự
# // * `get2()` → balanced 2 ký tự
# // * `get3()` → balanced 3 ký tự

# // Sau đó lấy **max độ dài**.

# // ---

# // # 1️⃣ Hàm `longestBalanced`

# // ```java
# // int a=0;
# // char[] c = s.toCharArray();
# // ```

# // * `a` = kết quả lớn nhất
# // * đổi string → char array cho nhanh

# // ---

# // ## 🔹 Xét balanced 1 ký tự

# // ```java
# // for(char x='a'; x<='c'; x++){
# // a=Math.max(a, get1(c, x));
# // }
# // ```

# // → thử từng ký tự `a, b, c`

# // ---

# // ## 🔹 Xét balanced 2 ký tự

# // ```java
# // a=Math.max(Math.max(a, get2(c,'a','b', a)),
# // Math.max(get2(c,'a','c', a), get2(c,'b','c', a)));
# // ```

# // → 3 cặp:

# // * (a,b)
# // * (a,c)
# // * (b,c)

# // ---

# // ## 🔹 Xét balanced 3 ký tự

# // ```java
# // a=Math.max(a, get3(c, a));
# // ```

# // ---

# // # 2️⃣ Hàm `get1` — Balanced 1 ký tự

# // ```java
# // private int get1(char[] c, char x)
# // ```

# // ### Ý nghĩa

# // Tìm substring dài nhất chỉ gồm **1 loại ký tự x**.

# // ---

# // ### Cách chạy

# // ```java
# // int a=0, b=0;
# // ```

# // * `b` = độ dài đoạn hiện tại
# // * `a` = max

# // ---

# // ### Duyệt chuỗi

# // ```java
# // for(char y:c){
# // if(x==y)b++;
# // ```

# // → gặp đúng ký tự → tăng độ dài

# // ---

# // ```java
# // else if(b>0){
# // if(a<b)a=b;
# // b=0;
# // }
# // ```

# // → gặp ký tự khác:

# // * cập nhật max
# // * reset đoạn

# // ---

# // ### Cuối vòng

# // ```java
# // return Math.max(a, b);
# // ```

# // → phòng trường hợp đoạn dài nhất ở cuối chuỗi

# // ---

# // # 3️⃣ Hàm `get2` — Balanced 2 ký tự

# // ```java
# // private int get2(char[] c, char x, char y, int max)
# // ```

# // Tìm substring mà:

# // ```
# // count(x) = count(y)
# // ```

# // ---

# // ## 🔑 Ý tưởng chính

# // Dùng **prefix sum + first occurrence**.

# // Quy ước:

# // * gặp `x` → +1
# // * gặp `y` → -1

# // Nếu tại 2 vị trí có cùng tổng → đoạn giữa balanced.

# // ---

# // ## Biến dùng

# // ```java
# // int clear = -1;
# // int a=0, v=c.length, t;
# // ```

# // * `v` = prefix sum (offset để không âm)
# // * `clear` = vị trí reset khi gặp ký tự khác x,y
# // * `a` = kết quả

# // ---

# // ## Map lưu first index

# // ```java
# // int[] map = new int[(c.length<<1)+1];
# // Arrays.fill(map, -2);
# // map[v]=-1;
# // ```

# // * Lưu vị trí đầu tiên mỗi giá trị prefix
# // * `-2` = chưa xuất hiện

# // ---

# // ## Duyệt chuỗi

# // ### Nếu gặp ký tự khác x,y

# // ```java
# // if(c[i]!=x&&c[i]!=y){
# // clear = i;
# // v=c.length;
# // map[v]=clear;
# // }
# // ```

# // → reset vì substring chỉ được chứa x,y

# // ---

# // ### Nếu gặp x hoặc y

# // ```java
# // if(c[i]==x)v++;
# // else v--;
# // ```

# // ---

# // ## Kiểm tra balanced

# // ### Nếu chưa có prefix này

# // ```java
# // if(map[v]<clear) map[v]=i;
# // ```

# // ---

# // ### Nếu đã có

# // ```java
# // else if(v==c.length){
# // t=i-clear;
# // }
# // else{
# // t=i-map[v];
# // }
# // ```

# // * Nếu tổng = 0 → tính từ `clear`
# // * Không → tính từ lần xuất hiện đầu

# // ---

# // # 4️⃣ Hàm `get3` — Balanced 3 ký tự

# // ```java
# // count(a) = count(b) = count(c)
# // ```

# // ---

# // ## 🔑 Ý tưởng

# // Ta không thể dùng 1 prefix sum → cần **2 hiệu số**:

# // Ví dụ lưu:

# // ```
# // (a-b, a-c)
# // ```

# // Nếu 2 vị trí có cùng cặp này → balanced.

# // ---

# // ## Nhưng code tối ưu bằng hash 1 số

# // ```java
# // int pow=1_000_000;
# // long v=1_000_001_000_000L;
# // ```

# // Tạo số lớn để encode 2 chiều.

# // ---

# // ## Quy ước cộng trừ

# // ```java
# // if(c[i]=='a') v+=pow+1;
# // else if(c[i]=='b') v-=pow;
# // else v--;
# // ```

# // Tương đương:

# // | Ký tự | (a-b, a-c) |
# // | ----- | ---------- |
# // | a | +1 , +1 |
# // | b | -1 , 0 |
# // | c | 0 , -1 |

# // ---

# // ## Map lưu first occurrence

# // ```java
# // Map<Long,Integer> map = new HashMap<>();
# // map.put(v, -1);
# // ```

# // ---

# // ## Duyệt

# // ```java
# // if(map.containsKey(v)){
# // t=i-map.get(v);
# // if(a<t)a=t;
# // }else map.put(v, i);
# // ```

# // Nếu trạng thái đã xuất hiện → balanced.

# // ---

# // # 📊 Độ phức tạp

# // | Hàm | Time |
# // | ---- | -------- |
# // | get1 | O(n) |
# // | get2 | O(n) × 3 |
# // | get3 | O(n) |

# // 👉 Tổng: **O(n)**

# // Rất tối ưu.

# // ---

# // # 🔥 Tóm tắt tư duy thuật toán

# // | Trường hợp | Kỹ thuật |
# // | ---------- | ------------------------- |
# // | 1 ký tự | Đếm đoạn liên tiếp |
# // | 2 ký tự | Prefix sum 1 chiều |
# // | 3 ký tự | Prefix sum 2 chiều (hash) |

# // ---

# // Nếu bạn muốn mình giải tiếp, mình có thể:

# // * Trace code từng bước với ví dụ cụ thể
# // * Vẽ bảng prefix sum
# // * So sánh với cách brute force O(n²)
# // * Viết lại bản dễ hiểu hơn

# // Bạn muốn mình đi sâu phần nào nhất?

# // Đây là bài toán về **chuỗi (string)** – yêu cầu bạn tìm **độ dài lớn nhất của
# // một “balanced substring”** (chuỗi con cân bằng) theo định nghĩa riêng của đề.

# // ---

# // ## 📌 Định nghĩa “balanced substring”

# // Một substring được gọi là **balanced** nếu:

# // * Nó chỉ gồm **2 ký tự khác nhau** (ví dụ: `0` và `1`, hoặc `a` và `b`… tùy
# // đề cho).
# // * Số lần xuất hiện của **hai ký tự này bằng nhau**.

# // 👉 Nói đơn giản:
# // Trong substring đó, **ký tự A xuất hiện bao nhiêu lần thì ký tự B cũng bấy
# // nhiêu lần**.

# // ---

# // ## 📥 Input (đầu vào)

# // * Một chuỗi `s` (string).
# // * Chuỗi chỉ gồm các ký tự nhất định (thường là nhị phân `0` và `1` trong
# // phiên bản phổ biến của bài).

# // ---

# // ## 📤 Output (đầu ra)

# // * Trả về **độ dài của balanced substring dài nhất** trong `s`.

# // ---

# // ## 🔎 Ví dụ minh họa

# // ### Ví dụ 1

# // ```
# // Input: s = "0011"
# // ```

# // Các substring cân bằng:

# // * `"01"` → 1 số 0, 1 số 1 → dài 2
# // * `"0011"` → 2 số 0, 2 số 1 → dài 4 ✅ lớn nhất

# // 👉 Output: `4`

# // ---

# // ### Ví dụ 2

# // ```
# // Input: s = "010011"
# // ```

# // Xét một số substring:

# // * `"01"` → cân bằng → 2
# // * `"0011"` → cân bằng → 4
# // * `"010011"` → 3 số 0, 3 số 1 → 6 ✅ lớn nhất

# // 👉 Output: `6`

# // ---

# // ### Ví dụ 3

# // ```
# // Input: s = "0001110"
# // ```

# // Balanced substring lớn nhất:

# // * `"000111"` → 3 số 0, 3 số 1 → dài 6 ✅

# // 👉 Output: `6`

# // ---

# // ## ⚠️ Lưu ý quan trọng

# // * Substring phải **liên tiếp** (không được bỏ ký tự).
# // * Không phải subsequence.
# // * Chỉ cần tìm **độ dài lớn nhất**, không cần trả substring.

# // ---

# // ## 🧠 Ý tưởng tư duy (intuitive)

# // Có vài cách nghĩ:

# // ### Cách 1 — Đếm prefix sum (phổ biến)

# // * Quy ước:

# // * `0 → -1`
# // * `1 → +1`
# // * Khi tổng prefix tại 2 vị trí bằng nhau → đoạn giữa là balanced.

# // ### Cách 2 — Nhóm block liên tiếp

# // Ví dụ:

# // ```
# // 0001110011
# // ```

# // Nhóm:

# // * `000` (3)
# // * `111` (3)
# // * `00` (2)
# // * `11` (2)

# // Balanced substring giữa 2 nhóm liên tiếp =
# // `2 × min(count1, count2)`

# // ---

# // ## 📊 Tóm tắt đề bài

# // | Thành phần | Ý nghĩa |
# // | ---------- | --------------------------- |
# // | Input | Chuỗi s |
# // | Yêu cầu | Tìm substring liên tiếp |
# // | Điều kiện | 2 ký tự xuất hiện bằng nhau |
# // | Output | Độ dài lớn nhất |

# // ---

# // Nếu bạn muốn, mình có thể:

# // * Giải chi tiết từng bước bằng ví dụ lớn
# // * So sánh với bài **Longest Balanced Substring I**
# // * Viết code Java / Python / C++

# // Bạn muốn mình giải theo hướng nào tiếp?
