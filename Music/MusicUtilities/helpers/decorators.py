from typing import Callable
from pyrogram import Client
from pyrogram.types import Message

def errors(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        try:
            return await func(client, message)
        except Exception as e:
            await message.reply(f'{type(e).__name__}: {e}', False)

    return decorator