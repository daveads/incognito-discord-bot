import discord

class anonymsg(discord.ui.Modal):
     def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        print(args)
        print(kwargs)

        self.add_item(discord.ui.InputText(label="User id", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="Input Message", style=discord.InputTextStyle.long))



     async def callback(self, interaction: discord.Interaction):
        
        log_chn = discord.utils.get(interaction.guild.channels, id=1061274643467599922)
        annoymdm_chn = discord.utils.get(interaction.guild.channels, id=1062857811777822820)
        
        embed = discord.Embed(title="Modal Results")
        embed.add_field(name="Short Input", value=self.children[0].value)
        embed.add_field(name="Long Input", value=self.children[1].value)

        # user = guild.get_member_named("Example#1234")
        #c = interaction.guild.get_member_named("daveads#6337")
        #print("checking id", c.id)

        try:
            user_id = self.children[0].value
            await interaction.response.send_message("sent")
            
            user = [int(x) for x in str(user_id)]

            if len(user) == 18:

                #user_obj = await self.bot.fetch_user(user_id)
                print(int(user_id))
                
                user_msg = await interaction.guild.fetch_member(int(user_id))

                await user_msg.send(f"{self.children[1].value}")
                print(self.children[1].value)

                #LOGS
                embed_log = discord.Embed(title=f"anonymous message", description=f"{self.children[1].value} \n\n**Sent By:** {interaction.user} <@{interaction.user.id}> \n\n**Sent To:** {user_msg} <@{user_msg.id}>" , color=discord.Colour(0x2f3136),)
                embed_log.set_footer(text="Powered by Incognito™")
                await log_chn.send(embed=embed_log)

                #Notify User
                # role to stop a user from receving anonymous message





        except:
            await interaction.response.send_message("you need to input a user id")

        #await interaction.response.send_message(embeds=[embed])
