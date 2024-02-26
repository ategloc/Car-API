create table car
(
    car_id SERIAL PRIMARY KEY ,
    car_name varchar(100),
    make_name varchar(100),
);

alter table car
    add constraint car_make_unique unique(car_name, car_make);