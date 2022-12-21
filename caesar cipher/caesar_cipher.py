import matplotlib.pylab as plt

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEY = 3


def caesar_encrypt(plain_text):
    cipher_text = ""
    plaint_text = plain_text.upper()

    for c in plaint_text:
        index = ALPHABET.find(c)
        index = (index + KEY) % len(ALPHABET)
        cipher_text += ALPHABET[index]

    return cipher_text


def caesar_decrypt(cipher_text):
    plain_text = ""

    for c in cipher_text:
        index = ALPHABET.find(c)
        if index != -1:
            index = (index - KEY) % len(ALPHABET)
            plain_text += ALPHABET[index]

    return plain_text


def bruteforce_crack(encrypted_text):
    for key in range(len(ALPHABET)):

        plain_text = ""
        for c in encrypted_text:
            index = ALPHABET.find(c)
            index = (index - key) % len(ALPHABET)
            plain_text += ALPHABET[index]

        print(plain_text)


def frequency_analise(text):
    text = text.upper()
    letter_frequencies = {}
    for c in text:
        if c not in letter_frequencies:
            letter_frequencies[c] = 0
        letter_frequencies[c] += 1

    return letter_frequencies


def plot_distribution(frequencies):
    plt.bar(frequencies.keys(), frequencies.values())
    plt.show()


def caesar_frequency_crack(cipher_text):
    freq = frequency_analise(cipher_text)
    letter_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    print(letter_freq)
    most_repeated_letter1 = letter_freq[0][0]
    most_repeated_letter2 = letter_freq[1][0]
    print(ALPHABET.find(most_repeated_letter1) - ALPHABET.find("E"), end=" or ")
    print(ALPHABET.find(most_repeated_letter2) - ALPHABET.find("E"))


if __name__ == "__main__":
    m = "My name is Balazs Holczer. I am from Budapest, Hungary. I am qualified as a physicist. At the moment I am working as a simulation engineer at a multinational company. I have been interested in algorithms and data structures and its implementations especially in Java since university. Later on I got acquainted with machine learning techniques, artificial intelligence, numerical methods and recipes such as solving differential equations, linear algebra, interpolation and extrapolation. These things may prove to be very very important in several fields: software engineering, research and development or investment banking. I have a special addiction to quantitative models such as the Black-Scholes model, or the Merton-model."
    encrypted_text = caesar_encrypt(m)
    caesar_frequency_crack(encrypted_text)
