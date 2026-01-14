# # // Separate Squares II(14/01/2026)
# # // **Separate Squares II – Giải thích đề bài (bằng tiếng Việt)**
# # // Ok, mình sẽ làm **3 việc rõ ràng** cho bạn:
# Dưới đây mình **giải thích thuật toán + thêm chú thích trực tiếp vào code Python** cho bài
# **3454. Separate Squares II** (đúng theo code bạn đưa).

# ---

# # 1️⃣ Ý tưởng thuật toán (hiểu bản chất)

# ## 🎯 Mục tiêu

# Tìm đường thẳng **y = k** sao cho:

# > **Diện tích hợp (union)** của các hình vuông **phía dưới** đường thẳng
# > = **phía trên**

# ⚠️ Lưu ý:

# * **Không** cộng chồng diện tích
# * Phải tính **diện tích union** của các hình vuông

# ---

# ## 🧠 Tư duy chính: Sweep Line theo trục Y

# ### Bước 1: Biến mỗi hình vuông thành 2 sự kiện

# Với hình vuông `(x, y, l)`:

# * Bắt đầu phủ tại `y`
# * Kết thúc phủ tại `y + l`

# Mỗi sự kiện chứa:

# ```
# (y, loại, x1, x2)
# ```

# * `loại = +1`: thêm đoạn [x1, x2]
# * `loại = -1`: xóa đoạn [x1, x2]

# ---

# ### Bước 2: Quét từ dưới lên theo Y

# Giữa 2 sự kiện Y liên tiếp:

# * Tập các đoạn X **không đổi**
# * Tính **union độ dài X**
# * Diện tích lát:

# ```
# height * union_width
# ```

# Lưu từng lát vào `areas`

# ---

# ### Bước 3: Tìm vị trí chia đôi diện tích

# * Tổng diện tích = `total`
# * Mục tiêu = `total / 2`
# * Duyệt từng lát:

#   * Nếu vượt nửa → nội suy:

# ```
# y + (phần thiếu) / width
# ```

# ---

# # 2️⃣ Code có chú thích chi tiết

# ```python
from typing import List
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:

        # ===== 1. Tạo sự kiện sweep line theo trục Y =====
        events = []
        for x, y, l in squares:
            # Bắt đầu hình vuông
            events.append((y, 1, x, x + l))
            # Kết thúc hình vuông
            events.append((y + l, -1, x, x + l))

        # Sắp xếp theo y tăng dần
        events.sort()

        # Danh sách các đoạn X đang hoạt động
        xs = []

        prev_y = events[0][0]
        total = 0          # tổng diện tích union
        areas = []         # lưu từng lát: (y_bắt_đầu, chiều_cao, độ_rộng)

        # ===== 2. Hàm tính độ dài union của các đoạn X =====
        def union_len(intervals):
            intervals.sort()
            res = 0
            end = -10**30

            for a, b in intervals:
                if a > end:
                    res += b - a
                    end = b
                elif b > end:
                    res += b - end
                    end = b
            return res

        # ===== 3. Sweep line theo Y =====
        for y, typ, x1, x2 in events:
            # Nếu có khoảng Y hợp lệ
            if y > prev_y and xs:
                h = y - prev_y               # chiều cao lát
                w = union_len(xs)            # độ rộng union X
                areas.append((prev_y, h, w))
                total += h * w

            # Cập nhật các đoạn X đang phủ
            if typ == 1:
                xs.append((x1, x2))
            else:
                xs.remove((x1, x2))

            prev_y = y

        # ===== 4. Tìm đường y chia đôi diện tích =====
        half = total / 2
        acc = 0

        for y, h, w in areas:
            if acc + h * w >= half:
                # Nội suy trong lát hiện tại
                return y + (half - acc) / w
            acc += h * w

        return 0.0


# 3️⃣ Ví dụ trực quan nhanh

# Giả sử:

# * Tại đoạn Y = [2, 5]
# * Union X = 10
# * Diện tích lát = 3 × 10 = 30

# Nếu còn thiếu 5 để đạt half:

# ```
# k = 2 + 5 / 10 = 2.5
# ```

# ---

# # 4️⃣ Độ phức tạp

# * Số sự kiện: `2n`
# * Mỗi lần tính `union_len`: `O(k log k)`
# * Tổng: **O(n² log n)** (bản Python này)

# 👉 Java/C++ bản chính thức dùng **Segment Tree + nén tọa độ** → **O(n log n)**

# ---

# 5️⃣ So sánh nhanh

