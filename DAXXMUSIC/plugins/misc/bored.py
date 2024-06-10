from pyrogram import Client, filters
import requests
from DAXXMUSIC import app

# URL for the Bored API
bored_api_url = "https://apis.scrimba.com/bored/api/activity"


# Function to handle /bored command
@app.on_message(filters.command("bored", prefixes="/"))
async def bored_command(client, message):
    # Fetch a random activity from the Bored API
    response = requests.get(bored_api_url)
    if response.status_code == 200:
        data = response.json()
        activity = data.get("ᴀᴄᴛɪᴠɪᴛʏ")
        if activity:
            # Send the activity to the user who triggered the command
            await message.reply(f"𝗮𝘄𝘄 𝗙𝗲𝗲𝗹𝗶𝗻𝗴 𝗕𝗼𝗮𝗿𝗲𝗱? 𝗛𝗼𝘄 𝗔𝗯𝗼𝘂𝘁:\n\n {activity}")
        else:
            await message.reply("𝗦𝗲𝗱 𝗡𝗼 𝗔𝗰𝘁𝗶𝘃𝗶𝘁𝘆 𝗙𝗼𝘂𝗻𝗱.")
    else:
        await message.reply("𝗢𝗼𝗽𝘀 𝗙𝗮𝗶𝗹𝗲𝗱 𝘁𝗼 𝗙𝗲𝘁𝗰𝗵 𝗔𝗰𝘁𝗶𝘃𝗶𝘁𝘆.")
