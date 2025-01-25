import random
import sys


def rearrange_words(words):
    random.shuffle(words)
    return words


if __name__ == "__main__":
    input_words = sys.argv[1:]
    if not input_words:
        print("Please provide words as command-line arguments.")
    else:
        rearranged = rearrange_words(input_words)
        print(" ".join(rearranged))
