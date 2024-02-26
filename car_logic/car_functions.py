from car_logic.car_db_connection import Car, get_session
import requests


def add_car(car_name, car_make):
    session = get_session()
    if not check_if_car_exists(car_name, car_make):
        raise ValueError('Car does not exist')
    car = Car(car_name=car_name, car_make=car_make)
    try:
        session.add(car)
        session.commit()
    except:
        session.rollback()
        raise ValueError('Car already exists')
    session.close()
    return car


def check_if_car_exists(car_name, car_make):
    cars_by_make = requests.get(
        f'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{car_make}?format=json'
    ).json().get('Results')
    for car in cars_by_make:
        if car.get('Model_Name') == car_name:
            return True
    return False

if __name__ == '__main__':
    add_car('Civic', 'Honda')