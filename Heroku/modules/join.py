import asyncio

from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant, FloodWait

from Heroku import ASSUSERNAME
from Heroku.setup.decorators import sudo_users_only, errors
from Heroku.setup.administrator import adminsOnly
from Heroku.setup.filters import command
from Heroku.calls import client as USER


@Client.on_message(
    command(["userbotjoin", "botjoin", "join"]) & ~filters.private & ~filters.bot
)
@errors
async def addchannel(client, message):
    if message.sender_chat:
        return await message.reply_text(
            "🔴 __You're an **Anonymous Admin**!__\n│\n╰ Revert back to user account from admin rights."
        )
    permission = "can_delete_messages"
    m = await adminsOnly(permission, message)
    if m == 1:
        return
    chid = message.chat.id
    try:
        invite_link = await message.chat.export_invite_link()
        if "+" in invite_link:
            kontol = (invite_link.replace("+", "")).split("t.me/")[1]
            link_bokep = f"https://t.me/joinchat/{kontol}"
    except:
        await message.reply_text(
            "**Add me admin first**",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = f"{ASSUSERNAME}"

    try:
        await USER.join_chat(link_bokep)
    except UserAlreadyParticipant:
        await message.reply_text(
            f"🔴 **{user.first_name} already join this group !!**",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"❌ **Assistant ({user.first_name}) can't join your group due to many join requests for userbot!**\n‼️ Make sure the user is not banned in the group."
            f"\n\n» `Manually add the {user.first_name} to your group`",
        )
        return


@USER.on_message(filters.group & command(["userbotleave", "odaleave", "odaleft"]))
async def rem(USER, message):
    if message.sender_chat:
        return await message.reply_text(
            "🔴 __You're an **Anonymous Admin**!__\n│\n╰ Revert back to user account from admin rights."
        )
    permission = "can_delete_messages"
    m = await adminsOnly(permission, message)
    if m == 1:
        return
    try:
        await USER.send_message(
            message.chat.id,
            "✅ ᴜsᴇʀʙᴏᴛ ʟᴇғᴛ ᴛʜᴇ ᴄʜᴀᴛ....",
        )
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            "❌ **Assistant can't leave your group! probably waiting for floodwaits**\n\n» Manually remove me from your group</b>"
        )

        return


@Client.on_message(command(["userbotleaveall", "leaveall"]))
@sudo_users_only
async def bye(client, message):
    left = 0
    sleep_time = 0.1
    lol = await message.reply("**Assistant leaving all groups**\n\n`Processing...`")
    async for dialog in USER.iter_dialogs():
        try:
            await USER.leave_chat(dialog.chat.id)
            await asyncio.sleep(sleep_time)
            left += 1
        except FloodWait as e:
            await asyncio.sleep(int(e.x))
        except Exception:
            pass
    await lol.edit(f"🏃‍♂️ `Assistant leaving...`\n\n» **Left:** {left} chats.")
