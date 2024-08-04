# import string

# alphabet = string.ascii_letters + string.digits + "!{_}?"

# flag = 'ldtdMdEQ8F7NC8Nd1F88CSF1NF3TNdBB1O'
# assert all(i in alphabet for i in flag)

# key = 25

# ct = ""
# for i in flag:
#     ct += (alphabet[(alphabet.index(i) + key) % len(alphabet)])

# print(f"{ct=}")

import string

alphabet = string.ascii_letters + string.digits + "!{_}?"

for key in range(67):
    if "K" == (alphabet[(alphabet.index("l") + key) % len(alphabet)]): print(key)