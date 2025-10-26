# // 2043. Simple Bank System(26/10/2025)
# Dưới đây là phiên bản **đã thêm chú thích chi tiết** và **giải thích thuật toán** cho bài **2043. Simple Bank System** (Python):

# ---

# ```python
from typing import List
class Bank:
    def __init__(self, balance: List[int]):
        # Khởi tạo ngân hàng với danh sách số dư của các tài khoản
        # balance[i] là số tiền trong tài khoản thứ (i + 1)
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # Kiểm tra xem cả hai tài khoản có hợp lệ hay không
        # (phải nằm trong phạm vi 1 đến tổng số tài khoản)
        if (account1 <= 0 or account1 > len(self.balance) or 
            account2 <= 0 or account2 > len(self.balance)):
            return False
        
        # Kiểm tra xem tài khoản nguồn có đủ tiền để chuyển không
        if self.balance[account1 - 1] - money < 0:
            return False
        
        # Thực hiện chuyển tiền
        self.balance[account1 - 1] -= money  # trừ tiền từ tài khoản 1
        self.balance[account2 - 1] += money  # cộng tiền vào tài khoản 2
        return True  # chuyển tiền thành công

    def deposit(self, account: int, money: int) -> bool:
        # Kiểm tra tài khoản hợp lệ
        if account <= 0 or account > len(self.balance):
            return False
        
        # Cộng thêm tiền vào tài khoản
        self.balance[account - 1] += money
        return True  # nạp tiền thành công

    def withdraw(self, account: int, money: int) -> bool:
        # Kiểm tra tài khoản hợp lệ
        if account <= 0 or account > len(self.balance):
            return False
        
        # Kiểm tra số dư có đủ để rút không
        if self.balance[account - 1] - money < 0:
            return False
        
        # Trừ tiền khỏi tài khoản
        self.balance[account - 1] -= money
        return True  # rút tiền thành công
# ```

# ---

# ### 🧠 Giải thích thuật toán:

# * **Ý tưởng chính:**
#   Mỗi tài khoản được biểu diễn bằng một phần tử trong mảng `balance`.
#   Mỗi hàm tương ứng với một hành động trên tài khoản.

# ---

# #### 🔹 Hàm `transfer(account1, account2, money)`

# * Mục tiêu: Chuyển `money` từ `account1` sang `account2`.
# * Bước 1: Kiểm tra `account1` và `account2` hợp lệ.
# * Bước 2: Kiểm tra `account1` có đủ tiền.
# * Bước 3: Trừ tiền `account1`, cộng vào `account2`.
#   ✅ Trả về `True` nếu thành công, `False` nếu không.

# ---

# #### 🔹 Hàm `deposit(account, money)`

# * Mục tiêu: Nạp `money` vào `account`.
# * Bước 1: Kiểm tra `account` hợp lệ.
# * Bước 2: Cộng `money` vào `balance[account - 1]`.
#   ✅ Trả về `True` nếu thành công.

# ---

# #### 🔹 Hàm `withdraw(account, money)`

# * Mục tiêu: Rút `money` từ `account`.
# * Bước 1: Kiểm tra `account` hợp lệ.
# * Bước 2: Kiểm tra đủ tiền để rút.
# * Bước 3: Trừ tiền khỏi tài khoản.
#   ✅ Trả về `True` nếu rút thành công.

# ---

### 💡 Ví dụ minh họa:

# ```python
# bank = Bank([10, 100, 20, 50, 30])

# print(bank.withdraw(3, 10))   # True → [10,100,10,50,30]
# print(bank.transfer(5, 1, 20)) # True → [30,100,10,50,10]
# print(bank.deposit(5, 20))    # True → [30,100,10,50,30]
# print(bank.transfer(3, 4, 15)) # False (không đủ tiền)
# ```

# ---

# Bạn có muốn mình thêm **phiên bản chạy thử bằng `input()` (Scanner kiểu Java)** để test ngoài LeetCode không?



# // Tốt lắm 👍 cùng mình **giải thích đề LeetCode 2043 – Simple Bank System** nhé:
# import java.util.*;

# class Bank {
#     private long[] balance; // Mảng lưu số dư của các tài khoản

#     // Hàm khởi tạo ngân hàng với số dư ban đầu của các tài khoản
#     public Bank(long[] balance) {
#         this.balance = balance;
#     }

