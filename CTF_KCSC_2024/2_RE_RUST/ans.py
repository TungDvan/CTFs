f = open('flag.enc', 'rb')
bytes = f.read(1)
flag_en1 = []
while bytes:
    tmp = int.from_bytes(bytes, 'big')
    flag_en1.append(tmp)
    bytes = f.read(1)

def rev_4(data, num):
    for i in range(len(data)):
        data[i] = data[i] ^ num

def rev_3(data):
    for i in range(len(data) - 3, -1, -1):
        if data[i + 2] + data[i] >= 256: data[i + 2] = data[i + 2] + data[i] - 256
        else: data[i + 2] = data[i + 2] + data[i]
        if data[i] + data[i + 2] >= 256: data[i] = data[i] + data[i + 2] - 256
        else: data[i] = data[i] + data[i + 2]

def rev_2(data):
    for i in range(0, len(data), 2):
        tmp1 = data[i + 1] & 0xF | data[i] & 0xF0
        tmp2 = data[i] & 0xF | data[i + 1] & 0xF0
        data[i] = tmp1
        data[i + 1] = tmp2

def rev_1(data):
    for i in range(0, len(data) // 2):
        data[i], data[len(data) - 1 - i] = data[len(data) - 1 - i], data[i]

def copy_arr():
    ans = []
    for i in flag_en1:
        ans.append(i)
    return ans

if __name__ == '__main__':
    for _ in range(256):
        flag_en = copy_arr()
        rev_4(flag_en, _)
        rev_3(flag_en)
        rev_2(flag_en)
        rev_1(flag_en)
        for i in flag_en: print(end = chr(i))
        print()


