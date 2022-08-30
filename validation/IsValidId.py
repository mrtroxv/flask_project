
def is_valid(id):
    if type(id) == int:
        if id > 0:
            return False
        else:
            return True
    else:
        return True

