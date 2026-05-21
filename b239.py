# // // Find the Length of the Longest Common Prefix(21/05/2026)
# // // Bài  yêu cầu:

# // // Cho 2 mảng số nguyên:

# // // * `arr1`
# // // * `arr2`

# // // Ta cần tìm:

# // // > Độ dài lớn nhất của **prefix chung** giữa **một số trong arr1** và **một số trong arr2**.

# // // ---

# // // ## Prefix là gì?

# // // Prefix = phần đầu của một số khi viết dưới dạng chuỗi.

# // // Ví dụ:

# // // * `12345`

# // //   * prefix có thể là:

# // //     * `"1"`
# // //     * `"12"`
# // //     * `"123"`
# // //     * `"1234"`
# // //     * `"12345"`

# // // ---

# // // ## Prefix chung là gì?

# // // Hai số có prefix chung nếu phần đầu giống nhau.

# // // Ví dụ:

# // // * `1234` và `1239`

# // //   * cùng bắt đầu bằng:

# // //     * `"1"`
# // //     * `"12"`
# // //     * `"123"`

# // // → prefix chung dài nhất là `"123"`

# // // → độ dài = `3`

# // // ---

# // // # Ví dụ 1

# // // ```text
# // // arr1 = [1,10,100]
# // // arr2 = [1000]
# // // ```

# // // Xét:

# // // * `1` và `1000`

# // //   * prefix chung: `"1"`
# // //   * độ dài = 1

# // // * `10` và `1000`

# // //   * prefix chung: `"10"`
# // //   * độ dài = 2

# // // * `100` và `1000`

# // //   * prefix chung: `"100"`
# // //   * độ dài = 3

# // // => đáp án = `3`

# // // ---

# // // # Ví dụ 2

# // // ```text
# // // arr1 = [1,2,3]
# // // arr2 = [4,4,4]
# // // ```

# // // Không số nào có cùng chữ số đầu.

# // // → không có prefix chung

# // // → kết quả = `0`

# // // ---

# // // # Ý chính bài này

# // // Ta phải:

# // // 1. Lấy từng số trong `arr1`
# // // 2. So sánh với từng số trong `arr2`
# // // 3. Tìm prefix chung dài nhất
# // // 4. Trả về độ dài lớn nhất

# // // ---

# // // ## Ví dụ trực quan

# // // ```text
# // // 12345
# // // 12399
# // // ```

# // // So từng ký tự:

# // // ```text
# // // 1 = 1
# // // 2 = 2
# // // 3 = 3
# // // 4 != 9
# // // ```

# // // → dừng

# // // → prefix chung là `"123"`

# // // → độ dài = `3`

# // // ---

# // // ## Cách hiểu ngắn gọn

# // // Bài toán hỏi:

# // // > “Trong tất cả các cặp số giữa 2 mảng, cặp nào có phần đầu giống nhau dài nhất?”

# // Cách tiếp cận và ý tưởng giải bài**Longest Common Prefix**bằng Trie của bạn rất chuẩn và rõ ràng!Để bài viết dễ đọc,trực quan và chuyên nghiệp hơn,mình đã format lại bằng cách sử dụng các hộp điểm nhấn,sơ đồ cây trực quan và cấu trúc code mẫu chuẩn Java.

# // ---

# // ##💡Ý tưởng cốt lõi

# // Thay vì so sánh chuỗi(String)rất tốn tài nguyên,ta biểu diễn các số dưới dạng**cây tiền tố(Trie)**dựa trên các chữ số từ`0`đến`9`.

# // 1.**Bước 1:**Tách từng chữ số của các số trong`arr1`từ trái sang phải và thêm vào Trie.2.**Bước 2:**Duyệt qua từng số trong`arr2`,đi dọc theo cây Trie để đếm xem khớp được tối đa bao nhiêu chữ số đầu.

# // ---

# // ##🌲Trực quan hóa cấu trúc Trie

# // Giả sử ta thêm các số`123`,`129`,và`15`vào Trie.Cấu trúc cây sẽ được hình thành như sau:

# // ```text[root]│(1)/\(2)(5)/\(3)(9)

# // ```

# // ---

# // ##🛠️ Giải thích chi tiết các thành phần

# // ###1. Cấu trúc Node(`TrieNode`)

# // Mỗi node trên cây đại diện cho một chữ số.Vì các chữ số chỉ chạy từ`0`đến`9`,ta dùng một mảng cố định có kích thước 10.

