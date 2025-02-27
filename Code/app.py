"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
import re
import random
from collections import defaultdict
from histogram import histogram, unique_words, frequency, save_histogram, stochastic_sampling
from SentenceGenerator import SentenceGenerator

app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.
filename = "wealth_of_nations.txt"
markov_generator = SentenceGenerator(filename)


@app.route("/")
def home():
    """Route that returns a web page containing the generated sentence."""
    sentence = markov_generator.generate_sentence(length=15)
    return render_template("index.html", sentence=sentence)


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""

    app.run(debug=True)
