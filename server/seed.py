from models import User, Pic, Sketch
from app import app, db
from faker import Faker
from faker_file.providers.jpeg_file import JpegFileProvider
from faker_file.storages.filesystem import FileSystemStorage

faker = Faker()


with app.app_context():
    User.query.delete()
    Pic.query.delete()
    Sketch.query.delete()

 
    pictures = [

    ]
    for i in range(10):
        # faker.image.transport(width?: number = 640, height?: number = 480, randomize?: boolean = false): string
        call_pictures = Pic(image_url=faker.image.nature())
        pictures.append(call_pictures)
        db.session.add_all(pictures)
        db.session.commit()

    # sketchy =[

    # ]


    