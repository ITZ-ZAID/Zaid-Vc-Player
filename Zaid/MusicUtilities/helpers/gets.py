from typing import Union
from pyrogram.types import Message, Audio, Voice

async def convert_count(count):
    if int(count) == 1:
        x = "First"
    elif int(count) == 2:
        x = "Second"
    elif int(count) == 3:
        x = "Third"
    elif int(count) == 4:
        x = "Fourth"
    elif int(count) == 5:
        x = "Fifth"    
    elif int(count) == 6:
        x = "Sixth"    
    elif int(count) == 7:
        x = "Seventh"    
    elif int(count) == 8:
        x = "Eighth"    
    elif int(count) == 9:
        x = "Ninth"
    elif int(count) == 10:
        x = "Tenth"    
    elif int(count) == 11:
        x = "Eleventh"
    elif int(count) == 12:
        x = "Twelfth"    
    elif int(count) == 13:
        x = "Thirteenth"     
    elif int(count) == 14:
        x = "Fourteenth"    
    elif int(count) == 15:
        x = "Fifteenth" 
    elif str(count) == "all":
        x = "all"
    return x
def get_url(message_1: Message) -> Union[str, None]:
    messages = [message_1]
    if message_1.reply_to_message:
        messages.append(message_1.reply_to_message)
    text = ""
    offset = None
    length = None
    for message in messages:
        if offset:
            break
        if message.entities:
            for entity in message.entities:
                if entity.type == "url":
                    text = message.text or message.caption
                    offset, length = entity.offset, entity.length
                    break
    if offset in (None,):
        return None
    return text[offset:offset + length]
random_assistant = ["5", "1", "2", "3", "4"]

themes = ["Black", "Grey", "Green", "Purple", "Red", "Lightred", "Blue", "Lightblue"]

def bytes(size: float) -> str:
    """humanize size"""
    if not size:
        return ""
    power = 1024
    t_n = 0
    power_dict = {0: " ", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        t_n += 1
    return "{:.2f} {}B".format(size, power_dict[t_n])


async def ass_det(assistant: int):
    print("HAHAHHAHA")
