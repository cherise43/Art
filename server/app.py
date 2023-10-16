import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, User, Pic, Artist, UserArt, Sketch, Art

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
#postgres://k_danz_2b14_user:LfX4jd3zeKSVkYANThBkeSNV7poCKzVF@dpg-ckmkuio710pc73d5jqv0-a.oregon-postgres.render.com/k_danz_2b14
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)  # Enable CORS for all routes
from flask_migrate import Migrate

migrate = Migrate(app, db)


db.init_app(app)

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'user_name': user.user_name, 'password': user.password} for user in users]
    return jsonify(user_list)

# POST a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user_name = data.get('user_name')
    password = data.get('password')

    existing_user = User.query.filter_by(user_name=user_name).first()
    if existing_user:
        return jsonify({'error': 'User with this username already exists'}), 400

    user = User(user_name=user_name, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'})

# DELETE a user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted'})

# GET all pics
@app.route('/pics', methods=['GET'])
def get_pics():
    pics = Pic.query.all()
    pic_list = [{'id': pic.id, 'caption': pic.caption, 'image_url': pic.image_url, 'user_id': pic.user_id} for pic in pics]
    return jsonify(pic_list)

# POST a new pic for a user
@app.route('/pics', methods=['POST'])
def create_pic():
    data = request.get_json()
    user_id = data.get('user_id')

    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    pic = Pic(user_id=user_id)
    db.session.add(pic)
    db.session.commit()
    return jsonify({'message': 'Pic created successfully'})

# PATCH (update) a pic by ID
@app.route('/pics/<int:pic_id>', methods=['PATCH'])
def update_pic(pic_id):
    pic = Pic.query.get(pic_id)
    if not pic:
        return jsonify({'error': 'Pic not found'}), 404

    data = request.get_json()
    pic.caption = data.get('caption')
    db.session.commit()
    return jsonify({'message': 'Pic updated successfully'})

# DELETE a pic by ID
@app.route('/pics/<int:pic_id>', methods=['DELETE'])
def delete_pic(pic_id):
    pic = Pic.query.get(pic_id)
    if not pic:
        return jsonify({'error': 'Pic not found'}), 404
    db.session.delete(pic)
    db.session.commit()
    return jsonify({'message': 'Pic deleted'})

# GET all artists
@app.route('/artists', methods=['GET'])
def get_artists():
    artists = Artist.query.all()
    artist_list = [{'id': artist.id, 'name': artist.name, 'rating': artist.rating, 'price': artist.price} for artist in artists]
    return jsonify(artist_list)

# GET all user-arts
@app.route('/user-arts', methods=['GET'])
def get_user_arts():
    user_arts = UserArt.query.all()
    user_art_list = [{'id': user_art.id, 'rating': user_art.rating, 'user_id': user_art.user_id, 'artist_id': user_art.artist_id} for user_art in user_arts]
    return jsonify(user_art_list)

# GET all sketches
@app.route('/sketches', methods=['GET'])
def get_sketches():
    sketches = Sketch.query.all()
    sketch_list = [{'id': sketch.id, 'title': sketch.title, 'description': sketch.description, 'image_url': sketch.image_url} for sketch in sketches]
    return jsonify(sketch_list)

# GET all arts
@app.route('/arts', methods=['GET'])
def get_arts():
    arts = Art.query.all()
    art_list = [{'id': art.id, 'name': art.name, 'rating': art.rating, 'price': art.price} for art in arts]
    return jsonify(art_list)

if __name__ == '__main__':
    app.run(port=5000)