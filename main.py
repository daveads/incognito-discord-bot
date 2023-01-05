import discord
import os
import json
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')
f = open('src/config.json')
data = json.load(f)


client = discord.Bot(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user}:Bot Logged In')

  
client.run(token)
