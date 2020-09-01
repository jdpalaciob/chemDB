""" Script to creates a DataBase with SQLAlchemy
"""

from sqlalchemy import create_engine, Column, Integer, String, Sequence, Numeric
from sqlalchemy.ext.declarative import declarative_base
from db_credentials import credentials

DB = credentials['data_base']
USER = credentials['user_name']
PASWRD = credentials['password']
HOST = credentials['host']
PORT = credentials['port']

engine = create_engine(f'postgresql://{USER}:{PASWRD}@{HOST}:{PORT}/{DB}')

Base = declarative_base()

class Reactvie(Base):
    __tablename__ = 'reactives'

    id = Column(Integer, Sequence('id'))
    chem_id = Column(String(7), primary_key=True)
    name = Column(String(100), nullable=False)
    chem_form = Column(String(20))
    cas_number = Column(String(12), unique=True)
    nature = Column(String(3))
    ph_nature = Column(String(5))
    quantity = Column(Numeric(6, 2), default=0)

Base.metadata.create_all(engine)
