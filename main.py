import asyncio
import discord
import os
import json
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('TOKEN')
#f = open('src/config.json')
#data = json.load(f)


from core.bot import Incognito

bot = Incognito()


async def load():
    for f in os.listdir("cogs"):
        if f.endswith(".py"):
            bot.load_extension(f'cogs.{f[:-3]}')


@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

@bot.command()
async def see(ctx: commands.Context):
    await ctx.reply("see")


async def main():
    await load()
    await bot.start(token)

asyncio.run(main())