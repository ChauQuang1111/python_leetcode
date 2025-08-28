# 3446. Sort Matrix by Diagonals(28/08/2025)



### Giải thích thuật toán

# Thuật toán này thực hiện việc sắp xếp các đường chéo của một ma trận vuông bằng cách chia bài toán thành hai phần chính:

# 1.  **Sắp xếp các đường chéo dưới và đường chéo chính**:

#       * Các đường chéo này bắt đầu từ cột đầu tiên (`j = 0`) và lần lượt từ các hàng `k = 0, 1, ..., n-1`.
#       * Thuật toán duyệt qua từng đường chéo này, trích xuất tất cả các phần tử vào một mảng tạm `arr`.
#       * Sau đó, nó sắp xếp mảng `arr` theo thứ tự **giảm dần** (`reverse=True`).
#       * Cuối cùng, các phần tử đã sắp xếp được đưa trở lại vị trí ban đầu của chúng trong ma trận.

# 2.  **Sắp xếp các đường chéo trên đường chéo chính**:

#       * Các đường chéo này bắt đầu từ hàng đầu tiên (`i = 0`) và lần lượt từ các cột `k = 1, 2, ..., n-1`.
#       * Tương tự, thuật toán trích xuất các phần tử của mỗi đường chéo vào một mảng tạm `arr`.
#       * Nó sắp xếp mảng `arr` theo thứ tự **tăng dần** (mặc định của `arr.sort()`).
#       * Sau đó, nó đưa các phần tử đã sắp xếp trở lại ma trận.

# Việc chia thành hai vòng lặp riêng biệt giúp xử lý các quy tắc sắp xếp khác nhau cho hai nhóm đường chéo một cách rõ ràng.



### Chú thích chi tiết từng dòng mã


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid) # Lấy kích thước của ma trận (giả sử là ma trận vuông n x n)

        # PHẦN 1: Xử lý đường chéo chính và các đường chéo phía dưới nó
        # Các đường chéo này bắt đầu từ hàng k và cột 0
        for k in range(n):
            arr = [] # Mảng tạm để lưu các phần tử của đường chéo hiện tại
            i, j = k, 0 # Điểm bắt đầu của đường chéo: hàng i=k, cột j=0

            # Duyệt qua đường chéo và thu thập các phần tử
            # Đường chéo có tọa độ (i, j), (i+1, j+1), ...
            while i < n:
                arr.append(grid[i][j])
                i += 1
                j += 1
            
            # Sắp xếp mảng tạm theo thứ tự GIẢM DẦN
            arr.sort(reverse=True)
            
            i, j = k, 0 # Đặt lại điểm bắt đầu
            idx = 0 # Thêm một chỉ mục để duyệt qua mảng arr

            # Đặt các phần tử đã sắp xếp trở lại ma trận
            while i < n:
                # Gán phần tử từ mảng tạm arr vào vị trí đúng trong grid
                grid[i][j] = arr[idx] 
                i += 1
                j += 1
                idx += 1
        
        # PHẦN 2: Xử lý các đường chéo phía trên đường chéo chính
        # Các đường chéo này bắt đầu từ hàng 0 và cột k
        for k in range(1, n): # Bắt đầu từ k=1 vì k=0 là đường chéo chính đã xử lý ở trên
            arr = []
            i, j = 0, k # Điểm bắt đầu của đường chéo: hàng i=0, cột j=k

            # Duyệt qua đường chéo và thu thập các phần tử
            while j < n:
                arr.append(grid[i][j])
                i += 1
                j += 1
            
            # Sắp xếp mảng tạm theo thứ tự TĂNG DẦN (mặc định)
            arr.sort()
            
            i, j = 0, k # Đặt lại điểm bắt đầu
            idx = 0 # Thêm một chỉ mục để duyệt qua mảng arr

            # Đặt các phần tử đã sắp xếp trở lại ma trận
            while j < n:
                # Gán phần tử từ mảng tạm arr vào vị trí đúng trong grid
                grid[i][j] = arr[idx] 
                i += 1
                j += 1
                idx += 1
        
        return grid












# Dựa trên tiêu đề "Sort Matrix by Diagonals", bài toán yêu cầu bạn sắp xếp các phần tử của một ma trận vuông dọc theo các đường chéo của nó.

# ### Giải thích chi tiết

# 1.  **Xác định các đường chéo**: Một ma trận có nhiều đường chéo:
#     * **Đường chéo chính**: Chạy từ góc trên cùng bên trái xuống góc dưới cùng bên phải.
#     * **Các đường chéo dưới đường chéo chính**: Bắt đầu từ cột đầu tiên.
#     * **Các đường chéo trên đường chéo chính**: Bắt đầu từ hàng đầu tiên.

# 2.  **Sắp xếp từng đường chéo**: Bạn cần coi mỗi đường chéo là một danh sách các số riêng biệt. Dựa vào ví dụ, có một quy tắc sắp xếp cụ thể:
#     * Các đường chéo dưới và trên đường chéo chính sẽ được sắp xếp theo thứ tự **giảm dần**.
#     * Các đường chéo trên đường chéo chính sẽ được sắp xếp theo thứ tự **tăng dần**.

# 3.  **Thay thế các phần tử**: Sau khi sắp xếp từng đường chéo, bạn phải đặt các phần tử đã sắp xếp trở lại vị trí ban đầu của chúng trong ma trận.

# Kết quả cuối cùng sẽ là ma trận đã được sửa đổi, trong đó tất cả các đường chéo của nó đã được sắp xếp theo các quy tắc trên.