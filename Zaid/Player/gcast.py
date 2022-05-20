from pyrogram import filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from config import SUDO_USERS
from Zaid.main import Test, bot as Client

@Client.on_message(filters.command(["gcast", "broadcast"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        lol = await message.reply("`Globally Broadcasting Msg...`")
        if not message.reply_to_message:
            await lol.edit("Usage: /gcast for bot\n /agcast broadcast By assistant\n\n**Reply to any text message for gcast**")
            return
        msg = message.reply_to_message.text
        sent=0
        failed=0
        for dialog in client.iter_dialogs():
            try:
                await client.send_message(dialog.chat.id, msg)
                sent += 1
                await lol.edit(f"**Successfully Send Message To** `{sent}` **Group, Failed to Send Message To** `{failed}` **Group**")
            except:
                failed += 1
                await lol.edit(f"**Successfully Send Message To** `{sent}` **Group, Failed to Send Message To** `{failed}` **Group**")
            await asyncio.sleep(0.7)
        await message.reply_text(f"**Send Message To** `{sent}` **Group, Failed to Send Message To** `{failed}` **Group**")





@Test.on_message(filters.command(["broadcast_assistant", "agcast"]))
async def bye(client: Test, message):
    if message.from_user.id in SUDO_USERS:
        lol = await message.reply("`Globally Broadcasting Msg...`")
        if not message.reply_to_message:
            await lol.edit("**Reply to any text message for gcast**")
            return
        msg = message.reply_to_message.text
        sent=0
        failed=0
        for dialog in client.iter_dialogs():
            try:
                await client.send_message(dialog.chat.id, msg)
                sent += 1
                await lol.edit(f"**Successfully Send Message To** `{sent}` **Group, Failed to Send Message To** `{failed}` **Group**")
            except:
                failed += 1
                await lol.edit(f"**Successfully Send Message To** `{sent}` **Group, Failed to Send Message To** `{failed}` **Group**")
            await asyncio.sleep(0.7)
        await message.reply_text(f"**Send Message To** `{sent}` **Group, Failed to Send Message To** `{failed}` **Group**")
