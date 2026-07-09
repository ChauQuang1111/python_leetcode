# // “Path Existence Queries in a Graph I” (09/07/2026)
# // thường là bài hỏi: trong một đồ thị, có tồn tại đường đi giữa hai đỉnh được hỏi hay không?



# // Hiểu đề bài

# // Cho một đồ thị gồm:



# // n đỉnh (vertices/nodes), thường được đánh số từ 0 đến n-1 hoặc 1 đến n.

# // m cạnh (edges) nối giữa các đỉnh.

# // q truy vấn (queries), mỗi truy vấn gồm hai đỉnh u và v.

# // Nhiệm vụ của mỗi truy vấn là kiểm tra:

# // Có tồn tại một đường đi từ u đến v hay không?

# // Nếu có thể đi từ u đến v qua một hoặc nhiều cạnh, ta trả lời:



# // YES, True, hoặc 1 (tùy đề bài yêu cầu).

# // Nếu không thể đi được, trả lời:



# // NO, False, hoặc 0.

# // Đường đi là gì?

# // Đường đi là một dãy các đỉnh liên tiếp sao cho mỗi cặp đỉnh liên tiếp đều có cạnh nối giữa chúng.

# // Ví dụ đồ thị:



# // Giữa 1 và 3: có đường đi 1 → 2 → 3, nên trả lời YES.

# // Giữa 1 và 5: không có cách nào đi sang nhóm 4–5, nên trả lời NO.

# // Ví dụ minh họa

# // Input:

# // Phân tích:



# // (1,3): đi được qua 1 → 2 → 3 → YES.

# // (1,5): không có đường nối từ nhóm 1-2-3 sang nhóm 4-5 → NO.

# // (4,5): có cạnh nối trực tiếp → YES.

# // Output:



# // Ý tưởng giải

# // Nếu số truy vấn ít

# // Với mỗi truy vấn (u, v), ta có thể:



# // Dùng DFS hoặc BFS bắt đầu từ u.

# // Nếu duyệt được tới v → YES.

# // Nếu duyệt hết mà chưa tới v → NO.

# // Nếu số truy vấn nhiều

# // Ta nên dùng DSU (Disjoint Set Union / Union-Find):



# // Ban đầu, mỗi đỉnh là một tập riêng.

# // Với mỗi cạnh (u, v), gộp u và v vào cùng một tập.

# // Khi trả lời truy vấn (u, v), chỉ cần kiểm tra u và v có cùng root hay không.

# // Nếu cùng root → YES, khác root → NO.



# // Tóm tắt

# // Bài hỏi tính liên thông giữa hai đỉnh trong đồ thị.

# // Hai đỉnh có đường đi giữa chúng nếu chúng nằm trong cùng một thành phần liên thông.

# // Giải bằng DFS/BFS nếu truy vấn ít.

# // Giải bằng DSU nếu có nhiều truy vấn cần trả lời nhanh.

# // Nếu bạn gửi nguyên văn đề bài hoặc ví dụ input/output cụ thể, mình có thể giải thích chi tiết theo đúng format của đề đó.

# // Code của bạn đang giải bài Path Existence Queries in a Graph I bằng cách tiền xử lý các thành phần liên thông theo chỉ số, thay vì tạo đồ thị rồi chạy BFS/DFS cho từng truy vấn.



# // Ý tưởng thuật toán

# // Giả sử nums đã được sắp xếp không giảm. Ta xem mỗi vị trí i là một đỉnh. Có thể đi từ vị trí i sang i+1 nếu:

# // nums[i+1]−nums[i]≤maxDiffnums[i+1] - nums[i] \le maxDiffnums[i+1]−nums[i]≤maxDiff

# // Vì mảng đã sắp xếp, nếu khoảng cách giữa hai phần tử liên tiếp vượt quá maxDiff, thì mọi phần tử bên trái không thể nối sang bên phải qua chuỗi các cạnh hợp lệ.

# // Do đó, ta chia mảng thành các đoạn liên thông:



# // Nếu nums[i] - nums[i-1] <= maxDiff, vị trí i thuộc cùng thành phần với i-1.

# // Nếu nums[i] - nums[i-1] > maxDiff, vị trí i bắt đầu một thành phần mới.

# // Mảng comp[i] lưu ID của thành phần liên thông chứa vị trí i.

# // Trả lời truy vấn

# // Với mỗi truy vấn [source, dest]:



