import mongoengine
from schema_DB import *
import re
from faker  import Faker

fake = Faker() 
name_regex = ['Jainel', 'Linda M', 'Linda M-M', 'll', 'L', 'llllllllllllllllllllllllllllll', 'Linda1', 'Ángel', 'ÁNGEL',
 'Jainel Marie', 'Torres-Santos', 'Del Pueblo', 'San-Jose', 'Juan-Del-Pueblo', 'Jainel marie', 'Dj', 'Juan Del Pueblo-Rosado Montoya']

email_regex = ['jainel.torres@upr.edu', 'juan.pueblo1@upr.edu', 'juanadelpueblo@upr.edu', 'j@upr.edu', '@upr.edu', 
'ncjsncxuiwehcuiewhuhceuwhceiuw.deoqhfduiewfhbiuejjcjwebnejbqei@upr.edu', 'ncjsncxuiwehcuiewhuhceuwhceiuw.deokqhfduiewfhbiuejjcjwebnejbqei@upr.edu']

admin_regex = ['jaineltorres', 'jainel.torres', 'jainel..torres', 'jainel.torres2', 'qwert', 'jai.el', 'jainelllll.lllllllll', 
'jainelllll.llllllllll', 'jainel$', 'jainel', 'Jainel.torres', '.jainel', 'jainel.', 'jainel3', 'Jainel4']

category_regex = ['', 'J', 'Ports/Lol', 'Parks & Recreations', 'Port, Camping, Building & Lol', 'Aeropuerto, Avión, Volar, Voló, Volaron, Volamos,A',
'Aeropuerto, Avión, Volar, Voló, Volaron, Volamos,AA', 'ala']

title_regex = ['The Great Rain', 'The Grea', 'The Great Magnific Extraodinary Sequence of Events', 
'The Great Magnific Extraodinary Sequence of Events2', 'the great sequence of event', 'The Great: Rain',
'the great sequence of evemt!']

roleFaculty_regex = ['ICOM', 'Icom', 'iCOM', 'i', 'I', 'IC', 'Ic', 'Ing. de Sistemas: CE', 'Ingeniero de Computadoras y si',
'Ingeniero de Computadoras y sis', 'The 4th engineer: CE']

description_regex = ['', '1', 'a','HIWJCNEIJJNIEWBDIEUDHBIUEWHFIUWEHFIUEWFHIUHEIWFBHWFBHERBFHRBFHBFHEWFBHEWBFWEHFBHWBFIHFBIWEUHFIUWEHIEWNHWEINCEIWJCNEIJNIEWBDIEUDHBIUEWHFIUWEHFIUEWFHIUHEIWFBHWFBHERBFHRBFHBFHEWFBHEWBFWEHFBHWBFIHFBIWEUHFIUWEHIEWNHWEINCEIWJCNEIJNIEWBDIEUDHBIUEWHFIUWEHFIUEWFHIUEWFHIUWFHUIWEFHUIWEFHIUWEFHEIUWFHEWUIFIUWNCWIDNCWIECNIUWHDUIEWHDUIWEHDUWEIDNUIWENDIWEUNDWEINDIEUWNDWEIUNDWEIUDNWEIUNDWIEDNWEIUDNWEIUNDUWEIDNWEUIDNWEUDNIWEUNDWEIUDNUEIWDNIUDNIUDNEIUDNEIUWNDWENDEWNDEWNDUENUDNIUWENDWENDIUNDINDDDUEWDIUWEHDUWIHDIUWW',
"HIWJCNEIJJNIEWBDIEUDHJBIUEWHFIUWEHFIUEWFHIUHEIWFBHWFBHERBFHRBFHBFHEWFBHEWBFWEHFBHWBFIHFBIWEUHFIUWEHIEWNHWEINCEIWJCNEIJNIEWBDIEUDHBIUEWHFIUWEHFIUEWFHIUHEIWFBHWFBHERBFHRBFHBFHEWFBHEWBFWEHFBHWBFIHFBIWEUHFIUWEHIEWNHWEINCEIWJCNEIJNIEWBDIEUDHBIUEWHFIUWEHFIUEWFHIUEWFHIUWFHUIWEFHUIWEFHIUWEFHEIUWFHEWUIFIUWNCWIDNCWIECNIUWHDUIEWHDUIWEHDUWEIDNUIWENDIWEUNDWEINDIEUWNDWEIUNDWEIUDNWEIUNDWIEDNWEIUDNWEIUNDUWEIDNWEUIDNWEUDNIWEUNDWEIUDNUEIWDNIUDNIUDNEIUDNEIUWNDWENDEWNDEWNDUENUDNIUWENDWENDIUNDINDDDUEWDIUWEHDUWIHDIUWW"]


for x in name_regex:
    z = re.match('^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ]*(-){0,1}[a-z A-Z À-ÿ]*[a-záéíóúñü]$', x)
    if (len(x) > 1 and len(x) < 31):
        print('Name: ' ,x ,' Result', z)
    else:
        print('NOT PASSED: ', x)

for x in name_regex:
    z = re.match('^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ]*(-){0,1}[a-z A-Z À-ÿ]*$', x)
    if (len(x) > 0 and len(x) < 31):
        print('Collab name: ' ,x ,' Result', z)
    else:
        print('NOT PASSED: ', x)


for x in email_regex:
    z = re.match('^[\.a-z0-9]*(@upr\.edu)$', x)
    if (len(x) > 8 and len(x) < 71):
        print('Email: ' ,x ,' Result', z)
    else:
        print('NOT PASSED: ', x)


