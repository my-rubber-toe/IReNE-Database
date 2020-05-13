from mongoengine import *
import json

#Connection to the Database
connect('IReNEdb')
#connect the db for testing purposes
#connect('IReNEdb', host='mongomock://localhost:27017')




class collaborator(Document):
    """
        Document Class for Collaborators.
        Collaborators are the users that will Create/Edit Case Studies.
        List of attributes (All of them are required):
            - first_name: <String> Collaborator's first name.
                - attribute follows following regex: ^[A-ZÁÉÍÓÚÑÜ][a-z A-Z \- À-ÿ]*$
                - min_Length : 1, max_length: 30
            - last_name: <String> Collaborator's last name.
                - attribute follows following regex: ^[A-ZÁÉÍÓÚÑÜ][a-z A-Z \- À-ÿ]*[a-záéíóúñü]$
                - min_Length : 1, max_length: 60
            - email: <String> Collaborator's email. It must be a @upr.edu email.
                - attribute follows following regex: ^[\.a-z0-9]*(@upr\.edu)$
                - min_Length : 9, max_length: 70
            - banned: <Boolean> <Default=False> When set to true, the Collaborator looses access to Tellspace service.
            - approved: <Boolean> <Default=False>  When set to true, the Collaborator gains access to Tellspace service.
    """
    first_name = StringField(min_length=1, max_length=30, required=True, regex='^[A-ZÁÉÍÓÚÑÜ][a-z A-Z \- À-ÿ]*$')
    last_name = StringField(min_length=1, max_length=60, required=True, regex='^[A-ZÁÉÍÓÚÑÜ][a-z A-Z \- À-ÿ]*[a-záéíóúñü]$')
    email = EmailField(min_length= 9,max_length=70, required=True, unique=True, regex='^[\.a-z0-9]*(@upr\.edu)$')
    banned = BooleanField(default=False,required=True)
    approved = BooleanField(default=False,required=True)

class admin(Document):
    """
        Document Class for Admin.
        Admin are the users that will have access to the Admin Dashboard.
        These attributes will be the credentials of the Admins for them to enter the Admin Dashboard.
        List of attributes(All of them are required):
            - username: <String>  Admin's username.
                - attribute follows following regex: (^[^.]([a-zA-Z0-9]*)[\.]([a-zA-Z0-9]*))[^.]$
                - min_Length : 6, max_length: 20
            - password: <String> Admin's  password.
    """
    username = StringField(min_length=6, max_length=20, required=True, unique=True, regex='(^[^.]([a-zA-Z0-9]*)[\.]([a-zA-Z0-9]*))[^.]$' )
    password = StringField(required=True)

class tag(Document):
    """
        Document Class for Tag.
        Tag are the tags available for used as keywords for the DocumentCase.
        There will be some pre-defined by the Team and/or Admin, and the majority will be created by the
        Collaborators.
        List of attributes:
            - tagItem: <String>  Tag that can be used in a DocumentCase.
                - attribute follows following regex: ^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$
                - min_Length : 1, max_length: 50, required, unique
    """
    tagItem = StringField(min_length=1, max_length=50, required=True, unique=True, regex='^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$')

class infrastructure(Document):
    """
        Document Class for Infrastructure.
        These are going to be the categories available for the description of the
        infrastructure in the DocumentCase.
        All of them  will be pre-defined by the Team and/or Admins.
        List of attributes:
            - infrastructureType: <String>  category that can be used in a DocumentCase.
                - attribute follows following regex: ^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$
                - min_Length : 1, max_length: 50, required, unique
    """
    infrastructureType = StringField(min_length=1,max_length=50, required=True, unique=True, regex='^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$')
    
