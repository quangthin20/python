'''Hàm trong python - Phần 3
Kiểu dữ liệu Function trong
Python - Packing và unpacking arguments.
Trong bài này, chúng ta sẽ cùng tìm hiểu những nội dung sau đây:
 Unpacking arguments với *
 Packing arguments với *
 Unpacking arguments với **
 Packing arguments với **'''

# 1. Unpacking arguments với *


def inputValue(a, b, c, d, e, f):
    print(a, b, c)
    print(d)
    print(e, f)


list_ = ['Thìn', 'Huế', '20032000', '13', 'Duy Tan', 'CNTT']
inputValue(*list_)
# Dùng * để input tuần tự vào hàm, việc này sẽ tiết kiệm công sức và thời gian so với input từng giá trị vào
'''Khi bạn sử dụng *, bạn không chỉ có thể unpack được các List mà bên cạnh
đó bạn có thể unpack các container khác như Tuple, Chuỗi, Generator, Set,
Dict (chỉ lấy được key'''
# Unpack 1 dict
dict_ = {'name': 'Thìn', 'home': 'Huế', 'birthday': '20032000',
         'luvnum': '13', 'university': 'Duy Tan', 'major': 'CNTT'}
inputValue(*dict_)
'''Pass argument bằng cách unpacking argument như thế này là đang truyền
vào dưới dạng positional argument. Hãy cẩn thận sử dụng kĩ thuật này với
những hàm có parameter dạng keyword-only argument.'''
# Ví dụ:
"""def ABC(*,m,n):
    print(m,n)
ABC(5,6)
*=> Ta sẽ có lỗi: ABC() takes 0 positional arguments but 2 were given
Sửa lại như sau:"""


def ABC(*, m=5, n=6):
    print(m, n)


ABC(m=6, n=5)
'''Trong trường hợp container của bạn unpack các giá trị có trong container
nhưng vẫn chưa đủ yêu cầu của hàm, thì bạn có thể truyền thêm:'''
# Packing arguments với *
'''Khi bạn sử dụng 'packing argument'. Đồng nghĩa với việc bạn nhờ một biến đi
gói tất cả các giá trị truyền vào cho hàm bằng 'positional argument' thành một
Tuple. Nếu không có gì để gói (bạn không truyền vào bất cứ argument nào)
thì bạn sẽ nhận được một tuple rỗng. Để giao nhiệm vụ cho một biến làm
công việc này, bạn đặt một dấu * trước nó.'''


def XYZ(*args):
    print(args)
    print(type(args))


XYZ(*{x for x in range(10)})
'''Chú ý:
Bạn không nên nhầm lẫn việc này với việc force keyword-only
argument
Không được phép để 2 parameter cùng làm nhiệm vụ packing
argument trong một hàm'''
# 2. Unpacking với **
'''Với Dict, thì nó phức tạp hơn một xíu khi mỗi phần tử là một cặp key và
value. Vậy nên một dấu * là không đủ nội công để unpack hết được các giá
trị. Do đó ta phải nhờ đến một cặp **.
Nếu bạn unpacking một Dictionary để truyền argument vào cho hàm khi gọi
hàm thì đây chính là dạng keyword argument. Vậy nên bạn phải chắc chắn
rằng parameter với key là giống nhau.'''
# Ví dụ:
dic = {'name': 'Quang Thìn', 'age': '19', 'programlang': 'python'}


def getData(name, age, programlang):
    print('name =>', name)
    print('age =>', age)
    print('programlang =>', programlang)


getData(**dic)
# Packing arguments với **
'''Đã có unpacking với ** thì cũng phải có packing. Khác với dấu * là gói những
positional argument thì ** lại gói các keyword argument. Và đương nhiên, nó
sẽ gói trong một Dict. Nếu không truyền gì vào sẽ là một dict rỗng'''


def kteam(**kwargs):
    print(kwargs)
    print(type(kwargs))


kteam(name='Kteam', member=69)


def kter(**kwargs):
    for key, value in kwargs.items():  # phương thức items của kiểu dữ liệu Dict
        print(key, '=>', value)


kter(id=3424, name='Henry', age=18, lang='Python')
'''Lưu ý:
bạn không được phép bỏ các positional parameter sau biến packing
mà có ** giống như với *.'''
