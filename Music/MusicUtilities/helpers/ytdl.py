from yt_dlp import YoutubeDL

ytdl = YoutubeDL(
    {
        "format": "bestaudio/best",
        "geo-bypass": True,
        "nocheckcertificate": True,
        "outtmpl": "downloads/%(id)s.%(ext)s",
    }
)

ytdl_opts = {"format" : "bestaudio", "quiet":True}