# 12/08/2025
# # LeetCode 215. Kth Largest Element in an Array
class Solution:                                                        
    def findKthLargest(self, nums, k):
        count = [0] * 20001
        for num in nums:
            count[num + 10000] += 1
        
        for i in range(len(count) - 1, -1, -1):
            if count[i] > 0:
                k -= count[i]
                if k <= 0:
                    return i - 10000
        return -1


# Một mảng count có kích thước 20001 được tạo ra và tất cả các phần tử ban đầu đều bằng 0.

# Lý do kích thước là 20001 là vì bài toán giả định các số trong mảng nums nằm trong khoảng từ -10000 đến 10000. Để xử lý các số âm, chúng ta cần "dịch" (offset) các giá trị này.

# Việc cộng 10000 vào mỗi số (num + 10000) sẽ đảm bảo rằng tất cả các giá trị sau khi dịch đều không âm và nằm trong phạm vi từ 0 (cho số -10000) đến 20000 (cho số 10000).

# Mỗi chỉ số i của mảng count sẽ tương ứng với số i - 10000 ban đầu.

# Vòng lặp này duyệt qua từng phần tử num trong mảng nums.

# Với mỗi num, chúng ta tăng giá trị tại chỉ số num + 10000 của mảng count lên 1.

# Sau khi vòng lặp kết thúc, mảng count sẽ lưu trữ số lần xuất hiện (tần suất) của mỗi số trong mảng nums. Ví dụ, count[10005] sẽ cho biết có bao nhiêu số 5 trong mảng ban đầu.

# Vòng lặp này duyệt qua mảng count từ cuối về đầu (từ chỉ số 20000 về 0).

# Điều này tương đương với việc duyệt qua các số trong mảng ban đầu từ lớn nhất đến nhỏ nhất.

# i đại diện cho một giá trị đã được dịch, và i - 10000 là giá trị thực tế của số đó.

# if count[i] > 0:: Kiểm tra xem có số nào tương ứng với giá trị i - 10000 hay không.

# k -= count[i]: Nếu có, chúng ta giảm k đi số lượng các số đó. Về mặt logic, chúng ta đang "loại bỏ" các phần tử lớn nhất.

# if k <= 0:: Sau khi giảm k, nếu k nhỏ hơn hoặc bằng 0, điều đó có nghĩa là phần tử lớn thứ k đã được tìm thấy. Phần tử này chính là giá trị tương ứng với chỉ số i hiện tại.

# return i - 10000: Trả về giá trị thực tế của số đó bằng cách đảo ngược phép dịch

# Nếu vòng lặp kết thúc mà k vẫn lớn hơn 0 (ví dụ: k quá lớn so với số lượng phần tử trong mảng), hàm sẽ trả về -1.

def main():
    # Ví dụ 1
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    solution = Solution()
    result1 = solution.findKthLargest(nums1, k1)
    print(f"Mảng: {nums1}, k = {k1}")
    print(f"Phần tử lớn thứ {k1} là: {result1}")
    print("-" * 30)

    # Ví dụ 2
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    result2 = solution.findKthLargest(nums2, k2)
    print(f"Mảng: {nums2}, k = {k2}")
    print(f"Phần tử lớn thứ {k2} là: {result2}")
    print("-" * 30)

    # Ví dụ 3 (có số âm)
    nums3 = [-1, -2, -3, -4, -5]
    k3 = 2
    result3 = solution.findKthLargest(nums3, k3)
    print(f"Mảng: {nums3}, k = {k3}")
    print(f"Phần tử lớn thứ {k3} là: {result3}")
    print("-" * 30)

# Gọi hàm main để chạy chương trình
if __name__ == "__main__":
    main()

