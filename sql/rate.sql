create table rate
(
    rate_id SERIAL PRIMARY KEY ,
    car_id int,
    rate int,
    constraint fk_car foreign key (car_id) references car(car_id)
);