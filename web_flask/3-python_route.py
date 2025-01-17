#!/usr/bin/python3
"""starts a Flask web application listening on 0.0.0.0, port 5000
Routes:
    /: display 'Hello HBNB!'
    /hbnb: display 'HBNB'
    /c/<text>: display 'C', followed by the value of the text variable
    /python/(<text>): display 'Python', followed bythevalue of text variable
use the option strict_slashes=False in your route definition"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Display 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """Display 'C', followed by the value of the text variable"""
    if '_' in text:
        text = text.replace('_', ' ')
        return "C {}".format(text)
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Display 'Python', followed by the value of the text variable"""
    if '_' in text:
        text = text.replace('_', ' ')
        return "Python {}".format(text)
    else:
        return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
