from pyrogram import filters
from pyrogram import __version__ as pyro_vr
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from main import *
from pyrogram import Client
from main import ALIVE_PIC
from levanter.help import *
 

 
@Client.on_message(filters.command(["alive", "awake"], [".", "!"]) & filters.me)
async def alive(client: Client, e: Message):
    ids = 0
    try:
        if bot:
            ids += 1
        Alive_msg = f"๐๐๐๐๐๐๐๐ ๐๐ ๐๐๐๐๐ ๐๐๐๐ ๐\n\n"
        Alive_msg += f"โ โโโโโโ โ โโโโโโ โ \n"
        Alive_msg += f"โบ Vแดสsษชแดษด : `Beta.0.1` \n"
        Alive_msg += f"โบ แดสสแด แด แดสsษชแดษด : `{pyro_vr}` \n"
        Alive_msg += f"โบ Aแดแดษชแด แด IDs : `{ids}` \n"
        Alive_msg += f"โบ ๊ฑแดแดสแดแด : [สแดแด แดษดแดแดส](https://github.com/Jeolpaul/Levanter) \n"
        Alive_msg += f"โ โโโโโโ โ โโโโโโ โ \n\n"
        await e.reply_photo(
        photo=ALIVE_PIC,
        caption=Alive_msg,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("โข ๐๐ฎ๐ฉ๐ฉ๐จ๐ซ๐ญ", url="https://t.me/BETA_SUPPORT"),
            InlineKeyboardButton("โข ๐๐ก๐๐ง๐ง๐๐ฅ", url="https://t.me/Beta_BoTZ")
            ],[            
            InlineKeyboardButton("โข ๐๐๐ฉ๐จ", url="https://github.com/Jeolpaul/Levanter")               
            ]]
            )
        )
    except Exception as lol:         
        Alive_msg = f"๐๐๐๐๐๐๐๐ ๐๐ ๐๐๐๐๐ ๐๐๐๐ ๐\n\n"
        Alive_msg += f"โ โโโโโโ โ โโโโโโ โ \n"
        Alive_msg += f"โบ Vแดสsษชแดษด : `Beta.0.1` \n"
        Alive_msg += f"โบ แดสสแด แด แดสsษชแดษด : `{pyro_vr}` \n"
        Alive_msg += f"โบ Aแดแดษชแด แด IDs : `{ids}` \n"
        Alive_msg += f"โบ ๊ฑแดแดสแดแด : [สแดแด แดษดแดแดส](https://github.com/Jeolpaul/Levanter) \n"
        Alive_msg += f"โ โโโโโโ โ โโโโโโ โ \n\n"
        await e.reply_photo(
        photo=ALIVE_PIC,
        caption=Alive_msg,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("โข ๐๐ก๐๐ง๐ง๐๐ฅ โข", url="https://t.me/beta_botz"),
                ],[
                    InlineKeyboardButton("โข ๐๐๐ฉ๐จ โข", url="https://github.com/Jeolpaul/Levanter"),
                ],
            ],
        ),
    ) 

add_command_help(
    "alive",
    [
        [
            ".alive",
            "This Command for check your bot working or nt",
        ]
    ],
)
