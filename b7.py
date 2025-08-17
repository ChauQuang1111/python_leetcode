# 837. New 21 Game(17/08/2025)
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k==0 or n>=k+maxPts:
            return 1.0
        dp = [0.0] * (n + maxPts + 1)        
        for i in range(k, n + 1):
            dp[i] = 1.0
# Khi đã ≥ k điểm, trò chơi kết thúc.

# Nếu điểm trong [k, n] → thắng → xác suất = 1.

# Nếu điểm > n → thua → xác suất = 0 (mặc định)
        windowSum = n - k + 1  # vì từ K đến N có (N-K+1) giá trị bằng 1
        for i in range(k - 1, -1, -1):
                    dp[i] = windowSum /maxPts
                    windowSum += dp[i] - dp[i + maxPts]

        return dp[0]
    
#     dp[x] là xác suất người chơi kết thúc với đúng số điểm x.

# Mình phải lưu dp cho tất cả giá trị điểm từ 0 đến n + maxPts.

# 2. Vì sao cần đến n + maxPts?

# Giả sử Alice đang có i điểm.

# Khi rút thẻ, cô ấy có thể thêm từ 1 → maxPts.

# Do đó, từ điểm n trở xuống, Alice có thể "vượt quá" n tối đa là maxPts điểm.

# Ví dụ:

# Nếu n = 10, maxPts = 10, thì Alice có thể kết thúc ở bất kỳ điểm nào từ 0 đến 20.

# Nghĩa là mảng dp phải có đủ 21 ô → dp[0..20].

# 3. Vì sao phải +1?

# Trong Python (và cả Java, C++), mảng có chỉ số từ 0 → length-1.

# Nếu bạn cần lưu 0 → n+maxPts, thì tổng số ô = (n+maxPts) + 1.

# Nếu không cộng 1, thì bạn chỉ có ô từ 0 → n+maxPts-1, thiếu mất 1 ô cuối cùng.

# 4. Tóm lại
# dp = [0.0] * (n + maxPts + 1)


# Bắt buộc phải có +1 để đảm bảo mảng đủ chỗ chứa các chỉ số từ 0 đến n+maxPts.

# Đây là kỹ thuật quen thuộc khi làm DP: nếu muốn lưu 0 → X thì phải cấp phát X+1 ô.
# Ok mình giải thích chi tiết dòng này trong bài 837. New 21 Game nhé:

# dp = [0.0] * (n + maxPts + 1)

# 1. Ý nghĩa của dp

# dp[x] biểu diễn xác suất đạt được tổng điểm bằng x trong trò chơi.

# Ta cần một mảng để lưu tất cả các giá trị đó.

# 2. Tại sao cần n + maxPts + 1 phần tử?

# Giả sử:

# n = 10 (giới hạn không được vượt quá)

# maxPts = 10 (mỗi lần rút được từ 1 → 10 điểm).

# 👉 Trường hợp xấu nhất:

# Trước khi dừng lại, người chơi có thể đạt tổng điểm n + maxPts - 1 = 10 + 10 - 1 = 19.

# Vì nếu đang có n-1 = 9 điểm, rút thêm tối đa maxPts = 10 thì đạt 19.

# Do đó, cần mảng dp có chỉ số từ 0 → n + maxPts để bao trùm tất cả giá trị có thể xảy ra.

# 3. Vì sao nhân với 0.0?

# Python tạo list với toàn giá trị 0.0 (số thực) để lưu xác suất (probability).

# Nếu để 0 (số nguyên), sau này tính toán với số thực có thể sai.

# Giải thích từng dòng

# windowSum = n - k + 1

# Ban đầu, dp[K], dp[K+1], …, dp[N] = 1.

# Có đúng (N - K + 1) số bằng 1.

# Vậy tổng windowSum = (N-K+1).

# dp[i] = windowSum / maxPts

# Xác suất thắng từ trạng thái i chính là trung bình của cửa sổ maxPts.

# windowSum += dp[i] - dp[i + maxPts]

# Khi lùi sang i-1, cửa sổ dịch sang trái:

# thêm dp[i]

# bỏ dp[i + maxPts].
# Khi i ≥ K và i ≤ N, thì dp[i] = 1.
# Số lượng các trạng thái này = N - K + 1.

# → Tổng xác suất = (N-K+1). này là độ dài của thanh window ấy ghi đúng dễ hiểu là đầu trừ cuối +1

# Cái này chính là tổng ban đầu để làm sliding window.