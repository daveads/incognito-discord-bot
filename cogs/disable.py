import discord
from discord.ext import commands

class Disable(commands.Cog):
     def __init__(self, bot):
        self.bot = bot

    

     @commands.slash_command(name = "disable", description = "disable Anonymous message")
     async def disable(self, ctx: discord.ApplicationContext):

        #1063106187891069008

        disable_roleObj = discord.utils.get(ctx.guild.roles, id=1063101418090803200)

        if disable_roleObj in ctx.user.roles:

            await ctx.respond("**Anonymous Message** `Already Disabled`", delete_after=5)

        else:

            user = await ctx.guild.fetch_member(ctx.author.id)
            await user.add_roles(disable_roleObj)
            await ctx.respond("**Anonymous Message** `Disabled`", delete_after=5)
            

            
def setup(bot):
    bot.add_cog(Disable(bot))
    