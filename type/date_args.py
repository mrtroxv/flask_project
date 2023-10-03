from datetime import datetime


def date_type(s):
    return datetime.strptime(s, "%m/%d/%Y")
