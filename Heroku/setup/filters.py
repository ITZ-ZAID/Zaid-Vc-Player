from typing import List, Union
from pyrogram import filters

from Heroku.config import CMD_MUSIC, SUDO_USERS


other_filters = filters.group & ~filters.edited & ~filters.via_bot & ~filters.forwarded

other_filters2 = (
    filters.private & ~filters.edited & ~filters.via_bot & ~filters.forwarded
)


def command(commands: Union[str, List[str]]):
    return filters.command(commands, CMD_MUSIC)
