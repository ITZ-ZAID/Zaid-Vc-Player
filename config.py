import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
if str(getenv("SESSION_NAME")).strip() == "BQDRL68AnmzfzdEie-C-ejLX2OUfrZWUkvE-5UNOf47hW-piRO7ZRcY8rYLehUudE6PK15uTKV6rUDx6x6Hz45fgp2Emo2bfvrOAfrNnS_4jTI14J2-tTn9TzY5fwvG_Xgr9ZuQBKZJ9JZhpe0vTsqmUjuBew511CgWP3qcgHdxB2l6j4LhLDnVIYPL5z6XgfvFPDjoPPRUrT-0Hg0jnnFrgjAZSs-3CrGt1vqHJqdZcwHy1zuvUBMEFLPZV-DWK4xl9wdq-aeyBXYxxXp21ObNuiPVqkw1ZQjYaGmLNzDl5KGj13B7MGxMJ8X2_N3x-sRa4dIFwHiQy9vL1X58BKGZNsft_PAAAAAFBABXuAQ":
    SESSION_NAME = str(None)
else:
    SESSION_NAME = str(getenv("SESSION_NAME"))

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

BOT_TOKEN = getenv("BOT_TOKEN", "5385491950:AAFp_hYLzKxYufE_lLXmuw3hbqpanzFSnjE")
BOT_NAME = getenv("BOT_NAME", "@Babu_SonaBot")

API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Cloner:Cloner@cluster0.cgc6t.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Nishu")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Timesisnotwaiting")
ALIVE_NAME = getenv("ALIVE_NAME", "Nishu")
BOT_USERNAME = getenv("BOT_USERNAME", "Baby_SonaBot")
OWNER_ID = getenv("OWNER_ID", "5330764294")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "BabyAssistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "RFS_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "RFS_BOTHUB")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
