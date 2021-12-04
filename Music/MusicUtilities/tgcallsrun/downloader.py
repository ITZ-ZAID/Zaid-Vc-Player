from os import path
import yt_dlp
from yt_dlp.utils import DownloadError

ytdl = yt_dlp.YoutubeDL(
    {
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "format": "bestaudio/best",
        "geo_bypass": True,
        "nocheckcertificate": True,
    }
 )


def download(url: str, my_hook) -> str:       
    ydl_optssx = {
        'format' : 'bestaudio/best',
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "geo_bypass": True,
        "nocheckcertificate": True,
        'quiet': True,
        'no_warnings': True,
    }
    info = ytdl.extract_info(url, False)
    try:
        x = yt_dlp.YoutubeDL(ydl_optssx)
        x.add_progress_hook(my_hook)
        dloader = x.download([url])
    except Exception as y_e:
        return print(y_e)
    else:
        dloader
    xyz = path.join("downloads", f"{info['id']}.{info['ext']}")
    return xyz