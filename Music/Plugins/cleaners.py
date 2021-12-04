from Music import app, SUDOERS
from pyrogram import filters, Client
from pyrogram.types import Message
from Music.MusicUtilities.helpers.filters import command
import subprocess
import shutil
import os
   
    
@Client.on_message(command("rmr") & filters.user(SUDOERS))
async def hsjdjs(_, message: Message):    
    dir = 'downloads'
    dir1 = 'search'
    shutil.rmtree(dir)
    shutil.rmtree(dir1)
    os.mkdir(dir)
    os.mkdir(dir1)
    await message.reply_text("Successfully cleaned all **temp** dir(s)!")
