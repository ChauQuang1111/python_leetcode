# // Bài LeetCode **1674 - Minimum Moves to Make Array Complementary(13/05/2026)
# // ---
from typing import List
from itertools import accumulate


class Solution:

    def minMoves(self, nums: List[int], limit: int) -> int:

        n = len(nums)

        # deltas dùng làm Difference Array
        #
        # Sau khi prefix sum:
        # cost[target] = n + prefix[target]
        #
        # Ban đầu:
        # mỗi cặp được xem như cần 2 moves
        #
        # Vì có n/2 cặp:
        # tổng cost ban đầu = n
        #
        # Sau đó dùng deltas để giảm cost

        deltas = [0] * ((limit << 1) + 2)

        lp = 0
        rp = n - 1

        # Duyệt các cặp đối xứng
        while lp < rp:

            left = nums[lp]
            right = nums[rp]

            # small <= large
            if left <= right:
                small = left
                large = right
            else:
                small = right
                large = left

            """
            Với cặp (small, large)

            target sum có thể từ:
            2 -> 2*limit

            ------------------------------------------------

            1. Ban đầu:
               mọi target đều cần 2 moves

            ------------------------------------------------

            2. Target trong đoạn:

               [small + 1 , large + limit]

               chỉ cần 1 move

               => giảm cost đi 1

            ------------------------------------------------

            3. Tại target = small + large

               cần 0 move

               => giảm thêm 1 lần nữa
            """

            # ------------------------------------------
            # Giảm 1 move cho đoạn:
            #
            # [small + 1 , large + limit]
            #
            # Difference Array:
            #
            # deltas[l] += val
            # deltas[r+1] -= val
            #
            # Ở đây val = -1
            # ------------------------------------------

            deltas[small + 1] -= 1

            deltas[large + limit + 1] += 1

            # ------------------------------------------
            # Tại đúng tổng hiện tại:
            #
            # target = small + large
            #
            # giảm thêm 1 lần nữa
            #
            # từ:
            # 1 move -> 0 move
            # ------------------------------------------

            deltas[small + large] -= 1

            deltas[small + large + 1] += 1

            lp += 1
            rp -= 1

        """
        accumulate(deltas)
        = prefix sum

        prefix[target]
        = tổng thay đổi cost tại target

        Cost thật:
        n + prefix[target]

        Lấy min trên mọi target.
        """

        return n + min(accumulate(deltas))
# // Ta sẽ giải thích ý tưởng của đoạn code này theo đúng logic của bài.

# // ---

# // # Ý tưởng tổng quát

# // Với mỗi cặp:

# // ```text id="bvf32o"
# // (nums[i], nums[n-1-i])
# // ```

# // ta muốn tất cả các cặp có cùng tổng `target`.

# // ---

# // Mỗi cặp với một `target` sẽ rơi vào:

# // * `0 move`
# // * `1 move`
# // * `2 move`

# // ---

# // # Ý tưởng cực quan trọng

# // Thay vì:

# // ```text id="mjz5n5"
# // thử từng target cho từng cặp
# // ```

# // (O(n * limit))

# // ta sẽ:

# // ```text id="zwy9oh"
# // đếm nhanh:
# // - bao nhiêu cặp cần ≤1 move
# // - bao nhiêu cặp cần 0 move
# // ```

# // rồi suy ra đáp án.

# // ---

# // # Phần 1: oneMove[]

# // ```java
# // int[] oneMove = new int[2 * limit + 2];
# // ```

# // Mảng difference array.

# // Nó dùng để đánh dấu:

# // ```text id="nd7kw1"
# // target nào có thể đạt bằng <=1 move
# // ```

# // ---

# // # Phần 2: noMove

# // ```java
# // Map<Integer, Integer> noMove = new HashMap<>();
# // ```

# // Lưu:

# // ```text id="i4v2lu"
# // bao nhiêu cặp đã có tổng = target
# // ```

# // tức là cần `0 move`.

# // ---

# // # Duyệt từng cặp

# // ```java
# // for (int i = 0; i < nums.length / 2; i++)
# // ```

# // Ghép:

# // ```java
# // j = n-1-i
# // ```

# // ---

# // Ví dụ:

# // ```text id="4p9yce"
# // nums = [1,2,4,3]
# // ```

# // cặp:

# // ```text id="w76qzq"
# // (1,3)
# // (2,4)
# // ```

# // ---

# // # 1. Đếm no move

# // ```java
# // noMove.merge(nums[i] + nums[j], 1, Integer::sum);
# // ```

# // Ví dụ:

# // ```text id="dk4z55"
# // (1,3)
# // sum = 4
# // ```

# // thì:

# // ```text id="t54wd1"
# // target=4
# // ```

