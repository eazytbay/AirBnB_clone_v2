#!/usr/bin/python3
"""This script Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>.
"""
from models import storage
from models.state import State
from os import environ
from flask import Flask, render_template
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_state(id=""):
    """ displays a HTML page with a list of cities by states """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    found = 0
    state = ""
    cities = []

    for x in states:
        if id == x.id:
            state = x
            found = 1
            break
    if found:
        states = sorted(state.cities, key=lambda k: k.name)
        state = state.name

    if id and not found:
        found = 2

    return render_template('9-states.html',
                           state=state,
                           array=states,
                           found=found)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
