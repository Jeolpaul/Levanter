from pyrogram import Client
from config import *

class App(JP):

    def __init__(self):
        super().__init__(
            "userbot",
            api_id=API_ID,
            api_hash=API_HASH,
            string_session=STRING_SESSION,
            plugins={"root": ""},
        )
