# # // 3577. Count the Number of Computer Unlocking Permutations(10/12/2025)
# # // Dưới đây là **giải thích dễ hiểu** cho đề bài **LeetCode 3577 – Count the Number of Computer Unlocking Permutations**.
# # // Dưới đây là**giải thích thuật toán**,kèm**code hoàn chỉnh với hàm`main`dùng`Scanner`**và**chú thích chi tiết**.
# Dưới đây là **giải thích thuật toán**, kèm **code đã thêm chú thích chi tiết** để bạn hiểu rõ từng dòng.

# ---

# # 🧠 **Giải thích thuật toán**

# Bạn có một mảng `complexity` độ dài **n**.

# Điều kiện của đề bài 3577 nói rằng:

# * Mật khẩu mở khoá chỉ hợp lệ nếu **tất cả các độ phức tạp phía sau đều lớn hơn độ phức tạp của máy đầu tiên**.

# Nghĩa là:

# ```
# complexity[i] > complexity[0]  với mọi i > 0
# ```

# Nếu tồn tại dù chỉ một phần tử `≤ complexity[0]` → **không có cách sắp xếp hợp lệ** → trả về **0**.

# ---

# ## ✅ Vì sao kết quả là (n−1)! ?

# Nếu điều kiện trên được thoả mãn:

# * Máy đầu tiên (máy có complexity nhỏ nhất) **phải đứng đầu**
# * Các máy còn lại (n−1 máy) có thể hoán đổi **tự do**

# → Số hoán vị = **(n−1)!**

# Và phải lấy modulo (10^9+7).

# ---

# ## 🧠 Precompute factorials (tối ưu)

# Vì factorial tính nhiều lần và rất lớn, ta tạo sẵn:

# ```
# facs[i] = (i!) mod MOD
# ```

# Lúc tính chỉ cần lấy:

# ```
# facs[n-1]
# ```

# ---

# # ✅ Code có chú thích chi tiết

# ```python
MOD = 10**9 + 7

# Tiền xử lý bảng giai thừa (factorial)
facs = {}
facs[1] = 1
facs[2] = 2

# Tính i! mod MOD cho i từ 3 đến 100000
for i in range(2, (10**5) + 1):
    # facs[i] = i! = (i-1)! * i
    facs[i] = (facs[i-1] * i) % MOD

from typing import List
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:

        # Lấy giá trị đầu tiên của mảng
        lowest = complexity[0]

        # Kiểm tra xem có phần tử nào sau <= lowest không
        # Nếu có → không có hoán vị hợp lệ
        for c in complexity[1:]:
            if c <= lowest:
                return 0

        # Nếu hợp lệ → số hoán vị = (n - 1)!
        return facs[len(complexity) - 1]
# ```

# ---

# # 📌 Tóm tắt nhanh

# * Kiểm tra **tính tăng dstrict**: `complexity[i] > complexity[0]`
# * Nếu sai → trả về 0
# * Nếu đúng → trả về factorial(n − 1)
# * Dùng precomputed factorial để tốc độ O(1)

# ---

# Bạn muốn mình viết thêm **ví dụ minh hoạ** hoặc **so sánh với lời giải Java** không?

# // ---

# // #🧠**Giải thích thuật toán**

# // Bạn được cho một mảng`comp`có độ dài`n`.

# // Thuật toán làm việc như sau:

# // ###✅**Bước 1—Kiểm tra tính hợp lệ**

# // ```java int first=comp[0];for(int i=1;i<n;i++){if(comp[i]<=first)return 0;}```

# // *Lấy phần tử đầu tiên`first=comp[0]`*Nếu có bất kì phần tử nào phía sau**≤first**,trả về**0**

# // 👉Nghĩa là:**Toàn bộ các phần tử sau phải lớn hơn phần tử đầu tiên.**Nếu không,không có hoán vị hợp lệ.

# // ---

# // ###✅**Bước 2—Tính giai thừa(n-1)!**

# // ```java long fact=1;for(int i=2;i<n;i++){fact=(fact*i)%MOD;}return(int)fact;```

# // Vòng lặp chạy từ 2 đến(n-1):

# // *Nếu`n=1`→trả về 1*Nếu`n=5`→tính`2*3*4=24=(5-1)!`

# // 👉Thuật toán kết luận rằng số hoán vị hợp lệ=**(n-1)!mod 1e9+7**

# // ---

# // #📌**Ý nghĩa**

# // *Điều kiện bắt buộc để có hoán vị hợp lệ:**comp[i]phải tăng so với comp[0]***Và số hoán vị hợp lệ chỉ phụ thuộc vào số phần tử:**(n-1)!**

# // ---

# // #✅**Code hoàn chỉnh(có`main`,dùng`Scanner`,chú thích đầy đủ)**

# // ```java

# import java.util.*;

# public class b114 {
#     static Scanner sc = new Scanner(System.in);
#     static final int MOD = 1_000_000_007;

