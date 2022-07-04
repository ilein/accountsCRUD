from model.models import *
from flask import Flask

app = Flask(__name__)


def register_blueprints():
    from view.bank_view import app_url as bank_url
    from view.currency_view import app_url as currency_url
    from view.person_view import app_url as person_url
    from view.account_view import app_url as account_url
    from view.main_view import app_url as main_url
    app.register_blueprint(bank_url, url_prefix='/bank')
    app.register_blueprint(currency_url, url_prefix='/currency')
    app.register_blueprint(person_url, url_prefix='/person')
    app.register_blueprint(account_url, url_prefix='/account')
    app.register_blueprint(main_url)


register_blueprints()

init_db()

if __name__ == '__main__':
    app.run(debug=True)
