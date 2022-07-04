import requests
import xml
import xml.etree.ElementTree as ET
from datetime import date


def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class CurrencyConverter:
    def __init__(self, curr_date=date.today()):
        curr_date_str = curr_date.strftime("%d/%m/%Y")
        url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={curr_date_str}'
        print(url)
        response = requests.get(url)
        string_xml = response.content
        tree = xml.etree.ElementTree.fromstring(string_xml)
        dict = {}
        for child in tree:
            val = float(child.find('Value').text.replace(',', '.'))
            dict[child.find('CharCode').text] = val
        self.currencies = dict

    def get_val_by_ident(self, ident):
        return self.currencies[ident]

    def convert(self, value, from_currency, to_currency):
        if from_currency == to_currency:
            return value
        from_val = value if from_currency in ('RUR', 'RUB') else value * self.currencies[from_currency]
        ret_val = from_val if to_currency in ('RUR', 'RUB') else from_val / self.currencies[to_currency]
        return round(ret_val, 2)
