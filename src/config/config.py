"""Configuration module for Agentic RAG system"""

import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# class Config:
#     """Configuration class for RAG system"""
    
#     # API Keys
#     OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
#     # Model Configuration
#     LLM_MODEL = "openai:gpt-4o"
    
#     # Document Processing
#     CHUNK_SIZE = 500
#     CHUNK_OVERLAP = 50
    
#     # Default URLs
#     DEFAULT_URLS = [
#         "https://lilianweng.github.io/posts/2023-06-23-agent/",
#         "https://lilianweng.github.io/posts/2024-04-12-diffusion-video/"
#     ]
    
#     @classmethod
#     def get_llm(cls):
#         """Initialize and return the LLM model"""
#         os.environ["OPENAI_API_KEY"] = cls.OPENAI_API_KEY
#         return init_chat_model(cls.LLM_MODEL)
    

class Config:
    
    """Configuration class for RAG system"""

    # API Keys
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    # Groq Model Configuration
    # Popular options:
    # - llama3-70b-8192 (best quality)
    # - llama3-8b-8192 (fast & cheap)
    # - mixtral-8x7b-32768 (great for long context)
    LLM_MODEL = "llama-3.1-8b-instant"

    # Document Processing
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50

    # Default URLs
    DEFAULT_URLS = [
        "https://lilianweng.github.io/posts/2023-06-23-agent/",
        "https://lilianweng.github.io/posts/2024-04-12-diffusion-video/"
    ]

    @classmethod
    def get_llm(cls):
        """Initialize and return the Groq LLM"""
        if not cls.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is not set")

        return ChatGroq(
            groq_api_key=cls.GROQ_API_KEY,
            model_name=cls.LLM_MODEL,
            temperature=0.2,
            max_tokens=2048,
        )