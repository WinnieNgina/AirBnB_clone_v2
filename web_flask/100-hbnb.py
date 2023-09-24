#!/usr/bin/python3
"""display Hello HBNB!"""

from flask import Flask
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from flask import render_template


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hnbn_all():
    '''Display a HTML page like 8-index.html'''
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template("100-hbnb.html", states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def close_session(self):
    '''Removes current SQLAlchemy session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)