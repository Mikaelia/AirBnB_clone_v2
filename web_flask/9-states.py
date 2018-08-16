#!/usr/bin/python3
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def cities_by_state():
    states = storage.all('State')
    state_list = [v for v in states.values()]
    return render_template('9-states.html', states=state_list)


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    state_found = None
    states = storage.all('State')
    for v in states.values():
        if id == v.id:
            state_found = v
    cities = storage.all('City')
    city_list = [v for v in cities.values() if v.state_id == id]
    return render_template(
        '9-states.html',
        state_found=state_found,
        cities=city_list)


@app.teardown_appcontext
def teardown(value):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
