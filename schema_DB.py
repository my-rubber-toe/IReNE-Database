from mongoengine import *
import datetime
import regex
#Connection to the Database
connect('IReNEdb')
#connec the db for testing purposes
#connect('IReNEdb', host='mongomock://localhost', alias='IReNEdb')


class Collaborator(Document):
    """
        Document Class for Collaborators. 
        Collaborators are the users that will Create/Edit Case Studies.
        List of attributes:
            - documentsID: list<String>  of document ids that the Collaborator created.
            - first_name: <String> Collaborator's first name.
            - last_name: <String> Collaborator's last name.
            - email: <String> Collaborator's email. It must be a @upr.edu email.
                - email attribute follows this regex: '(.*)\.(.*)@upr\.edu'
            - banned: <Boolean> <Default=False> When set to true, the Collaborator looses access to Tellspace service.
            - approved: <Boolean> <Default=False>  When set to true, the Collaborator gains access to Tellspace service.     
    """
    documentsID =  ListField(StringField(required=False))
    first_name = StringField(min_length=1, max_length=30, required=True)
    last_name = StringField(min_length=1, max_length=30, required=True)
    email = EmailField(required=True,max_length=50, unique=True, regex='(.*)\.(.*)@upr\.edu')
    banned = BooleanField(default=False,required=True)
    approved = BooleanField(default=False,required=True)

class Admin(Document):
    """
        Document Class for Admin. 
        Admin are the users that will have access to the Admin Dashboard.
        These attributes will be the credentials of the Admins for them to enter the Admin Dashboard.
        List of attributes:
            - username: <String>  Admin's username.
                - username attribute follows this regex: '(^(?=[a-zA-Z0-9])(?=.*[a-z])(?=.*[0-9])(?=.*[\.])(?=.*[A-Z])).*[^.]$' 
            - password: <String> Admin's  password.   
                - password attribute follows this regex: '([a-zA-Z0-9]+)*'
    """
    username = StringField(min_length=8, max_length=20, required=True, unique=True, regex='(^(?=[a-zA-Z0-9])(?=.*[a-z])(?=.*[0-9])(?=.*[\.])(?=.*[A-Z])).*[^.]$' )
    password = StringField(min_length=8,max_length=20, required=True, regex='([a-zA-Z0-9]+)*')

class Tag(Document):
    """
        Document Class for Tag. 
        Tag are the tags available for used as keywords for the DocumentCase.
        There will be some pre-defined by the Team, and the majority will be created by the
        Collaborators.
        List of attributes:
            - tagItem: <String>  Tag that can be used in a DocumentCase.   
    """
    tagItem = StringField(min_length=1, max_length=20, required=True, unique=True)

class Infrastructure(Document):
    """
        Document Class for Infrastructure. 
        These are going to be the categories available for the description of the
        infrastructure in the DocumentCase.
        All of them  will be pre-defined by the Team.
        List of attributes:
            - infrastructureType: <String>  category that can be used in a DocumentCase.   
    """
    infrastructureType = StringField(min_length=1,max_length=30, required=True, unique=True)
    
class Damage(Document):
    """
        Document Class for Damage. 
        These are going to be the categories available for the description of the
        Damage in the DocumentCase.
        All of them  will be pre-defined by the Team.
        List of attributes:
            - damageType: <String>  category that can be used in a DocumentCase.   
    """
    damageType = StringField(min_length=1,max_length=30, required=True, unique=True)

class Author(EmbeddedDocument):
    """
        EmbeddedDocument Class for Author. 
        These are going to be the authors of a DocumentCase, the ones who wrote it.
        An EmbeddedDocument is a Document Class that is defined inside another document.
        This one is going to be defined, and stored inside the DocumentCase Class. 
        The reason for this technique is that the Author Class has its own schema.
        List of attributes:
            - author_FN: <String>  Author's First Name. 
            - author_LN: <String>  Author's Last Name.
            - author_email: <String>  Author's Email.
            - author_faculty: <String>  Author's Faculty.  
    """
    author_FN = StringField(min_length=1,max_length=30, required=False)
    author_LN = StringField(min_length=1,max_length=30, required=False)
    author_email = EmailField(min_length=1,max_length=50, required=False, regex='(.*)\.(.*)@upr\.edu')
    author_faculty = StringField(min_length=1,max_length=30, required=False)

