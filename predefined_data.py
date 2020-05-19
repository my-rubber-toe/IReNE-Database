from mongoengine import *
from schema_DB import *
import json
import bson
"""
    This code is to populate the predefined data that will have the database, it should 
    run only once.
"""
def Categories():
    """
        Fills the db with predefined categories & tags
        For Infrastructure Types:
            - Streets or Highway
            - Bridges
            - Airports
            - Water Supply
            - Waste Water Management
            - Power Generation/Transmission
            - Telecommunications
            - Housing
            - Building
            - Ports
            - Public Transportation
        For Damage Types:
            - Earthquake
            - Hurricane
            - Tsunami
            - Flooding
            - Landslide
            - Fire/smoke
            - Extreme Precipitation
            - Water Damage
            - Wind Damage
            - Tornado
        For Tags:
            - Earthquake
            - Hurricane
            - Flooding
            - Water
            - Fire
            - Buildings
            - Housing
            - Telecommunications
            - Ports
            - Power Generation
    """  
    infrastructures = ["Streets or Highway", "Bridges", "Airports", "Water Supply", "Waste Water Management",
    "Power Generation/Transmission", "Telecommunications" , "Housing", "Building", "Ports",
    "Public Transportation"]
    damages = [ "Earthquake", "Hurricane", "Tsunami", "Flooding", "Landslide", "Fire/smoke", 
    "Extreme Precipitation", "Water Damage", "Wind Damage", "Tornado"]
    tags = ["Earthquake", "Hurricane", "Flooding", "Water", "Fire", "Buildings", "Housing", "Telecommunications", 
    "Ports", "Power Generation"]

    for infra in infrastructures:
        infras = infrastructure(infrastructureType=infra)
        infras.save()
    for damageDoc in damages:
        dama = damage(damageType=damageDoc)
        dama.save()
    for tagslist in tags:
        tagDoc = tag(tagItem=tagslist)
        tagDoc.save()

Categories()

def Locations():
    """
        Fills the db with predefined Locations of all the municipalities of Puerto Rico with their coordinates
    """  
    with open('cityPR.json', encoding='utf-8') as f:
        data = json.loads(f.read())
        for cities in data['city_PR']:
            cityDoc = city_pr(city= cities['city'], latitude=cities['latitude'], longitude=cities['longitude'])
            cityDoc.save()

Locations()

def Collabs():
    """
        Fills the db with 5 Collaborators mock-data
    """
    collab1 = collaborator(first_name="Jainel", last_name="Torres Santos", email="jainel.torres@upr.edu", approved=True)
    collab1.save()
    collab2 = collaborator(first_name="Roberto", last_name="Guzman", email="roberto.guzman3@upr.edu", approved=True)
    collab2.save()
    collab3 = collaborator(first_name="Alberto", last_name="Canela", email="alberto.canela@upr.edu",approved=True)
    collab3.save()
    collab4 = collaborator(first_name="Alejandro", last_name="Vasquez", email="alejandro.vasquez@upr.edu",approved=True)
    collab4.save()
    collab5 = collaborator(first_name="Yomar", last_name="Ruiz", email="yomar.ruiz@upr.edu",approved=True)
    collab5.save()
    collab6 = collaborator(first_name="VICTORIA M", last_name="TORRES SANTOS", email="victoria.black@upr.edu",approved=True)
    collab6.save()

Collabs()

