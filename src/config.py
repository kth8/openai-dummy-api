from dotenv import load_dotenv
from os import getenv

load_dotenv()

HOST = getenv("HOST", "127.0.0.1")
PORT = int(getenv("PORT", "7000"))
DEBUG = getenv("DEBUG", "false").lower() == "true"
LOG_LEVEL = getenv("LOG_LEVEL", "info")

import tiktoken

try:
    encoder = tiktoken.get_encoding("o200k_base")
except Exception as e:
    encoder = tiktoken.get_encoding("cl100k_base")
