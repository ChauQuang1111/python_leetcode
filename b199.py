#  Number of Steps to Reduce a Number in Binary Representation to One(26/02/2026)
 
#  Ok Quang 👍 mình sẽ:

# 1. ✅ Giải thích lại thuật toán ngắn gọn
# 2. ✅ Thêm comment chi tiết trực tiếp vào code Python của bạn

# ---

# # 🎯 Ý tưởng thuật toán (nhắc lại nhanh)

# Ta duyệt từ **phải sang trái** (bit cuối → bit đầu).

# Tại mỗi bit:

# * Nếu bit + carry = 1 → số đang là **lẻ**

#   * Cần `+1` và `/2` → 2 bước
#   * Sinh carry = 1
# * Nếu bit + carry = 0 hoặc 2 → số **chẵn**

#   * Chỉ cần `/2` → 1 bước

# Sau vòng lặp, nếu còn carry = 1 → cộng thêm 1 bước cuối.



# 🧠 Code có chú thích chi tiết

class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0      # Tổng số bước
        carry = 0      # Biến mô phỏng nhớ khi cộng 1
        n = len(s) - 1 # Vị trí bit cuối cùng
        
        # Duyệt từ bit cuối (LSB) về bit thứ 2 (không xử lý bit đầu tiên)
        for i in range(n, 0, -1):
            
            # Giá trị thực tế của bit sau khi cộng carry
            # int(s[i]) chuyển '0' hoặc '1' thành số 0 hoặc 1
            if int(s[i]) + carry == 1:
                
                # Nếu bằng 1 -> số hiện tại là số lẻ
                # Theo đề:
                #   lẻ -> +1 (1 bước)
                #   sau đó /2 (1 bước)
                # Tổng = 2 bước
                steps += 2
                
                # Khi cộng 1 vào số lẻ luôn sinh carry
                carry = 1
            else:
                # Trường hợp:
                # int(s[i]) + carry = 0 hoặc 2
                # => số hiện tại là số chẵn
                # => chỉ cần /2
                steps += 1
        
        # Sau khi xử lý xong tất cả bit trừ bit đầu:
        # Nếu carry = 1 nghĩa là còn dư một lần cộng
        # Ví dụ: 111 -> sau xử lý thành 1000
        # Cần thêm 1 bước cuối
        return steps + carry


# 🔥 Ví dụ chạy tay nhanh: `"1101"` (13)


1101
# ```

# * i=3 → 1+0=1 → lẻ → +2 bước, carry=1
# * i=2 → 0+1=1 → lẻ → +2 bước, carry=1
# * i=1 → 1+1=2 → chẵn → +1 bước
# * Kết thúc → carry=1 → +1

# Tổng = 6

# ---

# # 🎯 Tóm lại bản chất

# Thuật toán không thực sự chia số.

# Nó chỉ:

# * Đếm số lần xử lý bit
# * Mô phỏng carry
# * Duyệt O(n)
# * Không convert sang số lớn



# Nếu bạn muốn mình:

# * Vẽ sơ đồ bit chạy từng vòng
# * Hoặc chứng minh vì sao luôn đúng với mọi chuỗi
# * Hoặc tối giản thành công thức đếm bit

# Nói mình biết 👌

 
# ---

# ## 📌 Yêu cầu bài toán

# Bạn được cho một **chuỗi nhị phân `s`** (chỉ gồm ký tự `'0'` và `'1'`), biểu diễn **một số nguyên dương**.

# 👉 Nhiệm vụ của bạn là:

# Tính **số bước tối thiểu** để giảm số đó về **1**, theo các quy tắc:

# ### 🔁 Quy tắc biến đổi:

# Trong mỗi bước:

# * Nếu số **chẵn** → chia cho 2
# * Nếu số **lẻ** → cộng thêm 1

# Lặp lại cho đến khi số trở thành **1**.

# Trả về **tổng số bước**.

# ---

# ## 📖 Ví dụ minh họa

# ### Ví dụ 1:

# ```
# Input: s = "1101"
# ```

# Số `"1101"` trong hệ nhị phân = 13 trong hệ thập phân.

# Ta thực hiện:

# | Bước | Số (thập phân) | Thao tác      |
# | ---- | -------------- | ------------- |
# | 1    | 13             | lẻ → +1 → 14  |
# | 2    | 14             | chẵn → /2 → 7 |
# | 3    | 7              | lẻ → +1 → 8   |
# | 4    | 8              | chẵn → /2 → 4 |
# | 5    | 4              | chẵn → /2 → 2 |
# | 6    | 2              | chẵn → /2 → 1 |

# 👉 Tổng cộng: **6 bước**

# Output: `6`

# ---

# ### Ví dụ 2:

# ```
# Input: s = "10"
# ```

# "10" = 2

# * 2 → chẵn → /2 → 1

# 👉 Output: `1`

# ---

# ## 🎯 Tóm lại bản chất bài toán

# Bạn đang:

# * Làm việc với **chuỗi nhị phân**
# * Không cần convert sang số nguyên lớn (vì có thể rất dài)
# * Mô phỏng quá trình:

#   * Lẻ → cộng 1
#   * Chẵn → chia 2
# * Đếm số bước đến khi còn lại `"1"`

# ---

# ## ⚠️ Lưu ý quan trọng

# * Chuỗi có thể rất dài (tới 500 ký tự)
# * Nếu convert sang kiểu số nguyên thông thường có thể bị overflow
# * Cách tối ưu là xử lý trực tiếp trên chuỗi hoặc dựa trên logic bit

# ---

# Nếu bạn muốn, mình có thể:

# * Giải thích tư duy giải bài
# * Phân tích cách làm O(n)
# * Viết code Java theo style bạn thích (Scanner, while loop 😄)

# Bạn đang làm bài này bằng ngôn ngữ gì?
