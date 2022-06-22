## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQAOB4OCdT4fUkiEou0aQbFvlmARKnW5NYgPz8emHNI7qYWlFA0PZQHKKumijmk2tIRBEbGM5kk4Cy_ljp1InER33USyvdz1cOBKtj62su72fEuysA_bTzoBNLWCQcoAXXojY1ahRQDMUspiftQfPDBFcqNe_yGomCEm3dvXq6BQsRsc60jXHJEJbziFLEC3D0LzF8eX2z8wYYjCcWcUbWor8TgS7Y2w646govs1h5oObmqnkLpWv0t1-MkBCc7s2ef9e6nMKscd3M-185FrrPM9LkjrGcrpWx_U2G60sIQ1c2h4yz2gJKLk5PLA2sV6YxJ_Tu35qN_s2ZhFIMwTjPpmAAAAAUFZjAMA")
BOT_TOKEN = getenv("BOT_TOKEN", "5385491950:AAFp_hYLzKxYufE_lLXmuw3hbqpanzFSnjE")
BOT_NAME = getenv("BOT_NAME", "@Babu_Sonabot")
API_ID = int(getenv("API_ID", "13709231"))
API_HASH = getenv("API_HASH", "15ab30bcea9d6d8fc6a58919d2bcbe51")
OWNER_NAME = getenv("OWNER_NAME", "Nishu")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Trinetra_Owner")
ALIVE_NAME = getenv("ALIVE_NAME", "Nishu")
BOT_USERNAME = getenv("BOT_USERNAME", "Babu_SonaBot")
OWNER_ID = getenv("OWNER_ID", "5330764294")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "BabyAssistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "RFS_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "RFS_BOTHUB")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5132611794").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/RimuruDemonlord/VcBot")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
