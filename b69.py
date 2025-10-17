# 3003. Maximize the Number of Partitions After Operations(17/10/2025)
# Dưới đây là **giải thích chi tiết** và **code có chú thích từng dòng** cho bài **LeetCode 3003 — Maximize the Number of Partitions After Operations** 👇

# ---

# ### 🎯 **Yêu cầu đề bài tóm tắt**

# Cho một chuỗi ký tự `s` (gồm chữ thường `a-z`) và một số nguyên `k`.
# Ta muốn chia chuỗi thành **nhiều đoạn nhất có thể**, sao cho **mỗi đoạn có ≤ k ký tự khác nhau**.

# 👉 Tuy nhiên, ta **được phép thay đổi đúng 1 ký tự bất kỳ trong chuỗi `s`** thành bất kỳ chữ cái nào khác.
# → Hỏi: sau khi thay đổi ký tự đó tối ưu nhất, có thể chia được **nhiều đoạn nhất là bao nhiêu**?

# ---

# ### 🧩 **Ý tưởng chính của thuật toán**

# 1. Mỗi ký tự được biểu diễn bằng một **bitmask** — bit thứ `i` thể hiện ký tự `'a' + i` có xuất hiện hay không.
#    → Giúp kiểm tra số ký tự khác nhau bằng `.bit_count()`.

# 2. Duyệt qua chuỗi, chia thành các nhóm (partition) sao cho mỗi nhóm có ≤ `k` ký tự khác nhau.

#    * Làm việc này **từ trái sang phải (prefix)**.
#    * Và làm lại **từ phải sang trái (suffix)**.

# 3. Sau đó, thử “thay đổi 1 ký tự” ở **mỗi vị trí `i`**, rồi ghép **prefix trái + suffix phải** quanh vị trí đó, xem:

#    * Nếu thay đổi giúp gộp hoặc tách nhóm → số lượng nhóm có thể tăng.

# ---

# ### 🧠 **Chi tiết code có chú thích**
from typing import List
class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)

        # ✅ Mỗi ký tự được chuyển thành bitmask (bit 0 -> 'a', bit 25 -> 'z')
        # Ví dụ: 'a' -> 1 (000001), 'b' -> 2 (000010), ...
        set_bits = [1 << (ord(letter) - ord("a")) for letter in s]

        # -----------------------------
        # Hàm tạo prefix hoặc suffix partition
        # -----------------------------
        def make_prefix(set_bits: List[int]):
            prefix = [0]          # số lượng nhóm trước vị trí i
            prefix_mask = [0]     # mask chứa các ký tự của nhóm hiện tại
            mask = 0
            groups = 0
            for current_index_set_bits in set_bits:
                # thêm ký tự hiện tại vào nhóm
                mask |= current_index_set_bits
                # nếu vượt quá k ký tự khác nhau, phải tách nhóm
                if mask.bit_count() > k:
                    groups += 1
                    mask = current_index_set_bits  # nhóm mới bắt đầu
                prefix.append(groups)
                prefix_mask.append(mask)
            return prefix, prefix_mask

        # ✅ prefix từ trái sang phải
        prefix, prefix_mask = make_prefix(set_bits)
        # ✅ suffix từ phải sang trái (đảo ngược mảng)
        suffix, suffix_mask = make_prefix(set_bits[::-1])

        max_partitions_after_operations = 0

        # -----------------------------
        # Thử thay đổi ký tự tại mỗi vị trí index
        # -----------------------------
        for index in range(n):
            # Tổng số nhóm ở 2 phía (trái + phải)
            candidate = prefix[index] + suffix[-(index + 2)]

            # Hợp ký tự của 2 phía
            mask = prefix_mask[index] | suffix_mask[-(index + 2)]

            # Giờ xét xem thay đổi ký tự tại vị trí index giúp được mấy nhóm:
            if min(mask.bit_count() + 1, 26) <= k:
                # ✅ Nếu sau khi đổi, tổng ký tự khác nhau <= k
                # => có thể thêm 1 nhóm mới
                candidate += 1
            elif (
                prefix_mask[index].bit_count() == k
                and suffix_mask[-(index + 2)].bit_count() == k
                and mask.bit_count() < 26
            ):
                # ✅ Nếu cả 2 phía đều đủ k ký tự khác nhau
                # nhưng vẫn còn chỗ (tổng < 26) → có thể thêm 3 nhóm
                candidate += 3
            else:
                # ✅ Ngược lại, chỉ thêm 2 nhóm tối đa
                candidate += 2

            # Cập nhật kết quả lớn nhất
            max_partitions_after_operations = max(
                max_partitions_after_operations, candidate
            )

        return max_partitions_after_operations


