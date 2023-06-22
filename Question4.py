#Using the database and the collection created in question number 3, write a code to insert one record,
#and insert many records. Use the find() and find_one() methods to print the inserted record.

import pymongo

# add your connection string
client = pymongo.MongoClient('Connetion-string')

#Database created
db = client['gouravdb']

data = {
    "name": "gourav",
    "class": "DS-2.0"
}

data2 = [{"name":"rakesh","class":"english"},
         {"name":"keshav","class": "maths"}]

#collection created
collection = db['myrecord']

# Data added inside Collection
collection.insert_one(data)

# Multiple Data added inside Collection
collection.insert_many(data2)

# Find the all value for the parameter
for i in collection.find("name"):
    print(i)

# Find the Single value for the parameter
for i in collection.find_one('name'):
    print(i)