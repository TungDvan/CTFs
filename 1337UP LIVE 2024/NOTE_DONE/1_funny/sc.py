# from Crypto.Cipher import AES
# from Crypto.Util.Padding import pad, unpad

# a = b = c = d = e = f = g = h = i = j = k = l = m = n = o = p = q = r = s = t = u = v = w = x = y = z = 0


# key = input("Key > ").encode()
# iv = input("IV  > ").encode()

# # Kiểm tra độ dài của `key` và `iv`
# if len(key) != 32 or len(iv) != 16:
#     raise ValueError("Key must be 32 bytes and IV must be 16 bytes.")


from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

iv = b'\x1fdu\xae\x8f\x9a\xa5\x8b,\x94\xa0T\xe5ib\xd0'
key = b'/\xa0\xaa<?\xb54q\xdb\x00\x8e\xfe w\xae\x89\xf3R3\xd7.\x83c\xe6\xb6E\xac|\xfd\x92\x95j'
# Tạo một đối tượng AES CBC và giải mã dữ liệu được mã hóa
cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(
    cipher.decrypt(
        b'\xc0\xae\x13\x8a\xbb\x0b\xa1\x95\xf9\x8a\xe0\\\xb6\xc8\xd2\x1fHF*\x0bK\x11\xf2\x82\xfcIk\xd2|\xcdf\xd6@c\x17\xe9\xcc\xdd\x98O\xa5;=<\xea\\\x91\xf2\xc0I\x901)\x8bH\xab\xda}g\x95\x0f#<YN\x03\x94n\xd1\xed\xcf\x9a\xc4\xefU\x99\x92\xe7\xf0&^\xd9\xb9\xc7U\x7f\xce\x0eQ;9dU\xf2\x88\x17\xe2\xc0Q\x93&\xeb\x1f\xf9\'"$\x08?\x83~\xb1\xc8HK\x07\xce\xb2\x10\xd1\x9d\x99k\xba)X\xc5\x08\xec\xe7]\x81s\x9b\xdfsl\xad\xbc 8TM\xd9\xa1em;\xec\x03E\xa5EJ\xbaT:\'\xa3\xa9\xf4\xa9\x0b\xadL\xaer\xf1\x84\x02bI\xe3Ym-&\xb6\xae\\c\xa0\xbcJ@\xaf\xf9\x1d\x8bY\xa3\xa5\xe5b\xf3\xf1\x99b\xf2~\xbd\xf3\xd6\xf5m,\x82=u\x98G\x1b\x86s6\xcb\xf8x\xa9\x16\xfc\xe35\xd8\xca\x17K\xa4\xc6\x04d:\xbaN \xed\x15`\x8f\xd1\xe1\xfdHhr\xbc\xb08V\xb8\x8d\x83\x8a\xf2\x8e{\xe0M\xffs=\xfb\x8d;\xdf\xdd\xc1\x0fm\xeb{\xb5\x9bm\x83\xe7\xf9\x91F\xc0C\xdfP\rG\xd6\xfa\xd7Lb\x8eA\xe4\x008\xf2\xad\xd8\x0f\x9d\xb8\xbfM@\xf4\xca\xf4\xb2\xbbi\x0c\xff\x0fu\x9cT\x0b\xf8\x8e\x9c\x1e\xca\xbc\xcd\xaaG\xd9\x17xp\xd1B7\x0f\xe0\x914\xf1\xdb\xeczH\xbbc\xde\xfcyGA/\xce\x86\x91\xec\xe5:\xc1\x03\x8d]\x90J^\xdc\xa9+\x03Xh\xc3\xe9\x1cDxd\x1b\x0fF\x1f\x99\x18\x8e9DA{\x80\xea\xcf\xb0\xeb\xb0K\x8f\xe4\x07\x1f\x8e\x04n\xb8t\xe9\x13R\xf39\xf1\x17\x05\xfb\x00\xf8\xca\xfa}K\xa6\x8e+\xd5\xa9\x04\xb9I\xab+w\x93\xa8\xfek\xd3\x8bJt\xe3\xfea\xa1 \xb7\xb9\xae\x81\xe2:\xfc\x0b\x85\x15\xe4s\xef:xF\xd9\x83\xddi4\x9e6!\xc2\xbaP\\\xb4V6%\xc0"x\xd1\x15\xc1\x07\x10\xd0\xf9\x96\xee\xd6\xf1)\x9e\xe3\xb9\xe3T\xec\xdd\x8alF\x88\x101U\xed\xb8\xbcd\xfc\x02\xb3\xb4B\x04\xd4g\xc8\xc7\x83\x89^^\xc4\xfc\x02\xca\xcd\xb9\xa7\\|yU\xb71\xb4>\xa9\x1dxv4!\\\xe1\xc1\xe0?\xa3\xaf/(\x16\x0b\xcd\xd3\x99S\x0f\xe4\xfd\xa9\\\x17g\x9e\'N^\xca\x9f^\xec~G\xfa\xd9\xc5 R\xb1\x1f\x95\xaa\xe5:\xa7\x9f\xc2\x8bC\x88\xd2\xa1\xff\x83\x94a\x11J\xdb{\x1bb\x1aBs\x18\xef\xa7\xd7\x1e\xc3\xa4\xff\xa9v:M\xb2\xc59\x98\xe4f\x13!\xf5mz\xb1\x15\xdc\xf5x\xd3g\x0e%t\xda\x9aV\x0cQ\xe5Z{s5\xb1C\xe2!\xdf\xc4z\xaa9^/y\x01^\x99\xdb)4\x02,C\x16tQ\xa2Rj\x80f\xc5U\t\xbd\x1d\xaf/\xaf\x9b\x8cv\xd5\n\x0b\xf6$3\x97Ac\xd6\xff\xc0\x86\xe3\xe3\x1d\x87T\x1d\x8b\xab%S\x8a!\x9f\x1b\x9a$\xdb:\xf47\xa7,\x1cY\x9c*\xec\xcbt1\x9c\x9euGs\x18t\xf6\x81\xeb\xe0Dd\xedx\x02\xec"\xab\x80Bh\x03\xcb\x86\xe1*K\xa5O\xa3\xc2,q~\x87\x8a%\xcc%\x0c\xda-9F)\x00\x8b\xbe\x85\x17\xadl\xd2\xb0\x8c\x8e;U*\xfc4\xd6\r>\x04\xbe\x7f\x88\xc7T\xbd0\xa6\xe85\xa9.\x19\x8d\xfa%\x85\n\xe2\x84\xa8&\xcd\'\xb9\xd6\xebK\x8d\x10}\xc2\xd1\xde@9Uf\xa4_\xa2\xb9X\xd6;\xf9I\xcfc\xfc6\x94\xa5\x834\xbeBD\xfa\xfd\xb8.\x82\xfb)a\xf6L\x95V#\x05\xea}6\xe0C\xf7\xf4\xd3\xed\xba\x02v\xe5 \xcch,{\xad\xc7\xfc\xe1\xaf\xb3\x14R\xdb1\x07JK:g8\x8b\x9bw\x17\x1d\x13\x8ff\x8a\x0e\x98\xcd\xc4\xb1e^\x8c\xbai\x05\xa2\x9e\xc9\xd8{ D\x9c\x0f\xc1\x8a\x0b\x92\'\xed \x8f,\x00o\xa3\xb8%X\xa3\xde\xec\xfdu\x1a\xc9\xac\xfd\x1f\xf9<|\xd4G\x1a.\xac^\xfc\xc9I\x1fkG\xe9\xa1\x0e\xd2\x1b\x90\xb7\xfd\xd0.{\x00d6Y\x06\xcb,L\x9a\x82\xb5\xe6\x8f\xedp=\xbf\xbdFP\x88\xdf!\x0f}]\xecK\x0b3\x97f\xf6\'\x90\xe7\x9ex:xE\x9c\xe0\xbe\x14\xc8\x0f\xa3\xc8\xdag1\xe5{\xe1i|=\x14\x81wy\xb8W\xe7?j\x95;p\x1a\x95\xc7#6\xc3\x00\xec8\xae;\xc9\xf7\xcc\x0f\xb4K\x17w\x1f\xc9]\xa8D&\xb1\xacrs\xbeI\xc7\xab\xf29s\x85\xd7\xaf0\xb0|\x13\xa6\x96\x8f\xe2\x97\x84\x8ag\xf3\xb9ow!b\xa8\xd1\x83a[*$\x8a\xfdp\xc2\x7f\xb1f\xd4\x90z\xe3V\x16\xd8\xed\xa2@\n_\xb4\xd2)\xd4\x14\x85\xbay\xf65#3\xbf\x14\xbf\x1a\xb4\xcb\xd9\xc7\x0f\xe8\xa5!\xa0\xae\x00\x9a\xdb\xd8\xfbg\x8f\x99\xca&\x9f\xe7\x0c\xf3\x03\xd3rw\xe2P\x8c\x01\x0b\xa14-U\xb3\x8b?\x94\xfd\xed#\x99w4\xa2\xf7\xfaS\x10\xa5F\xcbY\x1a\xe7\x87I\xed\x02t,|\xb6c\x8f\xa4)\xa7\x8e\xe2\x18<\xaf\x05z g\xda\xa3\x19\xefq\xe4?\x92\xfdj+y}|\xc6\r}\xad\xd8\xecp\x96v\x8ah\x8b_\xec?\xfbpg\xc5\xfe\x9d=\x063\x17\x96\xe2>\xb1\xed-l\x95b\xb6\x81\xebF-\x1b\x12\xc2\x0b\xdeG\xbd\xdc\xe3\xf56u\xfd\x14\x17V\x8c\x87\x17_m?\xf7\xc3\xc2\xf0\x80;\x03\xea\xc9\xfd\x93~\xeff\x9b\xc5\r\x92\x9atb\xf9\x16\x8c&m4\xb5/F@\x12\')\xea\xff\x97\xf5C;\xd7\x08\xa0\xac`\xc5#\x8b\x80\t\xe4\xf1\x99\x81\xc9\xa7g\xe0\xb1\x02)CZVz\xa6\xcb\x84@!\x98\xf9n \xa0e.3\xa3I\xe8\xcd\x8a\x9d\xb6\xdf\x18G\xdd\xf8T6&\xaa\xde\xb6\x9d\xfb\xdb\x17\x00H\xe3Lm|\xc8\x80\xb0\x03\xd1\xd2\xaaw~\xa0\x00P\x1f\x1a_\x8b\t\x81\xc8p\xfa.\xfb\xd8;\x13\xbb\x80$\xe3\xa4\x05*\x91\x9eD$cc\xaf@\x9b\xaa\xb7&\xaf\x1a\xa1L/X\xc8\xafW\xa3\xb6\xd1\r\xa4\xe8\x91 ^4\xd4\xc7V7\xc6\xe4\x11\x12\xe0{x\x85\xbb\x92\x07\xc0\xd3\xec\xf2JcX\xdb\xcd\xda\xae\x80\xfa\x92\xae\xae&\x07\xaf\x86\xf8i\xabai\xed\x0c`'
    ),
    AES.block_size
)

