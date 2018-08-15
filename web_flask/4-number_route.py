#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Hello HBNB"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def route(n):
    return "{} is a number".format(n)


app.run(host='0.0.0.0')
