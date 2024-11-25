# file_path = "__pycache__/_test.cpython-311.pyc"
file_path = "_test0.py"
f = open(file_path, 'rb')

byte = f.read(1)

ans = []

while byte:
    byte = int.from_bytes(byte, 'big')
    ans.append(byte)
    byte = f.read(1)
    
for i in range(len(ans)):
    if i % 10 == 9: print(f'0x{ans[i]:02X}', end = ',\n')
    else: print(f'0x{ans[i]:02X}', end = ', ')