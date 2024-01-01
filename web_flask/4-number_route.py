#!/usr/bin/python3
"""
Flask web application
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/number/<int:n>")
def number_route(n):
    """
    display "n is a number" only if n is an integer
    """
    if isinstance(n, int):
        return str(n) + " is a number"


@app.route("/python")
@app.route("/python/<text>")
def python_route(text=None):
    """
    display “Python ”, followed by the value of the text
    """
    if text:
        q = ' '.join(text.split('_'))
    else:
        q = 'is cool'
    return "Python " + q


@app.route("/c/<text>")
def c_route(text):
    """
    display "C" followed by the value of the text variable
    """
    q = ' '.join(text.split('_'))
    return "C " + q


@app.route("/hbnb")
def hbnb_route():
    """
    return HBNB
    """
    return "HBNB"


@app.route("/")
def hello_route():
    """
    return page with message
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
