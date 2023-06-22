# Write a code to connect MongoDB to Python. Also, create a database and a collection in MongoDB.
import pymongo

# add your connection string
client = pymongo.MongoClient('Connetion-string')

#Database created
db = client['gouravdb']

data = {
    "name": "gourav",
    "class": "DS-2.0"
}

#collection created
collection = db['myrecord']

# Data added inside Collection
collection.insert_one(data)