### 🔍 **Tóm tắt lại luồng hoạt động**

# 1. **Biểu diễn** từng ký tự bằng bitmask.
# 2. **Tính prefix & suffix**: chia chuỗi thành nhóm hợp lệ ≤ `k` ký tự khác nhau.
# 3. **Thử đổi từng ký tự** và kiểm tra xem có thể tăng được số nhóm không.
# 4. **Chọn kết quả lớn nhất** sau khi duyệt hết.

# ---

# Nếu bạn muốn, mình có thể vẽ **sơ đồ trực quan** để thấy rõ cách “chia nhóm trước/sau khi đổi ký tự” — bạn có muốn mình vẽ không?

# ---

# ## 📝 Đề bài:

# Bạn được cho:

# * Một **chuỗi kí tự `s`** (chỉ gồm các chữ cái thường)
# * Một số nguyên `k`

# Bạn có thể thực hiện các phép sau:

# 1. Trước khi làm gì khác, **bạn được phép đổi tối đa 1 kí tự** trong `s` thành một kí tự khác nào đó (cả chữ cái thường).
# 2. Sau đó, bạn thực hiện các bước phân đoạn (`partitioning operations`) lặp lại cho đến khi `s` bị rỗng:

#    * Mỗi lần, bạn chọn **prefix dài nhất** của `s` mà prefix đó có **tối đa `k` kí tự phân biệt** (distinct characters).
#    * Xoá (delete) prefix đó khỏi đầu chuỗi `s`.
#    * Tăng số phân đoạn lên 1.
#    * Phần còn lại của chuỗi giữ nguyên thứ tự ban đầu.

# Trả về **số phân đoạn tối đa** có thể được tạo ra, nếu bạn chọn cách **thay đổi tối ưu nhất** (hoặc không thay đổi nếu tốt nhất).

# ---

# ## 🔍 Ví dụ:

# * Ví dụ 1:

#   ```
#   s = "accca", k = 2
#   ```

#   Bạn có thể thay `s[2]` (ký tự thứ 3, ‘c’) thành ‘b’. Khi đó `s` trở thành `"acbca"`.
#   Thực hiện phân đoạn:

#   1. Prefix có ≤2 kí tự phân biệt → `"acbca"` (toàn chuỗi), XOÁ hết → 1 phân đoạn
#      Có thể làm theo các prefix nhỏ hơn nếu muốn theo greedy lâu hơn? Có thể chọn `"ac"`, xoá rồi `"bc"`, rồi `"a"`, tổng là 3 phân đoạn.

#   Kết quả tối đa = **3**.

# * Ví dụ 2:

#   ```
#   s = "aabaab", k = 3
#   ```

#   Vì `k = 3` quá lớn so với số kí tự phân biệt có thể có, cho dù đổi kí tự hay không, bạn vẫn có thể cho prefix toàn bộ chuỗi mỗi lần, nên số phân đoạn = **1**.

# ---

# ## 💡 Ý tưởng/chiến lược

# Để tối đa hoá số phân đoạn, ta muốn làm sao để khi mình cứ lấy prefix “lớn nhất có ≤ k kí tự phân biệt” thì prefix đó **không quá lớn**, vì những prefix nhỏ hơn = xóa nhiều lần hơn = nhiều phân đoạn hơn.

# Việc được phép thay đổi **1 kí tự** cho phép bạn:

# * Thay vào một vị trí thích hợp để làm giảm sự đa dạng kí tự trong phần đầu chuỗi, để các prefix nhỏ hơn phải dừng lại từ sớm hơn → ra được nhiều phân đoạn hơn.

# Chiến lược:

