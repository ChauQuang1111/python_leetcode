# # Check if Binary String Has at Most One Segment of One”(06/03/2026)

# Bài **Check if Binary String Has at Most One Segment of Ones** yêu cầu:

# > Kiểm tra xem chuỗi nhị phân `s` có **tối đa 1 đoạn các số `1` liên tiếp** hay không.

# Ví dụ:

# * `"111000"` → chỉ **1 đoạn `1`** → ✅ True
# * `"110011"` → có **2 đoạn `1`** → ❌ False

# ---

# # Ý tưởng thuật toán

# Nếu chuỗi chỉ có **1 đoạn `1`**, thì dạng của nó sẽ giống:

# ```
# 000111000
# ```

# hoặc

# ```
# 111000
# ```

# hoặc

# ```
# 000111
# ```

# Tức là:

# ```
# 0...0 111...1 0...0
# ```

# Điều **không được xảy ra** là:

# ```
# 111000111
# ```

# vì có **2 đoạn `1`**.

# ---

# ## Quan sát quan trọng

# Nếu chuỗi có **2 đoạn `1`**, chắc chắn sẽ xuất hiện:

# ```
# 01
# ```

# giữa hai đoạn.

# Ví dụ:

# ```
# 111000111
#    ↑
#    01 xuất hiện
# ```

# Sau khi đã gặp `"01"` nghĩa là:

# * ta đã **kết thúc đoạn `1` đầu tiên**
# * nếu sau đó **lại có `1`** → tức là **đoạn `1` thứ hai**

# Nhưng LeetCode trick ở đây là:

# 👉 Trong chuỗi hợp lệ **không được có `"01"` giữa các đoạn `1`**.

# Vì nếu `"01"` xuất hiện rồi sau đó lại có `1` → tức có 2 segment.

# Do đó ta chỉ cần kiểm tra:

# ```
# "01" not in s
# ```

# ---

# # Code có chú thích

# ```python
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
        # Nếu trong chuỗi có substring "01"
        # nghĩa là đã có đoạn 1 kết thúc (1 -> 0)
        # và nếu sau đó còn xuất hiện 1 nữa thì sẽ tạo ra segment thứ hai
        
        # Tuy nhiên Python chỉ cần kiểm tra "01"
        # vì chuỗi hợp lệ sẽ có dạng:
        # 111...000... (tức là chỉ chuyển từ 1 sang 0 một lần)
        
        # Nếu có "01" rồi sau đó lại có 1 -> sẽ có thêm "01"
        # nên chỉ cần kiểm tra sự tồn tại của "01"
        
        return "01" not in s


# Ví dụ chạy

### Case 1

# ```
# s = "111000"
# ```

# Chuỗi có `"10"` nhưng **không có `"01"`**

# ```
# True
# ```

# ---

# ### Case 2

# ```
# s = "110011"
# ```

# Chuỗi có:

# ```
# 11 00 11
#    ↑
#    01 xuất hiện
# ```

# ```
# False
# ```

# ---

# # Độ phức tạp

# * **Time complexity:** `O(n)`
# * **Space complexity:** `O(1)`

# ---

# ✅ Nếu bạn muốn, mình có thể giải thích thêm **tại sao `"01"` là trick rất hay trong bài này (cách tư duy interview của Google/Meta)** — vì nhiều người ban đầu sẽ viết **code dài hơn nhiều**.


# ---

# ## 1. Binary string là gì?

# **Binary string** là chuỗi chỉ gồm **'0' và '1'**.

# Ví dụ:

# * `"1001"`
# * `"111000"`
# * `"010101"`

# ---

# ## 2. “Segment of ones” là gì?

# **Segment of ones** = **một đoạn các số 1 liên tiếp**.

# Ví dụ:

# | Chuỗi    | Các segment của '1'      |
# | -------- | ------------------------ |
# | `111000` | `111` → 1 segment        |
# | `1001`   | `1` và `1` → 2 segment   |
# | `110011` | `11` và `11` → 2 segment |
# | `000`    | 0 segment                |

# ---

# ## 3. “At most one segment of ones” nghĩa là gì?

# **At most one** = **tối đa 1**

# → Chuỗi **chỉ được có 0 hoặc 1 đoạn '1' liên tiếp**

# ---

# ## 4. Ví dụ

# ### Ví dụ 1

# Input:

# ```
# s = "1001"
# ```

# Phân tích:

# ```
# 1 000 1
# ```

# Có **2 đoạn '1'**

# ❌ **False**

# ---

# ### Ví dụ 2

# Input:

# ```
# s = "110"
# ```

# Phân tích:

# ```
# 11 0
# ```

# Có **1 đoạn '1'**

# ✅ **True**

# ---

# ### Ví dụ 3

# Input:

# ```
# s = "1"
# ```

# Có **1 đoạn**

# ✅ **True**

# ---

# ### Ví dụ 4

# Input:

# ```
# s = "0000"
# ```

# Không có đoạn `1`

# ✅ **True**

# ---

# ## 5. Ý tưởng kiểm tra

# Ta chỉ cần kiểm tra:

# > Có xuất hiện **pattern `"01"` rồi sau đó lại có `"1"`** không.

# Hoặc cách dễ hiểu hơn:

# Nếu chuỗi có **"01" rồi lại "10"** → nghĩa là **đã bắt đầu đoạn 1 thứ hai**.

# ---

# ## 6. Cách nghĩ đơn giản nhất

# Nếu chuỗi chứa **"01" rồi sau đó lại có "1"**
# → có **2 đoạn 1**

# Ví dụ:

# ```
# 110011
#    ↑
# đã kết thúc đoạn 1
# sau đó lại có 1
# ```

# ---

# ## 7. Ví dụ trực quan

# ```
# 11110000   ✅ 1 segment
# 00001111   ✅ 1 segment
# 11100111   ❌ 2 segments
# 10000001   ❌ 2 segments
# ```

# ---

# ✅ **Tóm lại đề bài yêu cầu:**

# > Kiểm tra xem chuỗi nhị phân có **tối đa 1 đoạn các số 1 liên tiếp** hay không.

# ---

# Nếu bạn muốn, mình có thể giải thích thêm:

# * **cách giải O(n) đơn giản nhất**
# * **1 dòng code Java / Python / C++ để pass LeetCode**.
