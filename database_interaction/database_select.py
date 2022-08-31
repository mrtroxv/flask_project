from database_interaction import database


def select(id):
    song = database.db.session.query(
        database.song).filter_by(id=id).first_or_404()
    model_dict = vars(song)
    del model_dict['_sa_instance_state']
    return model_dict
