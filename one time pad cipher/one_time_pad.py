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
    s = "My name is Balazs Holczer. I am from Budapest, Hungary. I am qualified as a physicist. At the moment I am working as a simulation engineer at a multinational company. I have been interested in algorithms and data structures and its implementations especially in Java since university. Later on I got acquainted with machine learning techniques, artificial intelligence, numerical methods and recipes such as solving differential equations, linear algebra, interpolation and extrapolation. These things may prove to be very very important in several fields: software engineering, research and development or investment banking. I have a special addiction to quantitative models such as the Black-Scholes model, or the Merton-model."
    keys = random_sequence(s)
    encrypted = encrypt(s, keys)
    print(encrypted)
    decrypted = decrypt(encrypted, keys)
    print(decrypted)
    plot_distribution(frequency_analysis(encrypted))
