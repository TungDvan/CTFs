def read_file():
    # Định nghĩa tên tệp nguồn và tệp đích
    source_file = 'flag.bmp'
    destination_file = 'picture_.txt'

    # Mở tệp nguồn ở chế độ đọc nhị phân và tệp đích ở chế độ ghi
    with open(source_file, 'rb') as src, open(destination_file, 'w', encoding='utf-8') as dest:
        while True:
            # Đọc từng byte từ tệp nguồn
            byte = src.read(1)
            if not byte:
                break
            # Chuyển byte sang dạng hexa và ghi vào tệp đích
            hex_value = format(byte[0], '02x')
            dest.write(f'{hex_value}\n')

def size_file():
    # Định nghĩa tên tệp
    file_name = 'flag.bmp.encrypted'

    # Mở tệp ở chế độ đọc nhị phân
    with open(file_name, 'rb') as file:
        # Di chuyển con trỏ đến cuối tệp
        file.seek(0, 2)
        # Lấy vị trí hiện tại của con trỏ (số byte của tệp)
        file_size = file.tell()

    # In ra số byte của tệp
    print(f'Số byte của tệp {file_name} là: {file_size}')

if __name__ == "__main__":
    read_file()
    # size_file()


# 42 B
# 4d M
# 56
# 6b
# 08  .\encryptor.exe flag.bmp.encrypted 25110

# encypt
# e0
# 3b
# e1
# 66
# f8