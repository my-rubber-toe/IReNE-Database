import googlemaps 
import json

"""
    This code is for using geocoding from google maps api and save a list of predefined adress,
    with their coordinates in a json file for later used in predefined_data.py file
"""
#You must provide a valid api key from google cloud platform
gmaps = googlemaps.Client(key='Your-API-KEY')

# Geocoding an address
cities = ['Adjuntas, PR', 'Aguada, PR', 'Aguadilla, PR', 'Aguas Buenas, PR', 'Aibonito, PR',
'Añasco, PR', 'Arecibo, PR', 'Arroyo, PR', 'Barceloneta, PR', 'Barranquitas, PR',
'Bayamón, PR', 'Cabo Rojo, PR', 'Caguas, PR', 'Camuy, PR', 'Canóvanas, PR',
'Carolina, PR', 'Cataño, PR', 'Cayey, PR', 'Ceiba, PR', 'Ciales, PR',
'Cidra, PR', 'Coamo, PR', 'Comerio, PR', 'Corozal, PR', 'Culebra, PR', 
'Dorado, PR', 'Fajardo, PR', 'Florida, PR', 'Guánica, PR', 'Guayama, PR',
'Guayanilla, PR', 'Guaynabo, PR', 'Gurabo, PR', 'Hatillo, PR', 'Hormigueros, PR',
'Humacao, PR', 'Isabela, PR', 'Jayuya, PR', 'Juana Díaz, PR', 'Juncos, PR',
'Lajas, PR', 'Lares, PR', 'Las Marías, PR', 'Las Piedras, PR', 'Loíza, PR',
'Luquillo, PR', 'Manatí, PR', 'Maricao, PR', 'Maunabo, PR', 'Mayagüez, PR',
'Moca, PR', 'Morovis, PR', 'Naguabo, PR', 'Naranjito, PR', 'Orocovis, PR',
'Patillas, PR', 'Peñuelas, PR', 'Ponce, PR', 'Quebradillas, PR', 'Rincón, PR',
'Río Grande, PR', 'Sabana Grande, PR', 'Salinas, PR', 'San Germán, PR', 'San Juan, PR',
'San Lorenzo, PR', 'San Sebastián, PR', 'Santa Isabel, PR', 'Toa Alta, PR',
'Toa Baja, PR', 'Trujillo Alto, PR', 'Utuado, PR', 'Vega Alta, PR', 'Vega Baja, PR',
'Vieques, PR', 'Villalba, PR', 'Yabucoa, PR', 'Yauco, PR']

json_out = []
for city in cities:
    geocode_result = gmaps.geocode(city)
    json_city =  { "city": city, "latitude":geocode_result[0]['geometry']['location']['lat'], 
    "longitude": geocode_result[0]['geometry']['location']['lng'] }
    json_out.append(json_city)

with open('cityPR.json', 'w') as outfile:
    json.dump({"city_PR" : json_out}, outfile)