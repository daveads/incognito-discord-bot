import discord
from discord.ext import commands

from modal.amp_modal import AmpM
class Amp(commands.Cog):
     def __init__(self, bot):
        self.bot = bot

    

     @commands.slash_command(name = "anonymous_public_message", description = "send a public anonymous message to a user", )
     async def apm(self, ctx: discord.ApplicationContext):
        #await ctx.respond("private message received", ephemeral=True)
        
        await ctx.send_modal(AmpM(title="public anonymous message"))

        #await ctx.send("hello")

        #print(ctx.channel.id)

        #await ctx.followup.send("hello", ephemeral=False)
            
def setup(bot):
    bot.add_cog(Amp(bot))
    