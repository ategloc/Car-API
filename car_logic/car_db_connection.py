from sqlalchemy import create_engine, UniqueConstraint
from sqlalchemy.orm import Mapped, relationship, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey
from variables.db_variables import db_connection
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Car(Base):
    __tablename__ = 'car'
    car_id = Column(Integer, primary_key=True)
    car_name = Column(String)
    car_make = Column(String)

    __table_args__ = (UniqueConstraint('car_name', 'car_make', name='car_make_unique'),)

    def __repr__(self):
        return f'Car: {self.car_name} - {self.car_make}'


def get_db_connection():
    return create_engine(db_connection, echo=True)


def get_session(engine=None):
    if engine is None:
        engine = get_db_connection()
    return sessionmaker(bind=engine)()
