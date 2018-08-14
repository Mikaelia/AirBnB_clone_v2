#!/usr/bin/python3
from flask import Flask, render_template

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
def number(n):
        return "{} is a number".format(n)

@app.route('/number_template')
@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    return render_template('5-number.html', n=n)

app.run(host= '0.0.0.0')