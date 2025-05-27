from pymongo import MongoClient
from dotenv import load_dotenv
from bson import Binary
import os

# Load .env variables
load_dotenv()
mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)
db = client["certificate_verification"]
collection = db["certificates"]

def insert_certificate(name, file_content, hash_value):
    collection.insert_one({
        "name": name,
        "content": Binary(file_content),
        "hash": hash_value
    })

def find_certificate_by_hash(hash_value):
    return collection.find_one({"hash": hash_value})
