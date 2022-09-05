import logging
import sys
from pyrogram import Client, filters, idle
from pyrogram.types import *
import requests
import os
import re
import asyncio
from datetime import datetime
from config import *

from apscheduler.schedulers.asyncio import AsyncIOScheduler

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)



API_ID = API_ID
API_HASH = API_HASH 
SUDO_USERS = SUDO_USERS
DB_URL = DB_URL
STRING_SESSION = STRING_SESSION

class App(Client):

    def __init__(self):
        super().__init__(
            "tgbot",
            api_id=API_ID,
            api_hash=API_HASH,
            session_name=STRING_SESSION,
            plugins={"root": "Levanter"},
        )

if not STRING_SESSION:
    logging.error("No String Session Found! Exiting!")
    sys.exit()

if not API_ID:
    logging.error("No Api-ID Found! Exiting!")
    sys.exit()

if not DB_URL:
    logging.error("No DB Found! Exiting!")
    sys.exit()

if not API_HASH:
    logging.error("No ApiHash Found! Exiting!")
    sys.exit()



idle()

print("YOUR USERBOT HAS STARTED SUCCESSFULLY")
