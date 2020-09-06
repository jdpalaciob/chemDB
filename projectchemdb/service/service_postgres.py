from projectchemdb.configuration.db_credentials import credentials
from projectchemdb.persistence import postgres_db as pdb

DB = credentials['data_base']
USER = credentials['user_name']
PASWRD = credentials['password']
HOST = credentials['host']


def check_data_base_status():
    try:
        pdb.stablish_connection(data_base=DB, user_name=USER, password=PASWRD, host=HOST)
        message = 'Access to Data Base granted'
        code_status = 200
        return message, code_status
    except Exception as ex:
        message = f'Error executing the check status of the databes. {ex}'
        code_status = 400
        return message, code_status


def insert_data(request_body):
    try:
        pdb.inserting_data(
            chem_id=request_body.get('chem_id', None),
            name=request_body.get('name', None),
            chem_formula=request_body.get('chem_formula', None),
            cas_number=request_body.get('cas_number', None),
            nature=request_body.get('nature', None),
            ph_nature=request_body.get('ph_nature'),
            quantity=request_body.get('quantity', None),
            data_base=DB, user_name=USER, password=PASWRD, host=HOST)
        message = f'REACTIVE {request_body["chem_id"]} HAS BEEN INSERTED'
        code_status = 200
        return message, code_status
    except Exception as ex:
        message = f'Error executing the insert query. {ex}'
        code_status = 400
        return message, code_status


def update_data(request_body):
    try:
        pdb.upgrade_data(
            chem_id=request_body.get('chem_id', None),
            name=request_body.get('name', None),
            chem_formula=request_body.get('chem_formula', None),
            cas_number=request_body.get('cas_number', None),
            nature=request_body.get('nature', None),
            ph_nature=request_body.get('ph_nature'),
            quantity=request_body.get('quantity', None),
            data_base=DB, user_name=USER, password=PASWRD, host=HOST)
        message = f'REACTIVE {request_body["chem_id"]} HAS BEEN UPDATED'
        code_status = 200
        return message, code_status
    except Exception as ex:
        message = f'Error executing the update query. {ex}'
        code_status = 400
        return message, code_status


def delete_data(request_body):
    try:
        pdb.delete_data(chem_id=request_body.get('chem_id', None), data_base=DB, user_name=USER, password=PASWRD,
                        host=HOST)
        message = f'REACTIVE {request_body["chem_id"]} HAS BEEN DELETED'
        code_status = 200
        return message, code_status
    except Exception as ex:
        message = f'Error executing the delete query. {ex}'
        code_status = 400
        return message, code_status


def search_data(request):
    try:
        view = request.args.get('view')
        column = request.args.get('where')
        condition = request.args.get('equals')

        data = pdb.view_data(
            view_field=view, column=column, condition_value=condition,
            data_base=DB, user_name=USER, password=PASWRD, host=HOST)

        str_row = []
        for row in data:
            row = [str(i) for i in row]
            string = ' | '.join(row)
            str_row.append(string)
        table = '\n'.join(str_row)

        code_status = 200
        return table, code_status
    except Exception as ex:
        message = f'Error executing the search in the database. {ex}'
        code_status = 400
        return message, code_status
