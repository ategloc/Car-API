from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from variables.db_variables import db_connection


def get_db_connection():
    return create_engine(db_connection, echo=True)


def get_session(engine=None):
    if engine is None:
        engine = get_db_connection()
    return sessionmaker(bind=engine)()
