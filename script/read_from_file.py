import sys
from flask_api import status


sys.path.append("../")
import json
from database_interaction import database_insert, database_update, database
from validation import insert_and_update_validation
from sqlalchemy.exc import IntegrityError


def handle_integrity_error(from_api, force_replace, i):
def handle_intergrity_error(from_api, force_replace, i):
    database.db.session.rollback()
    if not from_api:
        ur_choice = input("you have similar id, if u want to replace ur data type 1: ")
        if ur_choice == "1":
            database_update.update(i, i["id"])
    else:
        if force_replace:
            database_update.update(i, i["id"])


def insert_data(my_file, tag, force_replace, from_api):
    for i in my_file:
        if not insert_and_update_validation.is_valid_insert(i):
            print("id :", i["id"], "the data skiped")
            continue
        else:
            i["tag"] = tag
            try:
                database_insert.insert_mydata(i)
            except IntegrityError:
                handle_integrity_error(from_api, force_replace, i)
                handle_intergrity_error(from_api, force_replace, i)


def read_from_file(tag):
    f_path = f"..\my_file\data_{tag}.json"
    f = open(f_path, "r+")
    my_file = json.load(f)
    insert_data(my_file, tag, False, False)


def read_from_file_api(my_obj):
    from_api = True
    try:
        my_file_content = json.load(my_obj.my_file)
    except UnicodeDecodeError:
        return False

    tag = my_obj.my_tag
    force_replace = my_obj.my_force_replace
def read_from_file_api(my_file, tag, force_replace):
    from_api = True
    try:
        my_file_content = json.load(my_file)
    except UnicodeDecodeError:
        return False

    if str.lower(force_replace) == "true":
        force_replace = True
    else:
        force_replace = False

    insert_data(my_file_content, tag, force_replace, from_api)
    return True


if __name__ == "__main__":
    array_of_tags = ["new", "popular", "trending"]
    for tag in array_of_tags:
        read_from_file(tag)