# // cặp này cần 0 move.

# // ---

# // # 2. Đánh dấu vùng 1 move

# // ```java
# // oneMove[min + 1]++;
# // oneMove[max + limit + 1]--;
# // ```

# // ---

# // # Vì sao?

# // Giả sử:

# // ```text id="i8fdfy"
# // (a,b) = (2,5)
# // limit = 6
# // ```

# // ---

# // ## Những tổng đạt được bằng 1 move

# // Nếu đổi `2`:

# // ```text id="5z5d83"
# // [1..6] + 5
# // =
# // [6..11]
# // ```

# // Nếu đổi `5`:

# // ```text id="4a08lj"
# // 2 + [1..6]
# // =
# // [3..8]
# // ```

# // Gộp:

# // ```text id="9m5ghz"
# // [3..11]
# // ```

# // ---

# // Công thức tổng quát:

# // ```text id="0cfmsw"
# // [min(a,b)+1 , max(a,b)+limit]
# // ```

# // ---

# // Code:

# // ```java
# // oneMove[Math.min(a,b)+1]++;
# // oneMove[Math.max(a,b)+limit+1]--;
# // ```

# // để cộng đoạn bằng difference array.

# // ---

# // # Difference Array hoạt động thế nào

# // Ví dụ:

# // ```text id="yg1jqj"
# // +1 cho đoạn [3,11]
# // ```

# // ta làm:

# // ```text id="8p5qyk"
# // diff[3] += 1
# // diff[12] -= 1
# // ```

# // Sau prefix sum:

# // ```text id="q8i7lj"
# // 3..11 đều +1
# // ```

# // ---

# // # one nghĩa là gì?

# // ```java
# // one += oneMove[i];
# // ```

# // Sau prefix sum:

# // ```text id="7m4wrn"
# // one = số cặp có thể đạt target=i bằng <=1 move
# // ```

# // ---

# // # Tính cost cho mỗi target

# // ```java
# // ans = Math.min(
# //     ans,
# //     one + 2 * (pairs - one) - noMove.getOrDefault(i, 0)
# // );
# // ```

# // Đây là phần quan trọng nhất.

# // ---

# // Giả sử:

# // ```text id="73k7r5"
# // pairs = nums.length / 2
# // ```

# // ---

# // ## one cặp

# // Các cặp trong `one`:

# // ```text id="otih3j"
# // cần tối đa 1 move
# // ```

# // tạm tính:

# // ```text id="u3q02v"
# // 1 move mỗi cặp
# // ```

# // nên:

# // ```text id="6c4l7d"
# // one
# // ```

# // ---

# // ## Các cặp còn lại

# // ```text id="lq1hmb"
# // pairs - one
# // ```

# // không nằm trong vùng 1 move.

# // Nên chắc chắn cần:

# // ```text id="b1i6oi"
# // 2 move
# // ```

# // tổng:

# // ```text id="rxs8z2"
# // 2 * (pairs - one)
# // ```

# // ---

# // ## Nhưng có cặp thật ra cần 0 move

# // Ta đã tính:

# // ```text id="lnx2mk"
# // 1 move
# // ```

# // cho toàn bộ nhóm `one`.

# // Nhưng:

# // ```text id="n9q13u"
# // noMove[i]
# // ```

# // cặp thật ra cần:

# // ```text id="o98n9p"
# // 0 move
# // ```

# // nên phải trừ đi.

# // ---

# // # Công thức cuối

# // ```text id="fwz5g9"
# // total =
# // 1 * (số cặp 1 move hoặc 0 move)
# // + 2 * (số cặp 2 move)
# // - (số cặp 0 move)
# // ```

# // ---

# // # Ví dụ trực quan

# // Giả sử:

# // ```text id="5tr8vb"
# // pairs = 5
# // one = 4
# // noMove = 2
# // ```

# // ---

# // Ban đầu:

# // ```text id="k9lk0m"
# // 4 cặp ×1 move = 4
# // 1 cặp ×2 move = 2
# // => 6
# // ```

# // ---

# // Nhưng trong 4 cặp đó có 2 cặp thực ra 0 move:

# // ```text id="m6z2zw"
# // 6 - 2 = 4
# // ```

# // ---

# // # Độ phức tạp

# // ## Time

# // ```text id="s6mhdg"
# // O(n + limit)
# // ```

# // ---

# // ## Space

# // ```text id="e6ymlm"
# // O(limit)
# // ```

# // ---

# // # Ý tưởng cốt lõi cần nhớ

# // ## Với một cặp `(a,b)`:

# // ---

# // ## 0 move

# // ```text id="pq9j5l"
# // target = a+b
# // ```

# // ---

# // ## 1 move

