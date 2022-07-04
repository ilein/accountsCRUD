from flask import Blueprint, jsonify, request
from controller.person_controller import *

app_url = Blueprint('person', __name__)


@app_url.route('/', methods=['GET'])
def get_persons():
    return jsonify(PersonController.get_all()), 200


@app_url.route('/<id>', methods=['GET'])
def get_person_by_id(id):
    return jsonify(PersonController(id).get_item()), 200


@app_url.route('/', methods=['POST'])
def create_person():
    name = request.form.get('name')
    birthday = request.form.get('birthday')
    person = PersonController.create(name, birthday)
    res = model_to_dict(person)
    return jsonify(result=res), 200


@app_url.route('/<id>', methods=['PUT'])
def update_person(id):
    name = request.form.get('name')
    birthday = request.form.get('birthday')
    person = PersonController(id)
    if not person:
        return jsonify(result='Bank not exists'), 404
    res = model_to_dict(person.update(name, birthday))
    return jsonify(result=res), 200


@app_url.route('/<id>', methods=['DELETE'])
def delete_person(id):
    try:
        res = PersonController.delete(id)
    except ValueError as e:
        return jsonify(result=str(e)), 404
    return jsonify(result=res), 200