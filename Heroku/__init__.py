import asyncio
import importlib
import time

from pytgcalls import PyTgCalls
from pyrogram import Client

from Heroku import config


SUDO_USERS = config.SUDO_USERS
OWNER_ID = config.OWNER_ID
BOT_ID = config.BOT_ID
BOT_NAME = ""
BOT_USERNAME = ""
ASSID = config.ASSID
ASSNAME = ""
ASSUSERNAME = ""
SUDOERS = SUDO_USERS
OWNER = OWNER_ID

### Boot Time
boottime = time.time()

### auto
smexy = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
pytgcalls = PyTgCalls(smexy)

### Music Start Time
Music_START_TIME = time.time()

app = Client(
    ":memory:",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins={"root": "Heroku.modules"},
)
if config.CLONER_TOKEN:
   cloner = Client(
       ":memory:",
       config.API_ID,
       config.API_HASH,
       bot_token=config.CLONER_TOKEN,
       plugins={"root": "Heroku.plugins"},
   )
else:
   cloner = None

client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)


def all_info(app, client):
    global BOT_ID, BOT_NAME, BOT_USERNAME
    global ASSID, ASSNAME, ASSUSERNAME
    getme = app.get_me()
    getme1 = client.get_me()
    BOT_ID = getme.id
    ASSID = getme1.id
    if getme.last_name:
        BOT_NAME = getme.first_name + " " + getme.last_name
    else:
        BOT_NAME = getme.first_name
    BOT_USERNAME = getme.username
    ASSNAME = (
        f"{getme1.first_name} {getme1.last_name}"
        if getme1.last_name
        else getme1.first_name
    )
    ASSUSERNAME = getme1.username


app.start()
client.start()
if cloner:
   cloner.start()
all_info(app, client)
