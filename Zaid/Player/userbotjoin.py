import asyncio
from config import BOT_USERNAME, SUDO_USERS
from Zaid.decorators import authorized_users_only, sudo_users_only, errors
from Zaid.filters import command, other_filters
from Zaid.main import Test as USER
from pyrogram import filters
from Zaid.main import bot as Client, bot as app
from pyrogram.errors import UserAlreadyParticipant
from Zaid.Client.assistant import get_assistant_details, random_assistant
from Zaid.Database.active import get_active_chats


@Client.on_message(command("joinassistant", "userbotjoin"))
@sudo_users_only
async def basffy(client: app, message):
    if len(message.command) != 2:
        await message.reply_text(
            "**Usage:**\n/joinassistant [Chat Username or Chat ID]"
        )
        return
    chat = message.text.split(None, 2)[1]
    try:
        chat_id = (await app.get_chat(chat)).id
    except:
        return await message.reply_text(
            "Add Bot to this Chat First.. Unknown Chat for the bot"
        )
    _assistant = await get_assistant(chat_id, "assistant")
    if not _assistant:
        return await message.reply_text(
            "No Pre-Saved Assistant Found.\n\nYou can set Assistant Via /play inside {Chat}'s Group"
        )
    else:
        ran_ass = _assistant["saveassistant"]
    ASS_ID, ASS_NAME, ASS_USERNAME, ASS_ACC = await get_assistant_details(
        ran_ass
    )
    try:
        await ASS_ACC.join_chat(chat_id)
    except Exception as e:
        await message.reply_text(f"Failed\n**Possible reason could be**:{e}")
        return
    await message.reply_text("Joined.")


@app.on_message(filters.command("leavebot") & filters.user(SUDO_USERS))
async def baaaf(_, message):
    if len(message.command) != 2:
        await message.reply_text(
            "**Usage:**\n/leavebot [Chat Username or Chat ID]"
        )
        return
    chat = message.text.split(None, 2)[1]
    try:
        await app.leave_chat(chat)
    except Exception as e:
        await message.reply_text(f"Failed\n**Possible reason could be**:{e}")
        print(e)
        return
    await message.reply_text("Bot has left the chat successfully")


@app.on_message(filters.command("leaveassistant") & filters.user(SUDO_USERS))
async def baujaf(_, message):
    if len(message.command) != 2:
        await message.reply_text(
            "**Usage:**\n/leave [Chat Username or Chat ID]"
        )
        return
    chat = message.text.split(None, 2)[1]
    try:
        chat_id = (await app.get_chat(chat)).id
    except:
        return await message.reply_text(
            "Add Bot to this Chat First.. Unknown Chat for the bot"
        )
    _assistant = await get_assistant(chat, "assistant")
    if not _assistant:
        return await message.reply_text(
            "No Pre-Saved Assistant Found.\n\nYou can set Assistant Via /play inside {Chat}'s Group"
        )
    else:
        ran_ass = _assistant["saveassistant"]
    ASS_ID, ASS_NAME, ASS_USERNAME, ASS_ACC = await get_assistant_details(
        ran_ass
    )
    try:
        await ASS_ACC.leave_chat(chat_id)
    except Exception as e:
        await message.reply_text(f"Failed\n**Possible reason could be**:{e}")
        return
    await message.reply_text("Left.")


@Client.on_message(command(["leaveall", f"leaveall@{BOT_USERNAME}"]))
@sudo_users_only
async def leave_all(client, message):
    if message.from_user.id not in SUDO_USERS:
        return

    left = 0
    failed = 0
    lol = await message.reply("🔄 **userbot** leaving all chats !")
    async for dialog in USER.iter_dialogs():
        try:
            await USER.leave_chat(dialog.chat.id)
            left += 1
            await lol.edit(
                f"Userbot leaving all group...\n\nLeft: {left} chats.\nFailed: {failed} chats."
            )
        except BaseException:
            failed += 1
            await lol.edit(
                f"Userbot leaving...\n\nLeft: {left} chats.\nFailed: {failed} chats."
            )
        await asyncio.sleep(0.7)
    await client.send_message(
        message.chat.id, f"✅ Left from: {left} chats.\n❌ Failed in: {failed} chats."
    )