# * Giả sử bạn không thay đổi gì, thì quá trình phân đoạn là **greedy**: mỗi lần lấy prefix dài nhất có ≤ k distinct, xoá, tiếp tục với phần còn lại.
# * Xem xét thay đổi mỗi vị trí trong s (hoặc khoảng nào đó) thành một ký tự có ích để làm cho phân đoạn có thể nhiều hơn. Thường bạn muốn gây ảnh hưởng mạnh cho các prefix đầu, vì đó là những lần mà phân đoạn có thể tăng nhiều nếu prefix sớm bị “nghẽn” bởi số lượng kí tự phân biệt vượt k.

# ---

# ## ✅ Tóm tắt:

# * Chuỗi `s`, số `k`
# * Trước khi phân đoạn, bạn được quyền thay đổi **tối đa 1 kí tự**
# * Sau đó thực hiện: mỗi lần chọn prefix dài nhất có ≤ k ký tự phân biệt, xoá prefix đó, tăng count phân đoạn
# * Mục tiêu: thay đổi đâu hoặc không thay đổi sao cho số phân đoạn ra được là **lớn nhất**

# ---

# Nếu bạn muốn, mình có thể giải rõ một ví dụ từng bước (tức là chọn vị trí thay đổi + bước phân đoạn) và sau đó viết code minh hoạ bằng Java hay Python với chú thích rõ ràng?
# Tóm gọn lại cho bạn — đây là **yêu cầu chính của đề bài LeetCode 3003 – “Maximize the Number of Partitions After Operations”** 👇

# ---

# ## 🧩 **Yêu cầu đề bài:**

# > Cho một chuỗi ký tự `s` và một số nguyên `k`, bạn được phép **thay đổi tối đa 1 ký tự trong chuỗi**.
# > Sau đó, hãy chia chuỗi `s` thành **nhiều phần nhất có thể** (partition count tối đa), sao cho **mỗi phần** có **tối đa `k` ký tự phân biệt (distinct characters)**.

# 👉 **Trả về số lượng phần tối đa** mà bạn có thể tạo ra sau khi thực hiện phép thay đổi tối ưu (hoặc không thay đổi nếu không cần).

# ---

# ## 🔹 Cách chia chuỗi:

# * Bắt đầu từ đầu chuỗi.
# * Mỗi lần chọn **prefix dài nhất** (đoạn đầu) mà **có ≤ k ký tự khác nhau**.
# * Xoá đoạn đó khỏi chuỗi và tiếp tục làm với phần còn lại.
# * Mỗi lần như vậy tính là **một partition (một phần)**.

# ---

# ## 🔹 Mục tiêu:

# > Tìm số partition **nhiều nhất có thể** nếu bạn được phép thay đổi **tối đa 1 ký tự** trong chuỗi.

# ---

# ## 🔹 Ví dụ minh họa:

# ### 🧠 Ví dụ 1:

# ```
# s = "accca", k = 2
# ```

# Không đổi gì:

# * Phân đoạn đầu tiên có thể là `"acc"` (vì chỉ có `a, c`)
# * Sau khi xóa `"acc"`, còn lại `"ca"` → thêm 1 phân đoạn nữa
#   → Tổng = 2 partitions.

# Nếu đổi ký tự thứ 3 (`c`) thành `b`, ta được `"acbca"`
# → Phân đoạn 1: `"ac"` (a, c)
# → Phân đoạn 2: `"bc"` (b, c)
# → Phân đoạn 3: `"a"`
# → Tổng = **3 partitions** ✅ (nhiều hơn)

# ---

# ### ✅ Kết luận:

# **Đề yêu cầu:**
# Tìm **số partition tối đa** có thể đạt được từ chuỗi `s`
# 👉 khi được phép **thay đổi tối đa 1 ký tự**
# 👉 và mỗi partition có **≤ k ký tự phân biệt**.

# ---

# Nếu bạn muốn, mình có thể minh họa quy trình chia cụ thể cho từng bước (với bảng ký tự và đếm distinct) để bạn thấy rõ cách tính partition. Bạn muốn mình minh họa ví dụ `"accca", k=2"` từng bước không?
