from mongoengine import *
from schema_DB import *
import json

"""
    This code is to populate the predefined data that will have the database, it should 
    run only once.
"""
infrastructure = ["Streets or Highway", "Bridges", "Airports", "Water Supply", "Waste Water Management",
"Power Generation & Transmission", "Telecommunications" , "Housing", "Building", "Ports"
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

with open('cityPR.json') as f:
    data = json.loads(f.read())
    for cities in data['city_PR']:
        city = CityPR(city= cities['city'], latitude=cities['latitude'], longitude=cities['longitude'])
        city.save()
        


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