class damage(Document):
    """
        Document Class for Damage.
        These are going to be the categories available for the description of the
        Damage in the DocumentCase.
        All of them  will be pre-defined by the Team and/or Admins.
        List of attributes:
            - damageType: <String>  category that can be used in a DocumentCase.
                - attribute follows following regex: ^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$
                - min_Length : 1, max_length: 50, required, unique
    """
    damageType = StringField(min_length=1,max_length=50, required=True, unique=True, regex='^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$')

class city_pr(Document):
    """
        Document Class for CityPR.
        These are going to be the list of cities of Puerto Rico for the use of selection location
        for DocumentCase & as a filter list for a visualization.
        All of them  will be pre-defined by the Team.
        List of attributes(All of them are required):
            - city: <String>  address of a city of PR.
                - attribute follows following regex: ^[A-ZÁÉÍÓÚ][A-Z a-z À-ÿ]*(, PR)$
                - min_Length : 1, max_length: 50, unique
            - latitude: <Decimal> city's latitude.
                - min: 17.87, max: 18.53
            - longitude: <Decimal> city's longitude
                - min: -67.28, max: -65.23
    """
    city = StringField(min_length=1,max_length=50, required=True, unique=True, regex='^[A-ZÁÉÍÓÚ][A-Z a-z À-ÿ]*(, PR)$')
    latitude = DecimalField(min_value=17.87, max_value= 18.53, required=True)
    longitude = DecimalField(min_value=-67.28, max_value=-65.23, required=True) 

class author(EmbeddedDocument):
    """
        EmbeddedDocument Class for Author.
        These are going to be the authors of a DocumentCase, the ones who wrote it.
        An EmbeddedDocument is a Document Class that is defined inside another document.
        This one is going to be defined, and stored inside the DocumentCase Class.
        The reason for this technique is that the Author Class has its own schema.
        List of attributes(All of them are required):
            - author_FN: <String>  Author's First Name.
                - attribute follows following regex: ^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ]*[a-záéíóúñü]$
                - min_Length : 1, max_length: 30
            - author_LN: <String>  Author's Last Name.
                - attribute follows following regex: ^[A-ZÁÉÍÓÚÑÜ][a-z A-Z \- À-ÿ]*[a-záéíóúñü]$
                - min_Length : 1, max_length: 30
            - author_email: <String>  Author's Email.
                - attribute follows following regex: ^[\.a-z0-9]*(@upr\.edu)$
                - min_Length : 9, max_length: 70
            - author_faculty: <String>  Author's Faculty.
                - attribute follows following regex: ^[A-ZÁÉÍÓÚÑÜ][a-z A-Z \- \. : 0-9 À-ÿ]*$
                - min_Length : 1, max_length: 30
    """
    author_FN = StringField(min_length=1,max_length=30, required=True, regex='^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ]*[a-záéíóúñü]$')
    author_LN = StringField(min_length=1,max_length=30, required=True, regex='^[A-ZÁÉÍÓÚÑÜ][a-z A-Z \- À-ÿ]*[a-záéíóúñü]$')
    author_email = EmailField(min_length=9,max_length=70, required=True, regex='^[\.a-z0-9]*(@upr\.edu)$')
    author_faculty = StringField(min_length=1,max_length=30, required=True, regex='^[A-ZÁÉÍÓÚÑÜ][a-z A-Z \- \. : 0-9 À-ÿ]*$')

