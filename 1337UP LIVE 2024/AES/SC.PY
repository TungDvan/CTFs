from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def decrypt_aes(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)  # Tạo AES cipher với chế độ CBC
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)  # Giải mã và bỏ padding
    plaintext = list(plaintext)
    plaintext = [chr(i) for i in plaintext]
    return plaintext

if __name__ == "__main__":
    key = bytes.fromhex('31737427745F376C40675F755F326830756C646E27745F7335626D31745F3174')  
    iv_prefix = bytes.fromhex('05172B0C22410C2D0C22205E1C22')
    ciphertext = bytes.fromhex('99286748B056C365A16C1199FE885AA470FD5EA7963A1FCCB2DFCB278B7CC396A89E58BA9E9765130524486ABC7D1929')
    for byte1 in range(256):
        for byte2 in range(256):
            iv = iv_prefix + bytes([byte1, byte2]) 
            decrypted_text = decrypt_aes(key, iv, ciphertext)
            for i in decrypted_text: 
                try: print(end = i)
                except UnicodeEncodeError:  print(end = '~')
            print()

