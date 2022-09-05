import os
from os import getenv

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5172114510").split()))
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
LOG_CHAT = int(getenv("LOG_CHAT", ""))
MONGO_DB = getenv("MONGO_DB", "")
ALIVE_IMG = getenv("ALIVE_IMG", "https://graph.org/file/876df78ce11a5ca68fd30.jpg")
DB_URL = getenv("DATABASE_URL", "")
