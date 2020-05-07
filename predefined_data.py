from mongoengine import *
from schema_DB import *
import json

"""
    This code is to populate the predefined data that will have the database, it should 
    run only once.
"""
def Categories():
    """
        Fills the db with predefined categories & tags
    """  
    infrastructure = ["Streets or Highway", "Bridges", "Airports", "Water Supply", "Waste Water Management",
    "Power Generation & Transmission", "Telecommunications" , "Housing", "Building", "Ports",
    "Public Transportation"]
    damage = [ "Earthquake", "Hurricane", "Tsunami", "Flooding", "Landslide", "Fire/smoke", 
    "Extreme Precipitation", "Water Damage", "Wind Damage", "Tornado"]
    tags = infrastructure + damage

    for infra in infrastructure:
        infras = Infrastructure(infrastructureType=infra)
        infras.save()
    for damages in damage:
        dama = Damage(damageType=damages)
        dama.save()
    for tagslist in tags:
        tag = Tag(tagItem=tagslist)
        tag.save()

Categories()

def Locations():
    """
        Fills the db with predefined  addresses with their coordinates
    """  
    with open('cityPR.json') as f:
        data = json.loads(f.read())
        for cities in data['city_PR']:
            city = CityPR(city= cities['city'], latitude=cities['latitude'], longitude=cities['longitude'])
            city.save()

Locations()

def Collabs():
    """
        Fills the db with 5 Collaborators mock-data
    """
    collab1 = Collaborator(first_name="Jainel", last_name="Torres", email="jainel.torres@upr.edu", approved=True)
    collab1.save()
    collab2 = Collaborator(first_name="Roberto", last_name="Guzman", email="roberto.guzman3@upr.edu", approved=True)
    collab2.save()
    collab3 = Collaborator(first_name="Alberto", last_name="Canela", email="alberto.canela@upr.edu",approved=True)
    collab3.save()
    collab4 = Collaborator(first_name="Alejandro", last_name="Vasquez", email="alejandro.vasquez@upr.edu",approved=True)
    collab4.save()
    collab5 = Collaborator(first_name="Yomar", last_name="Ruiz", email="yomar.ruiz@upr.edu",approved=True)
    collab5.save()

Collabs()

def Admins():
    """
        Fills the db with 3 Admin mock-data
    """
    admin1 = Admin(username="jainel.torres", password="Password1")
    admin1.save()
    admin2 = Admin(username="alberto.canela", password= "Password1")
    admin2.save()
    admin3 = Admin(username="alejandro.vasquez", password="Password1")
    admin3.save()
    admin4 = Admin(username="yomar.ruiz", password= "Password0")
    admin4.save()
    admin5 = Admin(username="roberto.guzman", password="Password1")
    admin5.save()
    

Admins()

