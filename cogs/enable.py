import discord
from discord.ext import commands
from discord import guild_only

class Enable(commands.Cog):
     def __init__(self, bot):
        self.bot = bot

    

     @commands.slash_command(name = "enable", description = "allows you to receive Anonymous message")
     @guild_only()
     async def enable(self, ctx: discord.ApplicationContext):

        disable_roleObj = discord.utils.get(ctx.guild.roles, id=1063101418090803200)
        

        if disable_roleObj in ctx.user.roles:
            user = await ctx.guild.fetch_member(ctx.author.id)
            await user.remove_roles(disable_roleObj)
            await ctx.respond("**Anonymous Message** `Enable`", delete_after=5)

            
        else:
            await ctx.respond("**Anonymous Message** `Already Enabled`", delete_after=5)
            

def setup(bot):
    bot.add_cog(Enable(bot))
    