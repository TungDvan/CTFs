def convert_to_bit_list(number):
    bit_list = [0] * 64
    for i in range(64):
        bit_list[63 - i] = (number >> i) & 1 
    return bit_list

flag = ["@"] * 62
flag[0] = 'K'
flag[1] = 'C'
flag[2] = 'S'
flag[3] = 'C'
flag[4] = '{'
flag[61] = '}'
flag[24] = 'u'
flag[11] = 'g'
flag[60] = 'g'
flag[37] = 'c'
flag[20] = 'd'

number = [0x2101004011000, 0x10000210000040, 0x80000040200000, 0x4200100802000, 0x400000000000280, 0x8480C02000000, 0xA00008000080400, 0x844000044000, 0x100020080408000, 0x60010020000100, 0x1000008020020]
chr = ['_', 'a', 'e', 'f', 'i', 'l', 'n', 'o', 'r', 't', 'w']
cond = [0x31, 0x34, 0x37, 0x32, 0x3A, 0x33, 0x3B, 0x2F, 0x38, 0x36, 0x30]

for _ in range(len(number)):
    bit_list = convert_to_bit_list(number[_])
    bit_list = bit_list[::-1]
    for i in range(len(bit_list)):
        if i <= cond[_] and bit_list[i] == 1: 
            flag[i] = chr[_]

for i in flag: print(end = i)
