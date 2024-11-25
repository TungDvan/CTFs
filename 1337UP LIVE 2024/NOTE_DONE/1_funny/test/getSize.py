import os

# Hàm tính kích thước file
def get_file_size(file_path):
    try:
        size = os.path.getsize(file_path)  # Tính kích thước file (đơn vị: byte)
        return size
    except FileNotFoundError:
        print("File không tồn tại!")
        return None

# Đường dẫn đến file
file_path = "__pycache__/_test1.cpython-311.pyc"  # Thay bằng đường dẫn file của bạn
# file_path = "_test0.py"

# Gọi hàm và in kích thước file
size_in_bytes = get_file_size(file_path)
if size_in_bytes is not None:
    print(f"Kích thước của file là: {size_in_bytes:08X} byte")
