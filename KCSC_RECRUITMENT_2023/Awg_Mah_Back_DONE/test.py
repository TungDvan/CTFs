from pwn import *

with open('output.txt', 'rb') as (f):
    flag = f.read()
a = flag[0:len(flag) // 3]
b = flag[len(flag) // 3:2 * len(flag) // 3]
c = flag[2 * len(flag) // 3:]
c = xor(c, int(str(len(flag))[0]) * int(str(len(flag))[1]))
c = xor(b, c)
b = xor(a, b)
a = xor(c, a)
c = xor(b, c)
b = xor(a, b)
a = xor(a, int(str(len(flag))[0]) + int(str(len(flag))[1]))
enc = a + b + c
with open('input.txt', 'wb') as (f):
    f.write(enc) 
# KCSC{84cK_t0_BaCK_To_B4ck_X0r`_4nD_864_oM3g4LuL}