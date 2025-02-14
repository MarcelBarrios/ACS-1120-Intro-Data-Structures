"""Main script, uses other modules to generate sentences."""
from flask import Flask
import re
import random
from collections import defaultdict
from histogram import histogram, unique_words, frequency, save_histogram, stochastic_sampling

app = Flask(__name__)

# https://acs-1120-intro-data-structures-1-9xbj.onrender.com/
# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.
with open("wealth_of_nations.txt", "r", encoding="utf-8") as file:
    text = file.read()

histogram = histogram(text)

save_histogram(histogram)


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    return f"<p>Twitt Generator</p> <p>Histogram: {str(histogram)}</p>"


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""

    app.run(debug=True)