class actor(EmbeddedDocument):
    """
        EmbeddedDocument Class for Actor.
        These are going to be the Actor of a DocumentCase, the ones having a role in the DocumentCase.
        An EmbeddedDocument is a Document Class that is defined inside another document.
        This one is going to be defined, and stored inside the DocumentCase Class.
        The reason for this technique is that the Actor Class has its own schema.
        List of attributes(All of them are required):
            - actor_FN: <String>  Actor's First Name.
                - attribute follows following regex: ^[A-ZÁÉÍÓÚÑÜ][a-z A-Z \- \. : À-ÿ]*$
                - min_Length : 1, max_length: 30
            - actor_LN: <String>  Actor's Last Name.
                - attribute follows following regex: ^[A-ZÁÉÍÓÚÑÜ][a-z A-Z \- \. : À-ÿ]*$
                - min_Length : 1, max_length: 30
            - role: <String>  Actor's role in the DocumentCase.
                - attribute follows following regex: ^[A-ZÁÉÍÓÚÑÜ][a-z A-Z \- \. : 0-9 À-ÿ]*$
                - min_Length : 1, max_length: 30
    """
    actor_FN = StringField(min_length=1, max_length=30, required=True, regex='^[A-ZÁÉÍÓÚÑÜ][a-z A-Z \- \. : À-ÿ]*$')
    actor_LN = StringField(min_length=1,max_length=30, required=True, regex='^[A-ZÁÉÍÓÚÑÜ][a-z A-Z \- \. : À-ÿ]*$')
    role = StringField(min_length=1,max_length=30, required=True, regex= '^[A-ZÁÉÍÓÚÑÜ][a-z A-Z \- \. : 0-9 À-ÿ]*$')

class timeline(EmbeddedDocument):
    """
        EmbeddedDocument Class for Timeline.
        These will consist of the Timeline of a DocumentCase, describing the events followed.
        An EmbeddedDocument is a Document Class that is defined inside another document.
        This one is going to be defined, and stored inside the DocumentCase Class.
        The reason for this technique is that the Timeline Class has its own schema.
        List of attributes(All of them are required):
            - event: <String>  Event happend within the DocumentCase.
                - min_Length : 10, max_length: 100
            - eventStartDate: <String>  Date when the event started, it has to have the following format: 'YYYY-MM-DD'.
                - attribute follows following regex: [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]
                - min_Length : 9, max_length: 11
            - eventEndDate: <String>  Date when the event ended, it has to have the following format: 'YYYY-MM-DD'.
                - attribute follows following regex: [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]
                - min_Length : 9, max_length: 11
    """
    event = StringField(min_length=10, max_length=100, required=True)
    eventStartDate = StringField(min_length=9, max_length=11, required=True, regex='[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')
    eventEndDate = StringField(min_length=9, max_length=11,  required=True, regex='[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')

class section(EmbeddedDocument):
    """
        EmbeddedDocument Class for Section.
        These are going to be the body of the Document Case.
        An EmbeddedDocument is a Document Class that is defined inside another document.
        This one is going to be defined, and stored inside the DocumentCase Class.
        The reason for this technique is that the Section Class has its own schema.
        List of attributes(All of them are required):
            - secTitle: <String>  Section's title.
                - attribute follows following regex: ^([A-ZÁÉÍÓÚÑÜ]+)([A-Z a-z 0-9 À-ÿ : \-]*)([A-Za-z0-9À-ÿ]$)
                - min_Length : 1, max_length: 100
            - content: <String>  Section's body.
                - min_Length : 1
    """
    secTitle = StringField(min_length=1, max_length=100, required=True, regex='^([A-ZÁÉÍÓÚÑÜ]+)([A-Z a-z 0-9 À-ÿ : \-]*)([A-Za-z0-9À-ÿ]$)')
    content = StringField(min_length=1, required=True)


class location(EmbeddedDocument):
    """
        EmbeddedDocument Class for Location.
        These are going to be the body of the Document Case.
        An EmbeddedDocument is a Document Class that is defined inside another document.
        This one is going to be defined, and stored inside the DocumentCase Class.
        The reason for this technique is that the Location Class has its own schema.
        List of attributes:
            - address: <String>  Location's address.
                - attribute follows following regex: ^[A-ZÁÉÍÓÚ][A-Z a-z À-ÿ]*(, PR)$
                - min_Length : 1, max_length: 50
            - latitude: <Decimal> city's latitude.
                - min: 17.87, max: 18.53
            - longitude: <Decimal> city's longitude
                - min: -67.28, max: -65.23
    """
    address = StringField(min_length=1, max_length=50, required=True, regex='^[A-ZÁÉÍÓÚ][A-Z a-z À-ÿ]*(, PR)$')
    latitude = FloatField(min_value=17.86, max_value=18.54, required=True)
    longitude = FloatField(min_value=-67.29, max_value=-65.22, required=True)


