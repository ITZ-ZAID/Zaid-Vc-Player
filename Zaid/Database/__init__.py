from pyrogram import filters
from pymongo import MongoClient
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import MONGO_DB_URL
client = MongoClient(MONGO_DB_URL)
dbd = client["zaid"]
db = dbd


from motor.motor_asyncio import AsyncIOMotorClient as Bot
from config import MONGO_DB_URL as tmo


MONGODB_CLI = Bot(tmo)
dbb = MONGODB_CLI.program
