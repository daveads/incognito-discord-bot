import discord
from discord.ext import commands

from modal.announce_modal import announce
class announcer(commands.Cog):
     def __init__(self, bot):
        self.bot = bot

    

     @commands.slash_command(name = "announce", description = "feature announcement")
     #@discord.slash_command()
     async def announce(self, ctx: discord.ApplicationContext):

        if ctx.author.id == 840152379122384896:
            modal = announce(title="Incognito Announcement")

            await ctx.send_modal(modal)
                  
        else:
            await ctx.respond("Only @daveads#6337 can use this commands")


def setup(bot):
    bot.add_cog(announcer(bot))
    