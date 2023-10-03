def rating_type(rate):
    if type(rate) == float and rate >= 0 and rate <= 5:
        return rate
    else:
        raise Exception("invalid  rate input")
