from os import listdir, mkdir
from pyrogram import Client
from Zaid import config
from Zaid.MusicUtilities.tgcallsrun.queues import (clear, get, is_empty, put, task_done)
from Zaid.MusicUtilities.tgcallsrun.downloader import download
from Zaid.MusicUtilities.tgcallsrun.convert import convert
from Zaid.MusicUtilities.tgcallsrun.music import run
from Zaid.MusicUtilities.tgcallsrun.music import smexy as ASS_ACC
smexy = 1
