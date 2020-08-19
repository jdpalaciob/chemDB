""" Script for develop the data base block of chemDB  """
import psycopg2 as psql

def stablish_connection(data_base, user_name=None, password=None):
    conn = psql.connect(dbname=data_base, user=user_name, password=password, host='localhost', port=5432)
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS \
            reactives (id SERIAL PRIMARY KEY, name VARCHAR)'
        )
    conn.commit()
    conn.close()


if __name__ == '__main__':

    DB = 'chemDB'
    USER = 'plant_chief'
    PASWRD = 'plant123'

    stablish_connection(DB, USER, PASWRD)