# # Kiểm tra xem `b'INTIGRITI'` có nằm trong `decrypted` hay không
# if b'INTIGRITI' in decrypted:
print("gg")
print(decrypted.decode())


# _0 = "brybefejnkidosboguihagsepxeywufiazxoxzbmtjrcfsknpkldhzjauxayobidvhnaqgbxzfsjyrwaanndfompthvsbqkgxmqelqaifrfkfmonzvnkmrgmhccunoirbrybefejnkidosboguihagsepxeywufiazxoxzbmtjrcfsknpkldhzjauxayobidvhnaqgbxzfsjyrwaanndfompthvsbqkgxmqelqaifrfkfmonzvnkmrgmhccunoirbrybefejnkidosboguihagsepxeywufiazxoxzbmtjrcfsknpkldhzjauxayobidvhnaqgbxzfsjyrwaanndfompthvsbqkgxmqelqaifrfkfmonzvnkmrgmhccunoirbrybefejnkidosboguihagsepxeywufiazxoxzbmtjrcfsknpkldhzjauxayobidvhnaqgbxzfsjyrwaanndfompthvsbqkgxmqelqaifrfkfmonzvnkmrgmhccunoir"
# _1 = "xxxbhafmrsbuseiwnwiyibbprvienxuqromdwofcupvupdewoyjjxxxbhafmrsbuseiwnwiyibbprvienxuqromdwofcupvupdewoyjjxxxbhafmrsbuseiwnwiyibbprvienxuqromdwofcupvupdewoyjjxxxbhafmrsbuseiwnwiyibbprvienxuqromdwofcupvupdewoyjjxxxbhafmrsbuseiwnwiyibbprvienxuqromdwofcupvupdewoyjjxxxbhafmrsbuseiwnwiyibbprvienxuqromdwofcupvupdewoyjjxxxbhafmrsbuseiwnwiyibbprvienxuqromdwofcupvupdewoyjjxxxbhafmrsbuseiwnwiyibbprvienxuqromdwofcupvupdewoyjjxxxbhafmrsbuseiwnwiyibbprvienxuqromdwofcupvupdewoyjjxxxbhafmrsbuseiwnwiyibbprvienxuqromdwofcupvupdewoyjj"
# _2 = "ptjilemtmvowacennoaykdzojeqevimbbfmycmmgvbfzncavpptjilemtmvowacennoaykdzojeqevimbbfmycmmgvbfzncavpptjilemtmvowacennoaykdzojeqevimbbfmycmmgvbfzncavpptjilemtmvowacennoaykdzojeqevimbbfmycmmgvbfzncavpptjilemtmvowacennoaykdzojeqevimbbfmycmmgvbfzncavpptjilemtmvowacennoaykdzojeqevimbbfmycmmgvbfzncavpptjilemtmvowacennoaykdzojeqevimbbfmycmmgvbfzncavpptjilemtmvowacennoaykdzojeqevimbbfmycmmgvbfzncavpptjilemtmvowacennoaykdzojeqevimbbfmycmmgvbfzncavpptjilemtmvowacennoaykdzojeqevimbbfmycmmgvbfzncavpptjilemtmvowacennoaykdzojeqevimbbfmycmmgvbfzncavp"
# _3 = 'ksdpsbjmgekyyrdzxppurwcomfjvnoouvimxjbcdbwuooxhgcjeuivfydlfucajyibhlvcsijwethshnwbmvkftvwoosexgksdpsbjmgekyyrdzxppurwcomfjvnoouvimxjbcdbwuooxhgcjeuivfydlfucajyibhlvcsijwethshnwbmvkftvwoosexgksdpsbjmgekyyrdzxppurwcomfjvnoouvimxjbcdbwuooxhgcjeuivfydlfucajyibhlvcsijwethshnwbmvkftvwoosexgksdpsbjmgekyyrdzxppurwcomfjvnoouvimxjbcdbwuooxhgcjeuivfydlfucajyibhlvcsijwethshnwbmvkftvwoosexgksdpsbjmgekyyrdzxppurwcomfjvnoouvimxjbcdbwuooxhgcjeuivfydlfucajyibhlvcsijwethshnwbmvkftvwoosexgksdpsbjmgekyyrdzxppurwcomfjvnoouvimxjbcdbwuooxhgcjeuivfydlfucajyibhlvcsijwethshnwbmvkftvwoosexg'
# _4 = 'rdgvipgcyliyrswfpvbrhmrgtzevpdbuggfvvlbihwbrrdgvipgcyliyrswfpvbrhmrgtzevpdbuggfvvlbihwbrrdgvipgcyliyrswfpvbrhmrgtzevpdbuggfvvlbihwbrrdgvipgcyliyrswfpvbrhmrgtzevpdbuggfvvlbihwbrrdgvipgcyliyrswfpvbrhmrgtzevpdbuggfvvlbihwbrrdgvipgcyliyrswfpvbrhmrgtzevpdbuggfvvlbihwbrrdgvipgcyliyrswfpvbrhmrgtzevpdbuggfvvlbihwbrrdgvipgcyliyrswfpvbrhmrgtzevpdbuggfvvlbihwbrrdgvipgcyliyrswfpvbrhmrgtzevpdbuggfvvlbihwbrrdgvipgcyliyrswfpvbrhmrgtzevpdbuggfvvlbihwbrrdgvipgcyliyrswfpvbrhmrgtzevpdbuggfvvlbihwbrrdgvipgcyliyrswfpvbrhmrgtzevpdbuggfvvlbihwbrrdgvipgcyliyrswfpvbrhmrgtzevpdbuggfvvlbihwbr'
# _5 = 'pemzmblrzasbsuecggofxehwexdqowqwpbwlwqrlynupgpemzmblrzasbsuecggofxehwexdqowqwpbwlwqrlynupgpemzmblrzasbsuecggofxehwexdqowqwpbwlwqrlynupgpemzmblrzasbsuecggofxehwexdqowqwpbwlwqrlynupgpemzmblrzasbsuecggofxehwexdqowqwpbwlwqrlynupgpemzmblrzasbsuecggofxehwexdqowqwpbwlwqrlynupgpemzmblrzasbsuecggofxehwexdqowqwpbwlwqrlynupgpemzmblrzasbsuecggofxehwexdqowqwpbwlwqrlynupgpemzmblrzasbsuecggofxehwexdqowqwpbwlwqrlynupgpemzmblrzasbsuecggofxehwexdqowqwpbwlwqrlynupgpemzmblrzasbsuecggofxehwexdqowqwpbwlwqrlynupgpemzmblrzasbsuecggofxehwexdqowqwpbwlwqrlynupgpemzmblrzasbsuecggofxehwexdqowqwpbwlwqrlynupg'
# _6 = 'ofyngrbkaldjxznvvijkpecfgdbwrkmgjinsluahzyfckykgkwlmrhrubjyfmftlafujmbijvwolwpuayyxybdolmfquldxfmvxbzliwixespnzaxjyrmrhfhozizgfvanofyngrbkaldjxznvvijkpecfgdbwrkmgjinsluahzyfckykgkwlmrhrubjyfmftlafujmbijvwolwpuayyxybdolmfquldxfmvxbzliwixespnzaxjyrmrhfhozizgfvanofyngrbkaldjxznvvijkpecfgdbwrkmgjinsluahzyfckykgkwlmrhrubjyfmftlafujmbijvwolwpuayyxybdolmfquldxfmvxbzliwixespnzaxjyrmrhfhozizgfvanofyngrbkaldjxznvvijkpecfgdbwrkmgjinsluahzyfckykgkwlmrhrubjyfmftlafujmbijvwolwpuayyxybdolmfquldxfmvxbzliwixespnzaxjyrmrhfhozizgfvan'
# # # print(len(_0) +len(_1) +len(_2) +len(_3) +len(_4) +len(_5) +len(_6))
# # # _0 = _0[::-1]
# # # _1 = _1[::-1]
# # # _2 = _2[::-1]
# # # _3 = _3[::-1]
# # # _4 = _4[::-1]
# # # _5 = _5[::-1]
# # # _6 = _6[::-1]
# # print(len(_1))
# for i in range(len(_0)):
#     if _0[i] == 'x': print(end = _0[i])
#     else: print(end = ' ')
# print()
# for i in range(len(_1)):
#     if _1[i] == 'x': print(end = _1[i])
#     else: print(end = ' ')
# print()
# for i in range(len(_2)):
#     if _2[i] == 'x': print(end = _2[i])
#     else: print(end = ' ')
# print()
# for i in range(len(_3)):
#     if _3[i] == 'x': print(end = _3[i])
#     else: print(end = ' ')
# print()
# for i in range(len(_4)):
#     if _4[i] == 'x': print(end = _4[i])
#     else: print(end = ' ')
# print()
# for i in range(len(_5)):
#     if _5[i] == 'x': print(end = _5[i])
#     else: print(end = ' ')
# print()
# for i in range(len(_6)):
#     if _6[i] == 'x': print(end = _6[i])
#     else: print(end = ' ')