# // ```java
# // private class TrieNode {
# //     // children[3] != null nghĩa là có nhánh đi tiếp theo chữ số 3
# //     private final TrieNode[] children;

# //     private TrieNode() {
# //         children = new TrieNode[10];
# //     }}

# //     ```

# //     ###2.

# //     Mảng base
# //     để tách
# //     chữ số

# //     Thay vì
# //     chuyển số

# //     thành chuỗi (gây tốn bộ nhớ), ta dùng một mảng các lũy thừa của 10 để tính toán trực tiếp trên số nguyên. Do số nguyên trong Java (`int`) tối đa có 10 chữ số, ta chuẩn bị sẵn mảng sau:

# // ```java

# //     private final int[] BASE = {
# //             1000000000, 100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1
# //     };

# //     ```

# //     >**Ví dụ
# //     toán học:**
# //     Với $x = 1234 $>*
# //     Muốn lấy
# //     chữ số đầu:$1234/1000=1 $>*
# //     Cắt bỏ
# //     chữ số đầu:$1234\pmod{1000}=234 $>*
# //     Chữ số
# //     tiếp theo:$234/100=2 $>>

# //     ###3.
# //     Hàm tìm
# //     vị trí

# //     bắt đầu (`getStartIndex`)

# // Hàm này tìm xem số $x$ lớn hơn lũy thừa nào của 10 để biết phải bắt đầu chia từ vị trí (`index`) nào trong mảng `BASE`.

# // ```java

# // private int getStartIndex(int x) {
# //     for (int i = 0; i < BASE.length; i++) {
# //         if (x >= BASE[i]) {
# //             return i; // Trả về vị trí bắt đầu chia
# //         }
# //     }
# //     return BASE.length - 1;
# // }

# //     ```

# //     ###4.

# //     Hàm thêm
# //     số vào

# //     Trie (`add`)

# // Hàm này thực hiện tách từng chữ số của $x$ từ trái qua phải và xây dựng các node tương ứng.

# // ```java

# // private void add(int x) {
# //     TrieNode node = root;
# //     int i = getStartIndex(x);

# //     while (i < BASE.length) {
# //         int digit = x / BASE[i]; // Lấy chữ số hiện tại
# //         if (node.children[digit] == null) {
# //             node.children[digit] = new TrieNode(); // Tạo node mới nếu chưa có
# //         }
# //         node = node.children[digit]; // Đi xuống node con
# //         x %= BASE[i]; // Cắt bỏ chữ số vừa xử lý
# //         i++;
# //     }
# // }

# //     ```

# //     ###5.

# //     Hàm tìm
# //     độ dài
# //     tiền tố

# //     chung (`find`)

# // Hàm này kiểm tra xem một số $x$ từ `arr2` có thể đi sâu bao nhiêu tầng vào cây Trie đã xây dựng từ `arr1`.

# // ```java

# // private int find(int x) {
# //     TrieNode node = root;
# //     int i = getStartIndex(x);
# //     int length = 0;

# //     while (i < BASE.length) {
# //         int digit = x / BASE[i];
# //         // Nếu trong Trie có chữ số này, ta đi tiếp và tăng độ dài đếm được
# //         if (node.children[digit] != null) {
# //             length++;
# //             node = node.children[digit];
# //         } else {
# //             break; // Gặp chữ số không khớp -> Dừng lại ngay
# //         }
# //         x %= BASE[i];
# //         i++;
# //     }
# //     return length;
# // }

# //     ```

# //     ---

# //     ##🚀

# //     Hàm chính
# //     và Toàn
# //     bộ Source
# //     Code

# //     Dưới
# //     đây là
# //     mã nguồn
# //     hoàn chỉnh
# //     được tổ
# //     chức gọn
# //     gàng để
# //     bạn có
# //     thể chạy ngay:

# //     ```java

# //     public class Solution {
# //         private class TrieNode {
# //             private final TrieNode[] children = new TrieNode[10];
# //         }

# //         private final TrieNode root = new TrieNode();
# //         private final int[] BASE = { 100000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1 };

# //         private int getStartIndex(int x) {
# //             for (int i = 0; i < BASE.length; i++) {
# //                 if (x >= BASE[i])
# //                     return i;
# //             }
# //             return BASE.length - 1;
# //         }

