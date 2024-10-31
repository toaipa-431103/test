# example_with_errors.py

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
    print("Tổng của", a, "và", b, "là:", sum)

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
