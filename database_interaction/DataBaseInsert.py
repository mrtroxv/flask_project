from database_interaction import Database


def insert_mydata(my_dict):
    song = Database.Songs(id=my_dict['id'], name=my_dict['name'], author=my_dict['author'], type=my_dict['type'],
                          image_url=my_dict['image_url'], file_url=my_dict['file_url'], rating=my_dict['rating'], tag=my_dict['tag'])
    Database.db.session.add(song)
    Database.db.session.commit()