for x in admin_regex:
    z = re.match('(^[^.]([a-zA-Z0-9]*)[.]{0,1}([a-zA-Z0-9]*))[^.]$', x)
    if (len(x) > 5 and len(x) < 21):
        print('admin: ' ,x ,' Result', z)
    else:
        print('NOT PASSED: ', x)

for x in category_regex:
    z = re.match('^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & ,]*[a-záéíóúñü]$', x)
    if (len(x) > 1 and len(x) < 51):
        print('category: ' ,x ,' Result', z)
    else:
        print('NOT PASSED: ', x)

for x in title_regex:
    z = re.match('^[A-ZÁÉÍÓÚÑÜ][A-Z a-z 0-9 À-ÿ :]*[A-Za-z0-9À-ÿ]$', x)
    if (len(x) > 9 and len(x) < 51):
        print('title: ' ,x ,' Result', z)
    else:
        print('NOT PASSED: ', x)

for x in title_regex:
    z = re.match('^[A-ZÁÉÍÓÚÑÜ][A-Z a-z 0-9 À-ÿ :]*[A-Za-z0-9À-ÿ]$', x)
    if (len(x) > 1 and len(x) < 51):
        print('Sectitle: ' ,x ,' Result', z)
    else:
        print('NOT PASSED: ', x)

for x in roleFaculty_regex:
    z = re.match('^[A-ZÁÉÍÓÚÑÜ][a-z A-Z : 0-9 À-ÿ]*[.]{0,1}[ ]{0,1}[a-z A-Z : 0-9 À-ÿ]*[a-zA-Z0-9À-ÿ]$', x)
    if (len(x) > 1 and len(x) < 31):
        print('role/Faculty: ' ,x ,' Result', z)
    else:
        print('NOT PASSED: ', x)

for x in description_regex:
    if (len(x) > 0 and len(x) < 501):
        print('description: ' ,x , 'len: ', len(x))
    else:
        print('NOT PASSED: ', x, 'len: ', len(x))




my_word_list = [
    'Fire','The','Date',
    'City','Building','Water',
    'Rain','Shake',
    'Energy','Power','Pipes','Closed', 'Flood', 'wow'
    'Damage', 'PR', 'Island', 'What', 'is', 'comes', '.', ',', ':', 'iH', 'Hi', "Hello",
    'Linda M', 'Linda M-M', 'll', 'L', "Avión", "Volar", "Voló", "Volaron", "Volamos","AA", "!", "1", "2","", " ", "-"]

list_sentences = []
for x in range(700):
    list_sentences.append(fake.sentence(ext_word_list=my_word_list))

name_passed = []
name_notpassed = []
for x in list_sentences:
    z = re.match('^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ]*(-){0,1}[a-z A-Z À-ÿ]*[a-záéíóúñü]$', x)
    if (len(x) > 1 and len(x) < 31):
        print('Name: ' ,x ,' Result', z)
        name_passed.append(x)
    else:
        print('NOT PASSED: ', x)
        name_notpassed.append(x)

collabname_passed = []
collabname_notpassed = []
for x in list_sentences:
    z = re.match('^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ]*(-){0,1}[a-z A-Z À-ÿ]*$', x)
    if (len(x) > 0 and len(x) < 31):
        print('Collab name: ' ,x ,' Result', z)
        collabname_passed.append(x)
    else:
        print('NOT PASSED: ', x)
        collabname_notpassed.append(x)

cat_passed = []
cat_notpassed = []
for x in list_sentences:
    z = re.match('^[A-ZÁÉÍÓÚÑÜ][a-z A-Z À-ÿ / & ,]*[a-záéíóúñü]$', x)
    if (len(x) > 1 and len(x) < 51):
        print('category: ' ,x ,' Result', z)
        cat_passed.append(x)
    else:
        print('NOT PASSED: ', x)
        cat_notpassed.append(x)

title_passed = []
title_notpassed =[]
for x in list_sentences:
    z = re.match('^[A-ZÁÉÍÓÚÑÜ][A-Z a-z 0-9 À-ÿ :]*[A-Za-z0-9À-ÿ]$', x)
    if (len(x) > 9 and len(x) < 51):
        print('title: ' ,x ,' Result', z)
        title_passed.append(x)
    else:
        print('NOT PASSED: ', x)
        title_notpassed.append(x)

role_passed = []
role_notpassed =[]
for x in list_sentences:
    z = re.match('^[A-ZÁÉÍÓÚÑÜ][a-z A-Z : 0-9 À-ÿ]*[.]{0,1}[ ]{0,1}[a-z A-Z : 0-9 À-ÿ]*[a-zA-Z0-9À-ÿ]$', x)
    if (len(x) > 1 and len(x) < 31):
        print('role/Faculty: ' ,x ,' Result', z)
        role_passed.append(x)
    else:
        print('NOT PASSED: ', x)
        role_notpassed.append(x)


with open('test.json', 'w') as outfile:
    json.dump({"name_passed" : name_passed, "name_notpassed": name_notpassed,
     "collabname_passed": collabname_passed, "collabname_notpassed":collabname_notpassed,
     "cat_passed": cat_passed,"cat_notpassed":cat_notpassed,"title_passed":title_passed,
      "title_notpassed":title_notpassed, "role_passed":role_passed,"role_notpassed":role_notpassed }, outfile)