#     // Hàm chuyển tiền từ account1 sang account2
#     public boolean transfer(int account1, int account2, long money) {
#         // Kiểm tra nếu 1 trong 2 tài khoản không tồn tại
#         if (account1 - 1 >= balance.length || account2 - 1 >= balance.length || account1 <= 0 || account2 <= 0)
#             return false;

#         // Rút tiền từ account1, nếu rút thành công thì nạp vào account2
#         if (withdraw(account1, money)) {
#             return deposit(account2, money);
#         }

#         return false;
#     }

#     // Hàm nạp tiền vào tài khoản
#     public boolean deposit(int account, long money) {
#         // Kiểm tra tài khoản hợp lệ
#         if (account - 1 < balance.length && account > 0) {
#             this.balance[account - 1] += money; // Cộng thêm tiền
#             return true;
#         }
#         return false;
#     }

#     // Hàm rút tiền khỏi tài khoản
#     public boolean withdraw(int account, long money) {
#         // Kiểm tra tài khoản hợp lệ
#         if (account - 1 >= this.balance.length || account <= 0) return false;

#         // Kiểm tra đủ tiền không
#         if (this.balance[account - 1] < money) return false;

#         // Trừ tiền
#         this.balance[account - 1] -= money;
#         return true;
#     }

#     // In ra số dư hiện tại của tất cả tài khoản
#     public void printBalances() {
#         System.out.println("Số dư các tài khoản: " + Arrays.toString(balance));
#     }

#     // ================== HÀM MAIN ==================
#     public static void main(String[] args) {
#         Scanner sc = new Scanner(System.in);

#         // Nhập số lượng tài khoản
#         System.out.print("Nhập số lượng tài khoản: ");
#         int n = sc.nextInt();

#         // Nhập số dư ban đầu của từng tài khoản
#         long[] balance = new long[n];
#         System.out.println("Nhập số dư ban đầu của các tài khoản:");
#         for (int i = 0; i < n; i++) {
#             balance[i] = sc.nextLong();
#         }

#         // Tạo đối tượng Bank
#         Bank bank = new Bank(balance);

#         // Menu chức năng
#         while (true) {
#             System.out.println("\n=== MENU NGÂN HÀNG ===");
#             System.out.println("1. Nạp tiền");
#             System.out.println("2. Rút tiền");
#             System.out.println("3. Chuyển tiền");
#             System.out.println("4. Xem số dư");
#             System.out.println("5. Thoát");
#             System.out.print("Chọn chức năng: ");
#             int choice = sc.nextInt();

#             if (choice == 1) {
#                 System.out.print("Nhập số tài khoản: ");
#                 int acc = sc.nextInt();
#                 System.out.print("Nhập số tiền nạp: ");
#                 long money = sc.nextLong();
#                 System.out.println(bank.deposit(acc, money) ? "✅ Nạp thành công!" : "❌ Lỗi: tài khoản không hợp lệ.");

#             } else if (choice == 2) {
#                 System.out.print("Nhập số tài khoản: ");
#                 int acc = sc.nextInt();
#                 System.out.print("Nhập số tiền rút: ");
#                 long money = sc.nextLong();
#                 System.out.println(bank.withdraw(acc, money) ? "✅ Rút thành công!" : "❌ Lỗi: tài khoản không hợp lệ hoặc không đủ tiền.");

#             } else if (choice == 3) {
#                 System.out.print("Nhập tài khoản gửi: ");
#                 int acc1 = sc.nextInt();
#                 System.out.print("Nhập tài khoản nhận: ");
#                 int acc2 = sc.nextInt();
#                 System.out.print("Nhập số tiền chuyển: ");
#                 long money = sc.nextLong();
#                 System.out.println(bank.transfer(acc1, acc2, money) ? "✅ Chuyển thành công!" : "❌ Lỗi: chuyển thất bại.");

#             } else if (choice == 4) {
#                 bank.printBalances();

#             } else if (choice == 5) {
#                 System.out.println("Tạm biệt!");
#                 break;

#             } else {
#                 System.out.println("❌ Lựa chọn không hợp lệ.");
#             }
#         }

#         sc.close();
#     }
# }


# // ---

# // ## 🧾 **Đề bài tóm tắt**

