import asyncio, os, time, aiohttp
import aiohttp
from pyrogram import filters
from daxxhub import daxxhub as papadaxx
from DAXXMUSIC import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

###
@app.on_message(filters.command("daxxhub"))
async def daxxhub(_, message):
    text = message.text[len("/daxxhub") :]
    papadaxx(f"{text}").save(f"daxxhub_{message.from_user.id}.png")
    await message.reply_photo(f"daxxhub_{message.from_user.id}.png")
    os.remove(f"daxxhub_{message.from_user.id}.png")
####

@app.on_message(filters.command(["developer", "dev"]))
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("/dev Nick")
        return

    username = message.text.split(None, 1)[1]
    URL = f'https://t.me/niksonfire'

    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()

            try:
                url = result['html_url']
                name = result['name']
                company = result['company']
                bio = result['bio']
                created_at = result['created_at']
                avatar_url = result['avatar_url']
                blog = result['blog']
                location = result['location']
                repositories = result['public_repos']
                followers = result['followers']
                following = result['following']

                caption = f"""𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 𝗜𝗡𝗙𝗢 ✨ {name}
                
𝐔sᴇʀɴᴀᴍᴇ: {username}
𝐁ɪᴏ: {bio}
𝐋ɪɴᴋ: [Here]({url})
𝗼𝘄𝗻𝗲𝗿: [𝗡𝗜𝗖𝗞](https://t.me/niksonfire)"""

            except Exception as e:
                print(str(e))
                pass

    # Create an inline keyboard with a close button
    close_button = InlineKeyboardButton("𝗖𝗟𝗢𝗦𝗲", callback_data="close")
    inline_keyboard = InlineKeyboardMarkup([[close_button]])

    # Send the message with the inline keyboard
    await message.reply_photo(photo=avatar_url, caption=caption, reply_markup=inline_keyboard)
