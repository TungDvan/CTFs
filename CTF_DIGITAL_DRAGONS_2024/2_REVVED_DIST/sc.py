admin = [
    0x61, 0x64, 0x6D, 0x69, 0x6E
] 

for i in range(len(admin)): admin[i] ^= 0xde

encrypted_flag = [
    0xD9, 0xD6, 0xD2, 0xD0, 0xCB, 0x87, 0x8C, 0xD5, 0x8F, 0x83, 
    0x8E, 0xDB, 0x8B, 0x86, 0xD1, 0xDA, 0x8D, 0xD5, 0x8E, 0xD3, 
    0x87, 0xD9, 0x8B, 0x84, 0xD2, 0xD9, 0x88, 0x8A, 0xD4, 0x86, 
    0xDA, 0xD9, 0xD0, 0xD2, 0x89, 0x8D, 0xDC, 0xCE
]


decrypt = []

for i in range(38):
    decrypt.append(admin[i % len(admin)] ^ encrypted_flag[i])

for i in decrypt: print(chr(decrypt[i]), end = '')

# flag{86f831a81ae7f9c8c83bf29c6ecce92f}