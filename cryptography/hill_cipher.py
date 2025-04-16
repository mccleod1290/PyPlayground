import numpy as np

def get_key_matrix():
    print("Enter 2x2 key matrix (4 numbers separated by spaces):")
    key = list(map(int, input().split()))
    return np.array(key).reshape(2, 2)

def encrypt(text, key):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += 'X'
    result = ""
    for i in range(0, len(text), 2):
        block = np.array([ord(text[i]) - 65, ord(text[i+1]) - 65])
        encrypted = np.dot(key, block) % 26
        result += chr(encrypted[0] + 65) + chr(encrypted[1] + 65)
    return result

def decrypt(text, key):
    det = int(np.linalg.det(key))
    inv_det = pow(det, -1, 26)
    adj = np.array([[key[1,1], -key[0,1]], [-key[1,0], key[0,0]]])
    inv_key = (inv_det * adj) % 26
    result = ""
    for i in range(0, len(text), 2):
        block = np.array([ord(text[i]) - 65, ord(text[i+1]) - 65])
        decrypted = np.dot(inv_key, block) % 26
        result += chr(decrypted[0] + 65) + chr(decrypted[1] + 65)
    return result

text = input("Enter text: ")
key = get_key_matrix()
encrypted = encrypt(text, key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypt(encrypted, key)) 