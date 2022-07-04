from peewee import *
from datetime import date

pg_db = PostgresqlDatabase('test_hse', user='postgres', password='sys',
                           host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = pg_db

class Bank(BaseModel):
    id = AutoField(db_column='id', primary_key=True)
    name = CharField(db_column='name', null=False)
    bic = CharField(db_column='bic', max_length=9, null=False)
    city = CharField(null=True)
    class Meta:
        db_table = "t_bank"

class Currency(BaseModel):
    id = AutoField(db_column='id', primary_key=True)
    name = CharField(db_column='name', null=False)
    ident = CharField(db_column='ident', null=False)
    class Meta:
        db_table = "t_currency"

class Person(BaseModel):
    id = AutoField(db_column='id', primary_key=True)
    name = CharField(db_column='name', null=False)
    birthday = DateField(db_column='birthday')
    class Meta:
        db_table = "t_person"

class Account(BaseModel):
    id = AutoField(db_column='id', primary_key=True)
    acc_num = CharField(db_column='acc_num', unique=True, null=False)
    person = ForeignKeyField(Person, db_column='person_id', backref='t_account', null=False)
    bank = ForeignKeyField(Bank, db_column='bank_id', backref='t_account', null=False)
    currency = ForeignKeyField(Currency, db_column='currency_id', backref='t_account', null=False)
    amount = FloatField(db_column='amount', default=0.0, null=False)
    percent = FloatField(db_column='percent', default=0.0, null=False)
    create_date = DateField(db_column='create_date', null=False, default=date.today())
    class Meta:
        db_table = "t_account"

def init_db():
    pg_db.create_tables([Bank, Person, Currency, Account], safe=True)
