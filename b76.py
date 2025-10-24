#  // 2048. Next Greater Numerically Balanced Number(24/10/2025)
# Đây là giải thích chi tiết cho thuật toán sinh số cân bằng số học (Numerically Balanced Number) sử dụng **Đệ quy Quay lui (Backtracking)** để tìm số lớn hơn tiếp theo.

# ## Giải thích Thuật toán Đệ quy Quay lui

# Thuật toán này sử dụng đệ quy để thử xây dựng tất cả các số cân bằng số học tiềm năng và tìm số nhỏ nhất trong số đó mà lớn hơn số $n$ đã cho.

# -----

### Phương thức Chính: `nextBeautifulNumber(self, n: int)`

# Phương thức này thiết lập môi trường và gọi hàm đệ quy để tìm kiếm kết quả.

# 1.  **Xác định Độ dài:**

#       * `length = len(str(n))`
#           * **Mục đích:** Bắt đầu tìm kiếm với các số có cùng độ dài với $n$.
#           * Số cân bằng số học nhỏ nhất lớn hơn $n$ sẽ có **độ dài bằng** $L$ (độ dài của $n$) hoặc **độ dài bằng** $L+1$.

# 2.  **Tìm kiếm số cùng độ dài ($L$):**

#       * `count = [0] * 10`
# #       * `result = self.generate(n, 0, length, count)`
#           * Gọi đệ quy để tìm số cân bằng số học **nhỏ nhất** có độ dài **$L$** và **lớn hơn $n$**. Nếu không tìm thấy, `result` sẽ là `0`.

# 3.  **Tìm kiếm số có độ dài lớn hơn ($L+1$):**

#       * `count = [0] * 10`
#       * `next_len_result = self.generate(0, 0, length + 1, count)`
#           * Gọi đệ quy để tìm số cân bằng số học **nhỏ nhất** có độ dài **$L+1$**. Vì đối số `n` được truyền vào là `0`, hàm sẽ tìm số cân bằng số học nhỏ nhất có độ dài $L+1$ (ví dụ: nếu $L=6$, nó tìm 1224444).

# 4.  **Tổng hợp Kết quả:**

#       * `if result == 0:`
#       * `result = next_len_result`
#           * Nếu không tìm thấy số cùng độ dài mà lớn hơn $n$, thì chắc chắn kết quả phải là số cân bằng số học nhỏ nhất có độ dài $L+1$.
#       * Cuối cùng, trả về `result`.

