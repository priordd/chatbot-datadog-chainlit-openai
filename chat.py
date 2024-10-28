import os
from dotenv import load_dotenv
import chainlit as cl

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
