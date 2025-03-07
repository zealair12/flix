# Advanced Search Engine - Movie Recommendation System 🚀🎬

In my **CSCI-110** class, we had to write algorithms for a search engine. The search feature worked similarly to LinkedIn's search — giving you vague, far-off results even if the query was off by just a single character.

But then I thought about how on **Google**, even with a ton of typos in my query, I still get pretty relevant results. So, what was the difference? **Vector Search** is what made Google smarter. Instead of searching for exact matches, it looks for similar meaning using vectors (basically numerical representations of text). And that’s what I wanted to recreate.

I used **MongoDB Atlas** to store the movie data and a **Hugging Face model** to generate the movie plot vectors (aka embeddings). I used the `all-MiniLM-L6-v2` sentence transformer model, which is free and great for this kind of thing. What it does is **convert text** (in this case, movie plots) into vectors so I can perform **semantic search** — finding movies with similar meanings even if the words are different.

### How It Works 🔍:

1. **Embedding Generation**: The Hugging Face model takes the movie plot text and turns it into a vector.
2. **Similarity Measurement**: The query is also turned into a vector, and the dot product is used to compare the similarity between the query vector and movie plot vectors.
3. **Recommendation**: Movies with higher dot product values are more similar to the query, so they get recommended.

To figure out which movies are similar to the query, I used the **dot product** to compare the query vector with the vectors of the movie plots in the database. Basically, the higher the dot product, the more similar the movie is to the search query, so it’s a better recommendation. My main goal was to **turn movie information into vectors** and include those vectors in the movie dataset, so the system can recommend movies based on the meaning behind their plots.

I used the **sample_mflix.movies** dataset from MongoDB, which has over 20k movies. But since I had limited resources, I restricted the embeddings to 50 movies and set the vector dimensionality to 384 (because that’s what my model could handle). There is already an embedding of over 3.5k movies available, but it’s done using the **OpenAI API**, and I can’t afford that. It’s a shame that vector embeddings aren’t universal; they’re model-specific, so I couldn't use those embeddings without access to that particular API.

### Technologies Used 🛠️:

- **MongoDB Atlas**: Used for storing the movie data and performing vector-based searches.
- **Hugging Face**: Utilized the `all-MiniLM-L6-v2` sentence transformer model to generate embeddings for the movie plots.
- **VS Code**: My trusty IDE for writing and running the code.

### Python Libraries 📚:

- **pymongo**: For connecting to and interacting with MongoDB.
- **requests**: To interact with Hugging Face API and get embeddings.
- **dotenv**: To load the environment variables like the MongoDB URI and Hugging Face API key.

### Limitations ⚠️:

- It works but could've been a lot better if I had access to an API that could map all 20k+ vectors.
- I was only able to vectorize and add embeddings to the first 50 movies due to resource limitations.
- The OpenAI API provides larger embeddings for more movies, but I couldn't access it, so I had to stick to the Hugging Face model.

### Acknowledgements 🙏:

- **3Blue1Brown** really helped me understand the theory.
- **freeCodeCamp** helped me implement the application.
