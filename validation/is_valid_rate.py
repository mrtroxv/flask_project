def is_valid_rate(rate):
    if type(rate) == float and rate >= 0 and rate <= 5:
        return True
    return False
