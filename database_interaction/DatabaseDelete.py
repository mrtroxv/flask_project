from database_interaction import Database


def delete(id):
    song = Database.db.session.query(Database.Songs)
    for i in song:
        if i.id == id:
            Database.db.session.delete(i)
            Database.db.session.commit()