# // Nếu source == dest thì chắc chắn có đường đi.

# // Nếu comp[source] == comp[dest] thì hai đỉnh nằm trong cùng một thành phần liên thông, nên có đường đi.

# // Ngược lại, không có đường đi.

# // Code đã thêm chú thích

# // Ví dụ minh họa

# // 2 - 1 = 1 <= 2 → cùng thành phần.

# // 4 - 2 = 2 <= 2 → cùng thành phần.

# // 7 - 4 = 3 > 2 → tách thành phần mới.

# // 8 - 7 = 1 <= 2 → cùng thành phần với 7.

# // Nghĩa là các vị trí 0,1,2 cùng nhóm, còn 3,4 cùng nhóm khác.



# // Độ phức tạp

# // Tiền xử lý mảng comp: O(n).

# // Trả lời mỗi truy vấn: O(1).

# // Tổng thời gian: O(n + q), với q là số truy vấn.

# // Bộ nhớ phụ: O(n).

# // Chương trình đầy đủ có hàm main dùng Scanner

# // Ví dụ nhập

# // Kết quả

# // Ở ví dụ này:



# // 0 2 → cùng thành phần → true.

# // 1 4 → khác thành phần → false.

# // 3 4 → cùng thành phần → true.




# import java.util.*;

# public class b270{

#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#      int n = sc.nextInt();

#         // 2. Nhập mảng nums (Lưu ý: bài toán này thường mặc định mảng nums đã được sắp xếp tăng dần)
#         int[] nums = new int[n];
#         for (int i = 0; i < n; i++) {
#             nums[i] = sc.nextInt();
#         }

#         // 3. Nhập giá trị chênh lệch tối đa maxDiff
#         System.out.print("Nhập khoảng cách tối đa maxDiff: ");
#         int maxDiff = sc.nextInt();

#         // 4. Nhập số lượng truy vấn
#         System.out.print("Nhập số lượng truy vấn q: ");
#         int q = sc.nextInt();

#         // 5. Nhập các cặp truy vấn (source, dest)
#         int[][] queries = new int[q][2];
#         for (int i = 0; i < q; i++) {
#             queries[i][0] = sc.nextInt(); // Điểm gốc
#             queries[i][1] = sc.nextInt(); // Điểm đích
#         }

        
#         boolean[] results = pathExistenceQueries(n, nums, maxDiff, queries);

#         // 6. In kết quả ra màn hình
#         for (int i = 0; i < results.length; i++) {
#             System.out.println("Truy vấn " + i + " (" + queries[i][0] + " -> " + queries[i][1] + "): " + results[i]);
#         }

#         sc.close(); 
#     }
# public static boolean[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
#         // Mảng lưu kết quả cho từng truy vấn
#         boolean[] res = new boolean[queries.length];

#         // Mảng comp để đánh dấu "thành phần liên thông" của từng phần tử.
#         // Nếu hai phần tử có cùng giá trị comp, chúng thuộc cùng một nhóm và có đường đi đến nhau.
#         int[] comp = new int[n];

#         int com = 0; // Biến đếm nhãn nhóm
#         comp[0] = com; // Phần tử đầu tiên thuộc nhóm 0

#         // Duyệt qua mảng nums để phân nhóm dựa trên điều kiện khoảng cách (maxDiff)
#         for (int i = 1; i < n; i++) {
#             // Nếu khoảng cách giữa 2 phần tử liền kề lớn hơn maxDiff, 
#             // "đường đi" bị ngắt quãng, ta tạo một nhóm mới (tăng com)
#             if (nums[i] - nums[i - 1] > maxDiff) {
#                 com++;
#             }
#             // Gán nhãn nhóm cho phần tử hiện tại
#             comp[i] = com;
#         }

#         // Xử lý từng truy vấn
#         for (int i = 0; i < queries.length; i++) {
#             int source = queries[i][0]; // Điểm bắt đầu
#             int dest = queries[i][1];   // Điểm kết thúc

#             // Nếu điểm đầu trùng điểm cuối, hoặc hai điểm thuộc cùng một nhóm liên thông
#             if ((source == dest) || (comp[source] == comp[dest])) {
#                 res[i] = true; // Có đường đi tồn tại
#             }
#         }

#         return res;
# }
# }

from collections import defaultdict
from typing import List
from pprint import pprint

