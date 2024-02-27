## Needed packeges: Flask, Sqlalchemy, psycopg2, requests
`pip install Flask sqlalchemy psycopg2 requests`

## Use api from cloud:
1. Use the endpoints on https://car-rental-api.herokuapp.com/


## How to run the app:
1. Install the needed packages
2.   
   1. If you want to use own database (postgreSQL advised) set it up, execute sql from file "sql/car.sql", then "sql/rate.sql" and fill up connection details in 'variables/db_variables.py'
   2. If you want to use my database, fill up connection details in 'variables/db_variables.py' with data proivided in the email. 
3. Run the app by running the command `python -m flask -app main run`
4. Use the endpoints on http://localhost:5000/

## Available endpoints:
- /cars
    - GET: Get all cars
    - POST: Add a car
      - parameters: 
        - Car_make: string
        - Car_name: string
- /popular
    - GET: Get the most popular cars
      - parameters: 
        - Amount: int - OPTIONAL amount of cars to return
- /rate
    - POST: Rate a car
      - parameters: 
        - Car_make: string
        - Car_name: string
        - Rating: int from 1-5





### Why I chose the technologies I used:
- Flask: I chose Flask because it is lightweight and easy to use. It is also very good for small projects and it is easy to set up.
- SQLAlchemy: I chose Sqlalchemy because i wanted to use an ORM, so the code is not dependent of database type.
- PostgreSQL: I chose Postgresql because it is very good for small projects and it is easy to set up and was available on Heroku.