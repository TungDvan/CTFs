flag_1 = list(bytes.fromhex('7E54595F09434B0F4A5D59757B514A5B6D550D0F0C765B7D45'))
xor_1 = [0x38]
for i in range(len(flag_1)): print(end = chr(flag_1[i] ^ xor_1[i % len(xor_1)]))
print()
# Flag1{s7reaMCircUm574NcE}

flag_2 = list(bytes.fromhex('775A5051034D5644706002635F467D0570030558454B'))
xor_2 = [0x31, 0x36]
for i in range(len(flag_2)): print(end = chr(flag_2[i] ^ xor_2[i % len(xor_2)]))
print()
# Flag2{grAV3UnpL3A54nt}

flag_3 = list(bytes.fromhex('755e525500496177065b057c076602025d6152467a0755735046025d5d4f'))
xor_3 = [0x33, 0x32] 
for i in range(len(flag_3)): print(end = chr(flag_3[i] ^ xor_3[i % len(xor_3)]))
# Flag3{RE5i6N4T10nSatI5fAct1on}