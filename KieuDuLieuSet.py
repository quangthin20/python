#Kiểu dữ liệu Set trong python
'''
Set cũng là một container
+ Được giới hạn bằng cặp dấu ngoặc nhọn {}
+ Các phần tử cách nhau bởi dấu phẩy ,
+ Set không chưa hơn 1 phần tử trùng lặp
'''
#Khởi tạo set
set1 = {1,2,3}
print(set1)
set2 = {1,1,2,2,3,3,4}
print(set2)
set3 = {i for i in range(2,10)}
print(set3)
#Contructors
set4 = set((1,3,4,2,1,3))
print(set4)
print(type(set4))
#Một số toán tử với set thông dụng
#Toán tử in. Cú pháp <value> in <biến>
#ý nghĩa: trả về giá trị true nếu có phần tử trong set ngược lại false
a = 5 in set4
print(a)
#Toán tử - . cú pháp: <pre.set> - <next.set>
#Ý nghĩa: Trả về giá trị có trong pre.set mà không có trong next.set
set5 = set2 - set1
print(set5)
#Toán tử &. cú pháp <pre.set> & <next.set>
#Ý nghĩa: Trả về giá trị giao của <pre.set> và <next.set>
set6 = set3 & set2
print(set6)
#Toán tử  |. cú pháp <pre.set> | <next.set>
#Ý nghĩa: Trả về giá trị hợp của <pre.set> và <next.set>
set7 = set3 | set2
print(set7)
#Toán tử ^. cú pháp <pre.set> ^  <next.set>
#Ý nghĩa: Trả về giá trị các phần tử chỉ tồn tại trong <pre.set> và <next.set>
set8 = set3 ^ set2
print(set8)
''' Một số phương thức thường gặp'''
#Phương thức clear. Cú pháp. set.clear().
#Ý nghĩa: xóa mọi phần tử trong set
set8.clear()
print(set8)
#Phương thức clear. Cú pháp. set.copy().
#Ý nghĩa: copy set
set9 = set7.copy()
print(set9)
#Phương thức pop. Cú pháp. set.pop().
#Ý nghĩa: lấy ra phần tử đầu tiên của set
set10 = set7.pop()
print(set7)
print(set10)
#Phương thức remvove. Cú pháp. set.remove(x) và set.discard(x)
#Ý nghĩa: loại bỏ phần tử x, remove ko có sẽ báo lỗi, discard thì không
set7.discard(2)
print(set7)
set7.remove(6)
print(set7)
#Phương thức add/radd. Cú pháp. set.add()
#Ý nghĩa: thêm một phần tử vào set
set7.add(0)
print(set7)