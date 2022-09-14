from database_interaction import database


def filter_by_tag(tag, my_select_dict):
    search_tag = "%{}%".format(tag)
    my_select_dict = my_select_dict.filter(database.song.tag.like(search_tag))
    return my_select_dict
