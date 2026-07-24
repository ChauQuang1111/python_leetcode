# // Bài Number of Unique XOR Triplets II (24/07/2026)
# // Ý nghĩa đề bài
# // Cho một mảng nums.
# // Bạn chọn 3 chỉ số khác nhau i, j, k sao cho:

# // 0 <= i < j < k < n
# // Sau đó tính:
# // [
# // nums[i] \oplus nums[j] \oplus nums[k]
# // ]
# // Trong đó ⊕ là phép XOR.
# // Cuối cùng, hãy trả về số lượng giá trị XOR khác nhau thu được từ tất cả các bộ ba.
# // Ví dụ 1
# // nums = [1,2,3]
# // Chỉ có một bộ ba:

# // (1,2,3)

# // 1 ^ 2 = 3
# // 3 ^ 3 = 0
# // Các giá trị XOR thu được:

# // {0}
# // Đáp án:

# // 1
# // Ví dụ 2
# // nums = [1,2,3,4]
# // Các bộ ba là:

# // (1,2,3) = 0
# // (1,2,4) = 7
# // (1,3,4) = 6
# // (2,3,4) = 5
# // Tập giá trị:

# // {0,5,6,7}
# // Có 4 giá trị khác nhau.
# // Đáp án:

# // 4
# // "Unique" nghĩa là gì?
# // Ví dụ

# // nums = [1,1,2,2]
# // Các bộ ba có thể cho kết quả

# // 1^1^2 = 2
# // 1^2^2 = 1
# // ...
# // Nếu kết quả thu được là

# // 2
# // 2
# // 2
# // 1
# // 1
# // thì chỉ có

# // {1,2}
# // => đáp án là

# // 2
# // Không đếm số lần xuất hiện, chỉ đếm số giá trị XOR khác nhau.
# // Lưu ý
# // Đề II thường có ràng buộc lớn hơn bản I, nên không thể duyệt tất cả các bộ ba.
# // Nếu:

# // n = 10^5
# // thì số bộ ba là
# // [
# // \binom{10^5}{3}
# // \approx 1.67 \times 10^{14}
# // ]
# // không thể tính trực tiếp.
# // Do đó bài II yêu cầu khai thác tính chất của phép XOR hoặc dùng kỹ thuật tối ưu (ví dụ: quy hoạch động trên giá trị XOR, biến đổi Walsh–Hadamard, hoặc các tính chất đặc biệt của dữ liệu, tùy theo ràng buộc cụ thể của đề).
# // Tóm tắt đề bài
# // Input:

# // nums = [a1,a2,...,an]
# // Thực hiện:

# // Chọn mọi bộ ba i < j < k.
# // Tính nums[i] ^ nums[j] ^ nums[k].
# // Lấy tập các kết quả khác nhau.
# // Trả về kích thước của tập đó.
# // Nếu bạn đang nói đến bài LeetCode "Number of Unique XOR Triplets II", mình cũng có thể giải thích ý tưởng tối ưu và vì sao lời giải không cần duyệt (O(n^3)).
# // Dưới đây là phiên bản đầy đủ có main dùng Scanner, chú thích từng đoạn code, và giải thích thuật toán.

# import java.util.*;

# public class b276{
#     static Scanner sc = new Scanner(System.in);
#     public static void main(String[] args) {
#      int n = sc.nextInt();

#         int[] nums = new int[n];

#         // Nhập mảng
#         for (int i = 0; i < n; i++) {
#             nums[i] = sc.nextInt();
#         }

        

#         System.out.println(uniqueXorTriplets(nums));

#         sc.close(); 
#     }
# public  static int uniqueXorTriplets(int[] nums) {

#         // pairsPossible[x] = true nếu tồn tại một cặp có XOR bằng x
#         // 2048 = 2^11 vì nums[i] <= 1023 (10 bit),
#         // XOR lớn nhất chỉ đến 2047.
#         boolean[] pairsPossible = new boolean[2048];

#         // ans[x] = true nếu x là kết quả XOR của một bộ ba.
#         boolean[] ans = new boolean[2048];

#         int n = nums.length;

#         //-------------------------------------------------------
#         // Bước 1: Tính XOR của mọi cặp phần tử
#         //-------------------------------------------------------
#         for (int i = 0; i < n; i++) {
#             for (int j = i + 1; j < n; j++) {

#                 // Lưu rằng giá trị XOR này có thể tạo được
#                 pairsPossible[nums[i] ^ nums[j]] = true;
#             }
#         }

#         //-------------------------------------------------------
#         // Bước 2:
#         // Ban đầu thêm chính các phần tử của mảng vào ans.
#         //
#         // Vì:
#         // 0 ^ x = x
#         //
#         // Khi chưa có cặp (coi như XOR = 0),
#         // các giá trị này cũng được tính.
#         //-------------------------------------------------------
#         for (int e : nums) {
#             ans[e] = true;
#         }

