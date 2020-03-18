from mongoengine import *

#Connection to the Database

connect('IReNEdb', host='mongodb://localhost:27017/IReNEdb')


class Collaborator(Document):
    documentsID =  ListField(IntField(required=True))
    first_name = StringField(max_length=50, required=True)
    last_name = StringField(max_length=50, required=True)
    email = EmailField(required=True)
    banned = BooleanField(default=False,required=True)
    faculty = StringField(max_length=50, required=True)
    status = BooleanField(default=False,required=True)

class Session(Document):
    sessionToken = StringField(max_length=100, required=True)
    startDate = DateTimeField(required=True)
    endDate = DateTimeField(required=True)


class Admin(Document):
    username = StringField(max_length=50, required=True)
    password = StringField(max_length=50, required=True)

class TagList(Document):
    tagItem = ListField(StringField(max_length=50,required=True))

class Infrastructure(Document):
    infrastructureType = ListField(StringField(max_length=50, required=True))
    
class Damage(Document):
    damageType = ListField(StringField(max_length=50, required=True))

class Location(EmbeddedDocument):
    city = StringField(max_length=50, required=True)

class Author(EmbeddedDocument):
    author_FN = StringField(max_length=50, required=True)
    author_LN = StringField(max_length=50, required=True)
    author_email = EmailField(required=True)
    author_faculty = StringField(max_length=50, required=True)

class Actor(EmbeddedDocument):
    actor_FN = StringField(max_length=50, required=True)
    actor_LN = StringField(max_length=50, required=True)
    role = StringField(max_length=50, required=True)

class Timeline(EmbeddedDocument):
    event = StringField(max_length=2000, required=True)
    eventDate = DateTimeField(required=True)

class Section(EmbeddedDocument):
    secTitle = StringField(max_length=50, required=True)
    content = StringField(required=True)

class DocumentCase(Document):
    title = StringField(max_length=100, required=True)
    description = StringField(max_length=2000, required=True)
    published = BooleanField(default=False,required=True)
    incidentDate = DateTimeField(required=True)
    creationDate = DateTimeField(required=True)
    tagsDoc = ListField(StringField(max_length=50,required=True))
    infrasDocList =  ListField(StringField(max_length=50,required=True))
    damageDocList =  ListField(StringField(max_length=50,required=True))
    location = ListField(EmbeddedDocumentField(Location))
    author = ListField(EmbeddedDocumentField(Author))
    actor = ListField(EmbeddedDocumentField(Actor))
    section = ListField(EmbeddedDocumentField(Section))
    timeline = ListField(EmbeddedDocumentField(Timeline))



# collab = Collaborator( collabID = 1, documentsID = [1,2,3], first_name = "Jainel", 
# last_name = "Torres", email = "jainel.torres@upr.edu", faculty = "ICOM")
# collab.save()
admin1 = Admin(username = "jait", password = "loco")
admin1.save()
# for user in Collaborator.objects:
#     print (user.id)

# page = Page(comments=[comment1, comment2])
# date_modified = DateTimeField(default=datetime.datetime.utcnow)

# doc1 = DocumentCase( )

