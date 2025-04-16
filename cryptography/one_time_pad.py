import random
import string

def generate_key(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

def otp_encrypt(text, key):
    text = text.upper().replace(" ", "")
    result = ""
    for i in range(len(text)):
        result += chr((ord(text[i]) + ord(key[i]) - 130) % 26 + 65)
    return result

def otp_decrypt(text, key):
    result = ""
    for i in range(len(text)):
        result += chr((ord(text[i]) - ord(key[i])) % 26 + 65)
    return result

text = input("Enter text: ")
key = generate_key(len(text))
encrypted = otp_encrypt(text, key)
print("Key:", key)
print("Encrypted:", encrypted)
print("Decrypted:", otp_decrypt(encrypted, key)) 