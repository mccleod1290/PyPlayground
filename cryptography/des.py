from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def des_encrypt(text, key):
    cipher = DES.new(key.encode(), DES.MODE_ECB)
    padded_text = pad(text.encode(), DES.block_size)
    return cipher.encrypt(padded_text).hex()

def des_decrypt(encrypted_text, key):
    cipher = DES.new(key.encode(), DES.MODE_ECB)
    decrypted = cipher.decrypt(bytes.fromhex(encrypted_text))
    return unpad(decrypted, DES.block_size).decode()

text = input("Enter text: ")
key = input("Enter 8-character key: ")
encrypted = des_encrypt(text, key)
print("Encrypted:", encrypted)
print("Decrypted:", des_decrypt(encrypted, key)) 