from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict

from controller.currency_controller import *

app_url = Blueprint('currency', __name__)


@app_url.route('/', methods=['GET'])
def get_currencies():
    return jsonify(CurrencyController.get_all()), 200


@app_url.route('/<id>', methods=['GET'])
def get_currency_by_id(id):
    return jsonify(CurrencyController(id).get_item()), 200


@app_url.route('/', methods=['POST'])
def create_currency():
    name = request.form.get('name')
    ident = request.form.get('ident')
    currency = CurrencyController.create(name, ident)
    res = model_to_dict(currency)
    return jsonify(result=res), 200

@app_url.route('/<id>', methods=['PUT'])
def update_currency(id):
    name = request.form.get('name')
    ident = request.form.get('ident')
    currency = CurrencyController(id)
    if not currency:
        return jsonify(result='Currency not exists'), 404
    res = model_to_dict(currency.update(name, ident))
    return jsonify(result=res), 200

@app_url.route('/<id>', methods=['DELETE'])
def delete_currency(id):
    try:
        res = CurrencyController.delete(id)
    except ValueError as e:
        return jsonify(result=str(e)), 404
    return jsonify(result=res), 200