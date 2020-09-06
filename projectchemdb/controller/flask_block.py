""" Script to develop the API REST block of chemDB
"""

from flask import Flask, request, Response
from projectchemdb.service import service_postgres as service_db

app = Flask(__name__)


@app.route('/status')
def connection():
    message, code_status = service_db.check_data_base_status()
    return Response(message, status=code_status)


@app.route('/reactive', methods=['POST'])
def insertion():
    request_body = request.get_json()
    response_message, code_status = service_db.insert_data(request_body)
    return Response(response_message, status=code_status)


@app.route('/reactive', methods=['PUT'])
def update():
    request_body = request.get_json()
    response_message, code_status = service_db.update_data(request_body)
    return Response(response_message, status=code_status)


@app.route('/reactive', methods=['DELETE'])
def delete():
    request_body = request.get_json()
    response_message, code_status = service_db.delete_data(request_body)
    return Response(response_message, status=code_status)


@app.route('/reactives', methods=['GET'])
def query():
    response_message, code_status = service_db.search_data(request)
    return Response(response_message, status=200)


def run_app():
    app.debug = True
    app.run()
