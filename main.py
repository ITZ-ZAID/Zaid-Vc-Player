import asyncio
from pytgcalls import idle
from Zaid.main import call_py, bot, BOT, Venom1

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    print("[INFO]: STARTING PYTGCALLSS CLIENT")
    await call_py.start()
    await idle()
    print("[INFO]: STOPPING BOT & USERBOT")
    await bot.stop()
if Venom1:
        try:
            await Venom1.start()
        except Exception as e:
            print(str(e))

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
BOT.run_until_disconnected()
