# # # // // Bài **1545. Find Kth Bit in Nth Binary String (03/03/2026)

# # # // ##🔥Giải thích thuật toán–1545. Find Kth Bit in Nth Binary String

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        # Base case:
        # Khi n = 1 thì chuỗi S1 = "0"
        if n == 1:
            return '0'
        
        # Tính độ dài chuỗi Sn = 2^n - 1
        length = (1 << n) - 1
        
        # Tìm vị trí chính giữa
        # Vì cấu trúc: S(n-1) + "1" + reverse(invert(S(n-1)))
        mid = length // 2 + 1
        
        # Nếu k nằm đúng giữa
        # Theo định nghĩa luôn là '1'
        if k == mid:
            return '1'
        
        # Nếu k nằm ở nửa bên trái
        # Chính là bit thứ k của S(n-1)
        if k < mid:
            return self.findKthBit(n - 1, k)
        
        # Nếu k nằm ở nửa bên phải
        # Nó thuộc phần reverse(invert(S(n-1)))
        
        # Ta tìm vị trí đối xứng trong S(n-1)
        mirror = length - k + 1
        
        # Gọi đệ quy tìm bit trong S(n-1)
        bit = self.findKthBit(n - 1, mirror)
        
        # Vì phần này là invert nên phải đảo bit
        # Nếu '0' -> trả về '1'
        # Nếu '1' -> trả về '0'
        if bit == '0':
            return '1'
        else:
            return '0'




# # ## 🔥 Giải thích thuật toán (Python version)

# # Ta có định nghĩa:

# # [
# # S_n = S_{n-1} + "1" + reverse(invert(S_{n-1}))
# # ]

# # ---

# # ## 🎯 Cấu trúc quan trọng

# # Chuỗi `Sn` luôn có dạng:

# # ```
# # [ S(n-1) ] [ 1 ] [ reverse(invert(S(n-1))) ]
# # ```

# # ### 📌 Độ dài của Sn

# # [
# # length = 2^n - 1
# # ]

# # ### 📌 Vị trí chính giữa

# # [
# # mid = length // 2 + 1
# # ]

# # 👉 Bit ở giữa **luôn luôn là '1'**

# # ---

# # # 🧠 Tư duy tìm bit thứ k

# # Ta không tạo cả chuỗi (vì rất dài), mà dùng đệ quy.

# # ## ✅ Trường hợp 1: n == 1

# # ```
# # S1 = "0"
# # ```

# # → trả về `'0'`

# # ---

# # ## ✅ Trường hợp 2: k == mid

# # → luôn trả về `'1'`

# # ---

# # ## ✅ Trường hợp 3: k < mid

# # Bit nằm trong phần đầu `S(n-1)`
# # → gọi lại:

# # ```
# # findKthBit(n-1, k)
# # ```

# # ---

# # ## ✅ Trường hợp 4: k > mid

# # Bit nằm trong phần:

# # ```
# # reverse(invert(S(n-1)))
# # ```

# # Ta làm:

# # 1. Tìm vị trí đối xứng:

# #    ```
# #    mirror = length - k + 1
# #    ```
# # 2. Tìm bit ở `S(n-1)` tại vị trí mirror
# # 3. Đảo bit lại (0 ↔ 1)

# # ---

# # # 🚀 Độ phức tạp

# # * Time complexity: **O(n)**
# # * Space complexity: **O(n)** (do recursion stack)
# # * Không xây chuỗi thật → rất tối ưu

# # ---

# # # 💻 Code có chú thích chi tiết

# # ```python
# class Solution:
#     def findKthBit(self, n: int, k: int) -> str:
        
#         # Base case:
#         # Khi n = 1 thì chuỗi S1 = "0"
#         if n == 1:
#             return '0'
        
#         # Tính độ dài chuỗi Sn = 2^n - 1
#         length = (1 << n) - 1
        
#         # Tìm vị trí chính giữa
#         # Vì cấu trúc: S(n-1) + "1" + reverse(invert(S(n-1)))
#         mid = length // 2 + 1
        
#         # Nếu k nằm đúng giữa
#         # Theo định nghĩa luôn là '1'
#         if k == mid:
#             return '1'
        
#         # Nếu k nằm ở nửa bên trái
#         # Chính là bit thứ k của S(n-1)
#         if k < mid:
#             return self.findKthBit(n - 1, k)
        
#         # Nếu k nằm ở nửa bên phải
#         # Nó thuộc phần reverse(invert(S(n-1)))
        
#         # Ta tìm vị trí đối xứng trong S(n-1)
#         mirror = length - k + 1
        
#         # Gọi đệ quy tìm bit trong S(n-1)
#         bit = self.findKthBit(n - 1, mirror)
        
#         # Vì phần này là invert nên phải đảo bit
#         # Nếu '0' -> trả về '1'
#         # Nếu '1' -> trả về '0'
#         if bit == '0':
#             return '1'
#         else:


# # ---

# # # 🧩 Ví dụ trực quan

