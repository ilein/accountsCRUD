from model.models import *
from playhouse.shortcuts import model_to_dict, dict_to_model


class CurrencyController:
    def __init__(self, id):
        self.model: Currency = Currency.get_by_id(id)

    @staticmethod
    def get_all() -> list:
        return list(Currency.select().dicts())

    def get_item(self):
        return model_to_dict(self.model)

    @staticmethod
    def create(name, ident):
        currency = Currency.create(name=name, ident=ident)
        print(currency)
        return CurrencyController(currency.id).model

    def update(self, name, ident):
        self.model.name = name
        self.model.ident = ident
        self.model.save()
        return self.model

    @staticmethod
    def delete(id):
        currency = Currency.get_or_none(Currency.id == id)
        if not currency:
            raise ValueError('Not exists currency')
        currency.delete_instance()
        return f'currency {id} deleted'
