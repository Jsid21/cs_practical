import string

def generate_matrix(key):
    key = key.upper().replace('J', 'I')
    matrix = []
    used = set()

    for char in key:
        if char in string.ascii_uppercase and char not in used:
            matrix.append(char)
            used.add(char)

    for char in string.ascii_uppercase:
        if char != 'J' and char not in used:
            matrix.append(char)

    return [matrix[i*5:(i+1)*5] for i in range(5)]

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def prepare_text(text):
    text = text.upper().replace('J', 'I')
    text = ''.join([c for c in text if c in string.ascii_uppercase])

    digraphs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = 'X'
        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                b = 'X'
                i += 1
            else:
                i += 2
        else:
            i += 1
        digraphs.append(a + b)
    return digraphs

def encrypt_pair(a, b, matrix):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_pair(a, b, matrix):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def encrypt(text, key):
    matrix = generate_matrix(key)
    digraphs = prepare_text(text)
    return ''.join([encrypt_pair(a, b, matrix) for a, b in digraphs])

def decrypt(cipher, key):
    matrix = generate_matrix(key)
    digraphs = [cipher[i:i+2] for i in range(0, len(cipher), 2)]
    return ''.join([decrypt_pair(a, b, matrix) for a, b in digraphs])

# Example usage
if __name__ == "__main__":
    key = "MONARCHY"
    message = "INSTRUMENTS"

    encrypted = encrypt(message, key)
    print("Encrypted Text:", encrypted)

    decrypted = decrypt(encrypted, key)
    print("Decrypted Text:", decrypted)
