'''
Kiểu dữ liệu Tuple trong python
Đặc điểm:
+ Được giới hạn trong cặp dấu ngoặc tròn ()
+ Được ngăn cách nhau bởi dấu ,
+ Có khả năng chứa mọi giá trị, đối tượng trong python
+ Không thể thay đổi dữ liệu trong tuple
'''
#============================================================================
tup = (2,0,3,[2,3,2])
a = tuple(tup)
print(a)
tup1 = ('PGS Xìn')
print(tuple(tup1))
tup2 = (i for i in range(1,10) if i%2==0) #In các số chẵn trong tuple
b = tuple(tup2)
print(b)
#Phướng thức count. cú pháp: <tên_biến>.count(x)
#Trả về số lần xuất hiện của x trong tuple
print("n =",tup.count([2,3,2]))
#Các phương thức khác tương tự chuỗi trong python, xem lại Chuỗi trong python
'''
Chú ý: Khi nào nên sửa dụng Tuple
* Tốc độ truy suất của tuple nhanh hơn list
* Dung lượng chiếm ít bộ nhớ hơn list
* Tốc độ nhanh hơn
* Bảo vệ dữ liệu sẽ không thay đổi
* Có thể làm key ở dictionary
'''