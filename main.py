from flask import Flask, request, Response
from car_logic.car_functions import add_car
from rate_logic.rate_functions import add_rate, get_n_popular_cars, get_all_avg_rates

app = Flask(__name__)


@app.get('/cars')
def get_cars():
    cars = get_all_avg_rates()
    return_dict = {
        "Count": len(cars),
        "Cars": []
    }
    for row in cars:
        return_dict['Cars'].append(
            {
                "Car": {
                    "car_id": row['car'].car_id,
                    "car_name": row['car'].car_name,
                    "car_make": row['car'].car_make,
                },
                "Avg_rate": row['avg_rate']
            }
        )
    return return_dict


@app.get('/popular')
def get_popular():
    amount = request.args.get('Amount')
    if amount is None:
        amount = 10000
    try:
        cars = get_n_popular_cars(int(amount))
    except ValueError as e:
        return Response(str(e), status=400)
    return_dict = {
        "Count": len(cars),
        "Cars": []
    }
    for row in cars:
        return_dict['Cars'].append(
            {
                "Car": {
                    "car_id": row['car'].car_id,
                    "car_name": row['car'].car_name,
                    "car_make": row['car'].car_make,
                },
                "Amount_of_rates": row['amount_of_rates']
            }
        )
    return return_dict


@app.post('/cars')
def post_cars():
    try:
        if add_car(request.form['Car_name'], request.form['Car_make']):
            return 'Car added'
        return 'Car not added'
    except ValueError as e:
        return Response(str(e), status=400)


@app.post('/rate')
def post_rate():
    try:
        if add_rate(request.form['Car_name'], request.form['Car_make'], int(request.form['Rate'])):
            return 'Rate added'
        return 'Rate not added'
    except Exception as e:
        return Response(str(e), status=400)
