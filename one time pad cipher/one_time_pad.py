from random import randint
import matplotlib.pyplot as plt

ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(text, keys):
    text = text.upper()
    cipher_text = ""
    for index, char in enumerate(text):
        key_index = keys[index]
        char_index = ALPHABET.find(char)
        encrypted_index = (char_index + key_index) % len(ALPHABET)
        cipher_text += ALPHABET[encrypted_index]

    return cipher_text


def decrypt(text, keys):
    text = text.upper()
    decrypted_text = ""
    for index, char in enumerate(text):
        key_index = keys[index]
        char_index = ALPHABET.find(char)
        decrypted_index = (char_index - key_index) % len(ALPHABET)
        decrypted_text += ALPHABET[decrypted_index]

    return decrypted_text


def frequency_analysis(text):
    # the text we analyze
    text = text.upper()

    # to store the letter-frequency pair
    letter_frequency = {}

    for letter in text:
        if not letter in letter_frequency:
            letter_frequency[letter] = 0

        letter_frequency[letter] += 1

    return letter_frequency


def plot_distribution(letter_frequency):
    plt.bar(letter_frequency.keys(), letter_frequency.values())
    plt.show()


def random_sequence(text):
    random = []
    for _ in range(len(text)):
        random.append(randint(0, len(ALPHABET) - 1))

    return random


if __name__ == "__main__":
    s = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    keys = random_sequence(s)
    encrypted = encrypt(s, keys)
    print(encrypted)
    decrypted = decrypt(encrypted, keys)
    print(decrypted)
    plot_distribution(frequency_analysis(encrypted))
