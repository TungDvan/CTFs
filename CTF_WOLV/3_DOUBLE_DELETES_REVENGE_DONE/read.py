def read_4_bytes(file_path):
    with open(file_path, 'rb') as file:     # Mở file ở chế độ nhị phân đọc
        bytes_data = file.read(4)           # Đọc 4 byte từ file
        while bytes_data:
            reversed_bytes = bytes_data[::-1]
            hex_value = ''.join(f"{byte:02x}" for byte in reversed_bytes)
            print(end = "0x" + hex_value + ", ")
            bytes_data = file.read(4)


# file_path = 'flag.txt'                   # Thay đổi đường dẫn này thành đường dẫn đến file của bạn
# read_4_bytes(file_path)

flag_en = [
    0x8c6eecce, 0xed2f6e8b, 0xc62d0d6d, 0x0f2beea6, 0x2dabee66, 0x8dcea66c, 0x8e6e460e, 0xec860d0b, 0xeee60e4b, 0x2e860666, 0x0eebee46, 0xa6ad614f
]


def ROR4(ans):
    return (ans >> 13) | ((ans << 19) & ((1 << 32) - 1))

def ROL4(ans):
    return ((ans << 13) & ((1 << 32) - 1)) | (ans >> 19)

flag = []

for i in range(len(flag_en)):
    flag.append(ROR4(flag_en[i]))

for i in range(len(flag)):
    while flag[i]:
        print(chr(flag[i] & 0xff), end = '')
        flag[i] >>= 8

# wctf{i_th1nk_y0u_m1sund3rst00d_h0w_r0t13_w0rk5}