# // Bạn được cho một **hệ thống ngân hàng đơn giản** với `n` tài khoản,
# // mỗi tài khoản có một **số dư ban đầu** (được cho trong mảng `balance`).

# // Bạn phải **mô phỏng 3 loại giao dịch** sau:

# // 1. **transfer(account1, account2, money)**
# //    → Chuyển `money` từ `account1` sang `account2`.

# // 2. **deposit(account, money)**
# //    → Gửi thêm `money` vào tài khoản `account`.

# // 3. **withdraw(account, money)**
# //    → Rút `money` ra khỏi tài khoản `account`.

# // ---

# // ## ⚙️ **Yêu cầu chi tiết**

# // ### 🔸 Input:

# // * Mảng `balance`, trong đó:

# //   * `balance[i]` là số tiền ban đầu của tài khoản thứ **i + 1** (lưu ý index bắt đầu từ 1).
# // * Một chuỗi các lệnh gọi hàm (operations), ví dụ:

# //   ```
# //   deposit(1, 100)
# //   transfer(1, 2, 50)
# //   withdraw(2, 30)
# //   ```

# // ---

# // ### 🔸 Điều kiện hợp lệ:

# // * Một tài khoản `account` hợp lệ nếu `1 ≤ account ≤ n`.
# // * Với `withdraw` và `transfer`, nếu **không đủ tiền**, giao dịch thất bại → **trả về false**.
# // * Nếu mọi điều kiện hợp lệ và có đủ tiền → **cập nhật số dư và trả về true**.

# // ---

# // ### 🔸 Output:

# // * Kết quả của từng giao dịch (`true` hoặc `false`).
# // * Cuối cùng, mảng `balance` có thể bị thay đổi sau nhiều giao dịch.

# // ---

# // ## 💡 Ví dụ:

# // ```text
# // Input:
# // balance = [10, 100, 20, 50, 30]
# // Operations:
# // withdraw(3, 10)
# // transfer(5, 1, 20)
# // deposit(5, 20)
# // transfer(3, 4, 15)
# // withdraw(10, 50)

# // Output:
# // [true, true, true, false, false]
# // ```

# // ### 🔍 Giải thích:

# // * `withdraw(3, 10)` → tài khoản 3 có 20 → rút được 10 → ✅
# //   `balance = [10, 100, 10, 50, 30]`
# // * `transfer(5, 1, 20)` → tài khoản 5 có 30 → chuyển được 20 → ✅
# //   `balance = [30, 100, 10, 50, 10]`
# // * `deposit(5, 20)` → cộng thêm 20 → ✅
# //   `balance = [30, 100, 10, 50, 30]`
# // * `transfer(3, 4, 15)` → tài khoản 3 chỉ có 10 → ❌
# // * `withdraw(10, 50)` → tài khoản 10 không tồn tại → ❌

# // ---

# // ## ✅ **Tóm lại:**

# // * Mỗi tài khoản có số dư.
# // * Ba thao tác: **gửi tiền**, **rút tiền**, **chuyển tiền**.
# // * Kiểm tra hợp lệ và đủ tiền trước khi thực hiện.
# // * Trả về `true/false` theo kết quả từng giao dịch.

# // ---

# // Nếu bạn muốn, mình có thể viết luôn **phiên bản Java có hàm main + Scanner** để bạn thấy rõ cách chạy không?
# // Rất hay — đoạn code bạn đưa ra là một cách **mô phỏng hệ thống ngân hàng đơn giản (Simple Bank System)**, tương ứng với bài **LeetCode 2043**.
# // Giờ mình sẽ giải thích **chi tiết từng phần logic và thuật toán** 👇

# // ---

# // ## 🔹 1. Ý tưởng tổng quát

# // Ta có nhiều **tài khoản ngân hàng**, mỗi tài khoản có **số dư ban đầu** (`balance[i]`).
# // Cần hỗ trợ 3 loại thao tác:

# // 1. `deposit(account, money)` — **nạp tiền** vào tài khoản.
# // 2. `withdraw(account, money)` — **rút tiền** khỏi tài khoản.
# // 3. `transfer(account1, account2, money)` — **chuyển tiền** từ tài khoản `account1` sang `account2`.

# // Mỗi thao tác chỉ hợp lệ nếu:

