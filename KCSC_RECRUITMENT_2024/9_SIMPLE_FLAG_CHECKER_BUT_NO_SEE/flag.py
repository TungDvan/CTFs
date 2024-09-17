# # // 123456789012345678901234567890123456789012345678901234567

# # // 012345678901234567890123456789012345678901234567890123456
# # // KCSC{PoLym0rphi5m_O0P_of_Jav4_1s_ez_to_aPPro4ch_i5nt_it?}

# 't', '', 'i', '', 't', '', 'n', '', 'i', '', 'h', '', 'c', '', 'o', '', 'r', '', 'P', ''
# # // static int[] pos = { 10, 15, 19, 28, 30, 44, 49 };  so
# # // int[] pos = { 17, 21, 24, 29, 32, 35, 38, 47, 52 }; dau _ 

# // num[0] = 0
# // num[1] = 5
# // num[2] = 0
# // num[3] = 4
# // num[4] = 1
# // num[5] = 4
# // num[6] = 5

from z3 import *

a = [BitVec(f"a[{i}]", 64) for i in range(14)]
s = Solver()

s.add(a[0] + a[5] + a[6] == 294)
s.add(a[1] * a[3] == 8160)
s.add(a[3] ^ a[4] == 44)
s.add(a[2] ^ a[3] == 9)
s.add(a[0] * a[3] == 8058)
s.add(a[3] - a[4] == 28)
s.add(a[2] ^ a[7] == 28)
s.add(a[12] - a[13] + a[9] - a[8] == 38)
s.add(a[3] - a[4] == 28)
s.add(a[2] ^ a[11] == 0)
s.add(a[4] - a[6] == -44)
s.add(a[6] ^ a[8] == 19)
s.add(a[9] - a[5] == 25)
s.add(a[0] + a[5] + a[7] == 291)
s.add(a[10] ^ a[5] == 21)
s.add(a[1] == a[13])
s.add(a[11] == 111)

if s.check() == sat:
    m = s.model()
    for c in a:
        print(f"'{chr(m[c].as_long())}'", end = ' ')