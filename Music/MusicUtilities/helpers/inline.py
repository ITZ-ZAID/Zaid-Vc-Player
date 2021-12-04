from Music.config import UPDATES_CHANNEL, ZAID_SUPPORT
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)

def play_markup(videoid, user_id):
    buttons= [
            [
                InlineKeyboardButton(text="▶️", callback_data=f'resumevc2'),
                InlineKeyboardButton(text="⏸️", callback_data=f'pausevc2'),
                InlineKeyboardButton(text="⏭️", callback_data=f'skipvc2'),
                InlineKeyboardButton(text="⏹️", callback_data=f'stopvc2')
            ],
            [
                InlineKeyboardButton(text="🔎 ɢᴇᴛ ʟʏʀɪᴄꜱ", callback_data=f'lyrics {videoid}|{user_id}'),
                InlineKeyboardButton(text="🖱 ᴍᴇɴᴜ", callback_data=f'other {videoid}|{user_id}'),
            ],
            [
                InlineKeyboardButton(text=f"✨ ɢʀᴏᴜᴘ", url=f"https://t.me/{ZAID_SUPPORT}"),
                InlineKeyboardButton(text=f"📣 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ],
            [      
                InlineKeyboardButton(text="🗑 ᴄʟᴏsᴇ", callback_data=f'close2')
            ],
        ]
    return buttons 


def others_markup(videoid, user_id):
    buttons= [
            [
                InlineKeyboardButton(text="✨ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                InlineKeyboardButton(text="➕ Group Playlist", callback_data=f'group_playlist {videoid}|{user_id}')
            ],
            [
                InlineKeyboardButton(text="Get Audio", callback_data=f'gets audio|{videoid}|{user_id}'),
                InlineKeyboardButton(text="Get Video", callback_data=f'gets video|{videoid}|{user_id}')
            ],
            [
                InlineKeyboardButton(text="🔙", callback_data=f'goback {videoid}|{user_id}'),
                InlineKeyboardButton(text="🗑 Close", callback_data=f'close2')
            ],
        ]
    return buttons 





play_keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "▶️", callback_data="resumevc"
                    ),
                    InlineKeyboardButton(
                        "⏸️", callback_data="pausevc"
                    ),
                    InlineKeyboardButton(
                        "⏭️", callback_data="skipvc"
                    ),
                    InlineKeyboardButton(
                        "⏹️", callback_data="stopvc"
                    )
                ],
                [
                    InlineKeyboardButton(text=f"✨ ɢʀᴏᴜᴘ", url=f"https://t.me/{ZAID_SUPPORT}"),
                    InlineKeyboardButton(text=f"📣 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ],
                [
                    InlineKeyboardButton(
                        "🗑", callback_data="close"
                    )
                ]    
            ]
        )

def audio_markup(videoid, user_id):
    buttons= [
            [
                InlineKeyboardButton(text="▶️", callback_data=f'resumevc2'),
                InlineKeyboardButton(text="⏸️", callback_data=f'pausevc2'),
                InlineKeyboardButton(text="⏭️", callback_data=f'skipvc2'),
                InlineKeyboardButton(text="⏹️", callback_data=f'stopvc2')
            ],
            [
                InlineKeyboardButton(text=f"✨ ɢʀᴏᴜᴘ", url=f"https://t.me/{ZAID_SUPPORT}"),
                InlineKeyboardButton(text=f"📣 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ],
            [
                InlineKeyboardButton(text="🗑 Close", callback_data="close2")              
            ],
        ]
    return buttons 


def single_markup(ID, duration, user_id, query):
    buttons= [
            [
                InlineKeyboardButton(text="▶️ Start Playing", callback_data=f'Music {ID}|{duration}|{user_id}'),
                InlineKeyboardButton(text="🔎 Search More", callback_data=f'popat 1|{query}|{user_id}')
            ],
            [
                InlineKeyboardButton(text=f"✨ ɢʀᴏᴜᴘ", url=f"https://t.me/{ZAID_SUPPORT}"),
                InlineKeyboardButton(text=f"📣 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ],
            [
                InlineKeyboardButton(text="🗑 ᴄʟᴏsᴇ", callback_data=f"ppcl2 smex|{user_id}")
            ],
       ]  
    return buttons



def search_markup(ID1, ID2, ID3, ID4, ID5, duration1, duration2, duration3, duration4, duration5, user_id, query):
    buttons= [
            [
                InlineKeyboardButton(text="1️⃣", callback_data=f'Music {ID1}|{duration1}|{user_id}'),
                InlineKeyboardButton(text="2️⃣", callback_data=f'Music {ID2}|{duration2}|{user_id}'),
                InlineKeyboardButton(text="3️⃣", callback_data=f'Music {ID3}|{duration3}|{user_id}')
            ],
            [ 
                InlineKeyboardButton(text="4️⃣", callback_data=f'Music {ID4}|{duration4}|{user_id}'),
                InlineKeyboardButton(text="5️⃣", callback_data=f'Music {ID5}|{duration5}|{user_id}')
            ],
            [ 
                InlineKeyboardButton(text="🗑 ᴄʟᴏsᴇ", callback_data=f"ppcl2 smex|{user_id}") ,             
            ],
        ]
    return buttons   

def search_markup2(ID6, ID7, ID8, ID9, ID10, duration6, duration7, duration8, duration9, duration10 ,user_id, query):
    buttons= [
            [
                InlineKeyboardButton(text="6️⃣", callback_data=f'Music {ID6}|{duration6}|{user_id}'),
                InlineKeyboardButton(text="7️⃣", callback_data=f'Music {ID7}|{duration7}|{user_id}'),
                InlineKeyboardButton(text="8️⃣", callback_data=f'Music {ID8}|{duration8}|{user_id}')
            ],
            [ 
                InlineKeyboardButton(text="9️⃣", callback_data=f'Music {ID9}|{duration9}|{user_id}'),
                InlineKeyboardButton(text="🔟", callback_data=f'Music {ID10}|{duration10}|{user_id}')
            ],
            [ 
                
                InlineKeyboardButton(text="🗑 Close", callback_data=f"ppcl2 smex|{user_id}") ,             
            ],
        ]
    return buttons 


def personal_markup(link):
    buttons= [
            [
                InlineKeyboardButton(text="Watch on Youtube", url=f'{link}')
            ],
            [
                InlineKeyboardButton(text=f"✨ ɢʀᴏᴜᴘ", url=f"https://t.me/{ZAID_SUPPORT}"),
                InlineKeyboardButton(text=f"📣 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ],
            [ 
                InlineKeyboardButton(text="🗑 ᴄʟᴏsᴇ", callback_data=f'close2')
            ],
        ]
    return buttons   
  
start_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        "📜 Commands", url=""
                    )
                ],
                [
                    InlineKeyboardButton(text=f"✨ ɢʀᴏᴜᴘ", url=f"https://t.me/{ZAID_SUPPORT}"),
                    InlineKeyboardButton(text=f"📣 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ],
                [
                    InlineKeyboardButton(
                        "🗑 ᴄʟᴏsᴇ", callback_data="close2"
                    )
                ]    
            ]
        )
    
confirm_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        "Yes", callback_data="cbdel"
                    ),
                    InlineKeyboardButton(
                        "No", callback_data="close2"
                    )
                ],
                [
                    InlineKeyboardButton(text=f"✨ ɢʀᴏᴜᴘ", url=f"https://t.me/{ZAID_SUPPORT}"),
                    InlineKeyboardButton(text=f"📣 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ],    
            ]
        )

confirm_group_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        "Yes", callback_data="cbgroupdel"
                    ),
                    InlineKeyboardButton(
                        "No", callback_data="close2"
                    )
                ],
                [
                    InlineKeyboardButton(text=f"✨ ɢʀᴏᴜᴘ", url=f"https://t.me/{ZAID_SUPPORT}"),
                    InlineKeyboardButton(text=f"📣 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ],    
            ]
        )

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        "🗑 Close", callback_data="close2"
                    )
                ]    
            ]
        )

play_list_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        "Personal Playlist", callback_data="P_list"
                    ),
                    InlineKeyboardButton(
                        "Group's Playlist", callback_data="G_list"
                    )
                ],
                [
                    InlineKeyboardButton(text=f"✨ ɢʀᴏᴜᴘ", url=f"https://t.me/{ZAID_SUPPORT}"),
                    InlineKeyboardButton(text=f"📣 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                ],
                [
                    InlineKeyboardButton(
                        "🗑 ᴄʟᴏsᴇ", callback_data="close2"
                    )
                ]
            ]
        )

def playlist_markup(user_name, user_id):
    buttons= [
            [
                InlineKeyboardButton(text=f"Group's Playlist", callback_data=f'play_playlist {user_id}|group'),
                InlineKeyboardButton(text=f"{user_name[:8]}'s Playlist", callback_data=f'play_playlist {user_id}|personal'),
            ],
            [
                InlineKeyboardButton(text=f"✨ ɢʀᴏᴜᴘ", url=f"https://t.me/{ZAID_SUPPORT}"),
                InlineKeyboardButton(text=f"📣 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ],
            [
                InlineKeyboardButton(text="🗑 Close", callback_data="close2")              
            ],
        ]
    return buttons
