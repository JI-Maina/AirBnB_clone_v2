#!/usr/bin/python3
"""starts a Flask web application listening on 0.0.0.0, port 5000
Routes:
    /: display 'Hello HBNB!'
    /hbnb: display 'HBNB'
use the option strict_slashes=False in your route definition
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
