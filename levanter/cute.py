 
from pyrogram import *
from pyrogram.types import *
from helpers.basic import edit_or_reply
 
import asyncio
from levanter.help import *
 
 
@Client.on_message(filters.me & (filters.command(["cute"], ["."]) | filters.regex("^cute"))) 
async def hello_world(client: Client, message: Message):
    mg = await message.edit("π²πππ΄")
    await asyncio.sleep(0.2)
    await mg.edit("π²πππ΄ π²πππ΄")
    await asyncio.sleep(0.2)
    await mg.edit("π²πππ΄ π²πππ΄ π²πππ΄")
    await asyncio.sleep(0.2) 
    await mg.edit("π²πππ΄ π²πππ΄ π²πππ΄ π²πππ΄")
    await asyncio.sleep(0.2) 
    await mg.edit("ππΎ π²πππ΄")
    await asyncio.sleep(0.2) 
    await mg.edit("ππΎ ππΎ π²πππ΄ π²πππ΄") 
    await asyncio.sleep(0.2) 
    await mg.edit("π°π½π³") 
    await asyncio.sleep(0.2) 
    await mg.edit("πΎπ½π»π π²πππ΄ ππΎ π²πππ΄")


add_command_help(
    "cute",
    [
        [".cute", "Random editing Reply."],
    ],
)
