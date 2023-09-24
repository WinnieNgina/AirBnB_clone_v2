#!/usr/bin/python3
"""display Hello HBNB!"""

from flask import Flask
from models import storage
from models.state import State
from flask import render_template


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    '''
    script that starts a Flask web application:
    '''
    states = storage.all(State)
    return render_template('9-states.html', state=states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    '''State object is found with this id'''
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def close_session(self):
    '''Removes current SQLAlchemy session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
