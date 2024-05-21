#!/usr/bin/python3
"""Modeule that starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /states_list: HTML page with a list of all State objects in DBStorage.
"""

from models import storage
from flask import Flask, render_template
import sys
import os

# Get the absolute path to the root directory of your project
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ROOT_DIR)


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Returns an HTML page consisting of list of cities by
    states """
    states = storage.all("State")
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
