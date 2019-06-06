'''Xử lý file trong python
File có hai loại:
+ Text File 
+ File nhị phân
'''
# Để mở một file, ta dùng hàm open
# Cú pháp: open(file, mode = '?')
'''
? có thể là: 
- r: Mở để đọc, đây là mode mặc định
- r+: Mở để đọc và ghi
- w: Mở để ghi, xóa hết nội dung file hiện có, ko có sẽ tạo mới
- w+: mở để ghi và đọc,xóa hết nội dung file hiện có, ko có sẽ tạo mới
- a: Mở để ghi, ko có sẽ tạo mới
- a+: Mở để ghi và đọc, ko có sẽ tạo mới
'''
# Mở file
file_object = open("QuangThin.txt", mode="r", encoding="utf-8")
# Đọc file: cú pháp: <file>.read
data = file_object.read()
print(data)
'''
Phương thức readline. cú pháp. <file>.readline(size=)
#data1= file_object.readline()
#print(data1)

Phương thức readlines. cú pháp <file>.readlines(hint=-1)

file_obj = file_object.readlines()
print(file_obj)
# Đóng file: cú pháp. <file>.close()
'''
file_object.close()
