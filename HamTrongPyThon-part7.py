'''KIỂU DỮ LIỆU FUNCTION – FUNCTIONAL TOOLS'''
#HÀM MAP trong python
# Cú pháp: map(func, iterable)
#Ví dụ:
func = lambda x:x**2 #tạo ra 1 function 
kteam = [1,2,3,4] #iterable
print(list(map(func,kteam)))
# Nhiều iterable khác nhau, nhưng phải cùng số phần tử
#Ví dụ:
add = lambda x,y,z: x+y*z 
list_1 = [1,2,3,4]
list_2 = [2,3,4,5]
list_3 = [3,4,5,6]
print(list(map(add,list_1,list_2,list_3)))
#KQ trả ra: [7,14,23,34]
#Hàm Filter
#Cú pháp: filter(function or None, iterable)
#Ví dụ: 
listNum = [-9,-7,-5,3,4,6,12]
div3 = lambda x: x%3==0
print(list(filter(div3,listNum)))
#Kết quả trả ra: [-9,3,6,12]