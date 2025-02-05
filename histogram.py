import re
import random
from collections import defaultdict


def histogram(text):
    words = re.findall(r'\b\w+\b', text.lower()
                       )
    histogram = defaultdict(int)
    for word in words:
        histogram[word] += 1
    return dict(histogram)


def unique_words(histogram):
    return len(histogram)


def frequency(word, histogram):
    return histogram.get(word.lower(), 0)


def save_histogram(histogram, filename="histogram.txt"):
    hist_items = list(histogram.items())

    def get_count(item):
        return item[1]

    hist_items.sort(reverse=True, key=get_count)

    with open(filename, "w", encoding="utf-8") as file:
        for word, count in hist_items:
            file.write(f"{word} {count}\n")


def stochastic_sampling(histogram):
    total_count = sum(histogram.values())
    threshold = random.uniform(0, total_count)
    cumulative = 0

    for word, count in histogram.items():
        cumulative += count
        if threshold <= cumulative:
            return word


if __name__ == "__main__":
    try:
        with open("wealth_of_nations.txt", "r", encoding="utf-8") as file:
            text = file.read()

        histogram = histogram(text)

        save_histogram(histogram)
        print("Histogram saved to 'histogram.txt'.")

        print("Histogram:", histogram)
        print("Unique words:", unique_words(histogram))
        print("Frequency of 'wealth':", frequency("wealth", histogram))
        print("Frequency of 'nations':", frequency("nations", histogram))
        print("Frequency of 'economy':", frequency(
            "economy", histogram))

        print("stochatic sampling func: ", stochastic_sampling(histogram))

    except FileNotFoundError:
        print("Error: File 'Wealth_of_Nations.txt' not found. Make sure it exists in the same directory.")
