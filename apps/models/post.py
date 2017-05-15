from .. import db
from mongoengine import *


class Post(db.Document):
	title = StringField(max_length=60)
	content = StringField()
	time = DateTimeField()