from sqlalchemy import create_engine, UniqueConstraint
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from car_logic.car_db_mapping import Car

Base = declarative_base()


class Rate(Base):
    __tablename__ = 'rate'
    rate_id: Mapped[int] = mapped_column(primary_key=True)
    car_id: Mapped[int] = mapped_column(ForeignKey(Car.car_id))
    rate: Mapped[int] = mapped_column(Integer)

    def __repr__(self):
        return f"'Car_id': {self.car_id}, 'Rate': {self.rate}"
