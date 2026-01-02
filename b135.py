# # // 961. N-Repeated Element in Size 2N Array(02/01/2026)
# # // **Bài 961. N-Repeated Element in Size 2N Array – Giải thích đề bài (Tiếng Việt)**
# Dưới đây là **code Python có chú thích đầy đủ** + **giải thích thuật toán rõ ràng**, đúng tinh thần LeetCode 👇

# ---

# ## ✅ Code Python (có chú thích)

# ```python
from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # Tập hợp dùng để lưu các phần tử đã xuất hiện
        seen = set()

        # Duyệt từng phần tử trong mảng nums
        for x in nums:
            # Nếu x đã tồn tại trong set
            # → đây là phần tử bị lặp (xuất hiện N lần)
            if x in seen:
                return x

            # Nếu chưa tồn tại thì thêm x vào set
            seen.add(x)

        # Theo đề bài, dòng này không bao giờ được chạy tới
        return -1


## 🎯 Mục tiêu thuật toán

# Tìm **phần tử xuất hiện đúng N lần** trong mảng có kích thước `2N`.

# ---

# ## 🧠 Ý tưởng chính

# 👉 **Dùng `set` để phát hiện phần tử lặp đầu tiên**

# * `set` **không chứa phần tử trùng nhau**
# * Khi gặp một số **đã tồn tại trong set**
#   → chắc chắn đó là **số xuất hiện N lần**

# ---

## 🔍 Giải thích từng bước

# Giả sử:

# ```text
# nums = [2, 1, 2, 5, 3, 2]
# ```

# | x | seen trước | x in seen? | seen sau | Kết luận     |
# | - | ---------- | ---------- | -------- | ------------ |
# | 2 | {}         | ❌          | {2}      | tiếp         |
# | 1 | {2}        | ❌          | {2,1}    | tiếp         |
# | 2 | {2,1}      | ✅          | —        | **return 2** |

# ---

## ⏱️ Độ phức tạp

# | Loại      | Độ phức tạp |
# | --------- | ----------- |
# | Thời gian | **O(n)**    |
# | Bộ nhớ    | **O(n)**    |

# ---

# ## ✅ Vì sao thuật toán này đúng?

# * Chỉ có **1 phần tử bị lặp nhiều lần**
# * Phần tử đó **chắc chắn xuất hiện lại**
# * Ta **không cần đếm đủ N lần**
# * Chỉ cần gặp **lần lặp đầu tiên là đủ**

# ---

# ## 🧠 Mẹo nhớ nhanh khi đi thi

# > **“Số nào xuất hiện lại đầu tiên → chính là đáp án”**

# ---

# Nếu bạn muốn:

# * 🚀 Cách giải **O(1) bộ nhớ**
# * 🔥 Cách giải **không dùng set**
# * ✍️ So sánh Python vs Java

# 👉 cứ nói, mình giải tiếp cho bạn 👍

# import java.util.*;

# public class b136 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int n = sc.nextInt();

#         int[] nums = new int[n];

#         // Nhập các phần tử của mảng
#         for (int i = 0; i < n; i++) {
#             nums[i] = sc.nextInt();
#         }

#         // Gọi hàm và in kết quả
#         System.out.println(repeatedNTimes(nums));

#         sc.close();
#     }

#     // Hàm tìm phần tử xuất hiện N lần
#     public static int repeatedNTimes(int[] nums) {
#         // HashSet dùng để lưu các phần tử đã xuất hiện
#         HashSet<Integer> set = new HashSet<>();

#         // Duyệt từng phần tử trong mảng
#         for (int x : nums) {
#             /*
#              * set.add(x):
#              * - trả về true nếu x chưa tồn tại
#              * - trả về false nếu x đã tồn tại (bị lặp)
#              */
#             if (!set.add(x)) {
#                 // Khi gặp phần tử lặp đầu tiên → chính là số xuất hiện N lần
#                 return x;
#             }
#         }

#         // Theo đề bài, dòng này không bao giờ chạy
#         return -1;
#     }

# }

# // ---

# // ### 📌 Nội dung đề bài

# // Bạn được cho một **mảng số nguyên `nums`** có **độ dài = 2N**.

# // Trong mảng này:

# // * Có **N + 1 số khác nhau**
# // * Trong đó:

# // * **1 số xuất hiện đúng N lần**
# // * **N số còn lại mỗi số chỉ xuất hiện 1 lần**

# // 👉 **Nhiệm vụ:**
# // Tìm và **trả về số xuất hiện N lần** đó.

# // ---

# // ### 🔍 Hiểu đơn giản

# // * Tổng số phần tử: `2N`
# // * Có đúng **1 phần tử bị lặp rất nhiều (N lần)**
# // * Các phần tử khác **không bị lặp**

# // ---

# // ### 🧠 Ví dụ minh họa

