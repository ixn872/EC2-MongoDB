#For database
import pymongo
from pymongo import MongoClient
import urllib.parse


######Mongo connection stuff
username = urllib.parse.quote_plus('dbname')
password = urllib.parse.quote_plus('password')

url = "mongodb+srv://dbNicoleDouglas:{}@maincluster.ynnci.mongodb.net/{}?retryWrites=true&w=majority".format(password,dbname)
client = MongoClient(url)
db = client.<dbname>

collection = db.<yourcollection>

#Returns all the ids and object ids from the collection on MongoDB
def get_db_ids():
     ids = [] # create an empty list for IDs
     # iterate pymongo documents with a for loop
     ids = [doc["_id"] for doc in collection.find()]
     # append each document's ID to the list
     return ids
