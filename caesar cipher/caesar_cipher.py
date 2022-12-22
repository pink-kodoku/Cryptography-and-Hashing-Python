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
    m = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    encrypted_text = caesar_encrypt(m)
    caesar_frequency_crack(encrypted_text)
