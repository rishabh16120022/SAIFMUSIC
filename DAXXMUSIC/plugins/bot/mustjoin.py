
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from DAXXMUSIC import app

#--------------------------

MUST_JOIN = "@infinitelovefeelboyxd"
#------------------------
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://telegra.ph/file/b0ee2d9161f0c4436dd3a.jpg", caption=f"๏ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ ʏᴏᴜ'ᴠᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ [ ➣𝐒ᴜᴘᴘᴏʀᴛ](https://t.me/infinitelovefeelboyxd) ʏᴇᴛ, ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ᴍᴇ ᴛʜᴇɴ ᴊᴏɪɴ [➥ 𝐒ᴜᴘᴘᴏʀᴛ](https://t.me/Stylish_Bio_Dp_0) ᴀɴᴅ sᴛᴀʀᴛ ʜᴜɴɢᴀᴍᴀ ʙᴏᴛ ᴀɢᴀɪɴ ᴛʜɪs ʀᴇᴘᴏ ɪs ᴍᴀᴅᴇ ʙʏ [⚡ ɴɪᴄᴋ ⚡](https://t.me/Niksonfire)! ",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("๏ 𝐉ᴏɪɴ ๏", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"๏ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴍᴜsᴛ_Jᴏɪɴ ᴄʜᴀᴛ ๏: {MUST_JOIN} !")
