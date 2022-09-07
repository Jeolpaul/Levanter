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
        Alive_msg = f"𝐋𝐀𝐕𝐄𝐍𝐓𝐀𝐑 𝐈𝐒 𝐀𝐋𝐈𝐕𝐄 𝐁𝐀𝐁𝐘 💘\n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► Vᴇʀsɪᴏɴ : `Beta.0.1` \n"
        Alive_msg += f"► ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ : `{pyro_vr}` \n"
        Alive_msg += f"► Aᴄᴛɪᴠᴇ IDs : `{ids}` \n"
        Alive_msg += f"► ꜱᴏᴜʀᴄᴇ : [ʟᴀᴠᴇɴᴛᴀʀ](https://github.com/Jeolpaul/Levanter) \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo=ALIVE_PIC,
        caption=Alive_msg,
        reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "• 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 •", url="https://t.me/beta_botz")
                ],[
                    InlineKeyboardButton(
                        "• 𝐑𝐞𝐩𝐨 •", url="https://github.com/Jeolpaul/Levanter")
                ]],
        ),
    ) 
    except Exception as lol:         
        Alive_msg = f"𝐋𝐀𝐕𝐄𝐍𝐓𝐀𝐑 𝐈𝐒 𝐀𝐋𝐈𝐕𝐄 𝐁𝐀𝐁𝐘 💘\n\n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"► Vᴇʀsɪᴏɴ : `Beta.0.1` \n"
        Alive_msg += f"► ᴘʏʀᴏ ᴠᴇʀsɪᴏɴ : `{pyro_vr}` \n"
        Alive_msg += f"► Aᴄᴛɪᴠᴇ IDs : `{ids}` \n"
        Alive_msg += f"► ꜱᴏᴜʀᴄᴇ : [ʟᴀᴠᴇɴᴛᴀʀ](https://github.com/Jeolpaul/Levanter) \n"
        Alive_msg += f"◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(
        photo=ALIVE_PIC,
        caption=Alive_msg,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 •", url="https://t.me/beta_botz"),
                ],[
                    InlineKeyboardButton("• 𝐑𝐞𝐩𝐨 •", url="https://github.com/Jeolpaul/Levanter"),
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
