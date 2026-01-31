# // Find Smallest Letter Greater Than Target(31/01/2026)
# // Bài **“Find Smallest Letter Greater Than Target”** (LeetCode 744) — mình giải thích **đề bài bằng tiếng Việt**, dễ hiểu nhé 👍
# // Ok, mình giải thích **thuật toán**, rồi **viết lại code Java đầy đủ có `main` + `Scanner` + chú thích chi tiết** cho bạn nhé 👌
# // (Bài này cách bạn làm là **đúng và rất dễ hiểu**)
# Ok, mình giải thích **thuật toán** đúng theo **code Python bạn đưa**, rồi **viết lại code có chú thích từng dòng** để bạn dễ nhớ và dễ trình bày khi thi / phỏng vấn nhé 👌

# ---

## 🧠 Giải thích thuật toán (theo tư duy code của bạn)

### Ý tưởng chính

# * Ta cần tìm **chữ cái nhỏ nhất nhưng lớn hơn `target`**
# * Mảng `letters` **đã được sắp xếp**
# * Mặc định:

#   * `res = letters[0]` → dùng cho trường hợp **wrap around**
#   * `flag` dùng để đánh dấu **đã tìm được chữ > target hay chưa**

# ---

### Diễn giải từng bước

# 1. Gán:

#    * `res = letters[0]`
#      → nếu **không có chữ nào > target** thì trả về chữ đầu tiên
#    * `flag = False`
#      → chưa tìm thấy ký tự hợp lệ

# 2. Duyệt từng ký tự `ch` trong `letters`

# 3. Nếu **chưa tìm thấy ký tự nào > target** (`flag == False`)

#    * Nếu `ch > target`

#      * Gán `res = ch`
#      * Đánh dấu `flag = True`

# 4. Nếu **đã tìm được rồi** (`flag == True`)

#    * Nếu `ch > target` **và** `ch < res`

#      * Cập nhật `res` nhỏ hơn

# 5. Sau khi duyệt xong:

#    * Nếu có chữ > target → `res` là nhỏ nhất
#    * Nếu không có → `res = letters[0]`

# ---

### ⏱ Độ phức tạp

# * **Time:** `O(n)`
# * **Space:** `O(1)`

# ---

# ## 🧾 Code Python có chú thích chi tiết

# ```python
from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        # Gán mặc định là chữ đầu tiên (dùng cho trường hợp wrap around)
        res = letters[0]
        
        # Cờ đánh dấu đã tìm thấy chữ cái > target hay chưa
        flag = False

        # Duyệt từng ký tự trong mảng
        for ch in letters:
            
            # Nếu CHƯA tìm thấy chữ > target
            if not flag:
                if ch > target:
                    res = ch          # gán kết quả tạm thời
                    flag = True       # đánh dấu đã tìm thấy
            else:
                # Nếu ĐÃ tìm thấy rồi
                # Kiểm tra xem có chữ nào nhỏ hơn res nhưng vẫn > target không
                if ch > target and ch < res:
                    res = ch          # cập nhật kết quả nhỏ hơn

        # Trả về kết quả cuối cùng
        return res
# ```

# ---

# ## 📌 Nhận xét (quan trọng)

# ✔ Code **đúng logic**
# ✔ Thể hiện tư duy tìm **min thỏa điều kiện**
# ⚠ Tuy nhiên vì `letters` **đã được sort**, nên:

# * Không cần `flag`
# * Không cần so sánh `ch < res`
# * Có thể **return ngay** khi gặp `ch > target`

# 👉 Code của bạn mang tính **tổng quát**, dễ hiểu, rất ổn khi giải thích bằng lời.

# ---

# Nếu bạn muốn, mình có thể:

# * Rút gọn code này cho gọn hơn
# * Viết **phiên bản Binary Search**
# * Giải thích cách trình bày **thuật toán bằng lời** khi thi vấn đáp

# Cứ nói nhé 😄

# // ---

# // ## 🧠 Giải thích thuật toán (theo code của bạn)

# // ### Ý tưởng

# // * Mảng `letters` **đã được sắp xếp**
# // * Ta duyệt **từ trái sang phải**
# // * Gặp chữ cái **đầu tiên lớn hơn `target`** → trả về ngay
# // * Nếu duyệt hết mà **không có chữ nào lớn hơn `target`**
# //   → áp dụng **wrap around** → trả về `letters[0]`

# // ---

# // ### Phân tích từng bước

# // 1. Duyệt mảng `letters`
# // 2. So sánh từng phần tử với `target`
# // 3. Điều kiện:

# //    ```java
# //    letters[i] > target
# //    ```
# // 4. Thỏa → return luôn (vì mảng đã sort, đây là chữ nhỏ nhất > target)
# // 5. Không tìm thấy → return chữ đầu tiên

