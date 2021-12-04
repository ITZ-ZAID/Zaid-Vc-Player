from __future__ import unicode_literals
from datetime import datetime, timedelta
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaDocument,
    InputMediaVideo,
    InputMediaAudio,
    Message,
)
from yt_dlp import YoutubeDL
from pyrogram import Client, filters
import wget
import os
from os import path
from Music.MusicUtilities.helpers.thumbnails import down_thumb
from Music import app
from Music.MusicUtilities.helpers.inline import others_markup, play_markup
from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton
import yt_dlp
import asyncio
from PIL import Image
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

user_time = {}
youtube_next_fetch = 0
flex = {}

@Client.on_callback_query(filters.regex(pattern=r"other"))
async def closesmex(_,CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    userid = CallbackQuery.from_user.id 
    videoid, user_id = callback_request.split("|")    
    buttons = others_markup(videoid, user_id)
    await CallbackQuery.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))

    
@Client.on_callback_query(filters.regex(pattern=r"goback"))
async def goback(_,CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    userid = CallbackQuery.from_user.id 
    videoid, user_id = callback_request.split("|")    
    buttons = play_markup(videoid, user_id)
    await CallbackQuery.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_callback_query(filters.regex(pattern=r"good"))
async def good(_,CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    userid = CallbackQuery.from_user.id 
    videoid, user_id = callback_request.split("|")    
    buttons = others_markup(videoid, user_id)
    await CallbackQuery.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))    
    
@Client.on_callback_query(filters.regex("close"))
async def closed(_, query: CallbackQuery):
    await query.message.delete()
    await query.answer()  

@Client.on_callback_query(filters.regex(pattern=r"down"))
async def down(_,CallbackQuery):
    await CallbackQuery.answer()  
    
