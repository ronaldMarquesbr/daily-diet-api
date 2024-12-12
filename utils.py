from datetime import datetime


def is_valid_datetime(str_datetime):
    try:
        datetime.strptime(str_datetime, "%Y-%m-%d %H:%M:%S")

        return True

    except ValueError:
        return False
