import asyncio
import datetime
from VIPMUSIC import app
from pyrogram import Client
from VIPMUSIC.utils.database import get_served_chats
from config import PING_IMG_URL, AUTO_GCAST_MSG, AUTO_GCAST, LOGGER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

AUTO_GCASTS = f"{AUTO_GCAST}" if AUTO_GCAST else True


MESSAGE = f"""**𝐏ᴀɪᴅ 𝐏ʀᴏᴍᴏᴛɪᴏɴ 𝐀ᴠᴀɪʟᴀʙʟᴇ 𝐕ɪᴀ 𝐌ᴜsɪᴄ 𝐁ᴏᴛs

[𝐂ʜᴀᴛᴛɴɢ 𝐆ʀᴏᴜᴘs 𝐂ᴏʟᴏʀ 𝐓ʀᴀᴅɪɴɢ 𝐆ᴀᴍᴇs, 𝐂ʜᴀɴɴᴇʟs, 𝐁ᴇᴛᴛɪɴɢ, 𝐀ᴅs 𝐀ɴʏᴛʜɪɴɢ]

𝐏ʀᴏᴍᴏᴛᴇ 𝐀ɴʏᴛʜɪɴɢ 𝐘ᴏᴜ 𝐖ᴀɴᴛ 𝐎ɴ 𝐎ᴜʀ 𝐏ʟᴀᴛғᴏʀᴍ 𝐖ɪᴛʜ 𝐁ᴇsᴛ 𝐑ᴇsᴜʟᴛs.
𝐃ᴀɪʟʏ, 𝐖ᴇᴇᴋʟʏ, 𝐌ᴏɴᴛʜʟʏ, 𝐏ʟᴀɴs 𝐀ᴠɪᴀɪʟᴀʙʟᴇ.

𝐃ᴍ @ll_SARKAR_MERA_BABU_ll"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("➻𝐌ᴏʀᴇ 𝐈ɴғᴏ 𝐃ᴍ 𝐌ᴇ", url=f"https://t.me/ll_SARKAR_MERA_BABU_ll")
        ]
    ]
)

caption = f"""{AUTO_GCAST_MSG}""" if AUTO_GCAST_MSG else MESSAGE

TEXT = """**ᴀᴜᴛᴏ ɢᴄᴀsᴛ ɪs ᴇɴᴀʙʟᴇᴅ sᴏ ᴀᴜᴛᴏ ɢᴄᴀsᴛ/ʙʀᴏᴀᴅᴄᴀsᴛ ɪs ᴅᴏɪɴ ɪɴ ᴀʟʟ ᴄʜᴀᴛs ᴄᴏɴᴛɪɴᴜᴏᴜsʟʏ. **\n**ɪᴛ ᴄᴀɴ ʙᴇ sᴛᴏᴘᴘᴇᴅ ʙʏ ᴘᴜᴛ ᴠᴀʀɪᴀʙʟᴇ [ᴀᴜᴛᴏ_ɢᴄᴀsᴛ = (ᴋᴇᴇᴘ ʙʟᴀɴᴋ & ᴅᴏɴᴛ ᴡʀɪᴛᴇ ᴀɴʏᴛʜɪɴɢ)]**"""

async def send_text_once():
    try:
        await app.send_message(LOGGER_ID, TEXT)
    except Exception as e:
        pass

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await app.send_photo(chat_id, photo=PING_IMG_URL, caption=caption, reply_markup=BUTTON)
                    await asyncio.sleep(3)  # Sleep for 100 second between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats

async def continuous_broadcast():
    await send_text_once()  # Send TEXT once when bot starts

    while True:
        if AUTO_GCAST:
            try:
                await send_message_to_chats()
            except Exception as e:
                pass

        # Wait for 10000 seconds before next broadcast
        await asyncio.sleep(10000)

# Start the continuous broadcast loop if AUTO_GCAST is True
if AUTO_GCAST:  
    asyncio.create_task(continuous_broadcast())
