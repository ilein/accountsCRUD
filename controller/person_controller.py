from model.models import *
from playhouse.shortcuts import model_to_dict, dict_to_model


class PersonController:
    def __init__(self, id):
        self.model: Person = Person.get_by_id(id)

    @staticmethod
    def get_all() -> list:
        return list(Person.select().dicts())

    def get_item(self):
        return model_to_dict(self.model)

    @staticmethod
    def create(name, birthday):
        person = Person.create(name=name, birthday=birthday)
        print(person)
        return PersonController(person.id).model

    def update(self, name, birthday):
        self.model.name = name
        self.model.birthday = birthday
        self.model.save()
        return self.model


    @staticmethod
    def delete(id):
        person = Person.get_or_none(Person.id == id)
        if not person:
            raise ValueError('Not exists person')
        person.delete_instance()
        return f'currency {id} deleted'
