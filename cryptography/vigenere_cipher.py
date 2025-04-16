def vigenere_encrypt(text, key):
    text = text.upper().replace(" ", "")
    key = key.upper()
    result = ""
    for i in range(len(text)):
        char = text[i]
        key_char = key[i % len(key)]
        result += chr((ord(char) + ord(key_char) - 130) % 26 + 65)
    return result

def vigenere_decrypt(text, key):
    text = text.upper()
    key = key.upper()
    result = ""
    for i in range(len(text)):
        char = text[i]
        key_char = key[i % len(key)]
        result += chr((ord(char) - ord(key_char)) % 26 + 65)
    return result

text = input("Enter text: ")
key = input("Enter key: ")
encrypted = vigenere_encrypt(text, key)
print("Encrypted:", encrypted)
print("Decrypted:", vigenere_decrypt(encrypted, key)) 