@Client.on_callback_query(filters.regex(pattern=r"gets"))
async def getspy(_,CallbackQuery):  
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    userid = CallbackQuery.from_user.id 
    type, videoid, user_id = callback_request.split("|") 
    Name = CallbackQuery.from_user.first_name
    userLastDownloadTime = user_time.get(userid)
    try:
        if userLastDownloadTime > datetime.now():
            wait_time = round((userLastDownloadTime - datetime.now()).total_seconds() / 60, 2)
            return await CallbackQuery.message.reply_text(f"Okay {Name}, Fast Downloading Is Started... `Wait for {wait_time} min(s) before next download request")
    except:
        pass
    url = (f"https://www.youtube.com/watch?v={videoid}")
    
    try:
        title, thumbnail_url, formats = extractYt(url)
        now = datetime.now()
        user_time[userid] = now + \
                                     timedelta(minutes=youtube_next_fetch)
    except Exception:
        return await CallbackQuery.message.reply_text("❌ Failed To Fetch Data...")
    j = 0
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    for x in formats:
        check = (x["format"])
        if type == "audio":
            if "audio" in check:
                j += 1
                if j == 1:
                    a1 = InlineKeyboardButton(text=f"Audio 🎵 {humanbytes(x['filesize'])}", callback_data=f"ytdata audio||{x['format_id']}||{videoid}")
                if j == 2:
                    a2 = InlineKeyboardButton(text=f"Audio 🎵 {humanbytes(x['filesize'])}", callback_data=f"ytdata audio||{x['format_id']}||{videoid}")
                if j == 3:
                    a3 = InlineKeyboardButton(text=f"Audio 🎵 {humanbytes(x['filesize'])}", callback_data=f"ytdata audio||{x['format_id']}||{videoid}") 
                if j == 4:
                    a4 = InlineKeyboardButton(text=f"Audio 🎵 {humanbytes(x['filesize'])}", callback_data=f"ytdata audio||{x['format_id']}||{videoid}")
                if j == 5:
                    a5 = InlineKeyboardButton(text=f"Audio 🎵 {humanbytes(x['filesize'])}", callback_data=f"ytdata audio||{x['format_id']}||{videoid}")
                if j == 6:
                    a6 = InlineKeyboardButton(text=f"Audio 🎵 {humanbytes(x['filesize'])}", callback_data=f"ytdata audio||{x['format_id']}||{videoid}")  
        elif type == "video":
            if str(133) in check:
                a += 1
                if int(a) == 1:
                    j += 1
                    a += 1
                    a1 = InlineKeyboardButton(text=f"(240)p 📹 {humanbytes(x['filesize'])}", callback_data=f"ytdata video||{x['format_id']}||{videoid}")
            if str(134) in check:
                b += 1
                if int(b) == 1:
                    j += 1
                    b += 1
                    a2 = InlineKeyboardButton(text=f"(360)p 📹 {humanbytes(x['filesize'])}", callback_data=f"ytdata video||{x['format_id']}||{videoid}")
            if str(135) in check:
                c += 1
                if int(c) == 1:
                    j += 1
                    c += 1
                    a3 = InlineKeyboardButton(text=f"(480)p 📹 {humanbytes(x['filesize'])}", callback_data=f"ytdata video||{x['format_id']}||{videoid}")   
            if str(136) in check:
                d += 1
                if int(d) == 1:
                    j += 1
                    d += 1
                    a4 = InlineKeyboardButton(text=f"(720)p 📹 {humanbytes(x['filesize'])}", callback_data=f"ytdata video||{x['format_id']}||{videoid}")
            if str(137) in check:
                e += 1
                if int(e) == 1:
                    j += 1
                    e += 1
                    a5 = InlineKeyboardButton(text=f"(1080)p 📹 {humanbytes(x['filesize'])}", callback_data=f"ytdata video||{x['format_id']}||{videoid}")
            if str(313) in check:
                f += 1
                if int(f) == 1:
                    j += 1
                    f += 1
                    a6 = InlineKeyboardButton(text=f"(2160)p 📹 {humanbytes(x['filesize'])}", callback_data=f"ytdata video||{x['format_id']}||{videoid}")   
        else:
            return await CallbackQuery.message.reply_text("❌ Video Format Not Found")
    universal = InlineKeyboardButton(text="🗑 Close Menu", callback_data=f'close2')
    if j == 0:
        return await CallbackQuery.message.reply_text("❌ Video Format Not Found")
    elif j == 1:
        key = InlineKeyboardMarkup(
            [
                [
                    a1,
                ],
                [
                    InlineKeyboardButton(text="⬅️  Go Back", callback_data=f'good {videoid}|{user_id}'),
                    InlineKeyboardButton(text="🗑 Close Menu", callback_data=f'close2')
                ]    
            ]
        )
    elif j == 2:
        key = InlineKeyboardMarkup(
            [
                [
                    a1,
                    a2,
                ],
                [
                    InlineKeyboardButton(text="⬅️  Go Back", callback_data=f'good {videoid}|{user_id}'),
                    InlineKeyboardButton(text="🗑 Close Menu", callback_data=f'close2')
                ]    
            ]
        )  
    elif j == 3:
        key = InlineKeyboardMarkup(
            [
                [
                    a1,
                    a2,
                ],
                [
                    a3,
                ],
                [
                    InlineKeyboardButton(text="⬅️  Go Back", callback_data=f'good {videoid}|{user_id}'),
                    InlineKeyboardButton(text="🗑 Close Menu", callback_data=f'close2')
                ]    
            ]
        ) 
    elif j == 4:
        key = InlineKeyboardMarkup(
            [
                [
                    a1,
                    a2,
                ],
                [
                    a3,
                    a4,
                ],
                [
                    InlineKeyboardButton(text="⬅️  Go Back", callback_data=f'good {videoid}|{user_id}'),
                    InlineKeyboardButton(text="🗑 Close Menu", callback_data=f'close2')
                ]    
            ]
        )    
    elif j == 5:
        key = InlineKeyboardMarkup(
            [
                [
                    a1,
                    a2,
                ],
                [
                    a3,
                    a4,
                ],
                [
                    a5,
                ],
                [
                    InlineKeyboardButton(text="⬅️  Go Back", callback_data=f'good {videoid}|{user_id}'),
                    InlineKeyboardButton(text="🗑 Close Menu", callback_data=f'close2')
                ]    
            ]
        )  
    elif j == 6:
        key = InlineKeyboardMarkup(
            [
                [
                    a1,
                    a2,
                ],
                [
                    a3,
                    a4,
                ],
                [
                    a5,
                    a6,
                ],
                [
                    InlineKeyboardButton(text="⬅️  Go Back", callback_data=f'good {videoid}|{user_id}'),
                    InlineKeyboardButton(text="🗑 Close Menu", callback_data=f'close2')
                ]    
            ]
        )    
    else:
        return await CallbackQuery.message.reply_text("❌ Video Format Not Found")
    await CallbackQuery.edit_message_reply_markup(reply_markup=key)

    
    
