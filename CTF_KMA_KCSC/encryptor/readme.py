data_encrypt = [
    0xe0, 0x3b, 0xe1, 0x66, 0xf8
]

data_mau = [
    0x42, 0x4d, 0x56, 0x6b, 0x08
]   # BMVk

def copy_list():
    ans = []
    for i in range(len(data_mau)):
        ans.append(data_mau[i])
    return ans

def convert(a):
    ans = []
    for i in range(4):
        ans.append(a & 0xff)
        a = a >> 8
    return ans

def RC4(key):
    map = []
    for i in range(256): map.append(i)
    tmp = 0
    for i in range(256):
        tmp = (key[i % 4] + map[i] + tmp) % 256
        tmp_i = map[i]
        map[i] = map[tmp]
        map[tmp] = tmp_i
    return map

def RC4_en(map, data):
    tmp1, tmp2 = 0, 0
    for i in range(len(data)):
        tmp1 = (tmp1 + 1) % 256
        tmp2 = (map[tmp1] + tmp2) % 256
        tmp = map[tmp1]
        map[tmp1] = map[tmp2]
        map[tmp2] = tmp
        data[i] ^= map[(map[tmp1] + map[tmp2]) % 256]
        if data[i] != data_encrypt[i]: return False
    return True


if __name__ == "__main__":
    for i in range(4294967296):
        key = convert(i)
        map = RC4(key)
        data = copy_list()
        if RC4_en(map, data): 
            print(i)
            break





