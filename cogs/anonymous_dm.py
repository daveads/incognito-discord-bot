import discord
from discord.ext import commands

from modal.anonymsg import anonymsg

class Adm(commands.Cog):
     def __init__(self, bot):
        self.bot = bot

    

     @commands.slash_command(name = "anonymous_dm", description = "make the bot send a message to a user", )
     async def adm(self, ctx: discord.ApplicationContext):
   
        await ctx.send_modal(anonymsg(title="Incognito message"))


def setup(bot):
    bot.add_cog(Adm(bot))
    