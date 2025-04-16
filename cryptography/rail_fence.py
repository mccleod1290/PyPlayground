def rail_fence_encrypt(text, rails):
    text = text.replace(" ", "")
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    for char in text:
        fence[rail].append(char)
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1
    return ''.join([''.join(row) for row in fence])

def rail_fence_decrypt(text, rails):
    fence = [['' for _ in range(len(text))] for _ in range(rails)]
    rail = 0
    direction = 1
    for i in range(len(text)):
        fence[rail][i] = '*'
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1
    index = 0
    for i in range(rails):
        for j in range(len(text)):
            if fence[i][j] == '*':
                fence[i][j] = text[index]
                index += 1
    result = ''
    rail = 0
    direction = 1
    for i in range(len(text)):
        result += fence[rail][i]
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1
    return result

text = input("Enter text: ")
rails = int(input("Enter number of rails: "))
encrypted = rail_fence_encrypt(text, rails)
print("Encrypted:", encrypted)
print("Decrypted:", rail_fence_decrypt(encrypted, rails)) 