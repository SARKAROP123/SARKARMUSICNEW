from pyrogram.types import InlineKeyboardButton

import config
from config import SUPPORT_GROUP
from VIPMUSIC import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❍𝐀𝙳𝙳 𝙼𝙴 𝙸𝙽 𝙽𝙴𝚆 𝙶𝚁𝙾𝚄𝙿𝚂❍",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text="❍ 𝐇𝙴𝙻𝙿 ❍", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="❍ 𝐒ҽƚƚιɳɠ𝐒❍", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="", url=config.SUPPORT_GROUP),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❍ 𝐀ᴅᴅ 𝐌ᴇ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ ❍",
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐘ᴏᴜʀ 𝐇ᴇʟᴘᴇʀ ❍",
                callback_data="settings_back_helper",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐎ᴡɴᴇʀ ❍",
                url=f"https://t.me/ll_SARKAR_MERA_BABU_ll",
            ),
            InlineKeyboardButton(
                text="❍ 𝐀ʟʟ 𝐁ᴏᴛs ❍",
                url=f"https://t.me/TG_NAME_STYLE/4368",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐏𝐑𝐎𝐌𝐎𝐓𝐈𝐎𝐍 𝐀𝐕𝐀𝐈𝐋𝐀𝐁𝐋𝐄 ❍",
                url=f"https://t.me/TG_NAME_STYLE/4602",
            ),
        ],
        [
            InlineKeyboardButton(
                text="❍ 𝐌𝐀𝐍𝐀𝐆𝐄𝐌𝐄𝐍𝐓 ❍",
                url=f"help_back",
            ),
        ],
    ]
    return buttons


def alive_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="❍✿︎ ᴀᴅᴅ ᴍᴇ ✿︎❍", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}"),
        ],
    ]
    return buttons
                 
