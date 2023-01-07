from discord.ext import commands
import discord

from discord.ext import bridge, commands
from btn.confess_btn import ConfessBtn

#bot_configs = BotConfigs()

#jezzzzz

class Incognito(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        description = '''Discord profile bot '''
        super().__init__(command_prefix=commands.when_mentioned_or('$'), intents=intents, description=description)
        

    async def on_ready(self):
        self.add_view(ConfessBtn())
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        #c = self.get_guild(bot_configs.guild_id())
        #print("guild**********", c)
        print('------')