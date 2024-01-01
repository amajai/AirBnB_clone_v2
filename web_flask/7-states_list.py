#!/usr/bin/python3
"""
Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ def doc """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(error):
    """
    close storage
    """
    storage.close()


@app.route("/number_odd_or_even/<int:n>")
def odd_even_route(n):
    """
    display a HTML page only if n is an integer
    """
    if n % 2 == 0:
        oe = 'even'
    else:
        oe = 'odd'
    if isinstance(n, int):
        return render_template("6-number_odd_or_even.html", num=n, odd_even=oe)


@app.route("/number_template/<int:n>")
def number_template_route(n):
    """
    display a HTML page only if n is an integer
    """
    if isinstance(n, int):
        return render_template("5-number.html", num=n)


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
