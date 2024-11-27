# Анна Шуликова, 24А-когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

def test_create_and_get_order_by_track():
    # Создание заказа
    response = sender_stand_request.create_order(data.order_body)
    assert response.status_code == 201

    # Получение трек-номера
    track_number = response.json().get("track")
    assert track_number is not None

    # Получение данных заказа по трек-номеру
    order = sender_stand_request.get_order(track_number)
    assert order.status_code == 200