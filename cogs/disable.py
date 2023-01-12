import discord
from discord.ext import commands

from modal.announce_modal import announce
class Disable(commands.Cog):
     def __init__(self, bot):
        self.bot = bot

    

     @commands.slash_command(name = "disable", description = "disable Anonymous message")
     async def disable(self, ctx: discord.ApplicationContext):

        #1063106187891069008

        enable_roleObj = discord.utils.get(ctx.guild.roles, id=1063101418090803200)

        if enable_roleObj in ctx.user.roles:
            
            user = await ctx.guild.fetch_member(ctx.author.id)
            await user.remove_roles(enable_roleObj)
            
            await ctx.respond("**Anonymous Message** `Disabled`", delete_after=5)
            
        else:

            await ctx.respond("**Anonymous Message** `Already Disabled`", delete_after=5)

def setup(bot):
    bot.add_cog(Disable(bot))
    