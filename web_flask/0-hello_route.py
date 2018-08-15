#!/usr/bin/python3
from flask import Flask
"""
Initializes flask app to listen on 0.0.0.0:5000
"""

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Hello HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
