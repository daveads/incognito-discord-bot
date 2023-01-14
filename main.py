import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')


from core.bot import Incognito
bot = Incognito()

async def load():
    for f in os.listdir("cogs"):
        if f.endswith(".py"):
            bot.load_extension(f'cogs.{f[:-3]}')



async def run():
    await load()

asyncio.run(run())
bot.run(token)