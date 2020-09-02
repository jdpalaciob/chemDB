""" Script to creates a DataBase with SQLAlchemy
"""

from sqlalchemy import create_engine, Column, Integer, String, Sequence, Numeric, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from db_credentials import credentials

DB = credentials['data_base']
USER = credentials['user_name']
PASWRD = credentials['password']
HOST = credentials['host']
PORT = credentials['port']

engine = create_engine(f'postgresql://{USER}:{PASWRD}@{HOST}:{PORT}/{DB}', echo=False)

Base = declarative_base()

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

Base.metadata.create_all(engine)

def insert_data(data, engine):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    session.add(data)
    session.commit()

def update_data(chem_id, new_data, engine):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

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
        # return f'The reactvie with chem_id = {chem_id} has been updated'
    else:
        # return f'The reactive with chem_id = {chem_id} is not registered'
        raise NameError(f'The reactive with chem_id = {chem_id} is not registered')

def delete_data(chem_id, engine):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    chem = session.query(Reactive).filter_by(chem_id=chem_id).first()
    session.delete(chem)

    session.commit()

def query_data(*, view_field='*', column=None, condition=None, engine):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    if column and condition:
        txt = text(f"SELECT {view_field} FROM reactives \
            WHERE {column} = '{condition}'")
        result = session.query(Reactive).from_statement(txt).all()
    else:
        txt = text(f"SELECT {view_field} FROM reactives")
        result = session.query(Reactive).from_statement(txt).all()
    return result


if __name__ == '__main__':

    # ADD
    reactive_1 = Reactive(chem_id='MAN-001',
                          name='Hydrochloric Acid',
                          chem_form='HCl',
                          cas_number='7647-01-0',
                          nature='INO',
                          ph_nature='acid',
                          quantity=12)
    # insert_data(reactive_1, engine)
    
    # UPDATE
    reactive_2 = Reactive(chem_id='CAC-001',
                          name='Sulfuric Acid',
                          chem_form='H2SO4',
                          cas_number='7664-93-9',
                          nature='INO',
                          ph_nature='acid',
                          quantity=28)
    # insert_data(reactive_2, engine)
    # update_data('CAC-001', reactive_2, engine)

    # delete_data('CAC-001', engine)

    h = query_data(column='chem_form', condition='HCl', engine=engine)
    print(h)
