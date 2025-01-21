def encipher(v, k):
    y=v[0];z=v[1];sum=0;delta=0x9E3779B9;n=32
    w=[0,0]
    while(n>0):
        y += (z << 4 ^ z >> 5) + z ^ sum + k[sum & 3]
        y &= 4294967295 # maxsize of 32-bit integer
        sum += delta
        z += (y << 4 ^ y >> 5) + y ^ sum + k[sum>>11 & 3]
        z &= 4294967295
        n -= 1

    w[0]=y; w[1]=z
    return w

def decipher(v, k):
    y=v[0]
    z=v[1]
    sum=0xC6EF3720
    delta=0x9E3779B9
    n=32
    w=[0,0]
    # sum = delta<<5, in general sum = delta * n

    while(n>0):
        z -= (y << 4 ^ y >> 5) + y ^ sum + k[sum>>11 & 3]
        z &= 4294967295
        sum -= delta
        y -= (z << 4 ^ z >> 5) + z ^ sum + k[sum&3]
        y &= 4294967295
        n -= 1

    w[0]=y; w[1]=z
    return w

key = [0x3AB27278, 0x0A840805B, 0x0E864925B, 0x0B7B1EEDE]

flag_en = [
    0x1C37B6EC, 0xB0E36676, 0x4137C16F, 0x454D466D, 0x7A0AFE3B, 0x235B5B39, 0xCA317196, 0x7DB9C036, 0xBAC3881C, 0x089925A4,
    0xFE2A59A9, 0x94E61826
]

if __name__ == "__main__":
    # # k = [0x126575b, 0x51903231, 0x8aab8f5e, 0xca51930f]
    # k = [0x3AB27278, 0x0A840805B, 0x0E864925B, 0x0B7B1EEDE]


    # v2 = [0x1C37B6EC, 0xB0E36676]
    # tmp2 = decipher(v2, k)
    # for i in tmp2: print(hex(i))

    ans = []
    for i in range(0, len(flag_en), 2):
        v = flag_en[i:i+2:1]
        k = key[::]
        tmp = decipher(v, k)
        ans += tmp

    for i in ans:
        while i: 
            print(end = chr(i & 0xff))
            i >>= 8

# 0x4353434b KCSC
# 0x4554587b {XTE
# 0x6e655f41 A_en
# 0x70797263 cryp
# 0x6e6f6974 tion
# 0x646e615f _and 
# 0x6265645f _deb
# 0x65676775 ugge
# 0x65645f72 r_de
# 0x74636574 tect
# 0x5f6e6f69 ion_
# 0x7d3e3e3a :>>} 


# KCSC{XTEA_encryption_and_debugger_detection_:>>} 


