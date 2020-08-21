""" Script for develop the data base block of chemDB  """
import psycopg2 as psql


def non_null(*arg):
    """ filters the None (SQL NULL) arguments and cretes SQL column asociation"""
    result = []
    columns = ['name', 'chem_formula', 'cas_number', 'nature', 'ph_nature', 'quantity']
    for columns, value in zip(columns, arg):
        if value and value != '':
            string = columns + f"='{value}'"
            result.append(string)
    return ', '.join(result)

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
            id SERIAL,\
            chem_id CHAR(7) NOT NULL PRIMARY KEY,\
            name VARCHAR(100) NOT NULL,\
            chem_form VARCHAR(20),\
            CAS_number CHAR(12) UNIQUE,\
            nature CHAR(3),\
            ph_nature VARCHAR(5),\
            Quantity NUMERIC(6,2) DEFAULT 0\
            );'
        )
    conn.commit()
    conn.close()

def inserting_data(*, chem_id, name, chem_formula=None, cas_number=None, nature=None, ph_nature=None,
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
        chem_id, name, chem_form, CAS_number, nature, ph_nature, Quantity)\
        VALUES (%s,%s,%s,%s,%s,%s,%s);",
        (chem_id, name, chem_formula, cas_number, nature, ph_nature, quantity)
        )
    conn.commit()
    conn.close()

def upgrade_data(*, chem_id, name=None, chem_formula=None, cas_number=None, nature=None, ph_nature=None,
                   quantity=None, data_base, user_name=None, password=None):
    """ Allows the user to update some or all fields for a reactive """
    conn = psql.connect(
        dbname=data_base,
        user=user_name,
        password=password,
        host='localhost',
        port=5432
        )
    cur = conn.cursor()

    columns_modifier = non_null(name, chem_formula, cas_number, nature, ph_nature, quantity)

    cur.execute(
        "UPDATE reactives\
        SET " +  columns_modifier +
        f" WHERE chem_id='{chem_id}';"
        )
    conn.commit()
    conn.close()

def view_data(*, view_field='*', column=None, condition_value=None,
              data_base, user_name=None, password=None):
    """ Allows the user to search for data """

    conn = psql.connect(
        dbname=data_base,
        user=user_name,
        password=password,
        host='localhost',
        port=5432
        )
    cur = conn.cursor()

    if column and condition_value:

        cur.execute(
            f"SELECT {view_field} FROM reactives \
            WHERE {column}='{condition_value}';"
        )
    else:
        cur.execute(
            f"SELECT {view_field} FROM reactives;"
        )

    data = cur.fetchall()
    conn.close()
    return data

if __name__ == '__main__':

    DB = 'chemDB'
    USER = 'plant_chief'
    PASWRD = 'plant123'

    stablish_connection(DB, USER, PASWRD)

    CHEM_ID = 'MAN-001'
    NAME = 'Hydrochloric Acid'
    FORMULA = 'HCl'
    CAS = '7647-10-0'
    NATURE = 'INO'
    PH = 'acid'
    QUANTITY = 12

    inserting_data(chem_id=CHEM_ID, name=NAME, chem_formula=FORMULA, cas_number=CAS, nature=NATURE, ph_nature=PH, quantity=QUANTITY,
                   data_base=DB, user_name=USER, password=PASWRD)

    CHEM_ID = 'MAN-001'
    NAME = 'chlorine'
    PH = 'gas'
    QUANTITY = 20

    upgrade_data(chem_id = CHEM_ID, name=NAME, quantity=QUANTITY,
                 data_base=DB, user_name=USER, password=PASWRD)

    VIEW = '*'
    COLUMN = None
    CONDITION = None
    info = view_data(view_field=VIEW, column=COLUMN, condition_value=CONDITION,
                     data_base=DB, user_name=USER, password=PASWRD)
    for row in info:
        for i in row:
            print(i, end=' | ')
        print()
    print()
