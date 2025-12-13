
# # // Coupon Code Validator(13/12/2025)
# # // Mình giải thích **đề bài “Coupon Code Validator”** theo cách **dễ hiểu – từng ý một**, vì đề này thường gây rối do nhiều điều kiện.
# Mình sẽ **giải thích thuật toán từng bước** và **thêm chú thích trực tiếp vào code Python**, đúng như bạn yêu cầu, theo cách **dễ hiểu – học được** 👍

# ---

# ## 🧠 Ý tưởng thuật toán (giải thích trước)

# ### Bài toán làm gì?

# * Có 3 mảng song song:

#   * `code[i]` → mã coupon
#   * `businessLine[i]` → ngành hàng
#   * `isActive[i]` → còn hiệu lực hay không
# * Chỉ lấy **coupon hợp lệ**, thỏa:

#   1. `isActive[i] == True`
#   2. `code[i]` **không rỗng**
#   3. `code[i]` chỉ chứa **chữ, số, hoặc `_`**
#   4. `businessLine[i]` thuộc 1 trong 4 ngành hợp lệ

# ### Sau đó:

# * Sắp xếp coupon theo thứ tự:

#   ```
#   electronics → grocery → pharmacy → restaurant
#   ```
# * Nếu cùng ngành → sắp xếp theo **từ điển (A → Z)**

# ---

# ## 🧩 Cách làm (tóm tắt)

# 1. Gán mỗi ngành hàng 1 **số thứ tự**
# 2. Viết hàm kiểm tra **code hợp lệ**
# 3. Duyệt từng coupon:

#    * Nếu hợp lệ → lưu `(thứ tự ngành, code)`
# 4. Sort theo `(ngành, code)`
# 5. Trả về danh sách code

# ---

# ## ✅ Code có chú thích chi tiết

# ```python
from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:

        # Gán thứ tự cho từng ngành hàng
        # Dùng số để sắp xếp đúng thứ tự yêu cầu
        valid_categories = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }

        # Hàm kiểm tra một coupon code có hợp lệ không
        def is_valid_code(s: str) -> bool:
            # Nếu code rỗng → không hợp lệ
            if not s:
                return False

            # Kiểm tra từng ký tự
            for ch in s:
                # Chỉ cho phép chữ, số hoặc dấu _
                if not (ch.isalnum() or ch == '_'):
                    return False
            return True

        # Danh sách lưu coupon hợp lệ
        # Mỗi phần tử là (thứ tự ngành, mã coupon)
        valid = []

        # Duyệt song song 3 mảng
        for c, b, a in zip(code, businessLine, isActive):

            # Chỉ lấy coupon:
            # - còn hiệu lực
            # - ngành hợp lệ
            # - code hợp lệ
            if a and b in valid_categories and is_valid_code(c):
                valid.append((valid_categories[b], c))

        # Sắp xếp:
        # - trước theo ngành (0 → 3)
        # - sau theo tên coupon (A → Z)
        valid.sort(key=lambda x: (x[0], x[1]))

        # Chỉ lấy lại mã coupon, bỏ thứ tự ngành
        return [c for _, c in valid]


# ## 🔍 Ví dụ minh họa

# ### Input:

# ```python
# code = ["SAVE_10", "BUY-NOW", "MED_5", "FOOD_20"]
# businessLine = ["electronics", "grocery", "pharmacy", "restaurant"]
# isActive = [True, True, True, False]
# ```

# ### Phân tích:

# * `"SAVE_10"` ✅ hợp lệ
# * `"BUY-NOW"` ❌ có dấu `-`
# * `"MED_5"` ✅ hợp lệ
# * `"FOOD_20"` ❌ không active

# ### Output:

# ```python
# ["SAVE_10", "MED_5"]
# ```

# ---

# ## ✅ Tóm tắt cực ngắn

# * ✔ Dùng **dictionary** để sắp xếp theo ngành
# * ✔ Dùng **tuple (ngành, code)** để sort gọn
# * ✔ Code sạch, rõ, đúng chuẩn phỏng vấn

# Nếu bạn muốn:

