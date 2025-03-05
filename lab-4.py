def truy_cap_phan_tu(tuple_data):
        first_element = tuple_data[0]
        last_element = tuple_data[-1]
        return first_element, last_element
    
    #Nhập  tuple từ người dùng và xử lý chuỗi 
input_tuple = eval(input("Nhập tuple, ví dụ (1,2,3):"))
first , last = truy_cap_phan_tu(input_tuple)

#in kết quả

print("Phần tử đầu:",first)
print("Phần tử cuối:",last)