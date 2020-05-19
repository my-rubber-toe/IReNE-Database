import sys
sys.path.append("..")
from mongoengine import *
from schema_DB import *


#-------------------------Tests for Create------------------------------------
def test_create_Collab(fn,ln,email):
    """
        Creates a new Collaborator
    """
    strip_fn = fn.replace(" ", "")
    strip_ln = ln.replace(" ", "")
    # if (email == (strip_fn.lower() + "." + strip_ln.lower() + '@upr.edu')):
    collab = collaborator( first_name = fn, 
    last_name = ln, email = email)
    collab.save()

    collab_test = collaborator.objects.get(email = email)
    assert collab_test.first_name ==  fn
    assert collab_test.last_name ==  ln
    assert collab_test.email ==  email
    print("New Collab: \n\tFN: ", collab_test.first_name, "\n\tLN: ", collab_test.last_name, "\n\temail: ", collab_test.email)
    # else:
        # print('email must be a @upr.edu domain & must match with fn & ln')

def test_create_Admin(user_username, user_password):
    """
        Creates a new Admin
    """
    admin = admin(username = user_username, password = user_password)
    admin.save()
    test_admin = admin.objects.get(username = user_username)
    assert test_admin.username == user_username
    assert test_admin.password == user_password
    print("New Admin: \n\tUsername: ", test_admin.username, "\n\tPassword: ", test_admin.password)

def test_create_Tag(new_tag):
    """
        Creates a new Tag
    """
    new_tagdoc = tag(tagItem = new_tag)
    new_tagdoc.save()
    
    tag_test = tag.objects.get(tagItem = new_tag)
    assert tag_test.tagItem == new_tag
    print(tag_test.tagItem)

def test_create_Infrastructure(new_infras):
    """
        Creates a new Infrastructure Type
    """
    infras = infrastructure(infrastructureType = new_infras)
    infras.save()

    infras_test = infrastructure.objects.get(infrastructureType = new_infras)
    assert infras_test.infrastructureType == new_infras
    print(infras_test.infrastructureType)    

def test_create_Damage(new_damage):
    """
        Creates a new Damage Type
    """
    damage = damage(damageType = new_damage)
    damage.save()

    damage_test = damage.objects.get(damageType = new_damage)
    assert damage_test.damageType == new_damage
    print(damage_test.damageType)

