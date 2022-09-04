from validation import is_valid_id, is_valid_rate, is_valid_string


def is_valid_insert(req):
    for i in req:
        if i == 'id':
            if not is_valid_id.is_valid(req[i]):
                return False

        elif i == 'rating':
            if not is_valid_rate.is_valid_rate(req[i]):
                return False
        else:
            if not is_valid_string.is_valid_String(req[i]):
                return False
    return True