# * Viết lại **dễ hơn cho người mới**
# * So sánh với **Java version**
# * Tách từng bước ra cho dễ học

# 👉 cứ nói, mình giải thích tiếp cho bạn 👍

# import java.util.*;

# public class b117 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int n = sc.nextInt();
#         sc.nextLine(); // bỏ dòng trống

#         String[] code = new String[n];
#         String[] businessLine = new String[n];
#         boolean[] isActive = new boolean[n];

#         // Nhập dữ liệu cho từng coupon
#         for (int i = 0; i < n; i++) {
#             code[i] = sc.nextLine(); // mã coupon
#             businessLine[i] = sc.nextLine(); // ngành hàng
#             isActive[i] = sc.nextBoolean(); // trạng thái
#             sc.nextLine(); // bỏ dòng trống
#         }

#         List<String> result = validateCoupons(code, businessLine, isActive);

#         // In kết quả
#         for (String s : result) {
#             System.out.println(s);
#         }

#     }

#     public static List<String> validateCoupons(String[] code, String[] businessLine, boolean[] isActive) {

#         List<String> electronics = new ArrayList<>();
#         List<String> grocery = new ArrayList<>();
#         List<String> pharmacy = new ArrayList<>();
#         List<String> restaurant = new ArrayList<>();

#         for (int i = 0; i < code.length; i++) {

#             // Bỏ qua coupon không active hoặc rỗng
#             if (!isActive[i] || code[i].isEmpty())
#                 continue;

#             // Kiểm tra code hợp lệ
#             boolean validCode = true;
#             for (char c : code[i].toCharArray()) {
#                 if (!Character.isLetterOrDigit(c) && c != '_') {
#                     validCode = false;
#                     break;
#                 }
#             }

#             // Phân loại theo business line
#             if (validCode) {
#                 if (businessLine[i].equals("electronics")) {
#                     electronics.add(code[i]);
#                 } else if (businessLine[i].equals("grocery")) {
#                     grocery.add(code[i]);
#                 } else if (businessLine[i].equals("pharmacy")) {
#                     pharmacy.add(code[i]);
#                 } else if (businessLine[i].equals("restaurant")) {
#                     restaurant.add(code[i]);
#                 }
#             }
#         }

#         // Sắp xếp từng nhóm
#         Collections.sort(electronics);
#         Collections.sort(grocery);
#         Collections.sort(pharmacy);
#         Collections.sort(restaurant);

#         // Gộp kết quả
#         List<String> result = new ArrayList<>();
#         result.addAll(electronics);
#         result.addAll(grocery);
#         result.addAll(pharmacy);
#         result.addAll(restaurant);

#         return result;
#     }

# }

# // ---

# // ## 🧾 Coupon Code Validator là bài gì?

# // 👉 Bài toán yêu cầu bạn **kiểm tra một mã coupon có hợp lệ hay không**
# // Dựa trên **nhiều quy tắc cho trước**.

# // Kết quả thường là:

# // * `true / false`
# // * hoặc `"VALID" / "INVALID"`
# // * hoặc trả về **danh sách các coupon hợp lệ**

# // (tùy phiên bản đề)

# // ---

# // ## 🧠 Ý tưởng chung của bài

# // Một **coupon code hợp lệ** khi nó **thỏa mãn tất cả các điều kiện** mà đề bài
# // đưa ra.

# // Các điều kiện phổ biến gồm:

# // ---

# // ## ✅ 1. Độ dài của coupon

# // Ví dụ:

# // * Độ dài **từ 8 đến 12 ký tự**
# // * Không được quá ngắn hoặc quá dài

# // 📌 Ví dụ:

# // ```
# // ABC12345 ✅
# // AB12 ❌ (quá ngắn)
# // ```

# // ---

# // ## ✅ 2. Chỉ chứa ký tự hợp lệ

# // Thông thường:

# // * Chỉ gồm **chữ cái in hoa (A–Z)**
# // * Và **chữ số (0–9)**
# // * ❌ Không có khoảng trắng, ký tự đặc biệt

# // 📌 Ví dụ:

# // ```
# // SAVE2024 ✅
# // SAVE-2024 ❌ (có dấu -)
# // ```