# # Ví dụ:

# # ```
# # n = 3
# # S3 = "0111001"
# # ```

# # Tìm k = 6:

# # * length = 7
# # * mid = 4
# # * 6 > 4 → thuộc phần phải
# # * mirror = 7 - 6 + 1 = 2
# # * Tìm bit thứ 2 của S2
# # * Sau đó đảo bit lại

# # ---

# # Nếu bạn muốn mình:

# # * Vẽ cây đệ quy từng bước
# # * Viết phiên bản không dùng đệ quy
# # * Hoặc phân tích kiểu phỏng vấn FAANG

# # Nói mình biết nhé 🚀



# # // Ta có định nghĩa:

# # // [S_n=S_{n-1}+"1"+reverse(invert(S_{n-1}))]

# # // ---

# # // ###🎯Ý tưởng cốt lõi

# # // Chuỗi`S_n`luôn có cấu trúc:

# # // ```[S(n-1)][1][reverse(invert(S(n-1)))]```

# # // ###📌Độ dài chuỗi

# # // [length=2^n-1]

# # // Vị trí giữa:

# # // [mid=\frac{length}{2}+1]

# # // ---

# # // ##🧠Tư duy tìm kth bit

# # // Khi cần tìm bit thứ`k`trong`S_n`,ta chia thành 3 trường hợp:

# # // ---

# # // ###✅Trường hợp 1:n==1

# # // ```S1="0"```

# # // →luôn trả về`'0'`

# # // ---

# # // ###✅Trường hợp 2:k==mid

# # // Vì giữa luôn là`"1"`→trả về`'1'`

# # // ---

# # // ###✅Trường hợp 3:k<mid

# # // Bit nằm trong phần`S(n-1)`đầu tiên→gọi đệ quy:

# # // ```findKthBit(n-1,k)```

# # // ---

# # // ###✅Trường hợp 4:k>mid

# # // Bit nằm trong phần:

# # // ```reverse(invert(S(n-1)))```

# # // Ta làm:

# # // 1. Tìm vị trí đối xứng:

# # // [mirror=length-k+1]

# # // 2. Tìm bit ở`S(n-1)`tại vị trí`mirror`3. Đảo bit lại(0↔1)

# # // ---

# # // ##🚀Tại sao thuật toán nhanh?

# # // *Không xây chuỗi thật(vì có thể dài tới 2¹⁰-1=1023)*Chỉ đi đệ quy tối đa n lần*Time complexity:**O(n)***Space complexity:**O(n)**(do recursion stack)

# # // ---

# # // #💻Code hoàn chỉnh có`main`dùng`Scanner`

# # // (đúng theo style bạn hay dùng)

# # // ```java

# # import java.util.*;

# # public class b205 {
# #     static Scanner sc = new Scanner(System.in);

# #     public static void main(String[] args) {
# #         // Nhập n và k
# #         int n = sc.nextInt();
# #         int k = sc.nextInt();

# #         // In kết quả
# #         System.out.println(findKthBit(n, k));

# #         sc.close();
# #     }

# #     // Hàm tìm bit thứ k trong chuỗi Sn
# #     public static char findKthBit(int n, int k) {

# #         // Base case: nếu n = 1 thì chuỗi chỉ có "0"
# #         if (n == 1)
# #             return '0';

# #         // Tính độ dài chuỗi Sn = 2^n - 1
# #         int length = (1 << n) - 1;

# #         // Vị trí chính giữa
# #         int mid = length / 2 + 1;

# #         // Nếu k nằm đúng vị trí giữa
# #         if (k == mid)
# #             return '1';

# #         // Nếu k nằm bên trái (trong Sn-1 đầu tiên)
# #         if (k < mid)
# #             return findKthBit(n - 1, k);

# #         // Nếu k nằm bên phải
# #         // Ta tìm vị trí đối xứng trong Sn-1
# #         int mirror = length - k + 1;

# #         // Gọi đệ quy và đảo bit
# #         char bit = findKthBit(n - 1, mirror);

# #         if (bit == '0')
# #             return '1';
# #         else
# #             return '0';
# #     }
# # }

# # // ---

# # // ##🧩

# # // Ví dụ
# # // chạy thử

# # // Input:

# # // ```3 1```

# # // Output:

# # // ```0```

# # // ---

# # // Input:

# # // ```4 11```

# # // Output:

# # // ```1```

# # // ---

# # // Nếu bạn
# # // muốn mình:

# # // *
# # // Vẽ cây
# # // đệ quy
# # // cho bạn
# # // nhìn trực quan*
# # // Hoặc chuyển
# # // sang cách giải**không dùng

# # // recursion (iterative)**
# # // * Hoặc phân tích sâu để đi phỏng vấn

# # // Bạn nói mình biết 👍

# # // ## 1️⃣ Đề bài nói gì?

# # // Ta định nghĩa một dãy chuỗi nhị phân như sau:

# # // * **S₁ = "0"**
# # // * Với n > 1:

