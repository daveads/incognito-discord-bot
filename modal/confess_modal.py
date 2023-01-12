import discord
from datetime import datetime
import sqlite3
from model import confession


from core.config_parser import BotConfigs
botconfig = BotConfigs()

#modal
class cfs(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs, timeout=None)
        self.add_item(discord.ui.InputText(label="Input confession", style=discord.InputTextStyle.long ))
        #self.counter = 0


    async def callback(self, interaction: discord.Interaction):

        #self.counter += 1
        #print(self.counter)

        #DB query for counter
        counter = 0
        con = sqlite3.connect("confess.db")
        cur = con.cursor()
        count = cur.execute("SELECT * FROM confession WHERE ROWID IN ( SELECT max( ROWID ) FROM confession );")
        count_data = ()

        for i in count:
            count_data = i

        counter = count_data[len(count_data)-1]


        #input into DATABASE
        date = datetime.utcnow().strftime("%d-%m-%Y %H:%M")
        author = str(interaction.user)
        author_id = interaction.user.id
        confessed = self.children[0].value

        #print(type(date))
        #print(type(author))
        #print(type(author_id))
        #print(type(confessed))
        #print(type(counter+1))
        #print(interaction.local)

        confession.confess_data(date,author,author_id,confessed,counter+1)


        #confessions
        embed = discord.Embed(title=f"Confession #{counter+1}" , #{self.counter}
        description=self.children[0].value,
        color=discord.Colour(0x2f3136),
        )
        embed.set_footer(text="All confessions are anonymous | Powered by Incognito")
        #channel = client.get_channel(991832397769363456)

        channel = discord.utils.get(interaction.guild.channels, id=botconfig.channel("confessions"))

        # confession log
        incognito_logs_embed = discord.Embed(title=f"Confession logs #{counter+1}" , #{self.counter}
        description=f"{self.children[0].value}\n\n**Confessed by:** {interaction.user} <@{interaction.user.id}>",
        color=discord.Colour(0x2f3136),
        )
        incognito_logs_embed.set_footer(text=f"date: {datetime.utcnow().strftime('%d-%m-%Y %H:%M')}")

        #confess_log_channel = client.get_channel(1010023764387438643)

        incognito_logs = discord.utils.get(interaction.guild.channels, id=botconfig.channel("incognito_logs"))

        await channel.send(embeds=[embed])
        await incognito_logs.send(embeds=[incognito_logs_embed])
        await interaction.response.send_message("**Confession sent!**", delete_after=5)