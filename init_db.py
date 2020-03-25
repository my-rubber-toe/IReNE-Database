from pymongo import *

myclient = pymongo.MongoClient("mongodb://localhost:20717")
irene = myclient["IReNEdb"]

collab = irene["Collaborators"]
admin = irene["Admin"]
session = irene["Session"]
doc = irene["DocumentCase"]
taglist = irene["Tag"]
infra = irene["Infrastructure"]
damage = irene["Damage"]

#test if you are connected
#print ("server_info():", myclient.server_info())

# db = myclient["IReNE"]
# try: db.command("serverStatus")
# except Exception as e: print(e)
# else: print("You are connected!")
# myclient.close()