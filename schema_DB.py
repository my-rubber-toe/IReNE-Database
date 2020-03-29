from mongoengine import *
import datetime

#Connection to the Database
connect('IReNEdb')
#connec the db for testing purposes
# connect('IReNEdb', host='mongomock://localhost:27017')

class Collaborator(Document):
    documentsID =  ListField(StringField(required=False))
    first_name = StringField(min_length=1, required=True)
    last_name = StringField(min_length=1, required=True)
    email = EmailField(required=True, unique=True)
    banned = BooleanField(default=False,required=True)
    faculty = StringField(min_length=1, required=True)
    approved = BooleanField(default=False,required=True)

class Session(Document):
    sessionToken = StringField(min_length=1, required=True, unique=True)
    startDate = StringField(min_length=1, required=True)
    endDate = StringField(min_length=1, required=True)

class Admin(Document):
    username = StringField(min_length=1, required=True, unique=True)
    password = StringField(min_length=1, required=True)

class Tag(Document):
    tagItem = StringField(min_length=1,required=True, unique=True)

class Infrastructure(Document):
    infrastructureType = StringField(min_length=1, required=True, unique=True)
    
class Damage(Document):
    damageType = StringField(min_length=1, required=True, unique=True)

class Author(EmbeddedDocument):
    author_FN = StringField(min_length=1, required=True)
    author_LN = StringField(min_length=1, required=True)
    author_email = EmailField(min_length=1, required=True)
    author_faculty = StringField(min_length=1, required=True)

class Actor(EmbeddedDocument):
    actor_FN = StringField(min_length=1, required=True)
    actor_LN = StringField(min_length=1, required=True)
    role = StringField(min_length=1, required=True)

class Timeline(EmbeddedDocument):
    event = StringField(min_length=1, required=True)
    eventDate = StringField(min_length=1, required=True)

class Section(EmbeddedDocument):
    secTitle = StringField(min_length=1, required=True)
    content = StringField(required=True)

class DocumentCase(Document):
    creatoriD = StringField(min_length=1, required=True)
    title = StringField(min_length=1, required=True, unique=True)
    location = ListField(StringField(min_length=1,required=True))
    description = StringField(min_length=1, required=True)
    published = BooleanField(default=False,required=True)
    incidentDate = StringField(min_length=1, required=True)
    creationDate = StringField(min_length=1, required=True)
    lastModificationDate = StringField(min_length=1, required=True)
    tagsDoc = ListField(StringField(min_length=1,required=True))
    infrasDocList =  ListField(StringField(min_length=1,required=True))
    damageDocList =  ListField(StringField(min_length=1,required=True))
    author = ListField(EmbeddedDocumentField(Author))
    actor = ListField(EmbeddedDocumentField(Actor))
    section = ListField(EmbeddedDocumentField(Section))
    timeline = ListField(EmbeddedDocumentField(Timeline))



