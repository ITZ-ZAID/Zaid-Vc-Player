# Copyright (c) 2021 @Bruh_0x

import heroku3
import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message

from Music import BOT_USERNAME
from Music import client as ZAIDUB

# To Block a PM'ed User
@ZAIDUB.on_message(filters.private & filters.command("block", [".", "/"]) & filters.me & ~filters.edited)
async def ubblock(_, message: Message):
  shit_id = message.chat.id
  gonna_block_u = await message.edit_text("`Blocking User...`")
  try:
    await ZAIDUB.block_user(shit_id)
    await gonna_block_u.edit("`Successfully Blocked This User`")
  except Exception as lol:
    await gonna_block_u.edit(f"`Can't Block This Guy! May be this is durov?` \n\n**Error:** `{lol}`")


# To Unblock User That Already Blocked
@ZAIDUB.on_message(filters.command("unblock", [".", "/"]) & filters.me & ~filters.edited)
async def ubblock(_, message: Message):
  good_bro = int(message.command[1])
  gonna_unblock_u = await message.edit_text("`Unblocking User...`")
  try:
    await ZAIDUB.unblock_user(good_bro)
    await gonna_unblock_u.edit(f"`Successfully Unblocked The User` \n**User ID:** `{good_bro}`")
  except Exception as lol:
    await gonna_unblock_u.edit(f"`Can't Unblock That Guy!, I think he is still dumb!` \n\n**Error:** `{lol}`")


# To Get How Many Chats that you are in (PM's also counted)
@ZAIDUB.on_message(filters.private & filters.command("chats", [".", "/"]) & filters.me & ~filters.edited)
async def ubgetchats(_, message: Message):
  getting_chats = await message.edit_text("`Checking Your Chats, Hang On...`")
  async for dialog in ZAIDUB.iter_dialogs():
    try:
      total = await ZAIDUB.get_dialogs_count()
      await getting_chats.edit(f"**Total Dialogs Counted:** `{total}` \n\n**Not Stable Lol**")
    except Exception as lol:
      brokenmsg = await message.reply_text(f"`Never Gonna Give You Up!, but Something Went Wrong!`")
      await brokenmsg.edit(f"**Error:** `{lol}`")


# Leave From a Chat
@ZAIDUB.on_message(filters.command("kickme", [".", "/"]) & filters.me & ~filters.edited)
async def ubkickme(_, message: Message):
  i_go_away = await message.edit_text("`Leaving This Chat...`")
  try:
    await ZAIDUB.leave_chat(message.chat.id)
    await i_go_away.edit("`Successfully Leaved This Chat!`")
  except Exception as lol:
    await i_go_away.edit(f"`Can't Leave This Chat!, What a cruel world!` \n\n**Error:** `{lol}`")


# Alive Message
@ZAIDUB.on_message(filters.command("alive", [".", "/"]) & filters.me & ~filters.edited)
async def ubalive(_, message: Message):
  alive_msg = await message.edit_text("`Processing...`")
  alive_pic = "https://telegra.ph/file/f8a9af2ad589946130da1.jpg"
  await message.reply_photo(alive_pic, caption=f"**☑️ Zaid Music Userbot is Alive 🌀** \n\n**🤖 Version** \n ↳**Bot Version:** `2.5` \n ↳**Userbot Version:** `0.0` \n\n**🐬 Info**\n ↳**Music Bot:** @{BOT_USERNAME} \n ↳**Owner:** [Click Here](tg://user?id=1669178360)")
  await alive_msg.delete()
