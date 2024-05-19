#!/usr/bin/python3
"""Launches a Flask web application.

The web application listens on 0.0.0.0, port 5000.
Available routes:
    /: Returns the text 'Hello HBNB!'.
    /hbnb: Returns the text 'HBNB'.
    /c/<text>: Returns 'C' followed by the provided <text> value.
    /python/(<text>): Returns 'Python' followed by the provided <text> value.
    /number/<n>: Returns '<n> is a number' only if <n> is an integer.
"""
from flask import Flask, abort

app = Flask(__name__)


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """Returns 'C' followed by the provided <text> value.

    Underscores in <text> are replaced with spaces.
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text="is cool"):
    """Returns 'Python' followed by the provided <text> value.

    Underscores in <text> are replaced with spaces.
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Returns the text 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns the text 'HBNB'."""
    return "HBNB"


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """Returns '<n> is a number' only if <n> is an integer."""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

