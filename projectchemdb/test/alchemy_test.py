from projectchemdb.test.configuration_test import credentials
from projectchemdb.persistence.alchemy import Reactive, query_data, insert_data, delete_data, update_data
from sqlalchemy import create_engine

DB = credentials['data_base']
USER = credentials['user_name']
PASWRD = credentials['password']
HOST = credentials['host']
PORT = credentials['port']
engine = create_engine(f'postgresql://{USER}:{PASWRD}@{HOST}:{PORT}/{DB}', echo=False)

# ADD
reactive_1 = Reactive(chem_id='MAN-001',
                      name='Hydrochloric Acid',
                      chem_form='HCl',
                      cas_number='7647-01-0',
                      nature='INO',
                      ph_nature='acid',
                      quantity=12)

insert_data(reactive_1, engine)
h = query_data(column='chem_form', condition='HCl', engine=engine)
print(h)

# UPDATE
reactive_2 = Reactive(chem_id='CAC-001',
                      name='Sulfuric Acid',
                      chem_form='H2SO4',
                      cas_number='7664-93-9',
                      nature='INO',
                      ph_nature='acid',
                      quantity=28)
insert_data(reactive_2, engine)
update_data('CAC-001', reactive_2, engine)
delete_data('CAC-001', engine)

h = query_data(column='chem_form', condition='HCl', engine=engine)
print(h)
