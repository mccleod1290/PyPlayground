def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

text = input("Enter text: ")
shift = int(input("Enter shift value: "))
encrypted = caesar_encrypt(text, shift)
print("Encrypted:", encrypted)
print("Decrypted:", caesar_decrypt(encrypted, shift)) 