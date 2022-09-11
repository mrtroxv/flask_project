from database_interaction import database


def update(my_dict, id):
    our_dict = database.db.session.query(database.song).filter_by(id=id).first_or_404()
    for i in my_dict:
        if i == "name":
            our_dict.name = my_dict["name"]
        if i == "author":
            our_dict.author = my_dict["author"]
        if i == "file_url":
            our_dict.file_url = my_dict["file_url"]
        if i == "image_url":
            our_dict.image_url = my_dict["image_url"]
        if i == "rating":
            our_dict.rating = my_dict["rating"]
        if i == "tag":
            our_dict.tag = my_dict["tag"]
        if i == "type":
            our_dict.type = my_dict["type"]

    database.db.session.commit()
