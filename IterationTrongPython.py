#Khái niệm ITERATOR OBJECT: đọc tài liệu
data = [x for x in range(1,6)]
print(data)
itor = (x for x in range(1,6)) #Tạo ra một iterator
#Sử dụng next để in từng phần tử, nếu quá sẽ báo lỗi
print(next(itor))
print(next(itor))
print(next(itor))
print(next(itor))
print(next(itor))
''' Lưu ý: Iterator cũng chỉnh 1 đổi 2'''
''' *Một số hàm hỗ trợ cho iterable object'''
# Hàm tính tổng: cú pháp. sum([i,j,k,....],start = n) 
# Ý nghĩa: trả về tổng của các số trong hàm, cộng bắt đầu từ n, mặc định là 0
it_sum = sum([x for x in range(1,6)],10)
print(it_sum)
# Hàm tìm giá trị lớn nhất. cú pháp: max([i,j,k,....],*default ='X')
# Ý nghĩa: trả về số lớn nhất trong hàm, nếu ko có trả về giá trị X
it_max = max([1,2,4,5,9],default=6)
print(it_max)
#Hàm min tương tự max
it_min = min([1,2,4,5,9],default=6)
print(it_min)
#Hàm sorted, cú pháp sorted([i,j,k,....],reverse = True/False)
#Ý nghĩa: Trả về 1 list đã được sắp xếp, True: giảm dần, False tăng dần
it_sort = sorted([1,2,5,4,6,1,2,4,8],reverse=True)
print(it_sort)
