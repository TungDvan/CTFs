f = open('important_note.txt', 'rb')

byte = f.read(1)
ans = []
while byte:
    tmp = int.from_bytes(byte, 'little')
    ans.append(tmp)
    byte = f.read(1)
print(len(ans))
for i in range(len(ans)):
    if i % 10 == 9: print(f'0x{ans[i]:02x}', end = ',\n')
    else: print(f'0x{ans[i]:02x}', end = ', ')