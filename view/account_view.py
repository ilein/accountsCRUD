from flask import Blueprint, jsonify, request
from controller.account_controller import *

app_url = Blueprint('account', __name__)


@app_url.route('/', methods=['GET'])
def get_accounts():
    return jsonify(AccountController.get_all()), 200


@app_url.route('/<id>', methods=['GET'])
def get_account_by_id(id):
    return jsonify(AccountController(id).get_item()), 200


@app_url.route('/', methods=['POST'])
def create_account():
    acc_num = request.form.get('acc_num')
    person_id = request.form.get('person_id')
    bank_id = request.form.get('bank_id')
    currency_id = request.form.get('currency_id')
    amount = request.form.get('amount')
    percent = request.form.get('percent')
    create_date = request.form.get('create_date')
    account = AccountController.create(acc_num, person_id, bank_id, currency_id, amount, percent, create_date)
    res = model_to_dict(account)
    return jsonify(result=res), 200


@app_url.route('/<id>', methods=['PUT'])
def update_account(id):
    acc_num = request.form.get('acc_num')
    person_id = request.form.get('person_id')
    bank_id = request.form.get('bank_id')
    currency_id = request.form.get('currency_id')
    amount = request.form.get('amount')
    percent = request.form.get('percent')
    create_date = request.form.get('create_date')
    account = AccountController(id)
    if not account:
        return jsonify(result='Account not exists'), 404
    res = model_to_dict(account.update(acc_num, person_id, bank_id, currency_id, amount, percent, create_date))
    return jsonify(result=res), 200


@app_url.route('/update_currency/<id>', methods=['PUT'])
def update_account_currency(id):
    currency_id = request.form.get('currency_id')
    account = AccountController(id)
    if not account:
        return jsonify(result='Account not exists'), 404
    res = model_to_dict(account.update_currency(currency_id))
    return jsonify(result=res), 200


@app_url.route('/make_transaction/<id>', methods=['POST'])
def make_transaction(id):
    account = AccountController(id)
    if not account:
        return jsonify(result='Account not exists'), 404

    to_id = request.form.get('to_id')
    amount = request.form.get('amount')

    res = account.make_transaction(to_id, amount)
    return jsonify(result=res), 200



@app_url.route('/<id>', methods=['DELETE'])
def delete_account(id):
    try:
        res = AccountController.delete(id)
    except ValueError as e:
        return jsonify(result=str(e)), 404
    return jsonify(result=res), 200