def Documents():
    """
        Fills the db with Documents mock-data
    """                                                                                                                                                                                                                                             
    get_collab1 = Collaborator.objects.get(first_name= "Jainel")
    authorDoc1 = Author(author_FN = get_collab1.first_name, author_LN = get_collab1.last_name, 
    author_email = get_collab1.email, author_faculty="ICOM")
    actorDoc1 = Actor(actor_FN = "Victoria", actor_LN = "Black", role = "Mayor")
    timelineDoc1 = Timeline(event = "The rain has started", 
    eventStartDate = "2017-09-17", eventEndDate = "2017-09-19")
    sectionDoc1 = Section(secTitle = "Introduction", content = "It was raining a lot")
    citypr = CityPR.objects.get(city = 'Coamo, PR')
    loc = Location(address= citypr.city, latitude= citypr.latitude, longitude=citypr.longitude)
    doc1 = DocumentCase(creatoriD = get_collab1, title = ("The Great Rain"), location=[loc], 
    description = "It was a cold and stormy night...", published= True,
    incidentDate = "2017-09-17", 
    creationDate= "2018-03-20",
    lastModificationDate= "2019-04-08",
    tagsDoc=['Hurricane', 'Rain'], 
    infrasDocList= ["Building", "Water Supply"],
    damageDocList= ['Flooding'],
    author = [authorDoc1], actor = [actorDoc1],section = [sectionDoc1],timeline = [timelineDoc1], language="English")
    doc1.save()

    get_collab2 = Collaborator.objects.get(first_name= "Roberto")
    authorDoc2 = Author(author_FN = get_collab2.first_name, author_LN = get_collab2.last_name, 
    author_email = get_collab2.email, author_faculty= "ICOM")
    actorDoc2 = Actor(actor_FN = "Nelson", actor_LN = "Santos", role = "Ingeniero")
    timelineDoc2 = Timeline(event = "El temblor ha comenzado", 
    eventStartDate = "2019-02-09", eventEndDate = "2019-03-10")
    sectionDoc2 = Section(secTitle = "Cuerpo", content = "Estaba temblando mucho el suelo")
    citypr2 = CityPR.objects.get(city = 'Aguas Buenas, PR')
    loc2 = Location(address= citypr2.city, latitude= citypr2.latitude, longitude=citypr2.longitude)
    doc2 = DocumentCase(creatoriD = get_collab2, title = ("El gran Terremoto"), location=[loc2], 
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

        


#code for generating json file with list of cities with coors
# import googlemaps 
# import json
# gmaps = googlemaps.Client(key='AIzaSyAZEkjgNHbvCFQ4ohopyKSg3-zbfHx4pSk')

#         # Geocoding an address
#         cities = ['Adjuntas, PR', 'Aguada, PR', 'Aguadilla, PR', 'Aguas Buenas, PR', 'Aibonito, PR',
#         'Añasco, PR', 'Arecibo, PR', 'Arroyo, PR', 'Barceloneta, PR', 'Barranquitas, PR',
#         'Bayamón, PR', 'Cabo Rojo, PR', 'Caguas, PR', 'Camuy, PR', 'Canóvanas, PR',
#         'Carolina, PR', 'Cataño, PR', 'Cayey, PR', 'Ceiba, PR', 'Ciales, PR',
#         'Cidra, PR', 'Coamo, PR', 'Comerio, PR', 'Corozal, PR', 'Culebra, PR', 
#         'Dorado, PR', 'Fajardo, PR', 'Florida, PR', 'Guánica, PR', 'Guayama, PR',
#         'Guayanilla, PR', 'Guaynabo, PR', 'Gurabo, PR', 'Hatillo, PR', 'Hormigueros, PR',
#         'Humacao, PR', 'Isabela, PR', 'Jayuya, PR', 'Juana Díaz, PR', 'Juncos, PR',
#         'Lajas, PR', 'Lares, PR', 'Las Marías, PR', 'Las Piedras, PR', 'Loíza, PR',
#         'Luquillo, PR', 'Manatí, PR', 'Maricao, PR', 'Maunabo, PR', 'Mayagüez, PR',
#         'Moca, PR', 'Morovis, PR', 'Naguabo, PR', 'Naranjito, PR', 'Orocovis, PR',
#         'Patillas, PR', 'Peñuelas, PR', 'Ponce, PR', 'Quebradillas, PR', 'Rincón, PR',
#         'Río Grande, PR', 'Sabana Grande, PR', 'Salinas, PR', 'San Germán, PR', 'San Juan, PR',
#         'San Lorenzo, PR', 'San Sebastián, PR', 'Santa Isabel, PR', 'Toa Alta, PR',
#         'Toa Baja, PR', 'Trujillo Alto, PR', 'Utuado, PR', 'Vega Alta, PR', 'Vega Baja, PR',
#         'Vieques, PR', 'Villalba, PR', 'Yabucoa, PR', 'Yauco, PR']

#         json_out = []
#         for city in cities:
#             geocode_result = gmaps.geocode(city)
#             json_city =  { "city": city, "latitude":geocode_result[0]['geometry']['location']['lat'], 
#             "longitude": geocode_result[0]['geometry']['location']['lng'] }
#             json_out.append(json_city)

#         with open('cityPR.json', 'w') as outfile:
#             json.dump({"city_PR" : json_out}, outfile)