import heroku3
import asyncio
import os
import shlex

from typing import Tuple
from functools import wraps

from pyrogram.types import Message

from functools import wraps
from Heroku.config import HEROKU_API_KEY, HEROKU_APP_NAME


def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


heroku_client = heroku3.from_key(HEROKU_API_KEY) if HEROKU_API_KEY else None


def check_heroku(func):
    @wraps(func)
    async def heroku_cli(client, message):
        heroku_app = None
        if not heroku_client:
            await message.reply_text(
                "`Please Add HEROKU_API_KEY Key For This To Function To Work!`",
                parse_mode="markdown",
            )
        elif not HEROKU_APP_NAME:
            await message.reply_text(
                "`Please Add HEROKU_APP_NAME For This To Function To Work!`",
                parse_mode="markdown",
            )
        if HEROKU_APP_NAME and heroku_client:
            try:
                heroku_app = heroku_client.app(HEROKU_APP_NAME)
            except:
                await message.reply_text(
                    message,
                    "`Heroku Api Key And App Name Doesn't Match!`",
                    parse_mode="markdown",
                )
            if heroku_app:
                await func(client, message, heroku_app)

    return heroku_cli


def fetch_heroku_git_url(api_key, app_name):
    if not api_key:
        return None
    if not app_name:
        return None
    heroku = heroku3.from_key(api_key)
    try:
        heroku_applications = heroku.apps()
    except:
        return None
    heroku_app = None
    for app in heroku_applications:
        if app.name == app_name:
            heroku_app = app
            break
    if not heroku_app:
        return None
    return heroku_app.git_url.replace("https://", "https://api:" + api_key + "@")


HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)


async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    """run command in terminal"""
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )
