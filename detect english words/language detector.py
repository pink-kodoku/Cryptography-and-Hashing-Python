ENGLISH_WORDS = []

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEY = 3


# load the english words
def get_data():
    dictionary = open("words.txt", "r")

    for word in dictionary.read().split("\n"):
        ENGLISH_WORDS.append(word)

    dictionary.close()


def count_words(text):
    text = text.upper()
    words = text.split(" ")
    matches = 0

    for word in words:
        # can use tree data structure
        if word in ENGLISH_WORDS:
            matches += 1

    return matches


def is_text_english(text):
    matches = count_words(text)

    # larger than 80%
    if (float(matches) / len(text.split(" "))) * 100 >= 70:
        return True

    return False


if __name__ == "__main__":
    get_data()
    s1 = "My name is Balazs Holczer. I am from Budapest, Hungary. I am qualified as a physicist. At the moment I am working as a simulation engineer at a multinational company. I have been interested in algorithms and data structures and its implementations especially in Java since university. Later on I got acquainted with machine learning techniques, artificial intelligence, numerical methods and recipes such as solving differential equations, linear algebra, interpolation and extrapolation. These things may prove to be very very important in several fields: software engineering, research and development or investment banking. I have a special addiction to quantitative models such as the Black-Scholes model, or the Merton-model."
    s2 = "Hello world а теперь немного русского паххаха всмысле ттам же больше русского"
    print(is_text_english(s1))
    print(is_text_english(s2))
