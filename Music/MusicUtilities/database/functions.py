from typing import Dict, List, Union
from Music import db


restart_stagedb = db.restart_stage



async def start_restart_stage(chat_id: int, message_id: int):
    await restart_stagedb.update_one(
        {"something": "something"},
        {
            "$set": {
                "chat_id": chat_id,
                "message_id": message_id,
            }
        },
        upsert=True,
    )


async def clean_restart_stage() -> dict:
    data = await restart_stagedb.find_one({"something": "something"})
    if not data:
        return {}
    await restart_stagedb.delete_one({"something": "something"})
    return {"chat_id": data["chat_id"], "message_id": data["message_id"]}
