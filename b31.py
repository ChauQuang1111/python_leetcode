
# // 1733.Minimum Number of People to Teach(10/09/2025)
from typing import List

from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        
        # Bước 1: Chuyển danh sách ngôn ngữ của mỗi người sang tập hợp (set).
        # Sử dụng set giúp việc kiểm tra ngôn ngữ chung (giao điểm) rất nhanh chóng.
        learned = list(map(set, languages))

        # Bước 2: Khởi tạo các biến để theo dõi
        
        # 'total' đếm tổng số người duy nhất cần được dạy.
        total = 0
        
        # 'vis' (visited) là một mảng boolean để đánh dấu những người đã được thêm vào nhóm cần dạy.
        # Điều này giúp tránh việc đếm một người nhiều lần.
        vis = [False] * len(languages)
        
        # 'cnt' (count) là một mảng để đếm số người trong nhóm cần dạy đã biết mỗi ngôn ngữ.
        # Kích thước n + 1 để chỉ mục tương ứng với ID ngôn ngữ.
        cnt = [0] * (n + 1)

        def add(u: int) -> None:
            """
            Hàm này thêm một người vào nhóm cần dạy và cập nhật bộ đếm ngôn ngữ.
            
            Args:
                u (int): Chỉ mục của người cần thêm.
            """
            if vis[u]:
                # Nếu người này đã được thêm, không làm gì cả.
                return
            
            # Đánh dấu người này đã được thăm để tránh đếm lại.
            vis[u] = True
            
            # Sử dụng nonlocal để thay đổi biến 'total' ở phạm vi bao bọc.
            nonlocal total
            total += 1
            
            # Với mỗi ngôn ngữ mà người này biết, tăng bộ đếm tương ứng.
            for x in languages[u]:
                cnt[x] += 1

        # Bước 3: Duyệt qua các cặp bạn bè và xác định những người cần dạy.
        for u, v in friendships:
            # Chỉ số trong Python bắt đầu từ 0, trong khi ID người bắt đầu từ 1.
            # Vì vậy, ta cần trừ 1.
            
            # .isdisjoint() là một phương thức của set, trả về True nếu hai set không có phần tử chung.
            if learned[u - 1].isdisjoint(learned[v - 1]):
                # Nếu họ không có ngôn ngữ chung, thêm cả hai vào nhóm cần dạy.
                add(u - 1)
                add(v - 1)

        # Bước 4: Tính toán kết quả cuối cùng.
        # Kết quả bằng tổng số người cần dạy trừ đi số người đã biết ngôn ngữ được dạy.
        # max(cnt) tìm ra ngôn ngữ được biết bởi nhiều người nhất.
        return total - max(cnt)
    
    
# Đoạn code bạn cung cấp là một giải pháp rất hiệu quả và tinh gọn, sử dụng các tính năng mạnh mẽ của Python để giải quyết bài toán.

# Thuật toán này có thể được chia thành ba bước chính:

# 1.  **Xác định những người cần được dạy**:
#     * **Chuyển đổi dữ liệu**: Đầu tiên, code chuyển đổi danh sách các ngôn ngữ của mỗi người từ dạng `List[List[int]]` sang một danh sách các **`set`**. `set` là một cấu trúc dữ liệu cực kỳ nhanh để thực hiện các phép toán trên tập hợp, như tìm giao điểm.
#     * **Tìm các cặp không giao tiếp được**: Code duyệt qua từng cặp bạn bè. Với mỗi cặp, nó sử dụng phương thức `isdisjoint()` của `set` để kiểm tra xem hai người có bất kỳ ngôn ngữ chung nào không. `isdisjoint()` trả về `True` nếu hai tập hợp không có phần tử chung, tức là họ không thể giao tiếp.
#     * **Thu thập nhóm người cần dạy**: Nếu một cặp bạn bè không thể giao tiếp, code sẽ thêm cả hai người vào một nhóm. Để tránh đếm một người nhiều lần (vì họ có thể thuộc nhiều cặp bạn bè không giao tiếp được), code sử dụng một mảng boolean `vis` (viết tắt của "visited"). Chỉ những người chưa được thêm vào nhóm mới được xử lý.

# 2.  **Đếm tần suất ngôn ngữ**:
#     * Trong khi thu thập nhóm người cần dạy, code cũng đồng thời đếm xem mỗi ngôn ngữ được biết bởi bao nhiêu người trong nhóm này.
#     * Mảng `cnt` được sử dụng để lưu trữ số lượng người biết mỗi ngôn ngữ. Nếu một người biết ngôn ngữ `x`, giá trị `cnt[x]` sẽ được tăng lên.

