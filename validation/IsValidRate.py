def is_valid_rate(rate):
    if type(rate) == float:
        print(rate)
        if rate > 0:
            return False
        else:
            return True
    else:
        return True

