#   2273. Find Resultant Array After Removing Anagrams(13/10/2025)

## 🧩 Code có chú thích

# ```python
from itertools import groupby
from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        # groupby(words, sorted) sẽ nhóm các từ LIỀN KỀ trong danh sách `words`
        # có cùng "key" — tức là cùng giá trị trả về của hàm sorted(word)
        # (sorted(word) trả về danh sách ký tự đã sắp xếp, nên các anagram sẽ có cùng key)
        
        # Với mỗi nhóm gộp được (g), ta chỉ lấy phần tử đầu tiên (next(g))
        # => bỏ qua các từ liền kề là anagram
        return [next(g) for _, g in groupby(words, sorted)]


## 🧠 Giải thích thuật toán từng bước

# Giả sử input:

# ```python
# words = ["abba", "baba", "bbaa", "cd", "cd"]
# ```

# ### Bước 1️⃣: `groupby(words, sorted)`

# * Hàm `groupby` trong `itertools` sẽ **gom nhóm các phần tử liền kề có cùng "key"**.
# * Ở đây, key = `sorted(word)`
#   → Khi `sorted("abba")` = `['a', 'b', 'b', 'a']`
#   → Khi `sorted("baba")` = `['a', 'a', 'b', 'b']`

# → `"abba"`, `"baba"`, `"bbaa"` đều có cùng key `'aabb'` → được gom thành **một nhóm**.

# ### Bước 2️⃣: `[next(g) for _, g in groupby(...)]`

# * `g` là **iterator của nhóm các từ liền kề cùng key**.
# * `next(g)` lấy **từ đầu tiên của nhóm đó** → chính là từ đầu tiên trong các anagram liền kề.
# * Các từ anagram liền kề sau đó **bị bỏ qua**.

### Kết quả:


# Nhóm 1: ['abba', 'baba', 'bbaa']  → giữ 'abba'
# Nhóm 2: ['cd']                    → giữ 'cd'
# Nhóm 3: ['cd']                    → giữ 'cd'
# ```

# 👉 Kết quả cuối cùng: `['abba', 'cd']`

# ---

# ## ⏱️ Độ phức tạp

# * **Thời gian**: `O(n * k log k)`
#   (`sorted(word)` sắp xếp mỗi từ có độ dài `k`, thực hiện cho `n` từ)
# * **Không gian**: `O(n)` (do tạo danh sách kết quả mới)

# ---

# ## ✅ Ví dụ chạy

# ```python
# sol = Solution()
# print(sol.removeAnagrams(["abba", "baba", "bbaa", "cd", "cd"]))
# ```

# **Output:**

# ```python
# ['abba', 'cd']
# ```

# ---

# ### 💡 Tóm tắt ý tưởng

# > Nhóm các từ liền kề có cùng tập ký tự (sau khi sắp xếp).
# > Giữ lại từ đầu tiên trong mỗi nhóm.
# > Dùng `itertools.groupby` để làm việc này gọn và nhanh.

# ---

# Bạn có muốn mình viết thêm **phiên bản thủ công không dùng `groupby`** để thấy rõ bên trong `groupby` hoạt động như thế nào không?

# import java.util.*; 


# public class b66 {
#     static Scanner sc = new Scanner(System.in);

#     public static void main(String[] args) {
#         int n = sc.nextInt();
#         sc.nextLine(); // Bỏ dòng trống sau khi nhập số

#         // Nhập mảng từ
#         String[] words = new String[n];
#         System.out.println("Nhập " + n + " từ:");
#         for (int i = 0; i < n; i++) {
#             words[i] = sc.nextLine();
#         }

#         List<String> result = removeAnagrams(words);

#         // In kết quả
#         System.out.println("Kết quả sau khi xóa anagram liền kề:");
#         for (String word : result) {
#             System.out.println(word);
#         }

#         sc.close();
#     }

#     static List<String> res; // Danh sách kết quả cuối cùng

#     public static List<String> removeAnagrams(String[] words) {
#         // Trả về một danh sách "ảo" kế thừa từ AbstractList
#         // Khi gọi size() hoặc get(), nó mới thực sự xử lý
#         return new AbstractList<String>() {
#             @Override
#             public int size() {
#                 init(); // Khởi tạo dữ liệu khi cần
#                 return res.size();
#             }

#             @Override
#             public String get(int index) {
#                 init(); // Đảm bảo danh sách đã được tạo
#                 return res.get(index);
#             }

#             // Hàm xử lý chính: xóa các từ liền kề là anagram của nhau
#             protected void init() {
#                 if (res != null)
#                     return; // Nếu đã xử lý rồi thì không cần làm lại

#                 res = new ArrayList<>();
#                 res.add(words[0]); // Luôn thêm từ đầu tiên vào danh sách

