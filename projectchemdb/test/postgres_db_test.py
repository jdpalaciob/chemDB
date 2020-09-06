from projectchemdb.persistence.postgres_db import stablish_connection, inserting_data, upgrade_data, delete_data, \
    view_data

DB = 'python_chem_db'
USER = 'postgres'
PASWRD = 'postgres'
HOST = 'database-2.cjdum0pi52ge.us-east-1.rds.amazonaws.com'

stablish_connection(DB, USER, PASWRD, HOST)

CHEM_ID = 'MAN-001'
NAME = 'Hydrochloric Acid'
FORMULA = 'HCl'
CAS = '7647-10-0'
NATURE = 'INO'
PH = 'acid'
QUANTITY = 12

inserting_data(chem_id=CHEM_ID, name=NAME, chem_formula=FORMULA, cas_number=CAS, nature=NATURE, ph_nature=PH,
               quantity=QUANTITY,
               data_base=DB, user_name=USER, password=PASWRD, host=HOST)

CHEM_ID = 'MAN-001'
NAME = 'chlorine'
PH = 'gas'
QUANTITY = 20

upgrade_data(chem_id=CHEM_ID, name=NAME, quantity=QUANTITY, data_base=DB, user_name=USER, password=PASWRD, host=HOST)

VIEW = '*'
COLUMN = None
CONDITION = None
info = view_data(view_field=VIEW, column=COLUMN, condition_value=CONDITION, data_base=DB, user_name=USER,
                 password=PASWRD, host=HOST)
for row in info:
    for i in row:
        print(i, end=' | ')
    print()
print()

delete_data(chem_id='MAN-001', data_base=DB, user_name=USER, password=PASWRD, host=HOST)
