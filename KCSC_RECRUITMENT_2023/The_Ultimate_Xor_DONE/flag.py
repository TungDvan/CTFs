str1 = "mov	dword ptr [rbp - 0x10],"
str2 = "xor	al,"
str3 = "xor	eax,"

def copy_lines(input_file, output_file):
    try:
        # Mở tệp đầu vào ở chế độ đọc
        with open(input_file, 'r') as infile:
            # Mở tệp đầu ra ở chế độ ghi
            with open(output_file, 'w') as outfile:
                # Đọc từng dòng từ tệp đầu vào
                for line in infile:
                    # Ghi từng dòng vào tệp đầu ra
                    if str1 in line or str2 in line or str3 in line: outfile.write(line)
        
        print(f"Nội dung từ '{input_file}' đã được sao chép sang '{output_file}'.")
    
    except FileNotFoundError:
        print(f"Tệp '{input_file}' không tồn tại.")
    except IOError:
        print(f"Có lỗi xảy ra khi đọc từ '{input_file}' hoặc ghi vào '{output_file}'.")

# Tên tệp đầu vào và đầu ra
input_file = 'asm.txt'
output_file = 'out.txt'

# Gọi hàm để sao chép nội dung tệp
copy_lines(input_file, output_file)

# def extract_hex_value(line):
#     # Tách chuỗi theo dấu hai chấm
#     parts = line.split(':')
    
#     if len(parts) >= 2:
#         # Lấy phần sau dấu hai chấm và loại bỏ khoảng trắng
#         value_part = parts[1].strip()
        
#         # Kiểm tra nếu phần giá trị bắt đầu bằng '0x'
#         if value_part.startswith('0x'):
#             return value_part
#         else:
#             return None
#     else:
#         return None

# # Dòng mẫu
# line = "0x4015a4:	0x15"

# # Gọi hàm để lấy giá trị hex
# hex_value = extract_hex_value(line)
# if hex_value:
#     print(f"Giá trị hex lấy được là: {hex_value}, {type(hex_value)}")
# else:
#     print("Không tìm thấy giá trị hex.")

