import discord
from modal.confess_modal import cfs

class ConfessBtn(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="Click to confess", custom_id="confess-btn", style=discord.ButtonStyle.grey, emoji="✅")
    async def button_callback(self, button, interaction):

        #modal = cfs(title="confession")
        await interaction.response.send_modal(cfs(title="Incognito Confession"))