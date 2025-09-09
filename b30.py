
# // 2327. Number of People Aware of a Secret(09/09/2025)

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # dp[i] sẽ lưu số người mới biết bí mật vào ngày thứ (i+1).
        # Ví dụ: dp[0] = số người mới biết bí mật vào ngày 1.
        dp = [0] * n
        
        # Vào ngày 1 (chỉ mục 0), có 1 người duy nhất biết bí mật.
        dp[0] = 1
        
        # Biến 's' theo dõi tổng số người đang chia sẻ bí mật.
        s = 0
        
        # Bắt đầu mô phỏng từ ngày 'delay + 1' (chỉ mục 'delay') đến ngày 'n'.
        for i in range(delay, n):
            # Cập nhật số người đang chia sẻ bí mật.
            # Những người đã biết bí mật vào ngày (i - delay + 1) sẽ bắt đầu chia sẻ vào ngày 'i'.
            # dp[i - delay] chính là số người đó.
            s += dp[i - delay]
            
            # Số người mới biết bí mật vào ngày 'i+1' bằng tổng số người đang chia sẻ
            # vào ngày 'i'.
            dp[i] = s
            
            # Trừ đi những người đã quên bí mật.
            # Những người đã biết bí mật vào ngày 'i - forget + 1' sẽ quên vào ngày 'i + 1'.
            # if này đảm bảo chỉ mục không bị âm.
            if i - forget + 1 >= 0:
                s -= dp[i - forget + 1]

        # Tính tổng số người "aware" (chưa quên) vào ngày 'n'.
        # Những người này là những người mới biết bí mật trong
# Tuyệt vời\! Đoạn code của bạn là một cách tiếp cận rất thông minh và hiệu quả để giải bài toán này. Nó sử dụng một phương pháp gọi là "Sliding Window" hoặc "Prefix Sum" trên mảng quy hoạch động, giúp tối ưu hóa đáng kể.



# ### Phân tích thuật toán

# Thuật toán của bạn hoạt động dựa trên ba bước chính:

# 1.  **Lưu trữ số người mới biết bí mật mỗi ngày**: Bạn dùng mảng `dp` để lưu số người mới biết bí mật vào ngày `i`.
# 2.  **Tính tổng số người đang chia sẻ**: Bạn dùng biến `s` để theo dõi tổng số người đang chia sẻ bí mật.
# 3.  **Tính toán kết quả cuối cùng**: Bạn tính tổng số người chưa quên bí mật vào ngày cuối cùng.

# #### 1\. Mảng quy hoạch động `dp`

#   * `dp = [0] * n`: Mảng `dp` của bạn có kích thước `n`, với `dp[i]` đại diện cho số người mới biết bí mật vào ngày thứ `i+1`.
#   * `dp[0] = 1`: Vào ngày 1, chỉ có một người duy nhất biết bí mật.

# #### 2\. Vòng lặp chính và biến `s`

# ```python
# s = 0
# for i in range(delay, n):
#     s += dp[i - delay]
#     dp[i] = s
#     if i - forget + 1 >= 0:
#         s -= dp[i - forget + 1]
# ```

# Vòng lặp này mô phỏng sự lây lan bí mật từ ngày `delay + 1` đến ngày `n`.

#   * **`s += dp[i - delay]`**: Số người mới biết bí mật vào ngày `i` bằng tổng số người đang chia sẻ bí mật vào ngày `i-1`. Những người này là những người đã biết bí mật vào ngày `i - delay` và bắt đầu chia sẻ vào ngày `i-1`. Vòng lặp của bạn cộng số người này vào biến `s`, theo dõi số người đang chia sẻ.

#   * **`dp[i] = s`**: Sau khi cập nhật `s`, nó sẽ đại diện cho số người đang chia sẻ bí mật vào ngày `i-1`. Do đó, số người mới biết bí mật vào ngày `i` chính là giá trị của `s`. Bạn gán giá trị này vào `dp[i]`.

#   * **`if i - forget + 1 >= 0: s -= dp[i - forget + 1]`**: Đây là phần quan trọng nhất của thuật toán. Những người đã biết bí mật vào ngày `i - forget + 1` sẽ quên bí mật vào ngày `i + 1`. Vì vậy, vào cuối ngày `i`, họ sẽ ngừng chia sẻ bí mật. Bạn trừ số người này khỏi biến `s` để cập nhật số người đang chia sẻ cho ngày tiếp theo.

