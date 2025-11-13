# // Maximum Number of Operations to Move Ones to the End(13/11/2025)
# // Rất hay👍Đây là bài**LeetCode 3228–Maximum Number of Operations to Move Ones to the End**được viết bằng**Java**,với cách giải khác—ngắn gọn nhưng thông minh.Mình sẽ**giải thích chi tiết thuật toán**,**thêm chú thích vào code**,và**viết luôn hàm`main`dùng`Scanner`**cho bạn.👇


### 💡 **Giải thích thuật toán**

# **Ý tưởng chính:**

# * Khi di chuyển `'1'` về cuối chuỗi, ta quan tâm đến **các đoạn `'1'` nằm trước các `'0'`**.
# * Mỗi đoạn `'1'` (liên tiếp) sẽ phải **“vượt qua”** tất cả các `'0'` sau nó,
#   và việc này được thể hiện bằng cách cộng dồn tổng số `'1'` trước đó.

# ---

# ### ✅ **Code có chú thích đầy đủ**

# ```python
class Solution:
    def maxOperations(self, s: str) -> int:
        # Tách chuỗi thành các đoạn liên tiếp của '1', ngăn cách bởi '0'
        # Ví dụ: s = "11010" → s.split('0') = ['11', '1', ''] → ones = [2, 1]
        ones = [len(i) for i in s.split('0') if i]

        # Nếu không có '1' nào trong chuỗi, không cần hoán đổi
        if not ones:
            return 0

        tot = 0  # Tổng số '1' đã gặp ở các đoạn trước
        ans = 0  # Tổng số phép hoán đổi

        # Duyệt qua tất cả các đoạn '1', trừ đoạn cuối (nếu có)
        for f in ones[:-1]:
            tot += f       # Cộng thêm số '1' của đoạn hiện tại
            ans += tot     # Tất cả các '1' trước đó sẽ vượt qua ít nhất một '0'

        # Nếu chuỗi kết thúc bằng '1', tức là không có '0' nào sau cùng
        # → không cần thêm phép hoán đổi
        if s[-1] == '1':
            return ans

        # Ngược lại, nếu chuỗi kết thúc bằng '0'
        # → cần cộng thêm các hoán đổi còn lại cho phần cuối
        return ans + tot + ones[-1]
# ```

# ---

# ### 🧩 **Ví dụ minh họa**

# #### Input:

# ```python
# s = "11010"
# ```

# #### Các bước:

# 1. `s.split('0') = ['11', '1', '']`
#    👉 `ones = [2, 1]`  (các nhóm '1' liên tiếp)

# 2. Duyệt qua `ones[:-1] = [2]`

#    * `tot = 2`
#    * `ans = 2`

# 3. `s[-1] = '0'` → chạy dòng cuối:

#    ```
#    return ans + tot + ones[-1]
#    = 2 + 2 + 1 = 5
#    ```

# ✅ **Kết quả: 5**

# ---

# ### 🧠 **Tóm tắt ý tưởng**

# | Biến        | Ý nghĩa                                                                                |
# | ----------- | -------------------------------------------------------------------------------------- |
# | `ones`      | Danh sách độ dài các đoạn `'1'` liên tiếp                                              |
# | `tot`       | Tổng số `'1'` đã gặp từ các đoạn trước                                                 |
# | `ans`       | Tổng số phép di chuyển (swap)                                                          |
# | Công thức   | Mỗi đoạn `'1'` tạo thêm `tot` phép di chuyển, vì các `'1'` trước nó cần vượt qua `'0'` |
# | Độ phức tạp | O(n)                                                                                   |

# ---

# Bạn có muốn mình viết thêm **phiên bản Java tương đương** của thuật toán Python này để so sánh hai cách tiếp cận không?

# // ---

# // ###💡**Giải thích ý tưởng thuật toán**

# // Giả sử ta đang duyệt chuỗi từ**trái sang phải**:

# // *Biến`o`đếm**tổng số ký tự`'1'`đã gặp trước đó**.*Khi ta gặp một cặp**“10”**,nghĩa là:

# // *`s.charAt(i-1)=='1'`và`s.charAt(i)=='0'`.*Mỗi ký tự`'1'`trước đó đều có thể**trượt qua ký tự`'0'`này**trong quá trình hoán đổi.*Do đó,ta**cộng thêm`o`vào kết quả`res`**,vì tất cả các`'1'`trước đó đều sẽ di chuyển 1 bước về bên phải.

# // Cứ tiếp tục như vậy đến hết chuỗi.

# // ---

# // ###✏️**Code đầy đủ(có chú thích+hàm main dùng Scanner)**

# // ```java

# import java.util.*;

# public class b97 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         String s = sc.next();

#         int result = maxOperations(s);

#         System.out.println(result);

#         sc.close();
#     }

#     public static int maxOperations(String s) {
#         int res = 0; // Tổng số phép hoán đổi
#         int o = 0; // Số lượng ký tự '1' đã gặp
#         int n = s.length();

#         // Duyệt từng ký tự trong chuỗi
#         for (int i = 0; i < n; ++i) {
#             o += s.charAt(i) - '0'; // Nếu gặp '1' thì cộng thêm 1

#             // Nếu gặp "10" (tức là ký tự hiện tại < ký tự trước đó)
#             if (i > 0 && s.charAt(i) < s.charAt(i - 1)) {
#                 res += o; // Mỗi '1' trước đó sẽ đi qua ký tự '0' này
#             }
#         }

#         return res;
#     }

# }

# // ###🧩**

# // Ví dụ
# // minh họa
# // hoạt động code**

# // ####Input:

# // ```11010```

# // ####
# // Bước chạy:

# // |i|s[i]|s[i-1]|

# // o (số '1' gặp) | Điều kiện "10"? |

# // res (tổng phép đổi) |
# // | - | ---- | ------ | -------------- | --------------- | -------------------
# // |
# // | 0 | '1' | — | 1 | — | 0 |
# // | 1 | '1' | '1' | 2 | ❌ | 0 |
# // | 2 | '0' | '1' | 2 | ✅ | 0 + 2 = 2 |
# // | 3 | '1' | '0' | 3 | ❌ | 2 |
# // | 4 | '0' | '1' | 3 | ✅ | 2 + 3 = 5 |

# // ✅ Kết quả: `res = 5`

# // ---

# // // ### 🧠 **Tóm tắt logic**

# // | Biến | Ý nghĩa |
# // | ----------- | --------------------------------------- |
# // | `o` | Số lượng `'1'` đã gặp trước đó |
# // | `res` | Tổng số lần hoán đổi tối đa |
# // | Điều kiện | Nếu gặp `'10'`, cộng thêm `o` vào `res` |
# // | Độ phức tạp | O(n) |

# // ---

# // Bạn có muốn mình viết lại một **phiên bản dễ hiểu hơn (for-each hoặc
# // stream)** để học logic Java sạch hơn không?

# // ---

# // ### 🧩 **Đề bài (diễn giải dễ hiểu)**

# // Bạn được cho **một chuỗi nhị phân** `s` — chỉ gồm `'0'` và `'1'`.
# // Mỗi lần, bạn **có thể chọn một cặp ký tự liên tiếp `'10'`** trong chuỗi
# // và **đổi chỗ chúng lại**, để nó trở thành `'01'`.

# // 👉 Mỗi lần đổi như vậy được gọi là **một phép di chuyển (operation)**.
# // Bạn có thể lặp lại thao tác này **bao nhiêu lần tùy ý**,
# // cho đến khi **không thể đổi thêm được nữa** (tức là mọi `'1'` đã nằm bên phải
# // tất cả `'0'`).

# // **Yêu cầu:**
# // Hãy tính **số phép di chuyển tối đa** mà bạn có thể thực hiện.

# // ---

# // ### 💡 Ví dụ minh họa

# // #### Ví dụ 1:

# // ```
# // Input: s = "1101"
# // ```

# // Ta có thể thực hiện như sau:

# // | Bước | Chuỗi | Ghi chú |
# // | ---- | ------ | ---------------------- |
# // | 0 | "1101" | ban đầu |
# // | 1 | "1011" | đổi cặp "10" đầu tiên |
# // | 2 | "0111" | đổi cặp "10" tiếp theo |

# // → Không còn "10" nào nữa.
# // ✅ Kết quả: **2 phép di chuyển**

# // ---

# // #### Ví dụ 2:

# // ```
# // Input: s = "100"
# // ```

# // | Bước | Chuỗi | Ghi chú |
# // | ---- | ----- | ------------------ |
# // | 0 | "100" | ban đầu |
# // | 1 | "010" | đổi "10" |
# // | 2 | "001" | đổi "10" tiếp theo |

# // ✅ Kết quả: **2 phép di chuyển**

# // ---

# // ### ⚙️ **Mục tiêu**

# // Hãy tìm công thức hoặc cách tính tổng số **lần hoán đổi “10”** có thể thực
# // hiện
# // cho đến khi **mọi ‘1’ đều nằm về cuối chuỗi.**

# // ---

# // ### 💭 **Tư duy giải**

# // Mỗi ký tự `'1'` **cần phải di chuyển** sang **bên phải tất cả các ký tự
# // `'0'`** xuất hiện sau nó.

# // Vì thế:

# // * Nếu tại vị trí `i` có `'1'`,
# // thì số lần hoán đổi mà `'1'` này sẽ thực hiện
# // chính là **số lượng `'0'` xuất hiện *sau* vị trí đó.**

# // Tổng số phép di chuyển = tổng của (số lượng `0` phía sau mỗi `1`).

# // ---

# // ### ✏️ Ví dụ minh họa chi tiết

# // `s = "11010"`

# // * Vị trí 0: `'1'` → có 2 số `0` sau nó → +2
# // * Vị trí 1: `'1'` → có 2 số `0` sau nó → +2
# // * Vị trí 2: `'0'` → bỏ qua
# // * Vị trí 3: `'1'` → có 1 số `0` sau nó → +1
# // * Vị trí 4: `'0'` → bỏ qua

# // Tổng cộng: `2 + 2 + 1 = 5`
# // ✅ Kết quả: **5 phép di chuyển**

# // ---

# // ### 🔢 Công thức tổng quát

# // Nếu `zero` là số lượng `'0'` đã thấy **bên phải**, ta có thể duyệt chuỗi từ
# // **phải sang trái**:

# // ```
# // ops = 0
# // zero_count = 0
# // for i in reversed(s):
# // if s[i] == '0':
# // zero_count += 1
# // else:
# // ops += zero_count
# // return ops
# // ```

# // ---

# // ### ✅ Tóm tắt ý chính

# // | Mục | Giải thích |
# // | --------------- | ---------------------------------------- |
# // | **Input** | Chuỗi nhị phân `s` |
# // | **Operation** | Hoán đổi `'10'` → `'01'` |
# // | **Goal** | Tính tổng số phép hoán đổi tối đa |
# // | **Tư duy** | Mỗi `'1'` cần đi qua tất cả `'0'` sau nó |
# // | **Độ phức tạp** | O(n) |

# // ---

# // Bạn có muốn mình viết luôn code Java hoặc Python có **chú thích chi tiết từng
# // dòng** cho bài này không?
