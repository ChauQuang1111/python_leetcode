# 1578. Minimum Time to Make Rope Colorful(03/11/2025)
# Rất hay — đây là một **cách giải tối ưu khác** cho bài **1578. Minimum Time to Make Rope Colorful**, dùng **two pointers (l, r)** để duyệt cặp ký tự liền kề.
# Mình sẽ **giải thích chi tiết thuật toán**, rồi **thêm chú thích vào code** để bạn dễ hiểu.

# ---

# ## 🧠 Ý tưởng thuật toán

# * Duyệt chuỗi từ trái sang phải, luôn giữ một con trỏ `l` trỏ vào **kí tự cuối cùng trong nhóm hiện tại** (màu đang xét).

# * Dùng `r` để **xem ký tự tiếp theo**.

# * Nếu `colors[l] != colors[r]`:
#   👉 Hai ký tự khác màu → không cần xóa gì → di chuyển `l = r`.

# * Nếu `colors[l] == colors[r]`:
#   👉 Hai ký tự trùng màu → **phải xóa một trong hai** để tránh trùng.
#   → Xóa ký tự có `neededTime` nhỏ hơn, vì ta muốn **giữ lại phần tốn thời gian xóa nhiều hơn (tức giữ phần "đắt nhất")**.

#   * Nếu `neededTime[l] < neededTime[r]`:
#     Xóa `l`, cộng chi phí `neededTime[l]`, rồi cập nhật `l = r` (vì giữ `r` lại).
#   * Ngược lại:
#     Xóa `r`, cộng chi phí `neededTime[r]` (giữ `l` lại, không cần đổi `l`).

# Duyệt hết chuỗi, `res` chính là tổng chi phí tối thiểu.

# ---

# ## 📘 Code có chú thích

# ```python
from typing import List
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l = 0           # 'l' là con trỏ giữ vị trí của ký tự hiện tại trong nhóm cùng màu
        res = 0         # biến lưu tổng chi phí tối thiểu
        
        # Duyệt từ ký tự thứ 2 đến cuối (r là right pointer)
        for r in range(1, len(colors)):
            
            if colors[l] == colors[r]:
                # Nếu hai ký tự liên tiếp có cùng màu → phải xóa một trong hai
                
                if neededTime[l] < neededTime[r]:
                    # Xóa ký tự ở vị trí l (rẻ hơn)
                    res += neededTime[l]
                    # Giữ lại ký tự r (đắt hơn), cập nhật l = r
                    l = r
                else:
                    # Xóa ký tự ở vị trí r (rẻ hơn)
                    res += neededTime[r]
                    # Giữ lại ký tự l (vì đắt hơn), không cần đổi l
            else:
                # Nếu màu khác nhau → di chuyển l sang r
                l = r
        
        return res

## 🔍 Ví dụ minh họa

### Input:

# ```python
# colors = "abaac"
# neededTime = [1, 2, 3, 4, 5]
# ```

# ### Diễn giải:

# | Step | l | r | colors[l], colors[r] | neededTime[l], neededTime[r] | Hành động                             | res |
# | ---- | - | - | -------------------- | ---------------------------- | ------------------------------------- | --- |
# | 1    | 0 | 1 | a, b                 | 1, 2                         | khác màu → l=1                        | 0   |
# | 2    | 1 | 2 | b, a                 | 2, 3                         | khác màu → l=2                        | 0   |
# | 3    | 2 | 3 | a, a                 | 3, 4                         | cùng màu → xóa 3 (rẻ hơn), giữ 4, l=3 | 3   |
# | 4    | 3 | 4 | a, c                 | 4, 5                         | khác màu → l=4                        | 3   |

# ✅ Kết quả cuối cùng: `res = 3`

# ---

# ## ⚙️ Độ phức tạp

# * **Thời gian:** O(n) — duyệt một lần qua chuỗi.
# * **Không gian:** O(1) — chỉ dùng vài biến phụ.

# ---

# Tóm lại:
# 👉 Đây là giải pháp **greedy + two pointers** rất ngắn gọn, ý tưởng chính là **so sánh từng cặp ký tự cùng màu** và **xóa ký tự có thời gian nhỏ hơn** để tối ưu chi phí.

# Mô tả đề (ngắn gọn)

# Cho một chuỗi colors (mỗi ký tự là màu của một đoạn dây nối kế nhau) và mảng neededTime (cost để xóa đoạn đó). Ta cần loại bỏ một số đoạn sao cho không còn hai ký tự kề nhau giống màu nhau (tức colors[i] != colors[i+1] với mọi i). Mỗi lần xóa đoạn i, phải trả neededTime[i]. Hỏi tổng chi phí tối thiểu để đạt mục tiêu.

# Ý tưởng (greedy, trực quan)

# Nếu có một đoạn liên tiếp gồm k ký tự giống màu (ví dụ aaaa), thì trong k ký tự đó phải giữ lại đúng 1 và xóa k-1 cái còn lại.

# Để chi phí nhỏ nhất, trong mỗi đoạn liên tiếp cùng màu ta giữ phần có neededTime lớn nhất, và xóa tất cả phần còn lại (vì giữ phần lớn nhất giảm tổng tiền xóa).

# Vậy với mỗi nhóm liên tiếp cùng màu: thêm vào đáp án sum(group) - max(group).

# Chứng minh ngắn

# Trong một nhóm các ký tự cùng màu, bắt buộc phải xóa tất cả trừ 1. Việc giữ phần có chi phí lớn nhất là tối ưu vì nó tối thiểu hóa tổng chi phí xóa (tổng xóa = tổng cả nhóm − cost_được_giữ). Không có tương tác giữa các nhóm khác màu nên tối ưu toàn cục bằng tối ưu từng nhóm (greedy đúng).

# Thuật toán

# Duyệt chuỗi một lần, gom các ký tự liên tiếp giống nhau thành nhóm; với mỗi nhóm tính tổng chi phí và max chi phí, cộng sum − max vào kết quả. Độ phức tạp O(n), bộ nhớ O(1).

# Ví dụ

# colors = "abaac", neededTime = [1,2,3,4,5]
# Nhóm aa có times [3,4] ⇒ sum=7, max=4 ⇒ phải trả 7−4=3. Kết quả = 3.

# colors = "abc", neededTime = [1,2,3] ⇒ không có nhóm >1 ⇒ kết quả = 0.

# colors = "bbba", neededTime = [1,3,2,4]
# Nhóm bbb times [1,3,2] ⇒ sum=6, max=3 ⇒ trả 3.