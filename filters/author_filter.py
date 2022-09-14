from database_interaction import database


def filter_by_author(author, my_select_dict):
    search_author = "%{}%".format(author)
    my_select_dict = my_select_dict.filter(database.song.author.like(search_author))
    return my_select_dict
