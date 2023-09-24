#!/usr/bin/python3
"""display Hello HBNB!"""

from flask import Flask
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import render_template


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hnbn_filter():
    '''Display a HTML page like 6-index.html'''
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


@app.teardown_appcontext
def close_session(self):
    '''Removes current SQLAlchemy session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
