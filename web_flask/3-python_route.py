#!/usr/bin/python3
"""display Hello HBNB!"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''
    script that starts a Flask web application:
    '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''display HBNB'''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_func(text):
    '''display “C ” followed by the value of the text variable'''
    text = text.replace('_', ' ')
    return ("C {}".format(text))


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_cool(text):
    '''display Python followed by the value of the text variable'''
    text = text.replace('_', ' ')
    return ("Python {}".format(text))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
