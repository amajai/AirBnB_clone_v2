#!/usr/bin/python3
"""
Flask web application
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


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
