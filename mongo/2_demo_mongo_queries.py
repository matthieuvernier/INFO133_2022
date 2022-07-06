from pymongo import MongoClient
from random import randint

# pprint library is used to make the output look more pretty
from pprint import pprint

client = MongoClient("localhost", port=27017)
db=client.test

data = {
        'key1' : "hola",
        'key2' : 20
    }
    
result=db.my_collection.insert_one(data)

results=db.my_collection.find()

for result in results:
    print(result)