# // ---

# // ### ⏱ Độ phức tạp

# // * **Time:** `O(n)` (duyệt mảng)
# // * **Space:** `O(1)` (không dùng thêm bộ nhớ)

# // ---

# // ## ✅ Code Java đầy đủ (có `main`, `Scanner`, chú thích)

# // ```java
# import java.util.*;
# public class b165{
#     static Scanner sc = new Scanner(System.in);
#     public static void main(String[] args) {
#         int n = sc.nextInt();

#         char[] letters = new char[n];

 
#         for (int i = 0; i < n; i++) {
#             letters[i] = sc.next().charAt(0);
#         }

    
#         char target = sc.next().charAt(0);


#         // Gọi hàm và in kết quả
#         char result = nextGreatestLetter(letters, target);
#         System.out.println(result);

#         sc.close();
#     }
#  // Hàm tìm chữ cái nhỏ nhất nhưng lớn hơn target
#     public static char nextGreatestLetter(char[] letters, char target) {

#         // Duyệt từng ký tự trong mảng
#         for (int i = 0; i < letters.length; i++) {

#             // Nếu tìm thấy ký tự lớn hơn target
#             if (letters[i] > target) {
#                 return letters[i]; // trả về ngay
#             }
#         }

#         // Nếu không có ký tự nào lớn hơn target
#         // thì quay vòng và trả về phần tử đầu tiên
#         return letters[0];
#     }
# }
    



# // ## 🧪 Ví dụ chạy chương trình

# // **Input**

# // ```
# // Nhap so luong chu cai: 3
# // Nhap cac chu cai:
# // c
# // f
# // j
# // Nhap target: j
# // ```

# // **Output**

# // ```
# // Ket qua: c
# // ```

# // ---

# // ## 📌 Ghi chú thêm (quan trọng khi đi thi / phỏng vấn)

# // * Cách này **dễ hiểu**, rất tốt cho bài cơ bản
# // * Khi nâng cao:

# //   * Có thể tối ưu thành **Binary Search → O(log n)**

# // Nếu bạn muốn 👉 mình sẽ:

# // * Viết **phiên bản Binary Search**
# // * So sánh **2 cách**
# // * Giải thích cách nghĩ để tự code trong phòng thi

# // Chỉ cần nói nhé 😄

# // ---

# // ### 📌 Đề bài nói gì?

# // Bạn được cho:

# // * Một mảng **letters** gồm các **chữ cái viết thường** (`'a'` → `'z'`)
# // * Mảng này **đã được sắp xếp tăng dần**
# // * Một ký tự **target**

# // 👉 Nhiệm vụ:
# // **Tìm chữ cái nhỏ nhất trong `letters` nhưng phải LỚN HƠN `target`.**

# // ---

# // ### ⚠️ Điều quan trọng (bẫy đề)

# // * Mảng có tính **vòng tròn (wrap around)**
# // * Nếu **không có chữ nào lớn hơn `target`**, thì **trả về chữ cái đầu tiên của mảng**

# // ---

# // ### 📘 Ví dụ minh họa

# // #### Ví dụ 1

# // ```text
# // letters = ['c','f','j']
# // target = 'a'
# // ```

# // * Các chữ > `'a'` là: `'c', 'f', 'j'`
# // * Nhỏ nhất là `'c'`

# // ✅ **Kết quả: `'c'`**

# // ---

# // #### Ví dụ 2

# // ```text
# // letters = ['c','f','j']
# // target = 'c'
# // ```

# // * Phải **lớn hơn**, nên `'c'` không tính
# // * Các chữ > `'c'` là: `'f', 'j'`
# // * Nhỏ nhất là `'f'`

# // ✅ **Kết quả: `'f'`**

# // ---

# // #### Ví dụ 3 (wrap around)

# // ```text
# // letters = ['c','f','j']
# // target = 'j'
# // ```

# // * Không có chữ nào > `'j'`
# // * Quay vòng → lấy chữ đầu tiên

# // ✅ **Kết quả: `'c'`**

# // ---

# // ### 🧠 Tư duy bài toán

# // * Vì mảng **đã sắp xếp**
# // * Ta cần **phần tử đầu tiên > target**
# //   👉 Đây chính là bài **Binary Search (tìm kiếm nhị phân)**

# // ---

# // ### 🧩 Tóm tắt ngắn gọn

# // ✔ Mảng chữ cái đã sort
# // ✔ Tìm chữ **nhỏ nhất nhưng > target**
# // ✔ Không có thì **trả về phần tử đầu tiên**

# // ---

# // Nếu bạn muốn:

# // * Giải thích **tư duy binary search**
# // * Code **Python / Java**
# // * So sánh **cách làm brute force vs binary search**

# // 👉 cứ nói mình biết nhé 😄
