from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, func

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String)
    password = db.Column(db.String)

    # Define a one-to-many relationship with Pic
    pics = db.relationship('Pic', backref='user', lazy=True)

class Pic(db.Model):
    __tablename__ = 'pics'
    
    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String)
    image_url = db.Column(db.String)
    created_at = db.Column(DateTime, default=func.current_timestamp(), nullable=False)

    # Define a many-to-one relationship with User
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(DateTime, default=func.current_timestamp(), nullable=False)
    rating = db.Column(db.Integer)
    price = db.Column(db.Integer)

class UserArt(db.Model):
    __tablename__ = "user_arts"

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)

    # Define a many-to-one relationship with User
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref='user_arts')

    # Define a many-to-one relationship with Artist
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'), nullable=False)
    artist = db.relationship('Artist', backref='user_arts')

class Sketch(db.Model):
    __tablename__ = 'sketches'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    image_url = db.Column(db.String)
    created_at = db.Column(DateTime, default=func.current_timestamp(), nullable=False)
class Art(db.Model):
    __tablename__ = 'arts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    created_at = db.Column(DateTime, default=func.current_timestamp(), nullable=False)
    rating = db.Column(db.Integer)
    price = db.Column(db.Integer)