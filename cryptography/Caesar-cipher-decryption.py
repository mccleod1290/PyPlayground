def caesar_cipher_decrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift - key) % 26 + shift)
        else:
            result += char
    return result

encrypted = input("Enter text to decrypt: ")
key = int(input("Enter numeric key: "))
decrypted = caesar_cipher_decrypt(encrypted, key)
print("Decrypted text:", decrypted)