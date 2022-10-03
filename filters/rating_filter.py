from database_interaction import database


def filter_by_rating(rating, my_select_dict):
    my_select_dict = my_select_dict.filter(database.song.rating >= rating)
    return my_select_dict