# // ---

# // ## ✅ 3. Phải có ít nhất:

# // * 1 chữ cái
# // * 1 chữ số

# // 📌 Ví dụ:

# // ```
# // DISCOUNT9 ✅
# // DISCOUNT ❌ (không có số)
# // 12345678 ❌ (không có chữ)
# // ```

# // ---

# // ## ✅ 4. Không có ký tự lặp liên tiếp (tùy đề)

# // Ví dụ:

# // ```
# // ABCD1123 ❌ (11 lặp)
# // ABCD1234 ✅
# // ```

# // ---

# // ## ✅ 5. Không bắt đầu hoặc kết thúc bằng số (tùy đề)

# // Ví dụ:

# // ```
# // SALE2023 ❌ (kết thúc bằng số)
# // SALECODE ✅
# // ```

# // ---

# // ## 🎯 Mục tiêu cuối cùng

# // 👉 Với mỗi coupon:

# // * Kiểm tra **từng điều kiện**
# // * Nếu **vi phạm 1 điều kiện** → **KHÔNG hợp lệ**
# // * Nếu **qua hết** → **HỢP LỆ**

# // ---

# // ## 🧩 Cách tiếp cận khi làm bài

# // 1. Duyệt từng coupon
# // 2. Kiểm tra lần lượt:

# // * độ dài
# // * ký tự hợp lệ
# // * có chữ + số
# // * các quy tắc đặc biệt khác
# // 3. Trả kết quả

# // ---

# // ## 🧠 Ví dụ đơn giản

# // Giả sử quy tắc:

# // * Dài 8–12
# // * Chỉ chữ hoa + số
# // * Có ít nhất 1 chữ và 1 số

# // Input:

# // ```
# // ["SAVE2024", "abc12345", "DISCOUNT"]
# // ```

# // Output:

# // ```
# // ["SAVE2024"]
# // ```

# // ---

# // ## 🔑 Tóm tắt cực ngắn

# // > **Coupon Code Validator** =
# // > **Kiểm tra mã coupon có thỏa điều kiện không**

# // Không phải thuật toán khó, mà là:

# // * **Nhiều điều kiện**
# // * **Cần đọc đề thật kỹ**

# // ---

# // Nếu bạn muốn:

# // * 📌 Giải thích **một đề cụ thể** (LeetCode / HackerRank / CodeSignal…)
# // * 📌 Viết **code Java / Python**
# // * 📌 Giải thích từng dòng code

# // 👉 Bạn gửi **đề đầy đủ hoặc code**, mình giải thích chi tiết cho bạn 👍
# // Mình sẽ làm **3 việc** cho bạn, theo đúng yêu cầu:

# // 1. ✅ **Giải thích thuật toán (ý tưởng bài toán)**
# // 2. ✅ **Chú thích chi tiết vào code**
# // 3. ✅ **Thêm hàm `main` dùng `Scanner` để chạy thử**

# // ---

# // # 1️⃣ Giải thích đề & thuật toán (dễ hiểu)

# // ### 📌 Bài toán: *Coupon Code Validator*

# // Bạn được cho:

# // * `code[i]` → mã coupon
# // * `businessLine[i]` → ngành hàng của coupon đó
# // (`electronics`, `grocery`, `pharmacy`, `restaurant`)
# // * `isActive[i]` → coupon đó còn hiệu lực hay không

# // ### 👉 Nhiệm vụ:

# // * **Chỉ lấy những coupon hợp lệ**, thỏa:

# // 1. `isActive[i] == true`
# // 2. `code[i]` **không rỗng**
# // 3. `code[i]` chỉ chứa:

# // * chữ cái (`a-z`, `A-Z`)
# // * chữ số (`0-9`)
# // * dấu gạch dưới `_`

# // * Sau đó:

# // * Chia coupon theo **ngành hàng**
# // * **Sắp xếp từ điển (A → Z)** trong từng ngành
# // * Ghép kết quả theo thứ tự:

# // ```
# // electronics → grocery → pharmacy → restaurant
# // ```

# // ---

# // # 2️⃣ Code có chú thích chi tiết