class Solution:
    # -------------------------------------------------------------------------
    # CÁCH 1: Tiếp cận bằng Đệ quy + Ghi nhớ (Memoization) / Quy hoạch động
    # -------------------------------------------------------------------------
    def find_paths(self, q1: int, q2: int) -> bool:
        """
        Hàm đệ quy tìm kiếm xem có đường đi từ chỉ số q1 đến q2 hay không (giả định q1 < q2).
        Sử dụng cơ chế ghi nhớ (Memoization) để tránh tính toán lại.
        """
        # Nếu trạng thái (q1, q2) đã từng được tính và lưu trong ma trận, trả về ngay
        if q2 in self.path_matrix[q1]:
            return self.path_matrix[q1][q2]
        
        # Hệ thức quy hoạch động: Có đường đi từ q1 đến q2 KHI VÀ CHỈ KHI:
        # 1. Có đường đi từ q1 đến phần tử sát trước nó (q2 - 1)
        # TỒN TẠI ĐỒNG THỜI VỚI
        # 2. Khoảng cách giữa phần tử q2 và (q2 - 1) không vượt quá max_diff
        self.path_matrix[q1][q2] = self.find_paths(q1, q2 - 1) and (self.nums[q2] - self.nums[q2 - 1]) <= self.max_diff
        
        return self.path_matrix[q1][q2] 


    def pathExistenceQueries1(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        """
        Hàm xử lý truy vấn sử dụng cách tiếp cận Đệ quy có nhớ (find_paths).
        """
        # Khởi tạo ma trận kề dạng bảng băm lồng nhau (defaultdict của dict)
        self.path_matrix = defaultdict(dict)
        
        # Trường hợp cơ sở: Một phần tử luôn có đường đi tới chính nó
        for i in range(n):
            self.path_matrix[i][i] = True
            
        # Lưu các biến vào thuộc tính của object (self) để hàm find_paths có thể truy cập
        self.nums = nums
        self.max_diff = maxDiff
        
        ans = []
        # Duyệt qua từng truy vấn đầu vào
        for (q1, q2) in queries:
            # Đảm bảo q1 luôn nhỏ hơn q2 để xử lý duyệt một chiều từ trái sang phải
            q1, q2 = (q1, q2) if q2 > q1 else (q2, q1)
            # Gọi hàm đệ quy tìm đường và thêm kết quả vào mảng ans
            ans.append(self.find_paths(q1, q2))
            
        return ans


    # -------------------------------------------------------------------------
    # CÁCH 2: Tiếp cận tối ưu bằng Thành phần liên thông (Connected Components)
    # -------------------------------------------------------------------------
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        """
        Hàm tối ưu nhất: Gom nhóm các phần tử liên thông với nhau dựa trên khoảng cách liên kề.
        """
        # Nếu mảng rỗng thì không có truy vấn nào hợp lệ, trả về mảng rỗng
        if len(nums) == 0: 
            return []
            
        # connected_components[i] sẽ lưu "nhãn nhóm" (ID) của phần tử tại chỉ số i
        # Khởi đầu phần tử đầu tiên (chỉ số 0) thuộc nhóm mang số hiệu 0
        connected_components = [0]
        last_connected_components = 0 # Số hiệu nhóm hiện tại
        
        # Duyệt qua mảng bắt đầu từ phần tử thứ 2 (chỉ số 1)
        for i in range(1, n):
            # Nếu khoảng cách giữa phần tử hiện tại và phần tử ngay trước nó LỚN HƠN maxDiff,
            # nghĩa là "mạch" đường đi đã bị đứt gãy. Ta phải tạo một nhóm (thành phần liên thông) mới.
            if nums[i] - nums[i - 1] > maxDiff:
                last_connected_components += 1
            
            # Thêm số hiệu nhóm của phần tử i vào mảng quản lý
            connected_components.append(last_connected_components)

        # Trả về kết quả: Với mỗi truy vấn (q1, q2), nếu chúng thuộc cùng một nhóm liên thông 
        # (tức là connected_components[q1] == connected_components[q2]) thì trả về True, ngược lại False.
        return [connected_components[q1] == connected_components[q2] for q1, q2 in queries]
    
    
    





# Đoạn code đang giải bài toán: với mảng nums, hai vị trí i và j có đường đi nếu ta có thể đi từ vị trí này sang vị trí kia qua các phần tử kề nhau, và mọi cặp kề nhau trên đường đi đều có độ chênh lệch không vượt quá maxDiff.



# Ý tưởng cốt lõi

# Ta chỉ có thể di chuyển giữa k và k+1 khi:

# ∣nums[k+1]−nums[k]∣≤maxDiff|nums[k+1] - nums[k]| \le maxDiff∣nums[k+1]−nums[k]∣≤maxDiff

# Vì vậy, toàn bộ mảng được chia thành các thành phần liên thông (connected components):



# Nếu hai phần tử kề nhau thỏa điều kiện trên, chúng nằm trong cùng một thành phần.

# Nếu không thỏa, đó là một điểm ngắt và ta bắt đầu một thành phần mới.

# Hai chỉ số q1 và q2 có đường đi khi và chỉ khi chúng thuộc cùng một thành phần liên thông.



# Phiên bản tối ưu: gán nhãn thành phần liên thông

# Đây là hàm đang được sử dụng cuối cùng:



# Giải thích từng phần

# Khởi tạo

# Vị trí đầu tiên nums[0] được gán vào thành phần số 0.



# Duyệt mảng để tìm điểm ngắt

# Với mỗi cặp kề nhau nums[i-1] và nums[i]:



# Nếu nums[i] - nums[i-1] > maxDiff, ta không thể đi trực tiếp giữa hai vị trí này, nên tạo thành phần mới.

# Nếu điều kiện không xảy ra, nums[i] vẫn thuộc cùng thành phần với nums[i-1].

# Lưu ý: code dùng nums[i] - nums[i-1] thay vì abs(nums[i] - nums[i-1]). Điều này đúng khi nums là mảng không giảm (sorted/non-decreasing). Nếu mảng không đảm bảo sắp xếp, cần dùng abs(...).



# Trả lời truy vấn

# Hai chỉ số có đường đi nếu chúng có cùng nhãn thành phần.



# Ví dụ minh họa

# Giả sử:

# Cặp kề nhauChênh lệchKết luận(1, 3)2Cùng thành phần(3, 5)2Cùng thành phần(5, 10)5Ngắt thành phần(10, 12)2Cùng thành phần

# Kết quả:



# Các vị trí 0, 1, 2 thuộc thành phần 0.

# Các vị trí 3, 4 thuộc thành phần 1.

# Query (0, 2) → 0 == 0 → True.

# Query (1, 4) → 0 != 1 → False.

# Độ phức tạp

# Giai đoạnĐộ phức tạpDuyệt mảng để gán thành phầnO(n)Trả lời mỗi queryO(1)Tổng với q truy vấnO(n + q)Bộ nhớ phụO(n)

# Đây là phiên bản tối ưu nhất trong code vì:



# Chỉ cần duyệt mảng một lần để xác định các đoạn liên thông.

# Mỗi truy vấn chỉ cần so sánh hai số nguyên trong connected_components.

# Hai cách cũ trong code

# Cách 1: ma trận đường đi

# Ý tưởng:



# # path_matrix[i][j] lưu xem có đường đi từ i đến j hay không.

# # Muốn đi từ i đến j, phải đi được từ i đến j-1 và cạnh cuối (j-1, j) phải hợp lệ.

# # Độ phức tạp:



# # Tiền xử lý: O(n²).

# # Truy vấn: O(1).

# # Bộ nhớ: O(n²).

# Nhược điểm: tốn bộ nhớ và thời gian khi n lớn.



# Cách 2: đệ quy + memoization

# Ý tưởng:



# find_paths(q1, q2) kiểm tra đường đi từ q1 đến q2.

# Kết quả được lưu vào self.path_matrix để tránh tính lại.

# Độ phức tạp:



# Trong trường hợp xấu, vẫn có thể gần O(n²).

# Có thêm chi phí đệ quy.

# Tóm tắt

# Bài toán thực chất là kiểm tra xem hai chỉ số có nằm trong cùng một đoạn liên tục mà mọi chênh lệch kề nhau ≤ maxDiff hay không.

# Thuật toán tối ưu gán cho mỗi vị trí một mã thành phần liên thông.

# Mỗi khi gặp cặp kề nhau có chênh lệch vượt maxDiff, ta tăng mã thành phần.

# Trả lời query bằng cách so sánh hai mã thành phần.

# Kết luận: phiên bản cuối có độ phức tạp O(n + q), nhanh và tiết kiệm bộ nhớ hơn nhiều so với hai cách trước.