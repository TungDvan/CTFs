str1 = "mov	dword ptr [rbp - 0x10],"
str2 = "xor	al,"
str3 = "xor	eax,"
a = []
b = []
def extract_hex_value(line):
    # Tách chuỗi theo dấu hai chấm
    parts = line.split(':')
    
    if len(parts) >= 2:
        # Lấy phần sau dấu hai chấm và loại bỏ khoảng trắng
        value_part = parts[1].strip()
        
        # Kiểm tra nếu phần giá trị bắt đầu bằng '0x'
        if value_part.startswith('0x'):
            return value_part
        else:
            return None
    else:
        return None

def solve(input_file):
    with open(input_file, 'r') as infile:
            i = 0
            for line in infile:
                tmp = extract_hex_value(line)
                # print(type(tmp))
                tmp1 = int(tmp, 16)
                if i % 2 == 0: a.append(tmp1)
                else: b.append(tmp1)
                i += 1

# Tên tệp đầu vào và đầu ra
input_file = 'out.txt'

solve(input_file)
for i in range(len(a)):
    print(chr(a[i] ^ b[i]), end = '')

# I_reverse_all_this_and_all_I_got_is_this_flag

