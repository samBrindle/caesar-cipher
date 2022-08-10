
def encrypt(plain, shift):
    encrypted = ""

    for char in plain:
        if char.isupper():
            ord_char = ord(char)
            shifted_char = (ord_char + shift - 65) % 26 + 65
            encrypted += chr(shifted_char)
        elif char.islower():
            ord_char = ord(char)
            shifted_char = (ord_char + shift - 97) % 26 + 97
            encrypted += chr(shifted_char)
        else:
            encrypted += char

    return encrypted


def decrypt(cipher, shift):
    return encrypt(cipher, -shift)


