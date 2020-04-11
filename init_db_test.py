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
admin1 = Admin(username="jaits13", password="")
admin2
admin3


