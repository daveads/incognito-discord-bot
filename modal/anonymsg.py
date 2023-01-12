import discord

from core.config_parser import BotConfigs

botconfig = BotConfigs()

class anonymsg(discord.ui.Modal):
     def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    
        self.add_item(discord.ui.InputText(label="User id", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="Input Message", style=discord.InputTextStyle.long))



     async def callback(self, interaction: discord.Interaction):
        
        log_chn = discord.utils.get(interaction.guild.channels, id=botconfig.channel("incognito_logs"))
        
        annoymdm_chn = discord.utils.get(interaction.guild.channels, id=botconfig.channel("anonymous_dm_alert"))
        disable_roleObj = discord.utils.get(interaction.guild.roles, id=botconfig.role("disable_anony"))
        
        # user = guild.get_member_named("Example#1234")
        #c = interaction.guild.get_member_named("daveads#6337")
        #print("checking id", c.id)

        try:
            user_id = self.children[0].value
            #await interaction.response.defer()

            user = [int(x) for x in str(user_id)]

            if len(user) == 18:

                #user_obj = await self.bot.fetch_user(user_id)
                #print(int(user_id))
                
                user_msg = await interaction.guild.fetch_member(int(user_id))

                if disable_roleObj in user_msg.roles:
                    
                    await interaction.response.send_message("*You can't send this user a Message* \n **User disabled** `anonymous message`", delete_after=5)

                
                else:

                    #receving user
                    embed_user = discord.Embed(title="Incognito bot `anonymous dm`", description=f"{self.children[1].value}", color=0xFF5733)
                    await user_msg.send(embed=embed_user)

                    #sender
                    await interaction.response.send_message("sent", delete_after=5)


                    #LOGS
                    embed_log = discord.Embed(title=f"anonymous message", description=f"{self.children[1].value} \n\n**Sent By:** {interaction.user} <@{interaction.user.id}> \n\n**Sent To:** {user_msg} <@{user_msg.id}>" , color=discord.Colour(0x2f3136),)
                    embed_log.set_footer(text="Powered by Incognito")
                    await log_chn.send(embed=embed_log)

                    #Notify User
                    # role to stop a user from receving anonymous message
                    await annoymdm_chn.send(user_msg.mention)
                    embed_anno = discord.Embed(title="Incognito bot", description=f"Check Your Dm, You just got an anonymous message", color=0xFF5733)
                    await annoymdm_chn.send(embed=embed_anno)
                    
                


        except:
            await interaction.response.send_message("you need to input a user id", delete_after=5)

        #await interaction.response.send_message(embeds=[embed])
