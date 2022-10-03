from database_interaction import database


def filter_by_time_created(time_created, my_select_dict):
    my_select_dict = my_select_dict.filter(database.song.time_created >= time_created)
    return my_select_dict


def filter_by_time_updated(time_updated, my_select_dict):
    my_select_dict = my_select_dict.filter(database.song.time_updated >= time_updated)
    return my_select_dict