# //         private void add(int x) {
# //             TrieNode node = root;
# //             int i = getStartIndex(x);
# //             while (i < BASE.length) {
# //                 int digit = x / BASE[i];
# //                 if (node.children[digit] == null) {
# //                     node.children[digit] = new TrieNode();
# //                 }
# //                 node = node.children[digit];
# //                 x %= BASE[i];
# //                 i++;
# //             }
# //         }

# //         private int find(int x) {
# //             TrieNode node = root;
# //             int i = getStartIndex(x);
# //             int length = 0;
# //             while (i < BASE.length) {
# //                 int digit = x / BASE[i];
# //                 if (node.children[digit] != null) {
# //                     length++;
# //                     node = node.children[digit];
# //                 } else {
# //                     break;
# //                 }
# //                 x %= BASE[i];
# //                 i++;
# //             }
# //             return length;
# //         }

# //         public int longestCommonPrefix(int[] arr1, int[] arr2) {
# //             // Bước 1: Đưa toàn bộ số của arr1 vào Trie
# //             for (int num : arr1) {
# //                 add(num);
# //             }

# //             // Bước 2: Tìm prefix chung lớn nhất với các số trong arr2
# //             int maxPrefix = 0;
# //             for (int num : arr2) {
# //                 maxPrefix = Math.max(maxPrefix, find(num));
# //             }

# //             return maxPrefix;
# //         }
# //     }

# //     ```

# //     ---

# //     ##📊

# //     Đánh giá
# //     độ phức
# //     tạp thuật toán

# //     ***
# //     Độ phức
# //     tạp thời

# //     gian (Time Complexity):**
# // Mỗi số nguyên kiểu `int` có tối đa 9–10 chữ số. Do đó, thao tác `add` và `find` chỉ tốn tối đa một hằng số bước cố định $O(9) \approx O(1)$.
# // Gọi $N$ là số phần tử của `arr1` và $M$ là số phần tử của `arr2`, tổng thời gian chạy sẽ là:

# // $$\text{Tổng thời gian} = O(9 \times N + 9 \times M) \approx O(N + M)$$

# // Cách tiếp cận này tối ưu hơn rất nhiều so với việc duyệt trâu từng cặp

# // tốn $O(N \times M)$.
# // * **Độ phức tạp không

# // gian (Space Complexity):** $O(N \times 9 \times 10)$ cho việc lưu trữ các nút trên cây Trie, tuy nhiên do có nhiều tiền tố trùng nhau nên lượng bộ nhớ thực tế tiêu thụ thấp hơn rất nhiều.

# import java.util.Scanner;

# public class b240 {

#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         // Nhập số phần tử arr1
#         int n = sc.nextInt();

#         int[] arr1 = new int[n];

#         // Nhập arr1
#         for (int i = 0; i < n; i++) {
#             arr1[i] = sc.nextInt();
#         }

#         // Nhập số phần tử arr2
#         int m = sc.nextInt();

#         int[] arr2 = new int[m];

#         // Nhập arr2
#         for (int i = 0; i < m; i++) {
#             arr2[i] = sc.nextInt();
#         }

#         // In kết quả
#         System.out.println(longestCommonPrefix(arr1, arr2));

#         sc.close();
#     }

#     // Node của Trie
#     public static class TrieNode {

#         // Mỗi node có 10 nhánh từ 0 -> 9
#         public final TrieNode[] children;

#         public TrieNode() {
#             children = new TrieNode[10];
#         }
#     }

#     // Node gốc của Trie
#     public static TrieNode root;

#     // Mảng dùng để tách từng chữ số
#     // Ví dụ:
#     // 1234 / 1000 = 1
#     // 234 / 100 = 2
#     public static final int[] arr = {
#             100000000,
#             10000000,
#             1000000,
#             100000,
#             10000,
#             1000,
#             100,
#             10,
#             1
#     };

#     // Thêm một số vào Trie
#     public static void add(int x) {

#         // Bắt đầu từ root
#         TrieNode node = root;

#         // count(x) trả về vị trí bắt đầu
#         for (int i = count(x); i < 9; i++) {

#             // Lấy chữ số hiện tại
#             int digit = x / arr[i];

#             // Nếu chưa có node thì tạo mới
#             if (node.children[digit] == null) {
#                 node.children[digit] = new TrieNode();
#             }

#             // Di chuyển xuống node tiếp theo
#             node = node.children[digit];

#             // Loại bỏ chữ số vừa xử lý
#             x %= arr[i];
#         }
#     }

