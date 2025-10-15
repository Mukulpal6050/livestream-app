import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
PORT = int(os.getenv("PORT", 5000))

if not MONGO_URI:
    raise RuntimeError("MONGO_URI is not set in environment (.env).")

# Create client and get database
client = MongoClient(MONGO_URI)
# Use explicit DB name matching your deliverables
db = client["livestream_db"]
