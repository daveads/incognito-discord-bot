import discord
from discord.ext import commands

class announcer(commands.Cog):
     def __init__(self, bot):
        self.bot = bot

    

     @commands.slash_command(name = "announce", description = "feature announcement")
     #@discord.slash_command()
     async def announce(self, ctx: discord.ApplicationContext):

        if ctx.author.id == 840152379122384896:
            await ctx.respond("Hi, this is a global slash command from a cog!")

        else:
            await ctx.respond("Only @daveads#6337 can use this commands")


def setup(bot):
    bot.add_cog(announcer(bot))
    