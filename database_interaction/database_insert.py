from database_interaction import database
from database_interaction import time_added, time_update


def insert_mydata(my_dict: dict):
    my_dict["time_created"] = time_added.song_time_added()
    my_dict["time_updated"] = time_update.my_update_time()
    song = database.song(my_dict)
    database.db.session.add(song)
    database.db.session.commit()