class Solution:
    # --- Hàm Đệ quy Quay lui để sinh số cân bằng số học (Numerically Balanced Number) ---
    def generate(self, n: int, current: int, remaining: int, count: list[int]) -> int:
        # Điều kiện Dừng (Base Case): Số đã được xây dựng xong.
        if remaining == 0:
            # 1. Kiểm tra điều kiện "Lớn hơn n": số được sinh ra phải lớn hơn n.
            # 2. Kiểm tra điều kiện "Cân bằng Số học": Với mọi chữ số i,
            #    số lần xuất hiện c phải bằng 0 (không dùng) hoặc bằng chính i (c = i).
            if current > n and all(c == 0 or c == i for i, c in enumerate(count)):
                return current  # Trả về số cân bằng hợp lệ nhỏ nhất tìm được.
            return 0  # Số không hợp lệ (nhỏ hơn n hoặc không cân bằng).

        result = 0
        # Duyệt các chữ số 'd' từ 1 đến 9 để thêm vào cuối số 'current'.
        # Việc duyệt từ nhỏ đến lớn đảm bảo ta tìm được số nhỏ nhất trước.
        for d in range(1, 10):
            
            # --- Tỉa nhánh (Pruning) và Điều kiện Cân bằng ---
            # 1. 'count[d] < d': Chữ số 'd' chưa xuất hiện đủ d lần.
            # 2. 'd - count[d] <= remaining': Số lần chữ số 'd' cần thêm vào (d - count[d]) 
            #    phải NHỎ HƠN HOẶC BẰNG số lượng chữ số còn lại (remaining). Nếu không, không thể cân bằng được.
            if count[d] < d and d - count[d] <= remaining:
                
                count[d] += 1  # 1. Đánh dấu chữ số 'd' đã được sử dụng (chọn).
                
                # Gọi đệ quy: Thêm 'd' vào cuối 'current' và giảm số chữ số còn lại.
                result = self.generate(n, current * 10 + d, remaining - 1, count)
                
                count[d] -= 1  # 2. Quay lui (Backtrack): Hoàn tác thay đổi cho lần lặp tiếp theo.
                
                # 3. Dừng ngay lập tức: Nếu result khác 0, nghĩa là ta đã tìm thấy 
                #    số cân bằng số học nhỏ nhất hợp lệ, vì ta duyệt d từ 1 đến 9.
                if result != 0:
                    return result

        return result  # Trả về 0 nếu không tìm thấy số hợp lệ từ nhánh này.

    # --- Phương thức Chính ---
    def nextBeautifulNumber(self, n: int) -> int:
        # Bắt đầu tìm kiếm với độ dài bằng n.
        length = len(str(n))
        count = [0] * 10

        # Bước 1: Tìm số cân bằng số học nhỏ nhất có độ dài L (length) VÀ > n.
        result = self.generate(n, 0, length, count)
        
        # Bước 2: Tìm số cân bằng số học nhỏ nhất có độ dài L+1.
        # Ta dùng n=0 để ensure 'generate' tìm số cân bằng nhỏ nhất (vì mọi số > 0).
        count = [0] * 10 
        next_len_result = self.generate(0, 0, length + 1, count)
        
        # Bước 3: Tổng hợp kết quả.
        if result == 0:
            # Nếu không tìm thấy số cùng độ dài (result=0), kết quả phải là 
            # số cân bằng nhỏ nhất có độ dài lớn hơn.
            result = next_len_result
            
        return result
### Hàm Đệ quy: `generate(self, n: int, current: int, remaining: int, count: list[int])`

# Hàm này là cốt lõi của thuật toán, sử dụng kỹ thuật **Quay lui (Backtracking)** để sinh số.

#### Tham số:

#   * `n`: Số mục tiêu cần vượt qua (chỉ được sử dụng ở bước cuối cùng).
#   * `current`: Số đang được xây dựng (ở dạng số nguyên).
#   * `remaining`: Số lượng chữ số cần thêm vào để hoàn thành số.
#   * `count`: Mảng tần suất (độ dài 10) lưu số lần xuất hiện của mỗi chữ số (chỉ mục $i$ lưu số lần chữ số $i$ xuất hiện).

# #### 1\. Điều kiện Dừng (Base Case):

# ```python
# if remaining == 0:
    # 1. Số đã hoàn thành (đã đủ L hoặc L+1 chữ số).
    # 2. Kiểm tra điều kiện "Cân bằng Số học":
#     if current > n and all(c == 0 or c == i for i, c in enumerate(count)):
#         return current  # Trả về kết quả nếu nó > n VÀ thỏa mãn điều kiện cân bằng.
#     return 0  # Không thỏa mãn.
# ```

#   * **Kiểm tra tính Cân bằng:** `all(c == 0 or c == i for i, c in enumerate(count))`
#       * Duyệt qua mảng `count`. Đối với mỗi chữ số $i$ (từ 0 đến 9), số lần xuất hiện $c$ phải bằng 0 (chữ số không được sử dụng) hoặc bằng chính giá trị của nó ($c = i$).
#   * **Kiểm tra Điều kiện Lớn hơn:** `current > n`
#       * Chỉ chấp nhận số nếu nó lớn hơn số $n$ ban đầu.

# #### 2\. Bước Đệ quy (Recursive Step):

