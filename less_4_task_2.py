import requests
import json
import pprint

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


def currency_rates(*Valutes):
    """
    :param Valutes:
    :return:
    """

    response = requests.get(URL)

    dict_json = json.loads(response.text)
    func = []
    for value in Valutes:
        value = value.upper()
        usd_valute = dict_json.get('Valute').get(value)
        if usd_valute:
            usd_valute = usd_valute.get('Value')
            func.append(usd_valute)

        else:
            func.append("Запрос не обработан")

    return func


print(currency_rates('USD', 'EUR', 'BGN'))