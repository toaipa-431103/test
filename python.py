# example_with_more_errors.py

def multiply(a, b):
    """Tính tích của hai số."""
    return a * b

def is_even(number):
    """Kiểm tra xem một số có phải là số chẵn hay không."""
    return number % 2 == 0

def print_result(a, b):
    """In kết quả tích của a và b."""
    result = multiply(a, b)
    print("Kết quả của", a, "và", b, "là:", result)  # Lỗi: Không có dấu câu ở cuối câu.

def add_numbers(a, b):
    # Lỗi: Thiếu từ khóa 'return'
    sum = a + b  
    print("Tổng của", a, "và", b, "là:", sum)  # Gọi hàm không trả về giá trị.

def calculate_area(radius):
    """Tính diện tích hình tròn."""
    area = 3.14 * radius ** 2
    return area

# Lỗi logic: Kiểm tra một số có phải là số nguyên không
def is_integer(n):
    if n != int(n):  # Lỗi: Phép kiểm tra không chính xác
        return True   # Lỗi: Phải trả về False nếu không phải là số nguyên.
    return False

# Hàm không được sử dụng
def unused_function():
    """Hàm này không được sử dụng."""
    pass

if name == "__main__":
    print_result(6, 7)
    print_result(8, 5)
    print("Số 4 có phải là số chẵn không:", is_even(4))
    print("Số 5 có phải là số chẵn không:", is_even(5))
    add_numbers(3, 5)  # Gọi hàm không trả về giá trị

    # Lỗi: Gọi hàm không kiểm tra biến đầu vào
    area_of_circle = calculate_area(-5)  # Lỗi: Không nên tính diện tích với bán kính âm
    print("Diện tích hình tròn với bán kính -5 là:", area_of_circle)

    # Gọi hàm kiểm tra số nguyên
    print("5.5 có phải là số nguyên không:", is_integer(5.5))
    print("5 có phải là số nguyên không:", is_integer(5))
