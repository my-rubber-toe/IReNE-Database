
from mongoengine import *
from schema_DB import *
import names
import random
import namegenerator
import datetime
from faker  import Faker 

"""
    The purpose of this file is to auto generate mock data for the database
"""
fake = Faker() 

infrastructure = ["Streets or Highway", "Bridges", "Airports", "Water Supply", "Waste Water Management",
    "Power Generation & Transmission", "Telecommunications" , "Housing", "Building", "Ports",
    "Public Transportation"]
damage = [ "Earthquake", "Hurricane", "Tsunami", "Flooding", "Landslide", "Fire/smoke", 
    "Extreme Precipitation", "Water Damage", "Wind Damage", "Tornado"]
tags = infrastructure + damage

index = 0
for index in range(0,100):
    #mock data for creating collaborators
    fn = names.get_first_name()
    ln = names.get_last_name()
    emailc = fn.lower() + '.' + ln.lower() + "@upr.edu"
    print(emailc)
    collab1 = collaborator(first_name = fn, 
    last_name = ln, 
    approved = random.choice([True, False]),
    banned = random.choice([True, False]),
    email = emailc)
    collab1.save()
   

    #make fake text
    my_word_list = [
    'Fire','The','Date',
    'City','Building','Water',
    'Rain','Shake','Earthquake',
    'Energy','Power','Pipes','Closed','Hurricane', 'Flood', 'wow'
    'Damage','Infrastructure', 'PR', 'Island', 'What', 'is', 'comes' ]

    #random date
    start_date = datetime.date(2010, 1, 1)
    end_date = datetime.date(2020, 2, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    dates = []
    for x in range(100):
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        dates.append(str(random_date))

    #creates doc
    facultyITEM = ['ICOM', 'CIIC', 'INCI', 'INSO', 'INQU', 'INEL', 'MATE', 'QUIM', 'ADEM', 'PSIC']
    roles = ['Mayor', 'President', 'CEO','Owner','Resident','Engineer','Doctor']
    get_collab = collaborator.objects.get(email= emailc)
    authorDoc = author(author_FN = get_collab.first_name, author_LN = get_collab.last_name, 
    author_email = get_collab.email, author_faculty = random.choice(facultyITEM))

    actorDoc = actor(actor_FN = names.get_first_name(), actor_LN = names.get_last_name(), 
    role = random.choice(roles))

    start = random.choice(dates)
    end = random.choice(dates)
    while(start > end):
        end = random.choice(dates)
    
    timelineDoc = timeline(event = fake.sentence(ext_word_list=my_word_list), 
    eventStartDate = start, eventEndDate = end)

    titles=['Introduction', 'Body', 'Analysis', 'Conclusion', 'Executive Summary', 'Discussion']
    sectionDoc = section(secTitle = random.choice(titles), 
    content = fake.sentence(ext_word_list=my_word_list))
    languageDoc = ['English', 'Spanish']

    ad = ["Coamo, PR", "Arecibo, PR", "Santa Isabel, PR", "Camuy, PR", "Salinas, PR", "San Juan, PR", "Mayagüez, PR", "Carolina, PR", "Aguas Buenas, PR", "Isabela, PR", "Quebradillas, PR", "Moca, PR", "Añasco, PR", "Yabucoa, PR", "Caguas, PR", "Lares, PR", "Humacao, PR", "Gurabo, PR", "Vieques, PR", "Maricao, PR", "Patillas, PR", "Arroyo, PR", "Las Piedras, PR", "Cidra, PR", "Maunabo, PR", "Fajardo, PR", "Ceiba, PR", "Juncos, PR", "Orocovis, PR", "Utuado, PR", "Jayuya, PR", "Ciales, PR", "Corozal, PR", "Aibonito, PR", "Sabana Grande, PR", "Guánica, PR", "Cayey, PR", "Vega Baja, PR"]
    town1 = random.choice(ad)
    while True:
            town2 = random.choice(ad)
            if(town1 != town2):
                break

    citypr = city_pr.objects.get(city = town1)
    citypr1 = city_pr.objects.get(city = town2)
    loc = location(address= citypr.city, latitude= citypr.latitude, longitude=citypr.longitude)
    loc1 = location(address= citypr1.city, latitude= citypr1.latitude, longitude=citypr1.longitude)
    inc = random.choice(dates)
    created = random.choice(dates)
    mod = random.choice(dates)
    while(inc > created):
        created = random.choice(dates)
    
    while(created > mod):
        mod = random.choice(dates)
    

    doc = document_case(creatoriD = get_collab, title = ("The Great " + namegenerator.gen() + namegenerator.gen()), location=[loc,loc1], 
    description = fake.sentence(ext_word_list=my_word_list), published=random.choice([True, False]),
    incidentDate = inc, 
    creationDate= created,
    lastModificationDate= mod,
    tagsDoc=[random.sample(tags,3)], 
    infrasDocList= [random.sample(infrastructure,3)],
    damageDocList= [random.sample(damage,3)],
    author = [authorDoc], actor = [actorDoc],section = [sectionDoc],timeline = [timelineDoc], language=random.choice(languageDoc))
    doc.save()