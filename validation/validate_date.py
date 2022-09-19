from datetime import datetime


def valid_date(s):
    return datetime.strptime(s, "%m/%d/%Y")
