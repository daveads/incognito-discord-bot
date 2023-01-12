import discord
from discord.ext import commands

from modal.announce_modal import announce
class Enable(commands.Cog):
     def __init__(self, bot):
        self.bot = bot

    

     @commands.slash_command(name = "enable", description = "allows you to receive Anonymous message")
     async def enable(self, ctx: discord.ApplicationContext):

        roleObj = discord.utils.get(ctx.guild.roles, id=1063101418090803200)
        

        if roleObj in ctx.user.roles:
            await ctx.respond("**Anonymous Message** `Already Enabled`", delete_after=5)

        else:
            user = await ctx.guild.fetch_member(ctx.author.id)
            await user.add_roles(roleObj)
            await ctx.respond("**Anonymous Message** `Enable`", delete_after=5)

def setup(bot):
    bot.add_cog(Enable(bot))
    