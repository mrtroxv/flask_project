from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
base_path = os.path.abspath(os.path.dirname(__file__))
database_uri = "sqlite:///" + os.path.join(base_path, "../db/song.db")
app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
db = SQLAlchemy(app)


class song(db.Model):
    def __init__(self, payload: dict):
        self.id = payload.get("id")
        self.name = payload.get("name")
        self.author = payload.get("author")
        self.type = payload.get("type")
        self.image_url = payload.get("image_url")
        self.file_url = payload.get("file_url")
        self.rating = payload.get("rating")
        self.tag = payload.get("tag")
        self.time_created = payload.get("time_created")
        self.time_updated = payload.get("time_updated")

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
