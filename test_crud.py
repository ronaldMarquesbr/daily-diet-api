import requests
from datetime import datetime
import pytz
import pytest

url = "http://127.0.0.1:5000"


def test_create_meal():
    my_payload = {
        "name": "my meal",
        "description": "my description",
        "off_diet": True,
        "date": "2024-12-16T13:00:00-03:00"
    }

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


def get_meal(meal_id):
    return requests.get(f"{url}/meal/{meal_id}")


def create_meal(payload):
    return requests.post(f"{url}/meal", json=payload)


def convert_datetime_to_utc(dt_string):
    dt_obj = datetime.fromisoformat(dt_string)
    utc_dt = dt_obj.astimezone(pytz.utc)
    iso_dt = utc_dt.isoformat()

    return utc_dt


def convert_rfc_to_iso(dt_string):
    dt_obj = datetime.strptime(dt_string, "%a, %d %b %Y %H:%M:%S GMT").replace(tzinfo=pytz.utc)
    iso_format = dt_obj.isoformat()

    return dt_obj