# ```python
# # result = 0
# # for d in range(1, 10):
#     # Thử thêm chữ số 'd' vào cuối số 'current'
    
#     # Pruning (Tỉa nhánh) và Kiểm tra Điều kiện Cân bằng:
#     if result == 0 and count[d] < d and d - count[d] <= remaining:
#         # result == 0: Đảm bảo ta tìm thấy số nhỏ nhất. Nếu đã tìm thấy 1 kết quả hợp lệ, ta dừng.
#         # count[d] < d: Số lần chữ số 'd' xuất hiện chưa đạt đến d (chưa đủ điều kiện cân bằng).
#         # d - count[d] <= remaining: Số lần chữ số 'd' cần thêm vào (d - count[d]) 
#         # phải nhỏ hơn hoặc bằng số chữ số còn lại (remaining). Nếu không, số đó sẽ không bao giờ cân bằng được.

#         # Thực hiện Bước đệ quy:
#         count[d] += 1  # 1. Đánh dấu chữ số 'd' đã được sử dụng.
        
#         result = self.generate(n, current * 10 + d, remaining - 1, count)
        
#         count[d] -= 1  # 2. Quay lui: Hoàn tác thay đổi để thử chữ số tiếp theo.
        
#         # Vì chúng ta duyệt d từ 1 đến 9, số đầu tiên tìm thấy (result != 0) sẽ là 
#         # số cân bằng số học hợp lệ nhỏ nhất. Ta dùng điều kiện 'if result == 0 and ...' 
#         # để đảm bảo dừng lại ngay khi tìm thấy.

# return result
# ```

#   * **Tỉa nhánh (Pruning):** Điều kiện `d - count[d] <= remaining` là một kỹ thuật tối ưu hóa quan trọng. Nó loại bỏ các nhánh tìm kiếm không thể dẫn đến kết quả cân bằng số học.
#   * **Tìm số Nhỏ nhất:** Vòng lặp `for d in range(1, 10)` đảm bảo ta luôn thử các chữ số nhỏ hơn trước. Kết hợp với việc kiểm tra `if result == 0`, ngay khi tìm thấy một số hợp lệ, ta dừng lại và trả về nó.

# ## Tối ưu hóa (Why this is fast)

# 1.  **Tỉa nhánh:** Giảm thiểu đáng kể không gian tìm kiếm bằng cách loại bỏ các nhánh không khả thi.
# 2.  **Duyệt tối ưu:** Duyệt chữ số từ $1 \to 9$ đảm bảo số được xây dựng là **nhỏ nhất** có thể.
# 3.  **Chiến lược Độ dài:** Chia bài toán thành hai phần (cùng độ dài $L$ và độ dài $L+1$) giúp tìm kiếm hiệu quả hơn, đặc biệt đối với các số cùng độ dài mà lớn hơn $n$ (vì ta chỉ cần tìm số đầu tiên thỏa mãn).
# import java.util.*;

# public class b77 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int n = sc.nextInt();
#         System.out.println(nextBeautifulNumber(n));
#     }

#     public static final int[] balance = new int[] {
#             1, 22, 122, 212, 221, 333, 1333, 3133, 3313, 3331, 4444, 14444, 22333, 23233,
#             23323, 23332, 32233, 32323, 32332, 33223, 33232, 33322, 41444, 44144, 44414,
#             44441, 55555, 122333, 123233, 123323, 123332, 132233, 132323, 132332, 133223,
#             133232, 133322, 155555, 212333, 213233, 213323, 213332, 221333, 223133, 223313,
#             223331, 224444, 231233, 231323, 231332, 232133, 232313, 232331, 233123, 233132,
#             233213, 233231, 233312, 233321, 242444, 244244, 244424, 244442, 312233, 312323,
#             312332, 313223, 313232, 313322, 321233, 321323, 321332, 322133, 322313, 322331,
#             323123, 323132, 323213, 323231, 323312, 323321, 331223, 331232, 331322, 332123,
#             332132, 332213, 332231, 332312, 332321, 333122, 333212, 333221, 422444, 424244,
#             424424, 424442, 442244, 442424, 442442, 444224, 444242, 444422, 515555, 551555,
#             555155, 555515, 555551, 666666, 1224444
#     };