# | Phiên bản          | Ý tưởng                     | Tốc độ   |
# | ------------------ | --------------------------- | -------- |
# | Python này         | Sweep line + union thủ công | Dễ hiểu  |
# | Java bạn gửi trước | Sweep + Segment Tree        | Chuẩn CF |

# ---

# Nếu bạn muốn:

# * 👉 Tối ưu Python lên `O(n log n)`
# * 👉 Vẽ hình minh họa từng bước
# * 👉 So sánh chi tiết Java vs Python

# cứ nói tiếp nhé 👍

# // 1. **Giải thích thuật toán của đoạn code (tư duy + từng bước)**
# // 2. **Chú thích trực tiếp vào code (comment dễ hiểu)**
# // 3. **Thêm hàm `main` dùng `Scanner` để test**

# // ---

# // # 1️⃣ Giải thích thuật toán (từ trên xuống)

# // ## 🎯 Mục tiêu bài toán

# // Tìm đường thẳng **y = k** sao cho:

# // * **Diện tích hợp của các hình vuông phía dưới = phía trên**
# // * Tức là chia **tổng diện tích union của các hình vuông** thành 2 nửa bằng nhau

# // 👉 Không phải tổng (a_i^2), mà là **diện tích hợp (union)** vì các hình vuông có thể chồng nhau.

# // ---

# // ## 🧠 Ý tưởng chính trong code

# // ### 🔹 Bước 1: Quét theo trục Y (Sweep Line)

# // * Mỗi hình vuông tạo ra **2 sự kiện**:

# //   * Bắt đầu tại `y1`
# //   * Kết thúc tại `y2`
# // * Khi quét từ dưới lên:

# //   * Ta biết tại mỗi đoạn Y, **chiều dài X đang được phủ**

# // 📌 Diện tích = (chiều dài phủ trên trục X) × (độ cao Y)

# // ---

# // ### 🔹 Bước 2: Nén tọa độ X (Coordinate Compression)

# // Vì:

# // * X có thể rất lớn
# // * Segment Tree chỉ cần quản lý **các đoạn X xuất hiện**

# // → Lấy tất cả `x1`, `x2`, sort + unique

# // ---

# // ### 🔹 Bước 3: Segment Tree quản lý độ phủ X

# // Segment Tree lưu:

# // * `cnt[node]`: số hình vuông đang phủ đoạn đó
# // * `cover[node]`: tổng độ dài X đang được phủ

# // 📌 Nếu `cnt > 0` → đoạn đó được phủ hoàn toàn

# // ---

# // ### 🔹 Bước 4: Tính diện tích theo từng “lát” Y

# // Khi quét:

# // * Giữa `prevY` và `currY`
# // * Diện tích thêm:

# // ```
# // baseLen * (currY - prevY)
# // ```

# // Ta lưu lại:

# // * `sY[i]`: y bắt đầu
# // * `eY[i]`: y kết thúc
# // * `base[i]`: độ phủ X tại đoạn đó

# // ---

# // ### 🔹 Bước 5: Tìm y sao cho diện tích = 1/2 tổng

# // * Tổng diện tích = `area`
# // * Mục tiêu = `area / 2`
# // * Duyệt từng lát:

# //   * Nếu chưa đủ → cộng tiếp
# //   * Nếu vượt → nội suy:

# // ```
# // y = sY + (phần còn thiếu / baseLen)
# // ```

# // ---

# // # 2️⃣ Code có chú thích chi tiết

# import java.util.*;

# public class b148 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int n = sc.nextInt();

#         int[][] squares = new int[n][3];
#         for (int i = 0; i < n; i++) {
#             squares[i][0] = sc.nextInt(); // x
#             squares[i][1] = sc.nextInt(); // y
#             squares[i][2] = sc.nextInt(); // cạnh
#         }

#         double ans = separateSquares(squares);
#         System.out.println(ans);

#     }

#     // Sự kiện quét theo trục Y
#     static final class Event {
#         final long y; // tung độ xảy ra sự kiện
#         final int l, r; // đoạn X [l, r)
#         final int delta; // +1: bắt đầu phủ, -1: kết thúc phủ

#         Event(long y, int l, int r, int delta) {
#             this.y = y;
#             this.l = l;
#             this.r = r;
#             this.delta = delta;
#         }
#     }

#     // Segment Tree quản lý độ phủ trên trục X
#     static final class SegTree {
#         final long[] xs; // tọa độ X sau khi nén
#         final long[] cover; // tổng độ dài X đang được phủ
#         final int[] cnt; // số lớp phủ