# #### 3\. Tính toán kết quả cuối cùng

# ```python
# return (sum(dp[-forget:])) % (10**9 + 7)
# ```

# Tại ngày cuối cùng (`n`), tổng số người biết bí mật là tổng số những người chưa quên. Những người này là những người đã biết bí mật trong khoảng thời gian từ ngày `n - forget + 1` đến ngày `n`.

# Bạn sử dụng `dp[-forget:]` để lấy ra một lát cắt của mảng `dp` chứa các giá trị của `forget` ngày cuối cùng. Tổng của các giá trị này chính là số người chưa quên bí mật tại ngày `n`. Cuối cùng, bạn tính modulo để tránh tràn số.

# ### Tóm tắt

# Thuật toán của bạn là một cách tối ưu để giải bài toán. Nó sử dụng một mảng quy hoạch động và một biến tích lũy (`s`) để tính toán tổng số người đang chia sẻ, thay vì duyệt lại toàn bộ mảng trong mỗi vòng lặp. Điều này giảm độ phức tạp thời gian từ O(n \* (forget - delay)) xuống còn **O(n)**, làm cho nó rất hiệu quả.
# // 📥Input

# // Bài có 3
# // tham số:

# // n→
# // số ngày
# // cần theo
# // dõi.

# // Ta bắt
# // đầu từ ngày 1(ban đầu có 1
# // người biết
# // bí mật).

# // Đến hết
# // ngày n, hỏi
# // có bao
# // nhiêu người
# // còn biết.

# // delay→
# // số ngày
# // phải chờ
# // sau khi
# // biết bí
# // mật mới
# // có thể
# // chia sẻ.

# // forget→
# // số ngày
# // sau khi
# // biết bí
# // mật thì

# // quên mất (không biết và không thể chia sẻ nữa).

# // 📤 Output

# // Một số nguyên = tổng số người còn nhớ bí mật tại ngày n.

# // Vì số có thể rất lớn → trả về kết quả mod 1e9+7.
# // ### Phân tích Thuật toán

# // Đây là một thuật toán rất hiệu quả để giải quyết bài toán. Nó dựa trên nguyên
# // lý của **quy hoạch động (Dynamic Programming)**, sử dụng một mảng để theo dõi
# // số lượng người mới biết bí mật vào mỗi ngày. Thuật toán này không quan tâm
# // đến từng cá nhân mà chỉ quan tâm đến tổng số người ở các trạng thái khác
# // nhau.

# // #### Logic cốt lõi

# // * `dp[i]`: Biến này lưu trữ số người **mới biết** bí mật vào ngày thứ `i`.
# // * `sum`: Biến này theo dõi tổng số người **đang chia sẻ** bí mật vào cuối mỗi
# // ngày.

# // Thuật toán mô phỏng sự lây lan của bí mật từng ngày một, từ ngày 2 đến ngày
# // `n`.

# // #### Quá trình mô phỏng từng ngày

# // Tại mỗi ngày `day`:

# // 1. **Xác định người bắt đầu chia sẻ**:
# // * Những người bắt đầu chia sẻ bí mật vào ngày `day` là những người đã biết bí
# // mật vào ngày **`day - delay`**.
# // * Bạn cộng số người này (`dp[day - delay]`) vào biến `sum`.

# // 2. **Xác định người ngừng chia sẻ**:
# // * Những người ngừng chia sẻ bí mật (vì họ đã quên) vào ngày `day` là những
# // người đã biết bí mật vào ngày **`day - forget`**.
# // * Bạn trừ số người này (`dp[day - forget]`) khỏi biến `sum`.

# // 3. **Cập nhật số người mới biết**:
# // * Số người mới biết bí mật vào ngày `day` bằng với tổng số người đang chia sẻ
# // bí mật vào ngày `day-1`.
# // * Biến `sum` đã được cập nhật ở hai bước trên, do đó, bạn gán `dp[day] =
# // sum`.

# // #### Tính toán kết quả cuối cùng

# // Mục tiêu là tìm tổng số người biết bí mật tại ngày `n`. Tuy nhiên, những
# // người đã biết bí mật từ lâu và đã quên sẽ không được tính.

