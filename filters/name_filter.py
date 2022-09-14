from database_interaction import database


def filter_by_name(name, my_select_dict):
    search_name = "%{}%".format(name)
    my_select_dict = my_select_dict.filter(database.song.name.like(search_name))
    return my_select_dict
