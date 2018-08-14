#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello HBNB"

app.run(host= '0.0.0.0')