#     public static void main(String[] args) {
#         int n = sc.nextInt();

#         int[] comp = new int[n];
#         for (int i = 0; i < n; i++) {
#             comp[i] = sc.nextInt();
#         }

#         int result = countPermutations(comp);

#         System.out.println(result);
#     }

#     // Hàm chính tính số lượng hoán vị hợp lệ
#     public static int countPermutations(int[] comp) {
#         int n = comp.length;

#         // Lấy phần tử đầu tiên
#         int first = comp[0];

#         // Kiểm tra toàn bộ các phần tử sau phải lớn hơn first
#         for (int i = 1; i < n; i++) {
#             if (comp[i] <= first) {
#                 // Nếu có phần tử <= phần tử đầu tiên → không hợp lệ
#                 return 0;
#             }
#         }

#         // Tính (n - 1)! modulo 1e9+7
#         long fact = 1;
#         for (int i = 2; i < n; i++) {
#             fact = (fact * i) % MOD;
#         }

#         return (int) fact;
#     }

# }

# // Bạn muốn
# // mình làm
# // thêm gì không?**

# // *
# // Viết lại
# // code tối
# // ưu hơn?*
# // Giải thích
# // vì sao
# // công thức

# // lại là (n - 1)! ?
# // * Viết test mẫu cho bạn chạy thử?

# // Chỉ cần bảo mình!

# // ---

# // # 🧩 **Giải thích đề bài (dễ hiểu)**

# // Bạn được cho:

# // * Một số nguyên **m** (số hàng)
# // * Một số nguyên **n** (số cột)

# // => Tạo ra một bàn phím dạng **lưới m × n**.
# // Mỗi ô trong lưới là một nút để mở khóa.

# // Bạn cần đếm **tất cả những chuỗi nhấn nút hợp lệ** để mở khóa máy tính.

# // ---

# // # 🔐 **Quy tắc mở khóa (giống pattern lock Android)**

# // Một "unlocking permutation" (chuỗi mở khóa hợp lệ) phải thỏa:

# // 1. Bạn chọn một ô bất kỳ làm điểm bắt đầu.
# // 2. Mỗi bước bạn chọn một ô **chưa từng chọn trước đó**.
# // 3. Nếu để đi từ ô A → B mà phải đi **qua** một ô C,
# // thì C **phải đã được chọn trước đó**, nếu không **bước đó không hợp lệ**.

# // 📌 Giống hệt quy tắc khóa màn hình Android:
# // Muốn vẽ đường chéo qua 3 điểm thì phải chọn điểm giữa trước.

# // ---

# // # 🧠 **Ví dụ cụ thể**

# // ## Ví dụ: m = 1, n = 3

# // Lưới:

# // ```
# // 1 2 3
# // ```

# // Các chuỗi hợp lệ:

# // * 1 → 2
# // * 1 → 3 là **không hợp lệ** (vì phải đi qua 2 chưa chọn)
# // * 2 → 1
# // * 2 → 3
# // * 3 → 2
# // * 3 → 1
# // * …

# // ---

# // # 🔎 **Khái niệm quan trọng**

# // Ta có một ma trận các nút.
# // Giữa hai nút (A → B) có thể:

# // * **Đi trực tiếp** → hợp lệ.
# // * **Đi qua nút giữa** → phải kiểm tra nút giữa đã chọn chưa.

# // → Đây là bài toán **DFS + backtracking**, nhưng phải kiểm tra ràng buộc “đi
# // qua điểm giữa”.

# // ---

# // # 🎯 **Cần tính gì?**

# // Trả về **tổng số chuỗi mở khóa hợp lệ**,
# // với độ dài chuỗi ≥ 1 (ít nhất chọn 1 nút).

# // ---

# // # 🧮 **Độ khó?**

# // * m, n có thể lên tới 5–6 hoặc lớn hơn.
# // * Tổng số nút ≤ 25 → 25! quá lớn
# // → Nhưng nhờ các quy tắc “đi qua nút giữa”, nhiều đường bị chặn → thực tế nhỏ
# // hơn.

# // Bài yêu cầu dùng:

# // * **Backtracking**
# // * **Bitmask**
# // * **Memoization (DP)** để tối ưu

# // ---

# // # 📘 **Tóm tắt lại đề bài**

# // > Với một lưới m × n, đếm tổng số chuỗi chọn nút hợp lệ theo quy tắc:
# // >
# // > * Không chọn một nút hai lần
# // > * Nếu đường thẳng A → B đi qua nút C thì C phải được chọn trước
# // > → Trả về số chuỗi mở khóa hợp lệ.

# // ---

# // Nếu bạn muốn, mình có thể:

# // ✅ Vẽ hình minh họa cách kiểm tra "đi qua điểm giữa"
# // ✅ Viết **giải pháp chi tiết** (DFS + memo)
# // ✅ Viết **code tối ưu** (Python, Java, C++ tùy bạn chọn)

# // Bạn muốn tiếp theo phần nào?
