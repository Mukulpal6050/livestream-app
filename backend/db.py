# backend/db.py
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get Mongo URI from environment file
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB Atlas
client = MongoClient(MONGO_URI)

# Access default database mentioned in URI
db = client.get_database()

print("✅ Connected to MongoDB Atlas successfully!")