@Client.on_callback_query(filters.regex(pattern=r"ytdata"))
async def ytdata(_,CallbackQuery):  
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    user_id = CallbackQuery.from_user.id 
    type, format, videoid = callback_request.split("||") 
    Name = CallbackQuery.from_user.first_name
    if type == 'audio':
        a1 = InlineKeyboardButton(text=f"🎵 Audio Form", callback_data=f"boom audio||{format}||{videoid}")
        a2 = InlineKeyboardButton(text=f"💾 Document Form", callback_data=f"boom docaudio||{format}||{videoid}")
    else:
        a1 = InlineKeyboardButton(text=f"🎥 Video Form", callback_data=f"boom video||{format}||{videoid}")
        a2 = InlineKeyboardButton(text=f"💾 Document Form", callback_data=f"boom docvideo||{format}||{videoid}")
    key = InlineKeyboardMarkup(
            [
                [
                    a1,
                    a2,
                ],
                [
                    InlineKeyboardButton(text="⬅️  Go Back", callback_data=f'good {videoid}|{user_id}'),
                    InlineKeyboardButton(text="🗑 Close Menu", callback_data=f'close2')
                ]    
            ]
        )
    await CallbackQuery.edit_message_reply_markup(reply_markup=key)
    

inl = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="📥 Downloading...", callback_data=f'down')
                ]   
            ]
        )

upl = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="📤 Uploading...", callback_data=f'down')
                ]   
            ]
        )

def inl_mark(videoid, user_id):
    buttons= [
            [
                InlineKeyboardButton(text="❌ Download or Upload Failed", callback_data=f'down')
            ],
            [
                InlineKeyboardButton(text="⬅️  Go Back", callback_data=f'good {videoid}|{user_id}'),
                InlineKeyboardButton(text="🗑 Close Menu", callback_data=f'close2')
            ],
        ]
    return buttons 


ytdl_opts = {"format" : "bestaudio", "quiet":True}


@Client.on_callback_query(filters.regex(pattern=r"boom"))
async def boom(_,CallbackQuery): 
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    user_id = CallbackQuery.from_user.id 
    userid = user_id
    type, format_id, videoid = callback_request.split("||") 
    Name = CallbackQuery.from_user.first_name
    filext = "%(title)s.%(ext)s"
    userdir = os.path.join(os.getcwd(), "downloads", str(user_id))
    if not os.path.isdir(userdir):
        os.makedirs(userdir)
    filepath = os.path.join(userdir, filext)
    yturl = (f"https://www.youtube.com/watch?v={videoid}")
    try:
        with yt_dlp.YoutubeDL(ytdl_opts) as ytdl:
            x = ytdl.extract_info(yturl, download=False)
    except Exception as e:
        buttons = inl_mark(videoid, user_id)
        await CallbackQuery.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons)) 
    mystic = await CallbackQuery.edit_message_text("📥 Download Started...\n\n🔄 Downloading speed activated, Please hold on...", reply_markup = inl)
    fetched = f"""
**Track Downloaded**

❇️ **Title:** {x["title"]}
⏳ **Duration:** {round(x["duration"] / 60)} Mins
👀 **Views:** __{x["view_count"]}__
🎥 **Channel Name:** {x["uploader"]}

__Youtube Inline Download Powered By SHUBHANSHU/BOOO Music Player__ """    
    link = (x["webpage_url"])
    channel = (x["channel_url"])
    perf = (x['uploader'])
    thumbnail_url = (x["thumbnail"])
    filext = "%(title)s.png"
    main =  os.getcwd()
    img = wget.download(thumbnail_url)
    im = Image.open(img).convert("RGB")
    output_directory = os.path.join(os.getcwd(), "search", str(userid))
    if not os.path.isdir(output_directory):
        os.makedirs(output_directory)
    thumb_image_path = f"{output_directory}.png"
    im.save(thumb_image_path,"png")
    print(thumb_image_path)
    width = 0
    height = 0
    if os.path.exists(thumb_image_path):
        metadata = extractMetadata(createParser(thumb_image_path))
        if metadata.has("width"):
            width = metadata.get("width")
        if metadata.has("height"):
            height = metadata.get("height")
        img = Image.open(thumb_image_path)
        if type == 'audio':    
            img.resize((320, height))
        elif type == 'docaudio':    
            img.resize((320, height))
        elif type == 'docvideo':    
            img.resize((320, height))
        else:
            img.resize((90, height))
        img.save(thumb_image_path, "png")
    audio_command = [
        "yt-dlp",
        "-c",
        "--prefer-ffmpeg",
        "--extract-audio",
        "--audio-format", "mp3",
        "--audio-quality", format_id,
        "-o", filepath,
        yturl,
    ]
    video_command = [
        "yt-dlp",
        "-c",
        "--embed-subs",
        "-f", f"{format_id}+140",
        "-o", filepath,
        "--hls-prefer-ffmpeg", yturl]
    loop = asyncio.get_event_loop()
    med = None
    if type == 'audio':
        filename = await downloadaudiocli(audio_command)
        med = InputMediaAudio(
            media=filename,
            thumb=thumb_image_path,
            caption=fetched,
            title=os.path.basename(filename),
            performer=perf,
        )
    if type == 'video':
        filename = await downloadvideocli(video_command)
        dur = round(duration(filename))
        med = InputMediaVideo(
            media=filename,
            duration=dur,
            width=width,
            height=height,
            thumb=thumb_image_path,
            caption=fetched,
            supports_streaming=True
        )
    if type == 'docaudio':
        filename = await downloadaudiocli(audio_command)
        med = InputMediaDocument(
            media=filename,
            thumb=thumb_image_path,
            caption=fetched,
        )
    if type == 'docvideo':
        filename = await downloadvideocli(video_command)
        dur = round(duration(filename))
        med = InputMediaDocument(
            media=filename,
            thumb=thumb_image_path,
            caption=fetched,
        )
    if med:
        loop.create_task(send_file(CallbackQuery, med, filename, videoid, user_id, link, channel))
    else:
        print("med not found")
    
