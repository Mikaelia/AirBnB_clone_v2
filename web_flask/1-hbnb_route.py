#!/usr/bin/python3
from flask import Flask
"""
Script to start Flask application and create /hbnb view function
"""
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Hello HBNB"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
