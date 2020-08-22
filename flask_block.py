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

if __name__ == "__main__":
    app.debug = True
    app.run()
