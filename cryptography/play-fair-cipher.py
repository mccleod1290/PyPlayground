def prepare(text):
    # Remove spaces and convert to uppercase
    text = ''.join(text.split()).upper().replace('J', 'I')
    res = ''
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            # If last character, add X
            res += text[i] + 'X'
            i += 1
        elif text[i] == text[i + 1]:
            # If repeated letters, add X between them
            res += text[i] + 'X'
            i += 1
        else:
            # Add the pair of letters
            res += text[i] + text[i + 1]
            i += 2
    return res

def matrix(key):
    # Create 5x5 matrix from key
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Note: I/J share a position
    key = key.upper().replace('J', 'I')
    # Remove duplicates while preserving order
    key = ''.join(dict.fromkeys(key))
    # Add remaining letters
    key += ''.join(c for c in alphabet if c not in key)
    return [list(key[i:i+5]) for i in range(0, 25, 5)]

def pos(matrix, char):
    # Find position of character in matrix
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def playfair(text, key, encrypt=True):
    matrix_5x5 = matrix(key)
    text = prepare(text)
    result = ''
    
    for i in range(0, len(text), 2):
        row1, col1 = pos(matrix_5x5, text[i])
        row2, col2 = pos(matrix_5x5, text[i + 1])
        
        if row1 == row2:  # Same row
            result += matrix_5x5[row1][(col1 + (1 if encrypt else -1)) % 5]
            result += matrix_5x5[row2][(col2 + (1 if encrypt else -1)) % 5]
        elif col1 == col2:  # Same column
            result += matrix_5x5[(row1 + (1 if encrypt else -1)) % 5][col1]
            result += matrix_5x5[(row2 + (1 if encrypt else -1)) % 5][col2]
        else:  # Rectangle case
            result += matrix_5x5[row1][col2]
            result += matrix_5x5[row2][col1]
            
    return result

# Test the cipher
if __name__ == "__main__":
    key = input("Enter the key: ")
    message = input("Enter the message: ")
    
    encrypted = playfair(message, key, True)
    decrypted = playfair(encrypted, key, False)
    
    print(f"Original: {message}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")