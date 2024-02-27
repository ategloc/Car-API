from car_logic.car_db_mapping import Car
from car_logic.car_functions import get_car
from rate_logic.rate_db_mapping import Rate
from db_connection.db_connection import get_session
from sqlalchemy import func, desc


def add_rate(car_name, car_make, rate: int):
    if rate < 1 or rate > 5:
        raise ValueError('Rate must be between 1 and 5')
    session = get_session()
    car = get_car(car_name, car_make)
    if car is None:
        raise ValueError('Car does not exist')
    rate = Rate(car_id=car.car_id, rate=rate)
    try:
        session.add(rate)
        session.commit()
    except Exception as e:
        session.rollback()
        raise RuntimeError(str(e))
    session.close()
    return rate


def get_all_avg_rates():
    session = get_session()
    avg_rates_query = (
        session.query(
            Car, func.avg(Rate.rate).label('avg_rate')
        )
        .outerjoin(Rate, Car.car_id == Rate.car_id)
        .group_by(Car.car_id)
        .all()
    )
    session.close()
    return_list = []
    for row in avg_rates_query:
        return_list.append({"car": row.tuple()[0], "avg_rate": row.tuple()[1]})
    return return_list


def get_n_popular_cars(n: int = 10000):
    session = get_session()
    cars_query = (
        session.query(
            Car, func.count(Rate.rate_id).label('rate_amount')
        )
        .outerjoin(Rate, Car.car_id == Rate.car_id)
        .group_by(Car.car_id)
        .order_by(desc('rate_amount'))
        .limit(n)
        .all()
    )
    session.close()
    return_list = []
    for row in cars_query:
        return_list.append({"car": row.tuple()[0], "amount_of_rates": row.tuple()[1]})
    return return_list


if __name__ == '__main__':
    # add_rate('Civic', 'Honda', 5)
    print(get_n_popular_cars(5))
