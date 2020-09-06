""" Script to creates a DataBase with SQLAlchemy
"""

from sqlalchemy import Column, String, Numeric, text, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

my_metadata = MetaData()
Base = declarative_base(metadata=my_metadata)


class Reactive(Base):
    __tablename__ = 'reactives'

    chem_id = Column(String(7), primary_key=True)
    name = Column(String(100), nullable=False)
    chem_form = Column(String(20))
    cas_number = Column(String(12), unique=True)
    nature = Column(String(3))
    ph_nature = Column(String(5))
    quantity = Column(Numeric(6, 2), default=0)

    def __repr__(self):
        expression = f"""chem_id={self.chem_id}, name={self.name}, cas_number={self.cas_number}, nature={self.nature}, ph_nature={self.ph_nature}, quantity={self.quantity}"""
        return expression


def insert_data(data, engine):
    db_session = sessionmaker(bind=engine)
    session = db_session()
    session.add(data)
    session.commit()


def update_data(chem_id, new_data, engine):
    db_session = sessionmaker(bind=engine)
    session = db_session()
    chem = session.query(Reactive).filter_by(chem_id=chem_id).first()

    if chem:
        if new_data.name:
            chem.name = new_data.name
        if new_data.chem_form:
            chem.chem_form = new_data.chem_form
        if new_data.cas_number:
            chem.cas_number = new_data.cas_number
        if new_data.nature:
            chem.nature = new_data.nature
        if new_data.ph_nature:
            chem.ph_nature = new_data.ph_nature
        if new_data.quantity:
            chem.quantity = new_data.quantity
        return session.commit()
    else:
        raise NameError(f'The reactive with chem_id = {chem_id} is not registered')


def delete_data(chem_id, engine):
    db_session = sessionmaker(bind=engine)
    session = db_session()
    chem = session.query(Reactive).filter_by(chem_id=chem_id).first()
    session.delete(chem)
    session.commit()


def query_data(*, view_field='*', column=None, condition=None, engine):
    db_session = sessionmaker(bind=engine)
    session = db_session()

    if column and condition:
        txt = text(f"SELECT {view_field} FROM reactives \
            WHERE {column} = '{condition}'")
        result = session.query(Reactive).from_statement(txt).all()
    else:
        txt = text(f"SELECT {view_field} FROM reactives")
        result = session.query(Reactive).from_statement(txt).all()
    return result