#     // Tìm độ dài prefix chung lớn nhất
#     public static int find(int x) {

#         TrieNode node = root;

#         // Biến lưu số chữ số giống nhau
#         int ans = 0;

#         for (int i = count(x); i < 9; i++) {

#             // Lấy chữ số hiện tại
#             int digit = x / arr[i];

#             // Nếu không tồn tại nhánh này
#             // nghĩa là không match tiếp được
#             if (node.children[digit] == null) {
#                 break;
#             }

#             // Đi tiếp xuống Trie
#             node = node.children[digit];

#             // Xóa chữ số đã xử lý
#             x %= arr[i];

#             // Tăng độ dài prefix
#             ans++;
#         }

#         return ans;
#     }

#     // Tìm vị trí bắt đầu theo số chữ số
#     // Ví dụ:
#     // 1234 >= 1000
#     // nên trả về index của 1000
#     public static int count(int x) {

#         for (int i = 0; i < 9; i++) {

#             if (x >= arr[i]) {
#                 return i;
#             }
#         }

#         return -1;
#     }

#     // Hàm chính xử lý bài toán
#     public static int longestCommonPrefix(int[] arr1, int[] arr2) {

#         // Khởi tạo Trie
#         root = new TrieNode();

#         // Thêm toàn bộ số của arr1 vào Trie
#         for (int i : arr1) {
#             add(i);
#         }

#         int ans = 0;

#         // Với mỗi số trong arr2
#         // tìm độ dài prefix chung lớn nhất
#         for (int i : arr2) {
#             ans = Math.max(ans, find(i));
#         }

#         return ans;
#     }
# }


from typing import List
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:



        # Set dùng để lưu tất cả prefix của arr1

        prefixes = set()



        # Duyệt từng số trong arr1

        for a in arr1:



            # Tạo tất cả prefix của số a

            # Ví dụ:

            # 12345 -> 12345, 1234, 123, 12, 1

            while a > 0:



                # Nếu prefix đã tồn tại

                # thì không cần xử lý tiếp

                if a in prefixes:

                    break



                # Thêm prefix vào set

                prefixes.add(a)



                # Xóa chữ số cuối cùng

                # Ví dụ:

                # 12345 -> 1234

                a = a // 10



        # Biến lưu prefix chung lớn nhất tìm được

        r = 0



        # Duyệt từng số trong arr2

        for b in arr2:



            # Chỉ tiếp tục khi b còn lớn hơn r

            # vì nếu nhỏ hơn thì số chữ số

            # cũng không thể lớn hơn đáp án hiện tại

            while b > r:



                # Nếu tìm thấy prefix xuất hiện trong arr1

                if b in prefixes:



                    # Cập nhật đáp án

                    r = b



                    # Dừng vì đã tìm được prefix dài nhất

                    # của số hiện tại

                    break



                # Xóa chữ số cuối

                # để kiểm tra prefix ngắn hơn

                b = b // 10



        # Nếu có prefix chung

        # trả về số lượng chữ số

        # Ví dụ:

        # 123 -> 3

        if r:

            return len(str(r))



        return 0

# Ý tưởng thuật toán

# Bước 1: Lưu toàn bộ prefix của arr1

# Ví dụ:



# arr1 = [1234]

# Ta tạo:



# 1234

# 123

# 12

# 1

# và lưu vào set:



# prefixes = {1234, 123, 12, 1}

# Bước 2: Kiểm tra arr2

# Ví dụ:



# b = 1299

# Ta kiểm tra:



# 1299

# 129

# # 12

# # 1

# # Kiểm tra:

# # 1299 -> không có

# # 129  -> không có

# # 12   -> có

# # → prefix chung dài nhất là:



# 12

# → độ dài = 2

# Ví dụ hoàn chỉnh

# arr1 = [1234, 567]

# arr2 = [1299, 56]

# prefixes sau bước 1

# {

# 1234,123,12,1,

# 567,56,5

# }

# Xử lý 1299

# 1299 -> không có

# 129  -> không có

# 12   -> có

# → r = 12

# Xử lý 56

# 56 -> có

# → r = 56

# Kết quả

# len(str(56)) = 2

# Độ phức tạp

# Giả sử mỗi số có tối đa d chữ số.



# Tạo prefixes

# O(n * d)

# Kiểm tra arr2

# O(m * d)

# Tổng

# O((n + m) * d)

# với d ≤ 9

# → rất nhanh.