# // ```text id="6a8td0"
# // target ∈ [min+1 , max+limit]
# // ```

# // ---

# // ## 2 move

# // Ngoài đoạn trên.

# // ---

# // Đây chính là nền tảng toàn bộ bài 1674.

# // # Đề bài

# // Cho một mảng `nums` có độ dài **chẵn** và một số `limit`.

# // Ta ghép các phần tử đối xứng:

# // * `nums[0]` với `nums[n-1]`
# // * `nums[1]` với `nums[n-2]`
# // * ...

# // Mỗi cặp phải có cùng tổng sau khi chỉnh sửa.

# // ---

# // ## Bạn được phép làm gì?

# // Trong **1 move**, bạn có thể:

# // * đổi giá trị của một phần tử bất kỳ thành số từ `1 -> limit`

# // ---

# // # Mục tiêu

# // Tìm số move nhỏ nhất để:

# // TẤT CẢ các cặp đối xứng đều có cùng tổng.

# // ---

# // # Ví dụ

# // ```text
# // nums = [1,2,4,3]
# // limit = 4
# // ```

# // Các cặp:

# // ```text
# // (1,3) => tổng = 4
# // (2,4) => tổng = 6
# // ```

# // Hiện tại tổng chưa giống nhau.

# // ---

# // Ta muốn mọi cặp có cùng sum.

# // Ví dụ chọn target sum = 4:

# // * (1,3) đã đúng → 0 move
# // * (2,4):
# //   đổi 4 -> 2
# //   thành (2,2) => tổng 4

# //   cần 1 move

# // Tổng = 1 move.

# // Đáp án là `1`.

# // ---

# // # Ý nghĩa chữ "Complementary"

# // Một mảng complementary nghĩa là:

# // ```text
# // nums[i] + nums[n-1-i]
# // ```

# // đều bằng nhau với mọi `i`.

# // ---

# // # Phân tích số move của một cặp

# // Xét một cặp:

# // ```text
# // (a,b)
# // ```

# // Ta muốn biến thành tổng `x`.

# // ---

# // ## 0 move

# // Nếu:

# // ```text
# // a + b = x
# // ```

# // ---

# // ## 1 move

# // Ta đổi 1 số.

# // Ví dụ:

# // ```text
# // (a,b) = (2,5)
# // limit = 6
# // ```

# // Muốn tổng = 7:

# // * đã có 2+5=7 → 0 move

# // Muốn tổng = 6:

# // * đổi 5 -> 4
# // * được 2+4=6

# // → 1 move.

# // ---

# // ### Khoảng có thể đạt bằng 1 move

# // Nếu giữ `a`:

# // ```text
# // a + [1..limit]
# // ```

# // Nếu giữ `b`:

# // ```text
# // b + [1..limit]
# // ```

# // Gộp lại:

# // ```text
# // [min(a,b)+1 , max(a,b)+limit]
# // ```

# // Trong khoảng này → chỉ cần 1 move.

# // ---

# // ## 2 move

# // Nếu target nằm ngoài khoảng trên.

# // ---

# // # Ý tưởng tối ưu

# // Target sum có thể từ:

# // ```text
# // 2 -> 2*limit
# // ```

# // Ta thử mọi target.

# // ---

# // # Cost của mỗi cặp

# // Với mỗi cặp `(a,b)`:

# // ## Ban đầu:

# // mọi target cần 2 move.

# // ---

# // ## Giảm xuống 1 move

# // Trong đoạn:

# // ```text
# // [min(a,b)+1 , max(a,b)+limit]
# // ```

# // ---

# // ## Giảm xuống 0 move

# // Tại:

# // ```text
# // a+b
# // ```

# // ---

# // # Dùng Difference Array

# // Ta cập nhật nhanh:

# // ```text
# // diff[l] += val
# // diff[r+1] -= val
# // ```

# // để tính tổng cost cho mọi target.

# // ---

# // # Flow chuẩn

# // Với mỗi cặp `(a,b)`:

# // ```text
# // low = min(a,b)+1
# // high = max(a,b)+limit
# // sum = a+b
# // ```

# // ---

# // ## Ban đầu toàn bộ là 2 moves

# // ```text
# // diff[2] += 2
# // diff[2*limit +1] -= 2
# // ```

# // ---

# // ## Đoạn chỉ cần 1 move

# // ```text
# // diff[low] -= 1
# // diff[high+1] += 1
# // ```

# // ---

# // ## Tại đúng sum cần 0 move

# // ```text
# // diff[sum] -= 1
# // diff[sum+1] += 1
# // ```

# // ---

# // # Sau đó

# // Prefix sum để tính:

# // ```text
# // cost[target]
# // ```

# // Lấy min.

# // ---

# // # Minh họa trực quan

