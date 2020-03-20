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
    email = EmailField(required=True)
    banned = BooleanField(default=False,required=True)
    faculty = StringField(min_length=1, required=True)
    status = BooleanField(default=False,required=True)

class Session(Document):
    sessionToken = StringField(min_length=1, required=True)
    startDate = DateTimeField(required=True)
    endDate = DateTimeField(required=True)

class Admin(Document):
    username = StringField(min_length=1, required=True)
    password = StringField(min_length=1, required=True)

class Tag(Document):
    tagItem = StringField(min_length=1,required=True)

class Infrastructure(Document):
    infrastructureType = StringField(min_length=1, required=True)
    
class Damage(Document):
    damageType = StringField(min_length=1, required=True)

class Author(EmbeddedDocument):
    author_FN = StringField(min_length=1, required=True)
    author_LN = StringField(min_length=1, required=True)
    author_email = EmailField(required=True)
    author_faculty = StringField(min_length=1, required=True)

class Actor(EmbeddedDocument):
    actor_FN = StringField(min_length=1, required=False)
    actor_LN = StringField(min_length=1, required=False)
    role = StringField(min_length=1, required=False)

class Timeline(EmbeddedDocument):
    event = StringField(min_length=1, required=True)
    eventDate = DateTimeField(required=True)

class Section(EmbeddedDocument):
    secTitle = StringField(min_length=1, required=True)
    content = StringField(required=True)

class DocumentCase(Document):
    idCollab = StringField(min_length=1, required=True)
    title = StringField(min_length=1, required=True)
    location = ListField(StringField(min_length=1,required=True))
    description = StringField(min_length=1, required=True)
    published = BooleanField(default=False,required=True)
    incidentDate = DateTimeField(required=True)
    creationDate = DateTimeField(required=True)
    tagsDoc = ListField(StringField(min_length=1,required=True))
    infrasDocList =  ListField(StringField(min_length=1,required=True))
    damageDocList =  ListField(StringField(min_length=1,required=True))
    author = ListField(EmbeddedDocumentField(Author))
    actor = ListField(EmbeddedDocumentField(Actor))
    section = ListField(EmbeddedDocumentField(Section))
    timeline = ListField(EmbeddedDocumentField(Timeline))



