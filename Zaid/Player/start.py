import asyncio
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import MessageNotModified
from Zaid.main import Test, bot as Client
from config import START_PIC, UPDATES_CHANNEL, GROUP_SUPPORT


ALIVE_PIC = START_PIC
HOME_TEXT = "👋🏻 **ᴡᴇʟᴄᴏᴍᴇ [{}](tg://user?id={})** \n\n🤖 ɪᴍ **sʜᴀᴅᴏᴡ ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ**. \n** ɪᴀᴍ ᴀ ɴᴇxᴛ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴍᴜsɪᴄ ʀᴏʙᴏᴛ ᴡɪᴛʜ ᴄᴏʟʟ ғᴇᴀᴛᴜʀᴇs ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ & ᴠɪᴅᴇᴏ & ʀᴀᴅɪᴏ ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ**"
HELP_TEXT = """
🏷️ **sᴇᴛᴜᴘ ɢᴜɪᴅᴇ** :

\u2022 sᴛᴀʀᴛ ᴀ ᴠᴏɪᴄᴇ  ᴄʜᴀᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ.
\u2022 ᴀᴅᴅ ʙᴏᴛ  ɪɴ ᴄʜᴀᴛ ᴡɪᴛʜ ᴀᴅᴍɪɴ ʀɪɢʜᴛs.
\u2022 ᴅᴏɴᴇ sᴇᴛᴜᴘ ᴘʀᴏᴄᴇss ʀᴇᴀᴅ ᴄᴏᴍᴍᴀɴᴅs ʙᴇʟᴏᴡ 👇.
"""



USER_TEXT = """
🏷️ **ᴜsᴇʀs ᴄᴏᴍᴍᴀɴᴅs** :

\u2022 /play <Query> ᴛᴏ ᴘʟᴀʏ ᴀ sᴏɴɢ.
\u2022 /vplay <Query> ᴛᴏ ᴘʟᴀʏ ᴠɪᴅᴇᴏ.
\u2022 /stream <Live Url> ᴛᴏ ᴘʟᴀʏ ʟɪᴠᴇ sᴛʀᴇᴀᴍs 👇\n /song ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀ ᴀᴜᴅɪᴏ ғɪʟᴇ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ. \n /video ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ғʀᴏᴍ ʏᴏᴜᴛᴜʙᴇ\n /lyric ᴛᴏ ғɪɴᴅ sᴏɴɢ.
"""

SPAM_TEXT = """
🏷️ **sᴘᴀᴍ ʜᴇʟᴘ @adminsOnly** :

\u2022 /spam <Count> ᴛᴇxᴛ ᴛᴏ sᴘᴀᴍ ʏᴏᴜʀ ᴍᴇssᴀɢᴇ.
\u2022 /fspam <Count> ᴛᴇxᴛ ғᴏʀ sᴘᴀᴍᴍɪɴɢ.
\u2022 /delayspam <Count> ᴛᴇxᴛ ғᴏʀ sᴘᴀᴍᴍɪɴɢ.
"""

RAID_TEXT = """
🏷️ **ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅs @SudoOnly** :

\u2022 /vcraid <chatid> - ɢɪᴠᴇ ᴀ ᴄʜᴀᴛ ɪᴅ ᴇʟsᴇ ᴜsᴇʀɴᴀᴍᴇ ᴛᴏ ᴠᴏɪᴄᴇ ʀᴀɪᴅ.
\u2022 /vraid <chatid + ʀᴇᴘʟʏ ᴛᴏ ᴠɪᴅᴇᴏ ғɪʟᴇ> - ᴛᴏ ʀᴀɪᴅ ᴠɪᴅᴇᴏ.
\u2022 /raidpause - ᴛᴏ ᴘᴀᴜsᴇ ʀᴀɪᴅ.
\u2022 /raidresume ᴛᴏ ʀᴇsᴜᴍᴇ ʀᴀɪᴅ.
\u2022 /raidend <chatid> ᴛᴏ ᴇɴᴅ ᴀᴜᴅɪᴏ/ᴠɪᴅᴇᴏ ʀᴀɪᴅ.
"""

ADMIN = """
🏷️ **ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs** :

\u2022 /userbotjoin ᴛᴏ ɪɴᴠɪᴛᴇ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ.
\u2022 /end ᴛᴏ ᴇɴᴅ sᴛʀᴇᴀᴍɪɴɢ.
\u2022 /pause ᴛᴏ ᴘᴀᴜsᴇ sᴛʀᴇᴀᴍ.
\u2022 /resume ᴛᴏ ʀᴇsᴜᴍᴇ sᴛʀᴇᴀᴍ.
\u2022 /volume ᴛᴏ sᴇᴛ ᴠᴏʟᴜᴍᴇ.
\u2022 /skip ᴛᴏ sᴋɪᴘ ᴛʀᴀᴄᴋs.
"""

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("ᴀᴅᴍɪɴs", url="https://telegra.ph/𝗕ooo--‌ᴀꜰᴋ-ᴏꜰꜰʟɪɴᴇ-05-17-2"),
                InlineKeyboardButton("ᴜsᴇʀs", callback_data="users"),
            ],
            [
                InlineKeyboardButton("ʀᴀᴅɪᴏ", callback_data="raid"),
                InlineKeyboardButton("sᴘᴀᴍ 👻", callback_data="spam"),
            ],
            [
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="home"),
                InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close"),
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
                InlineKeyboardButton("ᴀᴅᴍɪɴs", url="https://telegra.ph/𝗕ooo--‌ᴀꜰᴋ-ᴏꜰꜰʟɪɴᴇ-05-17-2"),
                InlineKeyboardButton("ᴜsᴇʀs", callback_data="users"),
            ],
            [
                InlineKeyboardButton("ʀᴀᴅɪᴏ", callback_data="raid"),
                InlineKeyboardButton("sᴘᴀᴍ 👻", callback_data="spam"),
            ],
            [
                InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="home"),
                InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo=f"{ALIVE_PIC}", caption=f"{HELP_TEXT}", reply_markup=reply_markup)
