import sys
import random


def load_words(file_path="/usr/share/dict/words"):
    try:
        with open(file_path, 'r') as file:
            return set(word.strip().lower() for word in file)
    except FileNotFoundError:
        print("Error: Words file not found!")
        sys.exit(1)


def generate_anagrams(input_word, word_list):

    from itertools import permutations

    all_permutations = set("".join(p) for p in permutations(input_word))

    valid_anagrams = all_permutations.intersection(word_list)

    valid_anagrams.discard(input_word.lower())

    return sorted(valid_anagrams)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    words = load_words()

    input_word = sys.argv[1].lower()

    anagrams = generate_anagrams(input_word, words)

    if anagrams:
        print(f"Anagrams for '{input_word}': {', '.join(anagrams)}")
    else:
        print(f"No anagrams found for '{input_word}'.")
