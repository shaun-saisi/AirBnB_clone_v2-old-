#!/usr/bin/python3
"""Launches a Flask web application.

The web application will be available on 0.0.0.0:5000.
Available routes:
    /: Returns the text 'Hello HBNB!'.
    /hbnb: Returns the text 'HBNB'.
    /c/<text>: Returns 'C' followed by the provided <text> value,
               where underscores in <text> are replaced with spaces.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """Returns 'C' followed by the provided <text> value."""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Returns the text 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns the text 'HBNB'."""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

