# // 2353. Design a Food Rating System(17/09/2025)
import heapq
from collections import defaultdict
from typing import List

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # Map: food -> cuisine
        self.food2cuisine = {}
        # Map: food -> latest rating
        self.food2rating = {}
        # Map: cuisine -> heap [(−rating, foodName), ...]
        self.cuisine2heap = defaultdict(list)

        # Khởi tạo dữ liệu
        for f, c, r in zip(foods, cuisines, ratings):
            self.food2cuisine[f] = c
            self.food2rating[f] = r
            # Heap để tìm max rating (dùng -r để giả lập max heap)
            heapq.heappush(self.cuisine2heap[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        # Cập nhật rating mới nhất cho món ăn
        self.food2rating[food] = newRating
        # Lấy cuisine của món ăn
        c = self.food2cuisine[food]
        # Thêm phiên bản mới vào heap (lazy deletion: không xóa bản cũ)
        heapq.heappush(self.cuisine2heap[c], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine2heap[cuisine]
        while heap:
            rneg, name = heap[0]   # lấy phần tử trên cùng (max rating)
            # Kiểm tra xem có phải rating hiện tại không
            if -rneg == self.food2rating[name]:
                return name  # đúng bản mới nhất -> trả về tên
            # Nếu sai (phiên bản cũ) -> loại bỏ
            heapq.heappop(heap)
        return ""  # không có món ăn nào (trường hợp hiếm)












# Rồi 👍 mình sẽ giải thích chi tiết thuật toán trong code Python bạn gửi nhé:

# ---

## Ý tưởng chính

# Bạn cần một hệ thống:

# * Quản lý **món ăn** → có tên, loại ẩm thực (*cuisine*), và điểm đánh giá (*rating*).
# * Cho phép **đổi điểm** của một món ăn (`changeRating`).
# * Tìm **món ăn có rating cao nhất** trong một cuisine (`highestRated`).

#   * Nếu nhiều món cùng rating cao nhất → chọn món có **tên nhỏ hơn theo alphabet**.

# ---

# ## Các cấu trúc dữ liệu

# Trong code bạn dùng 3 cái map + heap:

# 1. `food2cuisine`: ánh xạ *tên món ăn → cuisine*.
#    👉 Dùng để biết món ăn thuộc cuisine nào.

# 2. `food2rating`: ánh xạ *tên món ăn → rating hiện tại*.
#    👉 Dùng để kiểm tra "phiên bản mới nhất" của rating khi lấy từ heap.

# 3. `cuisine2heap`: ánh xạ *cuisine → heap* chứa nhiều phiên bản `(−rating, foodName)`.
#    👉 Heap luôn đưa phần tử có rating cao nhất (vì `−rating` biến max thành min-heap).
#    👉 Nếu rating bằng nhau, heap sẽ so sánh tên (string so sánh theo alphabet).

# ---

# ## Hàm `changeRating(food, newRating)`

# * Cập nhật `food2rating[food] = newRating`.
# * Lấy cuisine của món ăn từ `food2cuisine`.
# * Đẩy một bản ghi mới `(−newRating, food)` vào heap.
#   👉 Heap bây giờ có thể chứa nhiều **phiên bản cũ** của cùng một món (lazy deletion).

# ---

# ## Hàm `highestRated(cuisine)`

# * Lấy heap của cuisine.
# * Lặp:

#   * Xem phần tử trên đỉnh `(−rating, name)`.
#   * Kiểm tra rating hiện tại trong `food2rating[name]`.

#     * Nếu bằng nhau → đây là bản mới nhất → **trả về name**.
#     * Nếu khác → bản cũ → bỏ (`heapq.heappop`).
#       👉 Nhờ cách này mà không cần xóa từng bản cũ trong heap khi `changeRating`.

# ---

# ## Tại sao dùng lazy deletion?

# * Nếu bạn muốn "cập nhật" trực tiếp heap thì phải tìm và sửa phần tử trong heap → **rất tốn chi phí** (O(n)).
# * Dùng lazy deletion: chỉ thêm bản mới vào heap (O(log n)), khi cần thì loại bỏ bản cũ.
#   👉 Đây là thủ thuật thường dùng trong LeetCode khi thao tác với heap.

# ---

## Độ phức tạp

# * `changeRating`: O(log n) để push vào heap.
# * `highestRated`: Trung bình O(log n) (có thể bỏ vài phần tử cũ, nhưng mỗi phần tử bị pop nhiều nhất một lần).
# * Bộ nhớ: O(n), vì mỗi lần change sẽ thêm một node vào heap (bản cũ không xóa ngay).

# ---

# 📌 Tóm lại:
# Thuật toán này quản lý nhiều phiên bản rating của món ăn trong heap (lazy deletion). Khi query, nó đảm bảo luôn trả về bản mới nhất bằng cách kiểm tra lại với `food2rating`.

# ---

# Bạn có muốn mình vẽ một **timeline ví dụ** (thêm vài món, đổi rating, rồi query) để thấy rõ "lazy deletion" hoạt động như thế nào không?

# import java.util.*;

# public class b39 {
#     static Scanner sc = new Scanner(System.in);

#     // Lớp Food: lưu thông tin của một món ăn
#     static class Food {
#         String name; // tên món ăn
#         String cuisine; // loại ẩm thực
#         int rating; // điểm đánh giá

#         Food(String name, String cuisine, int rating) {
#             this.name = name;
#             this.cuisine = cuisine;
#             this.rating = rating;
#         }
#     }

#     // Map ánh xạ từ tên món ăn -> đối tượng Food (luôn chứa rating MỚI NHẤT)
#     private Map<String, Food> foodMap;

#     // Map ánh xạ từ cuisine -> max heap các món ăn
#     private Map<String, PriorityQueue<Food>> cuisineToMaxHeap;

#     // Constructor
#     public b39(String[] foods, String[] cuisines, int[] ratings) {
#         foodMap = new HashMap<>();
#         cuisineToMaxHeap = new HashMap<>();

#         for (int i = 0; i < foods.length; i++) {
#             Food food = new Food(foods[i], cuisines[i], ratings[i]);
#             foodMap.put(foods[i], food);

#             cuisineToMaxHeap
#                     .computeIfAbsent(cuisines[i], k -> new PriorityQueue<>(
#                             (a, b) -> {
#                                 if (b.rating != a.rating) {
#                                     return b.rating - a.rating; // rating cao hơn trước
#                                 }
#                                 return a.name.compareTo(b.name); // tie-break bằng tên
#                             }))
#                     .add(food);
#         }
#     }

#     // Đổi rating cho một món ăn
#     public void changeRating(String foodName, int newRating) {
#         Food oldFood = foodMap.get(foodName);
#         Food updatedFood = new Food(foodName, oldFood.cuisine, newRating);
#         foodMap.put(foodName, updatedFood);
#         cuisineToMaxHeap.get(oldFood.cuisine).add(updatedFood);
#     }

#     // Lấy món ăn rating cao nhất của một cuisine
#     public String highestRated(String cuisine) {
#         PriorityQueue<Food> pq = cuisineToMaxHeap.get(cuisine);

#         while (!pq.isEmpty()) {
#             Food top = pq.peek();
#             Food latest = foodMap.get(top.name);

#             if (top.rating == latest.rating) {
#                 return top.name; // đúng version mới nhất
#             } else {
#                 pq.poll(); // bỏ version cũ
#             }
#         }
#         return "";
#     }

#     // ================== MAIN ==================
#     public static void main(String[] args) {
#         System.out.print("Nhập số món ăn: ");
#         int n = sc.nextInt();
#         sc.nextLine(); // bỏ xuống dòng

#         String[] foods = new String[n];
#         String[] cuisines = new String[n];
#         int[] ratings = new int[n];

#         for (int i = 0; i < n; i++) {
#             System.out.print("Tên món ăn: ");
#             foods[i] = sc.nextLine();
#             System.out.print("Loại ẩm thực: ");
#             cuisines[i] = sc.nextLine();
#             System.out.print("Rating: ");
#             ratings[i] = sc.nextInt();
#             sc.nextLine(); // bỏ xuống dòng
#         }

#         // Tạo hệ thống FoodRatings
#         b39 fr = new b39(foods, cuisines, ratings);

#         // Test chức năng
#         String queryCuisine = sc.nextLine();
#         System.out.println(queryCuisine + ": " + fr.highestRated(queryCuisine));

#         String foodToChange = sc.nextLine();
#         int newRating = sc.nextInt();
#         sc.nextLine();
#         fr.changeRating(foodToChange, newRating);

#         System.out.println(
#                 queryCuisine + ": " + fr.highestRated(queryCuisine));
#     }
# }
# // Ok👍

# // mình giải
# // thích chi
# // tiết thuật
# // toán của class`FoodRatings`
# // này nhé:

# // ---

# // ##
# // Ý tưởng
# // tổng quan

# // Bài toán
# // yêu cầu:

# // 1.
# // Quản lý**món ăn**(`food`)với:

# // *

# // tên (`name`)
# // * loại ẩm thực (`cuisine`)
# // * điểm đánh giá (`rating`).
# // 2. Hỗ trợ:

# // * **changeRating(food, newRating)** → cập nhật điểm của món ăn.
# // * **highestRated(cuisine)** → trả về tên món ăn có rating cao nhất của 1
# // cuisine, nếu trùng thì chọn tên **từ điển nhỏ nhất**.

# // \=> Giải pháp dùng:

# // * HashMap để tra cứu nhanh món ăn.
# // * PriorityQueue (max-heap) để lấy nhanh nhất món ăn có rating cao nhất theo
# // từng cuisine.

# // ---

# // ## Các cấu trúc dữ liệu

# // 1. **`foodMap`**:
# // `Map<String, Food>`

# // * key = tên món ăn
# // * value = đối tượng `Food` (lưu tên, cuisine, rating hiện tại)
# // → giúp tìm nhanh thông tin món ăn theo tên.

# // 2. **`cuisineToMaxHeap`**:
# // `Map<String, PriorityQueue<Food>>`

# // * key = tên cuisine
# // * value = max-heap (ưu tiên rating cao nhất, nếu bằng nhau thì theo tên từ
# // điển nhỏ nhất).
# // → giúp lấy nhanh món ăn cao điểm nhất trong cuisine.

# // ---

# // ## Thuật toán từng hàm

# // ### 1. **Constructor**

# // ```java
# // for (int i = 0; i < foods.length; i++) {
# // Food food = new Food(foods[i], cuisines[i], ratings[i]);
# // foodMap.put(foods[i], food);

# // cuisineToMaxHeap
# // .computeIfAbsent(cuisines[i], k -> new PriorityQueue<>(...))
# // .add(food);
# // }
# // ```

# // * Tạo `Food` cho mỗi món.
# // * Lưu vào `foodMap`.
# // * Thêm vào heap ứng với cuisine.
# // Heap sắp xếp theo:

# // * `rating` giảm dần
# // * nếu bằng thì `name`

# // tăng dần (so sánh chuỗi).

# // ---

# // ### 2. **changeRating(foodName, newRating)**

# // ```java
# // Food oldFood = foodMap.get(foodName);
# // Food updatedFood = new Food(foodName, oldFood.cuisine, newRating);

# // foodMap.put(foodName, updatedFood);
# // cuisineToMaxHeap.get(oldFood.cuisine).add(updatedFood);
# // ```

# // * Lấy món ăn cũ ra.
# // * Tạo `Food` mới với rating mới.
# // * Cập nhật vào `foodMap`.
# // * Đưa bản ghi mới vào heap.

# // 👉 **Lazy deletion**: không xóa bản cũ

# // khỏi heap (vì `PriorityQueue` không hỗ trợ remove nhanh). Thay vào đó, giữ
# // nguyên. Khi gọi `highestRated`, mình sẽ bỏ qua bản ghi cũ.

# // ---

# // ### 3. **highestRated(cuisine)**

# // ```java
# // PriorityQueue<Food> pq = cuisineToMaxHeap.get(cuisine);

# // while (!pq.isEmpty()) {
# // Food top = pq.peek();
# // Food latest = foodMap.get(top.name);

# // if (top.rating == latest.rating) {
# // return top.name;
# // } else {
# // pq.poll(); // bỏ bản cũ (rating không khớp)
# // }
# // }
# // return "";
# // ```

# // * Lấy top

# // của heap (rating cao nhất).
# // * Kiểm tra xem nó có phải bản mới nhất trong `foodMap` không.

# // * Nếu `rating` khớp → trả về tên món.
# // * Nếu không → bỏ bản cũ (poll) và tiếp tục.
# // * Vì mỗi lần `changeRating` thêm bản mới, heap có thể chứa nhiều bản cũ. Vòng
# // lặp sẽ dọn dần khi cần.

# // ## Độ phức tạp

# // * **changeRating**: `O(log n)` (thêm vào heap).
# // * **highestRated**: trung bình `O(log n)` (bỏ các bản cũ), worst-case có thể
# // nhiều stale nhưng vẫn chấp nhận được vì mỗi bản stale chỉ bị bỏ **một lần duy
# // nhất**.
# // // * Bộ nhớ: `O(n)`.

# // ---

# // 👉 Nói ngắn gọn:

# // * Dùng **HashMap** để lưu bản mới nhất.
# // * Dùng **PriorityQueue** để tìm nhanh nhất món cao điểm.
# // * Dùng **lazy deletion** để xử lý khi rating thay đổi.

# // ---

# // Bạn có muốn mình vẽ sơ đồ luồng

# // dữ liệu (foods → foodMap → heaps) để dễ hình dung hơn không?

# // Ok,
# // mình giải
# // thích bài**LeetCode 2353–
# // Design a
# // Food Rating System**
# // cho bạn nha👍

# // ---

# // ###**
# // Đề bài**

# // Bạn cần
# // thiết kế
# // một hệ
# // thống đánh
# // giá món

# // ăn (**Food Rating System**) với các chức năng sau:

# // * Có một danh sách các món ăn, mỗi món ăn thuộc về **một loại ẩm thực**
# // (cuisine) và có một **điểm đánh giá** (rating).
# // * Hệ thống phải hỗ trợ 3 thao tác:

# // 1. **`FoodRatings(String[] foods, String[] cuisines, int[] ratings)`**

# // * Khởi tạo hệ thống với:

# // * `foods[i]` là tên món ăn thứ `i`.
# // * `cuisines[i]` là loại ẩm thực của `foods[i]`.
# // * `ratings[i]` là điểm đánh giá của `foods[i]`.

# // 2. **`void changeRating(String food, int newRating)`**

# // * Cập nhật lại điểm số (`rating`) của món ăn `food` thành `newRating`.

# // 3. **`String highestRated(String cuisine)`**

# // * Trả về **tên món ăn có điểm đánh giá cao nhất** trong loại ẩm thực
# // `cuisine`.
# // * Nếu có nhiều món ăn có cùng điểm cao nhất → trả về **tên món ăn nhỏ nhất
# // theo thứ tự từ điển** (lexicographically smallest).

# // ---

# // ### **Ví dụ**

# // Input:

# // ```text
# // ["FoodRatings", "highestRated", "highestRated", "changeRating",
# // "highestRated", "changeRating", "highestRated"]
# // [[["kimchi","miso","sushi","moussaka","ramen","bulgogi"],
# // ["korean","japanese","japanese","greek","japanese","korean"],
# // [9,12,8,15,14,7]],
# // ["korean"], ["japanese"], ["sushi",16], ["japanese"], ["ramen",16],
# // ["japanese"]]
# // ```

# // Output:

# // ```text
# // [null, "kimchi", "ramen", null, "sushi", null, "ramen"]
# // ```

# // **Giải thích:**

# // * Ban đầu:

# // * `kimchi (korean, 9)`
# // * `miso (japanese, 12)`
# // * `sushi (japanese, 8)`
# // * `moussaka (greek, 15)`
# // * `ramen (japanese, 14)`
# // * `bulgogi (korean, 7)`

# // 1. `highestRated("korean")` → **kimchi** (9 cao nhất trong korean).
# // 2. `highestRated("japanese")` → **ramen** (14 > 12 > 8).
# // 3. `changeRating("sushi", 16)` → sushi update lên 16.
# // 4. `highestRated("japanese")` → **sushi** (16 cao nhất).
# // 5. `changeRating("ramen", 16)` → ramen update lên 16.
# // 6. `highestRated("japanese")` → sushi và ramen đều 16 → **ramen** thắng vì từ
# // điển nhỏ hơn.

# // ---

# // ### **Ý tưởng giải**

# // * Cần lưu trữ mối quan hệ:

# // * `food → (cuisine, rating)`
# // * `cuisine → danh sách các món ăn`
# // * Khi `changeRating`, cập nhật rating cho món ăn.
# // * Khi `highestRated`, tìm món ăn có rating cao nhất trong cuisine đó.
# // Để tối ưu:

# // * Dùng **Heap (PriorityQueue)** hoặc **TreeSet** để quản lý món ăn trong mỗi
# // cuisine.
# // * Ưu tiên `(-rating, name)` để vừa đảm bảo rating giảm dần, vừa lấy từ điển
# // nhỏ nhất.

# // ---

# // 👉 Bạn có muốn mình viết code Java/Python mẫu và chú thích chi tiết cách cài
# // đặt không?