# # for i in range(len(_6)):
# #     if _6[i] == 'x': print(end = _6[i])
# #     else: print(end = ' ')
# # for i in range(len(_5)):
# #     if _5[i] == 'x': print(end = _5[i])
# #     else: print(end = ' ')
# # for i in range(len(_4)):
# #     if _4[i] == 'x': print(end = _4[i])
# #     else: print(end = ' ')
# # for i in range(len(_3)):
# #     if _3[i] == 'x': print(end = _3[i])
# #     else: print(end = ' ')
# # for i in range(len(_2)):
# #     if _2[i] == 'x': print(end = _2[i])
# #     else: print(end = ' ')
# # for i in range(len(_1)):
# #     if _1[i] == 'x': print(end = _1[i])
# #     else: print(end = ' ')
# # for i in range(len(_0)):
# #     if _0[i] == 'x': print(end = _0[i])


# #     else: print(end = ' ')


# s = 'brybefejnkidosboguihagsepxeywufiazxoxzbmtjrcfsknpkldhzjauxayobidvhnaqgbxzfsjyrwaanndfompthvsbqkgxmqelqaifrfkfmonzvnkmrgmhccunoir'
# s = 'xxxbhafmrsbuseiwnwiyibbprvienxuqromdwofcupvupdewoyjj'
# s = 'ptjilemtmvowacennoaykdzojeqevimbbfmycmmgvbfzncavp'
# s = 'ksdpsbjmgekyyrdzxppurwcomfjvnoouvimxjbcdbwuooxhgcjeuivfydlfucajyibhlvcsijwethshnwbmvkftvwoosexg'
# s = 'rdgvipgcyliyrswfpvbrhmrgtzevpdbuggfvvlbihwbr'
# s = 'pemzmblrzasbsuecggofxehwexdqowqwpbwlwqrlynupg'
# s = 'ofyngrbkaldjxznvvijkpecfgdbwrkmgjinsluahzyfckykgkwlmrhrubjyfmftlafujmbijvwolwpuayyxybdolmfquldxfmvxbzliwixespnzaxjyrmrhfhozizgfvan'

# for i in range(len(s)):
#     if s[i] == 'x': print(i)

# 25    0   _   16  _   20  12
# 34    1       35      25  82
# 36    2       45          94
# 57    29      93          98
# 71                        105
# 96                        112

# map = [(476, 6), (468, 5), (282, 6), (506, 6), (420, 3), (492, 0), (192, 6), (56, 6), (144, 3), (324, 0), (360, 1), (352, 6), (30, 1), (260, 0), (298, 1), (480, 3)]
# (492, 0)    (360, 1)    _    (420, 3)    _    (468, 5)    (476, 6)
# (324, 0)    (30, 1)          (144, 3)                    (282, 6)
# (260, 0)    (298, 1),        (480, 3)                    (506, 6)
#                                                          (192, 6)
#                                                          (56, 6)
#                                                          (352, 6)
  