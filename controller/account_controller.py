from model.models import *
from controller.person_controller import *
from controller.currency_controller import *
from controller.bank_controller import *
from modules.CurrencyConverter import *


class AccountController:
    def __init__(self, id):
        self.model: Account = Account.get_by_id(id)

    @staticmethod
    def get_all():
        return list(Account.select().dicts())

    def get_item(self):
        return model_to_dict(self.model)

    @staticmethod
    def create(acc_num, person_id, bank_id, currency_id, amount, percent, create_date):
        person = PersonController(person_id).model
        if not person:
            raise ValueError('Invalid person_id')

        bank = BankController(bank_id).model
        if not bank:
            raise ValueError('Invalid bank_id')

        currency = CurrencyController(currency_id).model
        if not currency:
            raise ValueError('Invalid currency_id')

        account = Account.create(acc_num=acc_num, person=person, bank=bank, currency=currency,
                                 amount=amount, percent=percent, create_date=create_date)
        print(account)
        return AccountController(account.id).model

    def update(self, acc_num, person_id, bank_id, currency_id, amount, percent, create_date):
        person = PersonController(person_id).model
        if not person:
            raise ValueError('Invalid person_id')

        bank = BankController(bank_id).model
        if not bank:
            raise ValueError('Invalid bank_id')

        currency = CurrencyController(currency_id).model
        if not currency:
            raise ValueError('Invalid currency_id')
        self.model.acc_num = acc_num
        self.model.person = person
        self.model.bank = bank
        self.model.currency = currency
        self.model.amount = amount
        self.model.percent = percent
        self.model.create_date = create_date
        self.model.save()
        return self.model

    def update_currency(self, currency_id):
        currency = CurrencyController(currency_id).model
        if not currency:
            raise ValueError('Invalid currency_id')

        old_curr_ident = self.model.currency.ident
        new_curr_ident = currency.ident
        if old_curr_ident == new_curr_ident:
            return self.model
        else:
            cc = CurrencyConverter()
            new_amount = cc.convert(self.model.amount, old_curr_ident, new_curr_ident)
            self.model.currency = currency
            self.model.amount = new_amount
            self.model.save()
        return self.model

    def make_transaction(self, account_id, amount):
        add_amount = float(amount)

        to_account = AccountController(account_id).model
        if not to_account:
            raise ValueError('Invalid to_account_id')

        new_amount = self.model.amount - add_amount
        if (add_amount < 0) or (new_amount < 0):
            raise ValueError('Invalid amount')

        from_curr_ident = self.model.currency.ident
        to_curr_ident = to_account.currency.ident

        cc = CurrencyConverter()
        to_amount = to_account.amount + cc.convert(add_amount, from_curr_ident, to_curr_ident)

        self.model.amount = new_amount
        self.model.save()

        to_account.amount = to_amount
        to_account.save()

        return f'transaction to {account_id}:{add_amount}'


    @staticmethod
    def delete(id):
        account = Account.get_or_none(Account.id == id)
        if not account:
            raise ValueError('Not exists person')
        account.delete_instance()
        return f'currency {id} deleted'