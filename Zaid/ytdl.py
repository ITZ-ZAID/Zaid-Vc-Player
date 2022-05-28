from asgiref.sync import sync_to_async
from yt_dlp import YoutubeDL
from requests import get
from config import BOT_USERNAME

@sync_to_async
def getIds(video):
    ids = []
    with YoutubeDL({'quiet':True}) as ydl:
        info_dict = ydl.extract_info(video, download=False)
        try:
            info_dict = info_dict['entries']
            ids.extend([x.get('id'),x.get('playlist_index'),x.get('creator') or x.get('uploader'),x.get('title'),x.get('duration'),x.get('thumbnail')] for x in info_dict)
        except:
            ids.append([info_dict.get('id'),info_dict.get('playlist_index'),info_dict.get('creator') or info_dict.get('uploader'),info_dict.get('title'),info_dict.get('duration'),info_dict.get('thumbnail')])
    return ids

def audio_opt(path,uploader=f"@{BOT_USERNAME}"):
    return {
        "format": "bestaudio",
        "addmetadata": True,
        "geo_bypass": True,
        'noplaylist': True,
        "nocheckcertificate": True,
        "outtmpl": f"{path}/%(title)s - {uploader}.mp3",
        "quiet": True
    }

@sync_to_async
def ytdl_down(opts, url):
    with YoutubeDL(opts) as ydl:
        info = ydl.extract_info(url)
        return ydl.prepare_filename(info)

@sync_to_async
def thumb_down(videoId):
    with open(f"/tmp/thumbnails/{videoId}.jpg","wb") as file:
        file.write(get(f"https://img.youtube.com/vi/{videoId}/default.jpg").content)
    return f"/tmp/thumbnails/{videoId}.jpg"
