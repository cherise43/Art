# class  User(db.M)
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy_serializer import SerializerMix
from sqlalchemy import DateTime,func
db=SQLAlchemy()
class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String)
    password=db.Column(db.String)


    pics=db.relationship('Pic',backref='user')

# class Pic(db.Model):
#     __tablename__='pics'
#     id=db.Column(db.Integer,primary_key=True)
#     user_id=db.Column(db.Integer)
#     caption=db.Column(db.String)
#     image_url=db.Column(db.String)
#     created_at = db.Column(DateTime, default=func.current_timestamp())
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
#     users=db.relationship('User',back_populates='pics')

class Art(db.model):
    __tablename__ = 'artist'
    id=db.Column(db.Integer,primary_key=True)
    name= db.Column
    created_at=db.Column(db.DateTime,server_default=db.func.now())
    rating=db.Column(db.Integer)
    price=db.Column(db.Integer)

class Userart(db.Model):
    __tablename__ = "user_arts"
    id=db.Column
    rating =db.Column(db.Integer,db.Foreign)
    user_id=db.Column(db.Integer, db.ForeignKey=='users.id')
    art_id = db.Column(db.Integer,db.ForeignKey=='arts.id')

    

class Sketch(db.Model):
    __tablename__='sketchs'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String)
    description=db.Column(db.String)
    image_url=db.Column(db.String)
    created_at = db.Column(DateTime, default=func.current_timestamp())
