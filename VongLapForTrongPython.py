'''Vòng lặp for trong python
Cú pháp:
for var1,var2,... in sequency:
    <block>
'''
# Ví dụ:
iter_ = (x for x in range(4))  # 0,1,2,3
for value in iter_:
    print("->", value)
dic = {'name': "TQT", 'age': 19, 'hometown': 'Hue'}
dic['Hobby'] = 'Code'
dic['Program Languague'] = 'Python'
list_item = list(dic.items())
print(list_item)
#Cách vòng lặp duyệt 1 dict
for key, value in list_item:
    print(key, "->", value)
#Lệnh break 
''' Cú pháp:
for var1,var 2,... in sequence:
    <block>
    break
Ý nghĩa: dừng vòng lặp trong nhất chứa nó
'''
#Ví dụ: Tìm n nhỏ nhất trong khoảng 1 đến 99 sao cho s = 1+2+3+...+n <1000
s = 0
for i in range(1,1000):
    s+=i
    if s>1000:
        print(i-1)
        break
#Lệnh break 
''' Cú pháp:
for var1,var 2,... in sequence:
    <block>
    continue
Ý nghĩa: bỏ qua các lệnh sau continue và thực hiện lại vòng lặp
'''
# Ví dụ: 9!! (1x3x5x7x9)
giaithua = 1
for i in range(1,10):
    if i%2==0:
        continue
    giaithua*=i
print(giaithua)
# for - else:
#Ví dụ:
iter1 = (x for x in range(3))  # 0,1,2
for value in iter1:
    print("->", value)
else:
    print("Done")
print("-"*45)
'''
Vòng lặp for trong python - Phần 2
'''
# kiểu dữ liệu range (dãy số)
#cú pháp: range(start,stop,step), trong đó step = stop - 1
a = range(10)
print(list(a)) #In ra 10 số đầu tiên, mặc định start = 0
b = range(1,10)
print(list(b)) #In ra số từ 1 đến 9
c = range(10,0,-1)
print(list(c)) #In ra số từ 10 đến 1, (-1 là đảo ngược)
# Toán  tử in : Kiểm tra phần tử có trong range
print(c in b)
#Sử dụng range để duyệt list, tuple, Chuỗi
list_ = ["Quang Thìn", (20,15),{"Duy Tan","Da Nang"}]
for i in range(len(list_)):
    print(list_[i])
''' 
Sự khác nhau giữa sequence scan, indexing scan
Bản chất: indexing scan có thể update được dữ liệu
'''
# Ví dụ: sequence scan
danh_sach = [1,2,3]
for value in danh_sach:
    value+=1
print(danh_sach)
# Ví dụ: indexing scan
for value in range(len(danh_sach)):
    danh_sach[value]+=10
print(danh_sach)
'''Comprehension
Cú pháp: [output-expression for statement optional predicate]
Có thể hiểu: output - expression là khối lệnh, statement:các biến, optional predicate: điều kiện 
'''
# Ví dụ: in ra ước của 3 trong khoảng (1;100)
data_ = [var for var in range(1,101) if var%3==0]
print(data_)
# Ví dụ: In ra lập phương của các số từ 10 đến 20 trong dict
danh_sach1 = {k:k**2 for k in range(10, 21)}
print(danh_sach1)
# hàm enumerate . Cú pháp. enumerate(iterable,start) *start mặc định bằng 0
# Ý nghĩa: đánh số 
friend_list = ["Nhiên", "Chi","Tú Uyên","Kiều Loan"]
for index,friend in enumerate(friend_list,10):
    print(index,"=>",friend)
