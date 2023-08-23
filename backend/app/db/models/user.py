from mongoengine import Document, StringField, EmailField


class User(Document):
    name = StringField(required=True)
    email = EmailField(unique=True, required=True)
    password_hash = StringField(required=True)
