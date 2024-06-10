import math
from pyrogram.types import InlineKeyboardButton
from DAXXMUSIC import app
import config
from DAXXMUSIC.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        bar = "𝐇𝐞𝐥𝐥𝐨 𝐃𝐞𝐚𝐫🙋‍♂️"
    elif 10 < umm < 20:
        bar = "𝐓𝐡𝐢𝐬 𝐢𝐬 𝐇𝐮𝐧𝐠𝐚𝐦𝐚 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭❤"
    elif 20 <= umm < 30:
        bar = "𝐓𝐡𝐚𝐧𝐤𝐬 𝐅𝐨𝐫 𝐀𝐝𝐝𝐢𝐧𝐠 𝐦𝐞"
    elif 30 <= umm < 40:
        bar = "𝐭𝐨 𝐲𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ❤"
    elif 40 <= umm < 50:
        bar = "𝐈 𝐦 𝐀𝐜𝐭𝐢𝐯𝐞 𝟐𝟒*𝟕"
    elif 50 <= umm < 60:
        bar = "𝐢 𝐰𝐢𝐥𝐥 𝐥𝐞𝐭 𝐮𝐡 𝐟𝐞𝐞𝐥 𝐚𝐧𝐭𝐢𝐥𝐚𝐠 𝐦𝐮𝐬𝐢𝐜❤"
    elif 60 <= umm < 70:
        bar = ""
    elif 70 <= umm < 80:
        bar = "𝐌𝐲 𝐨𝐰𝐧𝐞𝐫 𝐢𝐬 𝐍𝐢𝐜𝐤 ❤"
    elif 80 <= umm < 95:
        bar = "𝐈 𝐡𝐚𝐯𝐞 𝐛𝐞𝐞𝐧 𝐝𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 𝐍𝐢𝐜𝐤❤"
    else:
        bar = "𝐓𝐡𝐚𝐧𝐤 𝐘𝐨𝐮💝"
    buttons = [
                [
            InlineKeyboardButton(
                text="👉🏻")
        ],
        
            
        [ 
            InlineKeyboardButton(text="💥 𝗷𝗼𝗶𝗻 𝗛𝗲𝗿𝗲 & 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 💞",url=f"https://t.me/infinitelovefeelboyxd"),
            InlineKeyboardButton(text="🥀 𝗨𝗣𝗗𝗔𝗧𝗘 𝗖𝗛𝗔𝗡𝗡𝗘𝗟  💞",url=f"https://t.me/Stylish_Bio_Dp_0"),
            InlineKeyboardButton(text="🥀 𝗼𝘄𝗻𝗲𝗿 🥀",url=f"https://t.me/niksonfire"),
        ]
        [
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            
            InlineKeyboardButton(text="💥 ᴊᴏɪɴ Ɦᴇʀᴇ & sᴜᴘᴘᴏʀᴛ 💞",url=f"https://t.me/infinitelovefeelboyxd"),
            InlineKeyboardButton(text="🥀 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ  💞",url=f"https://t.me/Stylish_Bio_Dp_0"),
            InlineKeyboardButton(text="❤ ᴅᴇᴠᴇʟᴏᴘᴇʀ ❤",url=f"https://t.me/niksonfire"),
            InlineKeyboardButton(text="🥀 ᴏᴡɴᴇʀ 🥀",url=f"https://t.me/feel_boy_1"), 
        
        ]
            
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"DAXXPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"DAXXPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="👈🏻",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="👉🏻",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
