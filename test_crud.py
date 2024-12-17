import requests
from datetime import datetime
import pytz
import pytest

url = "http://127.0.0.1:5000"


def test_create_meal():
    my_payload = create_payload()

    create_meal_response = create_meal(my_payload)
    assert create_meal_response.status_code == 200
    create_meal_data = create_meal_response.json()
    assert "id" in create_meal_data

    meal_id = create_meal_data.get("id")

    get_meal_response = get_meal(meal_id)
    assert get_meal_response.status_code == 200
    get_meal_data = get_meal_response.json()
    assert "id" in get_meal_data
    assert get_meal_data.get("id") == meal_id
    assert get_meal_data.get("name") == my_payload["name"]
    assert get_meal_data.get("description") == my_payload["description"]
    assert convert_rfc_to_iso(get_meal_data.get("date")) == convert_datetime_to_utc(my_payload.get("date"))
    assert get_meal_data.get("off_diet") == my_payload.get("off_diet")


def test_update_meal():
    my_payload = create_payload()
    create_meal_response = create_meal(my_payload)
    assert create_meal_response.status_code == 200
    create_meal_data = create_meal_response.json()
    meal_id = create_meal_data.get("id")

    new_payload = {
        "name": "Other name",
        "description": "Other description",
        "date": "2024-12-17T10:00:00+00:00",
        "off_diet": False
    }

    update_meal_response = update_meal(meal_id, new_payload)
    assert update_meal_response.status_code == 200
    update_meal_data = update_meal_response.json()
    assert update_meal_data.get("id") == meal_id

    get_meal_response = get_meal(meal_id)
    assert get_meal_response.status_code == 200
    get_meal_data = get_meal_response.json()

    assert get_meal_data.get("name") == new_payload.get("name")
    assert get_meal_data.get("description") == new_payload.get("description")
    assert (
            convert_rfc_to_iso(get_meal_data.get("date"))
            == convert_datetime_to_utc(new_payload.get("date"))
    )
    assert get_meal_data.get("off_diet") == new_payload.get("off_diet")


def get_meal(meal_id):
    return requests.get(f"{url}/meal/{meal_id}")


def create_meal(payload):
    return requests.post(f"{url}/meal", json=payload)


def create_payload():
    return {
        "name": "my meal",
        "description": "my description",
        "off_diet": True,
        "date": "2024-12-16T13:00:00-03:00"
    }


def update_meal(meal_id, payload):
    return requests.patch(f"{url}/meal/{meal_id}", json=payload)


def convert_datetime_to_utc(dt_string):
    dt_obj = datetime.fromisoformat(dt_string)
    utc_dt = dt_obj.astimezone(pytz.utc)

    return utc_dt


def convert_rfc_to_iso(dt_string):
    dt_obj = datetime.strptime(dt_string, "%a, %d %b %Y %H:%M:%S GMT").replace(tzinfo=pytz.utc)

    return dt_obj
