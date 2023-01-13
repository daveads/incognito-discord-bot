import discord

from core.config_parser import BotConfigs
botconfig = BotConfigs()

class AmpM(discord.ui.Modal):
     def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="User id", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="message", style=discord.InputTextStyle.long))

    
     async def callback(self, interaction: discord.Interaction):
        
        #announce_chn = 
        channel = discord.utils.get(interaction.guild.channels, id=interaction.channel.id)
        log_chn = discord.utils.get(interaction.guild.channels, id=botconfig.channel("incognito_logs"))
        
        try:
            
            user_id = self.children[0].value

            user = [int(x) for x in str(user_id)]

            if len(user) == 18:

                #user_obj = await self.bot.fetch_user(user_id)
                #print(int(user_id))
                
                user_msg = await interaction.guild.fetch_member(int(user_id))

                #PUBLIC MESSAGE
                embed_user = discord.Embed(title="Incognito bot `Anonymous Public Message`", description=f"{self.children[1].value}", color=0xFF5733)
                embed_user.set_footer(text=f"Sent by a User to {user_msg} ")
                await channel.send(user_msg.mention, embed=embed_user)
                

                #LOGS
                embed_log = discord.Embed(title=f"anonymous message", description=f"{self.children[1].value} \n\n**Sent By:** {interaction.user} <@{interaction.user.id}> \n\n**Sent To:** {user_msg} <@{user_msg.id}>" , color=discord.Colour(0x2f3136),)
                embed_log.set_footer(text="Powered by Incognito")
                await log_chn.send(embed=embed_log)

                await interaction.response.send_message("`Public Anonymous Message` **Sent!**", ephemeral=True, delete_after=5)

        except:
            await interaction.response.send_message("you need to input a user id", ephemeral=True, delete_after=5)
