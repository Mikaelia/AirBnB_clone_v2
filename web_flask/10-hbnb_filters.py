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
    states = storage.all('State')
    cities = storage.all('City')
    amenities = storage.all('Amenity')
    
    state_list = [v for v in cities.values() if v.state_id == id]
    city_list = [v for v in cities.values() if v.state_id == id]
    amenity_list = [v for v in cities.values() if v.state_id == id]
    return render_template(
        '10-hbnb_filters.html',
        states=state_list,
        cities=city_list,
        amenities=amenity_list)


@app.teardown_appcontext
def teardown(value):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
