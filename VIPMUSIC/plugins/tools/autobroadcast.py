import asyncio

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import AUTO_GCAST, AUTO_GCAST_MSG, LOG_GROUP_ID
from VIPMUSIC import app
from VIPMUSIC.utils.database import get_served_chats

# Convert AUTO_GCAST to boolean based on "On" or "Off"
AUTO_GCASTS = AUTO_GCAST.strip().lower() == "on"

START_IMG_URLS = "https://graph.org/file/099a1a58e21a817bd163b-1f4320a432bf0724c2.jpg"

MESSAGE = f"""๏꯭ P꯭ᴀɪ꯭ᴅ꯭ P꯭ʀ꯭ᴏ꯭ᴍ꯭ᴏ꯭ᴛ꯭ɪ꯭ᴏɴ꯭s꯭꯭ ꯭ᴀᴠ꯭ᴀɪ꯭ʟᴀ꯭ʙ꯭ʟ꯭ᴇ 

➻ Pʀᴏᴍᴏᴛᴇ ᴄʜᴀᴛᴛɪɴɢ ɢʀᴏᴜᴘs, ᴄᴏʟᴏᴜʀ ᴛʀᴀᴅɪɴɢ ɢᴀᴍᴇs, ᴄʜᴀɴɴᴇʟs, ʙᴇᴛᴛɪɴɢ ᴀᴅs ᴏʀ ᴀɴʏᴛʜɪɴɢ. 
๏ ᴅᴀɪʟʏ , ᴡᴇᴇᴋʟʏ , ᴍᴏɴᴛʜʟʏ ᴘʟᴀɴs ᴀᴠᴀɪʟᴀʙʟᴇ. 

➻ᴄᴏɴᴛᴀᴄᴛ: @ll_SARKAR_MERA_BABU_ll"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "➻𝐌ᴏʀᴇ 𝐈ɴғᴏ 𝐃ᴍ 𝐌ᴇ",
                url=f"https://t.me/ll_SARKAR_MERA_BABU_ll",
            )
        ]
    ]
)

caption = f"""{AUTO_GCAST_MSG}""" if AUTO_GCAST_MSG else MESSAGE

TEXT = """**ᴀᴜᴛᴏ ɢᴄᴀsᴛ ɪs ᴇɴᴀʙʟᴇᴅ sᴏ ᴀᴜᴛᴏ ɢᴄᴀsᴛ/ʙʀᴏᴀᴅᴄᴀsᴛ ɪs ᴅᴏɪɴɢ ɪɴ ᴀʟʟ ᴄʜᴀᴛs ᴄᴏɴᴛɪɴᴜᴏᴜsʟʏ.**\n**ɪᴛ ᴄᴀɴ ʙᴇ sᴛᴏᴘᴘᴇᴅ ʙʏ ᴘᴜᴛ ᴠᴀʀɪᴀʙʟᴇ [ᴀᴜᴛᴏ_ɢᴄᴀsᴛ = (Off)]**"""


async def send_text_once():
    try:
        await app.send_message(LOG_GROUP_ID, TEXT)
    except Exception as e:
        pass


async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get("chat_id")
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await app.send_photo(
                        chat_id,
                        photo=START_IMG_URLS,
                        caption=caption,
                        reply_markup=BUTTON,
                    )
                    await asyncio.sleep(
                        20
                    )  # Sleep for 20 seconds between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats


async def continuous_broadcast():
    await send_text_once()  # Send TEXT once when bot starts

    while True:
        if AUTO_GCASTS:
            try:
                await send_message_to_chats()
            except Exception as e:
                pass

        # Wait for 10000 seconds before next broadcast
        await asyncio.sleep(10000)


# Start the continuous broadcast loop if AUTO_GCASTS is True
if AUTO_GCASTS:
    asyncio.create_task(continuous_broadcast())
