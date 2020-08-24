""" Script to develop the API REST block of chemDB
"""

from flask import Flask, request, Response
import postgres_db as pdb
from db_credentials import credentials

app = Flask(__name__)

@app.route('/chemDB')
def connection():
    DB = credentials['data_base']
    USER = credentials['user_name']
    PASWRD = credentials['password']
    pdb.stablish_connection(data_base=DB, user_name=USER, password=PASWRD)
    return Response('Access to Data Base granted', status=200)

@app.route('/chemDB/insert', methods=['POST'])
def insertion():
    DB = credentials['data_base']
    USER = credentials['user_name']
    PASWRD = credentials['password']

    req_body = request.get_json()
    pdb.inserting_data(
                       chem_id=req_body.get('chem_id', None),
                       name=req_body.get('name', None),
                       chem_formula=req_body.get('chem_formula', None),
                       cas_number=req_body.get('cas_number', None),
                       nature=req_body.get('nature', None),
                       ph_nature=req_body.get('ph_nature'),
                       quantity=req_body.get('quantity', None),
                       data_base=DB, user_name=USER, password=PASWRD)
    return Response(f'REACTIVE {req_body["chem_id"]} HAS BEEN INSERTED', status=200)

@app.route('/chemDB/update', methods=['PUT'])
def update():
    DB = credentials['data_base']
    USER = credentials['user_name']
    PASWRD = credentials['password']

    req_body = request.get_json()
    pdb.upgrade_data(
                    chem_id=req_body.get('chem_id', None),
                    name=req_body.get('name', None),
                    chem_formula=req_body.get('chem_formula', None),
                    cas_number=req_body.get('cas_number', None),
                    nature=req_body.get('nature', None),
                    ph_nature=req_body.get('ph_nature'),
                    quantity=req_body.get('quantity', None),
                    data_base=DB, user_name=USER, password=PASWRD)
    return Response(f'REACTIVE {req_body["chem_id"]} HAS BEEN UPDATED', status=200)

@app.route('/chemDB/delete', methods=['DELETE'])
def delete():
    DB = credentials['data_base']
    USER = credentials['user_name']
    PASWRD = credentials['password']

    req_body = request.get_json()
    pdb.delete_data(
                    chem_id=req_body.get('chem_id', None),
                    data_base=DB, user_name=USER, password=PASWRD)
    return Response(f'REACTIVE {req_body["chem_id"]} HAS BEEN DELETED', status=200)

@app.route('/chemDB/info', methods=['GET'])
def query():
    DB = credentials['data_base']
    USER = credentials['user_name']
    PASWRD = credentials['password']

    view = request.args.get('view')
    column = request.args.get('where')
    condition = request.args.get('equals')

    data = pdb.view_data(
                view_field=view, column=column, condition_value=condition,
                data_base=DB, user_name=USER, password=PASWRD)

    str_row = []
    for row in data:
        row = [str(i) for i in row]
        string = ' | '.join(row)
        str_row.append(string)
    table = '\n'.join(str_row)

    return Response(table, status=200)



if __name__ == "__main__":
    app.debug = True
    app.run()
