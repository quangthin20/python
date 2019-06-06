"""     Hàm trong python - Phần 1
Cú pháp: def <Tên_hàm> (parameter1,parameter2,....):
            block-function
"""
#Ví dụ 1: Định nghĩa hàm cộng 2 số
def add(a,b):
    s = a + b
    return s
a = 10
b = 5
print(add(a,b))

#Ví dụ 2:
def QuangThin(hometown,greet,age=19):
    print(hometown)
    print(age)
    print(greet+"!")
QuangThin('Hue','Hello',20)
'''Lưu ý: Đối số mặc định được định nghĩa trên hàm phải để cuối cùng của hàm
Tuy nhiên vẫn có thể thay đổi được nội dung của đối số mặc định, xem ví dụ trên
Khi chưa định nghĩa hàm được, ta có thể dùng pass để chạy chương trình không bị lỗi, xem ví dụ dưới'''
def whatIsTheLove(you,I):
    pass
'''Như các bạn đã biết, unhashable container phổ biến mà ta đã từng biết như
LIST, DICT, SET. Ở đây có một cảnh báo cho bạn việc bạn sử dụng default
argument cho parameter là một unhashable container đó là giá trị của nó
không được làm mới (refresh) sau mỗi lần gọi hàm mà không pass argument
mới cho parameter đó. Đương nhiên là nếu bạn có pass cho nó một argument
mới thì container đó vẫn không hề mất giá trị nếu lần sau bạn gọi nó.
'''
# Ví dụ:
def repeat(list_ = []):
    list_.append('Xìn')
    print(list_)
repeat()
repeat()
repeat()