def test_create_doc (**docatr):
    """
        Creates a new Document
    """
    authorDoc = []
    for author_doc in docatr["author"]:
        auth = author(author_FN = author_doc[0], author_LN = author_doc[1], author_email = author_doc[2], 
        author_faculty = author_doc[3])
        authorDoc.append(auth)
    actorDoc = []
    for actor_doc in docatr["actor"]:
        act = actor(actor_FN = actor_doc[0], actor_LN = actor_doc[1], role = actor_doc[2])
        actorDoc.append(act)
    timelineDoc = []
    for tl in docatr["timeline"]:
        timel = timeline(event = tl[0], eventStartDate = tl[1], eventEndDate= tl[2])
        timelineDoc.append(timel)
    sectionDoc = []
    for sec in docatr["section"]:
        secdoc = section(secTitle = sec[0], content = sec[1])
        sectionDoc.append(secdoc)
    doc1 = document_case(creatoriD = docatr["creatoriD"],title = docatr["title"], language=docatr["language"], description = docatr["description"],
    incidentDate = docatr["incidentDate"], creationDate = docatr["creationDate"], lastModificationDate = docatr["lastModificationDate"],
    tagsDoc = docatr["tagsDoc"], infrasDocList = docatr["infrasDocList"], damageDocList = docatr["damageDocList"],
    location = docatr["location"], author = authorDoc, actor = actorDoc, 
    section = sectionDoc, timeline = timelineDoc)
    for new_tag in docatr["tagsDoc"]:
        if not tag.objects(tagItem=new_tag):
            newTag = tag(tagItem=new_tag)
            newTag.save()
    doc1.save()
    #process of testing the insert
    doc_test = document_case.objects.get(title = docatr["title"])
    assert doc_test.creatoriD == docatr["creatoriD"]
    assert doc_test.title == docatr["title"]
    assert doc_test.description == docatr["description"]
    assert doc_test.incidentDate == docatr["incidentDate"]
    assert doc_test.creationDate == docatr["creationDate"]
    assert doc_test.lastModificationDate == docatr["lastModificationDate"]
    assert doc_test.tagsDoc == docatr["tagsDoc"]
    assert doc_test.infrasDocList == docatr["infrasDocList"]
    assert doc_test.damageDocList == docatr["damageDocList"]
    assert doc_test.location == docatr["location"]
    assert doc_test.author[0].author_FN == authorDoc[0].author_FN
    assert doc_test.author[0].author_LN == authorDoc[0].author_LN
    assert doc_test.author[0].author_email == authorDoc[0].author_email
    assert doc_test.author[0].author_faculty == authorDoc[0].author_faculty 
    assert doc_test.actor[0].actor_FN == actorDoc[0].actor_FN
    assert doc_test.actor[0].actor_LN == actorDoc[0].actor_LN 
    assert doc_test.actor[0].role == actorDoc[0].role
    assert doc_test.timeline[0].event == timelineDoc[0].event
    assert doc_test.timeline[0].eventStartDate == timelineDoc[0].eventStartDate 
    assert doc_test.timeline[0].eventEndDate == timelineDoc[0].eventEndDate
    assert doc_test.section[0].secTitle == sectionDoc[0].secTitle
    assert doc_test.section[0].content == sectionDoc[0].content
    assert doc_test.language == "English"
    print("creatorID: " + doc_test.creatoriD)
    print("title: " + doc_test.title)
    print("description: " + doc_test.description)
    print("incidentDate: " + doc_test.incidentDate)
    print("creationDate: " + doc_test.creationDate)
    print("lastModificationDate: " + doc_test.lastModificationDate)
    print("tagsDoc: ", doc_test.tagsDoc)
    print("infrasDocList: ", doc_test.infrasDocList)
    print("damageDocList: " , doc_test.damageDocList)
    print("location: " , doc_test.location)
    print("author: \n\tname" , doc_test.author[0].author_FN, doc_test.author[0].author_LN, 
    "\n\temail",doc_test.author[0].author_email, "\n\tfaculty",doc_test.author[0].author_faculty)
    print("actor: \n\tname:" , doc_test.actor[0].actor_FN, doc_test.actor[0].actor_LN, 
    "\n\trole:",doc_test.actor[0].role)
    print("timeline: " , doc_test.timeline[0].event,doc_test.timeline[0].eventStartDate, doc_test.timeline[0].eventEndDate )
    print("section: \n\tsecTitle:" , doc_test.section[0].secTitle, "\n\tcontent:",  doc_test.section[0].content )

#-------------------------Tests for Updating------------------------------------

def test_update_Collab_FN(email_test, new_fn):
    """
        updates FN of collab
    """
    collab_test = collaborator.objects.get(email= email_test)
    print("old fn: ", collab_test.first_name)
    collaborator.objects(email=email_test).update_one(set__first_name = new_fn)
    collab_test.reload()
    assert collab_test.first_name == new_fn
    print("new fn: ",collab_test.first_name)

def test_update_Collab_LN(email_test, new_ln):
    """
        updates LN of collab
    """
    collab_test = collaborator.objects.get(email= email_test)
    print("old ln: ", collab_test.last_name)
    collaborator.objects(email=email_test).update_one(set__last_name = new_ln)
    collab_test.reload()
    assert collab_test.last_name == new_ln
    print("new ln: ",collab_test.last_name)

def test_update_Admin_Password(usern, new_pass):
    """
        updates password of admin
    """
    test_admin = admin.objects.get(username=usern)
    print("old password: ", test_admin.password)
    admin.objects(username = usern).update_one(set__password = new_pass)
    test_admin.reload()
    assert test_admin.password == new_pass
    print("new password: ", test_admin.password)

