""" Script for develop the data base block of chemDB  """
import psycopg2 as psql

def stablish_connection(data_base, user_name=None, password=None):
    """ Stablish connection and creates table """

    conn = psql.connect(
        dbname=data_base,
        user=user_name,
        password=password,
        host='localhost',
        port=5432
        )
    cur = conn.cursor()

    cur.execute(
        'CREATE TABLE IF NOT EXISTS reactives (\
            id SERIAL PRIMARY KEY,\
            name VARCHAR(100) NOT NULL,\
            chem_form VARCHAR(15),\
            CAS_number VARCHAR(50) UNIQUE,\
            nature CHAR(3),\
            ph_nature VARCHAR(5),\
            Quantity NUMERIC(6,2) DEFAULT 0\
            );'
        )
    conn.commit()
    conn.close()

def inserting_data(*, name, chem_formula=None, cas_number=None, nature=None, ph_nature=None,
                   quantity=None, data_base, user_name=None, password=None):
    """ Allows user to introduce records to the table in DB """

    conn = psql.connect(
        dbname=data_base,
        user=user_name,
        password=password,
        host='localhost',
        port=5432
        )
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO reactives (\
        name, chem_form, CAS_number, nature, ph_nature, Quantity)\
        VALUES (%s,%s,%s,%s,%s,%s);", (name, chem_formula, cas_number, nature, ph_nature, quantity)
        )
    conn.commit()
    conn.close()

if __name__ == '__main__':

    DB = 'chemDB'
    USER = 'plant_chief'
    PASWRD = 'plant123'

    stablish_connection(DB, USER, PASWRD)

    NAME = 'Hydrochloric Acid'
    FORMULA = 'HCl'
    CAS = '7647-10-0'
    NATURE = 'INO'
    PH = 'acid'
    QUANTITY = 12

    inserting_data(name=NAME, chem_formula=NAME, cas_number=CAS, nature=NATURE, ph_nature=PH, quantity=QUANTITY,
                   data_base=DB, user_name=USER, password=PASWRD)
    