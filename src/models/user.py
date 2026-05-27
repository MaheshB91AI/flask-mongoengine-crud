from app import db
from mongoengine import StringField
import uuid

class User(db.Document):
    _id = StringField(primary_key = True, default=lambda: str(uuid.uuid4()))
    name = StringField(required=True)
