import logging
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
cleanmode = {}

if not STRING_SESSION1:
    logging.error("No String Session Found! Exiting!")
    quit(1)

if not API_ID:
    logging.error("No Api-ID Found! Exiting!")
    quit(1)

if not MONGO_DB:
    logging.error("No MongoDB Found! Exiting!")
    quit(1)

if not API_HASH:
    logging.error("No ApiHash Found! Exiting!")
    quit(1)

if ALIVE_IMG:
    ALIVE_PIC = ALIVE_IMG
else: 
    ALIVE_PIC = 'https://graph.org/file/876df78ce11a5ca68fd30.jpg'

if LOG_CHAT:
    LOG_GROUP = LOG_CHAT
else:
    LOG_GROUP = 777000
Owner = LOG_GROUP

if STRING_SESSION1:
    bot1 = Client(session_name= STRING_SESSION1, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="levanter"))
else:
    bot1 = None

if STRING_SESSION2:
    bot2 = Client(session_name= STRING_SESSION2, api_id = API_ID, api_hash = API_HASH , plugins=dict(root="levanter"))
else:
    bot2 = None

scheduler = AsyncIOScheduler()
CMD_HELP = {}
START_TIME = datetime.now()

if bot1:
    bot1.start()
    bot1.join_chat("beta_botz")
    bot1.send_message(chat_id=message.chat.id, text="Laventar Has Started \nType  .alive To Check I'M Alive \nType .help To Know My Commands)
if bot2:
    bot2.start()
    bot2.join_chat("beta_botz")
    bot2.send_message(chat_id=message.chat.id, text="Laventar Has Started \nType  .alive To Check I'M Alive \nType .help To Know My Commands)

idle()

print("🎉 Successfully Deployed Levanter")
print("Enjoy! Your Userbot Has Started Successfully")
