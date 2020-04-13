from mongoengine import *
import datetime
import regex

#Connection to the Database
connect('IReNEdb')
#connec the db for testing purposes
#connect('IReNEdb', host='mongomock://localhost', alias='IReNEdb')


class Collaborator(Document):
    documentsID =  ListField(StringField(required=False))
    first_name = StringField(min_length=1, max_length=30, required=True)
    last_name = StringField(min_length=1, max_length=30, required=True)
    email = EmailField(required=True,max_length=50, unique=True, regex='(.*)\.(.*)@upr\.edu')
    banned = BooleanField(default=False,required=True)
    approved = BooleanField(default=False,required=True)

class Admin(Document):
    username = StringField(min_length=8, required=True, unique=True)
    password = StringField(min_length=8, required=True, regex='(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])')

class Tag(Document):
    tagItem = StringField(min_length=1, max_length=20, required=True, unique=True)

class Infrastructure(Document):
    infrastructureType = StringField(min_length=1,max_length=30, required=True, unique=True)
    
class Damage(Document):
    damageType = StringField(min_length=1,max_length=30, required=True, unique=True)

class Author(EmbeddedDocument):
    author_FN = StringField(min_length=1,max_length=30, required=True)
    author_LN = StringField(min_length=1,max_length=30, required=True)
    author_email = EmailField(min_length=1,max_length=50, required=True, regex='(.*)\.(.*)@upr\.edu')
    author_faculty = StringField(min_length=1,max_length=30, required=True)

class Actor(EmbeddedDocument):
    actor_FN = StringField(min_length=1, max_length=30, required=True)
    actor_LN = StringField(min_length=1,max_length=30, required=True)
    role = StringField(min_length=1,max_length=30, required=True)

class Timeline(EmbeddedDocument):
    event = StringField(min_length=10, max_length=250, required=True)
    eventStartDate = StringField(min_length=1, required=True, regex='[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')
    eventEndDate = StringField(min_length=1, required=True, regex='[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')

class Section(EmbeddedDocument):
    secTitle = StringField(min_length=1, max_length=250, required=True)
    content = StringField(required=True)

class DocumentCase(Document):
    creatoriD = StringField(min_length=1, required=True)
    title = StringField(min_length=10, max_length = 250, required=True, unique=True)
    language = StringField(min_length=1, required=True)
    location = ListField(StringField(min_length=1,required=True))
    description = StringField(min_length=10, max_length=500,required=False)
    published = BooleanField(default=False,required=True)
    incidentDate = StringField(min_length=1, required=True, regex='[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')
    creationDate = StringField(min_length=1, required=True, regex='[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')
    lastModificationDate = StringField(min_length=1, required=True, regex='[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')
    tagsDoc = ListField(StringField(min_length=1,max_length=30,required=True))
    infrasDocList =  ListField(StringField(min_length=1,max_length=30,required=True))
    damageDocList =  ListField(StringField(min_length=1,max_length=30,required=True))
    author = ListField(EmbeddedDocumentField(Author))
    actor = ListField(EmbeddedDocumentField(Actor))
    section = ListField(EmbeddedDocumentField(Section))
    timeline = ListField(EmbeddedDocumentField(Timeline))



