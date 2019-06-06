#=======================================================================
from fractions import Fraction

a = 13 #Gán cho 4 a giá trị 13 là giá trị số nguyên
print(a)
#Kiểu dữ liệu của a
print(type(a))

#=======================================================================

# lấy toàn bộ nội dung của thư viện Decimal
from decimal import*
#Lấy tối đa 10 chữ số thập phân
getcontext().prec = 10
# tính giá trị của b in ra 10 số thập phân
b=Decimal(232/203)
#in kiểu dữ liệu của b
print(type(b))

#=======================================================================

# lấy toàn bộ nội dung của thư viện fractions (Phân số)
from fractions import*

# gán frac cho phân số
frac = Fraction(60,36)
# in giá trị frac
print(frac)
# In kiểu của frac
print(type(frac))

#************************************************************************
# Số phức trong python
#C1: In số thực bình thường
d= 2+3j  #Nhập số phức d
e= 3+2j  #Nhập số phức e
f= d + e   #Tích của số phức d và e
print(f)
print(f.real)   #In phần thực của f
print(f.imag)   #In phần ảo của f
print(type(f))  #In kiểu của f
#C2
g=complex(10,2)
print(g)
#-------------------------------------------------------------------------
#Sử dụng thư viện math
import math
print(math.gcd(30,14))
#=============================================================================
print("-"*40)
print("Bài tập củng cố:")
