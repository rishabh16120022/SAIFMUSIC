from DAXXMUSIC import app
from pyrogram.errors import RPCError
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from os import environ
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
from os import environ
import random
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image, ImageDraw, ImageFont
import asyncio, os, time, aiohttp
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from asyncio import sleep
from pyrogram import filters, Client, enums
from pyrogram.enums import ParseMode
from logging import getLogger
from DAXXMUSIC.utils.daxx_ban import admin_filter
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import *
from pyrogram.types import *
from logging import getLogger


random_photo = [
    "https://telegra.ph/file/559396cd29ee4e847ed5d.jpg",
    "https://telegra.ph/file/d68e3c43f8a1586f903d4.jpg",
    "https://telegra.ph/file/9c89987d2ff15e4a1e3ef.jpg",
    "https://telegra.ph/file/c4a33a06f9b403083c1e3.jpg",
    "https://telegra.ph/file/8e29ab3ee6697978e160a.jpg",
    "https://telegra.ph/file/18605815b97d21199a9de.jpg",
]
# --------------------------------------------------------------------------------- #





LOGGER = getLogger(__name__)

class WelDatabase:
    def __init__(self):
        self.data = {}

    async def find_one(self, chat_id):
        return chat_id in self.data

    async def add_wlcm(self, chat_id):
        if chat_id not in self.data:
            self.data[chat_id] = {"state": "on"}  # Default state is "on"

    async def rm_wlcm(self, chat_id):
        if chat_id in self.data:
            del self.data[chat_id]

wlcm = WelDatabase()

class temp:
    ME = None
    CURRENT = 2
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None



def circle(pfp, size=(500, 500), brightness_factor=10):
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    pfp = ImageEnhance.Brightness(pfp).enhance(brightness_factor)
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def welcomepic(pic, user, chatname, id, uname, brightness_factor=1.3):
    background = Image.open("DAXXMUSIC/assets/wel2.png")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp, brightness_factor=brightness_factor) 
    pfp = pfp.resize((575, 575))
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('DAXXMUSIC/assets/font.ttf', size=70)
    welcome_font = ImageFont.truetype('DAXXMUSIC/assets/font.ttf', size=61)
    #draw.text((630, 540), f'ID: {id}', fill=(255, 255, 255), font=font)
    #
 #   draw.text((630, 300), f'NAME: {user}', fill=(255, 255, 255), font=font)
    draw.text((630, 450), f'ID: {id}', fill=(255, 255, 255), font=font)
#    draw.text((630, 150), f"{chatname}", fill=(225, 225, 225), font=welcome_font)
  #  draw.text((630, 230), f"USERNAME : {uname}", fill=(255, 255, 255), font=font)

    #
    pfp_position = (48, 88)
    background.paste(pfp, pfp_position, pfp)
    background.save(f"downloads/welcome#{id}.png")
    return f"downloads/welcome#{id}.png"


@app.on_message(filters.command("welcome") & ~filters.private)
async def auto_state(_, message):
    usage = "**ᴜsᴀɢᴇ:**\n**⦿ /welcome [on|off]**"
    if len(message.command) == 1:
        return await message.reply_text(usage)
    chat_id = message.chat.id
    user = await app.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in (
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,
    ):
        A = await wlcm.find_one(chat_id)
        state = message.text.split(None, 1)[1].strip().lower()
        if state == "off":
            if A:
                await message.reply_text("**ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ !**")
            else:
                await wlcm.add_wlcm(chat_id)
                await message.reply_text(f"**ᴅɪsᴀʙʟᴇᴅ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ** {message.chat.title}")
        elif state == "on":
            if not A:
                await message.reply_text("**ᴇɴᴀʙʟᴇ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ.**")
            else:
                await wlcm.rm_wlcm(chat_id)
                await message.reply_text(f"**ᴇɴᴀʙʟᴇᴅ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ ** {message.chat.title}")
        else:
            await message.reply_text(usage)
    else:
        await message.reply("**sᴏʀʀʏ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴇɴᴀʙʟᴇ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ!**")



@app.on_chat_member_updated(filters.group, group=-3)
async def greet_new_member(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    count = await app.get_chat_members_count(chat_id)
    A = await wlcm.find_one(chat_id)
    if A:
        return

    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    
    # Add the modified condition here
    if member.new_chat_member and not member.old_chat_member and member.new_chat_member.status != "kicked":
    
        try:
            pic = await app.download_media(
                user.photo.big_file_id, file_name=f"pp{user.id}.png"
            )
        except AttributeError:
            pic = "DAXXMUSIC/assets/upic.png"
        if (temp.MELCOW).get(f"welcome-{member.chat.id}") is not None:
            try:
                await temp.MELCOW[f"welcome-{member.chat.id}"].delete()
            except Exception as e:
                LOGGER.error(e)
        try:
            welcomeimg = welcomepic(
                pic, user.first_name, member.chat.title, user.id, user.username
            )
            button_text = "😻 𝐒𝐞𝐞 𝐧𝐞𝐰 𝐌𝐞𝐦𝐛𝐞𝐫 😻"
            add_button_text = "🥂 𝐊𝐢𝐝𝐧𝐚𝐩 𝐌𝐞 𝐁𝐚𝐛𝐲 😍"
            deep_link = f"tg://openmessage?user_id={user.id}"
            add_link = f"https://t.me/{app.username}?startgroup=true"
            temp.MELCOW[f"welcome-{member.chat.id}"] = await app.send_photo(
                member.chat.id,
                photo=welcomeimg,
                caption=f"""
**♡♡♡♡♡♡🥀 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐡𝐞𝐫𝐞 𝐃𝐞𝐚𝐫 💕 ♡♡♡♡♡♡**
╔════╤╤╤╤════╗
**✨ 𝐍𝐚𝐦𝐞 👉🏻** {user.mention}
**✨ 𝐈𝐃 👉🏻** `{user.id}`
**✨ 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 👉🏻** @{user.username}
**✨ 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 👉🏻** {count}
»»---------------►

**♡♡♡♡♡♡♡♡♡♡♡♡**
""",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(button_text, url=deep_link)],
                    [InlineKeyboardButton(text=add_button_text, url=add_link)],
                ])
            )
        except Exception as e:
            LOGGER.error(e)