#                 String cur = metaDo(words[0]); // Chuyển từ đầu tiên thành "chuỗi chuẩn hóa"
#                 for (int j = 1; j < words.length; j++) {
#                     String s0 = metaDo(words[j]); // Chuẩn hóa từ hiện tại
#                     // Nếu khác với từ trước (tức là không phải anagram liền kề)
#                     if (!s0.equals(cur)) {
#                         res.add(words[j]); // Thêm vào danh sách kết quả
#                         cur = s0; // Cập nhật mẫu anagram hiện tại
#                     }
#                 }
#             }
#         };
#     }

#     // Hàm chuẩn hóa một từ (sort ký tự trong chuỗi để dễ so sánh anagram)
#     public static String metaDo(String s) {
#         char[] chars = s.toCharArray();
#         Arrays.sort(chars); // Sắp xếp ký tự theo thứ tự ASCII
#         return String.valueOf(chars); // Trả lại chuỗi sau khi sắp xếp
#     }
# }

# // Hàm main để nhập và chạy chương trình

# // Tất nhiên 😊 — đây là **đề bài LeetCode 2273. Find Resultant Array After
# // Removing Anagrams**, mình sẽ giải thích chi tiết cho bạn:

# // ---

# // ### 🧩 **Đề bài**

# // Bạn được cho một **mảng các chuỗi `words`**.

# // 👉 **Nhiệm vụ:**
# // Hãy **loại bỏ** khỏi mảng các phần tử là **anagram liên tiếp** của nhau.
# // Sau khi loại bỏ, **trả về mảng còn lại theo thứ tự ban đầu**.

# // ---

# // ### 📘 **Giải thích thuật ngữ:**

# // * **Anagram**: Hai chuỗi là anagram của nhau nếu **chúng chứa cùng các ký tự
# // với cùng số lần xuất hiện**, chỉ khác thứ tự.
# // 🔹 Ví dụ: `"code"` và `"deco"` là anagram vì cả hai đều có c, o, d, e.

# // ---

# // ### 📥 **Input Example**

# // ```python
# // words = ["abba","baba","bbaa","cd","cd"]
# // ```

# // ---

# // ### ⚙️ **Cách xử lý**

# // * Xét từng từ trong mảng theo thứ tự.
# // * Nếu từ hiện tại là **anagram của từ trước đó**, thì **bỏ qua**.
# // * Ngược lại, **giữ lại** từ đó.

# // ---

# // ### 🔍 **Bước phân tích**

# // 1. `["abba", "baba", "bbaa", "cd", "cd"]`

# // * "abba" → giữ.
# // * "baba" → là anagram của "abba" (vì sắp xếp ký tự ra `"aabb"` giống nhau) ⇒
# // **bỏ**.
# // * "bbaa" → cũng là anagram của "abba" ⇒ **bỏ**.
# // * "cd" → không phải anagram của "abba" ⇒ **giữ**.
# // * từ thứ 5 `"cd"` → anagram của từ trước `"cd"` ⇒ **bỏ**.

# // ---

# // ### 📤 **Output**

# // ```python
# // ["abba", "cd"]
# // ```

# // ---

# // ### 💡 **Ý tưởng thuật toán**

# // * Duyệt qua mảng từ đầu đến cuối.
# // * So sánh **chuỗi hiện tại sau khi sắp xếp ký tự** với **chuỗi trước đó sau
# // khi sắp xếp ký tự**.
# // * Nếu khác → thêm vào kết quả.
# // * Nếu giống → bỏ qua.

# // ---

# // ### ✅ **Code minh họa (Python)**

# // ```python
# // class Solution:
# // def removeAnagrams(self, words):
# // res = [words[0]]
# // for i in range(1, len(words)):
# // if sorted(words[i]) != sorted(words[i - 1]):
# // res.append(words[i])
# // return res
# // ```

# // ---

# // ### 🧠 **Tóm tắt**

# // | Bước | Ý nghĩa |
# // | ---- | -------------------------- |
# // | 1 | So sánh từng cặp liên tiếp |
# // | 2 | Nếu là anagram → bỏ |
# // | 3 | Nếu khác → giữ lại |
# // | 4 | Trả kết quả cuối cùng |

# // ---

# // Bạn có muốn mình giải thích thêm **vì sao chỉ so sánh với từ trước đó (không
# // cần so sánh với tất cả từ trước)** không?
# // Rất hay 👏 — đây là một **cách viết cực “Java nâng cao”** cho bài *LeetCode
# // 2273 – Find Resultant Array After Removing Anagrams*.
# // Mình sẽ giải thích **từng phần** thuật toán, cấu trúc và ý tưởng đằng sau
# // đoạn code này nhé 👇

# // ---

# // ## 🧩 Mục tiêu bài toán

# // Giống như trước:

# // > Xóa **các từ liền kề là anagram của nhau** trong mảng `words`, và trả về
# // danh sách kết quả.

# // ---

# // ## ⚙️ Tổng quan cấu trúc

# // Code này **không dùng trực tiếp `ArrayList`**, mà **trả về một lớp ẩn danh
# // (anonymous inner class)** kế thừa `AbstractList<String>`.

# // ```java
# // return new AbstractList<String>() { ... };
# // ```

# // 👉 Điều này cho phép bạn **trả về một đối tượng “giống List”** mà chỉ cần
# // định nghĩa lại 2 phương thức bắt buộc:

# // * `size()`
# // * `get(index)`

# // ---

# // ## 🧠 Cơ chế hoạt động chi tiết

# // ### 1️⃣ Khi `removeAnagrams` được gọi

# // Nó **chưa xử lý ngay**.
# // Thay vào đó, nó **tạo một “lazy list”** – nghĩa là chỉ khi nào bạn **gọi
# // `size()` hoặc `get()`**, thì nó **mới khởi tạo danh sách `res`** thật sự.

# // ---

# // ### 2️⃣ `init()` — xử lý chính

# // Hàm `init()` sẽ thực hiện **lọc các từ không phải anagram liền kề**.

# // ```java
# // protected void init() {
# // if (res != null)
# // return; // nếu đã tính rồi thì bỏ qua
# // res = new ArrayList<String>();
# // res.add(words[0]); // thêm từ đầu tiên

# // String cur = metaDo(words[0]); // sắp xếp chữ cái để tạo “dấu vân tay”
# // for (int J = 1; J < words.length; J += 1) {
# // final String s0 = metaDo(words[J]);
# // if (!s0.equals(cur)) { // nếu không phải anagram của từ trước
# // res.add(words[J]);
# // cur = s0; // cập nhật “dấu vân tay”
# // }
# // }
# // }
# // ```

# // ---

# // ### 3️⃣ `metaDo()` — kiểm tra anagram

# // ```java
# // private static String metaDo(String s) {
# // char[] chars = s.toCharArray();
# // Arrays.sort(chars); // sắp xếp ký tự của chuỗi theo thứ tự ASCII
# // return String.valueOf(chars); // trả về dạng chuẩn hóa
# // }
# // ```

# // Ví dụ:

# // | Chuỗi | Sau khi `metaDo()` |
# // | ------ | ------------------ |
# // | "baba" | "aabb" |
# // | "abba" | "aabb" |

# // 👉 Hai chuỗi này cùng kết quả → anagram.

# // ---

# // ### 4️⃣ Hoạt động khi gọi list

# // Ví dụ:

# // ```java
# // List<String> ans = new Solution().removeAnagrams(new String[]{"abba", "baba",
# // "bbaa", "cd", "cd"});
# // System.out.println(ans);
# // ```

# // Khi `println` chạy, Java sẽ gọi `size()` và `get(i)` → `init()` được kích
# // hoạt → danh sách được tính toán xong rồi trả về.

# // ---

# // ## 📘 Ví dụ minh họa

# // Input:

# // ```
# // ["abba", "baba", "bbaa", "cd", "cd"]
# // ```

# // Quy trình:

# // | words[J] | metaDo() | cur | Giống cur? | Hành động | res |
# // | -------- | -------- | ---- | ---------- | --------- | ---------- |
# // | abba | aabb | — | — | thêm | [abba] |
# // | baba | aabb | aabb | ✅ | bỏ qua | [abba] |
# // | bbaa | aabb | aabb | ✅ | bỏ qua | [abba] |
# // | cd | cd | aabb | ❌ | thêm | [abba, cd] |
# // | cd | cd | cd | ✅ | bỏ qua | [abba, cd] |

# // Output:

# // ```
# // ["abba", "cd"]
# // ```

# // ---

# // ## ⏱️ Độ phức tạp

# // * Thời gian: **O(n × m log m)** (vì `Arrays.sort()` cho mỗi từ)
# // * Bộ nhớ: **O(n × m)** để lưu `res`

# // ---

# // ## 💡 Tổng kết

# // | Thành phần | Vai trò |
# // | ---------------------- | -------------------------------------- |
# // | `AbstractList<String>` | Tạo một List “ảo” chỉ tính khi cần |
# // | `init()` | Hàm chính lọc anagram |
# // | `metaDo()` | Chuẩn hóa chuỗi để phát hiện anagram |
# // | `res` | Lưu kết quả cuối cùng |
# // | `cur` | “Dấu vân tay” của từ cuối cùng đã thêm |

# // ---

# // Nếu bạn muốn, mình có thể giúp bạn **viết lại code này thành phiên bản Java
# // chuẩn hơn (không dùng AbstractList)** để dễ hiểu hơn — bạn muốn mình làm vậy
# // không?
