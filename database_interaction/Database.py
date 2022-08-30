from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
base_path = os.path.abspath(os.path.dirname(__file__))
database_uri = "sqlite:///" + os.path.join(base_path, "../db/songs.db")
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
db = SQLAlchemy(app)


class Songs (db.Model):
    def __init__(self, id=None, name=None, author=None, type=None, image_url=None, file_url=None, rating=None, tag=None, time_created=None, time_updated=None):
        self.id = id
        self.name = name
        self.author = author
        self.type = type
        self.image_url = image_url
        self.file_url = file_url
        self.rating = rating
        self.tag = tag
        self.time_created = time_created
        self.time_updated = time_updated

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    author = db.Column(db.String(255))
    type = db.Column(db.String(255))
    image_url = db.Column(db.String(511))
    file_url = db.Column(db.String(511))
    rating = db.Column(db.Float)
    tag = db.Column(db.String)
    time_created = db.Column(db.DateTime, nullable=True)
    time_updated = db.Column(db.DateTime, nullable=True)


db.create_all()

