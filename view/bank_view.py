from flask import Blueprint, jsonify, request
from controller.bank_controller import *
from playhouse.shortcuts import model_to_dict

app_url = Blueprint('bank', __name__)


@app_url.route('/', methods=['GET'])
def get_banks():
    return jsonify(BankController.get_all()), 200

@app_url.route('/<id>', methods=['GET'])
def get_bank_by_id(id):
    return jsonify(BankController(id).get_item()), 200

@app_url.route('/', methods=['POST'])
def create_bank():
    name = request.form.get('name')
    bic = request.form.get('bic')
    city = request.form.get('city')
    bank = BankController.create(name, bic, city)
    res = model_to_dict(bank)
    return jsonify(result=res), 200

@app_url.route('/<id>', methods=['PUT'])
def update_bank(id):
    name = request.form.get('name')
    bic = request.form.get('bic')
    city = request.form.get('city')
    bank = BankController(id)
    if not bank:
        return jsonify(result='Bank not exists'), 404
    res = model_to_dict(bank.update(name, bic, city))
    return jsonify(result=res), 200

@app_url.route('/<id>', methods=['DELETE'])
def delete_bank(id):
    try:
        res = BankController.delete(id)
    except ValueError as e:
        return jsonify(result=str(e)), 404
    return jsonify(result=res), 200