# // Ví dụ:

# // ```text
# // (a,b)=(2,5)
# // limit=6
# // ```

# // ---

# // ## 2 moves ở mọi nơi

# // ```text
# // 2 2 2 2 2 2 2 2 2 2 2
# // target:
# // 2 3 4 5 6 7 8 9 10 11 12
# // ```

# // ---

# // ## 1 move trong đoạn

# // ```text
# // [min+1,max+limit]
# // =
# // [3,11]
# // ```

# // thành:

# // ```text
# // 2 1 1 1 1 1 1 1 1 1 2
# // ```

# // ---

# // ## 0 move tại sum=7

# // ```text
# // 2 1 1 1 1 0 1 1 1 1 2
# // ```

# // ---

# // # Độ phức tạp

# // Có:

# // * `n/2` cặp
# // * target từ `2 -> 2*limit`

# // Độ phức tạp:

# // ```text
# // O(n + limit)
# // ```

# // rất tối ưu.

# // ---

# // # Code Java ngắn gọn

# // ```java
# // class Solution {
# //     public int minMoves(int[] nums, int limit) {
# //         int n = nums.length;
# //         int[] diff = new int[2 * limit + 2];

# //         int left = 0;
# //         int right = n - 1;

# //         while (left < right) {
# //             int a = nums[left];
# //             int b = nums[right];

# //             int low = Math.min(a, b) + 1;
# //             int high = Math.max(a, b) + limit;
# //             int sum = a + b;

# //             diff[2] += 2;
# //             diff[2 * limit + 1] -= 2;

# //             diff[low] -= 1;
# //             diff[high + 1] += 1;

# //             diff[sum] -= 1;
# //             diff[sum + 1] += 1;

# //             left++;
# //             right--;
# //         }

# //         int ans = Integer.MAX_VALUE;
# //         int cur = 0;

# //         for (int i = 2; i <= 2 * limit; i++) {
# //             cur += diff[i];
# //             ans = Math.min(ans, cur);
# //         }

# //         return ans;
# //     }
# // }
# // ```

# // ---

# // # Trọng tâm khó nhất của bài

# // Điểm khó là hiểu:

# // ```text
# // [min(a,b)+1 , max(a,b)+limit]
# // ```

# // vì sao là vùng cần 1 move.

# // Đây là ý tưởng quan trọng nhất của bài.

# import java.util.*;

# public class b232 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int n = sc.nextInt();

#         int[] nums = new int[n];

#         // Nhập mảng
#         for (int i = 0; i < n; i++) {
#             nums[i] = sc.nextInt();
#         }

#         // Nhập limit
#         int limit = sc.nextInt();

#         int result = minMoves(nums, limit);

#         System.out.println(result);

#         sc.close();
#     }

#     public static int minMoves(int[] nums, int limit) {

#         // oneMove[i]:
#         // số cặp có thể đạt tổng i bằng <= 1 move
#         int[] oneMove = new int[2 * limit + 2];

#         // noMove:
#         // lưu số cặp đã có tổng = i (0 move)
#         Map<Integer, Integer> noMove = new HashMap<>();

#         int n = nums.length;

#         // Duyệt các cặp đối xứng
#         for (int i = 0; i < n / 2; i++) {

#             int j = n - 1 - i;

#             int a = nums[i];
#             int b = nums[j];

#             // Tổng hiện tại của cặp
#             int sum = a + b;

#             // Đếm số cặp cần 0 move
#             noMove.merge(sum, 1, Integer::sum);

#             /*
#              * Với cặp (a,b)
#              *
#              * Các target có thể đạt bằng 1 move nằm trong:
#              *
#              * [min(a,b)+1 , max(a,b)+limit]
#              */

#             int low = Math.min(a, b) + 1;
#             int high = Math.max(a, b) + limit;

#             // Difference Array
#             // cộng +1 cho đoạn [low, high]

#             oneMove[low]++;

#             oneMove[high + 1]--;
#         }

#         int ans = n;

#         // one:
#         // số cặp có thể đạt target hiện tại bằng <=1 move
#         int one = 0;

#         // target sum chạy từ 2 -> 2*limit
#         for (int target = 2; target <= 2 * limit; target++) {

#             // Prefix sum
#             one += oneMove[target];

#             int totalPairs = n / 2;

#             /*
#              * one cặp:
#              * tạm tính mỗi cặp cần 1 move
#              *
#              * totalPairs - one:
#              * cần 2 moves
#              *
#              * trừ đi số cặp thật ra cần 0 move
#              */

#             int moves = one
#                     + 2 * (totalPairs - one)
#                     - noMove.getOrDefault(target, 0);

#             ans = Math.min(ans, moves);
#         }

#         return ans;
#     }
# }