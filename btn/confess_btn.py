import discord
from modal.confess_modal import cfs
from modal.anonymsg import anonymsg

class ConfessBtn(discord.ui.View):
    def __init__(self, bot) -> None:
        super().__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(label="Confess", style=discord.ButtonStyle.grey, emoji="😷", custom_id="confess-btn", row=1)
    async def button_callback(self, button, interaction):
        
        #modal = cfs(title="confession")
        await interaction.response.send_modal(cfs(title="Incognito Confession"))


    @discord.ui.button(label="Anonymous Dm", style=discord.ButtonStyle.red, emoji="✍️", custom_id="anony-mous", row=1)
    async def anonymsg(self, button, interaction):

        await interaction.response.send_modal(anonymsg(title="Incognito message"))
