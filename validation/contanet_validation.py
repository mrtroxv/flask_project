def contatnt_make_valid(my_dict):
    if my_dict["tag"] == None:
        my_dict["tag"] = "None"
    if my_dict["force_replace"] == None:
        my_dict["force_replace"] = "False"
    return my_dict


def is_valid(my_dict):
    if my_dict["my_file"] == None:
        return False
    return True
