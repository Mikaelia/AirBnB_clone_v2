#!/usr/bin/python3
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    states = storage.all('State')
    state_list = [v for v in states.values()]
    cities = storage.all('City')
    city_list = [v for v in cities.values()]
    return render_template('8-cities_by_states.html', cities=city_list, states=state_list)

@app.teardown_appcontext
def teardown(value):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
