import os
import re
import textwrap

import aiofiles
import aiohttp
from PIL import (Image, ImageDraw, ImageEnhance, ImageFilter,
                 ImageFont, ImageOps)
from youtubesearchpython.__future__ import VideosSearch
from config import BOT_NAME

YOUTUBE_IMG_URL = 'https://telegra.ph/file/58da23d726b601dc3b18e.jpg'

def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


async def play_thumb(videoid):   
    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown Mins"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                views = result["viewCount"]["short"]
            except:
                views = "Unknown Views"
            try:
                channel = result["channel"]["name"]
            except:
                channel = "Unknown Channel"

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(
                        f"play{videoid}.png", mode="wb"
                    )
                    await f.write(await resp.read())
                    await f.close()

        youtube = Image.open(f"play{videoid}.png")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(30))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)
        Xcenter = youtube.width / 2
        Ycenter = youtube.height / 2
        x1 = Xcenter - 250
        y1 = Ycenter - 250
        x2 = Xcenter + 250
        y2 = Ycenter + 250
        logo = youtube.crop((x1, y1, x2, y2))
        logo.thumbnail((520, 520), Image.ANTIALIAS)
        logo = ImageOps.expand(logo, border=15, fill="white")
        background.paste(logo, (50, 100))
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("Process/ImageFont/font2.ttf", 40)
        font2 = ImageFont.truetype("Process/ImageFont/font2.ttf", 70)
        arial = ImageFont.truetype("Process/ImageFont/font2.ttf", 30)
        name_font = ImageFont.truetype("Process/ImageFont/font.ttf", 30)
        para = textwrap.wrap(title, width=32)
        j = 0
        draw.text(
            (5, 5), f"{BOT_NAME}", fill="white", font=name_font
        )
        draw.text(
            (600, 150),
            "NOW PLAYING",
            fill="white",
            stroke_width=2,
            stroke_fill="white",
            font=font2,
        )
        for line in para:
            if j == 1:
                j += 1
                draw.text(
                    (600, 340),
                    f"{line}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="white",
                    font=font,
                )
            if j == 0:
                j += 1
                draw.text(
                    (600, 280),
                    f"{line}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="white",
                    font=font,
                )
        draw.text(
            (600, 400),
            f"Bot : {BOT_NAME} ",
            (255, 255, 255),
            font=arial,
        )
        draw.text(
            (600, 450),
            f"Views : {views[:23]}",
            (255, 255, 255),
            font=arial,
        )
        draw.text(
            (600, 500),
            f"Duration : {duration[:23]} Mins",
            (255, 255, 255),
            font=arial,
        )
        draw.text(
            (600, 550),
            f"Channel : {channel}",
            (255, 255, 255),
            font=arial,
        )
        try:
            os.remove(f"play{videoid}.png")
        except:
            pass
        background.save(f"pfinal{videoid}.png")
        return f"pfinal{videoid}.png"
    except Exception:
        return YOUTUBE_IMG_URL

async def queue_thumb(videoid):   
    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown Mins"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                views = result["viewCount"]["short"]
            except:
                views = "Unknown Views"
            try:
                channel = result["channel"]["name"]
            except:
                channel = "Unknown Channel"

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(
                        f"queue{videoid}.png", mode="wb"
                    )
                    await f.write(await resp.read())
                    await f.close()

        youtube = Image.open(f"queue{videoid}.png")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(30))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)
        Xcenter = youtube.width / 2
        Ycenter = youtube.height / 2
        x1 = Xcenter - 250
        y1 = Ycenter - 250
        x2 = Xcenter + 250
        y2 = Ycenter + 250
        logo = youtube.crop((x1, y1, x2, y2))
        logo.thumbnail((520, 520), Image.ANTIALIAS)
        logo = ImageOps.expand(logo, border=15, fill="white")
        background.paste(logo, (50, 100))
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("Process/ImageFont/font2.ttf", 40)
        font2 = ImageFont.truetype("Process/ImageFont/font2.ttf", 70)
        arial = ImageFont.truetype("Process/ImageFont/font2.ttf", 30)
        name_font = ImageFont.truetype("Process/ImageFont/font.ttf", 30)
        para = textwrap.wrap(title, width=32)
        j = 0
        draw.text(
            (5, 5), f"{BOT_NAME}", fill="white", font=name_font
        )
        draw.text(
            (600, 150),
            "IN QUEUE",
            fill="white",
            stroke_width=2,
            stroke_fill="white",
            font=font2,
        )
        for line in para:
            if j == 1:
                j += 1
                draw.text(
                    (600, 340),
                    f"{line}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="white",
                    font=font,
                )
            if j == 0:
                j += 1
                draw.text(
                    (600, 280),
                    f"{line}",
                    fill="white",
                    stroke_width=1,
                    stroke_fill="white",
                    font=font,
                )

        draw.text(
            (600, 450),
            f"Views : {views[:23]}",
            (255, 255, 255),
            font=arial,
        )
        draw.text(
            (600, 500),
            f"Duration : {duration[:23]} Mins",
            (255, 255, 255),
            font=arial,
        )
        draw.text(
            (600, 550),
            f"Channel : {channel}",
            (255, 255, 255),
            font=arial,
        )
        try:
            os.remove(f"queue{videoid}.png")
        except:
            pass
        background.save(f"qfinal{videoid}.png")
        return f"qfinal{videoid}.png"
    except Exception:
        return YOUTUBE_IMG_URL
