'''Kiểu dữ liệu Function trong Python - Biến locals và globals'''

name = 'Xìn'  # Biến toàn cục có thể sử dụng trong hàm


def callName():
    print('My name is', name)


callName()
# Giờ hãy thử biến trong hàm dùng cho toàn cục
'''def callMyName():
    myname = 'Trần Quang Thìn'
print("Tên tôi là:",myname)'''
# Lỗi ngay: NameError: name 'myname' is not defined : tên myname không được định nghĩa

'''Thay đổi giá trị argument gián tiếp qua parameter'''

'''
pass by reference
(Tham chiếu)
'''
# Ví dụ from HowKteam
num = 69
st = 'How Kteam'
lst = [1, 2, 3]
tup = tuple('Education')


def change(parameter):
    parameter = 'New value'


print('Changed successfully!')
change(num)
change(st)
change(lst)
change(tup)
print('*' * 10)
print('{}\n{}\n{}\n{}\n'.format(num, st, lst, tup))

'''pass by Value 
(tham trị)'''
lst_ = ['How Kteam', 1, 2]


def changelist(para):
    para[0] = 1
    print('Changed successfully!')
print(lst_)
changelist(lst_)
print(lst_)
'''Sử dụng lệnh global
Nếu như một biến nằm trong một hàm (như biến kteam trong ví dụ cuối ở
phần đầu) thì người ta hay gọi đó là local variable (biến chỉ có hiệu lực trong
một hàm nhỏ).
Đặt vấn đề là việc khai báo biến ở trong hàm trở nên cần thiết thì sao nhỉ?
Ta được Python hỗ trợ lệnh global
|| Cú pháp: global <variable>
=> Có thể dụng trong hàm để làm biến toàn cục
Tuy nhiên, BẠN KHÔNG NÊN SỬ DỤNG GLOBAL trừ khi hết cách. Nó giống như
hàm eval vậy. Việc sử dụng biến global làm cho chương trình rối, khó
kiểm soát cho nên hạn hãy chế tối đa việc sử dụng
'''
'''Giới thiệu hàm locals và globals'''

'''Cái tên hàm nói lên tất cả. Hàm locals cho ta biết được những biến local
(những biến được khai báo trong hàm) nằm trong chương trình của chúng ta.
Còn globals là hàm giúp chúng ta biết được những biến global trong chương
trình.
Kết quả trả ra của hai hàm này là một Dict. Với key là tên biến và value là giá
trị của biến.
Giới thiệu hàm locals và globals
Cái tên hàm nói lên tất cả. Hàm locals cho ta biết được những biến local
(những biến được khai báo trong hàm) nằm trong chương trình của chúng ta.
Còn globals là hàm giúp chúng ta biết được những biến global trong chương
trình.
Kết quả trả ra của hai hàm này là một Dict. Với key là tên biến và value là giá
trị của biến.'''
locals()
globals()