import random


def generate_anagram(word):
    letters = list(word.replace(" ", ""))
    random.shuffle(letters)
    return "".join(letters)


if __name__ == "__main__":
    user_input = input("Enter a word or phrase to generate an anagram: ")
    if not user_input.strip():
        print("Please enter a valid word or phrase.")
    else:
        anagram = generate_anagram(user_input)
        print(f"Anagram: {anagram}")