#     /**
#      * Tìm số cân bằng số học nhỏ nhất mà lớn hơn số n cho trước.
#      * 
#      * Số nguyên đầu vào.
#      * Số cân bằng số học nhỏ nhất > n.
#      */
#     public static int nextBeautifulNumber(int n) {
#         // 1. Mục tiêu: Tìm số x trong mảng 'balance' sao cho x là nhỏ nhất và x > n.
#         // Điều này tương đương với việc tìm số nhỏ nhất x sao cho x >= n + 1.

#         // 2. Sử dụng Arrays.binarySearch để tìm vị trí của (n + 1) trong mảng
#         // 'balance'.
#         int i = Arrays.binarySearch(balance, n + 1);

#         // 3. Xử lý kết quả của tìm kiếm nhị phân:
#         if (i < 0) {
#             // Nếu i < 0, tức là (n + 1) KHÔNG có trong mảng.
#             // i sẽ là: -(điểm chèn) - 1.
#             // Điểm chèn là chỉ mục của phần tử đầu tiên lớn hơn (n + 1).
#             // Ta cần chuyển i về chỉ mục của phần tử đó (i_chèn = -i - 1).
#             i = -i - 1;
#         }
#         // Nếu i >= 0 (Trường hợp tìm thấy): i là chỉ mục của (n + 1),
#         // đây chính là số cân bằng số học đầu tiên >= n + 1.

#         // 4. Trả về phần tử tại chỉ mục i, đây chính là số cân bằng số học
#         // lớn hơn n tiếp theo.
#         return balance[i];
#     }
# }

# // Mảng chứa tất cả các "Số Cân Bằng Số Học" (Numerically Balanced Numbers)
# // đã được tính toán trước và sắp xếp theo thứ tự tăng dần.
# // Việc này khai thác giới hạn nhỏ của bài toán (các số này không quá lớn).

# // Bạn đang hỏi về bài toán **"2048. Next Greater Numerically Balanced Number"**
# // (Số cân bằng số học lớn hơn tiếp theo) trên LeetCode.

# // ## Giải thích Đề bài

# // Đề bài yêu cầu bạn tìm **số cân bằng số học lớn hơn tiếp theo** (the next
# // greater numerically balanced number) so với một số nguyên dương $n$ đã cho.

# // ### 1. Số Cân bằng Số học (Numerically Balanced Number) là gì?

# // Một số nguyên dương được gọi là **cân bằng số học** nếu với **mỗi chữ số
# // $d$** có trong số đó, thì **số lần xuất hiện** của chữ số $d$ trong số đó
# // phải **bằng chính giá trị của $d$**.

# // #### Ví dụ về Số Cân bằng Số học:

# // * **22:**
# // * Chữ số có mặt là **2**.
# // * Số lần xuất hiện của chữ số **2** là **2** lần.
# // * Vì $2 = 2$, nên **22** là số cân bằng số học.
# // * **1333:**
# // * Chữ số **1** xuất hiện **1** lần.
# // * Chữ số **3** xuất hiện **3** lần.
# // * Vì $1 = 1$ và $3 = 3$, nên **1333** là số cân bằng số học.
# // * **122:**
# // * Chữ số **1** xuất hiện **1** lần.
# // * Chữ số **2** xuất hiện **2** lần.
# // * Vì $1 = 1$ và $2 = 2$, nên **122** là số cân bằng số học.

# // #### Ví dụ về Số KHÔNG Cân bằng Số học:

# // * **33:**
# // * Chữ số **3** xuất hiện **2** lần.
# // * Vì $2 \neq 3$, nên **33** không phải là số cân bằng số học.
# // * **121:**
# // * Chữ số **1** xuất hiện **2** lần.
# // * Chữ số **2** xuất hiện **1** lần.
# // * Đối với chữ số **1**: số lần xuất hiện ($2$) $\neq$ giá trị ($1$).
# // * Đối với chữ số **2**: số lần xuất hiện ($1$) $\neq$ giá trị ($2$).
# // * Nên **121** không phải là số cân bằng số học.

# // ***

# // ### 2. Yêu cầu của Bài toán

# // Cho một số nguyên dương $n$. Bạn cần tìm **số cân bằng số học nhỏ nhất** mà
# // **lớn hơn** $n$.

# // Tóm lại:
# // $$\text{Kết quả} = \min \{\text{số cân bằng số học } x \mid x > n\}$$

# // #### Ví dụ minh họa:

# // * **Nếu $n = 1$:**
# // * Các số cân bằng số học (theo thứ tự tăng dần) là: **1**, 22, 122, 212, 221,
# // 333, 1333, ...
# // * Số cân bằng số học đầu tiên lớn hơn 1 là **22**.
# // * **Nếu $n = 1000$:**
# // * Các số cân bằng số học lớn hơn 1000 là: 1333, 3133, 3313, 3331, 4444, ...
# // * Số cân bằng số học nhỏ nhất lớn hơn 1000 là **1333**.
# // Đây là một cách tiếp cận rất **hiệu quả và đơn giản** để giải quyết bài toán
# // "2048. Next Greater Numerically Balanced Number" (Số Cân Bằng Số Học Lớn Hơn
# // Tiếp Theo).

# // Thuật toán này dựa trên một nhận xét quan trọng: **phạm vi giới hạn của bài
# // toán**.

# // ---

# // ## Giải thích Thuật toán (Pre-computation và Binary Search)

# // Thuật toán trong đoạn mã trên sử dụng phương pháp **tính toán trước**
# // (pre-computation) và **tìm kiếm nhị phân** (binary search) để tìm ra kết quả.

# // ### 1. Tính toán trước (Pre-computation)

# // Các số cân bằng số học (Numerically Balanced Numbers) là rất hiếm và không
# // quá lớn trong giới hạn của các kiểu dữ liệu số nguyên tiêu chuẩn (ví dụ,
# // $2^{31}-1 \approx 2 \times 10^9$).

# // * Số cân bằng số học lớn nhất có thể là $666666$ (6 chữ số $6$, tổng cộng $6$
# // chữ số).
# // * Số cân bằng số học tiếp theo sẽ phải chứa chữ số $7$ (xuất hiện 7 lần), có
# // nghĩa là nó sẽ có ít nhất 7 chữ số.
# // * Số cân bằng số học lớn nhất trong mảng `balance` là $1224444$ (tổng cộng 7
# // chữ số: một chữ số 1, hai chữ số 2, bốn chữ số 4. Tổng số chữ số là
# // $1+2+4=7$).
# // * Do giới hạn của $n$ (thường là $10^6$ hoặc $10^7$ trong các bài toán
# // LeetCode), mảng `balance` đã liệt kê tất cả các số cân bằng số học lên đến
# // một giới hạn đủ lớn (trong trường hợp này, đến khoảng $1.2$ triệu, nhưng các
# // số cân bằng thực tế có thể lên tới $6,666,666$ hoặc cao hơn một chút nếu xét
# // các hoán vị của $1,2,2,3,3,3$). Mảng được cung cấp đã liệt kê các số cân bằng
# // lên đến $666666$ và một số số $7$ chữ số khác như $1224444$.

# // * Mảng **`balance`** chính là danh sách **tất cả** các số cân bằng số học có
# // giá trị nhỏ, được sắp xếp theo thứ tự tăng dần.

