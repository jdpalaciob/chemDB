""" Script to develop the API REST block of chemDB

DB = 'chemDB'
USER = 'plant_chief'
PASWRD = 'plant123'
"""

from flask import Flask, request
import postgres_db as pdb

app = Flask(__name__)

@app.route('/')
def homepage():
    # parameters in the form ?key=value
    name = request.args.get('name')
    last = request.args.get('last')
    return f'Hello {name} {last}'

@app.route('/chemDB')
def connection():
    DB = request.args.get('db')
    USER = request.args.get('user')
    PASWRD = request.args.get('pword')
    pdb.stablish_connection(data_base=DB, user_name=USER, password=PASWRD)
    return 'Access to Data Base granted'

@app.route('/chemDB/insert', methods=['GET','POST'])
def insertion():
    DB = request.args.get('db')
    USER = request.args.get('user')
    PASWRD = request.args.get('pword')

    chem_id = request.form['chem_id']
    name = request.form['name']
    chem_formula = request.form['chem_formula']
    cas = request.form['cas_number']
    nature = request.form['nature']
    ph = request.form['ph_nature']
    quantity = request.form['quantity']

    pdb.inserting_data(chem_id=chem_id, name=name, chem_formula=chem_formula, cas_number=cas, nature=nature, ph_nature=ph, quantity=quantity,
                        data_base=DB, user_name=USER, password=PASWRD)
    return f'REACTIVE {chem_id} HAS BEEN INSERTED'

if __name__ == "__main__":
    app.debug = True
    app.run()
