def content_make_valid(my_obj):
    if my_obj.my_tag == None:
        my_obj.my_tag = "None"
    if my_obj.my_force_replace == None:
        my_obj.my_force_replace = False
    else:
        if str.lower(my_obj.my_force_replace) == "true":
            my_obj.my_force_replace = True
        else:
            my_obj.my_force_replace = False
    return my_obj


def is_valid(my_obj):
    if my_obj.my_file == None:
        return False
    return True
