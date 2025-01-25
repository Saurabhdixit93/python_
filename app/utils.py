from dotenv import load_dotenv
import os

def load_env_variables():
    load_dotenv()
    return {
        "EMAIL": os.getenv("EMAIL"),
        "EMAIL_PASSWORD": os.getenv("EMAIL_PASSWORD"),
    }