#         SegTree(long[] xs) {
#             this.xs = xs;
#             int n = Math.max(1, xs.length - 1);
#             cover = new long[n << 2];
#             cnt = new int[n << 2];
#         }

#         // Lấy tổng chiều dài X đang được phủ
#         long covered() {
#             return cover[1];
#         }

#         void update(int l, int r, int delta) {
#             if (l >= r)
#                 return;
#             update(1, 0, xs.length - 1, l, r, delta);
#         }

#         void update(int node, int L, int R, int ql, int qr, int delta) {
#             if (qr <= L || R <= ql)
#                 return;

#             if (ql <= L && R <= qr) {
#                 cnt[node] += delta;
#                 pushUp(node, L, R);
#                 return;
#             }

#             int mid = (L + R) >>> 1;
#             update(node << 1, L, mid, ql, qr, delta);
#             update(node << 1 | 1, mid, R, ql, qr, delta);
#             pushUp(node, L, R);
#         }

#         void pushUp(int node, int L, int R) {
#             if (cnt[node] > 0) {
#                 // nếu có ít nhất 1 hình phủ → phủ toàn bộ đoạn
#                 cover[node] = xs[R] - xs[L];
#             } else if (L + 1 == R) {
#                 cover[node] = 0;
#             } else {
#                 cover[node] = cover[node << 1] + cover[node << 1 | 1];
#             }
#         }
#     }

#     // Hàm chính giải bài
#     public static double separateSquares(int[][] squares) {
#         int n = squares.length;
#         if (n == 0)
#             return -1;

#         // === Nén tọa độ X ===
#         long[] xs = new long[2 * n];
#         int p = 0;
#         for (int[] s : squares) {
#             xs[p++] = s[0];
#             xs[p++] = (long) s[0] + s[2];
#         }
#         Arrays.sort(xs);

#         int m = 1;
#         for (int i = 1; i < xs.length; i++) {
#             if (xs[i] != xs[m - 1])
#                 xs[m++] = xs[i];
#         }
#         xs = Arrays.copyOf(xs, m);

#         // === Tạo các sự kiện Y ===
#         Event[] events = new Event[2 * n];
#         int e = 0;
#         for (int[] s : squares) {
#             long x1 = s[0], x2 = (long) s[0] + s[2];
#             long y1 = s[1], y2 = (long) s[1] + s[2];

#             int l = lowerBound(xs, x1);
#             int r = lowerBound(xs, x2);

#             if (l < r) {
#                 events[e++] = new Event(y1, l, r, +1);
#                 events[e++] = new Event(y2, l, r, -1);
#             }
#         }

#         events = Arrays.copyOf(events, e);
#         Arrays.sort(events, Comparator.comparingLong(a -> a.y));

#         SegTree st = new SegTree(xs);

#         // Lưu từng lát diện tích
#         long[] sY = new long[e];
#         long[] eY = new long[e];
#         long[] base = new long[e];

#         long area = 0;
#         long prevY = events[0].y;
#         long baseLen = 0;
#         int gi = 0;

#         int i = 0;
#         while (i < e) {
#             long currY = events[i].y;
#             long dy = currY - prevY;

#             if (dy > 0 && baseLen > 0) {
#                 area += baseLen * dy;
#                 sY[gi] = prevY;
#                 eY[gi] = currY;
#                 base[gi] = baseLen;
#                 gi++;
#             }

#             while (i < e && events[i].y == currY) {
#                 st.update(events[i].l, events[i].r, events[i].delta);
#                 i++;
#             }

#             baseLen = st.covered();
#             prevY = currY;
#         }

#         // === Tìm y sao cho diện tích = 1/2 ===
#         double target = area / 2.0;
#         long pref = 0;

#         for (int k = 0; k < gi; k++) {
#             long sliceArea = base[k] * (eY[k] - sY[k]);
#             if (pref + sliceArea < target) {
#                 pref += sliceArea;
#             } else {
#                 return sY[k] + (target - pref) / base[k];
#             }
#         }

#         return prevY;
#     }

#     // lower_bound chuẩn
#     public static int lowerBound(long[] a, long key) {
#         int l = 0, r = a.length;
#         while (l < r) {
#             int mid = (l + r) >>> 1;
#             if (a[mid] < key)
#                 l = mid + 1;
#             else
#                 r = mid;
#         }
#         return l;
#     }

# }

# // ```

# // ---

# // # 3️⃣ Tóm tắt ngắn gọn để nhớ thi

