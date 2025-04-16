from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def rsa_encrypt(text, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    return cipher.encrypt(text.encode()).hex()

def rsa_decrypt(encrypted_text, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    return cipher.decrypt(bytes.fromhex(encrypted_text)).decode()

key = RSA.generate(2048)
public_key = key.publickey()
private_key = key

text = input("Enter text: ")
encrypted = rsa_encrypt(text, public_key)
print("Encrypted:", encrypted)
print("Decrypted:", rsa_decrypt(encrypted, private_key)) 