class Actor(EmbeddedDocument):
    """
        EmbeddedDocument Class for Actor. 
        These are going to be the Actor of a DocumentCase, the ones having a role in the DocumentCase.
        An EmbeddedDocument is a Document Class that is defined inside another document.
        This one is going to be defined, and stored inside the DocumentCase Class. 
        The reason for this technique is that the Actor Class has its own schema.
        List of attributes:
            - actor_FN: <String>  Actor's First Name. 
            - actor_LN: <String>  Actor's Last Name.
            - role: <String>  Actor's role in the DocumentCase. 
    """
    actor_FN = StringField(min_length=1, max_length=30, required=False)
    actor_LN = StringField(min_length=1,max_length=30, required=False)
    role = StringField(min_length=1,max_length=30, required=False)

class Timeline(EmbeddedDocument):
    """
        EmbeddedDocument Class for Timeline. 
        These will consist of the Timeline of a DocumentCase, describing the events followed.
        An EmbeddedDocument is a Document Class that is defined inside another document.
        This one is going to be defined, and stored inside the DocumentCase Class. 
        The reason for this technique is that the Timeline Class has its own schema.
        List of attributes:
            - event: <String>  Event happend within the DocumentCase. 
            - eventStartDate: <String>  Date when the event started, it has to have the following format: 'YYYY-MM-DD'.
                 - eventStartDate attribute follows this regex: '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
            - eventEndDate: <String>  Date when the event ended, it has to have the following format: 'YYYY-MM-DD'.
                - eventEndDate attribute follows this regex: '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
    """
    event = StringField(min_length=10, max_length=250, required=False)
    eventStartDate = StringField(min_length=1, required=False, regex='[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')
    eventEndDate = StringField(min_length=1, required=False, regex='[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')

class Section(EmbeddedDocument):
    """
        EmbeddedDocument Class for Section. 
        These are going to be the body of the Document Case.
        An EmbeddedDocument is a Document Class that is defined inside another document.
        This one is going to be defined, and stored inside the DocumentCase Class. 
        The reason for this technique is that the Section Class has its own schema.
        List of attributes:
            - secTitle: <String>  Section's title. 
            - content: <String>  Section's body.  
    """
    secTitle = StringField(min_length=1, max_length=250, required=False)
    content = StringField(required=False)

class DocumentCase(Document):
    """
        Document Class for DocumentCase. 
        DocumentCase will consist of a Case Study created by a Collaborator.
        List of attributes:
            - creatoriD: <String>  the Collaborator's id which created the Case study.
            - title: <String> The case study's title .
            - language: <String> The language which the case study is written.
            - location: List<String> of addresses where the case study took place.
            - description: <String> Case study's description.
            - published: <Boolean> <Default=False> When set to true, the case study will be visible in SearchSpace service.
            - incidentDate: <String>  Date when the incident happened, it has to have the following format: 'YYYY-MM-DD'.
                 - incidentDate attribute follows this regex: '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
            - creationDate: <String>  Date when the case study was created, it has to have the following format: 'YYYY-MM-DD'.
                - creationDate attribute follows this regex: '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]' 
            - lastModificationDate: <String>  Last date when the case study was modified, it has to have the following format: 'YYYY-MM-DD'.
                - lastModificationDate attribute follows this regex: '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'  
            - tagsDoc: List<String> of tags from the case study. 
            - infrasDocList: List<String> of infrastructure categories from the case study. 
            - damageDocList: List<String> of damage categories from the case study. 
            - author: List<Author> of author objects, the ones who wrote the case study.
            - section: List<Section> of section objects, this will consist the body of the case study.
            - timeline: List<Timeline> of timeline objects, this will consist of the events that happened within the case study.
                
    """
    creatoriD = StringField(min_length=1, required=True)
    title = StringField(min_length=10, max_length = 250, required=True, unique=True)
    language = StringField(min_length=1, required=False)
    location = ListField(StringField(min_length=1,required=False))
    description = StringField(min_length=10, max_length=500,required=False)
    published = BooleanField(default=False,required=True)
    incidentDate = StringField(min_length=1, required=True, regex='[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')
    creationDate = StringField(min_length=1, required=True, regex='[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')
    lastModificationDate = StringField(min_length=1, required=True, regex='[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')
    tagsDoc = ListField(StringField(min_length=1,max_length=30,required=False))
    infrasDocList =  ListField(StringField(min_length=1,max_length=30,required=True))
    damageDocList =  ListField(StringField(min_length=1,max_length=30,required=True))
    author = ListField(EmbeddedDocumentField(Author))
    actor = ListField(EmbeddedDocumentField(Actor))
    section = ListField(EmbeddedDocumentField(Section))
    timeline = ListField(EmbeddedDocumentField(Timeline))



