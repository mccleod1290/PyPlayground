def caesar_cipher(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

message = input("Enter text to encrypt: ")
key = int(input("Enter numeric key: "))
encrypted = caesar_cipher(message, key)
print("Encrypted text:", encrypted)