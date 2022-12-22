ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(plaintext, secret):
    secret_len = len(secret)
    secret_index = 0
    plaintext = plaintext.upper()

    encrypted_string = ""
    for c in plaintext:
        if secret_index == secret_len:
            secret_index = 0

        if ALPHABET.find(c) != -1:
            index = (ALPHABET.find(c) + ALPHABET.find(secret[secret_index])) % 26
            encrypted_string += ALPHABET[index]
            secret_index += 1

    return encrypted_string


def decrypt(plaintext, secret):
    secret_len = len(secret)
    plaintext = plaintext.upper()
    secret_index = 0

    decrypted_string = ""
    for c in plaintext:
        if secret_index == secret_len:
            secret_index = 0

        index = (ALPHABET.find(c) - ALPHABET.find(secret[secret_index])) % 26
        decrypted_string += ALPHABET[index]
        secret_index += 1

    return decrypted_string


if __name__ == "__main__":
    m = "Hello world, my name is hahahha"
    result = encrypt(m, "cat")
    print(decrypt(result, "cat"))
    print(result)