def test_update_doc(titleDoc, des, tags):
    """
        updates description of doc
    """
    #process of testing update
    doc_test = document_case.objects.get(title= titleDoc)
    print('old description: ' + doc_test.description + " \nold tags: " )
    print(doc_test.tagsDoc)
    document_case.objects(title = titleDoc).update_one(set__description = des)
    Documendocument_casetCase.objects(title = titleDoc).update_one(set__tagsDoc = tags)
    # DocumentCase.objects(title = "The great Flooding", author__author_LN = "TS").update_one(set__author__S__author_FN = "joy")
    doc_test.reload()
    print('new description: ' + doc_test.description + " \nnew tags: " )
    print(doc_test.tagsDoc)
    assert doc_test.description == des
    assert doc_test.tagsDoc == tags

#-----------------------------------Methods for deletion--------------------------

def test_delete_tag(deltag):
    """
        Deletes a tag
    """
    tag_read = tag.objects()
    tags = []
    for x in tag_read:
        tags.append(x.tagItem)
    print(tags)
    #eliminate more than one doc
    tag.objects(tagItem = deltag).delete()
    new_tags =[]
    new_tag_read = Tag.objects()
    for x in new_tag_read:
        new_tags.append(x.tagItem)
    print(new_tags)

def test_delete_doc(titleDoc):
    """
        Delete one doc
    """
    docs_read = document_case.objects()
    old_docs = []
    for x in docs_read:
        old_docs.append(x.title)
    print(old_docs)
    
    document_case.objects(title = titleDoc).delete()
    new_docs_read = document_case.objects()
    new_docs = []
    for x in new_docs_read:
        new_docs.append(x.title)
    print(new_docs)

#---------------------------------Methods for Read --------------------------

def test_read_infras():
    """
        Returns the list of Infrastructure Types from the DB
    """
    infra_read = infrastructure.objects()
    infras = []
    for x in infra_read:
        infras.append(x.infrastructureType)
    print(infras)
 
def test_read_damage():
    """
        Returns the list of Damage Types from the DB
    """
    damage_read = damage.objects()
    damages = []
    for x in damage_read:
        damages.append(x.damageType)
    print(damages)

def test_read_tags():
    """
        Returns the list of Tags from the DB
    """
    tag_read = tag.objects()
    tags = []
    for x in tag_read:
        tags.append(x.tagItem)
    print(tags)

def test_get_tag(gettag):
    """
        Returns a specific Tag from the DB
    """
    tagread = tag.objects.get(tagItem = gettag)
    print(tagread.tagItem)
    assert tagread.tagItem == gettag

def test_get_infras(infras):
    """
        Returns a specific Infrastructure Type from the DB
    """
    infraread = infrastructure.objects.get(infrastructureType = infras)
    print(infraread.infrastructureType)
    assert infraread.infrastructureType == infras

def test_get_damage(damage):
    """
        Returns a specific Damage Type from the DB
    """
    damageread = damage.objects.get(damageType = damage)
    print(damageread.damageType)
    assert damageread.damageType == damage

def test_read_doc(titleDoc):
    """
        Returns a specific Document from the DB
    """
    doc_test = document_case.objects.get(title = titleDoc)
    print("creatoriD: " + doc_test.creatoriD)
    print("title: " + doc_test.title)
    print("description: " + doc_test.description)
    print("incidentDate: " + doc_test.incidentDate)
    print("creationDate: " + doc_test.creationDate)
    print("lastModificationDate: " + doc_test.lastModificationDate)
    print("tagsDoc: ", doc_test.tagsDoc)
    print("infrasDocList: ", doc_test.infrasDocList)
    print("damageDocList: " , doc_test.damageDocList)
    print("location: " , doc_test.location)
    print("author: \n\tname" , doc_test.author[0].author_FN, doc_test.author[0].author_LN, 
    "\n\temail",doc_test.author[0].author_email, "\n\tfaculty",doc_test.author[0].author_faculty)
    print("actor: \n\tname:" , doc_test.actor[0].actor_FN, doc_test.actor[0].actor_LN, 
    "\n\trole:",doc_test.actor[0].role)
    print("timeline: " , doc_test.timeline[0].event,doc_test.timeline[0].eventStartDate, doc_test.timeline[0].eventEndDate )
    print("section: \n\tsecTitle:" , doc_test.section[0].secTitle, "\n\tcontent:",  doc_test.section[0].content )