# // ```java
# // import java.util.*;

# // class Solution {

# // public List<String> validateCoupons(String[] code, String[] businessLine,
# // boolean[] isActive) {

# // // Danh sách coupon cho từng ngành
# // List<String> electronics = new ArrayList<>();
# // List<String> grocery = new ArrayList<>();
# // List<String> pharmacy = new ArrayList<>();
# // List<String> restaurant = new ArrayList<>();

# // // Duyệt từng coupon
# // for (int i = 0; i < code.length; i++) {

# // // Nếu coupon không active hoặc code rỗng thì bỏ qua
# // if (!isActive[i] || code[i].isEmpty()) continue;

# // // Kiểm tra code có hợp lệ không
# // boolean validCode = true;

# // // Duyệt từng ký tự trong code
# // for (char c : code[i].toCharArray()) {

# // // Chỉ cho phép chữ, số hoặc dấu _
# // if (!Character.isLetterOrDigit(c) && c != '_') {
# // validCode = false;
# // break;
# // }
# // }

# // // Nếu code hợp lệ → phân loại theo businessLine
# // if (validCode) {
# // if (businessLine[i].equals("electronics")) {
# // electronics.add(code[i]);
# // }
# // else if (businessLine[i].equals("grocery")) {
# // grocery.add(code[i]);
# // }
# // else if (businessLine[i].equals("pharmacy")) {
# // pharmacy.add(code[i]);
# // }
# // else if (businessLine[i].equals("restaurant")) {
# // restaurant.add(code[i]);
# // }
# // }
# // }

# // // Sắp xếp từng nhóm coupon theo thứ tự từ điển
# // Collections.sort(electronics);
# // Collections.sort(grocery);
# // Collections.sort(pharmacy);
# // Collections.sort(restaurant);

# // // Gộp kết quả theo thứ tự yêu cầu
# // List<String> result = new ArrayList<>();
# // result.addAll(electronics);
# // result.addAll(grocery);
# // result.addAll(pharmacy);
# // result.addAll(restaurant);

# // return result;
# // }
# // }
# // ```

# // ---

# // # 3️⃣ Hàm `main` dùng `Scanner`

# // ```java
# // import java.util.*;

# // public class Main {
# // public static void main(String[] args) {
# // Scanner sc = new Scanner(System.in);

# // // Nhập số lượng coupon
# // int n = sc.nextInt();
# // sc.nextLine(); // bỏ dòng trống

# // String[] code = new String[n];
# // String[] businessLine = new String[n];
# // boolean[] isActive = new boolean[n];

# // // Nhập dữ liệu
# // for (int i = 0; i < n; i++) {
# // code[i] = sc.nextLine(); // mã coupon
# // businessLine[i] = sc.nextLine(); // ngành hàng
# // isActive[i] = sc.nextBoolean(); // trạng thái
# // sc.nextLine(); // bỏ dòng trống
# // }

# // Solution sol = new Solution();
# // List<String> result = sol.validateCoupons(code, businessLine, isActive);

# // // In kết quả
# // for (String s : result) {
# // System.out.println(s);
# // }
# // }
# // }
# // ```

# // ---

# // # 🔍 Ví dụ minh họa

# // ### Input:

# // ```
# // 4
# // SAVE_10
# // electronics
# // true
# // BUY_NOW
# // grocery
# // true
# // INVALID!
# // pharmacy
# // true
# // FOOD_5
# // restaurant
# // false
# // ```

# // ### Output:

# // ```
# // SAVE_10
# // BUY_NOW
# // ```

# // ---

# // # ✅ Tóm tắt ngắn gọn

# // * ✔ Lọc coupon hợp lệ
# // * ✔ Phân loại theo ngành
# // * ✔ Sắp xếp từng ngành
# // * ✔ Ghép kết quả đúng thứ tự

# // Nếu bạn muốn:

# // * viết lại **ngắn hơn**
# // * chuyển sang **Python**
# // * hoặc giải thích **từng hàm Java cơ bản** (`Character.isLetterOrDigit`,
# // `Collections.sort`…)

# // 👉 cứ nói, mình làm tiếp cho bạn 👍
