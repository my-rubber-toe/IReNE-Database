from mongoengine import *
from schema_DB import *

# connect('IReNEdb', host='mongomock://localhost:27017')

def test_insert_Collab():
    collab = Collaborator( documentsID = [1,2,3], first_name = "Jainel", 
    last_name = "Torres", email = "jainel.torres@upr.edu", faculty = "ICOM")
    collab.save()

    collab_test = Collaborator.objects.first()
    #first argument is the position where the second argument will insert
    collab_test.documentsID.insert(0,4)
    collab_test.save()
    assert collab_test.first_name ==  "Jainel"
    assert collab_test.last_name ==  "Torres"
    assert collab_test.email ==  "jainel.torres@upr.edu"
    assert collab_test.faculty ==  "ICOM"
    assert collab_test.documentsID == [1,2,3,4]

    # if (collab_test.first_name ==  "Jainel" and collab_test.last_name ==  "Torres" and
    #  collab_test.email ==  "jainel.torres@upr.edu" and collab_test.faculty ==  "ICOM"
    #  and collab_test.documentsID == [1,2,3,4]):
    #     print("it works")

def test_insert_Admin():
    admin1 = Admin(username = "jaits", password = "loco")
    admin1.save()

    test_admin = Admin.objects.first()
    assert test_admin.username == "jaits"
    assert test_admin.password == "loco"

def test_insert_TagList():
    taglist = TagList(tagItem = "Flood")
    taglist.save()

    taglist_test = TagList.objects.first()
    assert taglist_test.tagItem == "Flood"

def test_insert_Infrastructure():
    infras = Infrastructure(infrastructureType = "Building")
    infras.save()

    infras_test = Infrastructure.objects.first()
    assert infras_test.infrastructureType == "Building"    

def test_insert_Damage():
    damage = Damage(damageType = "Flooding")
    damage.save()

    damage_test = Damage.objects.first()
    assert damage_test.damageType == "Flooding" 

#-------------------------Tests for Updating------------------------------------
def test_update_Collab():
    collab = Collaborator( documentsID = [1,2,3], first_name = "Jainel", 
    last_name = "Torres", email = "jainel.torres@upr.edu", faculty = "ICOM")
    collab.save()

    collab_test = Collaborator.objects.first()
    Collaborator.objects(first_name = "Jainel",last_name = "Torres").update_one(set__faculty = "INEL")
    collab_test.reload()
    assert collab_test.faculty ==  "INEL"

def test_update_Admin():
    admin1 = Admin(username = "jaits", password = "LOZ")
    admin1.save()

    test_admin = Admin.objects.first()
    Admin.objects(username = "jaits").update_one(set__password = "mario")
    test_admin.reload()
    assert test_admin.password == "mario"


#-----------------------------------Methods for deletion--------------------------

#example of get 
# print(Colaborator.objects.get(faculty = "ICOM")

#example for append to a list
# blog_post = BlogPost.objects.get(id=post.id)
# blog_post.tags.insert(0,'nosql')
# blog_post.save()