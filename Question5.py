# we can use the find() method to query any specific value so that we can access that with desired output.

# Below program shows the use of find()
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