from mongoengine import *
from schema_DB import *
from googlemaps import *
 

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

# for infra in infrastructure:
#     infras = Infrastructure(infrastructureType=infra)
#     infras.save()
# for damages in damage:
#     dama = Damage(damageType=damages)
#     dama.save()
# for tagslist in tags:
#     tag = Tag(tagItem=tagslist)
#     tag.save()


gmaps = Client(key='AIzaSyA5sLr_OUnwbEQYISlZlgJFxHa4-8Nv-Gw')

# Geocoding an address
geocode_result = gmaps.geocode('Coamo, PR')
print(geocode_result)
cities = []