# 3.  **Tính toán kết quả cuối cùng**:
#     * **Tìm ngôn ngữ tối ưu**: Sau khi đã đếm tần suất, code tìm giá trị lớn nhất trong mảng `cnt` bằng cách sử dụng `max(cnt)`. Giá trị này chính là số người lớn nhất đã biết một ngôn ngữ cụ thể trong nhóm cần dạy. Ngôn ngữ tương ứng với số đếm này là ngôn ngữ tối ưu để dạy.
#     * **Tính toán số người cần dạy**: Số người tối thiểu cần dạy sẽ bằng **tổng số người trong nhóm cần dạy** (`total`) trừ đi **số người đã biết ngôn ngữ tối ưu đó** (`max(cnt)`).

# ### Tóm tắt

# Thuật toán của bạn rất hiệu quả vì nó tránh việc lặp đi lặp lại không cần thiết. Thay vì duyệt qua danh sách những người cần dạy nhiều lần để tìm ngôn ngữ tối ưu, nó tích hợp việc đếm ngôn ngữ vào ngay khi xác định được người cần dạy. Điều này làm cho thuật toán trở nên nhanh hơn và tinh gọn hơn.
# // ### Giải thích Đề bài: Minimum Number of People to Teach

# // Đề bài **1733. Minimum Number of People to Teach** yêu cầu bạn tìm số lượng
# // người ít nhất cần phải dạy một ngôn ngữ để giải quyết vấn đề giao tiếp trong
# // một nhóm bạn.

# // Bạn được cung cấp ba thông tin:

# // 1. **`n`**: Tổng số người.
# // 2. **`languages`**: Một mảng (hoặc danh sách) các ngôn ngữ mà mỗi người biết.
# // `languages[i]` là một danh sách các ngôn ngữ mà người `i+1` biết.
# // 3. **`friendships`**: Một mảng (hoặc danh sách) các cặp bạn bè. Mỗi cặp `[u,
# // v]` biểu thị rằng người `u` và người `v` là bạn.

# // #### Vấn đề cần giải quyết

# // * Một cặp bạn bè `[u, v]` có thể giao tiếp với nhau nếu họ **biết chung ít
# // nhất một ngôn ngữ**.
# // * Nếu một cặp bạn bè không thể giao tiếp, bạn cần phải dạy cho họ một ngôn
# // ngữ mới.
# // * Để dạy một ngôn ngữ, bạn phải dạy nó cho **tất cả những người** cần học.

# // #### Yêu cầu

# // Bạn phải tìm ra một ngôn ngữ duy nhất để dạy, sao cho:

# // * Ngôn ngữ đó được dạy cho **số lượng người ít nhất**.
# // * Việc dạy ngôn ngữ này sẽ cho phép **tất cả các cặp bạn bè** không thể giao
# // tiếp trước đó, giờ đây có thể giao tiếp.

# // Nói cách khác, bạn cần tìm một ngôn ngữ **tối ưu** để dạy. Ngôn ngữ tối ưu là
# // ngôn ngữ mà khi bạn dạy nó cho tất cả những người trong nhóm bạn bè không
# // giao tiếp được, tổng số người được dạy là ít nhất.

# // #### Tóm tắt các bước giải quyết

# // 1. **Tìm các cặp bạn bè không giao tiếp được**:
# // * Duyệt qua danh sách `friendships`.
# // * Với mỗi cặp `[u, v]`, kiểm tra xem họ có biết chung ngôn ngữ nào không.
# // * Thu thập tất cả những người thuộc các cặp không giao tiếp được vào một tập
# // hợp (set), vì một người có thể là thành viên của nhiều cặp như vậy.

# // 2. **Đếm số người cần dạy cho mỗi ngôn ngữ**:
# // * Duyệt qua tất cả các ngôn ngữ có sẵn.
# // * Đối với mỗi ngôn ngữ, đếm xem có bao nhiêu người trong tập hợp những người
# // không giao tiếp được biết ngôn ngữ đó.
# // * Ví dụ: Nếu ngôn ngữ 1 được biết bởi 3 người trong nhóm cần dạy, thì bạn cần
# // dạy nó cho `(tổng số người cần dạy) - 3` người.

# // 3. **Tìm ngôn ngữ tối ưu**:
# // * Ngôn ngữ tối ưu là ngôn ngữ mà số người cần dạy nó là ít nhất.
# // * Tức là, ngôn ngữ đó được biết bởi số lượng người lớn nhất trong nhóm những
# // người không giao tiếp được.
# // * Số người tối thiểu cần dạy = `(tổng số người trong tập hợp) - (số người tối
# // đa đã biết một ngôn ngữ)`.

# // ---

# // **Lưu ý quan trọng**:
# // * Nếu một cặp bạn bè đã có thể giao tiếp, họ không cần phải được dạy thêm
# // ngôn ngữ.
# // * Nếu một người đã biết một ngôn ngữ, họ không cần phải được dạy lại ngôn ngữ
# // đó.
# // * Bạn chỉ có thể dạy **một ngôn ngữ duy nhất** cho tất cả những người cần
# // học.