# // #### Ví dụ 1:

# // ```
# // nums = [1,2,3,3]
# // ```

# // * Độ dài mảng = 4 → `2N = 4` → `N = 2`
# // * Số **3 xuất hiện 2 lần**
# // * Các số khác (1, 2) chỉ xuất hiện 1 lần

# // ✅ **Kết quả:** `3`

# // ---

# // #### Ví dụ 2:

# // ```
# // nums = [2,1,2,5,3,2]
# // ```

# // * Độ dài mảng = 6 → `N = 3`
# // * Số **2 xuất hiện 3 lần**
# // * Các số khác chỉ xuất hiện 1 lần

# // ✅ **Kết quả:** `2`

# // ---

# // ### ⚠️ Điều quan trọng cần nhớ

# // * **Luôn chỉ có 1 đáp án đúng**
# // * Không cần xử lý trường hợp đặc biệt
# // * Không cần sắp xếp mảng (có thể làm nhanh hơn)

# // ---

# // ### 💡 Gợi ý tư duy (chưa phải code)

# // * Đếm số lần xuất hiện của mỗi phần tử
# // * Hoặc lợi dụng tính chất: vì số lặp **xuất hiện rất nhiều**, nên có thể phát
# // hiện sớm khi duyệt mảng

# // Nếu bạn muốn:

# // * ✅ Giải bằng **Java / Python**
# // * ✅ So sánh **nhiều cách giải (O(n), O(1))**
# // * ✅ Giải thích theo kiểu **dễ nhớ để đi thi LeetCode**

# // 👉 cứ nói mình sẽ làm tiếp nhé 👍
# // Mình giải thích **thuật toán** của đoạn code này **từng bước, đúng tư duy
# // LeetCode**, ngắn gọn và dễ nhớ nhé 👇

# // ---

# // ## 🎯 Mục tiêu thuật toán

# // Tìm **phần tử xuất hiện N lần** trong mảng `nums` có độ dài `2N`.

# // ---

# // ## 🧠 Ý tưởng chính

# // 👉 **Dùng HashSet để phát hiện phần tử bị lặp đầu tiên**

# // * `HashSet` **không cho phép trùng lặp**
# // * Khi thêm một phần tử đã tồn tại → biết ngay nó là số bị lặp

# // ---

# // ## 📌 Phân tích code chi tiết

# // ```java
# // java.util.HashSet<Integer> set = new java.util.HashSet<>();
# // ```

# // * Tạo một `HashSet` để lưu các số **đã xuất hiện**

# // ---

# // ```java
# // for (int x : nums) {
# // ```

# // * Duyệt từng phần tử `x` trong mảng `nums`

# // ---

# // ```java
# // if (!set.add(x)) return x;
# // ```

# // 🔑 **Dòng quan trọng nhất**

# // * `set.add(x)`:

# // * Trả về `true` → `x` chưa có trong set → thêm thành công
# // * Trả về `false` → `x` đã tồn tại → **bị lặp**

# // 👉 Khi `add(x)` trả về `false`
# // → đây chính là **số xuất hiện N lần**
# // → trả về ngay `x`

# // ---

# // ```java
# // return -1;
# // ```

# // * Dòng này chỉ để **đảm bảo code compile**
# // * Theo đề bài **không bao giờ chạy tới đây**

# // ---

# // ## 🔍 Ví dụ chạy tay

# // ### Input:

# // ```text
# // nums = [2,1,2,5,3,2]
# // ```

# // | x | set trước | add(x) | set sau | Kết luận |
# // | - | --------- | ------- | ------- | ------------ |
# // | 2 | {} | true | {2} | tiếp |
# // | 1 | {2} | true | {2,1} | tiếp |
# // | 2 | {2,1} | ❌ false | — | **return 2** |

# // ---

# // ## ⏱️ Độ phức tạp

# // | Loại | Giá trị |
# // | ----- | -------- |
# // | Time | **O(n)** |
# // | Space | **O(n)** |

# // ---

# // ## ✅ Vì sao thuật toán này đúng?

# // * Chỉ có **1 số bị lặp nhiều lần**
# // * Số đó **chắc chắn sẽ xuất hiện lại**
# // * `HashSet` phát hiện trùng **ngay lần gặp thứ 2**
# // * Không cần đếm đủ N lần

# // ---

# // ## 🧠 Cách nhớ nhanh khi đi thi

# // > **“Gặp số nào mà HashSet không thêm được → chính là đáp án”**

# // ---

# // Nếu bạn muốn:

# // * 🚀 Thuật toán **O(1) bộ nhớ**
# // * 🔥 Giải bằng **so sánh 3 phần tử liên tiếp**
# // * 🧪 So sánh các cách giải để chọn nhanh nhất khi thi

# // 👉 nói mình biết, mình giải tiếp cho bạn 👍