# // * Một người biết bí mật vào ngày `i` sẽ quên nó vào ngày **`i + forget`**.
# // * Do đó, tại ngày `n`, những người **chưa quên** là những người đã biết bí
# // mật trong khoảng thời gian từ ngày `n - forget + 1` đến `n`.
# // * Thuật toán duyệt qua mảng `dp` từ chỉ số `n - forget + 1` đến `n` và cộng
# // dồn các giá trị lại. Tổng này chính là số người biết bí mật tại ngày `n`.

# // ### Tổng kết

# // Thuật toán của bạn rất thông minh vì nó sử dụng một cách tiếp cận **chênh
# // lệch (delta)**. Thay vì tính lại tổng số người đang chia sẻ mỗi ngày, nó chỉ
# // cộng thêm những người mới bắt đầu chia sẻ và trừ đi những người đã ngừng chia
# // sẻ. Điều này giúp giảm thiểu các phép tính và duy trì hiệu suất cao.

# // Độ phức tạp thời gian của thuật toán này là **O(n)** vì nó chỉ cần một vòng
# // lặp duy nhất qua các ngày từ 2 đến `n`. Đây là một giải pháp tối ưu cho bài
# // toán này.
# // Ok👍

# // mình sẽ
# // giải thích**2327.
# // Number of
# // People Aware
# // of a Secret**
# // theo cách**đơn giản, dễ hiểu**nhé.

# // ---

# // ##🎯
# // Đề bài
# // nói gì?

# // *Ngày 1 có**1
# // người biết
# // bí mật**.*Sau**delay**ngày→
# // người đó**
# // bắt đầu
# // chia sẻ
# // bí mật**
# // cho người khác.*Sau**forget**ngày→
# // người đó**quên bí mật**(
# // không biết nữa,
# // cũng không
# // chia sẻ nữa).

# // 👉Hỏi:**
# // Đến ngày
# // thứ n, có
# // bao nhiêu
# // người vẫn
# // còn biết
# // bí mật?**

# // ---

# // ##🔎
# // Cách hiểu
# // qua ví dụ

# // ###
# // Ví dụ 1

# // ```n=6,delay=2,forget=4```

# // ***Ngày 1**:
# // A biết
# // bí mật.***Ngày 2**:
# // A chưa
# // thể chia

# // sẻ (chưa đủ delay=2).
# // * **Ngày 3**: A bắt đầu chia sẻ → B biết bí mật.
# // * **Ngày 4**:

# // * A vẫn còn nhớ → chia sẻ tiếp → C biết.
# // * B chưa thể chia

# // sẻ (vừa mới biết).
# // * **Ngày 5**:

# // *

# // A quên (forget=4 → quên sau 4 ngày).
# // * B bắt đầu chia sẻ → D biết.
# // * C chưa thể chia sẻ.
# // * **Ngày 6**:

# // * B còn nhớ → chia sẻ tiếp → E biết.
# // * C bắt đầu chia sẻ → F biết.

# // 👉 Đến **ngày 6**, người biết bí mật: B, C, D, E, F = **5 người**.

# // ---

# // ### Ví dụ 2

# // ```
# // n = 4, delay = 1, forget = 3
# // ```

# // * **Ngày 1**: A biết bí mật.
# // * **Ngày 2**: A chia

# // sẻ ngay (delay=1) → B biết.
# // * **Ngày 3**:

# // *

# // A quên (forget=3 → sau 3 ngày).
# // * B chia sẻ → C biết.
# // * **Ngày 4**:

# // * B quên.
# // * C chia sẻ → D biết.

# // 👉 Đến ngày 4, người biết bí mật: C, D = **2 người**.

# // ---

# // ## ✅ Tóm gọn

# // * Mỗi người có **hai mốc thời gian** sau khi biết bí mật:

# // * Sau `delay` ngày: bắt đầu chia sẻ.
# // * Sau `forget` ngày: quên luôn.
# // * Cần đếm số người **còn nhớ** đến ngày `n`.

# // ---

# // Bạn có muốn mình minh họa thêm bằng **timeline bảng (ngày 1 → ngày n)** để
# // nhìn trực quan hơn không?
