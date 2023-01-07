import discord
from discord.ext import commands


class ample(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.slash_command()  # Not passing in guild_ids creates a global slash command.
    #@discord.slash_command()
    async def hi(self, ctx: discord.ApplicationContext):
        await ctx.respond("Hi, this is a global slash command from a cog!")


def setup(bot):
    bot.add_cog(ample(bot))