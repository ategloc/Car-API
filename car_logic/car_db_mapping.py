from sqlalchemy import create_engine, UniqueConstraint
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Base = declarative_base()


class Car(Base):
    __tablename__ = 'car'

    car_id: Mapped[int] = mapped_column(primary_key=True)
    car_name: Mapped[str] = mapped_column(String)
    car_make: Mapped[str] = mapped_column(String)

    __table_args__ = (UniqueConstraint('car_name', 'car_make', name='car_make_unique'),)

    def __repr__(self):
        return f"'car_id': {self.car_id}, 'car_name': {self.car_name}, 'car_make': {self.car_make}"
