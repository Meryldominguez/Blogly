from flask_sqlalchemy import SQLAlchemy

import datetime

def now():
    return datetime.datetime.now()

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""
    db.app = app
    db.init_app(app)


class Post(db.Model):
    """Post class for db entry in posts table"""
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_title = db.Column(db.String(40), nullable=False)
    post_content = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(), default= datetime.datetime.now)
    user_id= db.Column(db.Integer, db.ForeignKey('users.id'))

class User(db.Model):
    """Accounts per user of blogly app"""
    __tablename__= "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    image_url = db.Column(db.String, nullable=True)

    posts= db.relationship('Post', backref="author")

    def get_full_name(self):
        return self.first_name+" "+self.last_name



