from typing import Dict, Union, List
from Music import db

playlistdb = db.playlist


async def get_playlist_count() -> dict:
    chats = playlistdb.find({"chat_id": {"$lt": 0}})
    if not chats:
        return {}
    chats_count = 0
    notes_count = 0
    for chat in await chats.to_list(length=1000000000):
        notes_name = await get_note_names(chat["chat_id"])
        notes_count += len(notes_name)
        chats_count += 1
    return {"chats_count": chats_count, "notes_count": notes_count}


async def _get_playlists(chat_id: int) -> Dict[str, int]:
    _notes = await playlistdb.find_one({"chat_id": chat_id})
    if not _notes:
        return {}
    return _notes["notes"]


async def get_note_names(chat_id: int) -> List[str]:
    _notes = []
    for note in await _get_playlists(chat_id):
        _notes.append(note)
    return _notes


async def get_playlist(chat_id: int, name: str) -> Union[bool, dict]:
    name = name
    _notes = await _get_playlists(chat_id)
    if name in _notes:
        return _notes[name]
    else:
        return False


async def save_playlist(chat_id: int, name: str, note: dict):
    name = name
    _notes = await _get_playlists(chat_id)
    _notes[name] = note

    await playlistdb.update_one(
        {"chat_id": chat_id}, {"$set": {"notes": _notes}}, upsert=True
    )


async def delete_playlist(chat_id: int, name: str) -> bool:
    notesd = await _get_playlists(chat_id)
    name = name
    if name in notesd:
        del notesd[name]
        await playlistdb.update_one(
            {"chat_id": chat_id}, {"$set": {"notes": notesd}}, upsert=True
        )
        return True
    return False
