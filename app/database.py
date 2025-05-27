from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()
mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)
db = client["certificate_verification"]
collection = db["certificates"]

def insert_certificate(name, hash_value):
    collection.insert_one({"name": name, "hash": hash_value})

def find_certificate_by_hash(hash_value):
    return collection.find_one({"hash": hash_value})
