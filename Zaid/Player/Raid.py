
#
# Copyright (C) 2022-2023 by Rexoma@Github, < https://github.com/Rexoma >.

import asyncio
import random
import asyncio
import time
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram import filters
from Zaid.main import bot as Client
from config import SUDO_USERS
from Zaid.data import RAID, GROUP, DEADLYSPAM
from traceback import format_exc
from typing import Tuple

def get_user(message: Message, text: str) -> [int, str, None]:
    """Get User From Message"""
    if text is None:
        asplit = None
    else:
        asplit = text.split(" ", 1)
    user_s = None
    reason_ = None
    if message.reply_to_message:
        user_s = message.reply_to_message.from_user.id
        reason_ = text if text else None
    elif asplit is None:
        return None, None
    elif len(asplit[0]) > 0:
        if message.entities:
            if len(message.entities) == 1:
                required_entity = message.entities[0]
                if required_entity.type == "text_mention":
                    user_s = int(required_entity.user.id)
                else:
                    user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        else:
            user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        if len(asplit) == 2:
            reason_ = asplit[1]
    return user_s, reason_


async def edit_or_send_as_file(
    text: str,
    message: Message,
    client: Client,
    caption: str = "`Result!`",
    file_name: str = "result",
    parse_mode="md",
):
    """Send As File If Len Of Text Exceeds Tg Limit Else Edit Message"""
    if not text:
        await message.edit("`Wait, What?`")
        return
    if len(text) > 1024:
        await message.edit("`OutPut is Too Large, Sending As File!`")
        file_names = f"{file_name}.text"
        open(file_names, "w").write(text)
        await client.send_document(message.chat.id, file_names, caption=caption)
        await message.delete()
        if os.path.exists(file_names):
            os.remove(file_names)
        return
    else:
        return await message.edit(text, parse_mode=parse_mode)

def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["raid"], [".", "!", "/"]))
async def raid(client: Client, message: Message):       
    sex = await message.reply_text("`Processing..`")
    quantity = message.command[1]
    text_ = get_text(message)
    spam_text = ' '.join(message.command[2:])
    user, reason = get_user(message, spam_text)
    failed = 0 
    try:
        userz = await client.get_users(user)
    except:
        await sex.edit(f"`404 : User Doesn't Exists In This Chat !`")
        return            
    if not text_:
        await sex.edit("`Who Should I Raid? You?`")
        return
    raid = random.choice(RAID) 
    uhm = f"[{userz.first_name}](tg://user?id={userz.id}) {raid}"
    quantity = int(quantity)

    if int(message.chat.id) in GROUP:
        await sex.edit("`You Can't spam there!`")
        return
    if int(userz) in DEADLYSPAM:
        await sex.edit("`You Can't!`")
        return    
    for _ in range(quantity):
        await asyncio.sleep(2)
        try:
            await client.send_message(message.chat.id, uhm)            
        except FloodWait as e:
            await asyncio.sleep(e.x)

