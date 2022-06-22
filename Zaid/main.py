import os
import sys
import random
import asyncio
from config import API_HASH, API_ID, BOT_TOKEN, SESSION_NAME, SESSION2, SESSION3, SESSION4, SESSION5
from pyrogram import Client
from pytgcalls import idle
from pytgcalls import PyTgCalls
from Zaid.Database.clientdb import get_assistant, save_assistant

bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "Zaid.Player"},
)


if not SESSION_NAME:
   ASS_CLI_1 = None
else:   
   ASS_CLI_1 = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)
   

if not SESSION2:
   user = None
else:
   user = Client(SESSION2, api_id=API_ID, api_hash=API_HASH)
   

if not SESSION3:
   user3 = None
else:
   user3 = Client(SESSION3, api_id=API_ID, api_hash=API_HASH)

if not SESSION4:
   user4 = None
else:
   user4 = Client(SESSION4, api_id=API_ID, api_hash=API_HASH)
   

if not SESSION5:
   user5 = None
else:
   user5 = Client(SESSION5, api_id=API_ID, api_hash=API_HASH)


call_py5 = PyTgCalls(user5)

Test = ASS_CLI_1
ASS_CLI_2 = user
call_py = PyTgCalls(ASS_CLI_1)
call_py2 = PyTgCalls(user)
call_py3 = PyTgCalls(user3)
call_py4 = PyTgCalls(user4)
call_py5 = PyTgCalls(user5)

ASSIDS = []
ASSID1 = 0
ASSNAME1 = ""
ASSUSERNAME1 = ""
ASSMENTION1 = ""
ASSID2 = 0
ASSNAME2 = ""
ASSUSERNAME2 = ""
ASSMENTION2 = ""
ASSID3 = 0
ASSNAME3 = ""
ASSUSERNAME3 = ""
ASSMENTION3 = ""
ASSID4 = 0
ASSNAME4 = ""
ASSUSERNAME4 = ""
ASSMENTION4 = ""
ASSID5 = 0
ASSNAME5 = ""
ASSUSERNAME5 = ""
ASSMENTION5 = ""
random_assistant = []

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    global ASSIDS
    global ASSID1, ASSNAME1, ASSMENTION1, ASSUSERNAME1
    global ASSID2, ASSNAME2, ASSMENTION2, ASSUSERNAME2
    global ASSID3, ASSNAME3, ASSMENTION3, ASSUSERNAME3
    global ASSID4, ASSNAME4, ASSMENTION4, ASSUSERNAME4
    global ASSID5, ASSNAME5, ASSMENTION5, ASSUSERNAME5
    await bot.start()
    if SESSION_NAME != "None":
       await Test.start()
       await call_py.start()
       random_assistant.append(1)
    if SESSION2 != "None":
       await user.start()
       await call_py2.start()
       random_assistant.append(2)
    if SESSION3 != "None":
       await user3.start()
       await call_py3.start()
       random_assistant.append(3)
    if SESSION4 != "None":
       await user4.start()
       await call_py4.start()
       random_assistant.append(4)
    if SESSION5 != "None":
       await user5.start()
       await call_py5.start()
       random_assistant.append(5)
    botinfo = bot.get_me()
    print("[INFO]: STARTING PYTGCALLSS CLIENT")
    await idle()



with bot as app:
    me_bot = app.get_me()


def init_db():
    global db_mem
    db_mem = {}

init_db()
