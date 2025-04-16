from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_encrypt(text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    padded_text = pad(text.encode(), AES.block_size)
    encrypted = cipher.encrypt(padded_text)
    return cipher.iv.hex() + encrypted.hex()

def aes_decrypt(encrypted_text, key):
    iv = bytes.fromhex(encrypted_text[:32])
    encrypted = bytes.fromhex(encrypted_text[32:])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(encrypted)
    return unpad(decrypted, AES.block_size).decode()

text = input("Enter text: ")
key = get_random_bytes(16)
encrypted = aes_encrypt(text, key)
print("Encrypted:", encrypted)
print("Decrypted:", aes_decrypt(encrypted, key)) 