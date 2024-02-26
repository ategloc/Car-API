from flask import Flask, request
from car_logic.car_functions import add_car

app = Flask(__name__)


@app.get('/cars')
def get_cars():
    add_car(request.form['car_name'], request.form['car_make'])

@app.get('/popular')
def get_popular():
    return 'Popular'

@app.post('/cars')
def post_cars():
    return 'Cars'

@app.post('/rate')
def post_rate():
    return 'Rate'