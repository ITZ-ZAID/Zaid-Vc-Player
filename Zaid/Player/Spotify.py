from Zaid.main import bot, call_py
from pyrogram import filters
from Zaid.mainhelper import parse_spotify_url,fetch_spotify_track,download_songs,thumb_down,copy
from Zaid.ytdl import getIds,ytdl_down,audio_opt
import spotipy
from os import mkdir
from random import randint
AUTH_CHATS = None
LOGGER = None
LOG_GROUP = None


client = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyClientCredentials())



@bot.on_message(filters.command(["spotify"]))
async def spotify_dl(_,message):
    link = message.matches[0].group(0)
    m = await message.reply_text(f"**Gathering info from your [link]({link}).**")
    try:
        parsed_item = await parse_spotify_url(link)
        item_type, item_id = parsed_item[0],parsed_item[1]
        randomdir = f"/tmp/{str(randint(1,100000000))}"
        mkdir(randomdir)
        if item_type in ["show", "episode"]:
            items = await getIds(link)
            for item in items:
                PForCopy = await message.reply_photo(item[5],caption=f"✔️ Episode Name : `{item[3]}`\n🕔 Duration : {item[4]//60}:{item[4]%60}")
                fileLink = await ytdl_down(audio_opt(randomdir,item[2]),f"https://open.spotify.com/episode/{item[0]}")
                thumbnail = await thumb_down(item[5],item[0])
                AForCopy = await message.reply_audio(fileLink,title=item[3].replace("_"," "),performer="Spotify",duration=int(item[4]),caption=f"[{item[3]}](https://open.spotify.com/episode/{item[0]})",thumb=thumbnail)
                if LOG_GROUP:
                    await copy(PForCopy,AForCopy)
            return await m.delete()
        elif item_type == "track":
            song = await fetch_spotify_track(client,item_id)
            PForCopy = await message.reply_photo(song.get('cover'),caption=f"🎧 Title : `{song['name']}`\n🎤 Artist : `{song['artist']}`\n💽 Album : `{song['album']}`\n🎼 Genre : `{song['genre']}`\n🗓 Release Year: `{song['year']}`")
            path = await download_songs(song,randomdir)
            thumbnail = await thumb_down(song.get('cover'),song.get('name'))
            AForCopy = await message.reply_audio(path,performer=song.get('artist'),title=f"{song.get('name')} - {song.get('artist')}",caption=f"[{song.get('name')}](https://open.spotify.com/track/{song.get('deezer_id')}) | {song.get('album')} - {song.get('artist')}",thumb=thumbnail)
            if LOG_GROUP:
                await copy(PForCopy,AForCopy)
            return await m.delete()
        elif item_type == "playlist":
            tracks = client.playlist_items(playlist_id=item_id,additional_types=['track'])
            total_tracks = tracks.get('total')
            track_no = 1
            for track in tracks['items']:
                song = await fetch_spotify_track(client,track.get('track').get('id'))
                PForCopy = await message.reply_photo(song.get('cover'),caption=f"🎧 Title : `{song['name']}`\n🎤 Artist : `{song['artist']}`\n💽 Album : `{song['album']}`\n🎼 Genre : `{song['genre']}`\n🗓 Release Year: `{song['year']}`\n🔢 Track No: `{track_no}`\n🔢 Total Track: `{total_tracks}`")
                path = await download_songs(song,randomdir)
                thumbnail = await thumb_down(song.get('cover'),song.get('name'))
                AForCopy = await message.reply_audio(path,performer=song.get('artist'),title=f"{song.get('name')} - {song.get('artist')}",caption=f"[{song.get('name')}](https://open.spotify.com/track/{song.get('deezer_id')}) | {song.get('album')} - {song.get('artist')}",thumb=thumbnail)
                track_no += 1
                if LOG_GROUP:
                    await copy(PForCopy,AForCopy)
            return await m.delete()
        elif item_type == "album":
            tracks = client.album_tracks(album_id=item_id)
            for track in tracks['items']:
                song = await fetch_spotify_track(client,track.get('id'))
                PForCopy = await message.reply_photo(song.get('cover'),caption=f"🎧 Title : `{song['name']}`\n🎤 Artist : `{song['artist']}`\n💽 Album : `{song['album']}`\n🎼 Genre : `{song['genre']}`\n🗓 Release Year: `{song['year']}`")
                path = await download_songs(song,randomdir)
                thumbnail = await thumb_down(song.get('cover'),song.get('name'))
                AForCopy = await message.reply_audio(path,performer=song.get('artist'),title=f"{song.get('name')} - {song.get('artist')}",caption=f"[{song.get('name')}](https://open.spotify.com/track/{song.get('deezer_id')}) | {song.get('album')} - {song.get('artist')}",thumb=thumbnail)
                if LOG_GROUP:
                    await copy(PForCopy,AForCopy)
            return await m.delete()
    except Exception as e:
        LOGGER.error(e)
        await m.edit_text(e)