def Admins():
    """
        Fills the db with 5 Admin mock-data
    """
    admin1 = admin(username="yomar.ruiz", password='$2y$12$F8JpE/vVYHW5CGHerUfy3er15s7ApqT7ziRkc9lTGpnVuw9X8jZ4W') #Password0
    admin1.save()
    admin2 = admin(username="roberto.guzman", password= '$2y$12$XZe.igfbsswNfEIrjcIXvOizWs9Xl4mfgw9Zj04bPajmdrr2Wcj1C') #Password1
    admin2.save()
    admin3 = admin(username="alejandro.vasquez", password='$2y$12$XZe.igfbsswNfEIrjcIXvOizWs9Xl4mfgw9Zj04bPajmdrr2Wcj1C') #Password1
    admin3.save()
    admin4 = admin(username="jainel.torres", password='$2y$12$XZe.igfbsswNfEIrjcIXvOizWs9Xl4mfgw9Zj04bPajmdrr2Wcj1C') #Password1
    admin4.save()
    admin5 = admin(username="alberto.canela", password='$2y$12$XZe.igfbsswNfEIrjcIXvOizWs9Xl4mfgw9Zj04bPajmdrr2Wcj1C') #Password1
    admin5.save()
    

Admins()

def Documents():
    """
        Fills the db with 2 Documents mock-data
    """                                                                                                                                                                                                                                             
    get_collab1 = collaborator.objects.get(first_name= "Jainel")
    authorDoc1 = author(author_FN = get_collab1.first_name, author_LN = "Torres-Santos", 
    author_email = get_collab1.email, author_faculty="ICOM")
    actorDoc1 = actor(actor_FN = "Victoria", actor_LN = "Black", role = "Mayor")
    timelineDoc1 = timeline(event = "The rain has started", 
    eventStartDate = "2017-09-17", eventEndDate = "2017-09-19")
    timelineDoc2 = timeline(event = "The case study started", 
    eventStartDate = "2018-07-17", eventEndDate = "2018-07-19")
    timelineDoc3 = timeline(event = "The rain has intensified", 
    eventStartDate = "2019-03-17", eventEndDate = "2019-05-10")
    sectionDoc1 = section(secTitle = "Introduction", content = "It was raining a lot")
    citypr = city_pr.objects.get(city = 'Coamo, PR')
    loc = location(address= citypr.city, latitude= citypr.latitude, longitude=citypr.longitude)
    doc1 = document_case(creatoriD = get_collab1, title = ("The Great Rainw"), location=[loc], 
    description = "It was a cold and stormy night...", published= True,
    incidentDate = "2017-09-17", 
    creationDate= "2018-03-20",
    lastModificationDate= "2019-04-08",
    tagsDoc=['Hurricane', 'Rain'], 
    infrasDocList= ["Building", "Water Supply"],
    damageDocList= ['Flooding'],
    author = [authorDoc1], actor = [actorDoc1],section = [sectionDoc1],
    timeline = [timelineDoc1,timelineDoc2,timelineDoc3], language="English")
    doc1.save()
    
    get_collab2 = collaborator.objects.get(first_name= "Roberto")
    authorDoc2 = author(author_FN = get_collab2.first_name, author_LN = get_collab2.last_name, 
    author_email = get_collab2.email, author_faculty= "ICOM")
    actorDoc2 = actor(actor_FN = "Nelson", actor_LN = "Santos", role = "Ingeniero")
    timelineDoc2 = timeline(event = "El temblor ha comenzado", 
    eventStartDate = "2019-02-09", eventEndDate = "2019-03-10")
    sectionDoc2 = section(secTitle = "Cuerpo", content = "Estaba temblando mucho el suelo")
    citypr2 = city_pr.objects.get(city = 'Aguas Buenas, PR')
    loc2 = location(address= citypr2.city, latitude= citypr2.latitude, longitude=citypr2.longitude)
    doc2 = document_case(creatoriD = get_collab2, title = ("El gran Terremoto"), location=[loc2], 
    description = "Era un lindo dia soleado...", published= False,
    incidentDate = "2019-02-09", 
    creationDate= "2020-02-20",
    lastModificationDate= "2020-02-20",
    tagsDoc=['Earthquake', 'Power Outage'], 
    infrasDocList= ["Building", "Housing"],
    damageDocList= ['Earthquake'],
    author = [authorDoc2], actor = [actorDoc2],section = [sectionDoc2],timeline = [timelineDoc2], language="Spanish")
    doc2.save()

Documents()
