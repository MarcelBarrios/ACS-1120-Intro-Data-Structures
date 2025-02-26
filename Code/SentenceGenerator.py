import random


class SentenceGenerator:
    """Generates a Markov Chain model and produces random sentences."""

    def __init__(self, filename):
        """Initialize with a filename and process the text."""
        self.filename = filename
        self.words = self.read_file()
        self.markov_chain = self.build_markov_chain()

    def read_file(self):
        """Reads a text file and returns a list of words."""
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                text = file.read()
            words = text.lower().split()  # Convert to lowercase and split into words
            return words
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            return []

    def build_markov_chain(self):
        """Creates a Markov chain (dictionary of word transitions)."""
        markov_chain = {}
        for i in range(len(self.words) - 1):
            word, next_word = self.words[i], self.words[i + 1]
            if word not in markov_chain:
                markov_chain[word] = []
            markov_chain[word].append(next_word)
        return markov_chain

    def generate_sentence(self, start_word=None, length=15):
        """Generates a random sentence using the Markov chain with weighted randomness."""
        if not self.markov_chain:
            return "Markov chain is empty. Unable to generate a sentence."

        if not start_word:
            # Pick a random start word
            start_word = random.choice(list(self.markov_chain.keys()))

        sentence = [start_word]

        for _ in range(length - 1):
            if sentence[-1] in self.markov_chain:
                next_words = self.markov_chain[sentence[-1]]

                # Build frequency dictionary
                frequency_dict = {}
                for word in next_words:
                    frequency_dict[word] = frequency_dict.get(word, 0) + 1

                # Implement weighted randomness using random.uniform()
                total = sum(frequency_dict.values())  # Total occurrences
                rand_val = random.uniform(0, total)

                cumulative = 0
                for word, freq in frequency_dict.items():
                    cumulative += freq
                    if rand_val <= cumulative:
                        next_word = word
                        break

                sentence.append(next_word)
            else:
                break  # Stop if there are no more transitions

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