class document_case(Document):
    """
        Document Class for DocumentCase.
        DocumentCase will consist of a Case Study created by a Collaborator.
        List of attributes:
            - Required: creatoriD, title, language, published, incidentDate, creationDate, lastModificationDate,
                infrasDocList, damageDocList, author, actor
            - creatoriD: <String>  the Collaborator's id which created the Case study.
            - title: <String> The case study's title.
                - attribute follows following regex: ^([A-ZÁÉÍÓÚÑÜ]+)([A-Z a-z 0-9 À-ÿ : \-]*)([A-Za-z0-9À-ÿ]$)
                - min_Length : 10, max_length: 100
            - language: <String> The language which the case study is written.
                - attribute follows following regex: ^[A-Z][a-z]*$
                - min_Length : 1, max_length: 20
            - description: <String> Case study's description.
                - min_Length : 1, max_length: 500
            - published: <Boolean> <Default=False> When set to true, the case study will be visible in SearchSpace service.
            - incidentDate: <String>  Date when the incident happened, it has to have the following format: 'YYYY-MM-DD'.
                - attribute follows following regex: [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]
                - min_Length : 9, max_length: 11
            - creationDate: <String>  Date when the case study was created, it has to have the following format: 'YYYY-MM-DD'.
                - attribute follows following regex: [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]
                - min_Length : 9, max_length: 11
            - lastModificationDate: <String>  Last date when the case study was modified, it has to have the following format: 'YYYY-MM-DD'.
                - attribute follows following regex: [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]
                - min_Length : 9, max_length: 11
            - tagsDoc: List<String> of tags from the case study.
                - For string:
                    - attribute follows following regex: ^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$
                    - min_Length : 1, max_length: 50, Required, Unique
                - For List:
                    - min_Length : 0, max_length: 10
            - infrasDocList: List<String> of infrastructure categories from the case study.
                - For string:
                    - attribute follows following regex: ^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$
                    - min_Length : 1, max_length: 50, Required, Unique
                - For List:
                    - min_Length : 1
            - damageDocList: List<String> of damage categories from the case study.
                - For string:
                    - attribute follows following regex: ^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$
                    - min_Length : 1, max_length: 50, Required, Unique
                - For List:
                    - min_Length : 1
            - location: List<Location> of addresses where the case study took place.
                - max_length: 5
            - author: List<Author> of author objects, the ones who wrote the case study.
                - min_Length : 1, max_length: 10
            - actor: List<Actor> of actor objects, the ones who plays a role in the case study.
                - min_Length : 1, max_length: 5
            - section: List<Section> of section objects, this will consist the body of the case study.
                - max_length: 10
            - timeline: List<Timeline> of timeline objects, this will consist of the events that happened within the case study.
                - max_length: 5
    """
    creatoriD = ReferenceField('collaborator')
    title = StringField(min_length=10, max_length = 100, required=True, unique=True, regex="^([A-ZÁÉÍÓÚÑÜ]+)([A-Z a-z 0-9 À-ÿ : \-]*)([A-Za-z0-9À-ÿ]$)")
    language = StringField(min_length=1, max_length=20,required=True, regex="^[A-Z][a-z]*$")
    description = StringField(min_length=1, max_length=500,required=False)
    published = BooleanField(default=True,required=True)
    incidentDate = StringField(min_length=9, max_length=11, required=True, regex='[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')
    creationDate = StringField(min_length=9, max_length=11, required=True, regex='[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')
    lastModificationDate = StringField(min_length=9, max_length=11, required=True, regex='[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')
    tagsDoc = ListField(StringField(min_length=1,max_length=50, unique=True, regex='^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$'), required=False, max_length=10)
    infrasDocList = ListField(StringField(min_length=1,max_length=50,required=True, unique=True, regex='^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$'),min_length=1)
    damageDocList = ListField(StringField(min_length=1,max_length=50,required=True, unique=True, regex='^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$'),min_length=1)
    location = ListField(EmbeddedDocumentField(location), max_length=5, required=False)
    author = ListField(EmbeddedDocumentField(author), min_length=1, max_length=10, required=True)
    actor = ListField(EmbeddedDocumentField(actor),min_length=1, max_length=5, required=True)
    section = ListField(EmbeddedDocumentField(section), max_length=10, required=False)
    timeline = ListField(EmbeddedDocumentField(timeline), max_length=5, required=False)


