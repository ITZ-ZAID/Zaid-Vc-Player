# @Aman

from Zaid.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) allows you to play music and video on groups through the new Telegram's video chats!**

💡 **Find out all the Bot's commands and how they work by clicking on the » 📚 Commands button!**

🔖 **To know how to use this bot, please click on the » ❓ Basic Guide button!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇꜱ", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton("ꜱᴏᴜʀᴄᴇ", url="https://GitHub.com/Timesisnotwaiting/Zaid-Vc-Player"),
                InlineKeyboardButton("✨ ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{UPDATES_CHANNEL}"),],
                [InlineKeyboardButton("📚 ᴄᴏᴍᴍᴀɴᴅꜱ", callback_data="cbcmds"),
                InlineKeyboardButton("❓ ꜱᴇᴛᴜᴘ", callback_data="cbsetup"),],
                [InlineKeyboardButton(" ᴀᴅᴅ ᴍᴇᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true",)],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Basic Guide for using this bot:**
        

1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**

📌 **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**

💡 **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

**✨ ᴘᴏᴡᴇʀᴅ ʙʏ ɴᴏɪɴᴏɪ ᴍᴜꜱɪᴄ** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **press the button below to read the explanation and see the list of available commands !**

**✗ Pᴏᴡᴇʀᴇᴅ 💕 Bʏ: Tᴇᴀᴍ DᴇCᴏᴅᴇ!** """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 ᴀᴅᴍɪɴ ᴄᴍᴅ", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 ꜱᴜᴅᴏ ᴄᴍᴅ", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 ʙᴀꜱɪᴄ ᴄᴍᴅ", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the basic commands:

➯ /play (song name/link) - play music on video chat
➯ /playlist - show you the playlist
➯ /lyric (query) - scrap the song lyric
➯ /search (query) - search a youtube video link

 **✗ Pᴏᴡᴇʀᴇᴅ 💕!** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the admin commands:

➯ /pause - pause the stream
➯ /resume - resume the stream
➯ /skip - switch to next stream
➯ /stop - stop the streaming
➯ /vmute - mute the userbot on voice chat
➯ /vunmute - unmute the userbot on voice chat
➯ /volume `1-200` - adjust the volume of music (userbot must be admin)
➯ /reload - reload bot and refresh the admin data
➯ /userbotjoin - invite the userbot to join group
➯ /userbotleave - order userbot to leave from group

**✗ Pᴏᴡᴇʀᴇᴅ 💕!** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the sudo commands:

➯ /rmw - clean all raw files
➯ /rmd - clean all downloaded files
➯ /sysinfo - show the system information
➯ /update - update your bot to latest version
➯ /restart - restart your bot
➯ /leaveall - order userbot to leave from all group

**✗ Pᴏᴡᴇʀᴇᴅ 💕!** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **settings of** {query.message.chat.title}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ nothing is currently streaming", show_alert=True)

# SETUP BUTTON OPEN......................................................................................................................................................................................

@Client.on_callback_query(filters.regex("cbsetup"))
async def cbsetup(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Hello !**
» **press the button below to read the explanation and see the help commands !**
**✗ Pᴏᴡᴇʀᴇᴅ 💕!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("welcome", callback_data="donate"),
                    InlineKeyboardButton("Lyric", callback_data="lyricss"),
                    InlineKeyboardButton("voice", callback_data="vcconv"),
                ],
                [
                    InlineKeyboardButton("How To Add Me ❓", callback_data="cbhowtouse"),
                ],
                [InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")],
            ]
        ),
    )
@Client.on_callback_query(filters.regex("donate"))
async def noiwel(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **Welcome to Donate Section ( soon )**

➯ Donate Via UPI/Wallet/netbanking etc 👉:https://rzp.io/l/GODFATHERDONATIONS.

➯ Donate Via PayPal 👉: [Click](https://www.paypal.me/mrakki58)

**✗ Pᴏᴡᴇʀᴇᴅ 💕!** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbsetup")]]
        ),
    )
@Client.on_callback_query(filters.regex("lyricss"))
async def noilyric(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **HEAR THE LYRIC PLUGIN**

➯ /lyric ( song name ) for the get lyric of song

**✗ Pᴏᴡᴇʀᴇᴅ 💕!** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbsetup")]]
        ),
    )
    
@Client.on_callback_query(filters.regex("vcconv"))
async def noivoice(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 **HEAR THE VOICE PLUGIN**

➯ /tts fot get voice from text message

**✗ Pᴏᴡᴇʀᴇᴅ 💕** """,
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbsetup")]]
        ),
    )    

    
@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    await query.message.delete()
