from langchain_google_genai import ChatGoogleGenerativeAI
from config import LLM_MODEL, GOOGLE_API_KEY

def get_llm():
    return ChatGoogleGenerativeAI(
        model=LLM_MODEL,
        google_api_key=GOOGLE_API_KEY,
    )