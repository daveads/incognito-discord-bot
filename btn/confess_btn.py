import discord
from modal.confess_modal import cfs

class ConfessBtn(discord.ui.View):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="Click to confess", style=discord.ButtonStyle.grey, emoji="✅")
    async def button_callback(self, button, interaction):

        modal = cfs(title="confession")
        await interaction.response.send_modal(cfs(title="Affinity confession"))