#         //-------------------------------------------------------
#         // Bước 3:
#         // Ghép từng XOR của cặp với từng phần tử
#         //
#         // Nếu pair = a ^ b
#         // thì
#         // pair ^ c = a ^ b ^ c
#         //
#         // chính là XOR của bộ ba.
#         //-------------------------------------------------------
#         for (int i = 0; i < 2048; i++) {

#             // Chỉ xét các XOR của cặp đã tồn tại
#             if (pairsPossible[i]) {

#                 for (int e : nums) {

#                     // Tạo XOR của bộ ba
#                     ans[i ^ e] = true;
#                 }
#             }
#         }

#         //-------------------------------------------------------
#         // Bước 4: Đếm số giá trị XOR khác nhau
#         //-------------------------------------------------------
#         int ret = 0;

#         for (boolean e : ans) {
#             if (e)
#                 ret++;
#         }

#         return ret;
#     }
# }




# // Giải thích thuật toán
# // Giả sử

# // nums = [1,2,3,4]
# // Bước 1: Tính XOR của mọi cặp
# // Hai vòng lặp

# // for (int i=0;i<n;i++)
# //     for (int j=i+1;j<n;j++)
# // tạo tất cả các cặp.
# // Ví dụ
# // CặpXOR1,231,321,452,312,463,47
# // Ta đánh dấu

# // pairsPossible[1] = true
# // pairsPossible[2] = true
# // pairsPossible[3] = true
# // pairsPossible[5] = true
# // pairsPossible[6] = true
# // pairsPossible[7] = true
# // Thay vì lưu từng cặp, ta chỉ cần biết giá trị XOR nào xuất hiện.
# // Bước 2: Khởi tạo đáp án
# // for (int e : nums)
# //     ans[e] = true;
# // Sau bước này

# // ans = {1,2,3,4}
# // Bước 3: Sinh XOR của bộ ba
# // Giả sử đã biết

# // pair = a ^ b
# // thì

# // pair ^ c

# // = (a ^ b) ^ c

# // = a ^ b ^ c
# // chính là XOR của bộ ba.
# // Ví dụ

# // pair = 6

# // (2 ^ 4)
# // Ghép với

# // 3
# // ta được

# // 6 ^ 3

# // = (2 ^ 4) ^ 3

# // = 2 ^ 3 ^ 4
# // Đó chính là XOR của bộ ba (2,3,4).
# // Thuật toán lặp

# // for (int i=0;i<2048;i++)
# // Nếu

# // pairsPossible[i]
# // thì thử

# // i ^ nums[0]

# // i ^ nums[1]

# // ...

# // i ^ nums[n-1]
# // Mỗi kết quả đều là XOR của một bộ ba.
# // Ví dụ
# // nums = [1,2,3]
# // XOR các cặp
# // 1^2 = 3

# // 1^3 = 2

# // 2^3 = 1
# // pairsPossible

# // 1
# // 2
# // 3
# // Ghép với từng phần tử

# // 1^1 = 0

# // 1^2 = 3

# // 1^3 = 2

# // 2^1 = 3

# // 2^2 = 0

# // 2^3 = 1

# // 3^1 = 2

# // 3^2 = 1

# // 3^3 = 0
# // Các giá trị thu được

# // 0
# // 1
# // 2
# // 3
# // Sau khi loại trùng

# // {0,1,2,3}
# // Độ phức tạp
# // Bước 1
# // Duyệt mọi cặp:
# // [
# // O(n^2)
# // ]
# // Bước 2
# // Khởi tạo:
# // [
# // O(n)
# // ]
# // Bước 3
# // Có tối đa 2048 giá trị XOR khác nhau.
# // Với mỗi giá trị, thử ghép với n phần tử:
# // [
# // O(2048 \times n)
# // ]
# // Do 2048 là hằng số, nên bước này coi như:
# // [
# // O(n)
# // ]
# // Tổng độ phức tạp
# // Thời gian: (O(n^2 + 2048 \times n) \approx O(n^2))
# // Bộ nhớ: (O(2048)), tức là (O(1)) vì kích thước mảng pairsPossible và ans là hằng số.
# Thuật toán này dựa trên ý tưởng **xây dựng dần các giá trị XOR của cặp và bộ ba**, thay vì duyệt mọi bộ ba `O(n³)`.

# Dưới đây là code có chú thích chi tiết:

