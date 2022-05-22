import asyncio
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import MessageNotModified
from Zaid.main import Test, bot as Client
from config import START_PIC, UPDATES_CHANNEL, GROUP_SUPPORT


ALIVE_PIC = START_PIC
HOME_TEXT = "👋🏻 **Hi Sir [{}](tg://user?id={})** \n\n🤖 Im **Zaid Vc Player**. \n**I Can Stream Lives, Radios, Raid, Vc Raid, YouTube Videos & Telegram Video Files On Voice Chat Of Telegram Groups**"
HELP_TEXT = """
🏷️ **Setup Guide** :

\u2022 Start a voice chat in your group.
\u2022 Add bot and user account in chat with admin rights.
\u2022 Done Setup Process Read Commands Below 👇.
"""



USER_TEXT = """
🏷️ **Users Commands** :

\u2022 /play <Query> To Play a Song.
\u2022 /vplay <Query> To Play Video.
\u2022 /stream <Live Url> To Play Live Streams 👇\n /song To Download A Audio file from YouTube. \n /video to download Video From YouTube\n /lyric to find Lyrics.
"""

SPAM_TEXT = """
🏷️ **Spam Help @adminsOnly** :

\u2022 /spam <Count> Text To Spam Your Message.
\u2022 /fspam <Count> Text for spamming.
\u2022 /delayspam <Count> Text for Spamming.
"""

RAID_TEXT = """
🏷️ **Raid Commands @SudoOnly** :

\u2022 /vcraid <chatid> - Give a Chat Id Else Username To Voice Raid.
\u2022 /vraid <chatid + Reply To Video File> - To Raid Video.
\u2022 /raidpause - To Pause Raid.
\u2022 /raidresume To Resume Raid.
\u2022 /raidend <chatid> To End Audio/Video Raid.
"""

ADMIN = """
🏷️ **admin Commands** :

\u2022 /userbotjoin To Invite Assistant To Your Chat.
\u2022 /end To End Streaming.
\u2022 /pause To Pause Stream.
\u2022 /resume To Resume Stream.
\u2022 /volume To Set Volume.
\u2022 /skip To Skip Tracks.
"""

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("👮 Aᴅᴍɪɴꜱ", url="https://telegra.ph/𝗕ooo--‌ᴀꜰᴋ-ᴏꜰꜰʟɪɴᴇ-05-17-2"),
                InlineKeyboardButton("🗨️ Uꜱᴇʀꜱ", callback_data="users"),
            ],
            [
                InlineKeyboardButton("🤬 Rᴀɪᴅ", callback_data="raid"),
                InlineKeyboardButton("🗨️ Sᴘᴀᴍ", callback_data="spam"),
            ],
            [
                InlineKeyboardButton("🤖 Cʟᴏɴᴇʀ", url="t.me/ZaidClonerBot"),
            ],
            [
                InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="home"),
                InlineKeyboardButton("🤷 Cʟᴏꜱᴇ", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="home":
        get_me = await client.get_me()
        USERNAME = get_me.username
        buttons = [
            [
                InlineKeyboardButton("🧐 Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀᴛ", url='https://t.me/{USERNAME}?startgroup=true'),
            ],
            [
                InlineKeyboardButton("💌 Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton("🏷️ Cʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ],
            [
                InlineKeyboardButton("🤖 Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", url="https://github.com/Itz-Zaid/Zaid-Vc-Player"),
            ],
            [
                InlineKeyboardButton("🤔 Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ", callback_data="help"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HOME_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="users":
        buttons = [
            [
                InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("🤷 Cʟᴏꜱᴇ", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                USER_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="admins":
        buttons = [
            [
                InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("🤷 Cʟᴏꜱᴇ", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(ADMIN, reply_markup=reply_markup)
        except MessageNotModified:
            pass

    elif query.data=="raid":
        buttons = [
            [
                InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("🤷 Cʟᴏꜱᴇ", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                RAID_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="spam":
        buttons = [
            [
                InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="help"),
                InlineKeyboardButton("🤷 Cʟᴏꜱᴇ", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                SPAM_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client: Client, message: Message):
    get_me = await client.get_me()
    USERNAME = get_me.username
    buttons = [
            [
                InlineKeyboardButton("🧐 Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀᴛ", url=f'https://t.me/{USERNAME}?startgroup=true'),
            ],
            [
                InlineKeyboardButton("💌 Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton("🏷️ Oꜰꜰɪᴄɪᴀʟ Cʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ],
            [
                InlineKeyboardButton("🤖 Sᴏᴜʀᴄᴇ Cᴏᴅᴇ", url="https://github.com/Itz-Zaid/Zaid-Vc-Player"),
            ],
            [
                InlineKeyboardButton("🤔 Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ", callback_data="help"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo=f"{ALIVE_PIC}", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)

@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client: Client, message: Message):
    get_me = await client.get_me()
    self.username = get_me.username
    buttons = [
            [
                InlineKeyboardButton("👮 Aᴅᴍɪɴꜱ", url="https://telegra.ph/𝗕ooo--‌ᴀꜰᴋ-ᴏꜰꜰʟɪɴᴇ-05-17-2"),
                InlineKeyboardButton("🗨️ Uꜱᴇʀꜱ", callback_data="users"),
            ],
            [
                InlineKeyboardButton("🤬 Rᴀɪᴅ", callback_data="raid"),
                InlineKeyboardButton("🗨️ Sᴘᴀᴍ", callback_data="spam"),
            ],
            [
                InlineKeyboardButton("🤖 Cʟᴏɴᴇʀ", url="t.me/ZaidClonerBot"),
            ],
            [
                InlineKeyboardButton("🔙 Bᴀᴄᴋ", callback_data="home"),
                InlineKeyboardButton("🤷 Cʟᴏꜱᴇ", callback_data="close"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo=f"{ALIVE_PIC}", caption=f"{HELP_TEXT}", reply_markup=reply_markup)
