#!/usr/bin/python3
""" Module that display “Hello HBNB! """

from flask import Flask, render_template

# instantiate app
app = Flask(__name__)

# create the index or home route


@app.route('/')
def index():
    """A route controller for the index page """
    return "Hello HBNB!"


# create the /hbnb route
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """A route controller for the hbnb page """
    return "HBNB"


# creates a /c/<text> route
@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """A route controller for the /c/<text> page """
    content = text.replace("_", " ")
    return (f'C {content}')


# creates a /python/<text> route
@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_route(text='is cool'):
    """A route controller for the /python/<text> page """
    content = text.replace("_", " ")
    return f'Python {content}'


# route that displays "n is a number" only if n is an integer
@app.route('/number/<int:n>', strict_slashes=False)
def isNumber(n):
    """display "n is a number" only if n is an int"""
    return f'{n} is a number'


# route that display a HTML page only if n is an integer
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


# route that display a HTML page only if n is an integer
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """display a HTML page only if n is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)


# run the development server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
