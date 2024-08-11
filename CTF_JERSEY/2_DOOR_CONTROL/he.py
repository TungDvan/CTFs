def ror(n):
    return ((n << 4) & ((1 << 8) - 1)) | (n >> 4)

pin = [
    0xC3, 0x83, 0x23, 0x23, 0xB3, 0xC3, 0x83, 0xE3, 0xA3, 0xE3, 0x33, 0x0C
]

for i in range(len(pin)):
    tmp = pin[i] ^ 0x55
    tmp = ror(tmp)
    tmp = ~tmp & 0xff
    tmp -= 96
    pin[i] = chr(tmp)

for i in range(len(pin)): print(end = pin[i])