from datetime import datetime


def timestamp_converter(obj):
    if isinstance(obj, datetime):
        return obj.__str__()