class creation_embedded(EmbeddedDocument):
    """
        Document Class for creation_embedded.
        creation_embedded will consist of a revision for a created case study.
        List of attributes:
            - Required: creatoriD, title, language, published, incidentDate, creationDate, lastModificationDate,
                infrasDocList, damageDocList, author, actor
            - creatoriD: <String>  the Collaborator's id which created the Case study.
            - title: <String> The case study's title.
                - attribute follows following regex: ^([A-ZÁÉÍÓÚÑÜ]+)([A-Z a-z 0-9 À-ÿ : \-]*)([A-Za-z0-9À-ÿ]$)
                - min_Length : 10, max_length: 100
            - language: <String> The language which the case study is written.
                - attribute follows following regex: ^[A-Z][a-z]*$
                - min_Length : 1, max_length: 20
            - description: <String> Case study's description.
                - min_Length : 1, max_length: 500
            - published: <Boolean> <Default=False> When set to true, the case study will be visible in SearchSpace service.
            - incidentDate: <String>  Date when the incident happened, it has to have the following format: 'YYYY-MM-DD'.
                - attribute follows following regex: [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]
                - min_Length : 9, max_length: 11
            - creationDate: <String>  Date when the case study was created, it has to have the following format: 'YYYY-MM-DD'.
                - attribute follows following regex: [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]
                - min_Length : 9, max_length: 11
            - lastModificationDate: <String>  Last date when the case study was modified, it has to have the following format: 'YYYY-MM-DD'.
                - attribute follows following regex: [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]
                - min_Length : 9, max_length: 11
            - tagsDoc: List<String> of tags from the case study.
                - For string:
                    - attribute follows following regex: ^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$
                    - min_Length : 1, max_length: 50, Required, Unique
                - For List:
                    - min_Length : 0, max_length: 10
            - infrasDocList: List<String> of infrastructure categories from the case study.
                - For string:
                    - attribute follows following regex: ^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$
                    - min_Length : 1, max_length: 50, Required, Unique
                - For List:
                    - min_Length : 1
            - damageDocList: List<String> of damage categories from the case study.
                - For string:
                    - attribute follows following regex: ^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$
                    - min_Length : 1, max_length: 50, Required, Unique
                - For List:
                    - min_Length : 1
            - location: List<Location> of addresses where the case study took place.
                - max_length: 5
            - author: List<Author> of author objects, the ones who wrote the case study.
                - min_Length : 1, max_length: 10
            - actor: List<Actor> of actor objects, the ones who plays a role in the case study.
                - min_Length : 1, max_length: 5
            - section: List<Section> of section objects, this will consist the body of the case study.
                - max_length: 10
            - timeline: List<Timeline> of timeline objects, this will consist of the events that happened within the case study.
                - max_length: 5
    """
    creatoriD = ReferenceField('collaborator')
    title = StringField(min_length=10, max_length = 100, required=True, unique=True, regex="^([A-ZÁÉÍÓÚÑÜ]+)([A-Z a-z 0-9 À-ÿ : \-]*)([A-Za-z0-9À-ÿ]$)")
    language = StringField(min_length=1, max_length=20,required=True, regex="^[A-Z][a-z]*$")
    description = StringField(min_length=1, max_length=500,required=False)
    published = BooleanField(default=True,required=True)
    incidentDate = StringField(min_length=9, max_length=11, required=True, regex='[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')
    creationDate = StringField(min_length=9, max_length=11, required=True, regex='[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')
    lastModificationDate = StringField(min_length=9, max_length=11, required=True, regex='[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')
    tagsDoc = ListField(StringField(min_length=1,max_length=50, unique=True, regex='^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$'), required=False, max_length=10)
    infrasDocList = ListField(StringField(min_length=1,max_length=50,required=True, unique=True, regex='^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$'),min_length=1)
    damageDocList = ListField(StringField(min_length=1,max_length=50,required=True, unique=True, regex='^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$'),min_length=1)
    location = ListField(EmbeddedDocumentField(location), max_length=5, required=False)
    author = ListField(EmbeddedDocumentField(author), min_length=1, max_length=10, required=True)
    actor = ListField(EmbeddedDocumentField(actor),min_length=1, max_length=5, required=True)
    section = ListField(EmbeddedDocumentField(section), max_length=10, required=False)
    timeline = ListField(EmbeddedDocumentField(timeline), max_length=5, required=False)

    def _author_to_json(self):
        auth = []
        for author in self.author:
            auth.append(json.loads(author.to_json()))
        return auth

    def _actor_to_json(self):
        actor = []
        for act in self.actor:
            actor.append(json.loads(act.to_json()))
        return actor

    def _timeline_to_json(self):
        timeline = []
        for timeL in self.timeline:
            timeline.append({
                'event': timeL.event,
                'eventStartDate': timeL.eventStartDate,
                'eventEndDate': timeL.eventEndDate
            })
        return timeline

    def _location_to_json(self):
        locations = []
        for location in self.location:
            locations.append(location.address)
        return locations

    def _section_to_json(self):
        sections = []
        for section in self.section:
            sections.append(
                {
                    'secTitle': section.secTitle,
                    'content': section.content
                }
            )
        return sections

    def to_json(self):
        if (self.title is None):
            return {}
        else:
            return {
                'creatoriD': str(self.creatoriD.id),
                'title': self.title,
                'language': self.language,
                'location': self._location_to_json(),
                'description': self.description,
                'published': self.published,
                'incidentDate': self.incidentDate,
                'creationDate': self.creationDate,
                'lastModificationDate': self.lastModificationDate,
                'tagsDoc': self.tagsDoc,
                'infrasDocList': self.infrasDocList,
                'damageDocList': self.damageDocList,
                'author': self._author_to_json(),
                'actor': self._actor_to_json(),
                'section': self._section_to_json(),
                'timeline': self._timeline_to_json()
            }


