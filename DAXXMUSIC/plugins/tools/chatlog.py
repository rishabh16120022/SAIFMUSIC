import random
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import LOGGER_ID as LOG_GROUP_ID
from DAXXMUSIC import app 
from pyrogram.errors import RPCError
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
import asyncio, os, aiohttp
from pathlib import Path
from pyrogram.enums import ParseMode

photo = [
    "https://telegra.ph/file/b0ee2d9161f0c4436dd3a.jpg",
    "https://telegra.ph/file/b0ee2d9161f0c4436dd3a.jpg",
    "https://telegra.ph/file/b0ee2d9161f0c4436dd3a.jpg",
    "https://telegra.ph/file/b0ee2d9161f0c4436dd3a.jpg",
    "https://telegra.ph/file/b0ee2d9161f0c4436dd3a.jpg",
    "https://telegra.ph/file/b0ee2d9161f0c4436dd3a.jpg",
]

@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(chat.id)
    for member in message.new_chat_members:
        if member.id == app.id:
            count = await app.get_chat_members_count(chat.id)
            msg = (
                f"📝 ᴍᴜsɪᴄ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ\n\n"
                f"____________________________________\n\n"
                f"📌 𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ: {chat.title}\n"
                f"🍂 𝐂ʜᴀᴛ 𝐈ᴅ: {chat.id}\n"
                f"🔐 𝐂ʜᴀᴛ 𝐔sᴇʀɴᴀᴍᴇ: @{chat.username}\n"
                f"🛰 𝐂ʜᴀᴛ 𝐋ɪɴᴋ: [ᴄʟɪᴄᴋ]({link})\n"
                f"📈 𝐆ʀᴏᴜᴘ 𝐌ᴇᴍʙᴇʀs: {count}\n"
                f"🤔 𝐀ᴅᴅᴇᴅ 𝐁ʏ: {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(f"𝐒ᴇᴇ 𝐆ʀᴏᴜᴘ 👀", url=f"{link}")]
            ]))

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"✫ <b><u>#𝐋ᴇғᴛ_𝐆ʀᴏᴜᴘ</u></b> ✫\n\n𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ : {title}\n\n𝐂ʜᴀᴛ 𝐈ᴅ : {chat_id}\n\n𝐑ᴇᴍᴏᴠᴇᴅ 𝐁ʏ : {remove_by}\n\n𝐁ᴏᴛ : @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)
        
