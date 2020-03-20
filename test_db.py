from mongoengine import *
from schema_DB import *
import datetime
#By running these functions
# connect('IReNEdb', host='mongomock://localhost:27017')

def test_insert_Collab():
    collab = Collaborator( first_name = "Jainel", 
    last_name = "Torres", email = "jainel.torres@upr.edu", faculty = "ICOM")
    collab.save()

    collab_test = Collaborator.objects.first()
    #first argument is the position where the second argument will insert
    # collab_test.documentsID.insert(0,4)
    collab_test.save()
    print(collab.id)
    assert collab_test.first_name ==  "Jainel"
    assert collab_test.last_name ==  "Torres"
    assert collab_test.email ==  "jainel.torres@upr.edu"
    assert collab_test.faculty ==  "ICOM"
    # assert collab_test.documentsID == [1,2,3,4]

# cola = Collaborator.objects.filter(first_name = "Jainel", last_name = "Torres")
# print(cola)

def test_insert_Admin():
    admin1 = Admin(username = "jaits", password = "loco")
    admin1.save()

    test_admin = Admin.objects.first()
    assert test_admin.username == "jaits"
    assert test_admin.password == "loco"

def test_insert_Tag():
    tag = Tag(tagItem = "Flood")
    tag.save()

    tag_test = Tag.objects.first()
    assert tag_test.tagItem == "Flood"

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

def test_insert_doc():
    #process of inserting a document
    authorDoc = Author(author_FN = "Jai", author_LN = "TS", author_email = "j@upr.edu", 
    author_faculty = "ICOM")
    actorDoc = Actor(actor_FN = "vic", actor_LN = "LOL", role = "mayor")
    timelineDoc = Timeline(event = "Maria Passed PR", eventDate = datetime.datetime(2017, 9, 16))
    sectionDoc = Section(secTitle = "Introduction", content = "It was bad...")
    doc1 = DocumentCase(title = "The great Flooding", description = "It was horrible",
    incidentDate = datetime.datetime(2017, 9, 16), creationDate = datetime.datetime(2019, 2, 17),
    tagsDoc = ["Flood", "Hurricane"], infrasDocList = ["Building"], damageDocList = ["Flooding"],
    location = ["Coamo"], author = [authorDoc], actor = [actorDoc], section = [sectionDoc],
    timeline = [timelineDoc])
    doc1.save()
    #process of testing the insert
    doc_test = DocumentCase.objects.first()
    # doc_embedded_test = DocumentCase.
    print(doc_test.creationDate)
    print(doc_test.author[0].author_FN)
    assert doc_test.title == "The great Flooding"
    assert doc_test.description == "It was horrible"
    assert doc_test.incidentDate == datetime.datetime(2017, 9, 16)
    assert doc_test.creationDate == datetime.datetime(2019, 2, 17)
    assert doc_test.tagsDoc == ["Flood", "Hurricane"]
    assert doc_test.infrasDocList == ["Building"]
    assert doc_test.damageDocList == ["Flooding"]
    assert doc_test.location == ["Coamo"]
    assert doc_test.author[0].author_FN == "Jai"
    assert doc_test.author[0].author_LN == "TS"
    assert doc_test.author[0].author_email == "j@upr.edu"
    assert doc_test.author[0].author_faculty == "ICOM"
    assert doc_test.actor[0].actor_FN == "vic"
    assert doc_test.actor[0].actor_LN == "LOL"
    assert doc_test.actor[0].role == "mayor"
    assert doc_test.timeline[0].event == "Maria Passed PR"
    assert doc_test.timeline[0].eventDate == datetime.datetime(2017, 9, 16)
    assert doc_test.section[0].secTitle == "Introduction"
    assert doc_test.section[0].content == "It was bad..."
   
#-------------------------Tests for Updating------------------------------------
def test_update_Collab():
    collab = Collaborator(first_name = "Jainel", last_name = "Torres",
    email = "jainel.torres@upr.edu", faculty = "ICOM")
    collab.save()

    collab_test = Collaborator.objects.first()
    Collaborator.objects(first_name = "Jainel",last_name = "Torres").update_one(set__faculty = "INEL", set__email = "j@upr.edu")
    collab_test.reload()
    assert collab_test.faculty ==  "INEL"
    assert collab_test.email == "j@upr.edu"


