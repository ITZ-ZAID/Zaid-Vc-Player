## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME","BQB7hcVKh6GNFKsXJR5-Ve3X7woxj1aWxJARiEURAqb7cBhu17GIgutwK30VJoMpXTkIGyGMZzDpT910AoEgo0DVWIk6pCQIQ__4YSKEgM6zoqdDdBgtvgEAg-9KZRkz0st3xrhHXbLLhinUqO4FFM26wp68qmNIUJDLN7bOG75KqWLhwHmsduyegruuUJ8tvqB4Lkpmf1KeHtLpGDHNUPNApwHona2P9Pz81jaW3gKjzBPf_sAophG5X9wCK2r8fZ7kKApn3fUPx1exj0EVbEz0Iva31hhqsSkk3GjL7sKK9os07eE8DgmSCgJYwnbchgFtZslnR-XEKcLRD-4krM-refTlWgA")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

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

BOT_TOKEN = getenv("BOT_TOKEN", "5544474027:AAG4gH91He35vMs4LMZfu_aqAhXneGzeALA")
BOT_NAME = getenv("BOT_NAME", "TUSHAR X ROBOT")

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Cloner:Cloner@cluster0.cgc6t.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "TUSHAR")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Timesisnotwaiting")
ALIVE_NAME = getenv("ALIVE_NAME", "Tushar op")
BOT_USERNAME = getenv("BOT_USERNAME", "Tushar_op_bot")
OWNER_ID = getenv("OWNER_ID", "5099353600")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "TUSHAR MUSIC")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "hjhvvl")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "hjhvvl")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5099353600").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "6000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
