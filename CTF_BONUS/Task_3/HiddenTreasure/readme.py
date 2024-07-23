def read_file():
    source_file = 'inside-the-mind-of-a-hacker-memory.bmp'
    destination_file = 'find_flag.txt'
    ans = []
    with open(source_file, 'rb') as src:
        i = 0
        while True:
            byte = src.read(1)
            if not byte:
                break
            if i >= 54 and (i - 54) % 3 == 0 and (byte == b'\x00' or byte == b'\x01') and i <= 771:
                hex_value = format(byte[0], '01x')
                ans.append(hex_value)
            i += 1
    return ans

def _bit(map, pos):
    ans = []
    for i in range(pos, pos + 8):
        ans.append(map[i])
    ans = ans[::-1]
    return ans

if __name__ == "__main__":
    flag = read_file()
    for i in range(0, len(flag), 8):
        ans = _bit(flag, i)
        binary_string = ''.join(map(str, ans))
        decimal_value = int(binary_string, 2)
        ascii_character = chr(decimal_value)
        print(ascii_character, end = '')
