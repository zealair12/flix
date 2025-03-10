import pymongo
import os
from dotenv import load_dotenv
from movie_recs import generate_embedding

# This loads the .env file
load_dotenv()

# MongoDB URI set directly in the script
mongo_uri = os.getenv('MONGO_URI')

# Connect to the database
client = pymongo.MongoClient(mongo_uri)
db = client.sample_mflix
collection = db.movies

# This is the search text we want to find similar plots for
query = "Imaginary characters from outer space at war"

# This is how we search using the embedding of the query
results = collection.aggregate([
    {
        "$vectorSearch": {
            "queryVector": generate_embedding(query),
            "path": "plot_embedding_hf",
            "numCandidates": 100,
            "limit": 4,
            "index": "PlotSemanticSearch",
        }
    }
])

# Show the results
for document in results:
    print(f"Movie Name: {document['title']},\nMovie Plot: {document['plot']}\n")