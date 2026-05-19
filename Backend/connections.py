from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017")

db = client['fenrir']
coll = db['names']
