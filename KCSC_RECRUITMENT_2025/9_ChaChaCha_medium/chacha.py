# from Crypto.Cipher import ChaCha20
# from Crypto.Random import get_random_bytes
# import binascii

# def chacha20_encrypt(key, nonce, plaintext):
#     """
#     Encrypts the plaintext using ChaCha20 algorithm.
#     :param key: 32-byte key for encryption
#     :param nonce: 12-byte nonce
#     :param plaintext: Data to be encrypted
#     :return: Encrypted ciphertext
#     """
#     cipher = ChaCha20.new(key=key, nonce=nonce)
#     ciphertext = cipher.encrypt(plaintext)
#     return ciphertext

# def chacha20_decrypt(key, nonce, ciphertext):
#     """
#     Decrypts the ciphertext using ChaCha20 algorithm.
#     :param key: 32-byte key for decryption
#     :param nonce: 12-byte nonce
#     :param ciphertext: Data to be decrypted
#     :return: Decrypted plaintext
#     """
#     cipher = ChaCha20.new(key=key, nonce=nonce)
#     plaintext = cipher.decrypt(ciphertext)
#     return plaintext

# if __name__ == "__main__":
#     # Key và nonce mẫu
#     key = bytes.fromhex("9EA86156573F5B6A1995AF6042B4788CD718CE61C6F219810AB55E6E593CD19E")
#     nonce = bytes.fromhex("6327885826A66520F404CE04C9E48062")  # Tạo nonce 12 byte ngẫu nhiên

#     # In ra key và nonce dưới dạng hex
#     print(f"Key (32 bytes): {binascii.hexlify(key)}")
#     print(f"Nonce (12 bytes): {binascii.hexlify(nonce)}")

#     # Dữ liệu cần mã hóa (plaintext)
#     plaintext = b"12345678"

#     # Mã hóa plaintext
#     ciphertext = chacha20_encrypt(key, nonce, plaintext)
#     print(f"Ciphertext (hex): {binascii.hexlify(ciphertext)}")

#     # Giải mã ciphertext
#     decrypted_plaintext = chacha20_decrypt(key, nonce, ciphertext)
#     print(f"Decrypted plaintext: {decrypted_plaintext.decode('utf-8')}")

#     # EF95A67FA284F620


import nacl.secret
import nacl.utils

# Tạo key 32 byte và nonce 16 byte ngẫu nhiên
key = bytes.fromhex("9EA86156573F5B6A1995AF6042B4788CD718CE61C6F219810AB55E6E593CD19E")
nonce = bytes.fromhex("6327885826A66520F404CE04C9E48062")  # Tạo nonce 12 byte ngẫu nhiên

# Dữ liệu cần mã hóa (ví dụ)
data = b"12345678"

# Khởi tạo cipher XChaCha20 với key và nonce
cipher = nacl.secret.SecretBox(key)

# Mã hóa dữ liệu
encrypted_data = cipher.encrypt(data, nonce)

# In kết quả
print("Original data:", data)
print("Encrypted data (hex):", encrypted_data.hex())

# Giải mã dữ liệu
decrypted_data = cipher.decrypt(encrypted_data)

# In kết quả giải mã
print("Decrypted data:", decrypted_data)
