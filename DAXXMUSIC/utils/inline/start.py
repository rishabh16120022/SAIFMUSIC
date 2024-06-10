from pyrogram.types import InlineKeyboardButton

import config
from DAXXMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton("🥀 𝗦𝗧𝗬𝗟𝗜𝗦𝗛 𝗗𝗣𝗭 𝗔𝗡𝗗 𝗕𝗜𝗢 ✨", url=f"https://t.me/Stylish_Bio_Dp_0"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper"),
        ]
    ]
    return buttons
