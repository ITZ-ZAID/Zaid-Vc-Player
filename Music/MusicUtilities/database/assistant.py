from typing import Dict, Union, List
from Music import db

assisdb = db.assis

async def get_assistant_count() -> dict:
    chats = assisdb.find({"chat_id": {"$lt": 0}})
    if not chats:
        return {}
    chats_count = 0
    notes_count = 0
    for chat in await chats.to_list(length=1000000000):
        notes_name = await get_as_names(chat["chat_id"])
        notes_count += len(notes_name)
        chats_count += 1
    return {"chats_count": chats_count, "notes_count": notes_count}

async def get_as_names(chat_id: int) -> List[str]:
    _notes = []
    for note in await _get_assistant(chat_id):
        _notes.append(note)
    return _notes

async def _get_assistant(chat_id: int) -> Dict[str, int]:
    _notes = await assisdb.find_one({"chat_id": chat_id})
    if not _notes:
        return {}
    return _notes["notes"]

async def get_assistant(chat_id: int, name: str) -> Union[bool, dict]:
    name = name.lower().strip()
    _notes = await _get_assistant(chat_id)
    if name in _notes:
        return _notes[name]
    else:
        return False

async def save_assistant(chat_id: int, name: str, note: dict):
    name = name.lower().strip()
    _notes = await _get_assistant(chat_id)
    _notes[name] = note
    await assisdb.update_one(
        {"chat_id": chat_id}, {"$set": {"notes": _notes}}, upsert=True
    )
