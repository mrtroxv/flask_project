from re import M
import sys

sys.path.append("../")
import json
from database_interaction import database_insert, database_update, database
from validation import insert_and_update_validation
from sqlalchemy.exc import IntegrityError


def insert_data(my_file):
    for i in my_file:
        if not insert_and_update_validation.is_valid_insert(i):
            print("id :", i["id"], "the data skiped")
            continue
        else:
            i["tag"] = "new"
            try:
                database_insert.insert_mydata(i)
            except IntegrityError:
                ur_choice = input(
                    "u have simelr id, if u want to keep ur data press 2 or 1 to update ur data : "
                )
                if ur_choice == "1":
                    database.db.session.rollback()
                    database_update.update(i, i["id"])
                else:
                    database.db.session.rollback()


def read_from_file_new_song():

    f = open("..\my_file\data_new.json", "r+")
    my_file = json.load(f)
    insert_data(my_file)


def read_from_file_trending_song():

    f = open("..\my_file\data_trending.json", "r+")
    my_file = json.load(f)
    insert_data(my_file)


def read_from_file_popular_song():

    f = open("..\my_file\data_popular.json", "r+")
    my_file = json.load(f)
    insert_data(my_file)


if __name__ == "__main__":
    read_from_file_new_song()
    read_from_file_trending_song()
    read_from_file_popular_song()
