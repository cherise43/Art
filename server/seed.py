from models import User, Pic, Artist, UserArt, Sketch
from app import app, db
from faker import Faker
import random

faker = Faker()

# Function to generate a random image URL
def generate_random_image_url():
    image_categories = ["abstract", "animals", "nature", "food", "people"]
    image_category = random.choice(image_categories)
    image_id = random.randint(1, 1000)
    return f"https://placeimg.com/640/480/{image_category}/{image_id}"

with app.app_context():
    db.drop_all()
    db.create_all()

    # Seed Users
    users = []
    for _ in range(10):
        user = User(
            user_name=faker.user_name(),
            password=faker.password()
        )
        users.append(user)
    db.session.add_all(users)
    db.session.commit()

    # Seed Pics with random image URLs
    pics = []
    for _ in range(10):
        pic = Pic(
            caption=faker.sentence(),
            image_url=generate_random_image_url(),
            user_id=random.choice(users).id
        )
        pics.append(pic)
    db.session.add_all(pics)
    db.session.commit()

    # Seed Artists
    artists = []
    for _ in range(5):
        artist = Artist(
            name=faker.name(),
            rating=random.randint(1, 5),
            price=random.randint(10, 100)
        )
        artists.append(artist)
    db.session.add_all(artists)
    db.session.commit()

    # Seed UserArt
    user_arts = []
    for _ in range(20):
        user_art = UserArt(
            rating=random.randint(1, 5),
            user_id=random.choice(users).id,
            artist_id=random.choice(artists).id
        )
        user_arts.append(user_art)
    db.session.add_all(user_arts)
    db.session.commit()

    # Seed Sketches with random image URLs
    sketches = []
    for _ in range(10):
        sketch = Sketch(
            title=faker.sentence(),
            description=faker.paragraph(),
            image_url=generate_random_image_url()
        )
        sketches.append(sketch)
    db.session.add_all(sketches)
    db.session.commit()

print("Database seeding completed.")