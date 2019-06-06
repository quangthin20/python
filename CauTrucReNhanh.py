'''
Cấu trúc rẽ nhánh trong python
if, elif, else
'''
import math

# Bài tập: Nhập 3 số a,b,c. Tìm max
num1 = int(input("Nhập số 1:"))
num2 = int(input("Nhập số 2:"))
num3 = int(input("Nhập số 3:"))
if num2>num1:
    max = num2
else:
    max = num1
if num3 > max:
    max = num3
print("max =",max)
print("_"*45)
# Giải phương trình bậc nhất ax+b=0
a = float(input("Nhập a:"))
b = float(input("Nhập b:"))
if b > 0:
    c = '+'
else:
    c = '-'
print("Phương trình {0}x {1} {2} = 0".format(a, c, abs(b)))
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    print("Phương trình có nghiệm x =", -b/a)
print("_"*45)
# Giải phương trình bậc 2: mx^2+nx+p=0
m = float(input("Nhập m:"))
n = float(input("Nhập n:"))
if n > 0:
    o1 = '+'
else:
    o1 = '-'
p = float(input("Nhập p:"))
if p > 0:
    o2 = '+'
else:
    o2 = '-'
print("Phương trình {0}x^2 {1} {2}x {3} {4}=0".format(m, o1, abs(n), o2, abs(p)))
if m == 0:
    if n == 0:
        if p == 0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print("Phương trình có nghiệm x =", -n/p)
else:
    dt = n*n - 4*m*p
    if dt < 0:
        print("Phương trình vô nghiệm")
    elif dt == 0:
        print("Phương trình có 1 nghiệm kép:", -n/2/m)
    else:
        x1 = (-n+math.sqrt(dt))/2/m
        x2 = (-n-math.sqrt(dt))/2/m
        print("Phương trình có 2 nghiệm x1 = {0} và x2={1}".format(x1, x2))
print("_"*45)
# Giải hệ phương trình {u1x + v1y = t1
#                      {u2x + v2y = t2
u1 = float(input("Nhập u1:"))
u2 = float(input("Nhập u2:"))
v1 = float(input("Nhập v1:"))
v2 = float(input("Nhập v2:"))
t1 = float(input("Nhập t1:"))
t2 = float(input("Nhập t2:"))
D = u1*v2 - u2*v1
Dx = t1*v2 - t2*v1
Dy = u1*t2 - u2*t1
if D!=0:
    x = Dx/D
    y = Dy/D
    print("Hệ phương trình có nghiệm ({0};{1})".format(x,y))
else:
    if (Dx == 0 & Dy == 0):
        print("Hệ phương trình có vsn")
    else:
        print("Hệ phương trình vô nghiệm")
