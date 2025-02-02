import sys
import random


def generate_sentence(word_count):
    words_file = "/usr/share/dict/words"

    with open(words_file, 'r') as file:
        words = file.read().splitlines()

    random_words = random.sample(words, word_count)

    sentence = " ".join(random_words) + "."
    return sentence


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        num_words = int(sys.argv[1])

        print(generate_sentence(num_words))

    except ValueError:
        print("Error: Please provide a valid number for the number of words.")