# // * Số tài khoản tồn tại (1 ≤ account ≤ balance.length).
# // * Tài khoản có đủ tiền khi rút hoặc chuyển.

# // ---

# // ## 🔹 2. Thuật toán và luồng xử lý

# // ### 🧩 `public Bank(long[] balance)`

# // Khởi tạo hệ thống ngân hàng với mảng `balance` lưu số dư ban đầu.
# // Ví dụ:

# // ```java
# // long[] balance = {10, 100, 20, 50, 30};
# // ```

# // → Tức là có 5 tài khoản với số dư tương ứng.

# // ---

# // ### 🧩 `deposit(int account, long money)`

# // **Mục tiêu:** cộng thêm `money` vào tài khoản `account`.

# // ```java
# // if (account - 1 < balance.length) {
# //     balance[account - 1] += money;
# //     return true;
# // }
# // return false;
# // ```

# // * `account - 1` vì chỉ số trong mảng là **0-based**, còn số tài khoản là **1-based**.
# // * Nếu tài khoản tồn tại, cộng thêm tiền và trả về `true`.
# // * Ngược lại (sai tài khoản) → `false`.

# // 📘 Ví dụ:

# // ```
# // balance = [10, 100, 20]
# // deposit(2, 50)
# // → balance[1] += 50 → balance = [10, 150, 20]
# // ```

# // ---

# // ### 🧩 `withdraw(int account, long money)`

# // **Mục tiêu:** trừ tiền nếu tài khoản có đủ tiền.

# // ```java
# // if (account - 1 >= balance.length) return false;
# // if (balance[account - 1] < money) return false;
# // balance[account - 1] -= money;
# // return true;
# // ```

# // * Kiểm tra tài khoản hợp lệ.
# // * Kiểm tra có đủ tiền.
# // * Nếu đủ → trừ tiền và trả về `true`.

# // 📘 Ví dụ:

# // ```
# // balance = [10, 150, 20]
# // withdraw(2, 100)
# // → balance[1] -= 100 → balance = [10, 50, 20]
# // ```

# // ---

# // ### 🧩 `transfer(int account1, int account2, long money)`

# // **Mục tiêu:** chuyển tiền từ `account1` sang `account2`.

# // ```java
# // if (account1 - 1 >= balance.length || account2 - 1 >= balance.length) return false;

# // if (withdraw(account1, money)) {
# //     return deposit(account2, money);
# // }
# // return false;
# // ```

# // 👉 Giải thích luồng:

# // 1. Kiểm tra cả hai tài khoản có tồn tại không.
# // 2. Nếu tài khoản `account1` có thể rút (`withdraw` thành công):

# //    * Thì nạp số tiền đó vào `account2` (`deposit`).
# // 3. Nếu rút thất bại (vì tài khoản không đủ tiền hoặc không tồn tại) → `false`.

# // 📘 Ví dụ:

# // ```
# // balance = [10, 50, 20]
# // transfer(2, 3, 30)

# // Bước 1: withdraw(2, 30) → true (balance = [10, 20, 20])
# // Bước 2: deposit(3, 30) → true (balance = [10, 20, 50])
# // Kết quả: true
# // ```

# // ---

# // ## 🔹 3. Tổng kết logic

# // | Hàm          | Công dụng   | Điều kiện hợp lệ                   | Hành động chính                |
# // | ------------ | ----------- | ---------------------------------- | ------------------------------ |
# // | `deposit()`  | Nạp tiền    | Tài khoản tồn tại                  | `balance[acc-1] += money`      |
# // | `withdraw()` | Rút tiền    | Tài khoản tồn tại + đủ tiền        | `balance[acc-1] -= money`      |
# // | `transfer()` | Chuyển tiền | Cả hai tài khoản tồn tại + đủ tiền | Gọi `withdraw()` + `deposit()` |

# // ---

# // ## 🔹 4. Độ phức tạp

# // * ⏱ **Thời gian:** O(1) cho mỗi thao tác.
# // * 💾 **Bộ nhớ:** O(n) cho `balance`.

# // ---

# // Nếu bạn muốn mình giúp viết lại phiên bản **ngắn gọn, tối ưu và pass toàn bộ test LeetCode**, mình có thể rút gọn lại và chỉnh điều kiện kiểm tra tài khoản hợp lệ gọn hơn — bạn muốn không?
