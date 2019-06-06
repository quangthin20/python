"""Phần 2: Hàm trong python
 Kiểu dữ liệu Function trong
Python - Positional và keyword argument.
"""
import math
# Ôn lại,


def TU(a, b):
    pass  # lệnh giữ chỗ khi chưa có code


TU(3, "Thìn")  # 3 và Thìn được xem là positional arg
TU(a=11, b='TU')  # a=11,b='TU' được xem là keyword arg
"""Khi pass argument theo positional argument. Thì các argument sẽ được gán LẦN LƯỢT cho các
parameter. Riêng đối với keyword argument. Bạn đã tự mình gán giá trị cho
các parameter."""


def func(a, b):
    print('a', a)
    print('b', b)


func(a=11, b=3)
func(b=3, a=11)
# ---------------------------------------------------------------------------------
# ==> Không hiểu gì
# Chú ý như thế này: keyword arguments phải nằm sau positional arguments nếu không sẽ lỗi ngay. Xem 2 ví dụ sau
"""def Love(name,verb=like,obj):
    print(name)
    print(verb)
    print(obj)
Love('Thìn','likes','Python')"""
# Dự đoán là lỗi, tên lỗi: non-default argument follows default argument
# Sửa lại như sau:


def Love(name, verb='likes', obj='Python'):
    print(name)
    print(verb)
    print(obj)
Love('Thìn', 'loves', 'R,Python')
'''Trong Python, có một số hàm bắt chúng ta buộc phải pass argument một
cách rõ ràng rành mạch như hàm sorted.'''
data = sorted([2,4,3,1],reverse=True)
print(data)
'''
Ví dụ dưới cho ta thấy, khi gọi hàm, ta có thể bỏ qua 2 keyword argument, nó lấy mặc định khi ta khai báo hàm
'''
def distance(x1,y1,x0=0,y0=0):
    dist = round(math.sqrt((x1-x0)**2+(y1-y0)**2),2)
    print('Khoảng cách giữa 2 điểm ({0};{1}) và ({2};{3}) là: {4}'.format(x1,y1,x0,y0,dist))
distance(2,2)
distance(2,2,1,1)
#Giả sử x0 ta ko muốn thay đổi, nhưng y0 ta muốn thay đổi, khi đó ta sẽ dùng keyword argument, ví dụ bên dưới
distance(1,2,y0=6)
"""Python cho phép chúng ta tạo ra các parameter chỉ nhận giá trị bằng việc
pass argument theo kiểu keyword argument.
Cú pháp
def function (*, key_arg1, key_arg2):
# function-block
Khi tạo một hàm mà có một parameter *. Thì Python sẽ hiểu đó không phải là
parameter mà chính là syntax để rồi nó biến các parameter sau * thành các
keyword only argument (chỉ nhận giá trị theo kiểu keyword argument)"""
#Nói dễ hiểu là sau parameter *, các giá trị tuyền vào phải theo kiểu keyword argument
#Hai ví dụ sau sẽ làm rõ vấn đề
#Ví dụ 1: sau parameter * không có keyword argument, lỗi ngay: Ham() takes 2 positional arguments but 3 were given
'''def Ham(subject,verbs,*,objects):
    print(subject)
    print(verbs)
    print(objects)
    Ham('Thìn','loves','coding')'''
#Ví dụ 2: sửa lại cho đúng
def Ham(subject,verbs,*,objects):
    print(subject)
    print(verbs)
    print(objects)
Ham('Thìn','loves',objects='coding')