# // ### 2. Tìm kiếm Nhị phân (Binary Search)

# // Mục tiêu của bài toán là tìm số cân bằng số học nhỏ nhất $x$ sao cho $x > n$.
# // Điều này tương đương với việc tìm số cân bằng số học nhỏ nhất $x$ trong danh
# // sách **lớn hơn hoặc bằng** $n + 1$.

# // 1. **Chuyển đổi mục tiêu tìm kiếm:** Hàm `nextBeautifulNumber(int n)` cần tìm
# // số $\min(x)$ với $x \in \text{balance}$ và $x \geq n + 1$.

# // 2. **Sử dụng `Arrays.binarySearch(balance, n + 1)`:**
# // * Hàm tìm kiếm nhị phân được sử dụng để tìm vị trí của giá trị **$n + 1$**
# // trong mảng `balance`.

# // 3. **Xử lý kết quả của `binarySearch`:**
# // * **Trường hợp 1: Tìm thấy (Exact Match):** Nếu $n + 1$ là một số cân bằng số
# // học, `binarySearch` trả về một chỉ mục $i \geq 0$. Kết quả là `balance[i]`.
# // * **Trường hợp 2: Không tìm thấy (Insertion Point):** Nếu $n + 1$ không phải
# // là số cân bằng số học, `binarySearch` trả về một giá trị âm: $-(\text{điểm
# // chèn} + 1)$. **Điểm chèn** (Insertion Point) chính là chỉ mục của phần tử đầu
# // tiên lớn hơn $n + 1$.
# // * Để chuyển giá trị âm này về chỉ mục cần tìm, ta thực hiện:
# // $$i = -i - 1$$
# // Ví dụ: Nếu `binarySearch` trả về $-5$, thì $i = -(-5) - 1 = 5 - 1 = 4$. Chỉ
# // mục $4$ là vị trí của phần tử đầu tiên lớn hơn $n + 1$.

# // 4. **Trả về kết quả:** Sau khi tìm được chỉ mục $i$ chính xác, `balance[i]`
# // chính là **số cân bằng số học nhỏ nhất lớn hơn hoặc bằng** $n + 1$ (tức là số
# // cân bằng số học nhỏ nhất lớn hơn $n$).

# // ---

# // ## Ưu điểm và Nhược điểm

# // ### Ưu điểm

# // | Ưu điểm | Giải thích |
# // | :--- | :--- |
# // | **Tốc độ cực nhanh ($\mathcal{O}(\log k)$)** | Vì mảng `balance` đã được
# // tính toán trước và sắp xếp, việc tìm kiếm chỉ mất thời gian $\mathcal{O}(\log
# // k)$ (với $k$ là kích thước của mảng `balance`), rất nhanh so với việc tạo ra
# // các số một cách động. |
# // | **Đơn giản** | Logic tìm kiếm rất gọn gàng và dễ hiểu. |
# // | **Hoàn hảo cho giới hạn bài toán** | Do số lượng các số cân bằng số học là
# // hữu hạn và không lớn trong giới hạn $10^7$, phương pháp này là tối ưu. |

# // ### Nhược điểm

# // | Nhược điểm | Giải thích |
# // | :--- | :--- |
# // | **Yêu cầu tính toán trước** | Phương pháp này chỉ hoạt động vì chúng ta đã
# // liệt kê được tất cả các số cân bằng số học. Nếu giới hạn của $n$ lớn hơn
# // nhiều (ví dụ $10^{18}$), mảng này sẽ quá lớn hoặc không thể xây dựng, và cần
# // phải sử dụng thuật toán sinh số động (dynamic generation). |
# // | **Thiếu tính tổng quát** | Nó là giải pháp cụ thể cho bài toán này, không
# // dễ dàng áp dụng cho các bài toán tương tự với quy tắc "cân bằng" phức tạp hơn
# // hoặc giới hạn lớn hơn. |