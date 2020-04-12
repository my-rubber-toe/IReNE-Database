from mongoengine import *
from schema_DB import *

#Fills the db with Collaborators mock-data
collab1 = Collaborator(first_name="Jainel", last_name="Torres", email="jainel.torres@upr.edu")
collab1.save()
collab2 = Collaborator(first_name="Roberto", last_name="Guzman", email="roberto.guzman3@upr.edu")
collab2.save()
collab3 = Collaborator(first_name="Alberto", last_name="Canela", email="alberto.canela@upr.edu")
collab3.save()
collab4 = Collaborator(first_name="Alejandro", last_name="Vasquez", email="alejandro.vasquez@upr.edu")
collab4.save()
collab5 = Collaborator(first_name="Yomar", last_name="Ruiz", email="yomar.ruiz@upr.edu")
collab5.save()

#Fills the db with Admin mock-data
admin1 = Admin(username="jaits13", password="icom5047@jaits13")
admin1.save()
admin2 = Admin(username="robg3", password= "icom5047@robg3")
admin2.save()
admin3 = Admin(username="aleva", password="icom5047@aleva")
admin3.save()

#Fills the db with Tag mock-data
tags = ['Hurricane', 'Rain', 'Earthquake', 'Fire', 'Burning', 'Flood', 'Power Outage']
for tag in tags:
    x = Tag(tagItem= tag)
    x.save()

#Fills the db with Damage mock-data
damage = ['Flooding', 'Earthquake', 'Fire', 'Tsunamis', 'Hurricane']
for dam in damage:
    x = Damage(damageType= dam)
    x.save()

#Fills the db with Infrastructure mock-data
infrastructure = ['Transportation', 'Energy', 'Water', 'Security', 'Ports', 'Structure', 'Construction']
for infras in infrastructure:
    x = Infrastructure(infrastructureType= infras)
    x.save()

#Fills the db with documentsx                                                                                                                                                                                                                                               mock-data
get_collab1 = Collaborator.objects.get(first_name= "Jainel")
authorDoc1 = Author(author_FN = get_collab1.first_name, author_LN = get_collab1.last_name, 
author_email = get_collab1.email, author_faculty="ICOM")
actorDoc1 = Actor(actor_FN = "Victoria", actor_LN = "Black", role = "Mayor")
timelineDoc1 = Timeline(event = "The rain has started", 
eventStartDate = "2017-09-17", eventEndDate = "2017-09-19")
sectionDoc1 = Section(secTitle = "Introduction", content = "It was raining a lot")
doc1 = DocumentCase(creatoriD = str(get_collab1.id), title = ("The Great Rain"), location=["Coamo, PR"], 
description = "It was a cold and stormy night...", published= True,
incidentDate = "2017-09-17", 
creationDate= "2018-03-20",
lastModificationDate= "2019-04-08",
tagsDoc=['Hurricane', 'Rain'], 
infrasDocList= ["Structure", "Water"],
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
doc2 = DocumentCase(creatoriD = str(get_collab2.id), title = ("El gran Terremoto"), location=["San Juan, PR"], 
description = "Era un lindo dia soleado...", published= False,
incidentDate = "2019-02-09", 
creationDate= "2020-02-20",
lastModificationDate= "2020-02-20",
tagsDoc=['Earthquake', 'Power Outage'], 
infrasDocList= ["Structure", "Energy"],
damageDocList= ['Earthquake'],
author = [authorDoc2], actor = [actorDoc2],section = [sectionDoc2],timeline = [timelineDoc2], language="Spanish")
doc2.save()