def read_get_admin(username):
    """
        Returns a specific Admin from the DB
    """
    getadmin = admin.objects.get(username = username)
    print("Username: " + getadmin.username)
    print("Password: " + getadmin.password)

def read_get_collabs():
    """
        Returns a list of Collaborators from the DB
    """
    collab = collaborator.objects()
    for x in collab:
        print("\nFN: " + x.first_name)
        print("LN: " + x.last_name)
        print("email: " + x.email)
        print("banned: " + str(x.banned))
        print("approved: " + str(x.approved))

def read_get_docs():
    """
        Returns a list of Documents from the DB
    """
    docs = document_case.objects()
    for doc_tests in docs:
        print("creatoriD: " + doc_tests.creatoriD)
        print("title: " + doc_tests.title)
        print("description: " + doc_tests.description)
        print("incidentDate: " + doc_tests.incidentDate)
        print("creationDate: " + doc_tests.creationDate)
        print("lastModificationDate: " + doc_tests.lastModificationDate)
        print("tagsDoc: ", doc_tests.tagsDoc)
        print("infrasDocList: ", doc_tests.infrasDocList)
        print("damageDocList: " , doc_tests.damageDocList)
        print("location: " , doc_tests.location)
        print("author: \n\tname" , doc_tests.author[0].author_FN, doc_tests.author[0].author_LN, 
        "\n\temail",doc_tests.author[0].author_email, "\n\tfaculty",doc_tests.author[0].author_faculty)
        print("actor: \n\tname:" , doc_tests.actor[0].actor_FN, doc_tests.actor[0].actor_LN, 
        "\n\trole:",doc_tests.actor[0].role)
        print("timeline: " , doc_tests.timeline[0].event,doc_tests.timeline[0].eventStartDate, doc_tests.timeline[0].eventEndDate )
        print("section: \n\tsecTitle:" , doc_tests.section[0].secTitle, "\n\tcontent:",  doc_tests.section[0].content )

if __name__ == '__main__':
    """
    Create test functions
    """
    # test_create_Collab("Pink","Snow","sNow.pimk@upr.edu")
    # test_create_Admin("jai.TSantos13", "ICOMuprm12345")
    # test_create_Tag(new_tag)
    # test_create_Infrastructure(new_infras)
    # test_create_Damage('Tsunamis')
    # test_create_doc(creatoriD= 'JBJBijnj283892husdBHB',language='English', title='The Great Moon', description="It was horrible..", incidentDate='2010-02-03',
    #  creationDate='2012-03-01', lastModificationDate='2014-08-03', 
    #  infrasDocList=['Structure', 'Water'],damageDocList=['Flooding'],  tagsDoc=['Flood', 'Rain'],
    #  location=['Coamo, PR'],author=[['Jainel', 'Torres', 'jainel.torres@upr.edu', 'ICOM']], 
    #  actor=[['Ricardo', 'Rosello', 'Governor']], timeline=[['It started to rain', '2010-02-03', '2010-04-01']],
    #  section=[['Introduction', 'It was raining a lot']])
    """
    Update test functions
    """
    # test_update_Collab_FN(email_test, new_fn)
    # test_update_Collab_LN(email_test, new_ln)
    # test_update_Admin_Password(usern, new_pass)
    # test_update_doc(titleDoc, des, tags)
    """
    Delete test functions
    """
    # test_delete_tag(tag)
    # test_delete_doc(titleDoc)
    """
    Read test functions
    """
    # test_read_infras()
    # test_read_damage()
    # test_read_tags()
    # test_get_tag('Burning')
    # test_get_infras('Structure')
    # test_get_damage("Tsunamis")
    # test_read_doc('The Great Rain')
    # read_get_admin('Jai.torress13')
    # read_get_collabs()
    # read_get_docs()
