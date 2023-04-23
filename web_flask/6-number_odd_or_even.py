#!/usr/bin/python3
"""starts a Flask web application listening on 0.0.0.0, port 5000
Routes:
    /: display 'Hello HBNB!'
    /hbnb: display 'HBNB'
    /c/<text>: display 'C', followed by the value of the text variable
    /python/(<text>): display 'Python', followed by the value of text variable
    /number/<n>: display 'n is a number' only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer
    /number_odd_or_even/<n>: display a HTML page only if n is an integer
use the option strict_slashes=False in your route definition"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Display 'C', followed by the value of the text variable"""
    if '_' in text:
        text = text.replace('_', ' ')
        return "C {}".format(text)
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python', followed by the value of the text variable"""
    if '_' in text:
        text = text.replace('_', ' ')
        return "Python {}".format(text)
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display 'n is a number' only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display a HTML page only if n is an integer"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
