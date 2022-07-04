from flask import Blueprint, jsonify

app_url = Blueprint('main', __name__)

@app_url.route('/', methods=['GET'])
def get_hello():
    return jsonify(result='Hello!'), 200