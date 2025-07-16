import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()  # ✅ Loads GROQ_API_KEY from .env

def load_llm():
    return ChatGroq(
        model_name="llama3-8b-8192",
        temperature=0.2
    )
