from datetime import datetime


def is_valid_datetime(str_datetime):
    try:
        datetime.fromisoformat(str_datetime)

        return True

    except ValueError:
        return False