class title_embedded(EmbeddedDocument):
    """
        Document Class for title_embedded.
        title_embedded will consist of a revision for the title of a case study.
        List of attributes:
            - title: <String> the title of the revised case study.
                - attribute follows following regex: ^([A-ZÁÉÍÓÚÑÜ]+)([A-Z a-z 0-9 À-ÿ : \-]*)([A-Za-z0-9À-ÿ]$)
                - min_Length : 10, max_length: 100, required
    """
    title = StringField(min_length=10, max_length=100, required=True, regex="^([A-ZÁÉÍÓÚ]+)([A-Z a-z 0-9 À-ÿ : \-]*)([A-Za-z0-9áéíóú]$)")

    def to_json(self):
        return self.title


class description_embedded(EmbeddedDocument):
    """
        Document Class for description_embedded.
        description_embedded will consist of a revision for the description of a case study.
        List of attributes:
            - description: <String> the description of the revised case study.
                - min_Length : 1, max_length: 500
    """
    description = StringField(min_length=0, max_length=500, required=False)

    def to_json(self):
        return self.description


class infrastructure_embedded(EmbeddedDocument):
    """
        Document Class for infrastructure_embedded.
        infrastructure_embedded will consist of a revision for the list of infrastructure types of a case study.
        List of attributes:
            - infrasDocList: List<String> the list of categories for infrastructure type for the revised case study.
                - For string:
                    - attribute follows following regex: ^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$
                    - min_Length : 1, max_length: 50, Required
    """
    infrasDocList = ListField(StringField(min_length=1,max_length=50,required=True, 
        regex='^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$'))

    def to_json(self):
        return self.infrasDocList


