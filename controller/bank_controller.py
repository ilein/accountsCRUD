from model.models import *
from playhouse.shortcuts import model_to_dict

class BankController:
    def __init__(self, id):
        self.model: Bank = Bank.get_by_id(id)

    @staticmethod
    def get_all() -> list:
        return list(Bank.select().dicts())

    def get_item(self):
        return model_to_dict(self.model)

    @staticmethod
    def create(name, bic, city):
        bank = Bank.create(name=name, bic=bic, city=city)
        print(bank)
        return BankController(bank.id).model

    def update(self, name, bic, city):
        self.model.name = name
        self.model.bic = bic
        self.model.city = city
        self.model.save()
        return self.model

    @staticmethod
    def delete(id):
        bank = Bank.get_or_none(Bank.id == id)
        if not bank:
            raise ValueError('Not exists bank')
        bank.delete_instance()
        return f'bank {id} deleted'



