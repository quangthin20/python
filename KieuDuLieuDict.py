'''
Kiểu dữ liệu Dict trong python
Dict (Dictionary) là một kiểu dữ liệu container. Dùng key đê phần biệt
Một dict gồm các yếu tố sau:
+ Được giới hạn trong cặp dấu ngoặc nhọn {}
+ Các phần tử cách nhau bởi dấu ,
+ Các phần tử phải là một cặp key-value
+ Các key-value ngăn cách nhau bởi dấu :
+ Các key phải là một hash object
'''
#================================================================================

#Phần 1:
#Cách khởi tạo dict: <biến> = {key1:value1,key2:value2,....}
dic = {'name':"TQT",'age':19,'hometown': 'Hue'}
print(dic)
#Khởi tạo dict rỗng
empty_dic = {}
print(empty_dic)
#Sử dụng comprehension
dic1 = {key: value for key, value in [('name','TQT'),('age',19),('hometown','Hue')]}
print(dic1)
#Sử dụng contructor
'''Có 4 cách khởi tạo Dict bằng contructors'''
#Khởi tạo dict rỗng
emp_dic = dict()
print(emp_dic)
'''
#===================================================================
#BÀI HÀM SẼ RÕ
#Khởi tạo dict từ một mapping object
class Map_Class:
    def key(seft):
        return[1,2,3]
    def __getitem__(seft,key):
        return key*2
map_obj = Map_Class()
dic_ = dict(map_obj)
print(dic_)
#=====================================================================
'''
iter_ = [('Name','QT'),('age',19),('Hometown','TTHue')]
dic2 = dict(iter_)
print(dic2)
#dict(**kwargs), không làm thay đổi biến khai báo ban đầu
name = 'Q.Thin'
birth = '20/03/2000'
home = 'Hue'
dic3 = dict(name='Kieu Loan',birth='23/02/2000',home='Quang Nam')
print(name,birth,home)
#Sử dụng phương thức fromkeys
#Ý nghĩa: tạo ra một dict với các keys nằm trong 1 iterable
iter1 = ('name','luvnum')
#tạo ra một dict gồm các key và value mặc định bằng None
dic_none = dict.fromkeys(iter1)
print(dic_none)
#Tham chiếu giá trị của key và chỉnh sửa value
dic_none['name'] = 'Kieu Loan'
dic_none['luvnum'] = 97
print(dic_none)
#Thêm phần tử vào dict
dic_none['age'] = 19
print(dic_none)
#=================================================================================
#Phần 2:
'''Các phương thức trong dict'''
#1. Phương thức copy. cú pháp <dict>.copy()
#Ý nghĩa: copy dict
dic4 = dic3.copy()
print(dic4)
#2. Phương thức clear. cú pháp <dict>.clear()
#Ý nghĩa: xóa mọi phần tử trong dict, dict trả về là dict rỗng
dic4.clear()
print(dic4)
#Các phương thức xử lý
#3. Phương thức get. Cú pháp: <dict>.get(key[default])
#Ý nghĩa: lấy ra key. nếu key không có trong dict thì trả về default, mặc định là None, có thể thay đổi default
dic5 = dic3.get('archive',"Miss UDN")
print(dic5)
#4. Phương thức items. cú pháp <dict>.items()
#Ý nghĩa: trả về một lớp gồm các tuple, giá trị 1 là key, giá trị 2 là value
dic6 = dic3.items()
print(dic6)
print(type(dic6)) #type của dic6, là một dict_items
list_items = list(dic6) #đưa dic6 về list
print(list_items[1][1]) #Xuất ra phần tử 1;1

