print("[INFO]: INITIALIZING THE SERVER")
from pyrogram import Client
import asyncio
from Music.config import API_ID, API_HASH, BOT_TOKEN, MONGO_DB_URI, SUDO_USERS
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
import time
import uvloop
from Music import config
import importlib
from pyrogram import Client as Bot
from Music.config import API_ID, API_HASH, BOT_TOKEN, MONGO_DB_URI, SUDO_USERS, LOG_GROUP_ID, OWNER_ID
from pyrogram import Client
from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
import time

def initialize():
    global dbb
    dbb = {}
    
initialize()

print("[INFO]: INITIALIZING DATABASE OF YUKKI SERVER")
MONGODB_CLI = MongoClient(MONGO_DB_URI)
db = MONGODB_CLI.wbb
SUDOERS = SUDO_USERS
OWNER = OWNER_ID
async def load_sudoers():
    global SUDOERS
    print("[INFO]: LOADING SUDO USERS")
    sudoersdb = db.sudoers
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudoers else sudoers["sudoers"]
    for user_id in SUDOERS:
        if user_id not in sudoers:
            sudoers.append(user_id)
            await sudoersdb.update_one(
                {"sudo": "sudo"}, {"$set": {"sudoers": sudoers}}, upsert=True
            )
    SUDOERS = (SUDOERS + sudoers) if sudoers else SUDOERS
    print("[INFO]: LOADED SUDO USERS OF YUKKI")
loop = asyncio.get_event_loop()
loop.run_until_complete(load_sudoers())
Music_START_TIME = time.time()
loop = asyncio.get_event_loop()



BOT_ID = 0
BOT_NAME = ""
BOT_USERNAME = ""
ASSID = 0
ASSNAME = ""
ASSUSERNAME = ""
ASSMENTION = ""
print("[INFO]: INITIALIZING BOT CLIENTS")
app = Client(
    'YukkiBot',
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)
aiohttpsession = ClientSession()

client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)

def all_info(app, client):
    global BOT_ID, BOT_NAME, BOT_USERNAME
    global ASSID, ASSNAME, ASSMENTION, ASSUSERNAME
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
    ASSMENTION = getme1.mention
    

    
print("[INFO]: STARTING BOT CLIENT")
app.start()
print("[INFO]: STARTING ASSISTANT CLIENT")
client.start()
print("[INFO]: LOADING BOT/ASSISTANT PROFILE INFO")
all_info(app, client)
print("[INFO]: LOADED BOT/ASSISTANT PROFILE INFO")