# # // [
# # // S_n = S_{n-1} + "1" + reverse(invert(S_{n-1}))
# # // ]

# # // Trong đó:

# # // * `+` là nối chuỗi
# # // * `reverse(x)` là đảo ngược chuỗi
# # // * `invert(x)` là đổi:

# # // * `'0' → '1'`
# # // * `'1' → '0'`

# # // ---/

# # // ## 2️⃣ Ví dụ xây dựng các chuỗi

# # // ### 🔹 S₁

# # // ```
# # // "0"
# # // ```

# # // ---

# # // ### 🔹 S₂

# # // S₂ = S₁ + "1" + reverse(invert(S₁))

# # // * S₁ = `"0"`
# # // * invert(S₁) = `"1"`
# # // * reverse("1") = `"1"`

# # // Vậy:

# # // ```
# # // S₂ = "0" + "1" + "1"
# # // = "011"
# # // ```

# # // ---

# # // ### 🔹 S₃

# # // S₃ = S₂ + "1" + reverse(invert(S₂))

# # // * S₂ = `"011"`
# # // * invert(S₂):

# # // ```
# # // 0→1
# # // 1→0
# # // 1→0
# # // => "100"
# # // ```
# # // * reverse("100") = `"001"`

# # // Vậy:

# # // ```
# # // S₃ = "011" + "1" + "001"
# # // = "0111001"
# # // ```

# # // ---

# # // ### 🔹 S₄

# # // S₄ = S₃ + "1" + reverse(invert(S₃))

# # // S₃ = `"0111001"`

# # // Kết quả:

# # // ```
# # // S₄ = "011100110110001"
# # // ```

# # // ---

# # // ## 3️⃣ Câu hỏi của bài

# # // Cho:

# # // * n
# # // * k

# # // Hãy trả về **bit thứ k** (1-indexed) trong chuỗi Sₙ.

# # // ---

# # // ## 4️⃣ Ví dụ đề bài

# # // ### Ví dụ 1:

# # // ```
# # // Input: n = 3, k = 1
# # // ```

# # // S₃ = `"0111001"`

# # // Bit thứ 1 = `'0'`

# # // ---

# # // ### Ví dụ 2:

# # // ```
# # // Input: n = 4, k = 11
# # // ```

# # // S₄ = `"011100110110001"`

# # // Đếm đến vị trí 11 → `'1'`

# # // ---

# # // ## 5️⃣ Điều quan trọng cần hiểu 🔥

# # // Chiều dài của chuỗi Sₙ là:

# # // [
# # // 2^n - 1
# # // ]

# # // Ví dụ:

# # // | n | Độ dài |
# # // | - | ------ |
# # // | 1 | 1 |
# # // | 2 | 3 |
# # // | 3 | 7 |
# # // | 4 | 15 |
# # // | 5 | 31 |

# # // ---

# # // ## 6️⃣ Cấu trúc cực kỳ quan trọng

# # // Mỗi Sₙ có dạng:

# # // ```
# # // [ Sₙ₋₁ ] [ 1 ] [ reverse(invert(Sₙ₋₁)) ]
# # // ```

# # // Gọi:

# # // * length = 2ⁿ - 1
# # // * mid = (length + 1) / 2

# # // 👉 Vị trí giữa luôn là `'1'`.

# # // ---

# # // ## 7️⃣ Tư duy để tìm kth bit

# # // Ta không cần xây cả chuỗi vì nó rất dài.

# # // Ta xét:

# # // ### 🔹 Nếu k == mid

# # // → luôn là `'1'`

# # // ---

# # // ### 🔹 Nếu k < mid

# # // → chính là bit thứ k của Sₙ₋₁

# # // ---

# # // ### 🔹 Nếu k > mid

# # // → nó nằm trong phần:

# # // ```
# # // reverse(invert(Sₙ₋₁))
# # // ```

# # // Ta sẽ:

# # // 1. Tìm vị trí đối xứng:

# # // ```
# # // mirror = length - k + 1
# # // ```

# # // 2. Lấy bit ở Sₙ₋₁ tại vị trí `mirror`

# # // 3. Đảo bit lại (invert)

# # // ---

# # // ## 8️⃣ Bản chất của bài

# # // Đây là bài:

# # // * Không xây chuỗi
# # // * Không brute force
# # // * Dùng đệ quy theo cấu trúc

# # // ---

# # // ## 9️⃣ Tóm tắt ngắn gọn

# # // Để tìm bit thứ k trong Sₙ:

# # // * Nếu k là giữa → trả về `'1'`
# # // * Nếu k nhỏ hơn giữa → quay về Sₙ₋₁
# # // * Nếu k lớn hơn giữa → tìm vị trí đối xứng và đảo bit

# # // ---

# # // Nếu bạn muốn, mình có thể:

# # // * Giải thích bằng sơ đồ trực quan
# # // * Hoặc viết code Java tối ưu theo style bạn hay dùng (Scanner, while, không
# # // try-catch)