class timeline_embedded(EmbeddedDocument):
    """
        Document Class for timeline_embedded.
        timeline_embedded will consist of a revision for the timeline of a case study.
        List of attributes:
            - timeline: List<timeline> the timeline of the revised case study.
    """
    timeline = ListField(EmbeddedDocumentField(timeline))

    def to_json(self):
        timeline = []
        for timeL in self.timeline:
            timeline.append({
                'event': timeL.event,
                'eventStartDate': timeL.eventStartDate,
                'eventEndDate': timeL.eventEndDate
            })
        return timeline


class section_embedded(EmbeddedDocument):
    """
        Document Class for section_embedded.
        section_embedded will consist of a revision for the section of a case study.
        List of attributes:
            - section: <section> the section of the revised case study.
    """
    section = EmbeddedDocumentField(section)

    def to_json(self):
        if (self.section == None):
            return {}
        return {
            'secTitle': self.section.secTitle,
            'content': self.section.content
        }


class damage_embedded(EmbeddedDocument):
    """
        Document Class for damage_embedded.
        damage_embedded will consist of a revision for the list of damage types of a case study.
        List of attributes:
            - damageDocList: List<String> the list of categories for damage type for the revised case study.
                - For string:
                    - attribute follows following regex: ^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$
                    - min_Length : 1, max_length: 50, Required
    """
    damageDocList = ListField(StringField(min_length=1,max_length=50,required=True, 
        regex='^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$'))

    def to_json(self):
        return self.damageDocList


class actor_embedded(EmbeddedDocument):
    """
        Document Class for actor_embedded.
        actor_embedded will consist of a revision for the actors of a case study.
        List of attributes:
            - actor: List<actor> the actors of the revised case study.
    """
    actor = ListField(EmbeddedDocumentField(actor))

    def to_json(self):
        actors = []
        for actor in self.actor:
            actors.append(
                {'actor_FN': actor.actor_FN,
                 'actor_LN': actor.actor_LN,
                 'role': actor.role})
        return actors


class author_embedded(EmbeddedDocument):
    """
        Document Class for author_embedded.
        author_embedded will consist of a revision for the authors of a case study
        List of attributes:
            - author: List<author> the authors of the revised case study.
    """
    author = ListField(EmbeddedDocumentField(author))

    def to_json(self):
        authors = []
        for author in self.author:
            authors.append(
                {'author_FN': author.author_FN,
                 'author_LN': author.author_LN,
                 'author_email': author.author_email,
                 'author_faculty': author.author_faculty})
        return authors


class incident_embedded(EmbeddedDocument):
    """
        Document Class for incident_embedded.
        incident_embedded will consist of a revision for the incident date of a case study
        List of attributes:
            - incidentDate: <string> the incident date of the revised case study.
    """
    incidentDate = StringField(min_length=9, max_length=11, required=True, regex='[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')
    def to_json(self):
        return self.incidentDate


class tag_embedded(EmbeddedDocument):
    """
        Document Class for tag_embedded.
        tag_embedded will consist of a revision for the list of tags of a case study.
        List of attributes:
            - tagsDoc: List<String> the list of tags for the revised case study.
                - For string:
                    - attribute follows following regex: ^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$
                    - min_Length : 1, max_length: 50
                - For list:
                    -  max_length: 10
    """
    tagsDoc = ListField(StringField(min_length=0,max_length=50,
        regex='^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & , \- ]*$'), required=False, max_length=10)
    def to_json(self):
        return self.tagsDoc


