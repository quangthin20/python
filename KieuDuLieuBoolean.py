'''Kiểu dữ liệu Boolean trong python
Boolean là kiểu dữ liệu chỉ có 2 giá trị True/False
'''
# So sánh giữa các số
num1 = 12**13
num2 = 13**12
print("num1 =", num1)
print("num2 =", num2)
print(num1 > num2)
print(num1 <= num2)
print(num1 != num2)
print('_'*45)
# So sánh chuỗi
str1 = "QuangThinDepTrai"
str2 = "QTDT"
print(str1 > str2)
print('_'*45)
print(ord('u'), end="||")
print(ord('T'))
print('_'*45)
# Toán tử is
# Cần phân biệt toán tử is và ==, is : là ; == : bằng
# Ví dụ
list_ = [1, 2, 3]
list_1 = [1, 2, 3]
print(list_ == list_1)  # Hai list bằng nhau
print(list_ is list_1)  # list_ ko phải là list_1
# Để list_1 is list_ ta làm như sau
list_1 = list_
print(list_ is list_1)
''' chú ý: 
+ khi so sánh == thì nó sẽ so sánh giá trị
+ khi dùng toán tử is thì nó sẽ get ID để so sánh
+ Các số từ -4 đến 255 hoặc 1 chuỗi có ít hơn 20 kí tự thì có cùng ID
'''
print('_'*45)
#NOT, AND, OR
# NOT : không (phủ định)
print(not(5 > 6))
print('_'*45)
# AND: và. Xem bảng sau:
'''
| Left value | Right value | Result |
|------------|-------------|--------|
|   True     |  True       |  True  |
|------------|-------------|--------|
|   True     |  False      |  False |
|------------|-------------|--------|
|   False    |  True       |  False |
|------------|-------------|--------|
|   False    |  False      |  False |
|------------|-------------|--------|
Ngoài ra còn có thể mở rộng cho 3,4,... các value
'''
print("_"*45)
print(1 < 2 and 3 < 5)  # Trường hợp True | True
print(3 > 1 and 10 > 11)  # Trường hợp True/False
print(3 > 4 and 10 < 11)  # Trường hợp False/True
print(3 > 4 and 10 > 11)  # Trường hợp False/False
# Trường hợp mở rộng
print(1 < 2 < 4 < 5 < 7 < 10 > 8)
# OR: hoặc. Xem bảng sau
'''
| Left value | Right value | Result |
|------------|-------------|--------|
|   True     |  True       |  True  |
|------------|-------------|--------|
|   True     |  False      |  True  |
|------------|-------------|--------|
|   False    |  True       |  True  |
|------------|-------------|--------|
|   False    |  False      |  False |
|------------|-------------|--------|
Ngoài ra còn có thể mở rộng cho 3,4,... các value
'''
print('_'*45)
print(1 < 2 or 3 < 5)  # Trường hợp True | True
print(3 > 1 or 10 > 11)  # Trường hợp True/False
print(3 > 4 or 10 < 11)  # Trường hợp False/True
print(3 > 4 or 10 > 11)  # Trường hợp False/False
'''
Các giá trị cũng là boolean
Ngoài trừ 0, None, Rỗng là False
Còn lại là True
'''
# Ví dụ:
print("_"*45)
print(bool(1))
print(bool([]))
print(bool(None))
# Syntaxnic sugar
print('_'*45)
x = 6
print(4<=x<10)
print (x in(3,6))