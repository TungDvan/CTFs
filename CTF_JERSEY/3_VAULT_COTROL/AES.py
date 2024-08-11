from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Khóa bí mật và IV
key = get_random_bytes(32)  # AES-256
iv = get_random_bytes(16)


# Dữ liệu cần mã hóa
plaintext = b"Hello, this is a secret message!"

# Mã hóa dữ liệu
cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

print(f"Ciphertext: {ciphertext.hex()}")

# Giải mã dữ liệu
cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)

print(f"Decrypted Data: {decrypted_data.decode()}")
