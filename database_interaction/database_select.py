from datetime import datetime
from validation import validate_date
from flask_restful import reqparse
import re
from database_interaction import database
from patterns import date_pattern
from filters import (
    name_filter,
    author_filter,
    type_filter,
    tag_filter,
    rating_filter,
    time_filter,
)

parser = reqparse.RequestParser()
parser.add_argument(
    "time_created",
    "time_updated",
    type=validate_date.valid_date,
    required=True,
    help="invalid date value",
)


def select(id):
    song = database.db.session.query(database.song).filter_by(id=id).first_or_404()
    model_dict = vars(song)
    del model_dict["_sa_instance_state"]
    return model_dict


def select_by_filters(request_data, page):
    list_of_song = []
    dict_of_select = database.db.session.query(database.song)
    for i in request_data:
        if i == "name":
            name = request_data.get("name")
            dict_of_select = name_filter.filter_by_name(name, dict_of_select)
        if i == "author":
            author = request_data.get("author")
            dict_of_select = author_filter.filter_by_author(author, dict_of_select)
        if i == "type":
            type = request_data.get("type")
            dict_of_select = type_filter.filter_by_type(type, dict_of_select)
        if i == "tag":
            tag = request_data.get("tag")
            dict_of_select = tag_filter.filter_by_tag(tag, dict_of_select)
        if i == "rating":
            rating = float(request_data.get("rating"))
            dict_of_select = rating_filter.filter_by_rating(rating, dict_of_select)
        if i == "time_created":
            time_created = parser.parse_args().get("time_created")
            dict_of_select = time_filter.filter_by_time_created(
                time_created, dict_of_select
            )
        if i == "time_updated":
            time_updated = parser.parse_args().get("time_updated")
            dict_of_select = time_filter.filter_by_time_updated(
                time_updated, dict_of_select
            )

    dict_of_select = dict_of_select.paginate(page, per_page=10)

    my_page = vars(dict_of_select)

    def serialize_song(song):
        song_dict = vars(song)
        song_dict.pop("_sa_instance_state")
        return song_dict

    list_of_song = [serialize_song(i) for i in my_page["items"]]
    return list_of_song
