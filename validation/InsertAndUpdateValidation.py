from operator import truediv
from validation import IsValidId, IsValidString, IsValidRate


def is_valid_insert(req):
    log = False
    for i in req:
        if i == 'id':
            if IsValidId.is_valid(req[i]):
                log = True
                break
        elif i == 'rating':
            if IsValidRate.is_valid_rate(req[i]):
                log = True
                break

        else:
            if IsValidString.is_valid_String(req[i]):
                log = True
                break
    return log

