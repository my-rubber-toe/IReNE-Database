
from mongoengine import *
from schema_DB import *
import names
import random
import namegenerator
from faker  import Faker 
fake = Faker() 


facultyITEM = ['ICOM', 'INEL', 'INSO', 'CIIC', ]
fn = names.get_first_name()
ln = names.get_last_name()
emailc = fn + '.' + ln + "@upr.edu"
collab1 = Collaborator(first_name = fn, 
last_name = ln, 
approved = random.choice([True, False]),
banned = random.choice([True, False]),
email = emailc
)
collab1.save()

infrastructure = ['Transportation', 'Energy', 'Water', 'Security', 'Ports', 'Structure', 'Construction']
damage = ['Flooding','Earthquake', 'Fire', 'Tsunamis', 'Hurricane']
tags = ['Hurricane', 'Rain', 'Earthquake', 'Fire', 'Burning', 'Flood', 'Power Outage']
#after running once, just comment this and run it again for more fake data
for infra in infrastructure:
    infras = Infrastructure(infrastructureType=infra)
    infras.save()
for damages in damage:
    dama = Damage(damageType=damages)
    dama.save()
for tagslist in tags:
    tag = Tag(tagItem=tagslist)
    tag.save()

#make fake text
my_word_list = [
'Fire','The','Date',
'City','Building','Water',
'Rain','Shake','Earthquake',
'Energy','Power','Pipes','Closed','Hurricane', 'Flood', 'wow'
'Damage','Infrastructure', 'PR', 'Island' ]
#code below is added inside of doc
#fake.sentence(ext_word_list=my_word_list)

#random date
start_date = datetime.date(2010, 1, 1)
end_date = datetime.date(2020, 2, 1)

time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
dates = []
for x in range(50):
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    dates.append(str(random_date))

#creates doc
roles = ['Mayor', 'President', 'CEO','Owner','Resident','Engineer','Doctor']
get_collab = Collaborator.objects.get(first_name= fn)
authorDoc = Author(author_FN = get_collab.first_name, author_LN = get_collab.last_name, 
author_email = get_collab.email, author_faculty = get_collab.faculty)

actorDoc = Actor(actor_FN = names.get_first_name(), actor_LN = names.get_last_name(), 
role = random.choice(roles))

timelineDoc = Timeline(event = fake.sentence(ext_word_list=my_word_list), 
eventStartDate = random.choice(dates), eventEndDate = random.choice(dates))

titles=['Introduction', 'Body', 'Analysis', 'Conclusion']
sectionDoc = Section(secTitle = random.choice(titles), 
content = fake.sentence(ext_word_list=my_word_list))
languageDoc = ['English', 'Spanish']

doc = DocumentCase(creatoriD = str(get_collab.id), title = namegenerator.gen(), location=[fake.address()], 
description = fake.sentence(ext_word_list=my_word_list), published=random.choice([True, False]),
incidentDate = random.choice(dates), 
creationDate= random.choice(dates),
lastModificationDate= random.choice(dates),
tagsDoc=[random.choice(tags),random.choice(tags)], 
infrasDocList= [random.choice(infrastructure), random.choice(infrastructure)],
damageDocList= [random.choice(damage), random.choice(damage)],
author = [authorDoc], actor = [actorDoc],section = [sectionDoc],timeline = [timelineDoc], language=random.choice(languageDoc))
doc.save()
# incident_date = fields.String(required=True, format="%Y-%m-%d")