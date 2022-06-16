## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2", ""))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5403221503:AAFHnF7-EzZMoeU4s16OdK6wWrPOOFeInFE")
BOT_NAME = getenv("BOT_NAME", "𝙂𝙖𝙡𝙖𝙘𝙩𝙪𝙨 🇮🇳")

API_ID = int(getenv("API_ID", "17222924"))
API_HASH = getenv("API_HASH", "1e3f116637d6ecfb92ef45a6d4949c8c")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Cloner:Cloner@cluster0.cgc6t.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Chiku")
OWNER_USERNAME = getenv("OWNER_USERNAME", "youknowchiku")
ALIVE_NAME = getenv("ALIVE_NAME", "Andy")
BOT_USERNAME = getenv("BOT_USERNAME", "AndyGalactus_bot")
OWNER_ID = getenv("OWNER_ID", "5331950210")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Chiku1224")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Thegalactuschat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Galatcusupdate")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
