def id_type(id):
    if type(id) == int and id >= 0:
        return id
    else:
        raise Exception("invalid id input")
