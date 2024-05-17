#!/usr/bin/python3
""" Module that display “Hello HBNB! """

from flask import Flask

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
    return "Welcome to HBNB!"


# run the development server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
