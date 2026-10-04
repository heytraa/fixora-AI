from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import EMBEDDING_MODEL, EMBEDDING_DIMENSION, GOOGLE_API_KEY

def get_embedder():
    return GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=GOOGLE_API_KEY,
        output_dimensionality=EMBEDDING_DIMENSION,
    )