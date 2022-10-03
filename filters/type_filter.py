from database_interaction import database


def filter_by_type(type, my_select_dict):
    search_type = "%{}%".format(type)
    my_select_dict = my_select_dict.filter(database.song.type.like(search_type))
    return my_select_dict
