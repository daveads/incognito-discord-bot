import discord
from modal.confess_modal import cfs

class ConfessBtn(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="Confess", style=discord.ButtonStyle.grey, emoji="😷", custom_id="confess-btn", row=1)
    async def button_callback(self, button, interaction):
        
        #modal = cfs(title="confession")
        await interaction.response.send_modal(cfs(title="Incognito Confession"))


    @discord.ui.button(label="Anonymous Dm", style=discord.ButtonStyle.red, emoji="✍️", custom_id="anony-mous", row=1)
    async def anonymsg(self, button, interaction):

        await interaction.response.send_message("still work in progress")
