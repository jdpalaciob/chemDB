from sqlalchemy import create_engine
from projectchemdb.configuration.db_credentials import credentials
from projectchemdb.persistence import alchemy

DB = credentials['data_base']
USER = credentials['user_name']
PASWRD = credentials['password']
HOST = credentials['host']
PORT = credentials['port']
engine = create_engine(f'postgresql://{USER}:{PASWRD}@{HOST}:{PORT}/{DB}', echo=False)


def check_data_base_status():
    try:
        create_engine(f'postgresql://{USER}:{PASWRD}@{HOST}:{PORT}/{DB}', echo=False)
        message = 'Access to Data Base granted'
        code_status = 200
        return message, code_status
    except Exception as ex:
        message = f'Error executing the check status of the databes. {ex}'
        code_status = 400
        return message, code_status


def insert_data(request_body):
    try:
        reactive = alchemy.Reactive(
            chem_id=request_body.get('chem_id', None),
            name=request_body.get('name', None),
            chem_form=request_body.get('chem_formula', None),
            cas_number=request_body.get('cas_number', None),
            nature=request_body.get('nature', None),
            ph_nature=request_body.get('ph_nature'),
            quantity=request_body.get('quantity', None))
        alchemy.insert_data(reactive, engine=engine)
        message = f'REACTIVE {request_body["chem_id"]} HAS BEEN INSERTED'
        code_status = 200
        return message, code_status
    except Exception as ex:
        message = f'Error executing the insert query. {ex}'
        code_status = 400
        return message, code_status


def update_data(request_body):
    try:
        reactive = alchemy.Reactive(
            chem_id=request_body.get('chem_id', None),
            name=request_body.get('name', None),
            chem_form=request_body.get('chem_formula', None),
            cas_number=request_body.get('cas_number', None),
            nature=request_body.get('nature', None),
            ph_nature=request_body.get('ph_nature'),
            quantity=request_body.get('quantity', None))
        alchemy.update_data(request_body.get('chem_id', None), reactive, engine=engine)
        message = f'REACTIVE {request_body["chem_id"]} HAS BEEN UPDATED'
        code_status = 200
        return message, code_status
    except Exception as ex:
        message = f'Error executing the update query. {ex}'
        code_status = 400
        return message, code_status


def delete_data(request_body):
    try:
        alchemy.delete_data(request_body.get('chem_id', None), engine=engine)
        message = f'REACTIVE {request_body["chem_id"]} HAS BEEN DELETED'
        code_status = 200
        return message, code_status
    except Exception as ex:
        message = f'Error executing the delete query. {ex}'
        code_status = 400
        return message, code_status


def search_data(request):
    try:
        column = request.args.get('where')
        condition = request.args.get('equals')
        message = str(alchemy.query_data(column=column, condition=condition, engine=engine))
        code_status = 200
        return message, code_status
    except Exception as ex:
        message = f'Error executing the search in the database. {ex}'
        code_status = 400
        return message, code_status