# // Đây là
# // giải thích
# // chi tiết
# // về thuật
# // toán trong
# // đoạn code
# // của bạn.
# // Thuật toán
# // này rất
# // hiệu quả
# // vì nó
# // sử dụng lớp**`BitSet`**
# // của Java
# // để tối
# // ưu hóa
# // việc kiểm
# // tra các
# // ngôn ngữ
# // chung giữa
# // hai người.

# // ---

# // ###
# // Phân tích
# // Thuật toán

# // Thuật toán
# // của bạn
# // giải quyết
# // bài toán
# // theo ba
# // bước chính, mỗi
# // bước đều
# // được tối
# // ưu hóa:

# // ####1.
# // Biểu diễn
# // ngôn ngữ
# // bằng BitSet

# // ***Mục đích**:
# // Chuyển danh
# // sách các
# // ngôn ngữ
# // của mỗi
# // người thành
# // một cấu
# // trúc dữ
# // liệu hiệu
# // quả để
# // thực hiện
# // các phép
# // toán trên
# // tập hợp.***
# // Cách làm**:*
# // Bạn tạo
# // một mảng`BitSet`
# // có kích
# // thước bằng
# // số người.*Mỗi`BitSet`
# // trong mảng
# // đại diện
# // cho một
# // người. Ví dụ,`bit[i]`
# // là các
# // ngôn ngữ
# // mà người thứ`i+1`biết.*
# // Với mỗi
# // ngôn ngữ`l`
# // mà một
# // người biết, bạn

# // bật (set) bit thứ `l` trong `BitSet` của họ.

# // Cách tiếp cận này rất hiệu quả về bộ nhớ và thời gian, đặc biệt khi số lượng

# // ngôn ngữ (`n`) không quá lớn.

# // #### 2. Tìm những người cần dạy

# // * **Mục đích**: Xác định những người thuộc các cặp bạn bè không thể giao tiếp
# // được.
# // * **Cách làm**:
# // * Bạn duyệt qua danh sách các cặp bạn bè `F`.
# // * Với mỗi cặp `[f[0], f[1]]`, bạn thực hiện phép toán **AND bitwise** trên
# // hai `BitSet` tương ứng của họ.
# // * `t.and(bit[f[1] - 1])`: Phép toán này tạo ra một `BitSet` mới (`t`) chỉ
# // chứa những bit được bật ở cả hai `BitSet` ban đầu. Nói cách khác, nó tìm ra
# // các ngôn ngữ chung mà cả hai người đều biết.
# // * `if (t.isEmpty())`: Nếu `BitSet` kết quả rỗng (`isEmpty()`), có nghĩa là họ
# // không có ngôn ngữ chung và không thể giao tiếp.
# // * `teach.add(...)`: Trong trường hợp này, bạn thêm cả hai người vào tập hợp
# // `teach`. Sử dụng `HashSet` đảm bảo rằng mỗi người chỉ được thêm vào một lần
# // duy nhất, ngay cả khi họ là thành viên của nhiều cặp bạn bè không giao tiếp
# // được.

# // #### 3. Tìm ngôn ngữ tối ưu và tính toán kết quả

# // * **Mục đích**: Tìm một ngôn ngữ tối ưu để dạy và tính số người tối thiểu cần
# // dạy.
# // * **Cách làm**:
# // * Bạn tạo một mảng `count` để đếm số người trong tập hợp `teach` đã biết mỗi
# // ngôn ngữ.
# // * Bạn duyệt qua từng người trong tập hợp `teach`, sau đó duyệt qua từng ngôn
# // ngữ mà họ biết.
# // * `count[l]++`: Tăng bộ đếm cho ngôn ngữ `l` mà người đó biết.
# // * `maxKnown = Arrays.stream(count).max().getAsInt()`: Bạn tìm giá trị lớn
# // nhất trong mảng `count`. Giá trị này chính là số người lớn nhất trong nhóm
# // `teach` đã biết một ngôn ngữ cụ thể. Ngôn ngữ tương ứng với giá trị này là
# // ngôn ngữ tối ưu để dạy, vì bạn sẽ cần dạy nó cho ít người nhất.
# // * `return teach.size() - maxKnown`: Số người tối thiểu cần dạy bằng tổng số
# // người trong nhóm cần dạy trừ đi số người đã biết ngôn ngữ tối ưu.

# // ### Tóm tắt

# // Thuật toán của bạn rất tối ưu vì nó sử dụng **`BitSet`** để biểu diễn tập hợp
# // ngôn ngữ, cho phép các phép toán tìm giao điểm cực kỳ nhanh. Đây là một cách
# // tiếp cận nâng cao so với việc sử dụng `HashSet` và lặp lại. Toàn bộ thuật
# // toán được chia thành các bước logic rõ ràng, dẫn đến một giải pháp hiệu quả
# // về cả thời gian và bộ nhớ.