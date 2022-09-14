from datetime import datetime
from database_interaction import database
from filters import (
    name_filter,
    author_filter,
    type_filter,
    tag_filter,
    rating_filter,
    time_filter,
)
from database_interaction import database


def select(id):
    song = database.db.session.query(database.song).filter_by(id=id).first_or_404()
    model_dict = vars(song)
    del model_dict["_sa_instance_state"]
    return model_dict


def select_by_filters(st, page):
    my_obj_dict = {}
    my_list = []
    my_select_dict = database.db.session.query(database.song)
    for i in st:
        if i == "name":
            name = st.get("name")
            my_select_dict = name_filter.filter_by_name(name, my_select_dict)
        if i == "author":
            author = st.get("author")
            my_select_dict = author_filter.filter_by_author(author, my_select_dict)
        if i == "type":
            type = st.get("type")
            my_select_dict = type_filter.filter_by_type(type, my_select_dict)
        if i == "tag":
            tag = st.get("tag")
            my_select_dict = tag_filter.filter_by_tag(tag, my_select_dict)
        if i == "rating":
            rating = float(st.get("rating"))
            my_select_dict = rating_filter.filter_by_rating(rating, my_select_dict)
        if i == "time_created":
            try:
                time_created = datetime.strptime(st.get("time_created"), "%m/%d/%Y")
            except ValueError:
                return False
            my_select_dict = time_filter.filter_by_time_created(
                time_created, my_select_dict
            )
        if i == "time_updated":
            try:
                time_updated = datetime.strptime(st.get("time_updated"), "%m/%d/%Y")
            except ValueError:
                return False
            my_select_dict = time_filter.filter_by_time_updated(
                time_updated, my_select_dict
            )

    my_select_dict = my_select_dict.paginate(page, per_page=10)

    my_page = vars(my_select_dict)
    for i in my_page["items"]:
        my_obj_dict = vars(i)
        del my_obj_dict["_sa_instance_state"]
        my_list.append(my_obj_dict)
    return my_list