def test_update_Admin():
    admin1 = Admin(username = "jaits", password = "LOZ")
    admin1.save()

    test_admin = Admin.objects.first()
    Admin.objects(username = "jaits").update_one(set__password = "mario")
    test_admin.reload()
    assert test_admin.password == "mario"

def test_update_doc():
    #process of inserting a document
    authorDoc = Author(author_FN = "Jai", author_LN = "TS", author_email = "j@upr.edu", 
    author_faculty = "ICOM")
    actorDoc = Actor(actor_FN = "vic", actor_LN = "LOL", role = "mayor")
    timelineDoc = Timeline(event = "Maria Passed PR", eventDate = datetime.datetime(2017, 9, 16))
    sectionDoc = Section(secTitle = "Introduction", content = "It was bad...")
    doc1 = DocumentCase(idCollab = "S", title = "The great Flooding", description = "It was horrible",
    incidentDate = datetime.datetime(2017, 9, 16), creationDate = datetime.datetime(2019, 2, 17),
    tagsDoc = ["Flood", "Hurricane"], infrasDocList = ["Building"], damageDocList = ["Flooding"],
    location = ["Coamo"], author = [authorDoc], actor = [actorDoc], section = [sectionDoc],
    timeline = [timelineDoc])
    doc1.save()
    #process of testing update
    doc_test = DocumentCase.objects.first()
    DocumentCase.objects(title = "The great Flooding").update_one(set__description = "whoa")
    DocumentCase.objects(title = "The great Flooding").update_one(set__tagsDoc = ["Flood", "Hurricane","severe"])
    DocumentCase.objects(title = "The great Flooding", author__author_LN = "TS").update_one(set__author__S__author_FN = "joy")
    DocumentCase.objects(title = "The great Flooding").update_one(set__creationDate = datetime.datetime(2018, 3, 10))
    doc_test.reload()
    assert doc_test.description == "whoa"
    assert doc_test.creationDate == datetime.datetime(2018, 3, 10)
    assert doc_test.tagsDoc == ["Flood", "Hurricane","severe"]
    assert doc_test.author[0].author_FN == "joy"
    
#-----------------------------------Methods for deletion--------------------------

def test_delete_tag():
    tag = Tag(tagItem = "Flood")
    tag.save()
    print(Tag.objects())
    #eliminate more than one doc
    Tag.objects(tagItem = "Flood").delete()
    print(Tag.objects())

def test_delete_doc():
    authorDoc = Author(author_FN = "Jai", author_LN = "TS", author_email = "j@upr.edu", 
    author_faculty = "ICOM")
    actorDoc = Actor(actor_FN = "vic", actor_LN = "LOL", role = "mayor")
    timelineDoc = Timeline(event = "Maria Passed PR", eventDate = datetime.datetime(2017, 9, 16))
    sectionDoc = Section(secTitle = "Introduction", content = "It was bad...")
    doc1 = DocumentCase(idCollab = "S", title = "The great Flooding", description = "It was horrible",
    incidentDate = datetime.datetime(2017, 9, 16), creationDate = datetime.datetime(2019, 2, 17),
    tagsDoc = ["Flood", "Hurricane"], infrasDocList = ["Building"], damageDocList = ["Flooding"],
    location = ["Coamo"], author = [authorDoc], actor = [actorDoc], section = [sectionDoc],
    timeline = [timelineDoc])
    doc1.save()
    iddoc = doc1.id
    #eliminate just one
    doc_del = DocumentCase.objects.get(id = iddoc)
    doc_del.delete()
 
#---------------------------------Methods for Read --------------------------

def test_read_tag():
    tag = Tag(tagItem = "Flood")
    tag.save()
    
    tagread = Tag.objects.get(tagItem = "Flood")
    print(tagread.tagItem)
    assert tagread.tagItem == "Flood"


#example of get 
# print(Colaborator.objects.get(faculty = "ICOM")

#example for append to a list
# blog_post = BlogPost.objects.get(id=post.id)
# blog_post.tags.insert(0,'nosql')
# blog_post.save()