# ```python
from typing import List
class Solution:
    def uniqueXorTriplets(self, V: List[int]) -> int:

        # X2 lưu tất cả giá trị XOR của 2 phần tử đã xét.
        # Ban đầu chứa 0 để xử lý trường hợp "chưa có cặp".
        X2 = {0}

        # X3 lưu tất cả kết quả XOR của 3 phần tử.
        # Ban đầu thêm toàn bộ phần tử của mảng.
        #
        # Vì:
        #   0 ^ a = a
        # Sau này khi ghép với X2 = {0}, ta sẽ sinh ra các giá trị này.
        X3 = set(V)

        # Giá trị XOR lớn nhất có thể.
        #
        # Nếu max(V) cần b bit để biểu diễn
        # thì XOR cũng chỉ có tối đa 2^b giá trị khác nhau.
        #
        # Ví dụ:
        # max = 7 (111) -> k = 8 (0..7)
        # max = 13 (1101) -> k = 16 (0..15)
        k = 1 << max(V).bit_length()

        # Duyệt từng phần tử từ cuối mảng
        while V:

            # Lấy một phần tử ra.
            #
            # Sau khi pop, phần tử này sẽ không còn trong V,
            # nên sẽ không bị ghép với chính nó.
            v = V.pop()

            # Với mỗi XOR của một cặp đã biết (x2),
            # ghép thêm v để tạo XOR của 3 phần tử.
            #
            # triplet = v ^ (a ^ b)
            #
            # Ví dụ:
            # X2 = {1,4}
            # v = 6
            #
            # tạo:
            # 6^1 = 7
            # 6^4 = 2
            X3 |= {v ^ x2 for x2 in X2}

            # Sinh tất cả XOR của các cặp có chứa v.
            #
            # Ghép v với mọi phần tử còn lại trong V.
            #
            # Ví dụ:
            # V = [2,5,7]
            # v = 3
            #
            # sinh:
            # 3^2
            # 3^5
            # 3^7
            X2 |= {v ^ vv for vv in V}

            # Nếu đã thu được toàn bộ giá trị XOR có thể có
            # thì dừng sớm.
            #
            # Ví dụ:
            # số bit = 3
            # chỉ có 8 kết quả XOR (0..7)
            # nếu X3 có đủ 8 giá trị thì không thể sinh thêm.
            if len(X3) == k:
                break

        return len(X3)
# ```

# ---

# ## Ý tưởng của thuật toán

# Giả sử mảng là:

# ```text
# V = [1,2,3,4]
# ```

# ### Bước 1

# ```text
# X2 = {0}
# X3 = {1,2,3,4}
# ```

# Lấy

# ```text
# v = 4
# ```

# Sinh triplet

# ```text
# 4 ^ 0 = 4
# ```

# Không có gì mới.

# Sinh pair

# ```text
# 4^1 = 5
# 4^2 = 6
# 4^3 = 7
# ```

# ```text
# X2 = {0,5,6,7}
# ```

# ---

# ### Bước 2

# Lấy

# ```text
# v = 3
# ```

# Ghép với toàn bộ pair

# ```text
# 3^0 = 3
# 3^5 = 6
# 3^6 = 5
# 3^7 = 4
# ```

# Các giá trị này chính là XOR của **3 phần tử**, vì:

# ```text
# 3^(4^1)
# = 3^4^1

# 3^(4^2)
# = 3^4^2

# ...
# ```

# Sau đó tạo pair mới

# ```text
# 3^1 = 2
# 3^2 = 1
# ```

# ---

# ### Vì sao không bỏ sót bộ ba?

# Giả sử có bộ ba:

# ```text
# a, b, c
# ```

# Trong quá trình duyệt, sẽ luôn có **một phần tử được lấy ra sau cùng** (ví dụ `c`).

# Khi đó:

# * `a ^ b` đã được thêm vào `X2` ở các bước trước.
# * Đến lượt `c`, thuật toán tính:

# ```text
# c ^ (a ^ b)
# ```

# Theo tính chất kết hợp của XOR:

# ```text
# c ^ (a ^ b)
# = a ^ b ^ c
# ```

# Chính là giá trị XOR của bộ ba cần tìm.

# Do đó **mỗi bộ ba đều được sinh đúng một lần**.

# ---

# ## Độ phức tạp

# * Mỗi phần tử `v` tạo:

#   * `O(|X2|)` giá trị mới cho `X3`
#   * `O(n)` cặp mới.

# * Điều quan trọng là `|X2|` **không thể lớn hơn số lượng giá trị XOR có thể có**, tức:

# ```text
# 2^(số bit của max(V))
# ```

# Nếu `max(V) ≤ 2^10`, thì `|X2| ≤ 1024`.

# Vì vậy thuật toán gần như chạy trong:

# [
# O(n \times 2^B)
# ]

# với `B` là số bit của giá trị lớn nhất, nhanh hơn rất nhiều so với cách duyệt tất cả bộ ba có độ phức tạp (O(n^3)).
