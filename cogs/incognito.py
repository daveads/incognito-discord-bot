import discord
from discord.ext import commands

from btn.confess_btn import ConfessBtn

class incognito_start(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def set(self, ctx):
        await ctx.channel.purge(limit=1)


        if ctx.message.author.id == 884581563914936360 or ctx.message.author.id == 840152379122384896:
            await ctx.message.channel.purge(limit=10)
            embed = discord.Embed(
            title="Incognito",
            description="`To send an anonymous confession`, \n**use the 😷 button** \n\n `To send an Anonymous message to a user` \n**use the ✍️ button**",
            color=discord.Colour(0x2f3136)
        )
            await ctx.message.channel.send(embed=embed, view=ConfessBtn()) #delete_after=5



    @commands.slash_command()  # Not passing in guild_ids creates a global slash command.
    #@discord.slash_command()
    async def hi(self, ctx: discord.ApplicationContext):
        await ctx.respond("Hi, this is a global slash command from a cog!")


def setup(bot):
    bot.add_cog(incognito_start(bot))