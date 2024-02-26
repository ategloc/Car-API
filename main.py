from flask import Flask, request, Response
from car_logic.car_functions import add_car

app = Flask(__name__)


@app.get('/cars')
def get_cars():
    return 'NOT IMPLEMENTED'
@app.get('/popular')
def get_popular():
    return 'NOT IMPLEMENTED'

@app.post('/cars')
def post_cars():
    try:
        if add_car(request.form['car_name'], request.form['car_make']):
            return 'Car added'
        return 'Car not added'
    except ValueError as e:
        return Response(str(e), status=400)


@app.post('/rate')
def post_rate():
    return 'NOT IMPLEMENTED'