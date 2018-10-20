from random import choice
from pymongo import MongoClient
import random
from pprint import pprint
url = '127.0.0.1:27017'
#'127.0.0.1:27017' #'52.90.61.82'
client = MongoClient(url)
db= client.test
# Issue the serverStatus command and print the results
users = db['users']
time_zone_list =[a for a in range(-12, 15)]
language_list =['English','Chinese','Spanish','French','Portuguese','Arabic','Russian','Hindi']
expertise_list =['Application process','Logistical support pre-departure',
                'Logistical support post-departure','Navigating services','Emotional support/guidance','Cross-cultural communication',
                'Conflict within your group','Managing Expections of sponsored refugees and the group','Transitioning out of sponsorship']
country_list =['USA','Canada','Argentina']
sponsor_list = ['Forming Sponsorship Group','Application in Process','Application Submitted - Awaiting Approval','Application Submitted - Approved','Post-Arrival']
contact_list = ['email','phone','skype','google hangout','facebook','whatsapp','viber']
type_list=[0,0,0,0,1,1,1,1,1,1]
num_of_mock = 10000


# code to populate user cred
for i in range(num_of_mock):
    person_query = {
        'email': str(i) + '@email.com',
        'password': 'asdf',
        'type': choice([0,1,1])
    }
    users.insert_one(person_query)


# code to populate different aspect of user
for document in users.find():
    id = document["_id"]
    document['firstName'] = 'John'
    document['lastName'] = 'Doe'
    document['bio'] = 'Community-based sponsorship programs allow individuals to directly engage in refugee resettlement efforts. Sponsors commit to providing financial, emotional and resettlement support to help newly-arrived refugees integrate into life in a new country.'
    document['time_zone'] = choice(time_zone_list)
    document['language'] = random.sample(language_list, choice(range(1,3)))
    document['expertise'] = random.sample(expertise_list, choice(range(1,5)))
    document['contact'] = choice(contact_list)
    document['city'] = "CITY"
    document['state'] = "STATE"
    document['country'] = choice(country_list)
    if document['type'] == 1:
        document['num_sponsored'] = choice(range(2,6))
        document['num_mentee'] = choice(range(1,6))
    else:
        document['num_sponsored'] = choice(range(0,2))
    sponsoring = choice([True,False])
    if sponsoring:
        document['sponsoring'] = sponsoring
        document['stage_sponsor'] = choice(sponsor_list)
    else:
        document['sponsoring'] = sponsoring

    users.update({"_id":id}, {'$set': document})
    # prefer contact list of contact

    # person.update_one({'_id':document["_id"]},{'$set':document})

    #insert_one^
    # person username mock data
