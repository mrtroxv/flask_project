from database_interaction import database


def insert_mydata(my_dict: dict):
    song = database.song(my_dict)
    database.db.session.add(song)
    database.db.session.commit()
