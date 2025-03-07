import pymongo
import requests
from dotenv import load_dotenv
import os

# This loads stuff from the .env file into Python so we can use them
load_dotenv()

# Grab secrets from the environment
hf_token = os.getenv("HF_API_KEY")
embedding_url = os.getenv("HF_EMBEDDING_URL")

# MongoDB URI set directly in the script
mongo_uri = "mongodb+srv://okechukwuzealachonu:ozachonu01@cluster0.fsagn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Connect to the database
client = pymongo.MongoClient(mongo_uri)
db = client.sample_mflix
collection = db.movies

def generate_embedding(text: str) -> list[float]:
    # This sends text to Hugging Face and gets the vector back.
    response = requests.post(
        embedding_url,
        headers={"Authorization": f"Bearer {hf_token}"},
        json={"inputs": text}
    )

    if response.status_code != 200:
        raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")

    return response.json()

# This adds embeddings to the first 50 movies with plots
for doc in collection.find({"plot": {"$exists": True}}).limit(50):
    doc["plot_embedding_hf"] = generate_embedding(doc["plot"])
    collection.replace_one({"_id": doc["_id"]}, doc)