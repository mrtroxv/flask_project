import sys

sys.path.append("../")
import json
from database_interaction import database_insert, database_update, database
from validation import insert_and_update_validation
from sqlalchemy.exc import IntegrityError


def insert_data(my_file, tag):
    for i in my_file:
        if not insert_and_update_validation.is_valid_insert(i):
            print("id :", i["id"], "the data skiped")
            continue
        else:
            i["tag"] = tag
            try:
                database_insert.insert_mydata(i)
            except IntegrityError:
                ur_choice = input(
                    "you have similar id, if u want to replace ur data type 1: "
                )
                database.db.session.rollback()
                if ur_choice == "1":
                    database_update.update(i, i["id"])


def read_from_file(tag):
    f_path = f"..\my_file\data_{tag}.json"
    f = open(f_path, "r+")
    my_file = json.load(f)
    insert_data(my_file, tag)


if __name__ == "__main__":
    array_of_tags = ["new", "popular", "trending"]
    for tag in array_of_tags:
        read_from_file(tag)
