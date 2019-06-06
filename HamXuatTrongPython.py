''' Tìm hiểu hàm print trong python thông qua các parameter
cú pháp: print(*object,sep=,end=,file=,flush=)
'''
from time import sleep #Nhập hàm sleep từ thư viện time
print('Quang Thìn', '20.03.2000')  # Sử dụng object
print('Quang Thìn', '20/03/2000', sep='||') #sep='' hay đổi giá trị mặc định thành ||
#end='' mặc định là newline \n, có thể thay đổi thành giá trị khác, ví dụ ___
print('Quang Thìn',end='\t')
print('20.03.2000')
print("Tui là:",end=' ')
sleep(2)
print("Trần Thiên Bảo")
#Lý do: xem tài liệu
#Một số ví dụ khác
'''
print("Tui là:",'\n',"Trần Thiên Bảo")
sleep(2)
print("Hay là Jacky")
'''
#file
with open('Q.Thin.txt','w') as f:
    print("Hello Vietnam",file=f)
    print([x for x in range(0,11)],file=f)
#flush
print("Tui là:",end=' ',flush=True)
sleep(2)
print("Trần Thiên Bảo")