# // * **Sweep line theo Y**
# // * **Segment tree quản lý union theo X**
# // * **Tính diện tích theo từng lát**
# // * **Nội suy để tìm y chia đôi diện tích**

# // Nếu bạn muốn:

# // * 👉 Vẽ hình minh họa từng bước
# // * 👉 Phân tích độ phức tạp
# // * 👉 Viết lại version **dễ hơn để học**

# // nói mình biết nhé 👍

# // > Đây là bài toán hình học (thường gặp trên Codeforces) về **các hình vuông
# // song song trục tọa độ**.

# // ---

# // ## 1. Mô tả bài toán (ý chính)

# // Bạn được cho **n hình vuông** trên mặt phẳng tọa độ 2D.

# // Mỗi hình vuông được mô tả bởi:

# // * Tọa độ **góc dưới bên trái** ((x_i, y_i))
# // * **Cạnh** có độ dài (a_i)

# // → Tức là hình vuông có:

# // * Trục song song với trục (Ox, Oy)
# // * Bao phủ vùng:
# // [
# // x_i \le x \le x_i + a_i,\quad
# // y_i \le y \le y_i + a_i
# // ]

# // ---

# // ## 2. Nhiệm vụ của bạn

# // Hãy tìm **một đường thẳng song song với trục hoành (trục Ox)**, tức là:

# // [
# // y = k
# // ]

# // sao cho:

# // * **Tổng diện tích phần các hình vuông nằm phía trên đường thẳng**
# // * **bằng tổng diện tích phần các hình vuông nằm phía dưới đường thẳng**

# // 👉 Nói cách khác:
# // Đường thẳng (y = k) **chia tổng diện tích tất cả hình vuông thành hai phần
# // bằng nhau**.

# // ---

# // ## 3. Lưu ý quan trọng

# // * **Một hình vuông có thể bị cắt bởi đường thẳng**

# // * Phần trên + phần dưới vẫn được tính vào tổng diện tích
# // * Không cần hình vuông phải nằm hoàn toàn trên hoặc dưới
# // * Có thể có **nhiều đáp án**, bạn chỉ cần in **một giá trị (k)** thỏa mãn
# // * Chấp nhận **sai số nhỏ** (số thực, thường là `1e-6`)

# // ---

# // ## 4. Cách hiểu trực quan

# // Hãy tưởng tượng:

# // * Bạn có nhiều hình vuông đặt lung tung
# // * Bạn **kéo một đường ngang từ dưới lên trên**
# // * Khi kéo, **diện tích phía dưới tăng dần**
# // * Tại **một vị trí nào đó**, diện tích dưới = diện tích trên
# // → đó chính là nghiệm

# // ---

# // ## 5. Ý tưởng cốt lõi (không phải lời giải chi tiết)

# // 1. **Tổng diện tích tất cả hình vuông**:
# // [
# // S = \sum a_i^2
# // ]
# // 2. Ta cần tìm (k) sao cho:
# // [
# // \text{Area_below}(k) = \frac{S}{2}
# // ]
# // 3. Với mỗi hình vuông:

# // * Nếu (k \le y_i): đóng góp 0
# // * Nếu (k \ge y_i + a_i): đóng góp toàn bộ (a_i^2)
# // * Nếu (y_i < k < y_i + a_i): đóng góp:
# // [
# // a_i \times (k - y_i)
# // ]
# // 4. Hàm diện tích **tăng đơn điệu theo k**
# // → dùng **binary search** trên (k)

# // ---

# // ## 6. Vì sao bài này là “Separate Squares II”?

# // * **Separate Squares I**: thường là chia theo **trục dọc**
# // * **Separate Squares II**: chia theo **trục ngang**
# // * Bản II khó hơn vì phải xử lý **cắt hình vuông theo chiều cao**

# // ---

# // ## 7. Tóm tắt ngắn gọn

# // 📌 **Bài toán yêu cầu**:
# // Tìm đường thẳng (y = k) sao cho nó chia **tổng diện tích các hình vuông**
# // thành **hai nửa bằng nhau**

# // 📌 **Bản chất**:

# // * Tính diện tích theo chiều cao
# // * Hàm đơn điệu
# // * Dùng **binary search + hình học**

# // ---

# // Nếu bạn muốn:

# // * 👉 Giải thích **bằng ví dụ cụ thể**
# // * 👉 Phân tích **code mẫu**
# // * 👉 So sánh **Separate Squares I vs II**

# // chỉ cần nói tiếp nhé 👍
