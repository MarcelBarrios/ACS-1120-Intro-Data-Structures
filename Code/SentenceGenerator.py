import random
import re


class SentenceGenerator:
    """Generates a Markov Chain model using trigrams and produces random sentences."""

    def __init__(self, filename):
        """Initialize with a filename and process the text."""
        self.filename = filename
        self.words = self.read_file()
        self.markov_chain = self.build_markov_chain()

    def read_file(self):
        """Reads a text file, removes non-word characters, and returns a list of words."""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                text = file.read().lower()  # Convert to lowercase

            # Remove all characters that are not letters or spaces
            cleaned_text = re.sub(r"[^a-z\s]", "", text)

            # Split into words
            words = cleaned_text.split()
            return words

        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            return []

    def build_markov_chain(self):
        """Creates a Markov chain using trigrams (triples of words)."""
        markov_chain = {}

        for i in range(len(self.words) - 2):
            key = (self.words[i], self.words[i + 1])  # Two-word key (bigram)
            next_word = self.words[i + 2]  # Next word to follow

            if key not in markov_chain:
                markov_chain[key] = []
            markov_chain[key].append(next_word)

        return markov_chain

    def generate_sentence(self, start_words=None, length=15):
        """Generates a random sentence using the Markov chain with weighted randomness."""
        if not self.markov_chain:
            return "Markov chain is empty. Unable to generate a sentence."

        if not start_words or start_words not in self.markov_chain:
            # Pick a random start word pair
            start_words = random.choice(list(self.markov_chain.keys()))

        sentence = list(start_words)

        for _ in range(length - 2):  # Already have 2 words
            key = (sentence[-2], sentence[-1])  # Use last two words as key

            if key in self.markov_chain:
                next_words = self.markov_chain[key]

                # Use weighted randomness
                frequency_dict = {}
                for word in next_words:
                    frequency_dict[word] = frequency_dict.get(word, 0) + 1

                total = sum(frequency_dict.values())
                rand_val = random.uniform(0, total)

                cumulative = 0
                for word, freq in frequency_dict.items():
                    cumulative += freq
                    if rand_val <= cumulative:
                        next_word = word
                        break

                sentence.append(next_word)
            else:
                break  # Stop if no transitions exist

        return " ".join(sentence)


# ---------------- MAIN EXECUTION ----------------
if __name__ == "__main__":
    filename = "wealth_of_nations.txt"

    # Create MarkovChainGenerator instance
    markov_generator = SentenceGenerator(filename)

    # Generate a random sentence
    random_sentence = markov_generator.generate_sentence(length=15)

    # Print results
    print("Randomly Generated Sentence:")
    print(random_sentence)
