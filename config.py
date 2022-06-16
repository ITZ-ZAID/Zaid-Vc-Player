## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BACNx-QZ0w-ZBCgp9kKVdRXC3kwTE_ase5Vc_ZvAojDD7yIreTwV9yUpk0qhlIAujSs3Kh8V0-NvVE8DtkPWrLMKcgv8AIQUErMYbHVRaqgHOpBs7vRp96ljt9UMeYzyBNZRXM8-gV3wnUqo8qrs0Bjrduma5fSqeD41zxLhPokKZnWYVVuK-JvOhdvapGQc5BPKRDDLK_zXT-OvLevrTELvcBY79FD3MOOCx0murJY74SL112lqt91CvfipQt63Ob4j3Blv3GDB3pSDvJPx3D9BRzLeSFcEZtLmjwixoveJDt-1OkzOIYX-Yve8jabqWF5n_HwEsgA25OzdkK0kLvOaebRCzwA")
BOT_TOKEN = getenv("BOT_TOKEN", "1918533631:AAHEt5AGNmmSm-yHBTLs6rR4IFmFcstoShs")
BOT_NAME = getenv("BOT_NAME", "Sufian Srk bot")
API_ID = int(getenv("API_ID", "8940184"))
API_HASH = getenv("API_HASH", "d4c0543f2c95dc2098ec8d2802f808da")
OWNER_NAME = getenv("OWNER_NAME", "sufian")
OWNER_USERNAME = getenv("OWNER_USERNAME", "sufiansrk10")
ALIVE_NAME = getenv("ALIVE_NAME", "Zaid")
BOT_USERNAME = getenv("BOT_USERNAME", "Sufian_srk_music_bot")
OWNER_ID = getenv("OWNER_ID", "1158888206")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Sufian_music_1")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "sufian_bot_update")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Sufian_bots_update")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1158888206").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph//file/5d97cd3b78d8bd99ff07d.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph//file/91d895bfa58125709c989.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/walal-zacky/Zaid-Vc-Player")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
