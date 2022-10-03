def string_type(s):
    if len(s.strip()) != 0:
        return s
    else:
        raise Exception("invalid str value")
