import os
from os import path
import aiohttp
import aiofiles
from os import path
from typing import Union
from asyncio import QueueEmpty
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from PIL import ImageGrab
from typing import Callable

def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage



def truncate(text):
    list = text.split(" ")
    text1 = ""
    text2 = ""    
    for i in list:
        if len(text1) + len(i) < 27:        
            text1 += " " + i
        elif len(text2) + len(i) < 25:        
            text2 += " " + i

    text1 = text1.strip()
    text2 = text2.strip()     
    return [text1,text2]


async def gen_thumb(thumbnail, title, userid, theme, ctitle):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()

    image = Image.open(f"./background.png")
    black = Image.open("cache/black.jpg")
    img = Image.open("cache/robot.png")
    image5 = changeImageSize(1280, 720, img)
    image1 = changeImageSize(1280, 720, image)
    image1 = image1.filter(ImageFilter.BoxBlur(10))
    image11 = changeImageSize(1280, 720, image)
    image1 = image11.filter(ImageFilter.BoxBlur(10))
    image2 = Image.blend(image1,black,0.6)

    # Cropping circle from thubnail
    image3 = image11.crop((280,0,1000,720))
    #lum_img = Image.new('L', [720,720] , 0)
   # draw = ImageDraw.Draw(lum_img)
   # draw.pieslice([(0,0), (720,720)], 0, 360, fill = 255, outline = "white")
   # img_arr =np.array(image3)
    #lum_img_arr =np.array(lum_img)
    #final_img_arr = np.dstack((img_arr,lum_img_arr))
    #image3 = Image.fromarray(final_img_arr)
    image3 = image3.resize((500,500))
    

    image2.paste(image3, (100,115))
    image2.paste(image5, mask = image5)

    # fonts
    font1 = ImageFont.truetype(r'cache/robot.otf', 30)
    font2 = ImageFont.truetype(r'cache/robot.otf', 60)
    font3 = ImageFont.truetype(r'cache/robot.otf', 49)
    font4 = ImageFont.truetype(r'cache/Mukta-ExtraBold.ttf', 35)

    image4 = ImageDraw.Draw(image2)

    # title
    title1 = truncate(title)
    image4.text((670, 280), text=title1[0], fill="red", font = font3, align ="left") 
    image4.text((670, 332), text=title1[1], fill="red", font = font3, align ="left") 

    # description
    views = f"Requester id: {userid}"
    channel = f"Playing on : {ctitle}"
    my = "Powered By Zaid"  

    image4.text((670, 410), text=views, fill="yellow", font = font4, align ="left") 
    image4.text((670, 460), text=channel, fill="yellow", font = font4, align ="left")
    image4.text((880, 670), text=my, fill="blue", font = font3, align ="left")
    
    image2.save(f"final.png")
    os.remove(f"background.png")
    final = f"final.png" 
    return final


async def down_thumb(thumbnail, userid):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open(f"search/thumb{userid}.png", mode="wb")
                await f.write(await resp.read())
                await f.close()
    final = f"search/thumb{userid}.png"
    return final