class location_embedded(EmbeddedDocument):
    """
        Document Class for location_embedded.
        location_embedded will consist of a revision for the locations of a case study.
        List of attributes:
            - location: List<location> the list of locations for the revised case study.
                - For List:
                   - max_length: 5
    """
    location = ListField(EmbeddedDocumentField(location), max_length=5, required=False)

    def to_json(self):
        locations = []
        for location in self.location:
            locations.append(location.address)
        return locations


class fields_embedded(EmbeddedDocument):
    """
        EmbeddedDocument Class for FieldsEmbedded. 
        These are going to be the revision log for DocumentCaseRevision.
        An EmbeddedDocument is a Document Class that is defined inside another document.
        This one is going to be defined, and stored inside the DocumentCaseRevision Class. 
        The reason for this technique is that the Section Class has its own schema.
        List of attributes:
            - old: dictionary field containing what was before the change. 
            - new: dictionary field containing the new changes made.
    """
    new = GenericEmbeddedDocumentField(required=True)
    old = GenericEmbeddedDocumentField(required=True)
    
class document_case_revision(Document):
    """
        EmbeddedDocument Class for Revision. 
        These are going to be the revision log for DocumentCaseRevision.
        An EmbeddedDocument is a Document Class that is defined inside another document.
        This one is going to be defined, and stored inside the DocumentCaseRevision Class. 
        The reason for this technique is that the Section Class has its own schema.
        List of attributes:
            - creatorId: <String> Collaborator ID who made the change.
            - docId: <String> DocumentCase id where the change was made.
            - creator_name: <String> Collaborator's name who made the change.
                - attribute follows following regex: ^[A-ZÁÉÍÓÚÑÜ][a-z A-Z \- À-ÿ]*[a-záéíóúñü]$
                - min_Length : 1, max_length: 90
            - document_title: <String> Collaborator's email who made the change.
                - attribute follows following regex: ^([A-ZÁÉÍÓÚ]+)([A-Z a-z 0-9 À-ÿ : \-]*)([A-Za-z0-9áéíóú]$)
                - min_Length : 10, max_length: 100
            - revision_date: <String> Date when the changes were made.
                - attribute follows following regex: [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]
                - min_Length : 9, max_length: 11
            - revision_number: <Integer> number id of the change made.
                - min: 0
            - revision_type: <String> Type of change.
                - attribute follows following regex: ^[a-z A-Z \- À-ÿ]*[a-záéíóúñü]$
                - min_Length : 1, max_length: 20
            - field_changed: <Revision> embedded document which contains the old & new changes made
    """
    creatorId = ReferenceField('collaborator')
    docId = ReferenceField('document_case')
    creator_name = StringField(min_length=1, max_length=90, required=True, 
        regex='^[A-ZÁÉÍÓÚÑÜ][a-z A-Z \- À-ÿ]*[a-záéíóúñü]$')
    creator_email = EmailField(required=True,min_length=9, max_length=50, regex='^[\.a-z0-9]*(@upr\.edu)$')
    document_title = StringField(min_length=10, max_length = 100, required=True, 
        regex="^([A-ZÁÉÍÓÚ]+)([A-Z a-z 0-9 À-ÿ : \-]*)([A-Za-z0-9áéíóú]$)")
    revision_date = StringField(min_length=9, max_length=11, required=True, 
        regex='[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]')
    revision_number = IntField(min_value=0, required=True)
    revision_type = StringField(min_length=1, max_length= 20, required=True, 
        regex='^[a-z A-Z \- À-ÿ]*[a-záéíóúñü]$')
    field_changed = EmbeddedDocumentField(fields_embedded)
    

