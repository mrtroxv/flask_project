from database_interaction import database


def delete(id):
    song = database.db.session.query(
        database.song).filter_by(id=id).first_or_404()
    database.db.session.delete(song)
    database.db.session.commit()