def p_mark(link, channel):
    buttons= [
            [
                InlineKeyboardButton(text="🎥 Watch on Youtube", url=f'{link}')
            ],
            [ 
                InlineKeyboardButton(text="📲 Visit Youtube Channel", url=f'{channel}')
            ],
        ]
    return buttons    
    
async def send_file(CallbackQuery, med, filename, videoid, user_id, link, channel):
    await CallbackQuery.edit_message_text("📤 Upload Started...\n\n🔄 Uploading speed activated, Please hold on...", reply_markup = upl)
    try:
        await app.send_chat_action(chat_id=CallbackQuery.message.chat.id, action="upload_document")
        buttons = p_mark(link, channel)
        await CallbackQuery.edit_message_media(media=med, reply_markup=InlineKeyboardMarkup(buttons))
    except Exception as e:
        print(e)
        buttons = inl_mark(videoid, user_id)
        await CallbackQuery.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons)) 
    finally:
        try:
            os.remove(filename)
            os.remove(thumb_image_path)
        except:
            pass
    
import subprocess as sp
import json


def probe(vid_file_path):
    """
    Give a json from ffprobe command line
    @vid_file_path : The absolute (full) path of the video file, string.
    """
    if type(vid_file_path) != str:
        raise Exception('Give ffprobe a full file path of the file')

    command = ["ffprobe",
               "-loglevel", "quiet",
               "-print_format", "json",
               "-show_format",
               "-show_streams",
               vid_file_path
               ]

    pipe = sp.Popen(command, stdout=sp.PIPE, stderr=sp.STDOUT)
    out, err = pipe.communicate()
    return json.loads(out)


def duration(vid_file_path):
    """
    Video's duration in seconds, return a float number
    """
    _json = probe(vid_file_path)

    if 'format' in _json:
        if 'duration' in _json['format']:
            return float(_json['format']['duration'])

    if 'streams' in _json:
        # commonly stream 0 is the video
        for s in _json['streams']:
            if 'duration' in s:
                return float(s['duration'])

    raise Exception('duration Not found')
    
    
def humanbytes(num, suffix='B'):
    if num is None:
        num = 0
    else:
        num = int(num)

    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)


def extractYt(yturl):
    ydl = yt_dlp.YoutubeDL()
    with ydl:
        qualityList = []
        r = ydl.extract_info(yturl, download=False)
        for format in r['formats']:
            # Filter dash video(without audio)
            if not "dash" in str(format['format']).lower():
                qualityList.append(
                {"format": format['format'], "filesize": format['filesize'], "format_id": format['format_id'],
                 "yturl": yturl})

        return r['title'], r['thumbnail'], qualityList  
    
async def downloadvideocli(command_to_exec):
    process = await asyncio.create_subprocess_exec(
        *command_to_exec,
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE, )
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    print(e_response)
    filename = t_response.split("Merging formats into")[-1].split('"')[1]
    return filename


async def downloadaudiocli(command_to_exec):
    process = await asyncio.create_subprocess_exec(
        *command_to_exec,
        # stdout must a pipe to be accessible as process.stdout
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE, )
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()
    print("Download error:", e_response)

    return t_response.split("Destination")[-1].split("Deleting")[0].split(":")[-1].strip()
