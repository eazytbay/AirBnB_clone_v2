#!/usr/bin/python3
"""This script Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /cities_by_states: HTML page with a list of all states and related cities.
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


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Shows an HTML page with a list of states """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    """ Shows an HTML page with a list of cities by states """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []
    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])
    return render_template('8-cities_by_states.html',
                           states=st_ct,
                           h_1="States")


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
