def create_key_matrix(key):
    key = key.upper().replace("J", "I")
    key = "".join(dict.fromkeys(key))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in key:
        alphabet = alphabet.replace(char, "")
    key_matrix = list(key + alphabet)
    return [key_matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair_encrypt(text, key):
    text = text.upper().replace("J", "I").replace(" ", "")
    if len(text) % 2 != 0:
        text += "X"
    matrix = create_key_matrix(key)
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            result += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        elif col1 == col2:
            result += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]
    return result

def playfair_decrypt(text, key):
    matrix = create_key_matrix(key)
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            result += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
        elif col1 == col2:
            result += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]
    return result

text = input("Enter text: ")
key = input("Enter key: ")
encrypted = playfair_encrypt(text, key)
print("Encrypted:", encrypted)
print("Decrypted:", playfair_decrypt(encrypted, key)) 