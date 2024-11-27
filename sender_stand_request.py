import configuration
import requests

# Функция для создания нового заказа
def create_order(body):
    res = requests.post(configuration.URL + configuration.CREATION_ORDER_PATHNAME, json=body)
    res.raise_for_status()
    return res

# Функция для получения информации о заказе по трек-номеру
def get_order(track_number):
    url = configuration.URL + configuration.GET_ORDER_PATHNAME + str(track_number)
    res = requests.get(url)
    res.raise_for_status()
    return res