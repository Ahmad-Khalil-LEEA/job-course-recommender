from sentence_transformers import SentenceTransformer

def get_embedding_model():
    # Use a lightweight model for demo purposes
    model = SentenceTransformer("all-MiniLM-L6-v2")
    return model
