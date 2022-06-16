import os
import asyncio
from Zaid.main import bot, call_py, call_py2, call_py3, call_py4, call_py5
from pytgcalls.types import Update
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from Zaid.queues import QUEUE, clear_queue, get_queue, pop_an_item
from pytgcalls.types.input_stream.quality import (
    HighQualityAudio,
    HighQualityVideo,
    LowQualityVideo,
    MediumQualityVideo,
)

from Zaid.Database.active import remove_active_video_chat, remove_active_chat
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from pyrogram import Client, filters
from pytgcalls.types.stream import StreamAudioEnded, StreamVideoEnded

from Zaid.Database.clientdb import *


keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="• Mᴇɴᴜ", callback_data="cbmenu"),
                InlineKeyboardButton(text="• Cʟᴏsᴇ", callback_data="cls"),
            ]
        ]
    )


async def skip_current_song(chat_id):
    _assistant = await get_assistant(chat_id, "assistant")
    assistant = _assistant["saveassistant"]
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        if len(chat_queue) == 1:
            if int(assistant) == 1:
               await call_py.leave_group_call(chat_id)
            if int(assistant) == 2:
               await call_py2.leave_group_call(chat_id)
            if int(assistant) == 3:
               await call_py3.leave_group_call(chat_id)
            if int(assistant) == 4:
               await call_py4.leave_group_call(chat_id)
            if int(assistant) == 5:
               await call_py5.leave_group_call(chat_id)
            await remove_active_video_chat(chat_id)
            await remove_active_chat(chat_id)
            clear_queue(chat_id)
            return 1
        else:
            try:
                songname = chat_queue[1][0]
                url = chat_queue[1][1]
                link = chat_queue[1][2]
                type = chat_queue[1][3]
                Q = chat_queue[1][4]
                if type == "Audio":
                    if int(assistant) == 1:
                       await call_py.change_stream(
                           chat_id,
                           AudioPiped(
                               url,
                           ),
                       )
                    if int(assistant) == 2:
                       await call_py2.change_stream(
                           chat_id,
                           AudioPiped(
                               url,
                           ),
                       )
                    if int(assistant) == 3:
                       await call_py3.change_stream(
                           chat_id,
                           AudioPiped(
                               url,
                           ),
                       )
                    if int(assistant) == 4:
                       await call_py4.change_stream(
                           chat_id,
                           AudioPiped(
                               url,
                           ),
                       )
                    if int(assistant) == 5:
                       await call_py5.change_stream(
                           chat_id,
                           AudioPiped(
                               url,
                           ),
                       )
                elif type == "Video":
                    if Q == 720:
                        hm = HighQualityVideo()
                    elif Q == 480:
                        hm = MediumQualityVideo()
                    elif Q == 360:
                        hm = LowQualityVideo()
                    if int(assistant) == 1:
                       await call_py.change_stream(
                           chat_id, AudioVideoPiped(url, HighQualityAudio(), hm)
                       )
                    if int(assistant) == 2:
                       await call_py2.change_stream(
                           chat_id, AudioVideoPiped(url, HighQualityAudio(), hm)
                       )
                    if int(assistant) == 3:
                       await call_py3.change_stream(
                           chat_id, AudioVideoPiped(url, HighQualityAudio(), hm)
                       )
                    if int(assistant) == 4:
                       await call_py4.change_stream(
                           chat_id, AudioVideoPiped(url, HighQualityAudio(), hm)
                       )
                    if int(assistant) == 5:
                       await call_py5.change_stream(
                           chat_id, AudioVideoPiped(url, HighQualityAudio(), hm)
                       )
                pop_an_item(chat_id)
                return [songname, link, type]
            except:
                if int(assistant) == 1:
                   await call_py.leave_group_call(chat_id)
                if int(assistant) == 2:
                   await call_py2.leave_group_call(chat_id)
                if int(assistant) == 3:
                   await call_py3.leave_group_call(chat_id)
                if int(assistant) == 4:
                   await call_py4.leave_group_call(chat_id)
                if int(assistant) == 5:
                   await call_py5.leave_group_call(chat_id)
                clear_queue(chat_id)
                return 2
    else:
        return 0


async def skip_item(chat_id, h):
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        try:
            x = int(h)
            songname = chat_queue[x][0]
            chat_queue.pop(x)
            return songname
        except Exception as e:
            print(e)
            return 0
    else:
        return 0


@call_py.on_kicked()
async def kicked_handler(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)

@call_py2.on_kicked()
async def kicked_handler(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)

@call_py3.on_kicked()
async def kicked_handler(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)

@call_py4.on_kicked()
async def kicked_handler(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)

@call_py5.on_kicked()
async def kicked_handler(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)




