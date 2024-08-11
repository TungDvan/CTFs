n = 0x581A655C65487A561657164D525E4351464F

while n:
    print(chr(0x25 ^ (n & 0xff)), end = '')
    n >>= 8