@call_py.on_closed_voice_chat()
async def closed_voice_chat_handler(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)


@call_py2.on_closed_voice_chat()
async def closed_voice_chat_handler(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)

@call_py3.on_closed_voice_chat()
async def closed_voice_chat_handler(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)


@call_py4.on_closed_voice_chat()
async def closed_voice_chat_handler(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)

@call_py5.on_closed_voice_chat()
async def closed_voice_chat_handler(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)


@call_py.on_left()
async def left_handler(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)

@call_py2.on_left()
async def left_handler(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)

@call_py3.on_left()
async def left_handler(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)

@call_py4.on_left()
async def left_handler(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)

@call_py5.on_left()
async def left_handler(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)

@call_py.on_stream_end()
async def stream_end_handler(_, u: Update):
    if isinstance(u, StreamAudioEnded):
        chat_id = u.chat_id
        print(chat_id)
        op = await skip_current_song(chat_id)
        if op==1:
           await bot.send_message(chat_id, "✅ **userbot has disconnected from video chat.**")
        elif op==2:
           await bot.send_message(chat_id, "❌ **an error occurred**\n\n» **Clearing** __Queues__ **and leaving video chat.**")
        else:
         await bot.send_message(chat_id, f"💡 **Streaming next track**\n\n🏷 **Name:** [{op[0]}]({op[1]}) | `{op[2]}`\n💭 **Chat:** `{chat_id}`", disable_web_page_preview=True, reply_markup=keyboard)
    else:
       pass


@call_py2.on_stream_end()
async def stream_end_handler(_, u: Update):
    if isinstance(u, StreamAudioEnded):
        chat_id = u.chat_id
        print(chat_id)
        op = await skip_current_song(chat_id)
        if op==1:
           await bot.send_message(chat_id, "✅ **userbot has disconnected from video chat.**")
        elif op==2:
           await bot.send_message(chat_id, "❌ **an error occurred**\n\n» **Clearing** __Queues__ **and leaving video chat.**")
        else:
         await bot.send_message(chat_id, f"💡 **Streaming next track**\n\n🏷 **Name:** [{op[0]}]({op[1]}) | `{op[2]}`\n💭 **Chat:** `{chat_id}`", disable_web_page_preview=True, reply_markup=keyboard)
    else:
       pass


@call_py3.on_stream_end()
async def stream_end_handler(_, u: Update):
    if isinstance(u, StreamAudioEnded):
        chat_id = u.chat_id
        print(chat_id)
        op = await skip_current_song(chat_id)
        if op==1:
           await bot.send_message(chat_id, "✅ **userbot has disconnected from video chat.**")
        elif op==2:
           await bot.send_message(chat_id, "❌ **an error occurred**\n\n» **Clearing** __Queues__ **and leaving video chat.**")
        else:
         await bot.send_message(chat_id, f"💡 **Streaming next track**\n\n🏷 **Name:** [{op[0]}]({op[1]}) | `{op[2]}`\n💭 **Chat:** `{chat_id}`", disable_web_page_preview=True, reply_markup=keyboard)
    else:
       pass

@call_py4.on_stream_end()
async def stream_end_handler(_, u: Update):
    if isinstance(u, StreamAudioEnded):
        chat_id = u.chat_id
        print(chat_id)
        op = await skip_current_song(chat_id)
        if op==1:
           await bot.send_message(chat_id, "✅ **userbot has disconnected from video chat.**")
        elif op==2:
           await bot.send_message(chat_id, "❌ **an error occurred**\n\n» **Clearing** __Queues__ **and leaving video chat.**")
        else:
         await bot.send_message(chat_id, f"💡 **Streaming next track**\n\n🏷 **Name:** [{op[0]}]({op[1]}) | `{op[2]}`\n💭 **Chat:** `{chat_id}`", disable_web_page_preview=True, reply_markup=keyboard)
    else:
       pass

@call_py5.on_stream_end()
async def stream_end_handler(_, u: Update):
    if isinstance(u, StreamAudioEnded):
        chat_id = u.chat_id
        print(chat_id)
        op = await skip_current_song(chat_id)
        if op==1:
           await bot.send_message(chat_id, "✅ **userbot has disconnected from video chat.**")
        elif op==2:
           await bot.send_message(chat_id, "❌ **an error occurred**\n\n» **Clearing** __Queues__ **and leaving video chat.**")
        else:
         await bot.send_message(chat_id, f"💡 **Streaming next track**\n\n🏷 **Name:** [{op[0]}]({op[1]}) | `{op[2]}`\n💭 **Chat:** `{chat_id}`", disable_web_page_preview=True, reply_markup=keyboard)
    else:
       pass


async def bash(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip()
    out = stdout.decode().strip()
    return out, err
